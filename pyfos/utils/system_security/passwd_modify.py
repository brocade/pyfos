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

:mod:`passwd_modify` - PyFOS util to change a password.
***************************************************************************************
The :mod:`passwd_modify` util provides options to change a passord for a
                         specified user.

This module is a stan-dalone script that can be used to a change password.

* Input:

| Infrastructure Options:

|   -i,--ipaddr=IPADDR     The IP address of the FOS switch.
|   -L,--login=LOGIN       The login name.
|   -P,--password=PASSWORD The password.
|   -f,--vfid=VFID         The VFID to which the request \
                            is directed [OPTIONAL].
|   -s,--secured=MODE      The HTTPS mode "self" or "CA" [OPTIONAL].
|   -v,--verbose           Verbose mode [OPTIONAL].

* Util Script Options:

  |    --user-name=USERNAME             Specifies the user name.
  |    --old-password=PASSWD            Enters the current password.
  |    --new-password=PASSWD            Sets the new password.

* Output:

    * The status of the password change operation.

.. function:: passwd_modify.change_password(
                  session, user_name, old_password, new_password)

    * Change the password for a specified user

        Example Usage of the Method::

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

        * Input:
            :param session: The session returned by the login.
            :param user-name: The user name.
            :param old-password: The existing password of the user.
            :param new-password: The new password.

        * Output:
            :rtype: A dictionary of return status matching the REST response.

        *Use Cases*

        Change a password for a specified user.
"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_security import password
from pyfos.utils import brcd_util


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
