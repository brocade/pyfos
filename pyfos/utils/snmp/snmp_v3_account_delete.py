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


# snmp_v3_account_delete.py(pyGen v1.0.0)


"""

:mod:`snmp_v3_account_delete` - PyFOS util to delete for v3_account
*******************************************************************************
The :mod:`snmp_v3_account_delete` PyFOS util to delete for v3_account


The SNMPv3 user account. This parameter is used to accesses system via SNMPv3\
in a secured manner by means of authentication and privacy. This parameter\
is also used to receive the traps and informs notifications for the\
configured host recipient. Refer to RFC 3414.

snmp_v3_account_delete : usage

* Infrastructure Options:
    * -i,--ipaddr=IPADDR: The IP address of the FOS switch.
    * -L,--login=LOGIN: The login name.
    * -P,--password=PASSWORD: The password.
    * -f,--vfid=VFID: The VFID to which the request is directed.
    * -s,--secured=MODE: The HTTPS mode "self" or "CA" [Optional].
    * -v,--verbose: Verbose mode [Optional].

* Util Script Options:
    * --index=INDEX The label for this object.
* Output:
    * Python dictionary content with RESTCONF response data.


.. function:: snmp_v3_account_delete.delete_v3_account(session, index)

    *Delete v3_account*

        Example Usage of the Method::

            ret = snmp_v3_account_delete.delete_v3_account(session, index)
            print (ret)

        Details::

            v3_accountObj = v3_account()
            v3_accountObj.set_index(index)
            print (ret)

        * Input::

            :param session: The session returned by the login.
            :param index: The label for this object.

        * Output:

            :rtype: Dictionary of response

"""


# Start utils imports
import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_snmp import v3_account

from pyfos.utils import brcd_util
# End module imports


def _delete_v3_account(session, v3_accountObj):
    return v3_accountObj.delete(session)


def delete_v3_account(session, index=None):
    v3_accountObj = v3_account()
    v3_accountObj.set_index(index)
    return _delete_v3_account(session, v3_accountObj)


def validate(v3_accountObj):
    if v3_accountObj.peek_index() is None:
        return 1
    return 0


def main(argv):
    filters = ["index"]
    inputs = brcd_util.parse(argv, v3_account, filters, validate)
    session = brcd_util.getsession(inputs)
    result = _delete_v3_account(session, inputs['utilobject'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
