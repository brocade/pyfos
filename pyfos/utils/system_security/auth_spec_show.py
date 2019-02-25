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

:mod:`auth_spec_show` - PyFOS util to show the authentication mode \
configuraion.
*********************************************************************************
The :mod:`auth_spec_show` util shows the authentication mode configuraion.

This module is a stand-alone script and API that can be used to display the
authentication mode configuraion.

* Input:

| Infrastructure Options:

|   -i,--ipaddr=IPADDR     The IP address of the FOS switch.
|   -L,--login=LOGIN       The login name.
|   -P,--password=PASSWORD The password.
|   -f,--vfid=VFID         The VFID to which the request is directed [OPTIONAL]
|   -s,--secured=MODE      The HTTPS mode "self" or "CA" [OPTIONAL].
|   -v,--verbose           Verbose mode [OPTIONAL].

* Output:
    * Display the authentication mode configuraion.

"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_security import auth_spec
from pyfos.utils import brcd_util


def main(argv):
    filters = []
    inputs = brcd_util.parse(argv, auth_spec, filters)

    # Login to switch
    session = brcd_util.getsession(inputs)

    # Print Authentication mode attributes
    mode_attributes = auth_spec.get(inputs['session'])
    pyfos_util.response_print(mode_attributes)

    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
