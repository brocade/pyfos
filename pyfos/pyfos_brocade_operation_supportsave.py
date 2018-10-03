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

:mod:`pyfos_brocade_operation_supportsave` - PyFOS module for supportsave\
 operation
***************************************************************************\
************
The :mod:`pyfos_brocade_operation_supportsave` provides REST support for
 supportsave operation.

"""

import pyfos.pyfos_rest_util as pyfos_rest_util
from pyfos.pyfos_type import pyfos_type
import pyfos.pyfos_version as ver


class supportsave(pyfos_rest_util.rest_object):
    """Class of supportsave operation

    Important class members:

        +---------------------------+------------------------------+---------------------------------------+
        | Attribute name            | Description                  |Frequstly used methods                 |
        +===========================+==============================+=======================================+
        | host                      | ipaddress of the remote host |:func:`set_host`                       |
        +---------------------------+------------------------------+---------------------------------------+
        | user-name                 | user-name of the remote host |:func:`set_user_name`                  |
        +---------------------------+------------------------------+---------------------------------------+
        | password                  | password for the remote user |:func:`set_password`                   |
        +---------------------------+------------------------------+---------------------------------------+
        | remote-directory          | path for the remote host     |:func:`set_remote_directory`           |
        +---------------------------+------------------------------+---------------------------------------+
        | protocol                  | protocol to access the host  |:func:`set_protocol`                   |
        +---------------------------+------------------------------+---------------------------------------+

    *Object methods*

        .. method:: post()

            Create an object and do post. Fields involved are set
            within the object using attribute's set method.
            This method is used to trigger supportsave operation in the 
            switch.

            Example usage of the method to post supportsave operation:

            .. code-block:: python

                ss_obj =
                    pyfos_brocade_operation_supportsave.supportsave()
                ss_obj.set_host("1.1.1.1")
                ss_obj.set_user_name("user")
                ss_obj.set_password("abcd")
                ss_obj.set_remote_directory("/a/b/c/d")
                ss_obj.set_protcolo("scp")
                ss_obj.post(session)

            The above example will trigger supportsave operation.

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary of error or success response

    *Attribute methods*

        .. method:: set_host()

            Sets host in the object.

            :param host: host name of the remote server 
            :rtype: dictionary of error or success response

        .. method:: set_user_name()

            Sets user name of the remote host.

            :param username: username of the remote server 
            :rtype: dictionary of error or success response

        .. method:: set_password()

            Setss remote username's password.

            :param password: password of the remote user 
            :rtype: dictionary of error or success response

        .. method:: set_remote_directory()

            Reads remote server path.

            :param path: path to store the supportsave logs 
            :rtype: dictionary of error or success response

        .. method:: set_protocol()

            Reads protocol of the remote server access.

            :param protocol: protocol to communicate with server  
            :rtype: dictionary of error or success response

        """
    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.rpc_supportsave,
                         "/rest/operations/supportsave", ver.VER_RANGE_821_and_ABOVE, 1, "connection")
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
        self.load(dictvalues, 1)
