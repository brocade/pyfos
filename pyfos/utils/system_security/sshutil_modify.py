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

:mod:`sshutil_modify` - PyFOS util to modify the allowed user and \
rekey interval.
**************************************************************************************
The :mod:`sshutil_modify` util is used to modify the allowed user and \
rekey interval.

This module is a stand-alone script that can be used to modify the public key,
allowed user, and rekey interval value.

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

  |    --user-name=USERNAME        Specifies the user name.
  |    --rekey-interval=INTERVAL   Sets the rekey interval value.

* Output:

    * The status of the sshutil modify operation.

.. function:: sshutil_modify.change_allowed_user(
                 session, user_name, rekey_interval)

    * Changes the allowed user name in a switch.

        Example Usage of the Method::

            ret = sshutil_modify.change_allowed_user(session, USERNAME)
            print (ret)

        Details::

            class SSHUTIL:
                USERNAME = root

            sshutil_obj = sshutil()
            sshutil_obj.change_allowed_user(session, user_name)
            result = sshutil_obj.patch(session)

        * Input:
            :param session: The session returned by the login.
            :param user-name: The user name.

        * Output:
            :rtype: A dictionary of return status matching the REST response.

        *Use Cases*

        1. Change the allowed user name for performing SSH operations.

.. function:: sshutil_modify.change_rekey_interval(session, rekey_interval)

    * Changes the rekey interval.

        Example Usage of the Method::

            ret = sshutil_modify.change_rekey_interval(session, REKEY)
            print (ret)

        Details::

            class SSHUTIL:
                INTERVAL = 990

            sshutil_obj = sshutil()
            sshutil_obj.change_rekey_interval(session, rekey_interval)
            result = sshutil_obj.patch(session)

        * Input:
            :param session: The session returned by the login.
            :param rekey-interval: The rekey interval duration.

        * Output:
            :rtype: A dictionary of return status matching the REST response.

        *Use Cases*

        1. Modify the rekey interval.

    """

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_security import sshutil
from pyfos.utils import brcd_util


def _sshutil(session, restobject):
    return restobject.patch(session)


def change_allowed_user(session, user_name):
    sshutil_obj = sshutil()
    sshutil_obj.set_sshutil_operation("allow-user-name")
    sshutil_obj.set_user_name(user_name)

    result = _sshutil(session, sshutil_obj)
    return result


def change_rekey_interval(session, rekey_interval):
    sshutil_obj = sshutil()
    sshutil_obj.set_sshutil_operation("rekey-interval")
    sshutil_obj.set_interval(rekey_interval)

    result = _sshutil(session, sshutil_obj)
    return result


def main(argv):

    # Print arguments
    # print(sys.argv[1:])

    filters = ['allow_user_name', 'rekey_interval']
    inputs = brcd_util.parse(argv, sshutil, filters)

    sshutil_obj = inputs['utilobject']

    # using variables instead of calling functions as the
    # function names are lengthy and difficult to fit the
    # the line length less than 80 chars for flake8.

    if sshutil_obj.peek_rekey_interval() is None:
        if sshutil_obj.peek_allow_user_name() is None:
            print("Missing input(s)")
            print(inputs['utilusage'])
            sys.exit()

    session = brcd_util.getsession(inputs)

    # pyfos_util.response_print(inputs['utilobject'].displaycustomcli())
    result = _sshutil(inputs['session'], inputs['utilobject'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
