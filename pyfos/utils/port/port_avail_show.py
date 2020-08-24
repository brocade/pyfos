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

:mod:`port_avail_show` - PyFOS util for specific port op use case.
***********************************************************************************
The :mod:`port_avail_show` provides for specific port op use case.

This module is a stand-alone script that can be used to display available
ports.

* Inputs:
    * -L=<login>: Login ID. If not provided, an interactive
        prompt will request one.
    * -P=<password>: Password. If not provided, an interactive
        prompt will request one.
    * -i=<IP address>: IP address.
    * -u=<user name>: The string name to be assigned to switch.
    * -f=<VFID>: VFID or -1 if VF is disabled. If unspecified,
        a VFID of 128 is assumed.

* Outputs:
    * List of ports that are available.

"""

import sys
from pyfos import pyfos_auth
import pyfos.pyfos_brocade_interface as pyfos_switchfcport
from pyfos import pyfos_util
from pyfos.utils import brcd_util


def usage():
    print("  Script specific options:")
    print("")
    print("    --name=NAME                  name of port. [OPTIONAL]")
    print("")


def id_avail_port(port, available_ports):
    neighbor_list = port.peek_neighbor()
    if len(neighbor_list) == 0:
        name = port.peek_name()
        port_type = port.peek_port_type()
        available_ports.append(
            {'name': name,
             'port-type': pyfos_switchfcport.port_type_to_str(int(port_type))})


def main(argv):
    valid_options = ["name"]
    inputs = brcd_util.generic_input(argv, usage, valid_options)

    session = brcd_util.getsession(inputs)

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
    else:
        if "name" in inputs:
            print("failed to get information on", inputs["name"])
        else:
            print("failed to get information on ports")

    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
