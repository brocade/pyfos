#!/usr/bin/env python3

# Copyright © 2018 Broadcom. All Rights Reserved. The term “Broadcom” refers to
# Broadcom Inc. and/or its subsidiaries.
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

:mod:`pyfos_brocade_operation_supportsave` - PyFOS module for the supportsave \
 operation.
******************************************************************************\
***********
The :mod:`pyfos_brocade_operation_supportsave` module provides REST support for
 the supportsave operation.

"""

from pyfos import pyfos_rest_util
from pyfos.pyfos_type import pyfos_type
import pyfos.pyfos_version as ver


class supportsave(pyfos_rest_util.rest_object):
    """Class of the supportsave Operation

    Important Class Members:

        +---------------------------+-------------------------------+---------------------------------------+
        | Attribute Name            | Description                   |Frequently Used Methods                |
        +===========================+===============================+=======================================+
        | host                      |IP address of the remote host. |:func:`set_host`                       |
        +---------------------------+-------------------------------+---------------------------------------+
        | user-name                 | User name of the remote host. |:func:`set_user_name`                  |
        +---------------------------+-------------------------------+---------------------------------------+
        | password                  | Password for the remote user. |:func:`set_password`                   |
        +---------------------------+-------------------------------+---------------------------------------+
        | remote-directory          | Path for the remote host.     |:func:`set_remote_directory`           |
        +---------------------------+-------------------------------+---------------------------------------+
        | protocol                  | Protocol to access the host.  |:func:`set_protocol`                   |
        +---------------------------+-------------------------------+---------------------------------------+
        | serial-mode               | Legacy serial-mode module     | :func:`set_serial_mode`               |
        |                           | supportsave collection. true  |                                       |
        |                           | : Supportsave process will be |                                       |
        |                           | done serialize module by      |                                       |
        |                           | module. false : Supportsave   |                                       |
        |                           | process will be done in       |                                       |
        |                           | parallel for multiple         |                                       |
        |                           | modules.                      |                                       |
        +---------------------------+-------------------------------+---------------------------------------+
        | port                      | User defined port number can  | :func:`set_port`                      |
        |                           | be configured only for        |                                       |
        |                           | scp/sftp protocol             |                                       |
        +---------------------------+-------------------------------+---------------------------------------+

    *Object Methods*

        .. method:: post()

            Configures supportsave. The required fields are set
            within the object using the attribute's set method.
            This method is used to trigger the supportsave operation in the \
            switch.

            Example Usage of the Method to Post the Supportsave Operation:

            .. code-block:: python

                ss_obj =
                    pyfos_brocade_operation_supportsave.supportsave()
                ss_obj.set_host("1.1.1.1")
                ss_obj.set_user_name("user")
                ss_obj.set_password("abcd")
                ss_obj.set_remote_directory("/a/b/c/d")
                ss_obj.set_protcolo("scp")
                ss_obj.post(session)

            The above example triggers the supportsave operation.

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary of errors or a success response.

    *Attribute Methods*

        .. method:: set_host()

            Sets the host in the object.

            :param host: The host name of the remote server.
            :rtype: A dictionary of errors or a success response.

        .. method:: set_user_name()

            Sets the user name of the remote host.

            :param username: The user name of the remote server.
            :rtype: A dictionary of errors or a success response.

        .. method:: set_password()

            Sets the remote username's password.

            :param password: The password of the remote user.
            :rtype: A dictionary of errors or a success response.

        .. method:: set_remote_directory()

            Reads the remote server path.

            :param path: The path to store the supportsave logs.
            :rtype: A dictionary of errors or a success response.

        .. method:: set_protocol()

            Reads the protocol of the remote server access.

            :param protocol: The protocol to communicate with the server.
            :rtype: A dictionary of errors or a success response.

        .. method:: set_serial_mode(value)

            Set the value of serial-mode in the supportsave object.

            :param serial_mode: Legacy serial-mode module supportsave.
            :rtype: A dictionary of error or a success response and a value
             with "serial-mode" as the key

        .. method:: set_port(value)

            Set the value of port in the supportsave object.

            :param port: Port number of remote server .
            :rtype: A dictionary of error or a success response and a value
             with "port" as the key

        """
    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.rpc_supportsave,
                         "/rest/operations/supportsave",
                         ver.VER_RANGE_821_and_ABOVE, 1, "connection")
        self.add(pyfos_rest_util.rest_attribute("host",
                 pyfos_type.type_ip_addr, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("user-name",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("password",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("remote-directory",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("protocol",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("serial-mode",
                 pyfos_type.type_bool, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("port",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.load(dictvalues, 1)
