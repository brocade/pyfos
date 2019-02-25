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
:mod:`maps_policy_show` - PyFOS util to display a MAPS policy.
***************************************************************\
*********************************

* Input:

* Infrastructure Options:

    * -i,--ipaddr=IPADDR     The IP address of the FOS switch.
    * -L,--login=LOGIN       The login name.
    * -P,--password=PASSWORD The password.
    * -f,--vfid=VFID         The VFID to which the request is \
                             directed [OPTIONAL].
    * -s,--secured=MODE      The HTTPS mode "self" or "CA" [OPTIONAL].
    * -v,--verbose           Verbose mode [OPTIONAL].

* Util Script Options:
   --name                 Specifies a MAPS policy.

* Output:
    If a policy name is entered, then all rules within the policy \
    are displayed.
    Otherwise, all policies present in the switch and its rules \
    are displayed.
"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_maps import maps_policy
from pyfos.utils import brcd_util


def show_maps_policy(session, maps_policy_object):
    name = maps_policy_object.peek_name()
    result = maps_policy_object.get(session, name)
    return result


def main(argv):

    filters = ['name']
    inputs = brcd_util.parse(argv, maps_policy, filters)
    maps_policy_object = inputs['utilobject']

    session = brcd_util.getsession(inputs)
    result = show_maps_policy(session, maps_policy_object)
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
