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

:mod:`sshutil_public_key_show` - PyFOS util for displaying keys on a switch.
***********************************************************************************
The :mod:`sshutil_public_key_show` util provides the option to display \
key information.

This module can be used to display key information.

* Input:

| Infrastructure Options:

|   -i,--ipaddr=IPADDR     The IP address of the FOS switch.
|   -L,--login=LOGIN       The login name.
|   -P,--password=PASSWORD The password.
|   -s,--secured=MODE      The HTTPS mode "self" or "CA" [OPTIONAL].
|   -v,--verbose           Verbose mode [OPTIONAL].

* Util Script Options:

  |    --user-name=USER-NAME    Specifies the user name.


* Output:
    * The SSH key related information.

.. function:: sshutil_show.show_system_security_sshutil(session)

    * Displays the SSH key information in the switch.

        Example Usage of the Method:

            ret = sshutil_show.show_system_security_sshutil(session, user_name)
            print (ret)

        Details::

            result = sshutil_show.show_system_security_sshutil(
              session, \'user\'')

        * Input:
            :param session: The session returned by the login.
            :param user_name: The user name for which the public keys \
                                are associated.

        * Output:
            :rtype: A dictionary of return status matching the REST response.

        *Use Cases*

        1. Retrieve the public key-related information.


"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_security import sshutil_public_key
from pyfos.utils import brcd_util


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

    if sshutil_obj.peek_user_name() is None:
        print("no input")
        print(inputs['utilusage'])
        sys.exit()

    result = show_system_security_sshutil(
        inputs['session'], sshutil_obj.peek_user_name())

    pyfos_util.response_print(result)

    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
