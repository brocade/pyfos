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

:mod:`pyfos_brocade_fdmi` - PyFOS module to provide REST support for FDMI.
*********************************************************************************************************
The :mod:`pyfos_brocade_fdmi` provides REST support for FDMI.

"""

from pyfos import pyfos_rest_util
from pyfos.pyfos_type import pyfos_type
import pyfos.pyfos_version as version


class hba(pyfos_rest_util.rest_object):
    """Class of FDMI HBA

    Important class members:

        +----------------------------------------+-------------------------------+----------------------------------------------------+
        | Attribute name                         | Description                   |Frequstly used methods                              |
        +========================================+===============================+====================================================+
        | hba-id                                 | Unique HBA identifier         |:meth:`peek_hba_id`                                 |
        +----------------------------------------+-------------------------------+----------------------------------------------------+
        | domain-id                              | Domain ID HBA is directly     |:meth:`peek_domain_id`                              |
        |                                        | attached to                   |                                                    |
        +----------------------------------------+-------------------------------+----------------------------------------------------+
        | manufacturer                           | Manufacturer of HBA           |:meth:`peek_manufacturer`                           |
        +----------------------------------------+-------------------------------+----------------------------------------------------+
        | serial-number                          | Serial number of HBA          |:meth:`peek_serial_number`                          |
        +----------------------------------------+-------------------------------+----------------------------------------------------+
        | model                                  | Model of HBA                  |:meth:`peek_model`                                  |
        +----------------------------------------+-------------------------------+----------------------------------------------------+
        | model-description                      | Describes HBA model           |:meth:`peek_model_description`                      |
        +----------------------------------------+-------------------------------+----------------------------------------------------+
        | node-name                              | Node name of HBA              |:meth:`peek_node_name`                              |
        +----------------------------------------+-------------------------------+----------------------------------------------------+
        | node-symbolic-name                     | Symbolic node name of HBA     |:meth:`peek_node_symbolic_name`                     |
        +----------------------------------------+-------------------------------+----------------------------------------------------+
        | hardware-version                       | Hardware version of HBA       |:meth:`peek_hardware_version`                       |
        +----------------------------------------+-------------------------------+----------------------------------------------------+
        | driver-version                         | Driver version of HBA         |:meth:`peek_driver_version`                         |
        +----------------------------------------+-------------------------------+----------------------------------------------------+
        | option-rom-version                     | Option ROM or BIOS version of |:meth:`peek_option_rom_version`                     |
        |                                        | HBA                           |                                                    |
        +----------------------------------------+-------------------------------+----------------------------------------------------+
        | firmware-version                       | Firmware version of HBA       |:meth:`peek_firmware_version`                       |
        +----------------------------------------+-------------------------------+----------------------------------------------------+
        | os-name-and-version                    | Type and version of the HBA's |:meth:`peek_os_name_and_version`                    |
        |                                        | OS                            |                                                    |
        +----------------------------------------+-------------------------------+----------------------------------------------------+
        | max-ct-payload                         | Maximum CT payload size       |:meth:`peek_max_ct_payload`                         |
        +----------------------------------------+-------------------------------+----------------------------------------------------+
        | vendor-id                              | Vendor ID of HBA              |:meth:`peek_vendor_id`                              |
        +----------------------------------------+-------------------------------+----------------------------------------------------+
        | vendor-specific-info                   | Vendor specific information   |:meth:`peek_vendor_specific_info`                   |
        +----------------------------------------+-------------------------------+----------------------------------------------------+
        | number-of-ports                        | Number of Nx_Ports on HBA     |:meth:`peek_number_of_ports`                        |
        +----------------------------------------+-------------------------------+----------------------------------------------------+
        | fabric-name                            | Fabric name                   |:meth:`peek_fabric_name`                            |
        +----------------------------------------+-------------------------------+----------------------------------------------------+
        | boot-bios-version                      | Boot BIOS version of HBA      |:meth:`peek_boot_bios_version`                      |
        +----------------------------------------+-------------------------------+----------------------------------------------------+
        | boot-bios-enabled                      | Indicate if boot BIOS is      |:meth:`peek_boot_bios_enabled`                      |
        |                                        | enabled                       |                                                    |
        +----------------------------------------+-------------------------------+----------------------------------------------------+
        | hba-port-list                          | List of HBA ports             |:meth:`peek_hba_port_list`                          |
        +----------------------------------------+-------------------------------+----------------------------------------------------+

    *Object methods*

        .. staticmethod:: get(session, hba_identifier=None)

            Returns a :class:`hba` object or a list of objects filled with
            FDMI HBA attributes.

            Each object can be printed using :func:`pyfos_util.response_print`
            and individual attributes accessed through peek methods.

            :param session: session handler returned by
                    :func:`pyfos_auth.login`
            :rtype: :class:`hba` object or list of objects. Dictionary in case
                    of error.

    *Attribute methods*

        .. method:: peek_hba_id()

            Reads HBA identifier from the object.

            :rtype: None or HBA identifier of the HBA

        .. method:: peek_domain_id()

            Reads domain ID from the object.

            :rtype: None or domain ID the HBA is directly attached to

        .. method:: peek_manufacturer()

            Reads manufacturer from the object.

            :rtype: None or manufacturer of the HBA

        .. method:: peek_serial_number()

            Reads serial number from the object.

            :rtype: None or serial number of the HBA

        .. method:: peek_model()

            Reads model from the object.

            :rtype: None or model of the HBA

        .. method:: peek_model_description()

            Reads model description from the object.

            :rtype: None or model description of the HBA

        .. method:: peek_node_name()

            Reads node name from the object.

            :rtype: None or node name of the HBA

        .. method:: peek_node_symbolic_name()

            Reads node symbolic name from the object.

            :rtype: None or node symbolic name of the HBA

        .. method:: peek_hardware_version()

            Reads hardware version from the object.

            :rtype: None or hardware version of the HBA

        .. method:: peek_driver_version()

            Reads driver version from the object.

            :rtype: None or driver version of the HBA

        .. method:: peek_option_rom_version()

            Reads option rom version from the object.

            :rtype: None or option rom version of the HBA

        .. method:: peek_firmware_version()

            Reads firmware version from the object.

            :rtype: None or firmware version of the HBA

        .. method:: peek_os_name_and_version()

            Reads OS name and version from the object.

            :rtype: None or OS name and version of the HBA

        .. method:: peek_max_ct_payload()

            Reads max CT payload from the object.

            :rtype: None or max CT payload of the HBA

        .. method:: peek_vendor_id()

            Reads vendor identifier from the object.

            :rtype: None or vendor identifier of the HBA

        .. method:: peek_vendor_specific_info()

            Reads vendor specific info from the object.

            :rtype: None or vendor specific info of the HBA

        .. method:: peek_number_of_ports()

            Reads number of ports from the object.

            :rtype: None or number of ports of the HBA

        .. method:: peek_fabric_name()

            Reads fabric name from the object.

            :rtype: None or fabric name

        .. method:: peek_boot_bios_version()

            Reads boot bios version from the object.

            :rtype: None or boot bios version of the HBA

        .. method:: peek_boot_bios_enabled()

            Reads boot bios enabled from the object.

            :rtype: None or boolean indicating boot bios state

        .. method:: peek_hba_port_list()

            Reads hba port list from the object.

            :rtype: None or list of HBA port(s)


        """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.fdmi_hba,
                         "/rest/running/brocade-fdmi/hba",
                         version.VER_RANGE_820a_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "hba-id", pyfos_type.type_wwn,
            None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute(
            "domain-id", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "manufacturer", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "serial-number", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "model", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "model-description", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "node-name", pyfos_type.type_wwn,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "node-symbolic-name", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "hardware-version", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "driver-version", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "option-rom-version", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "firmware-version", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "os-name-and-version", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "max-ct-payload", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "vendor-id", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "vendor-specific-info", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "number-of-ports", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "fabric-name", pyfos_type.type_wwn,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "boot-bios-version", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "boot-bios-enabled", pyfos_type.type_bool,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "hba-port-list", pyfos_type.type_wwn,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute(
            "wwn", pyfos_type.type_wwn,
            None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST), ["hba-port-list"])

        self.load(dictvalues, 1)


class port(pyfos_rest_util.rest_object):
    """Class of FDMI port

    Important class members:

        +----------------------------------------+-------------------------------+----------------------------------------------------+
        | Attribute name                         | Description                   |Frequstly used methods                              |
        +========================================+===============================+====================================================+
        | port-name                              | Port name                     |:meth:`peek_port_name`                              |
        +----------------------------------------+-------------------------------+----------------------------------------------------+
        | hba-id                                 | Unique HBA identifier         |:meth:`peek_hba_id`                                 |
        +----------------------------------------+-------------------------------+----------------------------------------------------+
        | domain-id                              | Domain ID HBA port is directly|:meth:`peek_domain_id`                              |
        |                                        | attached to                   |                                                    |
        +----------------------------------------+-------------------------------+----------------------------------------------------+
        | port-symbolic-name                     | Symbolic port name            |:meth:`peek_port_symbolic_name`                     |
        +----------------------------------------+-------------------------------+----------------------------------------------------+
        | port-id                                | Port identifier               |:meth:`peek_port_id`                                |
        +----------------------------------------+-------------------------------+----------------------------------------------------+
        | port-type                              | Port type                     |:meth:`peek_port_type`                              |
        +----------------------------------------+-------------------------------+----------------------------------------------------+
        | supported-class-of-service             | Supported class of service(s) |:meth:`peek_supported_class_of_service`             |
        +----------------------------------------+-------------------------------+----------------------------------------------------+
        | supported-fc4-type                     | Supported FC4 type(s)         |:meth:`peek_supported_fc4_type`                     |
        +----------------------------------------+-------------------------------+----------------------------------------------------+
        | active-fc4-type                        | Active FC4 type               |:meth:`peek_active_fc4_type`                        |
        +----------------------------------------+-------------------------------+----------------------------------------------------+
        | supported-speed                        | Supported port speed(s)       |:meth:`peek_supported_speed`                        |
        +----------------------------------------+-------------------------------+----------------------------------------------------+
        | current-port-speed                     | Current port speed            |:meth:`peek_current_port_speed`                     |
        +----------------------------------------+-------------------------------+----------------------------------------------------+
        | maximum-frame-size                     | Maximum frame size            |:meth:`peek_maximum_frame_size`                     |
        +----------------------------------------+-------------------------------+----------------------------------------------------+
        | os-device-name                         | OS device name                |:meth:`peek_os_device_name`                         |
        +----------------------------------------+-------------------------------+----------------------------------------------------+
        | host-name                              | Host name                     |:meth:`peek_host_name`                              |
        +----------------------------------------+-------------------------------+----------------------------------------------------+
        | node-name                              | Node name                     |:meth:`peek_node_name`                              |
        +----------------------------------------+-------------------------------+----------------------------------------------------+
        | fabric-name                            | Fabric name                   |:meth:`peek_fabric_name`                            |
        +----------------------------------------+-------------------------------+----------------------------------------------------+
        | port-state                             | State of the port             |:meth:`peek_port_state`                             |
        +----------------------------------------+-------------------------------+----------------------------------------------------+
        | number-of-discovered-ports             | Number of discovered ports    |:meth:`peek_number_of_discovered_ports`             |
        +----------------------------------------+-------------------------------+----------------------------------------------------+
        | vsa-service-category                   | VSA service category          |:meth:`peek_vsa_service_category`                   |
        +----------------------------------------+-------------------------------+----------------------------------------------------+
        | vsa-guid                               | VSA GUID                      |:meth:`peek_vsa_guid`                               |
        +----------------------------------------+-------------------------------+----------------------------------------------------+
        | vsa-version                            | VSA version                   |:meth:`peek_vsa_version`                            |
        +----------------------------------------+-------------------------------+----------------------------------------------------+
        | vsa-product-name                       | VSA product name              |:meth:`peek_vsa_product_name`                       |
        +----------------------------------------+-------------------------------+----------------------------------------------------+
        | vsa-port-info                          | VSA port info                 |:meth:`peek_vsa_port_info`                          |
        +----------------------------------------+-------------------------------+----------------------------------------------------+
        | vsa-qos-supported                      | VSA QOS support               |:meth:`peek_vsa_qos_supported`                      |
        +----------------------------------------+-------------------------------+----------------------------------------------------+
        | vsa-security                           | VSA security                  |:meth:`peek_vsa_security`                           |
        +----------------------------------------+-------------------------------+----------------------------------------------------+
        | vsa-connected-ports                    | List of VSA connected port(s) |:meth:`peek_vsa_connected_ports`                    |
        +----------------------------------------+-------------------------------+----------------------------------------------------+
        | vsa-storage-array-family               | VSA storage array family      |:meth:`peek_vsa_storage_array_family`               |
        +----------------------------------------+-------------------------------+----------------------------------------------------+
        | vsa-storage-array-name                 | VSA storage array name        |:meth:`peek_vsa_storage_array_name`                 |
        +----------------------------------------+-------------------------------+----------------------------------------------------+
        | vsa-storage-array-system-model         | VSA storage array system model|:meth:`peek_vsa_storage_array_system_model`         |
        +----------------------------------------+-------------------------------+----------------------------------------------------+
        | vsa-storage-array-os                   | VSA storage array OS          |:meth:`peek_vsa_storage_array_os`                   |
        +----------------------------------------+-------------------------------+----------------------------------------------------+
        | vsa-storage-array-node-count           | VSA storage array node count  |:meth:`peek_vsa_storage_array_node_count`           |
        +----------------------------------------+-------------------------------+----------------------------------------------------+
        | vsa-storage-array-nodes                | List of VSA storage array     |:meth:`peek_vsa_storage_array_nodes`                |
        |                                        | node(s)                       |                                                    |
        +----------------------------------------+-------------------------------+----------------------------------------------------+

    *Object methods*

        .. staticmethod:: get(session, port_name=None)

            Returns a :class:`port` object or a list of objects filled with
            FDMI port attributes.

            Each object can be printed using :func:`pyfos_util.response_print`
            and individual attributes accessed through peek methods.

            :param session: session handler returned by
                    :func:`pyfos_auth.login`
            :rtype: :class:`port` object or list of objects. Dictionary in case
                    of error.

    *Attribute methods*

        .. method:: peek_port_name()

            Reads port name from the object.

            :rtype: None or port name

        .. method:: peek_hba_id()

            Reads HBA identifier from the object.

            :rtype: None or HBA identifier of the HBA

        .. method:: peek_domain_id()

            Reads domain ID from the object.

            :rtype: None or domain ID the HBA port is directly attached to

        .. method:: peek_port_symbolic_name()

            Reads port symbolic name from the object.

            :rtype: None or port symbolic name

        .. method:: peek_port_id()

            Reads port identifier from the object.

            :rtype: None or port identifier

        .. method:: peek_port_type()

            Reads port type from the object.

            :rtype: None or port type

        .. method:: peek_supported_class_of_service()

            Reads supported class of service from the object.

            :rtype: None or supported class of service

        .. method:: peek_supported_fc4_type()

            Reads supported fc4 type from the object.

            :rtype: None or supported fc4 type

        .. method:: peek_active_fc4_type()

            Reads active fc4 type from the object.

            :rtype: None or active fc4 type

        .. method:: peek_supported_speed()

            Reads supported speed from the object.

            :rtype: None or supported speed

        .. method:: peek_current_port_speed()

            Reads current port speed from the object.

            :rtype: None or current port speed

        .. method:: peek_maximum_frame_size()

            Reads maximum frame size from the object.

            :rtype: None or maximum frame size

        .. method:: peek_os_device_name()

            Reads os device name from the object.

            :rtype: None or os device name

        .. method:: peek_host_name()

            Reads host name from the object.

            :rtype: None or host name

        .. method:: peek_node_name()

            Reads node name from the object.

            :rtype: None or node name

        .. method:: peek_fabric_name()

            Reads fabric name from the object.

            :rtype: None or fabric name

        .. method:: peek_port_state()

            Reads port state from the object.

            :rtype: None or port state

        .. method:: peek_number_of_discovered_ports()

            Reads number of discovered ports from the object.

            :rtype: None or number of discovered ports

        .. method:: peek_vsa_service_category()

            Reads VSA service category from the object.

            :rtype: None or VSA service category

        .. method:: peek_vsa_guid()

            Reads VSA GUID from the object.

            :rtype: None or VSA GUID

        .. method:: peek_vsa_version()

            Reads VSA version from the object.

            :rtype: None or VSA version

        .. method:: peek_vsa_product_name()

            Reads VSA product name from the object.

            :rtype: None or VSA product name

        .. method:: peek_vsa_port_info()

            Reads VSA port info from the object.

            :rtype: None or VSA port info

        .. method:: peek_vsa_qos_supported()

            Reads VSA QOS supported from the object.

            :rtype: None or VSA QOS supported

        .. method:: peek_vsa_security()

            Reads VSA security from the object.

            :rtype: None or VSA security

        .. method:: peek_vsa_connected_ports()

            Reads VSA connected ports from the object.

            :rtype: None or VSA connected ports

        .. method:: peek_vsa_storage_array_family()

            Reads VSA storage array family from the object.

            :rtype: None or VSA storage array family

        .. method:: peek_vsa_storage_array_name()

            Reads VSA storage array name from the object.

            :rtype: None or VSA storage array name

        .. method:: peek_vsa_storage_array_system_model()

            Reads VSA storage array system model from the object.

            :rtype: None or VSA storage array system model

        .. method:: peek_vsa_storage_array_os()

            Reads VSA storage array OS from the object.

            :rtype: None or VSA storage array OS

        .. method:: peek_vsa_storage_array_node_count()

            Reads VSA storage array node count from the object.

            :rtype: None or VSA storage array node count

        .. method:: peek_vsa_storage_array_nodes()

            Reads VSA storage array nodes from the object.

            :rtype: None or VSA storage array nodes

        """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.fdmi_port,
                         "/rest/running/brocade-fdmi/port",
                         version.VER_RANGE_820a_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "port-name", pyfos_type.type_wwn,
            None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute(
            "hba-id", pyfos_type.type_wwn,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "domain-id", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "port-symbolic-name", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "port-id", pyfos_type.type_hex_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "port-type", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "supported-class-of-service", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "supported-fc4-type", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "active-fc4-type", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "supported-speed", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "current-port-speed", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "maximum-frame-size", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "os-device-name", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "host-name", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "node-name", pyfos_type.type_wwn,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "fabric-name", pyfos_type.type_wwn,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "port-state", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "number-of-discovered-ports", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "vsa-service-category", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "vsa-guid", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "vsa-version", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "vsa-product-name", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "vsa-port-info", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "vsa-qos-supported", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "vsa-security", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "vsa-storage-array-family", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "vsa-storage-array-name", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "vsa-storage-array-system-model", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "vsa-storage-array-os", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "vsa-storage-array-node-count", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "vsa-storage-array-nodes", pyfos_type.type_str,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute(
            "nodes", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST),
            ["vsa-storage-array-nodes"])
        self.add(pyfos_rest_util.rest_attribute(
            "vsa-connected-ports", pyfos_type.type_wwn,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute(
            "wwns", pyfos_type.type_wwn,
            None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST),
            ["vsa-connected-ports"])

        self.load(dictvalues, 1)
