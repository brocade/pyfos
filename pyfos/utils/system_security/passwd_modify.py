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

:mod:`passwd_modify` - PyFOS util to change password
***************************************************************************************
The :mod:`passwd_modify` provides options to change passord for a
                         specified user.

This module is a standalone script that can be used to change password.

* inputs:

| Infrastructure options:

  | -i,--ipaddr=IPADDR     IP address of FOS switch.
  | -L,--login=LOGIN       login name.
  | -P,--password=PASSWORD password.
  | -f,--vfid=VFID         VFID to which the request is directed to [OPTIONAL].
  | -s,--secured=MODE      HTTPS mode "self" or "CA" [OPTIONAL].
  | -v,--verbose           verbose mode[OPTIONAL].

| Util scripts options:

  |    --user-name=USERNAME             User Name
  |    --old-password=PASSWD            Current password
  |    --new-password=PASSWD            New password

* outputs:

    * Status of the passwd change operation

.. function:: passwd_modify.change_password(
                  session, user_name, old_password, new_password)

    * Change password for a given user

        Example usage of the method::

            ret = passwd_modify.change_password(session, USERNAME, PASSWORD, \
PASSWORD)
            print (ret)

        Details::

            class PASSWD:
                USERNAME = root
                PASSWORD = pray4green
                PASSWORD = go4green

            passwd_obj = password()
            passwd_obj.change_password(session, user_name, old_password, \
new_password)
            result = sshutil_obj.patch(session)

        * inputs:
            :param session: session returned by login.
            :param user-name: user name.
            :param old-password: existing password of the user
            :param new-password: New password

        * outputs:
            :rtype: dictionary of return status matching rest response

        *use cases*

        Change password for a specified user.
"""

import sys
import pyfos.pyfos_auth as pyfos_auth
import pyfos.pyfos_util as pyfos_util
from pyfos.pyfos_brocade_security import password
import pyfos.utils.brcd_util as brcd_util


def _change_password(session, restobject):
        return restobject.patch(session)


def change_password(session, user_name, old_password, new_password):
    passwd_obj = password()
    passwd_obj.set_user_name(user_name)
    passwd_obj.set_new_password(new_password)
    passwd_obj.set_old_password(old_password)
    result = _change_password(session, passwd_obj)
    return result


def main(argv):

    # Print arguments
    # print(sys.argv[1:])

    filters = ['user_name', 'old_password', 'new_password']
    inputs = brcd_util.parse(argv, password, filters)

    passwd_obj = inputs['utilobject']

    if (passwd_obj.peek_user_name() is None and
            passwd_obj.peek_new_password() is None):
            print("Missing input(s)")
            print(inputs['utilusage'])
            sys.exit()
    session = brcd_util.getsession(inputs)

    # pyfos_util.response_print(inputs['utilobject'].displaycustomcli())
    result = _change_password(inputs['session'], inputs['utilobject'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
        main(sys.argv[1:])
