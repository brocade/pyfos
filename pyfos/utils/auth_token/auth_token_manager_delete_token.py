#!/usr/bin/env python3


# Copyright © 2019 Broadcom. All rights reserved.
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


# auth_token_manager_delete_token.py(pyGen v1.0.0)


"""

:mod:`auth_token_manager_delete_token` - PyFOS util to delete an AuthToken\
 from AuthTokenManager managed token store.
******************************************************************************\
*******************************************************************************
The :mod:`auth_token_manager_delete_token` PyFOS util to delete an AuthToken\
 from AuthTokenManager managed token store.


AuthTokenManager operation to Delete an AuthToken from managed token store.

auth_token_manager_delete_token : usage

* Infrastructure Options:
    * -f,--vfid=VFID: The VFID to which the request is directed.
    * -s,--secured=MODE: The HTTPS mode "self" or "CA" [Optional].
    * -v,--verbose: Verbose mode [Optional].

* Util Script Options:
    * --switch-auth-token=SWITCH-AUTH-TOKEN The switch Auth Token in base64\
      format.
    * --switch-user=SWITCH-USER The switch user account associated with Auth\
      Token.
    * --switch-ip-address=SWITCH-IP-ADDRESS The switch IP address associated\
      with Auth Token.
    * --migrate-config=MIGRATE-CONFIG The Configuration for Auth Token Manager\
      to be used.
    * --config=CONFIG The Configuration for Auth Token Manager to be used.
* Output:
    * Python dictionary content with RESTCONF response data.


.. function::\
auth_token_manager_delete_token.delete_auth_token_manager(\
switch_auth_token, switch_user, switch_ip_address, config)

    *Delete auth_token_manager*

        Example Usage of the Method::

            ret =\
            auth_token_manager_delete_token.delete_auth_token_manager(\
            switch_auth_token, switch_user, switch_ip_address,\
            config=None)
            print (ret)

        Details::

            auth_token_managerObj =\
            brcd_util.pseudodictrestobject("auth-token-manager")
            auth_token_managerObj.set_switch_user(switch_user)
            auth_token_managerObj.set_switch_ip_address(switch_ip_address)
            auth_token_managerObj.set_config(config)
            ret = _delete_auth_token_manager(auth_token_managerObj)
            print (ret)

        * Input::

            :param switch_user: The switch user account associated with Auth\
              Token.
            :param switch_ip_address: The switch IP address associated with\
              Auth Token.
            :param config: The Configuration for Auth Token Manager to be\
              used.

        * Output:

            :rtype: Dictionary of response

"""


# Start utils imports
import sys
from pyfos.pyfos_auth_token import auth_token_manager
from pyfos.utils import brcd_util
# End module imports


def _delete_auth_token_manager(auth_token_managerObj):
    tokenManager = auth_token_manager(auth_token_managerObj.peek_config())
    user = auth_token_managerObj.peek_switch_user()
    ip = auth_token_managerObj.peek_switch_ip_address()
    authToken = tokenManager.findToken(ip, user)
    if authToken is not None:
        return tokenManager.removeToken(authToken)
    return False


def delete_auth_token_manager(switch_user=None, switch_ip_address=None,
                              config=None):
    auth_token_managerObj = \
                          brcd_util.pseudodictrestobject("auth-token-manager")
    auth_token_managerObj.set_switch_user(switch_user)
    auth_token_managerObj.set_switch_ip_address(switch_ip_address)
    auth_token_managerObj.set_config(config)
    return _delete_auth_token_manager(auth_token_managerObj)


def validate(auth_token_managerObj):
    if auth_token_managerObj.peek_switch_user() is None or\
       auth_token_managerObj.peek_switch_ip_address() is None:
        return 1
    return 0


def main(argv):
    filters = ["switch_user", "switch_ip_address", "config", "ignoreMandatory"]
    inputs = brcd_util.parse(argv, "auth-token-manager", filters, validate)
    result = _delete_auth_token_manager(inputs['utilobject'])
    if result is False:
        print("Nothing to delete in local Auth Token cache.")
    else:
        print("Success.")


if __name__ == "__main__":
    main(sys.argv[1:])
