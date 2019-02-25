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

:mod:`sshutil_create` - PyFOS util for creating a host key or \
public/private key pair.
*******************************************************************************************
The :mod:`sshutil_create` util provides the option to generate a host key or \
public/private key pair.

This module can be used to generate a host key or public/private key pair.

* Input:

| Infrastructure Options:

|   -i,--ipaddr=IPADDR     The IP address of the FOS switch.
|   -L,--login=LOGIN       The login name.
|   -P,--password=PASSWORD The password.
|   -s,--secured=MODE      The HTTPS mode "self" or "CA" [OPTIONAL].
|   -v,--verbose           Verbose mode [OPTIONAL].


|  Util Script Options:

  |    --algorithm-type=ALGO	Sets the algorithm type.

  |    --key-type=TYPE   	Sets the key type.

  |    --passphrase=PASS     	Sets the passphrase.



* Output:

    * The status of the key generation.


.. function:: sshutil_create.generate_key(
                  session, algorithm_type, key_type, passphrase)


    * Generates a public/private key or a host key.


        Example Usage of the Method::

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

        * Input:
            :param Algorithm-type: The algorithm type.
            :param passphrase: 	The passphrase.

        * Output:
            :rtype: A dictionary of return status matching the REST response.

        *Use Cases*

        1. Generate a public/private key pair.
        2. Generate a host key.

"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_security import sshutil_key
from pyfos.utils import brcd_util


def _gen_key(session, restobject):
    return restobject.post(session)


def gen_key(session, algorithm_type, passphrase, key_type):
    sshutil_obj = sshutil_key()
    sshutil_obj.set_algorithm_type(algorithm_type)
    sshutil_obj.set_key_type(key_type)
    if passphrase is not None:
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
