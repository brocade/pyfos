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


# pyfos_brocade_operation_fabric.py(pyGen v1.0.0)


"""

:mod:`pyfos_brocade_operation_fabric` - PyFOS module The RPC\
command definition for fabric operation.
******************************************************************************\
*******************************************************************************
The :mod:`pyfos_brocade_operation_fabric` The PyFOS module\
support The RPC command definition for fabric operation.
"""


# Start module imports
from pyfos import pyfos_rest_util
from pyfos.pyfos_type import pyfos_type
from pyfos import pyfos_version as version
# End module imports


class fabric_operation_parameters(pyfos_rest_util.rest_object):

    """Class of fabric_operation_parameters

    *Description fabric_operation_parameters*

        Input container to perform fabric related operation.

    Important class members of fabric_operation_parameters:

    +---------------+------------------------------+--------------------------+
    | Attribute Name| Description                  |  Frequently Used Methods |
    +===============+==============================+==========================+
    | build-fabric  | The input which is required  | :func:`set_build_fabric` |
    |               | to initiate the build fabric | :func:`peek_build_fabric`|
    |               | operation. This operation    |                          |
    |               | requires switch to be enabled|                          |
    |               | state. And only 'true' should|                          |
    |               | be used as input. To verify  |                          |
    |               | the build fabric status      |                          |
    |               | please infer                 |                          |
    |               | brocade-fibrechannel-fabric? |                          |
    +---------------+------------------------------+--------------------------+

    *Object functions for fabric_operation_parameters*

    .. function:: get()

        Get the instances of class "fabric_operation_parameters from switch.
         The object can be printed using :func:`pyfos_utils.response_print`.

        :param session: The session handler returned by
         :func:`pyfos_auth.login`.

        :rtype: A dictionary of errors or a success response.

    .. method:: post()

        Performs fabric configuration related operations.

        *Example Usage of the Method to initiate build fabric operation::*

        .. code-block:: python

            ret = fabric_operations.rpc_fabric_operation_parameters(session,\
            build_fabric)
            print (ret)

        *Details::*

             fabric_operation_parametersObj = fabric_operation_parameters()
             fabric_operation_parametersObj.set_build_fabric(build_fabric)
             print (ret)

        :param session: The session handler returned by
         :func:`pyfos_auth.login`.
        :param build_fabric: The input which is required to initiate the\
          build fabric operation. This operation requires switch to be\
          enabled state. And only 'true' should be used as input. To\
          verify the build fabric status please infer\
          brocade-fibrechannel-fabric?

        :rtype: A dictionary of error or success information.


    *Class functions for fabric_operation_parameters*

        .. function:: peek_build_fabric()

            Reads the value assigned to build-fabric in the object.

            :rtype: None on error and a value on success.


        .. function:: set_build_fabric(value)

            Set the value of build-fabric in the object.

            :rtype: A dictionary of error or a success response.


    """

    def __init__(self, dictvalues=None):

        clsuri = "/rest" + "/operations" + "/fibrechannel-fabric"
        clstype = pyfos_rest_util.rest_obj_type.fabric_operation_parameters
        clsver = version.VER_RANGE_900_and_ABOVE
        super().__init__(clstype, clsuri, clsver, 1,
                         "fabric-operation-parameters")

        self.add(pyfos_rest_util.rest_attribute("build-fabric",
                 pyfos_type.type_bool, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.load(dictvalues, 1)
