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

:mod:`snmp_v3_account_modify` - PyFOS util for updating snmp v3 account
***********************************************************************
The :mod:`snmp_v3_account__modify` provides option to modify snmp v3 account
attribute

This module can be used to modify snmpv3 account attributes.

* inputs:

|  Infrastructure options:

  | -i,--ipaddr=IPADDR     IP address of FOS switch
  | -L,--login=LOGIN       login name.
  | -P,--password=PASSWORD password.
  | -f,--vfid=VFID         VFID to which the request is directed to [OPTIONAL].
  | -s,--secured=MODE      HTTPS mode "self" or "CA" [OPTIONAL].
  | -v,--verbose           verbose mode[OPTIONAL].

|  Util scripts options:

  | --index=VALUE             Index of SNMPv3 account
  | --user-name=VALUE         The snmpv3 user name
  | --authentication_protocol The snmpv3 user authentication protocol[OPTIONAL]
  | --privacy_protocol        The snmpv3 user privacy protocol[OPTIONAL]
  | --authentication_password The snmpv3 user authentication password[OPTIONAL]
  | --privacy_password        The snmpv3 user privacy password[OPTIONAL]
  | --manager_engine_id       The snmp manager engine id[OPTIONAL]

* outputs:

    * Status of the patch operation on v3 account's attributes

.. function:: v3_acc_obj.set_user_name(username)

    * Configures usm user name

        Example usage of the method::

            ret = v3_acc_obj.set_user_name(username)
            print (ret)

        Details::

            v3_acc_obj = v3_account()
            if username is not None:
               v3_acc_obj.set_user_name(username)

            result = _set_snmp_v3_account(session, v1_acc_obj)

        * inputs:
            :param session: session returned by login.
            :param username: user name of a snmpv3 account

        * outputs:
            :rtype: dictionary of return status matching rest response


.. function:: v3_acc_obj.set_authentication_protocol(authProt)

    * Configures snmpv3 user authenticaiton protocol

        Example usage of the method::

            ret = v3_acc_obj.set_authentication_protocol(authProt)
            print (ret)

        Details::

            v3_acc_obj = v3_account()
            if authProt is not None:
               v3_acc_obj.set_authentication_protocol(authProt)

            result = _set_authentication_protocol(session, v1_acc_obj)

        * inputs:
            :param session: session returned by login.
            :param authProt: snmpv3 user's authentication protocol

        * outputs:
            :rtype: dictionary of return status matching rest response


.. function:: v3_acc_obj.set_privacy_protocol(privProt)

    * Configures snmpv3 user's privacy protocol

        Example usage of the method::

            ret = v3_acc_obj.set_privacy_protocol(privProt)
            print (ret)

        Details::

            v3_acc_obj = v3_account()
            if privProt is not None:
               v3_acc_obj.set_privacy_protocol(privProt)

            result = _set_privacy_protocol(session, v1_acc_obj)

        * inputs:
            :param session: session returned by login.
            :param authProt: snmpv3 user's privacy protocol

        * outputs:
            :rtype: dictionary of return status matching rest response


.. function:: v3_acc_obj.set_authentication_password(authPasswd)

    * Configures snmpv3 user's authenticaiton password

        Example usage of the method::

            ret = v3_acc_obj.set_authentication_password(authPasswd)
            print (ret)

        Details::

            v3_acc_obj = v3_account()
            if authPasswd is not None:
               v3_acc_obj.set_authentication_password(authPasswd)

            result = _set_authentication_password(session, v1_acc_obj)

        * inputs:
            :param session: session returned by login.
            :param authPasswd: snmpv3 user's authentication password

        * outputs:
            :rtype: dictionary of return status matching rest response


.. function:: v3_acc_obj.set_privacy_password(privPasswd)

    * Configures snmpv3 user's privacy password

        Example usage of the method::

            ret = v3_acc_obj.set_privacy_password(privPasswd)
            print (ret)

        Details::

            v3_acc_obj = v3_account()
            if privPasswd is not None:
               v3_acc_obj.set_privacy_password(privPasswd)

            result = _set_privacy_password(session, v1_acc_obj)

        * inputs:
            :param session: session returned by login.
            :param privPasswd: snmpv3 user's privacy password

        * outputs:
            :rtype: dictionary of return status matching rest response


.. function:: v3_acc_obj.set_manager_engine_id(mgrEngId)

    * Configures snmpv3 manager engine id

        Example usage of the method::

            ret = v3_acc_obj.set_manager_engine_id(mgrEngId)
            print (ret)

        Details::

            v3_acc_obj = v3_account()
            if mgrEngId is not None:
               v3_acc_obj.set_manager_engine_id(mgrEngId)

            result = _set_manager_engine_id(session, v1_acc_obj)

        * inputs:
            :param session: session returned by login.
            :param mgrEngId: snmpv3 manager engine id

        * outputs:
            :rtype: dictionary of return status matching rest response


"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.utils import brcd_util
from pyfos.pyfos_brocade_snmp import v3_account


def _set_snmp_v3_account(session, restobject):
    return restobject.patch(session)


def _set_user_name(session, username):
    v3_acc_obj = v3_account()
    if username is not None:
        v3_acc_obj.set_user_name(username)
    result = _set_snmp_v3_account(session, v3_acc_obj)
    return result


def _set_authentication_protocol(session, authProt):
    v3_acc_obj = v3_account()
    if authProt is not None:
        v3_acc_obj.set_authentication_protocol(authProt)
    result = _set_snmp_v3_account(session, v3_acc_obj)
    return result


def _set_privacy_protocol(session, privProt):
    v3_acc_obj = v3_account()
    if privProt is not None:
        v3_acc_obj.set_privacy_protocol(privProt)
    result = _set_snmp_v3_account(session, v3_acc_obj)
    return result


def _set_authentication_password(session, authPasswd):
    v3_acc_obj = v3_account()
    if authPasswd is not None:
        v3_acc_obj.set_authentication_password(authPasswd)
    result = _set_snmp_v3_account(session, v3_acc_obj)
    return result


def _set_privacy_password(session, privPasswd):
    v3_acc_obj = v3_account()
    if privPasswd is not None:
        v3_acc_obj.set_privacy_password(privPasswd)
    result = _set_snmp_v3_account(session, v3_acc_obj)
    return result


def _set_manager_engine_id(session, mgrEngId):
    v3_acc_obj = v3_account()
    if mgrEngId is not None:
        v3_acc_obj.set_manager_engine_id(mgrEngId)
    result = _set_snmp_v3_account(session, v3_acc_obj)
    return result


def validate(v3_acc_obj):
    if (v3_acc_obj.peek_index() is None and
       v3_acc_obj.peek_user_name() is None):
        return 1
    return 0


def main(argv):

    # Print arguments
    # print(sys.argv[1:])

    filters = ['index', 'user_name', 'authentication_protocol',
               'privacy_protocol', 'authentication_password',
               'privacy_password', 'manager_engine_id']

    inputs = brcd_util.parse(argv, v3_account, filters, validate)

    session = brcd_util.getsession(inputs)

    result = _set_snmp_v3_account(inputs['session'], inputs['utilobject'])
    pyfos_util.response_print(result)

    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
