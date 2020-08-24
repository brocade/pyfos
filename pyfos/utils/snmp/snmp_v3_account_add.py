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


# snmp_v3_account_add.py(pyGen v1.0.0)


"""

:mod:`snmp_v3_account_add` - PyFOS util to create for v3_account
*******************************************************************************
The :mod:`snmp_v3_account_add` PyFOS util to create for v3_account


The SNMPv3 user account. This parameter is used to accesses system via SNMPv3\
in a secured manner by means of authentication and privacy. This parameter\
is also used to receive the traps and informs notifications for the\
configured host recipient. Refer to RFC 3414.

snmp_v3_account_add : usage

* Infrastructure Options:
    * -i,--ipaddr=IPADDR: The IP address of the FOS switch.
    * -L,--login=LOGIN: The login name.
    * -P,--password=PASSWORD: The password.
    * -f,--vfid=VFID: The VFID to which the request is directed.
    * -s,--secured=MODE: The HTTPS mode "self" or "CA" [Optional].
    * -v,--verbose: Verbose mode [Optional].

* Util Script Options:
    * --privacy-protocol=PRIVACY-PROTOCOL The privacy protocol (DES or\
      AES128) for the SNMPv3 user. Refer to RFC 3414.
    * --index=INDEX The label for this object.
    * --user-name=USER-NAME The name of the user that connects to the agent.
    * --authentication-protocol=AUTHENTICATION-PROTOCOL The authorization\
      protocol(MD5 or SHA) for the SNMPv3 user. Refer to RFC 3414.
    * --privacy-password=PRIVACY-PASSWORD This is write-only leaf and it\
      defines the privacy password for the SNMPv3 user to access the system\
      resources. The password should be base64 encoded. Refer to RFC 3414.
    * --manager-engine-id=MANAGER-ENGINE-ID The user-defined engine ID for the\
      SNMP manager which is used to receive the SNMPv3 informs\
      notifications. This parameter is applicable only when informs is\
      enabled.
    * --user-group=USER-GROUP Indicates whether the SNMPv3 user belongs to a\
      read-only or a read-write group.
    * --authentication-password=AUTHENTICATION-PASSWORD This is write-only\
      leaf and it defines the authentication password for the SNMPv3 user to\
      access the system resources. The password should be base64 encoded.\
      Refer to RFC 3414.
* Output:
    * Python dictionary content with RESTCONF response data.


.. function:: snmp_v3_account_add.create_v3_account(session, privacy_protocol,\
index, user_name, authentication_protocol, privacy_password,\
manager_engine_id, user_group, authentication_password)

    *Create v3_account*

        Example Usage of the Method::

            ret = snmp_v3_account_add.create_v3_account(session,\
            privacy_protocol, index, user_name, authentication_protocol,\
            privacy_password, manager_engine_id, user_group,\
            authentication_password)
            print (ret)

        Details::

            v3_accountObj = v3_account()
            v3_accountObj.set_privacy_protocol(privacy_protocol)
            v3_accountObj.set_index(index)
            v3_accountObj.set_user_name(user_name)
            v3_accountObj.set_authentication_protocol(authentication_protocol)
            v3_accountObj.set_privacy_password(privacy_password)
            v3_accountObj.set_manager_engine_id(manager_engine_id)
            v3_accountObj.set_user_group(user_group)
            v3_accountObj.set_authentication_password(authentication_password)
            print (ret)

        * Input::

            :param session: The session returned by the login.
            :param privacy_protocol: The privacy protocol (DES or AES128) for\
              the SNMPv3 user. Refer to RFC 3414.
            :param index: The label for this object.
            :param user_name: The name of the user that connects to the agent.
            :param authentication_protocol: The authorization protocol(MD5 or\
              SHA) for the SNMPv3 user. Refer to RFC 3414.
            :param privacy_password: This is write-only leaf and it defines\
              the privacy password for the SNMPv3 user to access the system\
              resources. The password should be base64 encoded. Refer to RFC\
              3414.
            :param manager_engine_id: The user-defined engine ID for the SNMP\
              manager which is used to receive the SNMPv3 informs\
              notifications. This parameter is applicable only when informs\
              is enabled.
            :param user_group: Indicates whether the SNMPv3 user belongs to a\
              read-only or a read-write group.
            :param authentication_password: This is write-only leaf and it\
              defines the authentication password for the SNMPv3 user to\
              access the system resources. The password should be base64\
              encoded. Refer to RFC 3414.

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


def _create_v3_account(session, v3_accountObj):
    return v3_accountObj.post(session)


def create_v3_account(session, privacy_protocol=None, index=None,
                      user_name=None, authentication_protocol=None,
                      privacy_password=None, manager_engine_id=None,
                      user_group=None, authentication_password=None):
    v3_accountObj = v3_account()
    v3_accountObj.set_privacy_protocol(privacy_protocol)
    v3_accountObj.set_index(index)
    v3_accountObj.set_user_name(user_name)
    v3_accountObj.set_authentication_protocol(authentication_protocol)
    v3_accountObj.set_privacy_password(privacy_password)
    v3_accountObj.set_manager_engine_id(manager_engine_id)
    v3_accountObj.set_user_group(user_group)
    v3_accountObj.set_authentication_password(authentication_password)
    return _create_v3_account(session, v3_accountObj)


def validate(v3_accountObj):
    if v3_accountObj.peek_index() is None or v3_accountObj.peek_user_name()\
       is None or v3_accountObj.peek_user_group() is None:
        return 1
    return 0


def main(argv):
    filters = ["privacy_protocol", "index", "user_name",
               "authentication_protocol", "privacy_password",
               "manager_engine_id", "user_group", "authentication_password"]
    inputs = brcd_util.parse(argv, v3_account, filters, validate)
    session = brcd_util.getsession(inputs)
    result = _create_v3_account(session, inputs['utilobject'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
