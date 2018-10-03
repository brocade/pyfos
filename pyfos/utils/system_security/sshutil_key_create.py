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

:mod:`sshutil_create` - PyFOS util for creating host or public/private key pair
*******************************************************************************
The :mod:`sshutil_create` provides option to generate host, public/private key

This module can be used to enerate public/private key pair and to
generate host key.

* inputs:

|  Infrastructure options:

  |   -i,--ipaddr=IPADDR     IP address of FOS switch

  |   -L,--login=LOGIN         login name.

  |   -P,--password=PASSWORD password.

  |   -s,--secured=MODE      HTTPS mode "self" or "CA" [OPTIONAL].

  |   -v,--verbose           verbose mode[OPTIONAL].


|  Util scripts options:

  |    --algorithm-type=ALGO	Algorithm type

  |    --key-type=TYPE   	Key type

  |    --passphrase=PASS     	Passphrase



* outputs:

    * Status of the key generate operation


.. function:: sshutil_create.generate_key(
                  session, algorithm_type, key_type, passphrase)


    * Generate public/private key or host key


        Example usage of the method::

            ret = sshutil_create.generate_keys(session, "rsa", \
"public-private-key", "pray4green")
            print (ret)

            ret =  sshutil_create.generate_host_key(session, "host-key", "rsa")
            print (ret)

        Details::

            sshutil_obj = sshutil_key()
            shutil.generate_keys(session, "rsa", "public-private-key", \
"pray4green")
            sshutil_create.generate_host_key(session, "rsa", "host-key")

            result = portgroup_obj.post(session)

        * inputs:
            :param Algorithm-type: Algorithm type
            :param passphrase: 	passphrase.

        * outputs:
            :rtype: dictionary of return status matching rest response

        *use cases*

        1. Generate public/private keys
        2. Generate host key

"""

import sys
import pyfos.pyfos_auth as pyfos_auth
import pyfos.pyfos_util as pyfos_util
from pyfos.pyfos_brocade_security import sshutil_key
import pyfos.utils.brcd_util as brcd_util


def _gen_key(session, restobject):
    return restobject.post(session)


def gen_key(session, algorithm_type, passphrase, key_type):
    sshutil_obj = sshutil_key()
    sshutil_obj.set_algorithm_type(algorithm_type)
    sshutil_obj.set_key_type(key_type)
    if (passphrase is not None):
        sshutil_obj.set_passphrase(passphrase)

    result = _gen_key(session, sshutil_obj)
    return result


def main(argv):

    # Print arguments
    # print(sys.argv[1:])

    filters = ['algorithm_type', 'passphrase', 'key_type']
    inputs = brcd_util.parse(argv, sshutil_key, filters)

    sshutil_obj = inputs['utilobject']

    if (sshutil_obj.peek_algorithm_type() is None or
       sshutil_obj.peek_key_type() is None):
            print("Missing input(s)")
            print(inputs['utilusage'])
            sys.exit()

    session = brcd_util.getsession(inputs)

    result = gen_key(inputs['session'], sshutil_obj.peek_algorithm_type(),
                     sshutil_obj.peek_passphrase(),
                     sshutil_obj.peek_key_type())
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
