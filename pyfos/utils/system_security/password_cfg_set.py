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
:mod:`password_cfg_set` - PyFOS util to change password config parameters.
******************************************************************************
This module is a standalone script and API that can be used to change
password config paramters.

* inputs:

| Infrastructure options:

|   -i,--ipaddr=IPADDR     IP address of FOS switch.
|   -L,--login=LOGIN       login name.
|   -P,--password=PASSWORD password.
|   -f,--vfid=VFID         VFID to which the request is directed to [OPTIONAL].
|   -s,--secured=MODE      HTTPS mode "self" or "CA" [OPTIONAL].
|   -v,--verbose           verbose mode[OPTIONAL].

* Util scripts options:
    --password-action			actions to be performed
    --minimum-length			minumum length of the password
    --character-set			minimum criteria of character set
    --user-name-allowed			can username be used in the password
    --min-lower-case-char		minimum lowercase alphabetic characters
    --min-upper-case-char		minimum uppercase alphabetic characters
    --min-numeric-char			minimum numeric digits
    --min-special-char			minimum special characters
    --past-password-history		number of past password values that are disallowed
    --min-password-age			Set the minimum number of days before which the password cannot be modified
    --max-password-age			Set the maximum number of days after which the password should be modified
    --warn-on-expire			number of days to display warning message till password expiration
    --lock-out-threshold		max number of login attempts before locking the account
    --lock-out-duration			duration, in minutes to wait and unlock the locked account
    --admin-lock-out-enabled		enable/disable admin lockout
    --repeat-char-limit			max length of repeated character sequences that is disallowed
    --sequence-character-limit		length of sequential character sequences that is disallowed
    --reverse-user-name-allowed		allow/disallow reverse string of the username as password
    --hash-type				Sets the hash type.
    --manual-hash-enabled		password change due to hash change is manually enforced
    --enforce-expire			enforce password to expire
    --min-diff				minimum difference between old and new password

* outputs:
    * success response or dictionary in case of error.

"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_security import password_cfg
from pyfos.utils import brcd_util


def main(argv):
    filters = ["minimum_length", "character_set", "user_name_allowed",
               "minimum_lower_case_character",
               "minimum_upper_case_character",
               "minimum_numeric_character",
               "minimum_special_character",
               "past_password_history",
               "minimum_password_age",
               "maximum_password_age",
               "warn_on_expire",
               "lock_out_threshold",
               "lock_out_duration",
               "admin_lock_out_enabled",
               "repeat_character_limit",
               "sequence_character_limit",
               "reverse_user_name_allowed",
               "hash_type",
               "manual_hash_enabled",
               "enforce_expire",
               "password_action", "minimum_difference"]

    inputs = brcd_util.parse(argv, password_cfg, filters)

    password_cfg_obj = inputs['utilobject']

    if (password_cfg_obj.peek_password_action() is None and
            password_cfg_obj.peek_minimum_length() is None and
            password_cfg_obj.peek_character_set() is None and
            password_cfg_obj.peek_user_name_allowed() is None and
            password_cfg_obj.peek_minimum_lower_case_character() is None and
            password_cfg_obj.peek_minimum_upper_case_character() is None and
            password_cfg_obj.peek_minimum_numeric_character() is None and
            password_cfg_obj.peek_minimum_special_character() is None and
            password_cfg_obj.peek_past_password_history() is None and
            password_cfg_obj.peek_lock_out_threshold() is None and
            password_cfg_obj.peek_lock_out_duration() is None and
            password_cfg_obj.peek_admin_lock_out_enabled() is None and
            password_cfg_obj.peek_repeat_character_limit() is None and
            password_cfg_obj.peek_sequence_character_limit() is None and
            password_cfg_obj.peek_reverse_user_name_allowed() is None and
            password_cfg_obj.peek_minimum_password_age() is None and
            password_cfg_obj.peek_maximum_password_age() is None and
            password_cfg_obj.peek_warn_on_expire() is None and
            password_cfg_obj.peek_minimum_difference() is None and
            password_cfg_obj.peek_enforce_expire() is None):
        print("Missing command line options")
        print(inputs['utilusage'])
        exit(1)
    elif (password_cfg_obj.peek_password_action() == "hash-config" and
          password_cfg_obj.peek_hash_type() is None and
          password_cfg_obj.peek_manual_hash_enabled() is None):
        print("Missing command line options")
        print(inputs['utilusage'])
        exit(1)
    elif (password_cfg_obj.peek_password_action() == "default" or
          password_cfg_obj.peek_password_action() == "delete-all"):
        pass

    session = brcd_util.getsession(inputs)

    result = password_cfg_obj.patch(session)
    pyfos_util.response_print(result)

    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
