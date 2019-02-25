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

:mod:`user_specific_password_cfg_show` - PyFOS util to display user specific \
password configurations
****************************************************************************************************
This module is a standalone script and API that can be used to display
user specific password config paramters.

* inputs:

| Infrastructure options:

|   -i,--ipaddr=IPADDR     IP address of FOS switch.

|   -L,--login=LOGIN       login name.

|   -P,--password=PASSWORD password.

|   -f,--vfid=VFID         VFID to which the request is directed to [OPTIONAL].

|   -s,--secured=MODE      HTTPS mode "self" or "CA" [OPTIONAL].

|   -v,--verbose           verbose mode[OPTIONAL].


* Util scripts options:



* outputs:
    * success response or dictionary in case of error.

"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_security import user_specific_password_cfg
from pyfos.utils import brcd_util


def main(argv):
    filters = []
    inputs = brcd_util.parse(argv, user_specific_password_cfg, filters)

    # Login to switch
    session = brcd_util.getsession(inputs)

    # Print Password configuration attributes
    result = user_specific_password_cfg.get(inputs['session'])
    pyfos_util.response_print(result)

    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
