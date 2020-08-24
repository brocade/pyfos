# Copyright 2020 Brocade Communications Systems LLC.  All rights reserved.
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

:mod:`pyfos_brocade_fabric_traffic_controller` - \
PyFOS module for Fabric Traffic Controller.
********************************************************************************************
The :mod:`pyfos_brocade_fabric_traffic_controller` \
provides REST support for Fabric Traffic Controller.

"""

from pyfos import pyfos_rest_util
from pyfos.pyfos_type import pyfos_type
import pyfos.pyfos_version as version


class fabric_traffic_controller_device(pyfos_rest_util.rest_object):
    """Class of Fabric Traffic Controller


    Important class members:

        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | Attribute name                    | Description                    |Frequstly used methods                                 |
        +===================================+================================+=======================================================+
        | n-port-id                         | Fibre Channel Address          |:meth:`peek_n_port_id`                                 |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | n-port-wwn                        | N_Port World Wide Name         |:meth:`peek_n_port_wwn`                                |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | f-port-wwn                        | Fabric Port World Wide Name    |:meth:`peek_f_port_wwn`                                |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | port-index                        | Port Index                     |:meth:`peek_port_index`                                |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | rdf-registrations                 | Registered Diagnostic          |:meth:`peek_rdf_registrations`                         |
        |                                   | Functions (RDF)                |                                                       |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | congestion-states                 | Congestion States              |:meth:`peek_congestion_states`                         |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | edc-owner                         | Fibre Channel Address of the   |:meth:`peek_edc_owner`                                 |
        |                                   | device that originated the     |                                                       |
        |                                   | Exchange Diagnostic            |                                                       |
        |                                   | Capabilities (EDC) exchange    |                                                       |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | fpin-send-statistics              | FPIN Send statistics           |:meth:`peek_fpin_send_statistics`                      |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | fpin-receive-statistics           | FPIN Receive statistics        |:meth:`peek_fpin_receive_statistics`                   |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | n-port-diagnostic-capabilities    | Diagnostic Capabilities of the |:meth:`peek_n_port_diagnostic_capabilities`            |
        |                                   | N_Port                         |                                                       |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | f-port-diagnostic-capabilities    | Diagnostic Capabilities of the |:meth:`peek_f_port_diagnostic_capabilities`            |
        |                                   | Fabric Port                    |                                                       |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | applied-signaling-capabilities    | Applied Congestion Detection   |:meth:`peek_applied_signaling_capabilities`            |
        |                                   | Signaling Capabilities at this |                                                       |
        |                                   | Port Index                     |                                                       |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+



    *Object methods*

        .. staticmethod:: get(session, n_port_id=None)

            Returns a :class:`fabric_traffic_controller` object or a list of
            objects filled with device attributes.

            Each object can be printed using :func:`pyfos_util.response_print`
            and individual attributes accessed through peek methods.

            :param session: session handler returned by
                    :func:`pyfos_auth.login`

            :rtype: :class:`n-port-id` object or list of objects. Dictionary in
                    case of error.



    *Attribute methods*

        .. method:: peek_n_port_id()

            Reads N_Port Identifier from the object.

            :rtype: None or N_Port Identifier of the device

        .. method:: peek_n_port_wwn()

            Reads N_Port world wide name.

            :rtype: None or N_Port world wide name of device

        .. method:: peek_f_port_wwn()

            Reads Fabric Port world wide name.

            :rtype: None or Fabric Port world wide name of device

        .. method:: peek_port_index()

            Reads Port Index of the N_Port.

            :rtype: None or Port Index number of N_Port

        .. method:: peek_rdf_registrations()

            Reads Registered Diagnostic Functions for the device.

            :rtype: None or Registered Diagnostic Functions for the device

        .. method:: peek_congestion_states()

            Reads Congestion states that apply to the device.

            :rtype: None or Congestion States

        .. method:: peek_edc_owner()

            Reads N_Port Identifier of the device that owns the EDC exchange.

            :rtype: None or N_Port Identifier of the EDC exchange owner

        .. method:: peek_fpin_send_statistics()

            Reads FPIN send statistics from the object.

            :rtype: None or FPIN Send Statistics

        .. method:: peek_fpin_receive_statistics()

            Reads FPIN receive statistics from the object.

            :rtype: None or FPIN Receive Statistics

        .. method:: peek_n_port_diagnostic_capabilities()

            Reads N_Port diagnostic capabilities from the object.

            :rtype: None or N_Port Diagnostic Capabilities

        .. method:: peek_f_port_diagnostic_capabilities()

            Reads Fabric Port diagnostic capabilities from the object.

            :rtype: None or Fabric Port Diagnostic Capabilities

        .. method:: peek_applied_signaling_capabilities()

            Reads Applied signaling capabilities from the object.

            :rtype: None or Applied Signaling Capabilities



        """

    def __init__(self, dictvalues={}):
        super().__init__(
            pyfos_rest_util.rest_obj_type.fabric_traffic_controller,
            "/rest/running/brocade-fabric-traffic-controller/"
            "fabric-traffic-controller-device",
            version.VER_RANGE_900_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "n-port-id", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute(
            "n-port-wwn", pyfos_type.type_wwn,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "f-port-wwn", pyfos_type.type_wwn,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "port-index", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "rdf-registrations", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute(
            "rdf-registration", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST),
            ["rdf-registrations"])
        self.add(pyfos_rest_util.rest_attribute(
            "congestion-states", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute(
            "congestion-state", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST),
            ["congestion-states"])
        self.add(pyfos_rest_util.rest_attribute(
            "edc-owner", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "fpin-send-statistics", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute(
            "peer-congestion-count", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
            ["fpin-send-statistics"])
        self.add(pyfos_rest_util.rest_attribute(
            "congestion-count", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
            ["fpin-send-statistics"])
        self.add(pyfos_rest_util.rest_attribute(
            "link-integrity-count", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
            ["fpin-send-statistics"])
        self.add(pyfos_rest_util.rest_attribute(
            "delivery-count", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
            ["fpin-send-statistics"])
        self.add(pyfos_rest_util.rest_attribute(
            "fpin-receive-statistics", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute(
            "peer-congestion-count", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
            ["fpin-receive-statistics"])
        self.add(pyfos_rest_util.rest_attribute(
            "congestion-count", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
            ["fpin-receive-statistics"])
        self.add(pyfos_rest_util.rest_attribute(
            "link-integrity-count", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
            ["fpin-receive-statistics"])
        self.add(pyfos_rest_util.rest_attribute(
            "delivery-count", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
            ["fpin-receive-statistics"])
        self.add(pyfos_rest_util.rest_attribute(
            "n-port-diagnostic-capabilities", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute(
            "tx-signal-capability", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
            ["n-port-diagnostic-capabilities"])
        self.add(pyfos_rest_util.rest_attribute(
            "tx-signal-cycle", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
            ["n-port-diagnostic-capabilities"])
        self.add(pyfos_rest_util.rest_attribute(
            "tx-signal-scale", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
            ["n-port-diagnostic-capabilities"])
        self.add(pyfos_rest_util.rest_attribute(
            "rx-signal-capability", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
            ["n-port-diagnostic-capabilities"])
        self.add(pyfos_rest_util.rest_attribute(
            "rx-signal-cycle", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
            ["n-port-diagnostic-capabilities"])
        self.add(pyfos_rest_util.rest_attribute(
            "rx-signal-scale", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
            ["n-port-diagnostic-capabilities"])
        self.add(pyfos_rest_util.rest_attribute(
            "degrade-activate-threshold", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
            ["n-port-diagnostic-capabilities"])
        self.add(pyfos_rest_util.rest_attribute(
            "degrade-deactivate-threshold", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
            ["n-port-diagnostic-capabilities"])
        self.add(pyfos_rest_util.rest_attribute(
            "fec-degrade-interval", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
            ["n-port-diagnostic-capabilities"])
        self.add(pyfos_rest_util.rest_attribute(
            "f-port-diagnostic-capabilities", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute(
            "tx-signal-capability", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
            ["f-port-diagnostic-capabilities"])
        self.add(pyfos_rest_util.rest_attribute(
            "tx-signal-cycle", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
            ["f-port-diagnostic-capabilities"])
        self.add(pyfos_rest_util.rest_attribute(
            "tx-signal-scale", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
            ["f-port-diagnostic-capabilities"])
        self.add(pyfos_rest_util.rest_attribute(
            "rx-signal-capability", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
            ["f-port-diagnostic-capabilities"])
        self.add(pyfos_rest_util.rest_attribute(
            "rx-signal-cycle", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
            ["f-port-diagnostic-capabilities"])
        self.add(pyfos_rest_util.rest_attribute(
            "rx-signal-scale", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
            ["f-port-diagnostic-capabilities"])
        self.add(pyfos_rest_util.rest_attribute(
            "degrade-activate-threshold", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
            ["f-port-diagnostic-capabilities"])
        self.add(pyfos_rest_util.rest_attribute(
            "degrade-deactivate-threshold", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
            ["f-port-diagnostic-capabilities"])
        self.add(pyfos_rest_util.rest_attribute(
            "fec-degrade-interval", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
            ["f-port-diagnostic-capabilities"])
        self.add(pyfos_rest_util.rest_attribute(
            "applied-signaling-capabilities", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute(
            "tx-signal-capability", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
            ["applied-signaling-capabilities"])
        self.add(pyfos_rest_util.rest_attribute(
            "tx-signal-cycle", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
            ["applied-signaling-capabilities"])
        self.add(pyfos_rest_util.rest_attribute(
            "tx-signal-scale", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
            ["applied-signaling-capabilities"])
        self.add(pyfos_rest_util.rest_attribute(
            "rx-signal-capability", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
            ["applied-signaling-capabilities"])
        self.add(pyfos_rest_util.rest_attribute(
            "rx-signal-cycle", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
            ["applied-signaling-capabilities"])
        self.add(pyfos_rest_util.rest_attribute(
            "rx-signal-scale", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
            ["applied-signaling-capabilities"])

        self.load(dictvalues, 1)
