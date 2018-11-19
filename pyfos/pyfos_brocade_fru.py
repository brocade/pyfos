# Copyright 2018 Brocade Communications Systems LLC.  All rights reserved.
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

:mod:`pyfos_brocade_fru` - PyFOS module to provide rest support for the FRU.
****************************************************************************
The :mod:`pyfos_brocade_fru` provides REST support for the FRU.

"""

from pyfos import pyfos_rest_util
from pyfos.pyfos_type import pyfos_type
import pyfos.pyfos_version as version


class fan(pyfos_rest_util.rest_object):
    """This class provides information for the given FAN unit.

    Important class members:

        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | Attribute name                    | Description                    | Frequently used methods                               |
        +===================================+================================+=======================================================+
        | unit-number                       | Fan Unit number                |:meth:`peek_unit_number`                               |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | power-consumption                 | Power consumption of the       |:meth:`peek_power_consumption`                         |
        |                                   | hardware component             |                                                       |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | operational-state                 | Operational state of the Fan   |:meth:`peek_operational_state`                         |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | part-number                       | Part number of the Fan         |:meth:`peek_part_number`                               |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | serial-number                     | Serial number of the Fan       |:meth:`peek_serial_number`                             |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | airflow-direction                 | Air flow direction of the Fan  |:meth:`peek_airflow_direction`                         |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+

    *Object methods*

        .. classmethod:: get()

            Returns :class:`fan`
            object or a list of objects filled with
            Fan attributes.

            Each object can be printed using :func:`pyfos_util.response_print`
            and individual attributes accessed through peek methods.

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary of error or
                :class:`fan` object

    *Attribute methods*

        .. method:: peek_unit_number()

            Reads fan unit number from the object.

            :rtype: None or fan unit number.

        .. method:: peek_power_consumption()

            Reads power consumption of the hardware component from the object.

            :rtype: None or power consumption by the unit.

        .. method:: peek_operational_state()

            Reads operational state of the fan.

            :rtype: None or operational state of the fan

        .. method:: peek_speed()

            Reads speed of the fan.

            :rtype: None or speed of the fan

        .. method:: peek_airflow_direction()

            Reads airflow direction of the fan.

            :rtype: None or airflow direction of the fan

        .. method:: peek_part_number()

            Reads part number of the fan.

            :rtype: None or part number of the fan

        .. method:: peek_serial_number()

            Reads serial number of the fan.

            :rtype: None or serial number of the fan

        """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.fan_unit,
                         "/rest/running/brocade-fru/fan",
                         version.VER_RANGE_821_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "unit-number", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute(
            "power-consumption", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "operational-state", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "speed", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "airflow-direction", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "part-number", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "serial-number", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.load(dictvalues, 1)


class power_supply(pyfos_rest_util.rest_object):
    """This class provides information for the given powersupply unit.

    Important class members:

        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | Attribute name                    | Description                    | Frequently used methods                               |
        +===================================+================================+=======================================================+
        | unit-number                       | Powersupply Unit number        |:meth:`peek_unit_number`                               |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | power-production                  | Power production of the        |:meth:`peek_power_production`                          |
        |                                   | hardware component             |                                                       |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | input-voltage                     | Input voltage of the           |:meth:`peek_input_voltage`                             |
        |                                   | powersupply Unit               |                                                       |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | part-number                       | Part number of the Unit        |:meth:`peek_part_number`                               |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | serial-number                     | Serial number of the Unit      |:meth:`peek_serial_number`                             |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | airflow-direction                 | Air flow direction of the Unit |:meth:`peek_airflow_direction`                         |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | operational-state                 | Operational state of the Unit  |:meth:`peek_operational_state`                         |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | power-source                      | Power supply input             |:meth:`peek_power_source`                              |
        |                                   | voltage type                   |                                                       |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | temperature                       | Temperature of the power       |:meth:`peek_temperature`                               |
        |                                   | supply sensor                  |                                                       |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+

    *Object methods*

        .. classmethod:: get()

            Returns :class:`power_supply`
            object or a list of objects filled with
            Powersupply attributes.

            Each object can be printed using :func:`pyfos_util.response_print`
            and individual attributes accessed through peek methods.

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary of error or
                :class:`power_supply` object

    *Attribute methods*

        .. method:: peek_unit_number()

            Reads powersupply unit number from the object.

            :rtype: None or powersupply unit number.

        .. method:: peek_power_production()

            Reads power production of the hardware component from the object.

            :rtype: None or power production by the unit.

        .. method:: peek_operational_state()

            Reads operational state of the powersupply.

            :rtype: None or operational state of the powersupply.

        .. method:: peek_input_voltage()

            Reads input voltage of the powersupply unit.

            :rtype: None or input voltage of the unit.

        .. method:: peek_airflow_direction()

            Reads airflow direction of the powersupply unit.

            :rtype: None or airflow direction of the powersupply.

        .. method:: peek_part_number()

            Reads part number of the powersupply unit.

            :rtype: None or part number of the powersupply unit.

        .. method:: peek_serial_number()

            Reads serial number of the powersupply unit.

            :rtype: None or serial number of the powersupply unit.

        .. method:: peek_power_source()

            Reads power supply input voltage type.

            :rtype: None or power supply input voltage type.

        .. method:: peek_temperature()

            Reads temperature of the powersupply sensor.

            :rtype: None or Temperature of the powersupply sensor.

        """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.ps_unit,
                         "/rest/running/brocade-fru/power-supply",
                         version.VER_RANGE_821_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "unit-number", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute(
            "power-production", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "operational-state", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "power-source", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "airflow-direction", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "input-voltage", pyfos_type.type_float,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "temperature", pyfos_type.type_float,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "part-number", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "serial-number", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.load(dictvalues, 1)


class blade(pyfos_rest_util.rest_object):
    """This class provides information of the blade for the given slot number.

    Important class members:

        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | Attribute name                    | Description                    | Frequently used methods                               |
        +===================================+================================+=======================================================+
        | slot-number                       | Slot number                    |:meth:`peek_slot_number`                               |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | manufacturer                      | Organization responsible for   |:meth:`peek_manufacturer`                              |
        |                                   | producing the blade            |                                                       |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | blade-type                        | Type of the blade              |:meth:`peek_blade_type`                                |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | part-number                       | Part number of the blade       |:meth:`peek_part_number`                               |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | serial-number                     | Serial number of the blade     |:meth:`peek_serial_number`                             |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | blade-id                          | ID of the blade                |:meth:`peek_blade_id`                                  |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | blade-state                       | current state of the blade     |:meth:`peek_blade_state`                               |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | model-name                        | model of the blade             |:meth:`peek_model_name`                                |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | firmware-version                  | FOS version of switch          |:meth:`peek_firmware_version`                          |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | fc-port-count                     | total number of fc ports       |:meth:`peek_fc_port_count`                             |
        |                                   | supported by the blade         |                                                       |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | ge-port-count                     | total number of ge ports       |:meth:`peek_ge_port_count`                             |
        |                                   | supported by the blade         |                                                       |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | ip-address-list/ip-address        | The IPv4/IPv6 address          |:meth:`peek_ip_address_list_ip_address`                |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | ip-gateway-list/ip-gateway        | The IP Address Gateway         |:meth:`peek_ip_gateway_list_ip_gateway`                |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | subnet-mask                       | Subnet mask of the network     |:meth:`peek_subnet_mask`                               |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | primary-firmware-version          | FOS version on the primary     |:meth:`peek_primary_firmware_version`                  |
        |                                   | partition of the CP blade      |                                                       |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | secondary-firmware-version        | FOS version on the secondary   |:meth:`peek_secondary_firmware_version`                |
        |                                   | partition of the CP blade      |                                                       |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | extension-enabled                 | Blade is extension capable     |:meth:`peek_extension_enabled`                         |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | extension-ve-mode                 | Extension blade VE mode        |:meth:`peek_extension_ve_mode`                         |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | extension-ve-mode                 | Extension blade VE mode        |:meth:`set_extension_ve_mode`                          |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | extension-app-mode                | Extension blade app mode       |:meth:`peek_extension_app_mode`                        |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | extension-app-mode                | Extension blade app mode       |:meth:`set_extension_app_mode`                         |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | extension-ge-mode                 | Extension blade ge mode        |:meth:`peek_extension_ge_mode`                         |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | extension-ge-mode                 | Extension blade ge mode        |:meth:`set_extension_ge_mode`                          |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+

    *Object methods*

        .. classmethod:: get()

            Returns :class:`blade`
            object or a list of objects filled with
            Blade attributes.

            Each object can be printed using :func:`pyfos_util.response_print`
            and individual attributes accessed through peek methods.

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary of error or
                :class:`blade` object

    *Attribute methods*

        .. method:: peek_slot_number()

            Reads blade slot number from the object.

            :rtype: None or blade slot number.

        .. method:: peek_manufacturer()

            Reads manufacturer name of the organization from the object.

            :rtype: None or manufacturer name of the blade.

        .. method:: peek_blade_type()

            Reads type of the blade.

            :rtype: None or type of the blade.

        .. method:: peek_blade_id()

            Reads ID of the blade.

            :rtype: None or ID of the blade.

        .. method:: peek_blade_state()

            Reads current state of the blade.

            :rtype: None or current state of the blade.

        .. method:: peek_part_number()

            Reads part number of the blade.

            :rtype: None or part number of the blade.

        .. method:: peek_serial_number()

            Reads serial number of the blade.

            :rtype: None or serial number of the blade.

        .. method:: peek_model_name()

            Reads model of the blade.

            :rtype: None or model of the blade.

        .. method:: peek_firmware_version()

            Reads FOS version of the switch.

            :rtype: None or firmware version of the switch.

        .. method:: peek_fc_port_count()

            Reads total number of fc ports on the blade.

            :rtype: None or total number of fc ports on the blade.

        .. method:: peek_ge_port_count()

            Reads total number of ge ports on the blade.

            :rtype: None or total number of ge ports on the blade.

        .. method:: peek_ip_address_list_ip_address()

            Reads IP Address from an object.

            :rtype: None or IP Address.

        .. method:: peek_ip_gateway_list_ip_gateway()

            Reads IP Gateway from an object.

            :rtype: None or IP Gateway.

        .. method:: peek_subnet_mask()

            Reads Subnet mask from an object.

            :rtype: None or subnet mask.

        .. method:: peek_primary_firmware_version()

            Reads FOS version of the primary partition of the blade.

            :rtype: None or firmware version of the primary partition.

        .. method:: peek_secondary_firmware_version()

            Reads FOS version of the secondary partition of the blade.

            :rtype: None or firmware version of the secondary partition.

        .. method:: peek_extension_enabled()

            Reads extension enabled/capable value for the blade or switch.

            :rtype: true or false.

        .. method:: peek_extension_app_mode()

            Reads extension blade app mode from the blade object.

            :rtype: None or app mode string.

        .. method:: set_extension_app_mode()

            Set the extension capable blade app mode in the blade object.

            :rtype: dictionary of error or success response and value
             with extension-app-mode as key.

        .. method:: peek_extension_ve_mode()

            Reads extension blade VE mode from the blade object.

            :rtype: None or VE mode string.

        .. method:: set_extension_ve_mode()

            Set the extension capable blade VE mode in the blade object.

            :rtype: dictionary of error or success response and value
             with extension-ve-mode as key.

        .. method:: peek_extension_ge_mode()

            Reads extension blade GE mode from the blade object.

            :rtype: None or VE mode string.

        .. method:: set_extension_ge_mode()

            Set the extension capable blade GE mode in the blade object.

            :rtype: dictionary of error or success response and value
             with extension-ge-mode as key.

        """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.blade_slot,
                         "/rest/running/brocade-fru/blade",
                         version.VER_RANGE_821_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "slot-number", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute(
            "manufacturer", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "blade-type", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "blade-id", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "blade-state", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "model-name", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "firmware-version", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "part-number", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "serial-number", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "fc-port-count", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "ge-port-count", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "primary-firmware-version", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "secondary-firmware-version", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "extension-enabled", pyfos_type.type_bool,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "extension-app-mode", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "extension-ve-mode", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "extension-ge-mode", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "ip-address-list", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute(
            "ip-address", pyfos_type.type_ip_addr,
            None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST),
            ["ip-address-list"])
        self.add(pyfos_rest_util.rest_attribute(
            "ip-gateway-list", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute(
            "ip-gateway", pyfos_type.type_ip_addr,
            None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST),
            ["ip-gateway-list"])
        self.add(pyfos_rest_util.rest_attribute(
            "subnet-mask", pyfos_type.type_ip_addr,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.load(dictvalues, 1)
