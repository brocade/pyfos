#!/usr/bin/env python3

# Copyright 2017 Brocade Communications Systems LLC.  All rights reserved.
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

:mod:`trunk_show_all` - PyFOS util for getting data about all E_Port trunks \
present in the switch.
********************************************************************************************************
The :mod:`trunk_show_all` - PyFOS util for getting data about all E_Port trunks \
present  in the switch.

This module is a standalone script that can be used to get the data about all \
E_Port trunks present in the switch.

* Input:

| Infrastructure Options:

|   -i,--ipaddr=IPADDR     The IP address of the FOS switch.
|   -L,--login=LOGIN       The login name.
|   -P,--password=PASSWORD The password.
|   -f,--vfid=VFID         The VFID to which the request is \
                           directed [OPTIONAL].
|   -s,--secured=MODE      The HTTPS mode "self" or "CA" [OPTIONAL].
|   -v,--verbose           Verbose mode [OPTIONAL].

* Util Scripts Options:

* Output:
    * Python dictionary content with RESTCONF response data.

"""

import sys
from pyfos import pyfos_auth
from pyfos.pyfos_brocade_fibrechannel_trunk import trunk
from pyfos import pyfos_util
from pyfos.utils import brcd_util


def usage():
    print("usage:")
    print('trunk_show_all.py -i <ipaddr> ')


def main(argv):
    filters = []
    inputs = brcd_util.parse(argv, trunk, filters)

    session = brcd_util.getsession(inputs)

    result = trunk.get(session)
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
