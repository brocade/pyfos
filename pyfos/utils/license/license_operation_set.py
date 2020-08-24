#!/usr/bin/env python3


# Copyright © 2019-2020 Broadcom. All rights reserved.
# The term “Broadcom” refers to Broadcom Inc. and/or its subsidiaries.
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


# license_operation_set.py(pyGen v1.0.0)


"""

:mod:`license_operation_set` - PyFOS util to create for\
license_parameters
*******************************************************************************
The :mod:`license_operation_set` PyFOS util to create for license_parameters


The license operation input container.

license_operation_set : usage

* Infrastructure Options:
    * -i,--ipaddr=IPADDR: The IP address of the FOS switch.
    * -L,--login=LOGIN: The login name.
    * -P,--password=PASSWORD: The password.
    * -f,--vfid=VFID: The VFID to which the request is directed.
    * -s,--secured=MODE: The HTTPS mode "self" or "CA" [Optional].
    * -v,--verbose: Verbose mode [Optional].

* Util Script Options:
    * --remote-directory=REMOTE-DIRECTORY The remote server file path from\
      which the license certificate to be transferred.
    * --license-password=PASSWORD The password for the remote server used to\
      copy the license certificate. The password must be base64 encoded.
      Refer to RFC 3414.
    * --port=PORT User defined port number for scp (Secure Copy Protocol) and\
      sftp (Secure FTP).
    * --name=NAME The representation of the license would be either license\
      key or serial number. The license key is a string with alpha numeric\
      characters and the License serial number is a string with the format\
      of 'FOS-XX-X-XX-XXXXXXXX'. Example of a license key and serial number\
      mentioned below. License key: 'HP9ttZNSgmB4MCD3NmNWgQDWtAKBFtXtBSFJF'\
      Serial number: 'FOS-00-0-02-11201234' This leaf is not included when\
      installing the licenses with serial number from a file.
    * --protocol=PROTOCOL The transport protocol.
    * --action=ACTION Action against specified license
    * --host=HOST The ip address or host name of the remote server.
    * --user-name=USER-NAME The user name of the remote server that is used to\
      copy the license certificates.
    * --license-payload=LICENSE-PAYLOAD This leaf allows user to send entire\
      license certificate content as a input. The license certificate payload\
      must be  base64 encoded to avoid the nested xml tag issue during input.\
      Refer to RFC 3414 for more details about base64 encode method.
* Output:
    * Python dictionary content with RESTCONF response data.


.. function:: license_operation_set.create_license_parameters(session,\
remote_directory, password, port, name, protocol, action, host, user_name,\
license_payload)

    *Create license_parameters*

        Example Usage of the Method::

            ret = license_operation_set.create_license_parameters(session,\
            remote_directory, password, port, name, protocol, action, host,\
            user_name, license_payload)
            print (ret)

        Details::

            license_parametersObj = license_parameters()
            license_parametersObj.set_remote_directory(remote_directory)
            license_parametersObj.set_password(password)
            license_parametersObj.set_port(port)
            license_parametersObj.set_name(name)
            license_parametersObj.set_protocol(protocol)
            license_parametersObj.set_action(action)
            license_parametersObj.set_host(host)
            license_parametersObj.set_user_name(user_name)
            license_parametersObj.set_license_payload(license_payload)
            print (ret)

        * Input::

            :param session: The session returned by the login.
            :param remote_directory: The remote server file path from which\
              the license certificate to be transferred.
            :param password: The password for the remote server used to copy\
              the license certificate. The password must be base64 encoded.\
              Refer to RFC 3414.
            :param port: User defined port number for scp (Secure Copy\
              Protocol) and sftp (Secure FTP).
            :param name: The representation of the license would be either\
              license key or serial number. The license key is a string with\
              alpha numeric characters and the License serial number is a\
              string with the format of 'FOS-XX-X-XX-XXXXXXXX'. Example of a\
              license key and serial number mentioned below. License key:\
              'HP9ttZNSgmB4MCD3NmNWgQDWtAKBFtXtBSFJF' Serial number:\
              'FOS-00-0-02-11201234' This leaf is not included when\
              installing the licenses with serial number from a file.
            :param protocol: The transport protocol.
            :param action: Action against specified license
            :param host: The ip address or host name of the remote server.
            :param user_name: The user name of the remote server that is used\
              to copy the license certificates.
            :param license_payload: This leaf allows user to send entire\
              license certificate content as a input. The license certificate\
              payload must be  base64 encoded to avoid the nested xml tag\
              issue during input. Refer to RFC 3414 for more details about\
              base64 encode method.

        * Output:

            :rtype: Dictionary of response

"""


