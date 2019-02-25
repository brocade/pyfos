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
:mod:`seccryptocfgtemplate_show` - PyFOS util to display cryptographic \
templates
********************************************************************************
The :mod:`seccryptocfgtemplate_show` util supports the 'seccryptocfg' CLI \
use case.

This module is a stand-alone script and API that can be used to display
cryptographic templates.

* Input:

| Infrastructure Options:

|   -i,--ipaddr=IPADDR     The IP address of the FOS switch.
|   -L,--login=LOGIN       The login name.
|   -P,--password=PASSWORD The password.
|   -f,--vfid=VFID         The VFID to which the request \
                            is directed [OPTIONAL].
|   -s,--secured=MODE      The HTTPS mode "self" or "CA" [OPTIONAL].
|   -v,--verbose           Verbose mode [OPTIONAL].

* Output:
    * The cryptographic templates or a dictionary in case of error.
"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_security import sec_crypto_cfg_template
from pyfos.utils import brcd_util


def main(argv):
    filters = ["name"]
    inputs = brcd_util.parse(argv, sec_crypto_cfg_template, filters)

    # Login to switch
    session = brcd_util.getsession(inputs)

    show_obj = inputs['utilobject']
    if show_obj.peek_name() is None:
        sec_crypto_templates = sec_crypto_cfg_template.get(inputs['session'])
    else:
        sec_crypto_templates = sec_crypto_cfg_template.get(
            inputs['session'], show_obj.peek_name())

    pyfos_util.response_print(sec_crypto_templates)

    # Session logout
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
