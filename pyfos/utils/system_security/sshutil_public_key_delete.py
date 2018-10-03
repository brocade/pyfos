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

:mod:`sshutil_public_key_delete`-PyFOS util to delete public key
*******************************************************************************
The :mod:`sshutil_public_key_delete` provides option to delete public key

This module can be used to delete public key

* inputs:

| Infrastructure options:

  | -i,--ipaddr=IPADDR     IP address of FOS switch.
  | -L,--login=LOGIN       login name.
  | -P,--password=PASSWORD password.
  | -f,--vfid=VFID         VFID to which the request is directed to [OPTIONAL].
  | -s,--secured=MODE      HTTPS mode "self" or "CA" [OPTIONAL].
  | -v,--verbose           verbose mode[OPTIONAL].

| Util scripts options:

  |    --user-name=USER    	User Name


* outputs:
    * Status of the delete operation

.. function:: sshutil_delete.del_members(session, user_name)

    * Delete public key.

        Example usage of the method::

            # Example 1: delete public key
            ret = sshutil_delete.del_public_keys(session, "user")
            print (ret)

        Details::

            sshutil_obj = sshutil()
            sshutil_obj.del_public_keys(session, "user")
                sshutil_obj.delete_public_keys(user_name)

         result = sshutil_obj.delete(session)

        * inputs:
            :param session: session returned by login.
            :param user-name: User Name.

        * outputs:
            :rtype: dictionary of return status matching rest response

        *use cases*

        1. Delete public key

"""

import sys
import pyfos.pyfos_auth as pyfos_auth
import pyfos.pyfos_util as pyfos_util
from pyfos.pyfos_brocade_security import sshutil_public_key
import pyfos.utils.brcd_util as brcd_util


def _sshutil_del(session, restobject):
    return restobject.delete(session)


def del_public_keys(session, user_name):
    sshutil_obj = sshutil_public_key()
    sshutil_obj.set_user_name(user_name)

    result = _sshutil_del(session, sshutil_obj)
    return result


def main(argv):

    # Print arguments
    # print(sys.argv[1:])

    filters = ['user_name']
    inputs = brcd_util.parse(argv, sshutil_public_key, filters)

    sshutil_obj = inputs['utilobject']

    if (sshutil_obj.peek_user_name() is None):
            print("Missing input(s)")
            print(inputs['utilusage'])
            sys.exit()

    session = brcd_util.getsession(inputs)

    # pyfos_util.response_print(inputs['utilobject'].displaycustomcli())
    # result = _sshutil_del(inputs['session'], sshutil_obj)
    result = del_public_keys(inputs['session'], sshutil_obj.peek_user_name())
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
