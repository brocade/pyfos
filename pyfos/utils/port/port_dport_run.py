#!/usr/bin/env python3

# Copyright © 2018 Broadcom. All Rights Reserved. The term “Broadcom” refers to
# Broadcom Inc. and/or its subsidiaries.
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

:mod:`port_dport_run` - PyFOS util for a specific port op use case.
***********************************************************************************
The :mod:`port_dport_run` util provides for a specific port op use case.

This module is a stand-alone script that can be used to run a D_Port
on a given port.

* Input:
    * -L=<login>: The login ID. If not provided, an interactive
        prompt will request one.
    * -P=<password>: The password. If not provided, an interactive
        prompt will request one.
    * -i=<IP address>: The IP address.
    * -n=<port name>: The <slot>/<port> name of the port.
    * -f=<VFID>: The VFID or -1 if VF is disabled. If unspecified,
        a VFID of 128 is assumed.

* Output:
    * Python dictionary content with RESTCONF response data.

"""

import sys
import time
from pyfos import pyfos_auth
import pyfos.pyfos_brocade_interface as pyfos_switchfcport
import pyfos.pyfos_brocade_fibrechannel_diagnostics as pyfos_diag
from pyfos import pyfos_util
from pyfos.utils import brcd_util


def usage():
    print("  Script specific options:")
    print("")
    print("    --name=NAME                  name of port")
    print("")


def wait_diag_completion(session, name):
    count = 0
    print("wait for the test to complete")

    time.sleep(5)
    diag_info = pyfos_diag.fibrechannel_diagnostics.get(session, name)
    if pyfos_util.is_failed_resp(diag_info):
        print("Cannot validate test result")
        pyfos_util.response_print(diag_info)
        return

    diag_state = diag_info.peek_state()
    if diag_info.peek_state() == "PASSED":
        print("D-Port test completed")
        pyfos_util.response_print(diag_info)
        return

    while ("IN PROGRESS" in diag_state or
           "NOT STARTED" in diag_state or
           "RESPONDER" in diag_state or
           "STOPPED" in diag_state):
        print(".")
        count += 1
        time.sleep(5)
        diag_info = pyfos_diag.fibrechannel_diagnostics.get(
                session, name)

        if diag_info.peek_state() == "PASSED":
            print("D-Port test completed")
            pyfos_util.response_print(diag_info)
            return
        elif count > 12:
            break

    print("D-Port test failed")
    pyfos_util.response_print(diag_info)


def main(argv):
    valid_options = ["name"]
    inputs = brcd_util.generic_input(argv, usage, valid_options)

    session = pyfos_auth.login(inputs["login"], inputs["password"],
                               inputs["ipaddr"], inputs["secured"],
                               verbose=inputs["verbose"])
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
    if pyfos_util.is_failed_resp(result):
        print("Failed to disable port", name)
        pyfos_auth.logout(session)
        pyfos_util.response_print(result)
        usage()
        sys.exit()

    pyfos_util.response_print(result)

    # PUT - D-Port mode set
    print("disable dport " + name)
    port = pyfos_switchfcport.fibrechannel({"name": name, "d-port-enable": 0})
    result = port.patch(session)
    pyfos_util.response_print(result)

    # PUT - D-Port mode set
    print("enable dport " + name)
    port = pyfos_switchfcport.fibrechannel({"name": name, "d-port-enable": 1})
    result = port.patch(session)
    pyfos_util.response_print(result)

    # PUT - Re-enable the port
    print("enable " + name)
    port = pyfos_switchfcport.fibrechannel(
            {"name": name,
             "enabled-state": pyfos_switchfcport.ENABLED_STATE_TYPE.ONLINE})
    result = port.patch(session)
    pyfos_util.response_print(result)

    # GET state of the test. As default mode is auto,
    # it will start the test once port is enabled
    print("auto started dport testing")
    wait_diag_completion(session, name)

    diag_info = pyfos_diag.fibrechannel_diagnostics(
        {"name": name, "payload-pattern": {"payload": "0x30540242"}})
    print("SET new attributes and Restart the diagnostics test")
    result = diag_info.patch(session)
    pyfos_util.response_print(result)

    diag_info = pyfos_diag.fibrechannel_diagnostics(
        {
            "name": name,
            "diagnostic-control": pyfos_diag.DIAG_RESTART
        })
    print("restart diag")
    result = diag_info.patch(session)
    pyfos_util.response_print(result)

    # Wait for few secs to complete tests.
    print("restart dport with new parameters " + name)
    wait_diag_completion(session, name)

    print("SET new attributes and start the diagnostics test in the same call")
    diag_info = pyfos_diag.fibrechannel_diagnostics()
    diag_info.set_name(name)
    diag_info.set_payload_pattern_payload("0x02423054")
    diag_info.set_diagnostic_control(pyfos_diag.DIAG_START)
    result = diag_info.patch(session)
    pyfos_util.response_print(result)

    # Wait for few secs to complete tests.
    print("start dport with new parameters " + name)
    wait_diag_completion(session, name)

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
    print("enable " + name)
    port = pyfos_switchfcport.fibrechannel(
            {"name": name,
             "enabled-state": pyfos_switchfcport.ENABLED_STATE_TYPE.ONLINE})
    result = port.patch(session)
    pyfos_util.response_print(result)

    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
