#!/usr/bin/env python3


# Copyright © 2019-2020 Broadcom. All rights reserved.
# The term “Broadcom” refers to Broadcom Inc. and/or its subsidiaries.
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


# lldp_gigabitethernet_operations.py(pyGen v1.0.0)


"""

:mod:`lldp_gigabitethernet_operations` - PyFOS util  support for RPC\
 operations of lldp_operations
******************************************************************************\
*******************************************************************************
The :mod:`lldp_gigabitethernet_operations` PyFOS util  support for RPC\
 operations of lldp_operations


LLDP actions container

lldp_gigabitethernet_operations : usage

* Infrastructure Options:
    * -i,--ipaddr=IPADDR: The IP address of the FOS switch.
    * -L,--login=LOGIN: The login name.
    * -P,--password=PASSWORD: The password.
    * -f,--vfid=VFID: The VFID to which the request is directed.
    * -s,--secured=MODE: The HTTPS mode "self" or "CA" [Optional].
    * -v,--verbose: Verbose mode [Optional].
    * -a,--authtoken: AuthToken value or AuthTokenManager config\
    file[OPTIONAL].
    * -z,--nosession: Sessionless authentication based login[OPTIONAL].
    * --nocredential: No credential to be sent in the request[OPTIONAL].

* Util Script Options:
    * --slot-port=SLOT-PORT: Port name
    * --action=ACTION: LLDP actions on the given port
* Output:
    * Python dictionary content with RESTCONF response data.


.. function:: lldp_gigabitethernet_operations.rpc_lldp_operations(session,\
slot_port, action)

    *RPC lldp_operations*

    Example Usage of the Method::

            ret = lldp_gigabitethernet_operations.rpc_lldp_operations(session,\
 slot_port, action)
            print (ret)

    Details::

        lldp_operationsObj = lldp_operations()
        lldp_operationsObj.set_slot_port(slot_port)
        lldp_operationsObj.set_action(action)
        ret = _rpc_lldp_operations(session, lldp_operationsObj)
        print (ret)

    **Inputs**

    :param session: The session returned by the login.
    :param slot_port: Port name
    :param action: LLDP actions on the given port

    **Output**

    :rtype: Dictionary of response

"""


# Start utils imports
import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_operation_lldp import lldp_operations

from pyfos.utils import brcd_util
# End module imports


def _rpc_lldp_operations(session, lldp_operationsObj):
    return lldp_operationsObj.post(session)


def rpc_lldp_operations(session, slot_port=None, action=None):
    lldp_operationsObj = lldp_operations()
    lldp_operationsObj.set_slot_port(slot_port)
    lldp_operationsObj.set_action(action)
    return _rpc_lldp_operations(session, lldp_operationsObj)


def validate(lldp_operationsObj):
    if lldp_operationsObj.peek_slot_port() is None or\
       lldp_operationsObj.peek_action() is None:
        return 1
    return 0


def main(argv):
    filters = ["slot_port", "action"]
    inputs = brcd_util.parse(argv, lldp_operations, filters, validate)
    session = brcd_util.getsession(inputs)
    result = _rpc_lldp_operations(session, inputs['utilobject'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
