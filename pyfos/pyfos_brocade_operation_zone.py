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


# pyfos_brocade_operation_zone.py(pyGen v1.0.0)...with some help


"""

:mod:`pyfos_brocade_operation_zone` - PyFOS module used for zoning RPC \
 operations performed on a Brocade switch.
******************************************************************************\
*******************************************************************************
The :mod:`pyfos_brocade_operation_zone` module provides REST support for \
 zoning RPC operations performed on a Brocade switch.
"""


# Start module imports
from pyfos import pyfos_rest_util
from pyfos.pyfos_type import pyfos_type
from pyfos import pyfos_version as version
# End module imports


class zone_operation_parameters(pyfos_rest_util.rest_object):

    """Class of zone_operation_parameters

    Important class members:

        +--------------------------+---------------------------------+-------------------------------------------------+
        | Attribute Name           | Description                     |  Frequently Used Methods                        |
        +==========================+=================================+=================================================+
        | action                   | The type of RPC zone action     | :func:`set_action`                              |
        |                          | operation to perform.           | :func:`peek_action`                             |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | zone-object              | The zone object upon which      | :func:`set_zone_object`                         |
        |                          | the RPC zone action will be     | :func:`peek_zone_object`                        |
        |                          | performed.                      |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+

    *Object Methods*

    .. method:: post()

        Configures the specified zone operation RPC. The required fields are
        set within the object using the attribute's set method.  This method
        is used to trigger the zone operation in the switch.

        :param session: The session handler returned by
         :func:`pyfos_auth.login`.

        :rtype: A dictionary of errors or a success response.


    *Class functions for zone_operation_parameters*

        .. function:: set_action(value)

            Set the value of action in the object.

            :rtype: A dictionary of error or a success response and a value
             with "action" as the key

        .. function:: peek_action(value)

            Reads the value of action in the object.

            :rtype: None on error and a value on success.

        .. function:: set_zone_object(value)

            Set the value of zone-object in the object.

            :rtype: A dictionary of error or a success response and a value
             with "zone-object" as the key

        .. function:: peek_zone_object(value)

            Reads the value of zone-object in the object.

            :rtype: None on error and a value on success.

    """

    def __init__(self, dictvalues=None):

        clsuri = "/rest" + "/operations" + "/fibrechannel-zone"
        clstype = pyfos_rest_util.rest_obj_type.zone_operation_parameters
        clsver = version.VER_RANGE_900_and_ABOVE
        super().__init__(clstype, clsuri, clsver, 1,
                         "zone-operation-parameters")
        self.add(pyfos_rest_util.rest_attribute("action", pyfos_type.type_str,
                 None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("zone-object",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.load(dictvalues, 1)
