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

:mod:`extension_circuit_show` - PyFOS util for displaying a circuit object.
***********************************************************************************
The :mod:`extension_circuit_show` util displays a circuit.

This module is a stand-alone script that can be used to the show an extension
circuit.

extension_circuit_show.py: Usage

* Infrastructure Options:
    * -i,--ipaddr=IPADDR: The IP address of the FOS switch.
    * -L,--login=LOGIN: The login name.
    * -P,--password=PASSWORD: The password.
    * -f,--vfid=VFID: The VFID to which the request is directed.
    * -s,--secured=MODE: The HTTPS mode "self" or "CA" [Optional].
    * -v,--verbose: Verbose mode [Optional].

* Util Script Options:
    * -n,--name=NAME: Sets the name or slot/port of the circuit.
    * -c,--circuit-id=CIRCUIT-ID: Sets the ID of the circuit.
    * -S,--local-ip=LOCAL-IP: Sets the local IP address of the circuit.
    * -D,--remote-ip=REMOTE-IP: Sets the remote IP address of the circuit.
    * -a,--admin-enabled=VALUE: Sets admin-enabled.

* Output:
    * Python dictionary content with RESTCONF response data.

.. function:: extension_circuit_show.show_extension_circuit(session,\
name, cid, local, remote)

    *Show Extension Circuit*

        Example Usage of the Method::

                ret = extension_circuit_show.show_extension_circuit(session,
                name, cid, local, remote)
                print (ret)

        Details::

            circuit = {
                            "name": name,
                            "circuit-id": circuit,
                            "local-ip-address": local,
                            "remote-ip-address" : remote,
                      }
            result = extension_circuit_show._show_extension_circuit(session,
            circuit)

        * Input:
            :param session: The session returned by the login.
            :param name: Sets the VE_Port name expressed as slot/port.
            :param cid: Sets the circuit ID.
            :param local: Sets the local IP address of the circuit.
            :param remote: Sets the remote IP address of the circuit.

        * Output:
            :rtype: A list of circuits.

        *Use Cases*

         Show the circuit details.

"""


import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_extension_tunnel import extension_circuit
from pyfos.utils import brcd_util


isHttps = "0"


def _show_extension_circuit(session, cirobject):
    objlist = extension_circuit.get(session)
    cirlist = []
    if isinstance(objlist, extension_circuit):
        objlist = [objlist]
    if isinstance(objlist, list):
        for i in range(len(objlist)):
            if cirobject.peek_name() is not None and\
               cirobject.peek_name() != objlist[i].peek_name():
                continue
            if cirobject.peek_circuit_id() is not None and\
               cirobject.peek_circuit_id() != objlist[i].peek_circuit_id():
                continue
            if cirobject.peek_remote_ip_address() is not None and\
               cirobject.peek_remote_ip_address() !=\
               objlist[i].peek_remote_ip_address():
                continue
            if cirobject.peek_local_ip_address() is not None and\
               cirobject.peek_local_ip_address() !=\
               objlist[i].peek_local_ip_address():
                continue
            if cirobject.peek_admin_enabled() is not None and\
               cirobject.peek_admin_enabled() !=\
               objlist[i].peek_admin_enabled():
                continue
            cirlist.append(objlist[i])
    else:
        print(objlist)
    return cirlist


def show_extension_circuit(session, name, cid=None, local=None, remote=None):
    value_dict = {'name': name, 'circuit-id': cid,
                  'local-ip-address': local,
                  'remote-ip-address': remote}
    cirobject = extension_circuit(value_dict)
    result = _show_extension_circuit(session, cirobject)
    return result


def main(argv):
    # myinput = "-i 10.17.3.70  -n 4/19 -c 0 -S 134.10.10.1 -D 154.10.10.1"
    # myinput = "-i 10.17.3.70 -S 134.10.10.1"
    # argv = myinput.split()
    filters = ["name", "circuit_id", "remote_ip_address", "local_ip_address",
               "admin_enabled"]
    inputs = brcd_util.parse(argv, extension_circuit, filters)
    circobject = inputs['utilobject']
    session = brcd_util.getsession(inputs)
    result = _show_extension_circuit(session, circobject)
    if len(result) == 0:
        print("No Circuit found.")
    else:
        pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
