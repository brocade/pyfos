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

:mod:`tacacs_server_set` - PyFOS util to modify tacacs server configuration
*******************************************************************************
The :mod:`tacacs_server_create` supports 'aaaconfig' CLI use case.

This module is a standalone script and API that can be used to modify a
tacacs server.

* inputs:

| Infrastructure options:

|   -i,--ipaddr=IPADDR     IP address of FOS switch.
|   -L,--login=LOGIN       login name.
|   -P,--password=PASSWORD password.
|   -f,--vfid=VFID         VFID to which the request is directed to [OPTIONAL].
|   -s,--secured=MODE      HTTPS mode "self" or "CA" [OPTIONAL].
|   -v,--verbose           verbose mode[OPTIONAL].

* Util scripts options:
    --server                        set tacacs server name/ip
    --port                          set tacacs server port number
    --timeout                       set tacacs server timeout value
    --authentication                set tacacs server authentication type
    --secret                        set tacacs server secret type
    --encryption                    set tacacs server encryption type
    --position                      set tacacs server position

* outputs:
    * success response or dictionary in case of error

"""

import sys
import pyfos.pyfos_auth as pyfos_auth
import pyfos.pyfos_util as pyfos_util
from pyfos.pyfos_brocade_security import tacacs_server
import pyfos.utils.brcd_util as brcd_util


def main(argv):
    filters = ["server", "port", "timeout", "authentication",
               "secret", "encryption_type", "position"]
    inputs = brcd_util.parse(argv, tacacs_server, filters)

    tacacs_obj = inputs['utilobject']

    if tacacs_obj.peek_server() is None:
        print("Missing command line options")
        print(inputs['utilusage'])
        exit(1)

    if not (tacacs_obj.peek_port() or
       tacacs_obj.peek_timeout() or tacacs_obj.peek_authentication() or
       tacacs_obj.peek_secret() or tacacs_obj.peek_encryption_type() or
       tacacs_obj.peek_position()):
        print("Missing command line options")
        print(inputs['utilusage'])
        exit(1)

    # Login to switch
    session = brcd_util.getsession(inputs)

    result = tacacs_obj.patch(session)
    pyfos_util.response_print(result)

    # Log out
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
