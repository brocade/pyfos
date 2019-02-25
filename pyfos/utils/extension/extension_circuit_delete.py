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

:mod:`extension_circuit_delete` - PyFOS util for deleting a circuit object.
********************************************************************************
The :mod:`extension_circuit_delete` util is used to delete a circuit.

This module is a stand-alone script that can be used to delete an extension
circuit.

extension_circuit_delete.py: Usage

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

* Output:
    * Python dictionary content with RESTCONF response data.

.. function:: extension_circuit_delete.delete_extension_circuit(session,\
name, cid)

    *Delete Extension Circuit*

        Example Usage of the Method::

                ret = extension_circuit_delete.delete_extension_circuit(
                session, name, cid)
                print (ret)

        Details::

            circuit = {
                            "name": name,
                            "circuit-id": circuit,

                      }
            result = extension_circuit_delete._delete_extension_circuit(
            session, circuit)

        * Input:
            :param session: The session returned by the login.
            :param name: Sets the VE_Port name expressed as slot/port.
            :param cid: Sets the ID of the circuit.

        * Output:
            :rtype: A dictionary of return status matching the REST response.

        *Use Cases*

         Delete a circuit to an existing tunnel.

"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_extension_tunnel import extension_circuit
from pyfos.utils import brcd_util


isHttps = "0"


def _delete_extension_circuit(session, cirobject):
    result = cirobject.delete(session)
    return result


def delete_extension_circuit(session, name, cid):
    value_dict = {'name': name, 'circuit-id': cid}
    cirobject = extension_circuit(value_dict)
    result = _delete_extension_circuit(session, cirobject)
    return result


def validate(circobject):
    if circobject.peek_name() is None or \
       circobject.peek_circuit_id() is None:
        return 1
    return 0


def main(argv):
    # myinput = str("-h -i 10.17.3.70  -n 4/19 -c 0 ")
    # argv = myinput.split()
    filters = ["name", "circuit_id"]
    inputs = brcd_util.parse(argv, extension_circuit, filters, validate)
    circobject = inputs['utilobject']
    session = brcd_util.getsession(inputs)
    result = _delete_extension_circuit(session, circobject)
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
