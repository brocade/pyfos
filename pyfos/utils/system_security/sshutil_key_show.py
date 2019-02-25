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

:mod:`sshutil_key_show` - PyFOS util for displaying the SSH host key \
on a switch.
***********************************************************************************
The :mod:`sshutil_key_show` util provides the option to display the \
SSH host key information.

This module can be used to display the SSH host key information. If the user \
name is not provided, all SSH-related information is displayed.

* Input:

| Infrastructure Options:

|   -i,--ipaddr=IPADDR     The IP address of the FOS switch.
|   -L,--login=LOGIN       The login name.
|   -P,--password=PASSWORD The password.
|   -s,--secured=MODE      The HTTPS mode "self" or "CA" [OPTIONAL].
|   -v,--verbose           Verbose mode [OPTIONAL].

* Util Script Options:

  |    --algorithm-type=ALGO-TYPE      Sets the algorithm type (rsa/dsa/ecdsa).
  |    --key-type=KEY-TYPE             Sets the key type \
                                         (public-private-key or host-key).


* Output:
    * The information related to the SSH key.

.. function:: sshutil_show.show_system_security_sshutil_key(session)

    * Displays the SSH host key information in the switch.

        Example Usage of the Method:

            ret = sshutil_show.show_system_security_sshutil_key(session, \
algo_type, key_type)
            print (ret)

        Details::

            result = sshutil_show.show_system_security_sshutil(
              session, \'algo_type\', \'key_type\')

        * Input:
            :param session: The session returned by the login.
            :param algo_type: The algorithm type of the host key.
            :param key_type: The key type.

        * Output:
            :rtype: A dictionary of return status matching the REST response.

        *Use Cases*

        1. Retrieve the SSH host key.


"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_security import sshutil_key
from pyfos.utils import brcd_util


def _get_sshutil_key(session, restobject, userinput):
    return restobject.get(session, userinput)


def show_system_security_sshutil_key(session, userinput):
    sshutil_obj = sshutil_key()
    result = _get_sshutil_key(session, sshutil_obj, userinput)
    return result


def main(argv):
    # Print arguments
    # print(sys.argv[1:])

    filters = ['key_type', 'algorithm_type']
    inputs = brcd_util.parse(argv, sshutil_key, filters)

    sshutil_obj = inputs['utilobject']

    session = brcd_util.getsession(inputs)

    if (sshutil_obj.peek_algorithm_type() is None or
            sshutil_obj.peek_key_type() is None):
        print("missing input(s)")
        print(inputs['utilusage'])
        sys.exit()

    userinput = {"algorithm-type": sshutil_obj.peek_algorithm_type(),
                 "key-type": sshutil_obj.peek_key_type()}

    result = show_system_security_sshutil_key(
        inputs['session'], userinput)
    pyfos_util.response_print(result)

    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
