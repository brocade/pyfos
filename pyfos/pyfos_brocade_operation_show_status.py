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

:mod:`pyfos_brocade_operation_show_status` - PyFOS module for supportsave\
operation status
***************************************************************************\
********************
The :mod:`pyfos_brocade_operation_show_status` provides REST support for
firmwaredownload and supportsave operation status.

"""

from pyfos import pyfos_rest_util
from pyfos.pyfos_type import pyfos_type
import pyfos.pyfos_version as ver


class show_status(pyfos_rest_util.rest_object):
    """Class of supportsave operation status

    Important class members:

        +-------------------------------+-------------------------------+---------------------------------------+
        | Attribute name                | Description                   | Frequently used functions             |
        +===============================+===============================+=======================================+
        | message-id                    | The message id of operation   |:func:`peek_message_id`                |
        |                               |                               |:func:`set_message_id`                 |
        +-------------------------------+-------------------------------+---------------------------------------+
        | operation                     | The type of operation         |:func:`peek_operation`                 |
        +-------------------------------+-------------------------------+---------------------------------------+
        | application-name              | The application name          |:func:`peek_application_name`          |
        +-------------------------------+-------------------------------+---------------------------------------+
        | percentage-complete           | completion percentage value   |:func:`peek_percentage_complete`       |
        +-------------------------------+-------------------------------+---------------------------------------+
        | status                        | status of the operation       |:func:`peek_status`                    |
        +-------------------------------+-------------------------------+---------------------------------------+

    *Object functions*

        .. function:: get()

            Fill the object with values for all the attributes. Once filled,
            the object can be printed using :func:`pyfos_utils.response_print`

            :param session: session handler returned
             by :func:`pyfos_auth.login`
            :rtype: dictionary of error or success response

    *Attribute functions*

        .. function:: peek_status()

            Reads the status from the object.

            :rtype: None on error and value on success

        .. function:: peek_operation()

            Reads the type of the operation

            :rtype: None on error and value on success

        .. function:: peek_application_name()

            Reads the application name from an object.

            :rtype: None on error and value on success

        .. function:: peek_percentage_complete()

            Reads percentage completion from the object.

            :rtype: None on error and value on success

        .. function:: peek_message_id()

            Reads message ID from an object.

            :rtype: None on error and value on success

        .. function:: set_message_id(msgId)

            Set the message ID.

            :rtype: dictionary of error or success response and
             value with "message id" as key

        """
    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.rpc_show_status,
                         "/rest/operations/show-status",
                         ver.VER_RANGE_900_and_ABOVE, 1)
        self.add(pyfos_rest_util.rest_attribute("message-id",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("status",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("application-name",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("percentage-complete",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("operation",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "eula-text", pyfos_type.type_str,
                 None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "firmwaredownload", pyfos_type.type_na,
                 dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute(
                 "message", pyfos_type.type_na,
                 None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST),
                 ["firmwaredownload"])
        self.load(dictvalues, 1)
