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

:mod:`sshutil_modify` - PyFOS util to modify allowed user, rekey interval
**************************************************************************************
The :mod:`sshutil_modify` used to modify allowed user, rekey interval.

This module is a standalone script that can be used to modify public key,
allowed user and rekey interval value.

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
  |    --rekey-interval=INTERVAL        Rekey interval value

* outputs:

    * Status of the sshutil  modify operation

.. function:: sshutil_modify.change_allowed_user(
                 session, user_name, rekey_interval)

    * Change allowed user name in a switch

        Example usage of the method::

            ret = sshutil_modify.change_allowed_user(session, USERNAME)
            print (ret)

        Details::

            class SSHUTIL:
                USERNAME = root

            sshutil_obj = sshutil()
            sshutil_obj.change_allowed_user(session, user_name)
            result = sshutil_obj.patch(session)

        * inputs:
            :param session: session returned by login.
            :param user-name: user name.

        * outputs:
            :rtype: dictionary of return status matching rest response

        *use cases*

        1. Changes the allowed user name for doing SSH operations

.. function:: sshutil_modify.change_rekey_interval(session, rekey_interval)

    * Change the rekey interval duration

        Example usage of the method::

            ret = sshutil_modify.change_rekey_interval(session, REKEY)
            print (ret)

        Details::

            class SSHUTIL:
                INTERVAL = 990

            sshutil_obj = sshutil()
            sshutil_obj.change_rekey_interval(session, rekey_interval)
            result = sshutil_obj.patch(session)

        * inputs:
            :param session: session returned by login.
            :param rekey-interval: rekey interval duration

        * outputs:
            :rtype: dictionary of return status matching rest response

        *use cases*

        1. Modifies rekey interval
    """

import sys
import pyfos.pyfos_auth as pyfos_auth
import pyfos.pyfos_util as pyfos_util
from pyfos.pyfos_brocade_security import sshutil
import pyfos.utils.brcd_util as brcd_util


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

    if (sshutil_obj.peek_rekey_interval() is None):
        if (sshutil_obj.peek_allow_user_name() is None):
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
