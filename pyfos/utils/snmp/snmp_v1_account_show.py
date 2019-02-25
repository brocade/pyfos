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

:mod:`snmp_v1_account_show` - PyFOS util to show the snmpv1 account.
********************************************************************
The :mod:`snmp_v1_account_show` provides option to display the
snmp v1 account information.

This module can be used to display the snmp v1 account information
including the index, community name and community group

* inputs:

| Infrastructure options:

|   -i,--ipaddr=IPADDR     IP address of FOS switch.
|   -L,--login=LOGIN       login name.
|   -P,--password=PASSWORD password.
|   -f,--vfid=VFID         VFID to which the request is directed to [OPTIONAL].
|   -s,--secured=MODE      HTTPS mode "self" or "CA" [OPTIONAL].
|   -v,--verbose           verbose mode[OPTIONAL].

  Util scripts options:

  | --index=INDEX          Index of SNMPv1 account

* outputs:
    * SNMP v1 account configuration details.

.. function:: snmp_v1_account_info(session)

    * Display the snmp v1 account information.

        Example usage of the method:

            result = snmp_v1_account_info(inputs['session'])
            print (result)

        Details::

           snmp_v1_acc_obj = v1_account()
           result = snmp_v1_acc_obj.get(session)

        * inputs:
            :param session: session returned by login.

        * outputs:
            :rtype: dictionary of return snmp v1 account rest response

        *use cases*

        1. Retrieve the snmp v1 account details.
"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.utils import brcd_util
from pyfos.pyfos_brocade_snmp import v1_account


def snmp_v1_account_info(session, v1_account_obj):
    snmp_v1_acc_obj = v1_account()
    if v1_account_obj is None:
        result = snmp_v1_acc_obj.get(session, None)
    else:
        result = snmp_v1_acc_obj.get(session, v1_account_obj)

    return result


def main(argv):

    # Print arguments
    # print(sys.argv[1:])

    filters = ['index']
    inputs = brcd_util.parse(argv, v1_account, filters)

    v1_account_obj = inputs['utilobject']

    session = brcd_util.getsession(inputs)

    result = snmp_v1_account_info(
        inputs['session'], v1_account_obj.peek_index())
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
