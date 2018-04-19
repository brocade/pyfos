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

:mod:`port_name_set` - PyFOS util for specific port op use case.
***********************************************************************************
The :mod:`port_name_set` provides for specific port op use case.

This module is a stand-alone script that can be used to set a port name.

* Inputs:
    * -L=<login>: Login ID. If not provided, an interactive
        prompt will request one.
    * -P=<password>: Password. If not provided, an interactive
        prompt will request one.
    * -i=<IP address>: IP address.
    * --name=<port name>: <slot>/<port> name of the port.
    * --username=<user name>: The string name to be assigned to switch.
    * -f=<VFID>: VFID or -1 if VF is disabled. If unspecified,
        a VFID of 128 is assumed.

* Outputs:
    * Python dictionary content with RESTCONF response data.

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
    print("    --username=USERNAME          user friendly name")
    print("")


def main(argv):
    valid_options = ["name", "username"]
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

    if "username" not in inputs:
        pyfos_auth.logout(session)
        usage()
        sys.exit()
    username = inputs["username"]

    port = pyfos_switchfcport.fibrechannel()
    port.set_name(name)
    port.set_user_friendly_name(username)
    result = port.patch(session)
    pyfos_util.response_print(result)

    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
