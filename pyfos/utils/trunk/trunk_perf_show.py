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

:mod:`trunk_perf_show` - PyFOS util for getting info \
        of performance of a E-port trunk
*********************************************************************************************************************************
The :mod:`trunk_perf_show` - PyFOS util for getting info \
        of performance of a E-port trunk

This module is a standalone script that can be used to get the info \
        of performance of a E-port trunk

* inputs:

| Infrastructure options:

|   -i,--ipaddr=IPADDR     IP address of FOS switch.
|   -L,--login=LOGIN       login name.
|   -P,--password=PASSWORD password.
|   -f,--vfid=VFID         VFID to which the request is directed to [OPTIONAL].
|   -s,--secured=MODE      HTTPS mode "self" or "CA" [OPTIONAL].
|   -v,--verbose           verbose mode[OPTIONAL].

* Util scripts options:
    --group=VALUE                group of the E-Port Trunk

* outputs:
    * Python dictionary content with RESTCONF response data

"""

import sys
from pyfos import pyfos_auth
from pyfos.pyfos_brocade_fibrechannel_trunk import performance
from pyfos import pyfos_util
from pyfos.utils import brcd_util


def main(argv):
    filters = ["group"]
    inputs = brcd_util.parse(argv, performance, filters)

    fcObject = inputs['utilobject']
    if fcObject.peek_group() is None:
        print("Missing options in the commandline:")
        print(inputs['utilusage'])
        sys.exit(1)

    session = brcd_util.getsession(inputs)
    result = fcObject.get(session, fcObject.peek_group())
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
