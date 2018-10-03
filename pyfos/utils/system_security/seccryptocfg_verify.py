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

:mod:`seccryptocfg_verify_set` - PyFOS util to verify applied template
*******************************************************************************
The :mod:`seccryptocfg` supports 'seccryptocfg' CLI use case.

This module is a standalone script and API that can be used to verify the
applied templates.

* inputs:

| Infrastructure options:

|   -i,--ipaddr=IPADDR     IP address of FOS switch.
|   -L,--login=LOGIN       login name.
|   -P,--password=PASSWORD password.
|   -f,--vfid=VFID         VFID to which the request is directed to [OPTIONAL].
|   -s,--secured=MODE      HTTPS mode "self" or "CA" [OPTIONAL].
|   -v,--verbose           verbose mode[OPTIONAL].

* Util scripts options:
    --action                   set cryptographic action to perform
    --template-name            set template name

* outputs:
    * success response or dictionary in case of error

"""

import sys
import pyfos.pyfos_auth as pyfos_auth
import pyfos.pyfos_util as pyfos_util
from pyfos.pyfos_brocade_security import sec_crypto_cfg_template_action
import pyfos.utils.brcd_util as brcd_util


def main(argv):
    filters = ["template_name", "action"]
    inputs = brcd_util.parse(argv, sec_crypto_cfg_template_action, filters)

    crypto_obj = inputs['utilobject']

    if crypto_obj.peek_action() is None:
        print("Missing command line options")
        print(inputs['utilusage'])
        exit(1)

    if crypto_obj.peek_template_name() is None:
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
