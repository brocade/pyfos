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

:mod:`chassis_show` - PyFOS util to display chassis attributes.
************************************************************************
The :mod:`chassis_show` util displays chassis attributes.

This module is a stand-alone script that can be used to display chassis
attributes.

* Input:

| Infrastructure Options:

  | -i,--ipaddr=IPADDR     The IP address of the FOS switch.
  | -L,--login=LOGIN       The login name.
  | -P,--password=PASSWORD The password.
  | -f,--vfid=VFID         The VFID to which the request is \
                            directed [OPTIONAL].
  | -s,--secured=MODE      The HTTPS mode "self" or "CA" [OPTIONAL].
  | -v,--verbose           Verbose mode [OPTIONAL].

* Output:
    * Python dictionary content with RESTCONF response data.

"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_chassis import chassis
from pyfos.utils import brcd_util


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
