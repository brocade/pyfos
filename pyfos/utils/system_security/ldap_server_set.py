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

:mod:`ldap_server_set` - PyFOS util to modify ldap server configuration
*******************************************************************************
The :mod:`ldap_server_create` supports 'aaaconfig' CLI use case.

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
    --server                                 set ldap server name/ip
    --port                                   set ldap server port number
    --timeout                                set ldap server timeout value
    --domain                                 set ldap server domain name
    --position                               set ldap server position
    --tls-mode                               set ldap server tls mode

* outputs:
    * success response or dictionary in case of error

"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_security import ldap_server
from pyfos.utils import brcd_util


def main(argv):
    filters = ["server", "port", "timeout", "domain", "position", "tls_mode"]

    inputs = brcd_util.parse(argv, ldap_server, filters)

    ldap_obj = inputs['utilobject']

    if ldap_obj.peek_server() is None:
        print("Missing command line options")
        print(inputs['utilusage'])
        exit(1)

    if not (ldap_obj.peek_port() or
            ldap_obj.peek_timeout() or ldap_obj.peek_domain() or
            ldap_obj.peek_position() or ldap_obj.peek_tls_mode()):
        print("Missing command line options")
        print(inputs['utilusage'])
        exit(1)

    # Login to switch
    session = brcd_util.getsession(inputs)

    result = ldap_obj.patch(session)
    pyfos_util.response_print(result)

    # Log out
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
