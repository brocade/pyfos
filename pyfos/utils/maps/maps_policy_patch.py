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

:mod:`maps_policy_patch` - PyFOS util to update MAPS policy
*******************************************************************************

This script is used to update the rule list in a MAPS Policy.

Note: if we use patch operation all the rules in a policy will be
replaced by what is provided in the input.
If we wish to add rules to the existing policy please use POST operation.
If we wish to delete rules from existing policy please use DELETE operation.

* inputs:

| Infrastructure options:

|   -i,--ipaddr=IPADDR     IP address of FOS switch.
|   -L,--login=LOGIN       login name.
|   -P,--password=PASSWORD password.
|   -f,--vfid=VFID         VFID to which the request is directed to [OPTIONAL].
|   -s,--secured=MODE      HTTPS mode "self" or "CA" [OPTIONAL].
|   -v,--verbose           verbose mode[OPTIONAL].

* Util scripts options:
    --name                 specify MAPS Policy
    --rule-list            Rule list inside MAPS policy

* outputs:
    * success response or dictionary in case of error.

"""


import sys
import pyfos.pyfos_auth as pyfos_auth
import pyfos.pyfos_util as pyfos_util
from pyfos.pyfos_brocade_maps import maps_policy
import pyfos.utils.brcd_util as brcd_util


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

    result = maps_obj.patch(session)
    pyfos_util.response_print(result)

    # Log out
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
