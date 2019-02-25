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

:mod:`seccryptocfg_export_set` - PyFOS util to export a default template.
*******************************************************************************
The :mod:`seccryptocfg` util supports exporting a default template.

This module is a stand-alone script and API that can be used to export a \
default template.

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

    --action                  Sets the cryptographic action to perform.
    --template-name           Sets the default template name.
    --user-name               Sets the host machine login name.
    --host-ip                 Sets the host machine login IP address.
    --remote-user-password    Sets the host machine password in base64.
    --protocol-type           Sets the file transfer protocol type.
    --remote-directory        Sets the remote template file path.

* Output:
    * A success response or a dictionary in case of error.

"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_security import sec_crypto_cfg_template_action
from pyfos.utils import brcd_util


def main(argv):
    filters = ["template_name", "action",
               "remote_user_name", "remote_host_ip", "remote_user_password",
               "remote_directory", "file_transfer_protocol_type"]

    inputs = brcd_util.parse(argv, sec_crypto_cfg_template_action, filters)

    crypto_obj = inputs['utilobject']

    if (crypto_obj.peek_action() is None or
            crypto_obj.peek_template_name() is None or
            crypto_obj.peek_remote_user_name() is None or
            crypto_obj.peek_remote_host_ip() is None or
            crypto_obj.peek_remote_user_password() is None or
            crypto_obj.peek_remote_directory() is None or
            crypto_obj.peek_file_transfer_protocol_type() is None):
        print("Missing command line options")
        print(inputs['utilusage'])
        exit(1)

    # Login to switch
    session = brcd_util.getsession(inputs)

    result = crypto_obj.patch(session)
    pyfos_util.response_print(result)

    # Log out
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
