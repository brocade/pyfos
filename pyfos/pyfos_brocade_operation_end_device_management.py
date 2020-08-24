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

:mod:`pyfos_brocade_operation_end_device_management` - PyFOS module for the\
 End Device Management operation.
******************************************************************************\
******************************************************************************
The :mod:`pyfos_brocade_operation_end_device_management` module provides REST\
support for the End Device Management operation.

"""

from pyfos import pyfos_rest_util
from pyfos.pyfos_type import pyfos_type
import pyfos.pyfos_version as ver


class end_device_management(pyfos_rest_util.rest_object):
    """Class of the End Device Management Operation

    Important Class Members:

        +---------------------------+-----------------------------------+---------------------------------------+
        | Attribute Name            | Description                       |Frequently Used Methods                |
        +===========================+===================================+=======================================+
        | n-port-wwn                |The (PWWN) of the device.          |:func:`set_n_port_wwn`                 |
        +---------------------------+-----------------------------------+---------------------------------------+
        | n-port-id                 |The (FCID) of the device           |:func:`set_n_port_id`                  |
        +---------------------------+-----------------------------------+---------------------------------------+
        | version                   |Version identifier for the device. |:func:`set_version`                    |
        +---------------------------+-----------------------------------+---------------------------------------+
        | payload                   |Opaque payload in base64 format    |:func:`set_payload`                    |
        +---------------------------+-----------------------------------+---------------------------------------+

    *Object Methods*

        .. method:: post()

            Manages HBA. The required fields are set
            within the object using the attribute's set method.
            This method is used for managing the HBA.

            Example Usage of the Method to
            Post the End Device Management Operation:

            .. code-block:: python

                ss_obj =
                    pyfos_brocade_operation_end_device_management.end_device_management()
                ss_obj.set_n_port_wwn("xx:xx:xx:xx:xx:xx:xx:xx:xx")
                ss_obj.set_n_port_id("DDAAAL")
                ss_obj.set_verison(verison)
                ss_obj.set_payload("xyz")

            The above example triggers the End Device Management Operation.

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary of errors or a success response.

    *Attribute Methods*

        .. method:: set_port_wwn()

            Sets the remote device PWWN in the object.

            :param n-port-wwn: The PWWN of the remote device.
            :rtype: A dictionary of errors or a success response.

        .. method:: set_n_port_id()

            Sets the FCID of the remote device.

            :param n-port-id: The FCID of the remote device.
            :rtype: A dictionary of errors or a success response.

        .. method:: set_payload()

            Sets the payload for the remote device.

            :param payload: The payload for the remote host.
            :rtype: A dictionary of errors or a success response.

        .. method:: set_version()

            Sets the version for the remote device.

            :param version: Version identifier used by the device.
            :rtype: A dictionary of errors or a success response.
        """
    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.rpc_device_management,
                         "/rest/operations/device-management",
                         ver.VER_RANGE_821_and_ABOVE, 1, "device")
        self.add(pyfos_rest_util.rest_attribute("n-port-wwn",
                 pyfos_type.type_wwn, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("n-port-id",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("version",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("payload",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.load(dictvalues, 1)
