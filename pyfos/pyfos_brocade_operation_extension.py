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


# pyfos_brocade_operation_extension.py(pyGen v1.0.0)


"""

:mod:`pyfos_brocade_operation_extension` - PyFOS module for RPC command\
definition for Extension operation on a Brocade switch.
******************************************************************************\
*******************************************************************************
The :mod:`pyfos_brocade_operation_extension` The PyFOS module support for RPC\
command definition for Extension operation on a Brocade switch.
"""


# Start module imports
from pyfos import pyfos_rest_util
from pyfos.pyfos_type import pyfos_type
from pyfos import pyfos_version as version
# End module imports


class extension_operation_status(pyfos_rest_util.rest_object):

    """Class of extension_operation_status

    *Description extension_operation_status*

        The container for Extension  operation status

    Important class members of extension_operation_status:

        +--------------------------+---------------------------------+-------------------------------------------------+
        | Attribute Name           | Description                     |  Frequently Used Methods                        |
        +==========================+=================================+=================================================+
        | status-message           | The status message informing    | :func:`set_status_message`                      |
        |                          | the operation status            | :func:`peek_status_message`                     |
        +--------------------------+---------------------------------+-------------------------------------------------+

    *Object functions for extension_operation_status*

    .. function:: get()

        Get the instances of class "extension_operation_status from switch.
         The object can be printed using :func:`pyfos_utils.response_print`.

        :param session: The session handler returned by
         :func:`pyfos_auth.login`.

        :rtype: A dictionary of errors or a success response.


    *Class functions for extension_operation_status*

        .. function:: peek_status_message()

            Reads the value assigned to status-message in the object.

            :rtype: None on error and a value on success.


        .. function:: set_status_message(value)

            Set the value of status-message in the object.

            :rtype: A dictionary of error or a success response and a value
             with "status-message" as the key


    """

    def __init__(self, dictvalues=None):

        clsuri = "/rest" + "/operations" + "/extension"
        clstype = pyfos_rest_util.rest_obj_type.extension_operation_status
        clsver = version.VER_RANGE_900_and_ABOVE
        super().__init__(clstype, clsuri, clsver, 1,
                         "extension-operation-status")

        self.add(pyfos_rest_util.rest_attribute("status-message",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.load(dictvalues, 1)


class extension_operation_parameters(pyfos_rest_util.rest_object):

    """Class of extension_operation_parameters

    *Description extension_operation_parameters*

        The extension operation input container.

    Important class members of extension_operation_parameters:

        +---------------------------------+-------------------------------------------------+--------------------------------------------------------+
        | Attribute Name                  | Description                                     |  Frequently Used Methods                               |
        +=================================+=================================================+========================================================+
        | slot                            | The slot number of for the datapath             | :func:`set_slot`                                       |
        |                                 | processor.                                      | :func:`peek_slot`                                      |
        +---------------------------------+-------------------------------------------------+--------------------------------------------------------+
        | dp-id                           | Extension Data Path Processor ID. Based on      | :func:`set_dp_id`                                      |
        |                                 | platform either it will have a single DP or     | :func:`peek_dp_id`                                     |
        |                                 | dual DP. In case of single DP only DP0 is       |                                                        |
        |                                 | supported, and in case of dual DP both DP0      |                                                        |
        |                                 | and DP1 are supported 0 : DP0 1 : DP1.          |                                                        |
        +---------------------------------+-------------------------------------------------+--------------------------------------------------------+
        | config-default                  | Default the extension configuration for the     | :func:`set_config_default`                             |
        |                                 | switch or blade. The config default operation   | :func:`peek_config_default`                            |
        |                                 | is a disruptive operation and details are as    |                                                        |
        |                                 | below. switch : After successful operation      |                                                        |
        |                                 | the switch  automatically reboots. blade : A    |                                                        |
        |                                 | blade should be in online state for the         |                                                        |
        |                                 | operation  to be allowed and the blade may be   |                                                        |
        |                                 | slot powered off and on  to allow different     |                                                        |
        |                                 | extension modes to be applied correctly.        |                                                        |
        |                                 | Supported values: false: No operation true :    |                                                        |
        |                                 | Default the extension configuration.            |                                                        |
        +---------------------------------+-------------------------------------------------+--------------------------------------------------------+
        | global-lan-statistics-reset     | Reset the global LAN statistics on a DP.        | :func:`set_global_lan_statistics_reset`                |
        |                                 | Supported values: false: No operation true :    | :func:`peek_global_lan_statistics_reset`               |
        |                                 | Reset the global LAN statistics.                |                                                        |
        +---------------------------------+-------------------------------------------------+--------------------------------------------------------+
        | config-clear                    | Clear the extension configuration for the       | :func:`set_config_clear`                               |
        |                                 | switch or blade. The config clear operation     | :func:`peek_config_clear`                              |
        |                                 | may be disruptive in nature. switch : A         |                                                        |
        |                                 | switch needs to be rebooted after a config      |                                                        |
        |                                 | clear operation, without which future config    |                                                        |
        |                                 | operations will be blocked. blade : A blade     |                                                        |
        |                                 | needs to be powered off before clearing the     |                                                        |
        |                                 | slot corresponding configuration. Supported     |                                                        |
        |                                 | values: false: No operation true : Clear the    |                                                        |
        |                                 | extension configuration.                        |                                                        |
        +---------------------------------+-------------------------------------------------+--------------------------------------------------------+

    *Object functions for extension_operation_parameters*

    .. function:: get()

        Get the instances of class "extension_operation_parameters from
         switch. The object can be printed using
         :func:`pyfos_utils.response_print`.

        :param session: The session handler returned by
         :func:`pyfos_auth.login`.

        :rtype: A dictionary of errors or a success response.


    *Class functions for extension_operation_parameters*

        .. function:: peek_slot()

            Reads the value assigned to slot in the object.

            :rtype: None on error and a value on success.


        .. function:: set_slot(value)

            Set the value of slot in the object.

            :rtype: A dictionary of error or a success response and a value
             with "slot" as the key


        .. function:: peek_dp_id()

            Reads the value assigned to dp-id in the object.

            :rtype: None on error and a value on success.


        .. function:: set_dp_id(value)

            Set the value of dp-id in the object.

            :rtype: A dictionary of error or a success response and a value
             with "dp-id" as the key


        .. function:: peek_config_default()

            Reads the value assigned to config-default in the object.

            :rtype: None on error and a value on success.


        .. function:: set_config_default(value)

            Set the value of config-default in the object.

            :rtype: A dictionary of error or a success response and a value
             with "config-default" as the key


        .. function:: peek_global_lan_statistics_reset()

            Reads the value assigned to global-lan-statistics-reset in the
             object.

            :rtype: None on error and a value on success.


        .. function:: set_global_lan_statistics_reset(value)

            Set the value of global-lan-statistics-reset in the object.

            :rtype: A dictionary of error or a success response and a value
             with "global-lan-statistics-reset" as the key


        .. function:: peek_config_clear()

            Reads the value assigned to config-clear in the object.

            :rtype: None on error and a value on success.


        .. function:: set_config_clear(value)

            Set the value of config-clear in the object.

            :rtype: A dictionary of error or a success response and a value
             with "config-clear" as the key


    """

    def __init__(self, dictvalues=None):

        clsuri = "/rest" + "/operations" + "/extension"
        clstype = pyfos_rest_util.rest_obj_type.extension_operation_parameters
        clsver = version.VER_RANGE_900_and_ABOVE
        super().__init__(clstype, clsuri, clsver, 1,
                         "extension-operation-parameters")

        self.add(pyfos_rest_util.rest_attribute("slot", pyfos_type.type_int,
                 None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("dp-id", pyfos_type.type_int,
                 None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("config-default",
                 pyfos_type.type_bool, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("global-lan-statistics-reset",
                 pyfos_type.type_bool, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("config-clear",
                 pyfos_type.type_bool, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.load(dictvalues, 1)
