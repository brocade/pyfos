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

:mod:`sshutil_public_key_show` - PyFOS util for displaying keys on a switch
***********************************************************************************
The :mod:`sshutil_public_key_show` provides option to display key information

This module can be used to display key information.

* inputs:

|  Infrastructure options:

  |   -i,--ipaddr=IPADDR     IP address of FOS switch
  |   -L,--login=LOGIN       login name.
  |   -P,--password=PASSWORD password.
  |   -s,--secured=MODE      HTTPS mode "self" or "CA" [OPTIONAL].
  |   -v,--verbose           verbose mode[OPTIONAL].

|  Util scripts options:

  |    --user-name=USER-NAME                             User Name


* outputs:
    * SSH key related information

.. function:: sshutil_show.show_system_security_sshutil(session)

    * Display the SSH key information in the switch.

        Example usage of the method:

            ret = sshutil_show.show_system_security_sshutil(session, user_name)
            print (ret)

        Details::

            result = sshutil_show.show_system_security_sshutil(
              session, \'user\'')

        * inputs:
            :param session: session returned by login.
            :param user_name: user name for which public keys are associated

        * outputs:
            :rtype: dictionary of return status matching rest response

        *use cases*

        1. Retrieve the public key related information.


"""

import sys
import pyfos.pyfos_auth as pyfos_auth
import pyfos.pyfos_util as pyfos_util
from pyfos.pyfos_brocade_security import sshutil_public_key
import pyfos.utils.brcd_util as brcd_util


def _get_sshutil_public_key(session, restobject):
    return restobject.get(session)


def show_system_security_sshutil(session, user_name):
    sshutil_obj = sshutil_public_key()
    sshutil_obj.set_user_name(user_name)
    result = _get_sshutil_public_key(session, sshutil_obj)
#    result = sshutil_obj.get(session, user_name)
    return result


def main(argv):
    # Print arguments
    # print(sys.argv[1:])

    filters = ['user_name']
    inputs = brcd_util.parse(argv, sshutil_public_key, filters)

    sshutil_obj = inputs['utilobject']

    session = brcd_util.getsession(inputs)

    if (sshutil_obj.peek_user_name() is None):
        print("no input")
        print(inputs['utilusage'])
        sys.exit()

    result = show_system_security_sshutil(
            inputs['session'], sshutil_obj.peek_user_name())

    pyfos_util.response_print(result)

    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
