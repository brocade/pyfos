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

:mod:`portavaileshow` - PyFOS util for specific port op use case.
***********************************************************************************
The :mod:`portavaileshow` provides for specific port op use case.

This module is a standalone script that can be used to display available
ports.

* inputs:
    * -L=<login>: Login ID. If not provided, interactive
        prompt will request one.
    * -P=<password>: Password. If not provided, interactive
        prompt will request one.
    * -i=<IP address>: IP address
    * -u=<user name>: string name to be assigned to switch
    * -f=<VFID>: VFID or -1 if VF is disabled. If unspecified,
        VFID of 128 is assumed.

* outputs:
    * List of ports that are available

"""

import pyfos.pyfos_auth as pyfos_auth
import pyfos.pyfos_switchfcport as pyfos_switchfcport
import pyfos.pyfos_util as pyfos_util
import sys
import pyfos.utils.brcd_util as brcd_util

isHttps = "0"


def usage():
    print("usage:")
    print('portavailshow.py -i <ipaddr> -n <name>')


def id_avail_port(port, available_ports):
    neighbor_list = port.peek_neighbor()
    if len(neighbor_list) == 0:
        name = port.peek_name()
        port_type = port.peek_port_type()
        available_ports.append(
            {'name': name,
             'port-type': pyfos_switchfcport.port_type_to_str(int(port_type))})


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

    if "name" in inputs:
        name = inputs["name"]
        result = pyfos_switchfcport.fibrechannel.get(session, name)
    else:
        result = pyfos_switchfcport.fibrechannel.get(session)

    if not pyfos_util.is_failed_resp(result):
        available_ports = []
        if isinstance(result, list):
            for port in result:
                id_avail_port(port, available_ports)
        else:
            id_avail_port(result, available_ports)

    pyfos_util.response_print(available_ports)

    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
