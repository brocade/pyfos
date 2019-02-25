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

:mod:`port_trunk_area_show` - PyFOS util for getting info \
about a port trunk area group.
****************************************************************************************************************
The :mod:`port_trunk_area_show` - PyFOS util for getting info \
about a port trunk area group.

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
    --trunk-index=VALUE    The trunk index of the port trunk area group.

* Output:
    * Python dictionary content with RESTCONF response data.

"""

import sys
from pyfos import pyfos_auth
from pyfos.pyfos_brocade_fibrechannel_trunk import trunk_area
from pyfos import pyfos_util
from pyfos.utils import brcd_util


def usage():
    print("usage:")
    print('portcfgmirrorport.py -i <ipaddr> --name <name> --enable/--disable')


def main(argv):
    filters = ["trunk_index"]
    inputs = brcd_util.parse(argv, trunk_area, filters)

    fcObject = inputs['utilobject']
    if fcObject.peek_trunk_index() is None:
        print("Missing options in the commandline:")
        print(inputs['utilusage'])
        sys.exit(1)
    else:
        print(fcObject.peek_trunk_index())

    session = brcd_util.getsession(inputs)
    result = fcObject.get(session, fcObject.peek_trunk_index())
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
