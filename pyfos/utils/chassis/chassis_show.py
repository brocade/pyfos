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

:mod:`chassis_show` - PyFOS util for specific chassis op use case.
************************************************************************
The :mod:`chassis_show` provides for specific chassis op use case.

This module is a standalone script that can be used to display chassis
attributes

* inputs:

| Infrastructure options:

  | -i,--ipaddr=IPADDR     IP address of FOS switch.
  | -L,--login=LOGIN       login name.
  | -P,--password=PASSWORD password.
  | -f,--vfid=VFID         VFID to which the request is directed to [OPTIONAL].
  | -s,--secured=MODE      HTTPS mode "self" or "CA" [OPTIONAL].
  | -v,--verbose           verbose mode[OPTIONAL].

* outputs:
    * Python dictionary content with RESTCONF response data

"""

import sys
import pyfos.pyfos_auth as pyfos_auth
import pyfos.pyfos_util as pyfos_util
from pyfos.pyfos_brocade_chassis import chassis
import pyfos.utils.brcd_util as brcd_util


def show_chassis_details(session):
    chassis_obj = chassis()
    result = chassis_obj.get(session)
    return result


def main(argv):

    # Print arguments
    # print(sys.argv[1:])

    filters = []
    inputs = brcd_util.parse(argv, chassis, filters)

    session = brcd_util.getsession(inputs)

    result = show_chassis_details(inputs['session'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
