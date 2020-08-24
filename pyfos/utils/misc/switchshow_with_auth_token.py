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

:mod:`switchshow_with_auth_token` - PyFOS util for switchshow using \
AuthToken login support.
******************************************************************************\
**********************************
The :mod:`switchshow_with_auth_token` PyFOS util for switchshow using \
AuthToken login support.
"""


import sys
import time
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_fibrechannel_switch import fibrechannel_switch
from pyfos.utils.misc.switchshow_with_auth_token_manager import example_login


# pylint: disable=W0613
def main(argv):
    # Login to the switch
    session = example_login()
    if pyfos_auth.is_failed_login(session):
        print("login failed because",
              session.get(pyfos_auth.CREDENTIAL_KEY)
              [pyfos_auth.LOGIN_ERROR_KEY])
        sys.exit(3)
    print("Login to Switch.")

    # Get the credential
    credential = session.get("credential")

    # Delete the AuthToken example
    # Get a connection based on the session
    conn = pyfos_util.http_connection(session)

    pyfos_util.debug(session, "DELETE ", "/rest/auth-token", "")

    # Delete request is sent
    conn.request("DELETE", "/rest/auth-token", "", credential)

    delay = session.get("throttle_delay")
    if delay > 0:
        time.sleep(delay)

    resp = conn.getresponse()
    page = resp.read()

    if resp.status == 204:
        print("Auth Token Delete.")

    if len(page) != 0:
        print("The AuthToken Delete operation")
        pyfos_util.response_print(pyfos_util.parse_page(page))

    # Generate the authtoken
    print("Create an Auth Token a afresh")
    my_auth_token = None

    conn = pyfos_util.http_connection(session)

    pyfos_util.debug(session, "POST ", "/rest/auth-token", "")

    conn.request("POST", "/rest/auth-token", "", credential)

    delay = session.get("throttle_delay")
    if delay > 0:
        time.sleep(delay)

    response = conn.getresponse()
    page = response.read()
    # print (page)
    auth = response.getheader('authorization')
    if response.status == 201:
        if auth is not None:
            # Save the AuthToken
            my_auth_token = auth

    print("Auth Token : ", my_auth_token)

    # Session Logout
    pyfos_auth.logout(session)
    print("Session Logout")

    if my_auth_token is None:
        print("Unable to create an AuthToken")
        sys.exit(1)

    # Token based authentication session
    tokensession = example_login(password=None, tokenArg=my_auth_token)
    if pyfos_auth.is_failed_login(tokensession):
        print("Token based login failed because",
              tokensession.get(pyfos_auth.CREDENTIAL_KEY)
              [pyfos_auth.LOGIN_ERROR_KEY])
        sys.exit(3)
    print("AuthToken based Session Login")

    # Using Token Session for operation
    print("Get the swithshow with authToken")
    fcobj = fibrechannel_switch.get(tokensession)
    pyfos_util.response_print(fcobj)

    # Patch operation example.
    fcobjnew = fibrechannel_switch()
    fcobjnew.set_name(fcobj.peek_name())
    fcobjnew.set_user_friendly_name("mybanner")
    print("Patch with banner :", fcobjnew.peek_user_friendly_name())
    ret = fcobjnew.patch(tokensession)
    pyfos_util.response_print(ret)

    # Revert the banner to original
    print("Revert Patch with banner :", fcobj.peek_user_friendly_name())
    fcobjnew.set_user_friendly_name(fcobj.peek_user_friendly_name())
    ret = fcobjnew.patch(tokensession)
    pyfos_util.response_print(ret)

    # Token Session logout
    pyfos_auth.logout(tokensession)
    print("AuthToken based Session Logout.")

    # Login to the switch
    session = example_login()
    if pyfos_auth.is_failed_login(session):
        print("login failed because",
              session.get(pyfos_auth.CREDENTIAL_KEY)
              [pyfos_auth.LOGIN_ERROR_KEY])

    print("Session Login")

    # Get the credential
    credential = session.get("credential")

    # Delete the AuthToken
    conn = pyfos_util.http_connection(session)

    pyfos_util.debug(session, "DELETE ", "/rest/auth-token", "")

    conn.request("DELETE", "/rest/auth-token", "", credential)

    delay = session.get("throttle_delay")
    if delay > 0:
        time.sleep(delay)

    resp = conn.getresponse()
    page = resp.read()
    if resp.status == 204:
        print("Auth Token Delete.")

    if len(page) != 0:
        print("The AuthToken delete operation")
        pyfos_util.response_print(pyfos_util.parse_page(page))

    # Session Logout
    pyfos_auth.logout(session)
    print("Session Logout")


if __name__ == "__main__":
    main(sys.argv[1:])
