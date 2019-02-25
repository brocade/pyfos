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

:mod:`auth_spec_set` - PyFOS util to modify the authentication \
mode configuration.
***************************************************************\
********************
The :mod:`auth_spec_set` supports the 'aaaconfig' CLI use case.

This module is a stand-alone script and API that can be used to modify an
LDAP server.

* Input:

| Infrastructure Options:

|   -i,--ipaddr=IPADDR     The IP address of the FOS switch.
|   -L,--login=LOGIN       The login name.
|   -P,--password=PASSWORD The password.
|   -f,--vfid=VFID         The VFID to which the request is \
                           directed [OPTIONAL].
|   -s,--secured=MODE      The HTTPS mode "self" or "CA" [OPTIONAL].
|   -v,--verbose           Verbose mode [OPTIONAL].

* Util Script Options:
    --authentication-mode         Sets the authentication mode.
    --activate-no-log-out         Enables or disables log out.
    --primary-auth-log-messages   Enables or disables primary authentication \
                                  error messages.

* Output:
    * A success response or dictionary in case of error.

"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_security import auth_spec
from pyfos.utils import brcd_util


def main(argv):
    filters = ["activate_no_log_out", "authentication_mode",
               "primary_auth_log_messages"]

    inputs = brcd_util.parse(argv, auth_spec, filters)

    server_obj = inputs['utilobject']

    if (server_obj.peek_authentication_mode() is None and
            server_obj.peek_primary_auth_log_messages() is None and
            server_obj.peek_activate_no_log_out() is None):
        print("Missing command line options")
        print(inputs['utilusage'])
        exit(1)

    # Login to switch
    session = brcd_util.getsession(inputs)

    result = server_obj.patch(session)
    pyfos_util.response_print(result)

    # Log out
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
