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

# pyfos_brocade_operation_license.py(pyGen v1.0.0)


"""

:mod:`pyfos_brocade_operation_license` - PyFOS module The RPC command\
definition for license operation on a Brocade switch.
******************************************************************************\
*******************************************************************************
The :mod:`pyfos_brocade_operation_license` The PyFOS module support The RPC\
command definition for license operation on a Brocade switch.
"""


# Start module imports
from pyfos import pyfos_rest_util
from pyfos.pyfos_type import pyfos_type
from pyfos import pyfos_version as version
# End module imports


class license_operation_status(pyfos_rest_util.rest_object):

    """Class of license_operation_status

    *Description license_operation_status*

        license operation status

    Important class members of license_operation_status:

        +--------------------------+---------------------------------+-------------------------------------------------+
        | Attribute Name           | Description                     |  Frequently Used Methods                        |
        +==========================+=================================+=================================================+
        | status-message           | The status message. This        |                                                 |
        |                          | message is an information for   | :func:`peek_status_message`                     |
        |                          | the user to perform             |                                                 |
        |                          | additional action such as       |                                                 |
        |                          | reboot, port/switch/chassis     |                                                 |
        |                          | disable or enable for the       |                                                 |
        |                          | license to take effect.         |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+

    *Object functions for license_operation_status*

    .. function:: get()

        Get the instances of class "license_operation_status from switch. The
         object can be printed using :func:`pyfos_utils.response_print`.

        :param session: The session handler returned by
         :func:`pyfos_auth.login`.

        :rtype: A dictionary of errors or a success response.


    *Class functions for license_operation_status*

        .. function:: peek_status_message()

            Reads the value assigned to status-message in the object.

            :rtype: None on error and a value on success.


    """

    def __init__(self, dictvalues=None):

        clsuri = "/rest" + "/operations" + "/license"
        clstype = pyfos_rest_util.rest_obj_type.license_operation_status
        clsver = version.VER_RANGE_900_and_ABOVE
        super().__init__(clstype, clsuri, clsver, 1,
                         "license-operation-status")

        self.add(pyfos_rest_util.rest_attribute("status-message",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.load(dictvalues, 1)


class license_parameters(pyfos_rest_util.rest_object):

    """Class of license_parameters

    *Description license_parameters*

        The license operation input container.

    Important class members of license_parameters:

        +--------------------------+---------------------------------+-------------------------------------------------+
        | Attribute Name           | Description                     |  Frequently Used Methods                        |
        +==========================+=================================+=================================================+
        | remote-directory         | The remote server file path     | :func:`set_remote_directory`                    |
        |                          | from which the license          |                                                 |
        |                          | certificate to be               |                                                 |
        |                          | transferred.                    |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | password                 | The password for the remote     | :func:`set_password`                            |
        |                          | server used to copy the         |                                                 |
        |                          | license certificate. The        |                                                 |
        |                          | password must be base64         |                                                 |
        |                          | encoded. Refer to RFC 3414.     |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | port                     | User defined port number for    | :func:`set_port`                                |
        |                          | scp (Secure Copy Protocol)      |                                                 |
        |                          | and sftp (Secure FTP).          |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | name                     | The representation of the       | :func:`set_name`                                |
        |                          | license would be either         |                                                 |
        |                          | license key or serial number.   |                                                 |
        |                          | The license key is a string     |                                                 |
        |                          | with alpha numeric characters   |                                                 |
        |                          | and the License serial number   |                                                 |
        |                          | is a string with the format     |                                                 |
        |                          | of 'FOS-XX-X-XX-XXXXXXXX'.      |                                                 |
        |                          | Example of a license key and    |                                                 |
        |                          | serial number mentioned         |                                                 |
        |                          | below. License key:             |                                                 |
        |                          | 'HP9ttZNSgmB4MCD3NmNWgQDWtAKB   |                                                 |
        |                          | FtXtBSFJF' Serial number:       |                                                 |
        |                          | 'FOS-00-0-02-11201234' This     |                                                 |
        |                          | leaf is not included when       |                                                 |
        |                          | installing the licenses with    |                                                 |
        |                          | serial number from a file.      |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | protocol                 | The transport protocol.         | :func:`set_protocol`                            |
        |                          |                                 |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | action                   | Action against specified        | :func:`set_action`                              |
        |                          | license                         |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | host                     | The ip address or host name     | :func:`set_host`                                |
        |                          | of the remote server.           |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | user-name                | The user name of the remote     | :func:`set_user_name`                           |
        |                          | server that is used to copy     |                                                 |
        |                          | the license certificates.       |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | license-payload          | This leaf allows user to send   | :func:`set_license_payload`                     |
        |                          | entire license certificate      |                                                 |
        |                          | content as a input.             |                                                 |
        |                          | The license certificate payload |                                                 |
        |                          | must be base64 encoded to avoid |                                                 |
        |                          | the nested xml tag issue        |                                                 |
        |                          | during input.                   |                                                 |
        |                          | Refer to RFC 3414 for more      |                                                 |
        |                          | details about base64 encode     |                                                 |
        |                          | method.                         |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+

    *Object functions for license_parameters*

    .. function:: get()

        Get the instances of class "license_parameters from switch. The object
         can be printed using :func:`pyfos_utils.response_print`.

        :param session: The session handler returned by
         :func:`pyfos_auth.login`.

        :rtype: A dictionary of errors or a success response.


    *Class functions for license_parameters*


        .. function:: set_remote_directory(value)

            Set the value of remote-directory in the object.

            :rtype: A dictionary of error or a success response and a value
             with "remote-directory" as the key


        .. function:: set_password(value)

            Set the value of password in the object.

            :rtype: A dictionary of error or a success response and a value
             with "password" as the key


        .. function:: set_port(value)

            Set the value of port in the object.

            :rtype: A dictionary of error or a success response and a value
             with "port" as the key


        .. function:: set_name(value)

            Set the value of name in the object.

            :rtype: A dictionary of error or a success response and a value
             with "name" as the key


        .. function:: set_protocol(value)

            Set the value of protocol in the object.

            :rtype: A dictionary of error or a success response and a value
             with "protocol" as the key


        .. function:: set_action(value)

            Set the value of action in the object.

            :rtype: A dictionary of error or a success response and a value
             with "action" as the key


        .. function:: set_host(value)

            Set the value of host in the object.

            :rtype: A dictionary of error or a success response and a value
             with "host" as the key


        .. function:: set_user_name(value)

            Set the value of user-name in the object.

            :rtype: A dictionary of error or a success response and a value
             with "user-name" as the key


        .. function:: set_license_payload(value)

            Set the value of license-payload in the object.

            :rtype: A dictionary of error or a success response and a value
             with "license-payload" as the key


    """

    def __init__(self, dictvalues=None):

        clsuri = "/rest" + "/operations" + "/license"
        clstype = pyfos_rest_util.rest_obj_type.license_parameters
        clsver = version.VER_RANGE_900_and_ABOVE
        super().__init__(clstype, clsuri, clsver, 1, "license-parameters")

        self.add(pyfos_rest_util.rest_attribute("remote-directory",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("password",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("port", pyfos_type.type_int,
                 None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("name", pyfos_type.type_str,
                 None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("protocol",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("action", pyfos_type.type_str,
                 None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("host", pyfos_type.type_str,
                 None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("user-name",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("license-payload",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG,
                 version.VER_RANGE_900a_and_ABOVE))
        self.load(dictvalues, 1)
