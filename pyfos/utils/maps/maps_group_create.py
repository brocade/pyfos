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

:mod:`maps_group_create` - PyFOS util to create a MAPS group.
*******************************************************************************

This script is used to create a MAPS group and add members to an \
existing group.

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

    --name                 Specifies the group name.
    --group-type           Sets the group type (not required when \
                            adding members).
    --group-feature        Sets the group feature name (required for \
                            dynamic groups).
    --feature-pattern      Sets the feature pattern value (required for \
                            dynamic groups).
    --members-member       Sets the member string (required for static groups).

* Output:

    * A success response or a dictionary in case of error.

"""


import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_maps import group
from pyfos.utils import brcd_util


def main(argv):

    filters = ["name", "group_type", "group_feature",
               "feature_pattern", "members_member"]
    inputs = brcd_util.parse(argv, group, filters)

    grp_obj = inputs['utilobject']
    if grp_obj.peek_name() is None:
        print("Missing command line options")
        print(inputs['utilusage'])
        exit(1)

    # Login to switch
    session = brcd_util.getsession(inputs)

    result = grp_obj.post(session)
    pyfos_util.response_print(result)

    # Log out
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
