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

:mod:`sshutil_key_show` - PyFOS util for displaying SSH host key on a switch
***********************************************************************************
The :mod:`sshutil_key_show` provides option to display SSH host key information

This module can be used to display key information. If user name is not
provided, then all SSH related information will be displayed.

* inputs:

|  Infrastructure options:

  |   -i,--ipaddr=IPADDR     IP address of FOS switch
  |   -L,--login=LOGIN       login name.
  |   -P,--password=PASSWORD password.
  |   -s,--secured=MODE      HTTPS mode "self" or "CA" [OPTIONAL].
  |   -v,--verbose           verbose mode[OPTIONAL].

|  Util scripts options:

  |    --algorithm-type=ALGO-TYPE      rsa/dsa/ecdsa
  |    --key-type=KEY-TYPE             public-private-key or host-key


* outputs:
    * SSH key related information

.. function:: sshutil_show.show_system_security_sshutil_key(session)

    * Display the SSH host key information in the switch.

        Example usage of the method:

            ret = sshutil_show.show_system_security_sshutil_key(session, \
algo_type, key_type)
            print (ret)

        Details::

            result = sshutil_show.show_system_security_sshutil(
              session, \'algo_type\', \'key_type\')

        * inputs:
            :param session: session returned by login.
            :param algo_type: algorithm type of host key
            :param key_type: key type

        * outputs:
            :rtype: dictionary of return status matching rest response

        *use cases*

        1. Retrieve the SSH host key.


"""

import sys
import pyfos.pyfos_auth as pyfos_auth
import pyfos.pyfos_util as pyfos_util
from pyfos.pyfos_brocade_security import sshutil_key
import pyfos.utils.brcd_util as brcd_util


def _get_sshutil_key(session, restobject):
    return restobject.get(session)


def show_system_security_sshutil_key(session, key_type, algorithm_type):
    sshutil_obj = sshutil_key()
    sshutil_obj.set_key_type(key_type)
    sshutil_obj.set_algorithm_type(algorithm_type)
    result = _get_sshutil_key(session, sshutil_obj)
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

    result = show_system_security_sshutil_key(
            inputs['session'], sshutil_obj.peek_key_type(),
            sshutil_obj.peek_algorithm_type())
    pyfos_util.response_print(result)

    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
