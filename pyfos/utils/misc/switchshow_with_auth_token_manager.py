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

"""

:mod:`switchshow_with_auth_token_manager` - PyFOS util for switchshow using \
AuthTokenManager login support.
******************************************************************************\
**********************************
The :mod:`switchshow_with_auth_token_manager` PyFOS util for switchshow using \
AuthTokenManager login support.
"""


import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_auth_token import auth_token_manager
from pyfos.pyfos_brocade_fibrechannel_switch import fibrechannel_switch


def example_login(user="admin", password="fibranne", ip="10.200.154.63",
                  https=None, throttle=1.1, verbose=0, tokenArg=None,
                  sessionless=False):
    """
    This function is a wrapper function to get a session dictionary for REST
    operation based on the input options specified, all subsequent REST
    operation can be performed by using this session dictionary. The session
    returned is based on inputs for.

    **Regular REST login session**
        *tokenArg* is None
        *sessionless* is False
    **Auth Token based REST login session**
        *tokenArg* is either a Token Manager instance or an Auth token string
        *password* is None
        *sessionless* is False.
    **sessionless  session without any login**
        *tokenArg* must be None
        *password* is mandatory
        *sessionless* is True.
    """
    return pyfos_auth.login(user, password, ip, https, throttle, verbose,
                            tokenArg, sessionless)


def exampleTokenManager(config=None):
    return auth_token_manager(config)


# pylint: disable=W0613
def main(argv):
    # Login to the switch
    print("\nLogin to the switch")
    session = example_login()
    if pyfos_auth.is_failed_login(session):
        print("login failed because",
              session.get(pyfos_auth.CREDENTIAL_KEY)
              [pyfos_auth.LOGIN_ERROR_KEY])
        sys.exit(3)
    # Get an instance of auth token manager
    print("Get Auth Token Manager instance")
    examplemgrauthtoken = exampleTokenManager()

    # Display authtoken manager details
    print("Display the Auth Token Manager details.")
    examplemgrauthtoken.show()

    # Delete any existing authtoken
    ret = examplemgrauthtoken.delete(session)
    print("Delete Auth Token from the switch\nRet:")
    pyfos_util.response_print(ret)

    # Display authtoken manager details
    print("Display the Auth Token Manager details.")
    examplemgrauthtoken.show()

    # Generate the authtoken
    ret = examplemgrauthtoken.generateToken(session)
    print("Generate Auth Token from the switch\nRet:")
    pyfos_util.response_print(ret)

    # Display authtoken manager details
    print("Display the Auth Token Manager details.")
    examplemgrauthtoken.show()

    print("Get the swithshow with regular session")
    ret = fibrechannel_switch.get(session)
    pyfos_util.response_print(ret)

    # Session Logout
    pyfos_auth.logout(session)

    # Token based authentication session error scenario with default
    # password used and not None.
    print("AuthToken Login error scenario")
    tokensession = example_login(tokenArg=examplemgrauthtoken)
    if pyfos_auth.is_failed_login(tokensession):
        print("Token based login failed because",
              tokensession.get(pyfos_auth.CREDENTIAL_KEY)
              [pyfos_auth.LOGIN_ERROR_KEY])

    print("AuthToken Login Success scenario.")
    # Token based authentication session Success scenario
    tokensession = example_login(password=None,
                                 tokenArg=examplemgrauthtoken)
    if pyfos_auth.is_failed_login(tokensession):
        print("Token based login failed because",
              tokensession.get(pyfos_auth.CREDENTIAL_KEY)
              [pyfos_auth.LOGIN_ERROR_KEY])
        sys.exit(3)

    # Using Token Session for operation
    print("Get the swithshow with authToken based login session.")
    fcobj = fibrechannel_switch.get(tokensession)
    pyfos_util.response_print(fcobj)

    # Patch operation example.
    fcobjnew = fibrechannel_switch()
    fcobjnew.set_name(fcobj.peek_name())
    fcobjnew.set_user_friendly_name("mybanner")
    print("AuthToken login session patch with banner :",
          fcobjnew.peek_user_friendly_name())
    ret = fcobjnew.patch(tokensession)
    pyfos_util.response_print(ret)

    # Revert the banner to original
    print("AuthToken login session patch revert banner :",
          fcobj.peek_user_friendly_name())
    fcobjnew.set_user_friendly_name(fcobj.peek_user_friendly_name())
    ret = fcobjnew.patch(tokensession)
    pyfos_util.response_print(ret)

    print("AuthToken login session Logout")
    # Token Session logout
    pyfos_auth.logout(tokensession)


if __name__ == "__main__":
    main(sys.argv[1:])
