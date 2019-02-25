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

:mod:`snmp_v1_account_modify` - PyFOS util for updating snmp v1 account
***********************************************************************
The :mod:`snmp_v1_account__modify` provides option to modify snmp v1 account
attribute

This module can be used to modify snmpv1 account attributes.

* inputs:

|  Infrastructure options:

  | -i,--ipaddr=IPADDR     IP address of FOS switch
  | -L,--login=LOGIN       login name.
  | -P,--password=PASSWORD password.
  | -f,--vfid=VFID         VFID to which the request is directed to [OPTIONAL].
  | -s,--secured=MODE      HTTPS mode "self" or "CA" [OPTIONAL].
  | -v,--verbose           verbose mode[OPTIONAL].

|  Util scripts options:

  | --index=VALUE                             Index of SNMPv1 account
  | --community-name=VALUE                    The community name

* outputs:

    * Status of the patch operation on v1 account's attribute

.. function:: v1_acc_obj.set_community_name(community)

    * Configures community name

        Example usage of the method::

            ret = v1_acc_obj.set_community_name(community)
            print (ret)

        Details::

            v1_acc_obj = v1_account()
            if community is not None:
                v1_acc_obj.set_community_name(community)

            result = _set_snmp_v1_account(session, v1_acc_obj)

        * inputs:
            :param session: session returned by login.
            :param community: community name of a snmpv1 account

        * outputs:
            :rtype: dictionary of return status matching rest response


"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.utils import brcd_util
from pyfos.pyfos_brocade_snmp import v1_account


def _set_snmp_v1_account(session, restobject):
    return restobject.patch(session)


def _set_community_name(session, community):
    v1_acc_obj = v1_account()
    if community is not None:
        v1_acc_obj.set_community_name(community)
    result = _set_snmp_v1_account(session, v1_acc_obj)
    return result


def validate(v1_acc_obj):
    if (v1_acc_obj.peek_index() is None and
            v1_acc_obj.peek_community_name() is None):
        return 1
    return 0


def main(argv):

    # Print arguments
    # print(sys.argv[1:])

    filters = ['index', 'community_name']

    inputs = brcd_util.parse(argv, v1_account, filters, validate)

    session = brcd_util.getsession(inputs)

    result = _set_snmp_v1_account(inputs['session'], inputs['utilobject'])
    pyfos_util.response_print(result)

    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
