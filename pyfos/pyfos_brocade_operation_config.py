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

:mod:`pyfos_brocade_operation_config` - PyFOS module for the config \
 operation.
******************************************************************************\
*******************************************
The :mod:`pyfos_brocade_operation_config` The PyFOS module supports for
 the config operation.

"""

from pyfos import pyfos_rest_util
from pyfos.pyfos_type import pyfos_type
import pyfos.pyfos_version as ver


class config(pyfos_rest_util.rest_object):
    """Class of the config Operation

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
        | path                      | Path for the remote host.     |:func:`set_path`                       |
        +---------------------------+-------------------------------+---------------------------------------+
        | protocol                  | Protocol to access the host.  |:func:`set_protocol`                   |
        +---------------------------+-------------------------------+---------------------------------------+

    *Object Methods*

        .. method:: post()

            Install firmware and set configuration to factory
            default. The required fields are set
            within the object using the attribute's set method.

            Example Usage of the Method to Post the config upload/download Operation:

            .. code-block:: python

                fci_obj =
                    pyfos_brocade_operation_config.config()
                fci_obj.set_host("1.1.1.1")
                fci_obj.set_user_name("user")
                fci_obj.set_password("abcd")
                fci_obj.set_path("/a/b/c/d")
                fci_obj.set_protcolo("scp")
                fci_obj.set_type("all")
                fci_obj.set_upload(True)
                fci_obj.post(session)

            The above example triggers the config operation.

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary of errors or a success response.

    *Attribute Methods*

        .. method:: set_host()

            Sets host name to download firmware from in the object.

            :param host: host name.
            :rtype: A dictionary of errors or a success response.

        .. method:: set_user_name()

            Sets user name to download the firmware with in the object.

            :param user_name: user name.
            :rtype: A dictionary of errors or a success response.

        .. method:: set_password()

            Sets password to download the firmware with in the object.

            :param password: password.
            :rtype: A dictionary of errors or a success response.

        .. method:: set_path()

            Sets the remote server path in the object.

            :param path: The path to download firmware from.
            :rtype: A dictionary of errors or a success response.

        .. method:: set_protocol()

            Sets the protocol of the remote server access.

            :param protocol: The protocol to communicate with the server.
            :rtype: A dictionary of errors or a success response.

        """
    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.rpc_license,
                         "/rest/operations/config",
                         ver.VER_RANGE_820_ABOVE, 1, "config-parameters")
        self.add(pyfos_rest_util.rest_attribute("host",
                 pyfos_type.type_ip_addr, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("user-name",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("password",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("path",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("protocol",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("type",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("upload",
                 pyfos_type.type_bool, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.load(dictvalues, 1)
