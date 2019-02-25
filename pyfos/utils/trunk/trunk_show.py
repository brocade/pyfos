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

:mod:`trunk_show` - PyFOS util for getting data about \
an E_Port trunk group.
***********************************************************************************
The :mod:`trunk_show` - PyFOS util for getting data about \
an E_Port trunk group.

This module is a stand-alone script that can be used to get data about \
an E_Port trunk group.

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
    --group=VALUE          The group index of the E_Port trunk group.
    --source_port=VALUE    The source port of the E_Port trunk group.

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
    print('portcfgmirrorport.py -i <ipaddr> --name <name> --enable/--disable')


def main(argv):
    filters = ["group", "source_port"]
    inputs = brcd_util.parse(argv, trunk, filters)

    fcObject = inputs['utilobject']
    if fcObject.peek_group() is None:
        print("Missing group index in inputs:")
        print(inputs['utilusage'])
        sys.exit(1)

    if fcObject.peek_source_port() is None:
        print("Missing source port in inputs:")
        print(inputs['utilusage'])
        sys.exit(1)

    session = brcd_util.getsession(inputs)
    result = fcObject.getInstances(session)
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
