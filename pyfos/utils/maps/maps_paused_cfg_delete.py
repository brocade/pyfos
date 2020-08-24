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

:mod:`maps_paused_cfg_delete` - PyFOS util to continue MAPS monitoring \
for members.
************************************************************************************

This script is used to continue MAPS monitoring for members.
Supported members are ports, SFPs, and circuits.

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
    --group-type          Specifies the group. \
                             'all' indicates complete supported groups \
                             to be paused or restarted.
    --members-member      Sets the members (separated by ";") on which to \
                             pause or continue MAPS monitoring. \
                             'all' indicates complete group specified \
                             to be puased or restarted.

* Output:
    * A success response or a dictionary in case of error.

"""


import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_maps import paused_cfg
from pyfos.utils import brcd_util


def main(argv):

    filters = ["group_type", "members_member"]
    inputs = brcd_util.parse(argv, paused_cfg, filters)

    pause_obj = inputs['utilobject']
    if (pause_obj.peek_group_type() is None or
            pause_obj.peek_members_member() is None):
        print("Missing command line options")
        print(inputs['utilusage'])
        exit(1)

    # Login to switch
    session = brcd_util.getsession(inputs)

    result = pause_obj.delete(session)
    pyfos_util.response_print(result)

    # Log out
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