# Start utils imports
import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_operation_license import license_parameters

from pyfos.utils import brcd_util
# End module imports


def _create_license_parameters(session, license_parametersObj):
    return license_parametersObj.post(session)


def create_license_parameters(session, remote_directory=None, password=None,
                              port=None, name=None, protocol=None,
                              action=None, host=None, user_name=None,
                              license_payload=None):
    license_parametersObj = license_parameters()
    license_parametersObj.set_remote_directory(remote_directory)
    license_parametersObj.set_password(password)
    license_parametersObj.set_port(port)
    license_parametersObj.set_name(name)
    license_parametersObj.set_protocol(protocol)
    license_parametersObj.set_action(action)
    license_parametersObj.set_host(host)
    license_parametersObj.set_user_name(user_name)
    license_parametersObj.set_license_payload(license_payload)
    return _create_license_parameters(session, license_parametersObj)


def validate(license_parametersObj):
    if license_parametersObj.peek_action() is None:
        print("The property action is missing\n")
        return 1

    if license_parametersObj.peek_license_payload() is not None:
        if license_parametersObj.peek_action() == "remove":
            linestr = "\nThe remove operation cannot be performed on "
            print(linestr + "license-payload property")
            return 1
        if license_parametersObj.peek_user_name() is not None:
            linestr = "\nThe combination of name and license-payload "
            print(linestr + "properties are not allowed")
            return 1
        if license_parametersObj.peek_remote_directory() is not None or\
           license_parametersObj.peek_password() is not None or\
           license_parametersObj.peek_protocol() is not None or\
           license_parametersObj.peek_user_name() is not None or\
           license_parametersObj.peek_port() is not None:
            linestr = "\nThe combination of server-parameters and license-"
            print(linestr + "payload properties are not allowed")
            return 1
    if license_parametersObj.peek_name() is not None:
        if license_parametersObj.peek_remote_directory() is not None or\
           license_parametersObj.peek_password() is not None or\
           license_parametersObj.peek_protocol() is not None or\
           license_parametersObj.peek_user_name() is not None or\
           license_parametersObj.peek_port() is not None:
            linestr = "\nThe combination of server-parameters and name"
            print(linestr + "property not allowed")
            return 1

    if license_parametersObj.peek_action() == "remove":
        if license_parametersObj.peek_remote_directory() is not None or\
           license_parametersObj.peek_password() is not None or\
           license_parametersObj.peek_protocol() is not None or\
           license_parametersObj.peek_user_name() is not None or\
           license_parametersObj.peek_port() is not None:
            linestr = "\nThe combination of server-parameters and remove "
            print(linestr + "action not allowed")
            return 1
    if license_parametersObj.peek_name() is None and\
       license_parametersObj.peek_license_payload() is None:
        if license_parametersObj.peek_remote_directory() is None:
            print("\nThe property remote_directory is missing\n")
            return 1
        elif license_parametersObj.peek_password() is None:
            print("\nThe property password is missing\n")
            return 1
        elif license_parametersObj.peek_protocol() is None:
            print("\nThe property protocol missing\n")
            return 1
        elif license_parametersObj.peek_host() is None:
            print("\nThe property host is missing  \n")
            return 1
        elif license_parametersObj.peek_user_name() is None:
            print("\nThe property user_name is missing  \n")
            return 1

    return 0


def main(argv):
    filters = ["remote_directory", "password", "port", "name", "protocol",
               "action", "host", "user_name", "license_payload"]
    inputs = brcd_util.parse(argv, license_parameters, filters, validate)
    session = brcd_util.getsession(inputs)
    result = _create_license_parameters(session, inputs['utilobject'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
