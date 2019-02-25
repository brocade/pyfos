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

:mod:`radius_server_set` - PyFOS util to modify a RADIUS server configuration.
*******************************************************************************
The :mod:`radius_server_set` util supports modifying a RADIUS \
server configuration.

This module is a stand-alone script and API that can be used to modify a
RADIUS server configuration.

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
    --server               Sets the RADIUS server name or IP address.
    --port                 Sets the RADIUS server port number.
    --timeout              Sets the RADIUS server timeout value.
    --authentication       Sets the RADIUS server authentication type.
    --secret               Sets the RADIUS server secret type.
    --encryption-type      Sets the RADIUS server encryption type.
    --position             Sets the RADIUS server position.

* Output:
    * A success response or a dictionary in case of error.

"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_security import radius_server
from pyfos.utils import brcd_util


def main(argv):
    filters = ["server", "port", "timeout", "authentication",
               "secret", "encryption_type", "position"]
    inputs = brcd_util.parse(argv, radius_server, filters)

    radius_obj = inputs['utilobject']

    if radius_obj.peek_server() is None:
        print("Missing command line options")
        print(inputs['utilusage'])
        exit(1)

    if not (radius_obj.peek_port() or
            radius_obj.peek_timeout() or radius_obj.peek_authentication() or
            radius_obj.peek_secret() or radius_obj.peek_encryption_type() or
            radius_obj.peek_position()):
        print("Missing command line options")
        print(inputs['utilusage'])
        exit(1)

    # Login to switch
    session = brcd_util.getsession(inputs)

    result = radius_obj.patch(session)
    pyfos_util.response_print(result)

    # Log out
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
