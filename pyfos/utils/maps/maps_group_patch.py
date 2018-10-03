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

:mod:`maps_group_patch` - PyFOS util to update dynamic group
*******************************************************************************

+This script can be used to update dynamic groups.

* inputs:

| Infrastructure options:

|   -i,--ipaddr=IPADDR     IP address of FOS switch.
|   -L,--login=LOGIN       login name.
|   -P,--password=PASSWORD password.
|   -f,--vfid=VFID         VFID to which the request is directed to [OPTIONAL].
|   -s,--secured=MODE      HTTPS mode "self" or "CA" [OPTIONAL].
|   -v,--verbose           verbose mode[OPTIONAL].

* Util scripts options:
    --name                 specify group name
    --group-type           group type
    --group-feature        dynamic group feature name
    --feature-pattern      feature pattern value

* outputs:
    * success response or dictionary in case of error.

"""


import sys
import pyfos.pyfos_auth as pyfos_auth
import pyfos.pyfos_util as pyfos_util
from pyfos.pyfos_brocade_maps import group
import pyfos.utils.brcd_util as brcd_util


def main(argv):

    filters = ["name", "group_feature", "feature_pattern"]
    inputs = brcd_util.parse(argv, group, filters)

    grp_obj = inputs['utilobject']
    if grp_obj.peek_name() is None:
        print("Missing command line options")
        print(inputs['utilusage'])
        exit(1)

    if (grp_obj.peek_group_feature() is None or
            grp_obj.peek_feature_pattern() is None):
        print("Missing command line options")
        print(inputs['utilusage'])
        exit(1)

    # Login to switch
    session = brcd_util.getsession(inputs)

    result = grp_obj.patch(session)
    pyfos_util.response_print(result)

    # Log out
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
