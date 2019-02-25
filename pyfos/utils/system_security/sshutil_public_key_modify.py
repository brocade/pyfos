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

:mod:`sshutil_public_key_modify` - PyFOS util to modify a public key.
**************************************************************************************
The :mod:`sshutil_public_key_modify` util is used to modify a public key.

This module is a stand-alone script that can be used to modify a public key.

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

  |    --user-name=USERNAME             Specifies the user name.
  |    --remote-host-ip=IP              Sets the remote host IP address.
  |    --remote-host-directory=DIR      Sets the remote host directory.
  |    --public-key-name=KEYNAME        Sets the public key name (.pub).
  |    --remote-login-user=LOGINUSER    Sets the remote login user.
  |    --remote-login-password=PASSWORD Sets the remote login password.
  |    --algorithm-type=ALGOTYPE        Sets the algorithm type.
  |    --action=OPERATION               Sets the SSHUtil operation.

* Output:

    * The status of the sshutil modify operation.

.. function:: sshutil_modify.import_export_public_key(session, user_name, \
                             remote_ip, remote_dir, pub_key_name, login_name, \
                             login_password, action, algorithm_type)

    * Import or export a specified public key from/to a remote server \
        to/from a switch.

        Example Usage of the Method::

            ret = sshutil_modify.import_export_public_key(
                      session, USERNAME, IP, DIR, KEYNAME,
                      LOGINUSER, PASSWORD, ACTION, ALGORITHM)
            print (ret)

        Details::

            class SSHUTIL:
                USERNAME = root
                IP = 10.70.4.109
                DIR = /root/ca
                KEYNAME = key.pub
                LOGINUSER = root
                PASSWORD = pray4green

            sshutil_obj = sshutil_public_key_action()
            if operation == IMPORT:
                sshutil_obj.import_export_public_key(
                    session, user_name, remote_ip, remote_dir, pub_key_name,
                    login_name, login_password, action, algo_type)

        * Input:
            :param session: The session returned by the login.
            :param user-name: The user name.
            :param remote-host-ip: The remote host IP address.
            :param remote-host-directoy: The location in the remote host for \
                                           the public key.
            :param public-key-name: The name of the public key (.pub).
            :param remote-login-user: The user name of the remote host.
            :param remote-login-password: The password of the remote host.
            :param action: The action (import or export).
            :param algorithm_type: The algorithm type.

        * Output:
            :rtype: A dictionary of return status matching the REST response.

        *Use Cases*

        1. Import a specified public key from a remote server to the switch.
        2. Export a public key from the switch to a remote server.
    """

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_security import sshutil_public_key_action
from pyfos.utils import brcd_util


def _import_export_key(session, restobject):
    return restobject.patch(session)


def import_export_public_key(session, user_name, remote_ip, remote_dir,
                             pub_key_name, login_name, login_password,
                             action, algorithm_type):
    sshutil_obj = sshutil_public_key_action()
    sshutil_obj.set_action(action)
    sshutil_obj.set_user_name(user_name)
    sshutil_obj.set_algorithm_type(algorithm_type)
    sshutil_obj.set_remote_host_ip(remote_ip)
    sshutil_obj.set_remote_dir(remote_dir)
    sshutil_obj.set_public_key_name(pub_key_name)
    sshutil_obj.set_remote_user_name(login_name)
    sshutil_obj.set_remote_user_password(login_password)

    result = _import_export_key(session, sshutil_obj)
    return result


def main(argv):

    # Print arguments
    # print(sys.argv[1:])

    filters = ['user_name', 'action', 'public_key_name', 'remote_host_ip',
               'remote_directory', 'remote_user_name', 'remote_user_password',
               'algorithm_type']
    inputs = brcd_util.parse(argv, sshutil_public_key_action, filters)

    sshutil_obj = inputs['utilobject']

    # using variables instead of calling functions as the
    # function names are lengthy and difficult to fit the
    # the line length less than 80 chars for flake8.

    if (sshutil_obj.peek_remote_host_ip() is None and
            sshutil_obj.peek_remote_directory() is None and
            sshutil_obj.peek_remote_user_name() is None and
            sshutil_obj.peek_remote_user_password() is None and
            sshutil_obj.peek_action() is None):
        print("Missing input(s)")
        print(inputs['utilusage'])
        sys.exit()

    session = brcd_util.getsession(inputs)

    # pyfos_util.response_print(inputs['utilobject'].displaycustomcli())
    result = _import_export_key(inputs['session'], inputs['utilobject'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
