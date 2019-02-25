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

:mod:`license_show` - PyFOS util to show installed licenses  on a switch.
*************************************************************************
The :mod:`license_show` provides option to display installed licenses on a
switch.

This module is a standalone script that can be used to display installed
licenses on a switch.

* inputs:

| Infrastructure options:

  | -i,--ipaddr=IPADDR     IP address of FOS switch.
  | -L,--login=LOGIN       login name.
  | -P,--password=PASSWORD password.
  | -f,--vfid=VFID         VFID to which the request is directed to [OPTIONAL].
  | -s,--secured=MODE      HTTPS mode "self" or "CA" [OPTIONAL].
  | -v,--verbose           verbose mode[OPTIONAL].

* outputs:
    * Information of  all installed licenses on the switch.

"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.utils import brcd_util
# pylint: disable=W0622
from pyfos.pyfos_brocade_license import license


def get_license_info(session):
    license_obj = license()
    result = license_obj.get(session)
    return result


def main(argv):

    # Print arguments
    # print(sys.argv[1:])

    filters = []
    inputs = brcd_util.parse(argv, license, filters)

    session = brcd_util.getsession(inputs)

    result = get_license_info(inputs['session'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
