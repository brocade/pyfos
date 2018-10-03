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

:mod:`sshutil_delete`-PyFOS util to delete public/private/host key, known host
*******************************************************************************
The :mod:`sshutil_delete` provides option to delete public/private/host key or
          known hosts.

This module can be used to delete public/private/host key or to delete known
          hosts in a switch.

* inputs:

| Infrastructure options:

  | -i,--ipaddr=IPADDR     IP address of FOS switch.
  | -L,--login=LOGIN       login name.
  | -P,--password=PASSWORD password.
  | -f,--vfid=VFID         VFID to which the request is directed to [OPTIONAL].
  | -s,--secured=MODE      HTTPS mode "self" or "CA" [OPTIONAL].
  | -v,--verbose           verbose mode[OPTIONAL].

| Util scripts options:

  |    --algorithm-type=ALGO    Algorithm type
  |    --key-type=TYPE          Key Type


* outputs:
    * Status of the delete operation

.. function:: sshutil_delete.del_members(session, key_type, algo_type)

    * Delete public/private/host key or known hosts.

        Example usage of the method::

            # Example 1: delete public key
            ret = sshutil_delete.del_public_keys(
                      session, "public-private-key", "rsa")
            print (ret)

            # Example 2: delete host key
            ret = sshutil_delete.del_host_key(session, "host-key", "rsa")
            print (ret)

        Details::

            sshutil_obj = sshutil_key()
            sshutil_obj.del_public_keys(session, "user")
                sshutil_obj.delete_private_key()
                sshutil_obj.delete_host_key(algo_type)

         result = sshutil_obj.delete(session)

        * inputs:
            :param session: session returned by login.
            :param algorithm-type: Algorithm type
            :param key-type: key type

        * outputs:
            :rtype: dictionary of return status matching rest response

        *use cases*

        1. Delete private key
        2. delete host key

"""

import sys
import pyfos.pyfos_auth as pyfos_auth
import pyfos.pyfos_util as pyfos_util
from pyfos.pyfos_brocade_security import sshutil_key
import pyfos.utils.brcd_util as brcd_util


def _sshutil_del(session, restobject):
    return restobject.delete(session)


def del_key(session, key_type, algo_type):
    sshutil_obj = sshutil_key()
    sshutil_obj.set_key_type(key_type)
    sshutil_obj.set_algorithm_type(algo_type)

    result = _sshutil_del(session, sshutil_obj)
    return result


def main(argv):

    # Print arguments
    # print(sys.argv[1:])

    filters = ['key_type', 'algorithm_type']
    inputs = brcd_util.parse(argv, sshutil_key, filters)

    sshutil_obj = inputs['utilobject']

    if (sshutil_obj.peek_key_type() is None or
       sshutil_obj.peek_algorithm_type() is None):
            print("Missing input(s)")
            print(inputs['utilusage'])
            sys.exit()

    session = brcd_util.getsession(inputs)

    # pyfos_util.response_print(inputs['utilobject'].displaycustomcli())
    result = _sshutil_del(inputs['session'], sshutil_obj)
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
