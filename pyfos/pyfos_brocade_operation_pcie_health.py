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


# pyfos_brocade_operation_pcie_health.py(pyGen v1.0.0)


"""

:mod:`pyfos_brocade_operation_pcie_health` - PyFOS module \
for Brocade PCIe health operations.
******************************************************************************\
*******************************************************************************
The :mod:`pyfos_brocade_operation_pcie_health` module provides REST support \
for Brocade PCIe health operations.
"""


# Start module imports
from pyfos import pyfos_rest_util
from pyfos.pyfos_type import pyfos_type
from pyfos import pyfos_version as version
# End module imports


class slot_test(pyfos_rest_util.rest_object):

    """Class of slot_test

    *Description slot_test*

        slot test query response parameters for the PCIe health operations.

    Important class members of slot_test:

        +--------------------------+---------------------------------+-------------------------------------------------+
        | Attribute Name           | Description                     |  Frequently Used Methods                        |
        +==========================+=================================+=================================================+
        | status                   | Test the PCIe links between     | :func:`peek_status`                             |
        |                          | the non-transparent ports of    |                                                 |
        |                          | the PCIe switch in the blades   |                                                 |
        |                          | and the standby CP.             |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | slot-id                  | The number of the physical      | :func:`set_slot_id`                             |
        |                          | slot in the chassis in which    | :func:`peek_slot_id`                            |
        |                          | the blade is inserted. 255      |                                                 |
        |                          | indicates all the slots present |                                                 |
        |                          | in the switch.                  |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+

    *Object functions for slot_test*

    .. function:: post()

        Get the instances of class "slot_test from switch. The object can be
         printed using :func:`pyfos_utils.response_print`.

        :param session: The session handler returned by
         :func:`pyfos_auth.login`.

        :rtype: A dictionary of errors or a success response.


    *Class functions for slot_test*

        .. function:: peek_status()
        
           Reads the value assigned to status in the object.
 
           :rtype: None on error and a value on success.

       	.. function:: peek_slot_id()

           Reads the value assigned to slot-id in the object.

           :rtype: None on error and a value on success. 

        .. function:: set_slot_id(value)

           Set the value of slot-id in the object.

           :rtype: A dictionary of error or a success response and a value
             with "slot-id" as the key


    """

    def __init__(self, dictvalues=None):

        clsuri = "/rest" + "/operations" + "/pcie-health-test"
        clstype = pyfos_rest_util.rest_obj_type.slot_test
        clsver = version.VER_RANGE_900_and_ABOVE
        super().__init__(clstype, clsuri, clsver, 1, "slot-test")

        self.add(pyfos_rest_util.rest_attribute("status", pyfos_type.type_str,
                 None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("slot-id",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.load(dictvalues, 1)
