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


# auth_token_manager_add_token.py(pyGen v1.0.0)


"""

:mod:`auth_token_manager_add_token` - PyFOS util to add an AuthToken to\
 AuthTokenManager's tokens store
******************************************************************************\
*******************************************************************************
The :mod:`auth_token_manager_add_token` PyFOS util to add an AuthToken\
 to AuthTokenManager's tokens store


AuthTokenManager operation to add an AuthToken to managed token store.

auth_token_manager_add_token : usage

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
    * --config=CONFIG The Configuration for Auth Token Manager to be used.
* Output:
    * Python dictionary content with RESTCONF response data.


.. function:: auth_token_manager_add_token.add_auth_token_manager(\
switch_auth_token, switch_user, switch_ip_address, config=None)

    *Create auth_token_manager*

        Example Usage of the Method::

            ret =\
            auth_token_manager_add_token.add_auth_token_manager(\
            switch_auth_token, switch_user, switch_ip_address,\
            config)
            print (ret)

        Details::

            auth_token_managerObj = \
            brcd_util.pseudodictrestobject("auth-token-manager")
            auth_token_managerObj.set_switch_auth_token(switch_auth_token)
            auth_token_managerObj.set_switch_user(switch_user)
            auth_token_managerObj.set_switch_ip_address(switch_ip_address)
            auth_token_managerObj.set_config(config)
            ret = _add_auth_token_manager(auth_token_managerObj)
            print (ret)

        * Input::

            :param switch_auth_token: The switch Auth Token in base64 format.
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


def _add_auth_token_manager(auth_token_managerObj):
    tokenManager = auth_token_manager(auth_token_managerObj.peek_config())
    user = auth_token_managerObj.peek_switch_user()
    ip = auth_token_managerObj.peek_switch_ip_address()
    token = auth_token_managerObj.peek_switch_auth_token()
    authToken = tokenManager.getAuthTokenInstance(ip, user, token)
    return tokenManager.addToken(authToken)


def add_auth_token_manager(switch_auth_token, switch_user,
                           switch_ip_address, config=None):
    auth_token_managerObj = \
                          brcd_util.pseudodictrestobject("auth-token-manager")
    auth_token_managerObj.set_switch_auth_token(switch_auth_token)
    auth_token_managerObj.set_switch_user(switch_user)
    auth_token_managerObj.set_switch_ip_address(switch_ip_address)
    auth_token_managerObj.set_config(config)
    return _add_auth_token_manager(auth_token_managerObj)


def validate(auth_token_managerObj):
    if auth_token_managerObj.peek_switch_auth_token() is None or\
       auth_token_managerObj.peek_switch_user() is None or\
       auth_token_managerObj.peek_switch_ip_address() is None:
        return 1
    return 0


def main(argv):
    filters = ["switch_auth_token", "switch_user", "switch_ip_address",
               "config", "ignoreMandatory"]
    inputs = brcd_util.parse(argv, "auth-token-manager", filters, validate)
    result = _add_auth_token_manager(inputs['utilobject'])
    if result is False:
        print("Operation Failed.")
    else:
        print("Success.")


if __name__ == "__main__":
    main(sys.argv[1:])
