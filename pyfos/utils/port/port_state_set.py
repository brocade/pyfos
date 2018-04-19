#!/usr/bin/env python3

# Copyright 2018 Brocade Communications Systems LLC.  All rights reserved.
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

:mod:`port_state_set` - PyFOS util for specific port op use case.
***********************************************************************************
The :mod:`port_state_set` provides for specific port op use case.

This module is a standalone script that can be used to enable or disable
a port

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
import pyfos.pyfos_brocade_fibrechannel as pyfos_switchfcport
import pyfos.pyfos_util as pyfos_util
import sys
import pyfos.utils.brcd_util as brcd_util


def usage():
    print("  Script specific options:")
    print("")
    print("    --name=NAME                  name of port")
    print("    --enable                     to enable")
    print("    --disable                    to disable")
    print("")


def main(argv):
    valid_options = ["name", "enable", "disable"]
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

    if "name" not in inputs:
        pyfos_auth.logout(session)
        usage()
        sys.exit()
    name = inputs["name"]

    if "enable" not in inputs and "disable" not in inputs:
        pyfos_auth.logout(session)
        usage()
        sys.exit()

    if "enable" in inputs:
        enabled = 1
    if "disable" in inputs:
        enabled = 0

    port = pyfos_switchfcport.fibrechannel()
    port.set_name(name)
    if enabled:
        port.set_enabled_state(pyfos_switchfcport.ENABLED_STATE_TYPE.ONLINE)
    else:
        port.set_enabled_state(pyfos_switchfcport.ENABLED_STATE_TYPE.OFFLINE)
    result = port.patch(session)
    pyfos_util.response_print(result)

    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
