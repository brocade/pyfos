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


# pyfos_brocade_operation_lldp.py(pyGen v1.0.0)


"""

:mod:`pyfos_brocade_operation_lldp` - PyFOS module The RPC command\
 definition for LLDP port operations on a Brocade switch.
******************************************************************************\
*******************************************************************************
The :mod:`pyfos_brocade_operation_lldp` The PyFOS module support The RPC\
 command definition for LLDP port operations on a Brocade switch.
"""


# Start module imports
from pyfos import pyfos_rest_util
from pyfos.pyfos_type import pyfos_type
from pyfos import pyfos_version as version
# End module imports


class lldp_operations(pyfos_rest_util.rest_object):

    """Class of lldp_operations

    *Description lldp_operations*

        LLDP actions container

    Important class members of lldp_operations:

        +--------------------------+---------------------------------+-------------------------------------------------+
        | Attribute Name           | Description                     |  Frequently Used Methods                        |
        +==========================+=================================+=================================================+
        | slot-port                | Port name                       | :func:`set_slot_port`                           |
        |                          |                                 | :func:`peek_slot_port`                          |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | action                   | LLDP actions on the given       | :func:`set_action`                              |
        |                          | port                            | :func:`peek_action`                             |
        +--------------------------+---------------------------------+-------------------------------------------------+

    *Object functions for lldp_operations*

    .. function:: get()

        Get the instances of class "lldp_operations from switch. The object
         can be printed using :func:`pyfos_utils.response_print`.

        :param session: The session handler returned by
         :func:`pyfos_auth.login`.

        :rtype: A dictionary of errors or a success response.


    *Class functions for lldp_operations*

        .. function:: peek_slot_port()

            Reads the value assigned to slot-port in the object.

            :rtype: None on error and a value on success.


        .. function:: set_slot_port(value)

            Set the value of slot-port in the object.

            :rtype: A dictionary of error or a success response and a value
             with "slot-port" as the key


        .. function:: peek_action()

            Reads the value assigned to action in the object.

            :rtype: None on error and a value on success.


        .. function:: set_action(value)

            Set the value of action in the object.

            :rtype: A dictionary of error or a success response and a value
             with "action" as the key


    """

    def __init__(self, dictvalues=None):

        clsuri = "/rest" + "/operations" + "/lldp"
        clstype = pyfos_rest_util.rest_obj_type.lldp_operations
        clsver = version.VER_RANGE_900_and_ABOVE
        super().__init__(clstype, clsuri, clsver, 1, "lldp-operations")

        self.add(pyfos_rest_util.rest_attribute("slot-port",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("action", pyfos_type.type_str,
                 None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.load(dictvalues, 1)
