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

:mod:`pyfos_brocade_name_server` - PyFOS module to provide rest support for Name Server.
*********************************************************************************************************
The :mod:`pyfos_brocade_name_server` provides REST support for Name Server.

"""

from pyfos import pyfos_rest_util
from pyfos.pyfos_type import pyfos_type
import pyfos.pyfos_version as version


class fibrechannel_name_server(pyfos_rest_util.rest_object):
    """Class of Name Server

    Important class members:

        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | Attribute name                    | Description                    |Frequstly used methods                                 |
        +===================================+================================+=======================================================+
        | port-id                           | Fibrechannel address           |:meth:`peek_port_id`                                   |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | class-of-service                  | Class of service levels        |:meth:`peek_class_of_service`                          |
        |                                   | supported by the device        |                                                       |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | port-name                         | Device port WWN                |:meth:`peek_port_name`                                 |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | node-name                         | Device node WWN                |:meth:`peek_node_name`                                 |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | port-symbolic-name                | Symbolic port name of device   |:meth:`peek_port_symbolic_name`                        |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | node-symbolic-name                | Symbolic node name of device   |:meth:`peek_node_symbolic_name`                        |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | fc4-type                          | Registered FC-4 types          |:meth:`peek_fc4_type`                                  |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | port-type                         | List of principal device       |:meth:`peek_port_type`                                 |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | state-change-registeration        | State change registration of   |:meth:`peek_state_change_registration`                 |
        |                                   | device                         |                                                       |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | name-server-device-type           | Definition for the type and    |:meth:`peek_name_server_device_type`                   |
        |                                   | role of a device               |                                                       |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | fabric-port-name                  | The F_Port WWN to which        |:meth:`peek_fabric_port_name`                          |
        |                                   | N_Port connects                |                                                       |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | port-index                        | Index number of N_Port to      |:meth:`peek_port_index`                                |
        |                                   | which device connects          |                                                       |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | share-area                        | Indicates if port uses shared  |:meth:`peek_share_area`                                |
        |                                   | area or 10 bit area addressing |                                                       |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | frame-redirection                 | Port involved in Frame         |:meth:`peek_frame_redirection`                         |
        |                                   | Redirection zoning             |                                                       |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | partial                           | Indicates if device entry is   |:meth:`peek_partial`                                   |
        |                                   | incomplete                     |                                                       |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | lsan                              | Indicates if device is part of |:meth:`peek_lsan`                                      |
        |                                   | active LSAN zone               |                                                       |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | link-speed                        | Displays link speed            |:meth:`peek_link_speed`                                |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | port-properties                   | port properties                |:meth:`peek_port_properties`                           |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | connected-through-ag              | Indicates if device is         |:meth:`peek_connected_through_ag`                      |
        |                                   | connected through AG           |                                                       |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | real-device-behind-ag             | Indicates if device non NPIV   |:meth:`peek_real_device_behind_ag`                     |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | cascaded-ag                       | Indicates if device is         |:meth:`peek_cascaded_ag`                               |
        |                                   | connected via cascaded AG      |                                                       |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | slow-drain-device-quarantine      | Indicates if device is         |:meth:`peek_slow_drain_device_quarantine`              |
        |                                   | credit stalled                 |                                                       |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | fcoe-device                       | Indicates if device is FCoE    |:meth:`peek_fcoe_device`                               |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | fc4-features                      | Indicates registered FC-4      |:meth:`peek_fc4_features`                              |
        |                                   | Features bits for FC-4 Types   |                                                       |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+

    *Object methods*

        .. staticmethod:: get(session, port_id=None)

            Returns a :class:`fibrechannel_name_server` object or a list of
            objects filled with Name Server attributes.

            Each object can be printed using :func:`pyfos_util.response_print`
            and individual attributes accessed through peek methods.

            :param session: session handler returned by
                    :func:`pyfos_auth.login`

            :rtype: :class:`port-id` object or list of objects. Dictionary in
                    case of error.

    *Attribute methods*

        .. method:: peek_port_id()

            Reads port identifier from the object.

            :rtype: None or port identifier of the device

        .. method:: peek_class_of_service()

            Reads class of service from the object.

            :rtype: None or class of service supported by the device.

        .. method:: peek_port_name()

            Reads device port WWN.

            :rtype: None or port WWN of device

        .. method:: peek_node_name()

            Reads device node WWN.

            :rtype: None or node WWN of device

        .. method:: peek_port_symbolic_name()

            Reads symbolic port name of device.

            :rtype: None or symbolic port name of device

        .. method:: peek_node_symbolic_name()

            Reads symbolic node name of the device.

            :rtype: None or symbolic node name of the device

        .. method:: peek_node_name()

            Reads node name from the object.

            :rtype: None or node name of device

        .. method:: peek_fc4_type()

            Reads values of type field.

            :rtype: None or values of type field

        .. method:: peek_port_type()

            Reads principal device.

            :rtype: None or principal device

        .. method:: peek_state_change_registration()

            Reads state change registration of device.

            :rtype: None or state change registration

        .. method:: peek_name_server_device_type()

            Reads type and role of a device.

            :rtype: None or Name Server device type

        .. method:: peek_fabric_port_name()

            Reads the F_Port WWN to which N_Port connects.

            :rtype: None or F_Port WWN

        .. method:: peek_port_index()

            Reads Index number of N_Port.

            :rtype: None or Index number of N_Port

        .. method:: peek_share_area()

            Reads if port uses Brocade Shared Area.

            :rtype: None or share area

        .. method:: peek_frame_redirection()

            Reads port involved in frame redirection zoning.

            :rtype: None or port involved in frame redirection zoning

        .. method:: peek_partial()

            Reads if device entry is incomplete.

            :rtype: None or device entry

        .. method:: peek_lsan()

            Reads active LSAN zone of device.

            :rtype: None or device LSAN zone

        .. method:: peek_link_speed()

            Reads link speed.

            :rtype: None or link speed

        .. method:: peek_port_properties()

            Reads port properties.

            :rtype: None or port properties

        .. method:: peek_connected_through_ag

            Reads if device is connected through AG.

            :rtype: None or if device is connected through AG

        .. method:: peek_real_device_behind_ag()

            Reads if device is not a NPIV connected AG.

            :rtype: None or if device is not a NPIV connected AG

        .. method:: peek_cascaded_ag()

            Reads if device connected via cascaded AG.

            :rtype: None or if device connected via cascaded AG

        .. method:: peek_slow_drain_device_quarantine()

            Reads if device is stalling credit.

            :rtype: None or if device is stalling credit

        .. method:: peek_fcoe_device()

            Reads if device is FCoE.

            :rtype: None or if device is FCoE

        .. method:: peek_fc4_features()

            Reads registered FC-4 features.

            :rtype: None or FC-4 features


        """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.name_server,
                         "/rest/running/brocade-name-server/"
                         "fibrechannel-name-server",
                         version.VER_RANGE_820a_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "port-id", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute(
            "port-name", pyfos_type.type_wwn,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "port-symbolic-name", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "fabric-port-name", pyfos_type.type_wwn,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "node-name", pyfos_type.type_wwn,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "node-symbolic-name", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "class-of-service", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "fc4-type", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "fc4-features", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "port-type", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "state-change-registration", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "name-server-device-type", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "port-index", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "share-area", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
             "frame-redirection", pyfos_type.type_str,
             None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "partial", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "lsan", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "link-speed", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "port-properties", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "cascaded-ag", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "connected-through-ag", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "real-device-behind-ag", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "fcoe-device", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "slow-drain-device-quarantine", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
             "permanent-port-name", pyfos_type.type_str,
             None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.load(dictvalues, 1)
