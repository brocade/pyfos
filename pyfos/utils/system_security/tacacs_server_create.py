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

:mod:`tacacs_server_create` - PyFOS util to create a TACACS+ \
server configuration.
***********************************************************************************
The :mod:`tacacs_server_create` util supports creating a TACACS+ \
server configuration.

This module is a stand-alone script and API that can be used to create a
TACACS+ server.

* Input:

| Infrastructure Options:

|   -i,--ipaddr=IPADDR     The IP address of the FOS switch.
|   -L,--login=LOGIN       The login name.
|   -P,--password=PASSWORD The password.
|   -f,--vfid=VFID         The VFID to which the request \
                            is directed [OPTIONAL].
|   -s,--secured=MODE      The HTTPS mode "self" or "CA" [OPTIONAL].
|   -v,--verbose           Verbose mode [OPTIONAL].

* Util Script Options:
    --server                Specifies the TACACS+ server name or IP address.
    --port                  Specifies the TACACS+ server port number.
    --timeout               Specifies the TACACS+ server timeout value.
    --authentication        Specifies the TACACS+ server authentication type.
    --secret                Specifies the TACACS+ server secret type.
    --encryption            Specifies the TACACS+ server encryption type.

* Output:
    * A success response or a dictionary in case of error.

"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_security import tacacs_server
from pyfos.utils import brcd_util


def main(argv):
    filters = ["server", "port", "timeout", "authentication",
               "secret", "encryption_type"]
    inputs = brcd_util.parse(argv, tacacs_server, filters)

    tacacs_obj = inputs['utilobject']
    if tacacs_obj.peek_server() is None:
        print("Missing command line options")
        print(inputs['utilusage'])
        exit(1)

    # Login to switch
    session = brcd_util.getsession(inputs)

    result = tacacs_obj.post(session)
    pyfos_util.response_print(result)

    # Log out
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
