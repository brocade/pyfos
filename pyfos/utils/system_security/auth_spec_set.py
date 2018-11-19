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

:mod:`auth_spec_set` - PyFOS util to modify authentication mode configuration
*******************************************************************************
The :mod:`auth_spec_set` supports 'aaaconfig' CLI use case.

This module is a standalone script and API that can be used to modify a
ldap server.

* inputs:

| Infrastructure options:

|   -i,--ipaddr=IPADDR     IP address of FOS switch.
|   -L,--login=LOGIN       login name.
|   -P,--password=PASSWORD password.
|   -f,--vfid=VFID         VFID to which the request is directed to [OPTIONAL].
|   -s,--secured=MODE      HTTPS mode "self" or "CA" [OPTIONAL].
|   -v,--verbose           verbose mode[OPTIONAL].

* Util scripts options:
    --authentication-mode         set authentication mode
    --activate-no-log-out         set enable/disable log out
    --primary-auth-log-messages   set enable/disable primary authentication
                                                             error messages

* outputs:
    * success response or dictionary in case of error

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
