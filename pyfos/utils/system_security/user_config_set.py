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

:mod:`user_config_set` - PyFOS util to modify an existing user account
*************************************************************************************
The :mod:`user_config_set` supports 'userconfig' CLI use case.

This module is a standalone script and API that can be used to modify a
existing user account

* inputs:

| Infrastructure options:

|   -i,--ipaddr=IPADDR     IP address of FOS switch.
|   -L,--login=LOGIN       login name.
|   -P,--password=PASSWORD password.
|   -f,--vfid=VFID         VFID to which the request is directed to [OPTIONAL].
|   -s,--secured=MODE      HTTPS mode "self" or "CA" [OPTIONAL].
|   -v,--verbose           verbose mode[OPTIONAL].

* Util scripts options:
    --name                           set name of the user
    --password-change-enforced       set to expire password
    --password                       set user password
    --account-locked                 set to unlock the specified user account
                                                            if already locked
    --role                           set user role
    --chassis-access-role            set the account's access permissions
                                         regarding chassis-level commands
    --account-description            set the description for the new account
    --account-enabled                Enable/disable a user account
    --access-start-time              set the starting time from when the
                                                        users can access
    --access-end-time                set the ending time till when the
                                                      users can access
    --home-virtual-fabric            set account's home fid
    --vf-role-id                     set virtual fabric role name and id list

* outputs:
    * success response or dictionary in case of error.

"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_security import user_config
from pyfos.utils import brcd_util


def main(argv):
    filters = ["name", "role", "home_virtual_fabric",
               "virtual_fabric_role_id_list_role_id", "account_description",
               "account_enabled", "password_change_enforced",
               "access_start_time", "access_end_time",
               "chassis_access_role", "account_locked"]
    inputs = brcd_util.parse(argv, user_config, filters)

    user_obj = inputs['utilobject']
    if user_obj.peek_name() is None:
        print("Missing command line options")
        print(inputs['utilusage'])
        exit(1)

    if (user_obj.peek_account_description() is None and
            user_obj.peek_role() is None and
            user_obj.peek_virtual_fabric_role_id_list_role_id() == "[]" and
            user_obj.peek_chassis_access_role() is None and
            user_obj.peek_account_enabled() is None and
            user_obj.peek_password_change_enforced() is None and
            user_obj.peek_home_virtual_fabric() is None and
            user_obj.peek_access_start_time() is None and
            user_obj.peek_access_end_time() is None and
            user_obj.peek_account_locked() is None):
        print("Missing command line options")
        print(inputs['utilusage'])
        exit(1)

    # Login to switch
    session = brcd_util.getsession(inputs)

    result = user_obj.patch(session)
    pyfos_util.response_print(result)

    # Log out
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
