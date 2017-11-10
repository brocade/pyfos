#!/usr/bin/env python3

# Copyright 2017 Brocade Communications Systems, Inc.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may also obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""

:mod:`portdportrun` - PyFOS util for specific port op use case.
***********************************************************************************
The :mod:`portdportrun` provides for specific port op use case.

This module is a standalone script that can be used to run D-Port
on a given port

* inputs:
    * -L=<login>: Login ID. If not provided, interactive
        prompt will request one.
    * -P=<password>: Password. If not provided, interactive
        prompt will request one.
    * -i=<IP address>: IP address
    * -n=<port name>: <slot>/<port> name of the port
    * -f=<VFID>: VFID or -1 if VF is disabled. If unspecified,
        VFID of 128 is assumed.

* outputs:
    * Python dictionary content with RESTCONF response data

"""

import pyfos.pyfos_auth as pyfos_auth
import pyfos.pyfos_switchfcport as pyfos_switchfcport
import pyfos.pyfos_util as pyfos_util
import sys
import time
import pyfos.utils.brcd_util as brcd_util

isHttps = "0"


def usage():
    print("usage:")
    print('portdportrun.py -i <ipaddr> -n <name>')


def wait_diag_completion(session, name):
    count = 0
    print("wait for the test to complete")

    time.sleep(10)
    diag_info = pyfos_switchfcport.fibrechannel_diagnostics.get(session, name)
    # pyfos_util.response_print(diag_info)
    diag_state = diag_info.peek_state()
    while ("IN PROGRESS" in diag_state or
           "NOT STARTED" in diag_state or
           "RESPONDER" in diag_state or
           "STOPPED" in diag_state):
        print(".")
        count += 1
        time.sleep(10)
        diag_info = pyfos_switchfcport.fibrechannel_diagnostics.get(
                session, name)
        if count > 12:
            break

    diag_info = pyfos_switchfcport.fibrechannel_diagnostics.get(session, name)
    time.sleep(2)
    pyfos_util.response_print(diag_info)
    if diag_info.peek_state() == "PASSED":
        return 0
    else:
        return -1


def main(argv):
    inputs = brcd_util.generic_input(argv, usage)

    session = pyfos_auth.login(inputs["login"], inputs["password"],
                               inputs["ipaddr"], isHttps)
    if pyfos_auth.is_failed_login(session):
        print("login failed because",
              session.get(pyfos_auth.CREDENTIAL_KEY)
              [pyfos_auth.LOGIN_ERROR_KEY])
        usage()
        sys.exit()

    brcd_util.exit_register(session)

    vfid = None
    if 'vfid' in inputs:
        vfid = inputs['vfid']

    if vfid is not None:
        pyfos_auth.vfid_set(session, vfid)

    if 'name' not in inputs:
        pyfos_auth.logout(session)
        usage()
        sys.exit()
    name = inputs["name"]

    # PUT - Disable one port
    print("disable " + name)
    port = pyfos_switchfcport.fibrechannel(
            {"name": name,
             "enabled-state": pyfos_switchfcport.ENABLED_STATE_TYPE.OFFLINE})
    result = port.patch(session)
    pyfos_util.response_print(result)

    # PUT - D-Port mode set
    print("disable dport " + name)
    port = pyfos_switchfcport.fibrechannel({"name": name, "d-port-enable": 0})
    result = port.patch(session)
    pyfos_util.response_print(result)

    # PUT - D-Port mode set
    port = pyfos_switchfcport.fibrechannel({"name": name, "d-port-enable": 1})
    result = port.patch(session)
    pyfos_util.response_print(result)

    # PUT - Re-enable the port
    port = pyfos_switchfcport.fibrechannel(
            {"name": name,
             "enabled-state": pyfos_switchfcport.ENABLED_STATE_TYPE.ONLINE})
    result = port.patch(session)
    pyfos_util.response_print(result)

    # GET state of the test. As default mode is auto,
    # it will start the test once port is enabled
    wait_diag_completion(session, name)

    # TEST#1
    # ======
    # GET fibrechannel - one port - Check the values
    print("geting port state " + name)
    port = pyfos_switchfcport.fibrechannel.get(session, name)
    pyfos_util.response_print(port)

    # GET Diagnostics info for one port
    print("geting dport test status for all")
    diag_info = pyfos_switchfcport.fibrechannel_diagnostics.get(session, name)
    pyfos_util.response_print(diag_info)

    # TEST#2
    # ======
    # SET new attributes and Restart the diagnostics test
    # parameters = {"frame-count": 4, "frame-size": 2112,
    # "fec": "enable", "cr": "enable"}
    # pyfos_auth.debug_set(session, 1)
    # parameters = {"pattern": "JTSPAT"}
    # parameters = {"payload": "305402420"}
    print("restart dport with new parameters " + name)
    diag_info = pyfos_switchfcport.fibrechannel_diagnostics(
        {"name": name, "payload-pattern": {"payload": "305402420"}})
    result = diag_info.patch(session)
    pyfos_util.response_print(result)

    diag_info = pyfos_switchfcport.fibrechannel_diagnostics(
        {
            "name": name,
            "diagnostic-control": pyfos_switchfcport.DIAG_RESTART
        })
    result = diag_info.patch(session)
    pyfos_util.response_print(result)

    # Wait for few secs to complete tests.
    wait_diag_completion(session, name)

    # GET Diagnostics info for one port
    print("dport status with new parameters " + name)
    diag_info = pyfos_switchfcport.fibrechannel_diagnostics.get(session, name)
    pyfos_util.response_print(diag_info)

    # TEST#3
    # ======
    # SET new attributes and start the diagnostics test in the same call
    # Wait for few secs to port to settle down before starting the tests
    wait_diag_completion(session, name)
    print("start dport with new parameters " + name)
    diag_info = pyfos_switchfcport.fibrechannel_diagnostics()
    diag_info.set_name(name)
    diag_info.set_payload_pattern_payload("305402420")
    diag_info.set_diagnostic_control(pyfos_switchfcport.DIAG_START)
    result = diag_info.patch(session)
    pyfos_util.response_print(result)

    # Wait for few secs to complete tests.
    wait_diag_completion(session, name)

    # GET Diagnostics info for one port
    print("dport status with new parameters " + name)
    diag_info = pyfos_switchfcport.fibrechannel_diagnostics.get(session, name)
    pyfos_util.response_print(diag_info)

    # PUT - Disable one port
    print("disable " + name)
    port = pyfos_switchfcport.fibrechannel(
            {"name": name,
             "enabled-state": pyfos_switchfcport.ENABLED_STATE_TYPE.OFFLINE})
    result = port.patch(session)
    pyfos_util.response_print(result)

    # PUT - D-Port mode set
    print("disable dport " + name)
    port = pyfos_switchfcport.fibrechannel({"name": name, "d-port-enable": 0})
    result = port.patch(session)
    pyfos_util.response_print(result)

    # PUT - Re-enable the port
    port = pyfos_switchfcport.fibrechannel(
            {"name": name,
             "enabled-state": pyfos_switchfcport.ENABLED_STATE_TYPE.ONLINE})
    result = port.patch(session)
    pyfos_util.response_print(result)

    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
