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


# slot_test.py(pyGen v1.0.0)


"""

:mod:`slot_test` - PyFOS util  support for RPC operations of slot_test
*******************************************************************************
The :mod:`slot_test` PyFOS util  support for RPC operations of slot_test


slot test query response parameters for the PCIe health operations.

slot_test : usage

* Infrastructure Options:
    * -i,--ipaddr=IPADDR: The IP address of the FOS switch.
    * -L,--login=LOGIN: The login name.
    * -P,--password=PASSWORD: The password.
    * -f,--vfid=VFID: The VFID to which the request is directed.
    * -s,--secured=MODE: The HTTPS mode "self" or "CA" [Optional].
    * -v,--verbose: Verbose mode [Optional].

* Util Script Options:
    * --slot-id=SLOT-ID The number of the physical slot in the chassis in\
      which the blade is inserted. 255 indicates for all the slots present \
      the switch.
* Output:
    * Python dictionary content with RESTCONF response data.


.. function:: slot_test.rpc_slot_test(session, slot_id)

    *RPC slot_test*

        Example Usage of the Method::

            ret = slot_test.rpc_slot_test(session, slot_id)
            print (ret)

        Details::

            slot_testObj = slot_test()
            slot_testObj.set_slot_id(slot_id)
            print (ret)

        * Input::

            :param session: The session returned by the login.
            :param slot_id: The number of the physical slot in the chassis in\
              which the blade is inserted.

        * Output:

            :rtype: Dictionary of response

"""


# Start utils imports
import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_operation_pcie_health import slot_test

from pyfos.utils import brcd_util
# End module imports


def _rpc_slot_test(session, slot_testObj):
    return slot_testObj.post(session)


def rpc_slot_test(session, slot_id=None):
    slot_testObj = slot_test()
    slot_testObj.set_slot_id(slot_id)
    return _rpc_slot_test(session, slot_testObj)


def validate(slot_testObj):
    if slot_testObj.peek_slot_id() is None:
        return 1
    return 0


def main(argv):
    filters = ["slot_id"]
    inputs = brcd_util.parse(argv, slot_test, filters, validate)
    session = brcd_util.getsession(inputs)
    result = _rpc_slot_test(session, inputs['utilobject'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
