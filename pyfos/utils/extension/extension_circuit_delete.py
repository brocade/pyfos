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
The :mod:`extension_circuit_delete` Util is used to delete a circuit.

This module is a stand-alone script that can be used to delete an extension
circuit.

extension_circuit_delete.py: Usage

* Infrastructure options:
    * -i,--ipaddr=IPADDR: IP address of FOS switch.
    * -L,--login=LOGIN: Login name.
    * -P,--password=PASSWORD: Password.
    * -f,--vfid=VFID: VFID to which the request is directed.
    * -s,--secured=MODE: HTTPS mode "self" or "CA"[Optional].
    * -v,--verbose: Verbose mode[Optional].

* Util scripts options:
    * -n,--name=NAME: Set name or slot/port of the circuit.
    * -c,--circuit-id=CIRCUIT-ID: Set circuit-id of the circuit.

* Outputs:
    * Python dictionary content with RESTCONF response data.

.. function:: extension_circuit_delete.delete_extension_circuit(session,\
name, cid)

    *Delete extension circuit*

        Example usage of the method::

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

        * Inputs:
            :param session: Session returned by login.
            :param name: VE port name expressed as slot/port.
            :param cid: Circuit ID.

        * Outputs:
            :rtype: Dictionary of return status matching rest response.

        *Use cases*

         Delete a circuit to an existing tunnel.

"""

import pyfos.pyfos_auth as pyfos_auth
import pyfos.pyfos_util as pyfos_util
from pyfos.pyfos_brocade_extension_tunnel import extension_circuit
import sys
import pyfos.utils.brcd_util as brcd_util


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
