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

:mod:`switchshow_with_sessionless` - PyFOS util for switchshow using \
AuthToken login support.
******************************************************************************\
**********************************
The :mod:`switchshow_with_sessionless` PyFOS util for switchshow using \
AuthToken login support.

"""


import sys
import base64
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_fibrechannel_switch import fibrechannel_switch
from pyfos import pyfos_version
from pyfos.utils.misc.switchshow_with_auth_token_manager import example_login


def dummy_session(user="admin", password="fibranne", ip="10.200.154.63",
                  https=None, throttle=1.1, verbose=0, tokenArg=None,
                  sessionless=True):
    """
    This function creates a dummy session without any login to switch.
    returns a login session equivalent dictionary to be used for all REST
    operations.

    """
    auth = user + ":" + password
    auth_encoded = base64.b64encode(auth.encode())

    credential = {"Authorization": "Basic " + auth_encoded.decode()}
    ver9_0_0 = pyfos_version.fosversion("9.0.0")
    mysession = {"credential": credential, "ip_addr": ip,
                 "user": user,
                 "vfid": -1, "ishttps": https, "debug": verbose,
                 "version": ver9_0_0,
                 "throttle_delay": throttle,
                 "auth_token": tokenArg,
                 "sessionless": sessionless}
    return mysession


# pylint: disable=W0613
def main(argv):
    """
    This function shows the following sequence of operation.

    **Support for login/logout sequence for Sessionless**
        *login* returns a pseudo session without actual Login.
        *REST operation support* for GET Examples.
        *logout* no-operation logout.

    **Dummy session creation and operations**
        *Pseudo session* using dummy function without login.
        *REST operation support* for GET/PATCH examples.

    """
    # Login to the switch
    login_sessionless = example_login(sessionless=True)
    if pyfos_auth.is_failed_login(login_sessionless):
        print("login failed because",
              login_sessionless.get(pyfos_auth.CREDENTIAL_KEY)
              [pyfos_auth.LOGIN_ERROR_KEY])
        sys.exit(3)
    print("Login to Switch with session-less option, Actually there is no ",
          "login done to switch.")

    # Using sessionless Session for operation
    print("\nGet the swithshow with session-less")
    fcobj = fibrechannel_switch.get(login_sessionless)
    pyfos_util.response_print(fcobj)

    # Sessionless Session logout(No-operation)
    pyfos_auth.logout(login_sessionless)
    print("\nLogout session-less based login session no-op.")

    # Dummy session to the switch
    pseudosession = dummy_session()
    print("\nGet swithshow using pseudo-session with session-less [Allowed].")
    fcobj = fibrechannel_switch.get(pseudosession)
    pyfos_util.response_print(fcobj)

    # Patch operation example.
    print("\nPatch using pseudo-session for session-less [Forbidden]")
    fcobjnew = fibrechannel_switch()
    fcobjnew.set_name(fcobj.peek_name())
    fcobjnew.set_user_friendly_name("mybanner")
    print("Patch with banner :", fcobjnew.peek_user_friendly_name())
    ret = fcobjnew.patch(pseudosession)
    pyfos_util.response_print(ret)

    # Revert the banner to original
    print("\nPatch using pseudo-session for session-less[Forbidden]")
    print("Revert Patch with banner :", fcobj.peek_user_friendly_name())
    fcobjnew.set_user_friendly_name(fcobj.peek_user_friendly_name())
    ret = fcobjnew.patch(pseudosession)
    pyfos_util.response_print(ret)
    print("No logout required for pseudo-session")


if __name__ == "__main__":
    main(sys.argv[1:])
