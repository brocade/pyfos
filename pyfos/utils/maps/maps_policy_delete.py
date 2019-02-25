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

:mod:`maps_policy_delete` - PyFOS util to delete a MAPS policy.
*******************************************************************************


This script is used to delete rules in a MAPS policy or to delete a \
MAPS policy.
If a rule list is provided in the input, then those rules are deleted from
the specified policy.
If the rule list is empty, then the MAPS policy is deleted.

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
   --rule-list           Sets the rule list in the MAPS policy.

* Output:
    * A success response or a dictionary in case of error.


"""


import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_maps import maps_policy
from pyfos.utils import brcd_util


def main(argv):

    filters = ["name", "rule_list_rule"]
    inputs = brcd_util.parse(argv, maps_policy, filters)

    maps_obj = inputs['utilobject']
    if maps_obj.peek_name() is None:
        print("Missing command line options")
        print(inputs['utilusage'])
        exit(1)

    # Login to switch
    session = brcd_util.getsession(inputs)

    result = maps_obj.delete(session)
    pyfos_util.response_print(result)

    # Log out
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
