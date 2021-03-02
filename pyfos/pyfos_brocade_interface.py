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

:mod:`pyfos_brocade_interface` - PyFOS module for Brocade Interface objects.
******************************************************************************
The :mod:`pyfos_brocade_interface` module provides REST support \
for Brocade interfaces.
"""
from pyfos import pyfos_rest_util
from pyfos.pyfos_type import pyfos_type
import pyfos.pyfos_version as version


class PORT_TYPE:
    N_PORT = 0
    NL_PORT = 1
    UF_NL_PORT = 2
    NX_PORT = 3
    FL_PORT = 6
    E_PORT = 7
    # B_PORT = 7
    G_PORT = 10
    U_PORT = 11
    F_PORT = 15
    L_PORT = 16
    EX_PORT = 19
    D_PORT = 20
    VE_PORT = 25


def port_type_to_str(port_type):
    """Return string value for port type in integer

    :param port_type: port type in :class:`PORT_TYPE`
    :rtype: port type in string value
    """
    if port_type == PORT_TYPE.N_PORT:
        return "N_PORT"
    elif port_type == PORT_TYPE.NL_PORT:
        return "NL_PORT"
    elif port_type == PORT_TYPE.UF_NL_PORT:
        return "UF_NL_PORT"
    elif port_type == PORT_TYPE.NX_PORT:
        return "NX_PORT"
    elif port_type == PORT_TYPE.FL_PORT:
        return "FL_PORT"
    elif port_type == PORT_TYPE.E_PORT:
        return "E_PORT"
    elif port_type == PORT_TYPE.G_PORT:
        return "G_PORT"
    elif port_type == PORT_TYPE.U_PORT:
        return "U_PORT"
    elif port_type == PORT_TYPE.F_PORT:
        return "F_PORT"
    elif port_type == PORT_TYPE.L_PORT:
        return "L_PORT"
    elif port_type == PORT_TYPE.EX_PORT:
        return "EX_PORT"
    elif port_type == PORT_TYPE.D_PORT:
        return "D_PORT"
    elif port_type == PORT_TYPE.VE_PORT:
        return "VE_PORT"
    else:
        return "Unknown"


class SPEED_TYPE:
    AUTO = 0
    G1FC = 1000000000
    G2FC = 2000000000
    G4FC = 4000000000
    G8FC = 8000000000
    G10FC = 10000000000
    G16FC = 16000000000
    G32FC = 32000000000
    G128FC = 128000000000


def speed_type_to_str(speed_type):
    """Return string value for speed type in integer

    :param speed_type: speed type in :class:`SPEED_TYPE`
    :rtype: speed type in string value
    """
    if speed_type == SPEED_TYPE.AUTO:
        return "AUTO"
    elif speed_type == SPEED_TYPE.G1FC:
        return "1G_FC"
    elif speed_type == SPEED_TYPE.G2FC:
        return "2G_FC"
    elif speed_type == SPEED_TYPE.G4FC:
        return "4G_FC"
    elif speed_type == SPEED_TYPE.G8FC:
        return "8G_FC"
    elif speed_type == SPEED_TYPE.G10FC:
        return "10_GFC"
    elif speed_type == SPEED_TYPE.G16FC:
        return "16_GFC"
    elif speed_type == SPEED_TYPE.G32FC:
        return "32_FC"
    elif speed_type == SPEED_TYPE.G128FC:
        return "128_FC"
    else:
        return "Speed unknown"


class OPERATIONAL_STATUS_TYPE:
    ONLINE = 2
    TESTING = 2
    OFFLINE = 3
    FAULTY = 5


def operational_status_type_to_str(speed_type):
    """Return string value for operational status type in integer

    :param os_type: operational status type in :class:`OPERATIONAL_STATUS_TYPE`
    :rtype: operational status type in string value
    """
    if speed_type == OPERATIONAL_STATUS_TYPE.ONLINE:
        return "ONLINE"
    elif speed_type == OPERATIONAL_STATUS_TYPE.TESTING:
        return "TESTING"
    elif speed_type == OPERATIONAL_STATUS_TYPE.OFFLINE:
        return "OFFLINE"
    elif speed_type == OPERATIONAL_STATUS_TYPE.FAULTY:
        return "FAULTY"
    else:
        return "Status unknown"


class ENABLED_STATE_TYPE:
    ONLINE = 2
    OFFLINE = 6
    TESTING = 7
    FAULTY = 20


def enabled_state_type_to_str(speed_type):
    """Return string value for enable state type in integer

    :param es_type: enabled state type in :class:`ENABLED_STATE_TYPE`
    :rtype: enabled state type in string value
    """
    if speed_type == ENABLED_STATE_TYPE.ONLINE:
        return "ONLINE"
    elif speed_type == ENABLED_STATE_TYPE.TESTING:
        return "TESTING"
    elif speed_type == ENABLED_STATE_TYPE.OFFLINE:
        return "OFFLINE"
    elif speed_type == ENABLED_STATE_TYPE.FAULTY:
        return "FAULTY"
    else:
        return "State unknown"


class fibrechannel(pyfos_rest_util.rest_object):
    """Class of FC ports

    Important Class Members:

        +-------------------------------+-------------------------------+------------------------------------------------+
        | Attribute name                | Description                   |Frequstly used methods                          |
        +===============================+===============================+================================================+
        | name                          | name of port                  |:func:`set_name`                                |
        |                               |                               |:func:`peek_name`                               |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | wwn                           | WWN of port                   |:func:`peek_wwn`                                |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | operational-status            | current operational status    |:func:`peek_operational_status`                 |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | enabled_state                 | enabled state of port         |:func:`set_enabled_state`                       |
        |                               |                               |:func:`peek_enabled_state`                      |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | user-friendly-name            | string name of port           |:func:`set_user_friendly_name`                  |
        |                               |                               |:func:`peek_user_friendly_name`                 |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | speed                         | speed of port                 |:func:`set_speed`                               |
        |                               |                               |:func:`peek_speed`                              |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | auto-negotiate                | indicate if auto negotiate is |:func:`peek_auto_negotiate`                     |
        |                               | enabled or not                |                                                |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | g-port-locked                 | indicate locked to G_Port     |:func:`set_g_port_locked`                       |
        |                               |                               |:func:`peek_g_port_locked`                      |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | n-port-enabled                | Port is configured as N-port  |:func:`set_n_port_enabled`                      |
        |                               | when switch is in Access      |:func:`peek_n_port_enabled`                     |
        |                               | Gateway mode                  |                                                |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | e-port-disable                | indicate E_Port disabled      |:func:`set_e_port_disable`                      |
        |                               |                               |:func:`peek_e_port_disable`                     |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | d-port-enable                 | indicate D_Port enabled       |:func:`set_d_port_enable`                       |
        |                               |                               |:func:`peek_d_port_enable`                      |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | persistent-disable            | indicate persistently disabled|:func:`set_persistent_disable`                  |
        |                               | port                          |:func:`peek_persistent_disable`                 |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | neighboar/wwn                 | list of neighbors' WWNs       |:func:`peek_neighbor_wwn`                       |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | neighbor-node-wwn             | The neighbor node WWN         | :func:`peek_neighbor_node_wwn`                 |
        |                               | logically connected to this   |                                                |
        |                               | port.                         |                                                |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | fcid                          | FCID of port                  |:func:`peek_fcid`                               |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | port-type                     | type of port                  |:func:`peek_port_type`                          |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | qos-enabled                   | indicate QoS mode             |:func:`set_qos_enabled`                         |
        |                               |                               |:func:`peek_qos_enabled`                        |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | compression-configured        | indicate compression mode     |:func:`set_compression_configured`              |
        |                               |                               |:func:`peek_compression_configured`             |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | compression-active            | indicate active compression   |:func:`peek_compression_active`                 |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | encryption-active             | indicate active encryption    |:func:`peek_encryption_active`                  |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | target-driven-zoning-enable   | target driven zoning mode     |:func:`set_target_driven_zoning_enable`         |
        |                               |                               |:func:`peek_target_driven_zoning_enable`        |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | mirror-port-enabled           | mirrorport  mode              |:func:`set_mirror_port_enabled`                 |
        |                               |                               |:func:`peek_mirror_port_enabled`                |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | sim-port-enabled              | sim port mode                 |:func:`set_sim_port_enabled`                    |
        |                               |                               |:func:`peek_sim_port_enabled`                   |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | isl-ready-mode-enabled        | isl ready mode                |:func:`set_isl_ready_mode_enabled`              |
        |                               |                               |:func:`peek_isl_ready_mode_enabled`             |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | trunk-port-enabled            | trunk-port-enabled            |:func:`set_trunk_port_enabled`                  |
        |                               |                               |:func:`peek_trunk_port_enabled`                 |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | long-distance                 | long distance                 |:func:`peek_long_distance`                      |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | vc-link-init                  | vc link init                  |:func:`peek_vc_link_init`                       |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | ex-port-enabled               | ex port mode                  |:func:`set_ex_port_enabled`                     |
        |                               |                               |:func:`peek_ex_port_enabled`                    |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | edge-fabric-id                | Specifies the fabric ID. The  | :func:`set_edge_fabric_id`                     |
        |                               | valid values for FID are from | :func:`peek_edge_fabric_id`                    |
        |                               | 1 through 128.                |                                                |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | preferred-front-domain-id     | Specifies the preferred domain| :func:`set_preferred_front_domain_id`          |
        |                               | ID. the valid values are 1 to | :func:`peek_preferred_front_domain_id`         |
        |                               | 239.                          |                                                |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | neighbor-switch-ipv4-address  | The IPv4 address of the switch| :func:`peek_neighbor_switch_ipv4_address`      |
        |                               | connected to the EX-port. In  |                                                |
        |                               | case of trunked EX-Ports, IP  |                                                |
        |                               | address will be available     |                                                |
        |                               | only on the master port.      |                                                |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | neighbor-switch-ipv6-address  | The IPv6 address of the switch| :func:`peek_neighbor_switch_ipv6_address`      |
        |                               | connected to the EX-port. In  |                                                |
        |                               | case of trunked EX-Ports, IP  |                                                |
        |                               | address will be available     |                                                |
        |                               | only on the master port.      |                                                |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | npiv-enabled                  | Npiv Enabled                  |:func:`set_npiv_enabled`                        |
        |                               |                               |:func:`peek_npiv_enabled`                       |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | npiv-pp-limit                 | Npiv pp-limit                 |:func:`set_npiv_pp_limit`                       |
        |                               |                               |:func:`peek_npiv_pp_limit`                      |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | rate-limit-enabled            | Rate Limit                    |:func:`set_rate_limit_enabled`                  |
        |                               |                               |:func:`peek_rate_limit_enabled`                 |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | csctl-mode-enabled            | csctl mode                    |:func:`set_csctl_mode_enabled`                  |
        |                               |                               |:func:`peek_csctl_mode_enabled`                 |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | port-autodisable-enabled      | port autodisable mode         |:func:`set_port_autodisable_enabled`            |
        |                               |                               |:func:`peek_port_autodisable_enabled`           |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | e-port-credit                 | e-port-credit                 |:func:`set_e_port_credit`                       |
        |                               |                               |:func:`peek_e_port_credit`                      |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | octet-speed-combo             | octet-speed-combo             |:func:`set_octet_speed_combo`                   |
        |                               |                               |:func:`peek_octet_speed_combo`                  |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | non-dfe-enabled               | non-dfe enabled               |:func:`set_non_dfe_enabled`                     |
        |                               |                               |:func:`peek_non_dfe_enabled`                    |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | fec-enabled                   | fec mode                      |:func:`set_fec_enabled`                         |
        |                               |                               |:func:`peek_fec_enabled`                        |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | via-tts-fec-enabled           | via-tts-fec mode              |:func:`set_via_tts_fec_enabled`                 |
        |                               |                               |:func:`peek_via_tts_fec_enabled`                |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | npiv-flogi-logout-enabled     | npiv-flogi-logout mode        |:func:`set_npiv_flogi_logout_enabled`           |
        |                               |                               |:func:`peek_npiv_flogi_logout_enabled`          |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | f-port-buffers                | f-port-buffers                |:func:`set_f_port_buffers`                      |
        |                               |                               |:func:`peek_f_port_buffers`                     |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | fault-delay-enabled           | fault-delay mode              |:func:`set_fault_delay_enabled`                 |
        |                               |                               |:func:`peek_fault_delay_enabled`                |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | credit-recovery-enabled       | credit recovery mode          |:func:`set_credit_recovery_enabled`             |
        |                               |                               |:func:`peek_credit_recovery_enabled`            |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | rscn-suppression-enabled      | rscn suppression mode         |:func:`set_rscn_suppression_enabled`            |
        |                               |                               |:func:`peek_rscn_suppression_enabled`           |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | los-tov-mode-enabled          | los tov mode mode             |:func:`set_los_tov_mode_enabled`                |
        |                               |                               |:func:`peek_los_tov_mode_enabled`               |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | credit-recovery-active        | credit recovery active state  |:func:`peek_credir_recovery_active`             |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | fec-active                    | fec active state              |:func:`peek_fec_active`                         |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | max-speed			| Max Speed of the port         |:func:`peek_max_speed` 		         |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | default-index			| Default Index of the port	|:func:`peek_default_index`		         |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | pod-license-status		| License status of the port	|:func:`peek_pod_license_status`	         |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | physical-state		| Physical status of the port	|:func:`peek_physical_state`		         |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | is-enabled_state              | enabled state of port         |:func:`set_is_enabled_state`                    |
        |                               |                               |:func:`peek_is_enabled_state`                   |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | segmentation-reason		| Segmentation reason for port	|:func:`peek_segmentation_reason`	         |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | port-type-string		| Type of a port in string	|:func:`peek_port_type_string`		         |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | encryption-enabled		| Encryption enable/disable	|:func:`peek_encryption_enabled`	         |
        |                               |                               |:func:`set_encryption_enabled`                  |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | compression-configured	| Compression enable/disable	|:func:`peek_compression_configured`	         |
        |                               |                               |:func:`set_compression_configured`              |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | port-peer-beacon-enabled	| port peer beacon enable/	|:func:`peek_port_peer_beacon_enabled`	         |
        |                               | disable			|:func:`set_port_peer_beacon_enabled`            |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | pod-license-state		| License enable/disable for a	|:func:`peek_pod_license_state`		         |
        |                               | port				|:func:`set_pod_license_state` 		         |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | reserved-buffers		| reserved-buffers of a port	|:func:`peek_reserved_buffers`		         |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | average-transmit-buffer-usage	| Avg transmit buffer usage of  |:func:`peek_average_transmit_buffer_usage`      |
        |                               | a port			|						 |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | average-transmit-frame-size	| Avg transmit frame size of	|:func:`peek_average_transmit_frame_size`        |
        |                               | a port			|					         |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | average-receive-buffer-usage	| Avg receive buffer usage of	|:func:`peek_average_receive_buffer_usage`       |
        |                               | a port			|						 |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | average-receive-frame-size	| Avg transmit frame size of	|:func:`peek_average_receive_frame_size`         |
        |                               | a port			|					         |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | current-buffer-usage		| current buffer usage of port	|:func:`peek_current_buffer_usage`	         |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | recommended-buffers		| recommended buffers for a port|:func:`peek_recommended_buffers`	         |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | measured-link-distance	| measured-link-distance of port|:func:`peek_measured_link_distance`	         |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | chip-instance			| chip instance where port is 	|:func:`peek_chip_instance`		         |
        |                               | present			|					         |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | chip-buffers-available	| chip buffers available for    |:func:`peek_chip_buffers_available`	         |
        |                               | a port			|					         |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | port-health			| port health			|:func:`peek_port_health`		         |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | authentication-protocol	| authentication protocol	|:func:`peek_authentication_protocol`	         |
        |                               | enabled for a port		|					         |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | disable-reason		| port disable reason		|:func:`peek_disable_reason`		         |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | le-domain			| Translated domain of a port	|:func:`peek_le_domain`		 	         |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | clean-address-enabled		| Clean address mode enable/	|:func:`peek_clean_address_enabled`	         |
        |                               | disable			|:func:`set_clean_address_enabled`               |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | congestion-signal-enabled	| Congestion signal enable/	|:func:`peek_congestion_signal_enabled`	         |
        |                               | disable                       |:func:`set_congestion_signal_enabled`           |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | areas/area                    | list of areas in the switch   |:func:`peek_areas_area`                         |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | index                         | user-port of the port         |:func:`peek_index`                              |
        +-------------------------------+-------------------------------+------------------------------------------------+
        | neighbor-port-index           | The neighbor port index       |:func:`peek_neighbor_port_index`                |
        |                               | logically connected to this   |                                                |
        |                               | port.                         |                                                |
        +-------------------------------+-------------------------------+------------------------------------------------+
        |  neighbor-switch-user         | The neighbor switch user      |:func:`peek_neighbor_switch_user_friendly_name` |
        |       -friendly-name          | friendly name logically       |                                                |                                                
        |                               | connected to this port.       |                                                |
        +-------------------------------+-------------------------------+------------------------------------------------+

    *Object methods*

        .. method:: get(session, name=None)

            Returns a :class:`fibrechannel` object or a list of
            objects filled with attributes gathered
            from switch. If optional name is given, either an
            object matching the name of the port is returned
            or an empty object is returned if no match is found.

            Each object can be printed using :func:`pyfos_util.response_print`
            and individual attributes accessed
            through peek methods.

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: a :class:`fibrechannel` object if name is
                given or a list of objects if there are more than one

        .. method:: patch(session)

            Apply configurable attribute(s) within the object to
            a port of the switch.

            *Below is an example using individual sets:*

            .. code-block:: python

                # initialize the switch object
                switch = pyfos_switch.fibrechannel()
                # set the enabled-state attribute to
                # enable the port 0/0 on the switch
                switch.set_name("0/0")
                switch.set_enabled_state(pyfos_switchfcport.enableState)
                # execute HTTP patch command to apply the object to the
                # switch connected through session
                switch.patch(session)

            *Below is an example of combining object \
                    initialization and attribute sets:*

            .. code-block:: python

                # initialize the switch object and set the
                # enable-state attribute
                switch = pyfos_switch.fibrechannel({"name" : "0/0",
                    "enabled-state" : pyfos_switch.enableState})
                # execute HTTP patch command to apply the object to the
                # switch connected through session
                switch.patch(session)

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: a dictionary of error or success information

    *Attribute methods*

        .. method:: set_name(name)

            Sets port name in the object.

            :param name: port name to be set within the object
            :rtype: None or dictionary of error information

        .. method:: peek_name()

            Reads port name in the object.

            :rtype: None or port name

        .. method:: peek_wwn()

            Reads port WWN in the object.

            :rtype: None or port WWN

        .. method:: peek_operational_status()

            Reads operational status of port in the object.

            :rtype: None or port WWN

        .. method:: set_enabled_state(newstate)

            Sets enabled state in the object.

            :param newstate: new port state to be set within the object
            :rtype: None or dictionary of error information

        .. method:: peek_enabled_state()

            Reads enabled state in the object.

            :rtype: None or enabled state

        .. method:: set_user_friendly_name(newname)

            Sets user friendly name in the object.

            :param newname: new name to be set within the object
            :rtype: None or dictionary of error information

        .. method:: peek_user_friendly_name()

            Reads user friendly name in the object.

            :rtype: None or user friendly name

        .. method:: set_speed(newspeed)

            Sets new speed in the object.

            :param newspeed: new speed to be set within the object
            :rtype: None or dictionary of error information

        .. method:: peek_speed()

            Reads speed of port in the object.

            :rtype: None or speed of port

        .. method:: peek_auto_negotiate()

            Reads indicate if auto negotiate mode is on in the object.
            When speed is set to auto negotiate, this attribute will return
            True while speed attribute will indicate the negotiated speed.

            :rtype: None, True, or False

        .. method:: set_g_port_locked(newmode)

            Sets G_Port locked indication in the object.

            :param newmode: new mode to be set within the object
            :rtype: None or dictionary of error information

        .. method:: peek_g_port_locked()

            Reads G_Port locked mode of port in the object.

            :rtype: None, True, or False

        .. method:: set_n_port_enabled(newmode)

            Sets N_Port enabled indication in the object. A port can be
            configured as N-port only when the switch is in
            Access Gateway mode.

            :param newmode: new mode to be set within the object
            :rtype: None or dictionary of error information

        .. method:: peek_n_port_enabled()

            Reads N_Port enabled mode of port in the object.

            :rtype: None, True, or False

        .. method:: set_e_port_disable(newmode)

            Sets E_Port disable mode indication in the object.

            :param newmode: new mode to be set within the object
            :rtype: None or dictionary of error information

        .. method:: peek_e_port_disable()

            Reads E_Port disable mode of port in the object.

            :rtype: None, True, or False

        .. method:: set_d_port_enable(newmode)

            Sets D_Port enable indication in the object.

            :param newmode: new mode to be set within the object
            :rtype: None or dictionary of error information

        .. method:: peek_d_port_enable()

            Reads D_Port mode of port in the object.

            :rtype: None, True, or False

        .. method:: set_persistent_disable(newmode)

            Sets persistently disabled indication in the object.

            :param newmode: new mode to be set within the object
            :rtype: None or dictionary of error information

        .. method:: peek_persistent_disable()

            Reads persistent disabled mode of port in the object.

            :rtype: None, True, or False

        .. method:: peek_neighbor_wwn()

            Reads a list of neighboar WWNs of port in the object.

            :rtype: None or a list of WWNs

        .. function:: peek_neighbor_node_wwn()

            Reads the value assigned to neighbor-node-wwn in the object.

            :rtype: None on error and a value on success.

        .. method:: peek_fcid()

            Reads FCID of port in the object.

            :rtype: None or FCID

        .. method:: peek_port_type()

            Reads port type of port in the object.

            :rtype: None or port type

        .. method:: set_qos_enabled(newmode)

            Sets QoS mode indication in the object.

            :param newmode: new mode to be set within the object
            :rtype: None or dictionary of error information

        .. method:: peek_qos_enabled()

            Reads QoS mode of port in the object.

            :rtype: None, True, or False

        .. method:: set_compression_configured(newmode)

            Sets compression mode indication in the object.

            :param newmode: new mode to be set within the object
            :rtype: None or dictionary of error information

        .. method:: peek_compression_configured()

            Reads compression mode of port in the object.

            :rtype: None, True, or False

        .. method:: peek_compression_active()

            Reads compression mode of port in the object.

            :rtype: None, True, or False

        .. method:: peek_encryption_active()

            Reads encryption mode of port in the object.

            :rtype: None, True, or False

        .. method:: set_target_driven_zoning_enable(newmode)

            Sets target driven zoning mode indication in the object.

            :param newmode: new mode to be set within the object
            :rtype: None or dictionary of error information

        .. method:: peek_target_driven_zoning_enable()

            Reads target driven zoning mode of port in the object.

            :rtype: None, True, or False

        .. method:: set_mirror_port_enabled(newmode)

            Sets mirrorport config for the port in the object.

            :param newmode: new mode to be set within the object
            :rtype: None or dictionary of error information
        .. method:: peek_mirror_port_enabled()

            Gets mirrorport config for the port in the object.

            :param newmode: new mode to be set within the object
            :rtype: None or dictionary of error information

        .. method:: set_sim_port_enabled(newmode)

            Sets simport config for the port in the object.

            :param newmode: new mode to be set within the object
            :rtype: None or dictionary of error information
        .. method:: peek_sim_port_enabled()

            Gets simport config for the port in the object.

            :param newmode: new mode to be set within the object
            :rtype: None or dictionary of error information

        .. method:: set_isl_ready_mode_enabled(newmode)

            Sets isl ready mode config for the port in the object.

            :param newmode: new mode to be set within the object
            :rtype: None or dictionary of error information
        .. method:: peek_isl_ready_mode_enabled()

            Gets isl ready mode config for the port in the object.

            :param newmode: new mode to be set within the object
            :rtype: None or dictionary of error information

        .. method:: set_trunk_port_enabled(newmode)

            Sets trunkport config for the port in the object.

            :param newmode: new mode to be set within the object
            :rtype: None or dictionary of error information
        .. method:: peek_trunk_port_enabled()

            Gets trunkport config for the port in the object.

            :param newmode: new mode to be set within the object
            :rtype: None or dictionary of error information

        .. method:: peek_long_distance()

            Gets long distance mode config for the port in the object.

            :param newmode: new mode to be set within the object
            :rtype: None or dictionary of error information

        .. method:: peek_vc_link_init()

            Gets vc link init mode config for the port in the object.

            :param newmode: new mode to be set within the object
            :rtype: None or dictionary of error information


        .. method:: set_ex_port_enabled(newmode)

            Sets export config for the port in the object.

            :param newmode: new mode to be set within the object
            :rtype: None or dictionary of error information
        .. method:: peek_ex_port_enabled()

            Gets export config for the port in the object.

            :param newmode: new mode to be set within the object
            :rtype: None or dictionary of error information

        .. method:: set_npiv_enabled(newmode)

            Sets npiv capable config for the port in the object.

            :param newmode: new mode to be set within the object
            :rtype: None or dictionary of error information
        .. method:: peek_npiv_enabled()

            Gets npiv capable config for the port in the object.

            :param newmode: new mode to be set within the object
            :rtype: None or dictionary of error information

        .. method:: set_npiv_pp_limit_enabled(newmode)

            Sets npiv login limit config for the port in the object.

            :param newmode: new mode to be set within the object
            :rtype: None or dictionary of error information
        .. method:: peek_npiv_pp_limit_enabled()

            Gets npiv login limit config for the port in the object.

            :param newmode: new mode to be set within the object
            :rtype: None or dictionary of error information

        .. method:: set_rate_limit_enabled(newmode)

            Sets rate limit config for the port in the object.

            :param newmode: new mode to be set within the object
            :rtype: None or dictionary of error information
        .. method:: peek_rate_limit_enabled()

            Gets rate limit config for the port in the object.

            :param newmode: new mode to be set within the object
            :rtype: None or dictionary of error information

        .. method:: set_csctl_mode_enabled(newmode)

            Sets csctl config for the port in the object.

            :param newmode: new mode to be set within the object
            :rtype: None or dictionary of error information
        .. method:: peek_csctl_mode_enabled()

            Gets csctl config for the port in the object.

            :param newmode: new mode to be set within the object
            :rtype: None or dictionary of error information

        .. method:: set_port_autodisable_enabled(newmode)

            Sets port auto disable mode config for the port in the object.

            :param newmode: new mode to be set within the object
            :rtype: None or dictionary of error information
        .. method:: peek_port_autodisable_enabled()

            Gets port auto disable mode config for the port in the object.

            :param newmode: new mode to be set within the object
            :rtype: None or dictionary of error information

        .. method:: set_e_port_credit(newmode)

            Sets e port credits config for the port in the object.

            :param newmode: new mode to be set within the object
            :rtype: None or dictionary of error information
        .. method:: peek_e_port_credit()

            Gets e port credits config for the port in the object.

            :param newmode: new mode to be set within the object
            :rtype: None or dictionary of error information

        .. method:: set_octet_speed_combo(newmode)

            Sets octet speed combo config for the port in the object.

            :param newmode: new mode to be set within the object
            :rtype: None or dictionary of error information
        .. method:: peek_octet_speed_combo()

            Gets octet speed combo config for the port in the object.

            :param newmode: new mode to be set within the object
            :rtype: None or dictionary of error information

        .. method:: set_non_dfe_enabled(newmode)

            Sets non-dfe config for the port in the object.

            :param newmode: new mode to be set within the object
            :rtype: None or dictionary of error information
        .. method:: peek_non_dfe_enabled()

            Gets non-dfe config for the port in the object.

            :param newmode: new mode to be set within the object
            :rtype: None or dictionary of error information

        .. method:: set_fec_enabled(newmode)

            Sets fec config for the port in the object.

            :param newmode: new mode to be set within the object
            :rtype: None or dictionary of error information
        .. method:: peek_fec_enabled()

            Gets fec config for the port in the object.

            :param newmode: new mode to be set within the object
            :rtype: None or dictionary of error information

        .. method:: peek_via_tts_fec_enabled()

            Gets fec via tts config for the port in the object.

            :param newmode: new mode to be set within the object
            :rtype: None or dictionary of error information

        .. method:: peek_npiv_flogi_logout_enabled()

            Gets npiv flogi logout config for the port in the object.

            :param newmode: new mode to be set within the object
            :rtype: None or dictionary of error information

        .. method:: set_f_port_buffers(newmode)

            Sets f port buffers config for the port in the object.

            :param newmode: new mode to be set within the object
            :rtype: None or dictionary of error information
        .. method:: peek_f_port_buffers()

            Gets f port buffers config for the port in the object.

            :param newmode: new mode to be set within the object
            :rtype: None or dictionary of error information

        .. method:: set_fault_delay_enabled(newmode)

            Sets falut delay  config for the port in the object.

            :param newmode: new mode to be set within the object
            :rtype: None or dictionary of error information
        .. method:: peek_fault_delay_enabled()

            Gets falut delay  config for the port in the object.

            :param newmode: new mode to be set within the object
            :rtype: None or dictionary of error information

        .. method:: set_credit_recovery_enabled(newmode)

            Sets credit recovery config for the port in the object.

            :param newmode: new mode to be set within the object
            :rtype: None or dictionary of error information
        .. method:: peek_credit_recovery_enabled()

            Gets credit recovery config for the port in the object.

            :param newmode: new mode to be set within the object
            :rtype: None or dictionary of error information

        .. method:: set_rscn_suppression_enabled(newmode)

            Sets rscn suppression config for the port in the object.

            :param newmode: new mode to be set within the object
            :rtype: None or dictionary of error information
        .. method:: peek_rscn_suppression_enabled()

            Gets rscn suppression config for the port in the object.

            :param newmode: new mode to be set within the object
            :rtype: None or dictionary of error information

        .. method:: set_los_tov_mode_enabled(newmode)

            Sets los tov mode config for the port in the object.

            :param newmode: new mode to be set within the object
            :rtype: None or dictionary of error information
        .. method:: peek_los_tov_mode_enabled()

            Gets los tov mode config for the port in the object.

            :param newmode: new mode to be set within the object
            :rtype: None or dictionary of error information

        .. method:: peek_credit_recovery_active()

            Gets the status of the credit recovery's active status

            :rtype: Returns the state of credit recovery of port.

        .. method:: peek_fec_active()

            Gets the status of the fec's active status

            :rtype: Returns the state of fec of port.

        .. method:: peek_max_speed()

            Gets the max speed of the Port is capable of.

            :rtype: Returns Max Speed of The Port

        .. method:: peek_default_index()

            Gets the default index of the port

            :rtype: Returns default index of the port

        .. method:: set_is_enabled_state(newstate)

            Sets enabled state of the port in the object.

            :param newstate: new port state to be set within the object
            :rtype: None or dictionary of error information

        .. method:: peek_is_enabled_state()

            Reads enabled state of the port in the object.

            :rtype: None or enabled state

        .. function:: peek_chip_instance()

            Reads the value assigned to chip-instance in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_clean_address_enabled()

            Reads the value assigned to clean-address-enabled in the object.

            :rtype: None on error and a value on success.


        .. function:: set_clean_address_enabled(value)

            Set the value of clean-address-enabled in the object.

            :rtype: A dictionary of error or a success response and a value
             with "clean-address-enabled" as the key

        .. function:: peek_current_buffer_usage()

            Reads the value assigned to current-buffer-usage in the object.

            :rtype: None on error and a value on success.

        .. function:: peek_compression_configured()

            Reads the value assigned to compression-configured in the
             object.

            :rtype: None on error and a value on success.

        .. function:: set_compression_configured(value)

            Set the value of compression-configured in the object.

            :rtype: A dictionary of error or a success response and a value
             with "compression-configured" as the key

        .. function:: peek_le_domain()

            Reads the value assigned to le-domain in the object.

            :rtype: None on error and a value on success.

        .. function:: peek_port_health()

            Reads the value assigned to port-health in the object.

            :rtype: None on error and a value on success.

        .. function:: peek_recommended_buffers()

            Reads the value assigned to recommended-buffers in the object.

            :rtype: None on error and a value on success.

        .. function:: peek_pod_license_status()

            Reads the value assigned to pod-license-status in the object.

            :rtype: None on error and a value on success.

        .. function:: peek_average_receive_buffer_usage()

            Reads the value assigned to average-receive-buffer-usage in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_average_receive_frame_size()

            Reads the value assigned to average-receive-frame-size in the
             object.

            :rtype: None on error and a value on success.

        .. function:: peek_pod_license_state()

            Reads the value assigned to pod-license-state in the object.

            :rtype: None on error and a value on success.


        .. function:: set_pod_license_state(value)

            Set the value of pod-license-state in the object.

            :rtype: A dictionary of error or a success response and a value
             with "pod-license-state" as the key

        .. function:: peek_chip_buffers_available()

            Reads the value assigned to chip-buffers-available in the
             object.

            :rtype: None on error and a value on success.

        .. function:: peek_port_peer_beacon_enabled()

            Reads the value assigned to port-peer-beacon-enabled in the
             object.

            :rtype: None on error and a value on success.


        .. function:: set_port_peer_beacon_enabled(value)

            Set the value of port-peer-beacon-enabled in the object.

            :rtype: A dictionary of error or a success response and a value
             with "port-peer-beacon-enabled" as the key

        .. function:: peek_port_type_string()

            Reads the value assigned to port-type-string in the object.

            :rtype: None on error and a value on success.

        .. function:: peek_encryption_enabled()

            Reads the value assigned to encryption-enabled in the object.

            :rtype: None on error and a value on success.

        .. function:: set_encryption_enabled(value)

            Set the value of encryption-enabled in the object.

            :rtype: A dictionary of error or a success response and a value
             with "encryption-enabled" as the key

        .. function:: peek_disable_reason()

            Reads the value assigned to disable-reason in the object.

            :rtype: None on error and a value on success.

        .. function:: peek_segmentation_reason()

            Reads the value assigned to segmentation-reason in the object.

            :rtype: None on error and a value on success.

        .. function:: peek_reserved_buffers()

            Reads the value assigned to reserved-buffers in the object.

            :rtype: None on error and a value on success.

        .. function:: peek_average_transmit_frame_size()

            Reads the value assigned to average-transmit-frame-size in the
             object.

            :rtype: None on error and a value on success.

        .. function:: peek_measured_link_distance()

            Reads the value assigned to measured-link-distance in the
             object.

            :rtype: None on error and a value on success.

        .. function:: peek_average_transmit_buffer_usage()

            Reads the value assigned to average-transmit-buffer-usage in the
             object.

            :rtype: None on error and a value on success.

        .. function:: peek_authentication_protocol()

            Reads the value assigned to authentication-protocol in the
             object.

            :rtype: None on error and a value on success.

        .. function:: peek_congestion_signal_enabled()

            Reads the value assigned to congestion-signal-enabled in the
             object.

            :rtype: None on error and a value on success.

        .. function:: set_congestion_signal_enabled(value)

            Set the value of congestion-signal-enabled in the object.

            :rtype: A dictionary of error or a success response and a value
             with "congestion-signal-enabled" as the key

        .. function:: peek_ex_port_enabled()

            Reads the value assigned to ex-port-enabled in the object.

            :rtype: None on error and a value on success.

        .. function:: set_ex_port_enabled(value)

            Set the value of ex-port-enabled in the object.

            :rtype: A dictionary of error or a success response and a value
             with "ex-port-enabled" as the key

        .. function:: peek_edge_fabric_id()

            Reads the value assigned to edge-fabric-id in the object.

            :rtype: None on error and a value on success.

        .. function:: set_edge_fabric_id(value)

            Set the value of edge-fabric-id in the object.

            :rtype: A dictionary of error or a success response and a value
             with "edge-fabric-id" as the key

        .. function:: peek_preferred_front_domain_id()

            Reads the value assigned to preferred-front-domain-id in the
             object.

            :rtype: None on error and a value on success.

        .. function:: set_preferred_front_domain_id(value)

            Set the value of preferred-front-domain-id in the object.

            :rtype: A dictionary of error or a success response and a value
             with "preferred-front-domain-id" as the key

        .. function:: peek_neighbor_switch_ipv4_address()

            Reads the value assigned to neighbor-switch-ipv4-address in the
             object.

            :rtype: None on error and a value on success.

        .. function:: peek_neighbor_switch_ipv6_address()

            Reads the value assigned to neighbor-switch-ipv6-address in the
             object.

            :rtype: None on error and a value on success.

        .. function:: peek_index()

            Reads the value assigned to index in the
             object.

            :rtype: None on error and a value on success.

        .. function:: peek_areas_area()

            Reads the list of areas of the switch in the
             object.

            :rtype: None on error and a value on success.

        .. function:: peek_neighbor_port_index()

            Reads the value assigned to neighbor-port-index in the object.

            :rtype: None on error and a value on success.

        .. function:: peek_neighbor_switch_user_friendly_name()

            Reads the value assigned to neighbor-switch-user-frienly-name in the object.

            :rtype: None on error and a value on success.

     """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.port_config,
                         "/rest/running/brocade-interface/fibrechannel")

        self.add(pyfos_rest_util.rest_attribute(
            "name", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute(
            "wwn", pyfos_type.type_wwn,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "operational-status", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "enabled-state", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "user-friendly-name", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "speed", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "auto-negotiate", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "g-port-locked", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "n-port-enabled", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "e-port-disable", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "d-port-enable", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "persistent-disable", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "neighbor", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute(
            "wwn", pyfos_type.type_na,
            None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST), ["neighbor"])
        self.add(pyfos_rest_util.rest_attribute(
            "neighbor-node-wwn", pyfos_type.type_wwn,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG,
            version.VER_RANGE_820a_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute(
            "fcid", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "port-type", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "qos-enabled", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "compression-configured", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "compression-active", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "encryption-active", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "target-driven-zoning-enable", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "mirror-port-enabled", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG,
            version.VER_RANGE_820a_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute(
            "sim-port-enabled", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG,
            version.VER_RANGE_820a_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute(
            "isl-ready-mode-enabled", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG,
            version.VER_RANGE_820a_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute(
            "trunk-port-enabled", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG,
            version.VER_RANGE_820a_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute(
            "long-distance", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG,
            version.VER_RANGE_820a_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute(
            "vc-link-init", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG,
            version.VER_RANGE_820a_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute(
            "ex-port-enabled", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG,
            version.VER_RANGE_820a_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute(
            "npiv-enabled", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG,
            version.VER_RANGE_820a_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute(
            "npiv-pp-limit", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG,
            version.VER_RANGE_820a_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute(
            "rate-limit-enabled", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG,
            version.VER_RANGE_820a_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute(
            "csctl-mode-enabled", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG,
            version.VER_RANGE_820a_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute(
            "port-autodisable-enabled", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG,
            version.VER_RANGE_820a_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute(
            "e-port-credit", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG,
            version.VER_RANGE_820a_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute(
            "octet-speed-combo", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG,
            version.VER_RANGE_820a_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute(
            "non-dfe-enabled", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG,
            version.VER_RANGE_820a_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute(
            "fec-enabled", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG,
            version.VER_RANGE_820a_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute(
            "via-tts-fec-enabled", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG,
            version.VER_RANGE_820a_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute(
            "npiv-flogi-logout-enabled", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG,
            version.VER_RANGE_820a_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute(
            "f-port-buffers", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG,
            version.VER_RANGE_820a_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute(
            "fault-delay-enabled", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG,
            version.VER_RANGE_820a_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute(
            "credit-recovery-enabled", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG,
            version.VER_RANGE_820a_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute(
            "rscn-suppression-enabled", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG,
            version.VER_RANGE_820a_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute(
            "los-tov-mode-enabled", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG,
            version.VER_RANGE_820a_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute(
            "credit-recovery-active", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG,
            version.VER_RANGE_820a_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute(
            "fec-active", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG,
            version.VER_RANGE_820a_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute(
            "fcid-hex", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG,
            version.VER_RANGE_820a_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute(
            "max-speed", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG,
            version.VER_RANGE_821_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute(
            "default-index", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG,
            version.VER_RANGE_821_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute(
            "pod-license-status", pyfos_type.type_bool,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG,
            version.VER_RANGE_821b_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute(
            "physical-state", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG,
            version.VER_RANGE_821b_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute(
            "is-enabled-state", pyfos_type.type_bool,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG,
            version.VER_RANGE_821b_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute(
            "segmentation-reason", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG,
            version.VER_RANGE_900_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute(
            "port-type-string", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG,
            version.VER_RANGE_900_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute(
            "encryption-enabled", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG,
            version.VER_RANGE_900_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute(
            "compression-configured", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG,
            version.VER_RANGE_900_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute(
            "port-peer-beacon-enabled", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG,
            version.VER_RANGE_900_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute(
            "pod-license-state", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG,
            version.VER_RANGE_900_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute(
            "reserved-buffers", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG,
            version.VER_RANGE_900_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute(
            "average-transmit-buffer-usage", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG,
            version.VER_RANGE_900_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute(
            "average-transmit-frame-size", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG,
            version.VER_RANGE_900_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute(
            "average-receive-buffer-usage", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG,
            version.VER_RANGE_900_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute(
            "average-receive-frame-size", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG,
            version.VER_RANGE_900_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute(
            "current-buffer-usage", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG,
            version.VER_RANGE_900_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute(
            "recommended-buffers", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG,
            version.VER_RANGE_900_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute(
            "measured-link-distance", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG,
            version.VER_RANGE_900_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute(
            "chip-instance", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG,
            version.VER_RANGE_900_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute(
            "chip-buffers-available", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG,
            version.VER_RANGE_900_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute(
            "port-health", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG,
            version.VER_RANGE_900_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute(
            "authentication-protocol", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG,
            version.VER_RANGE_900_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute(
            "disable-reason", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG,
            version.VER_RANGE_900_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute(
            "le-domain", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG,
            version.VER_RANGE_900_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute(
            "clean-address-enabled", pyfos_type.type_bool,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG,
            version.VER_RANGE_900_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute(
            "congestion-signal-enabled", pyfos_type.type_bool,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG,
            version.VER_RANGE_900_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute(
            "edge-fabric-id", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG,
            version.VER_RANGE_900_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute(
            "preferred-front-domain-id", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG,
            version.VER_RANGE_900_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute(
            "neighbor-switch-ipv4-address", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG,
            version.VER_RANGE_900_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute(
            "neighbor-switch-ipv6-address", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG,
            version.VER_RANGE_900_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute(
            "index", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG,
            version.VER_RANGE_900_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute(
            "areas", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER,
            version.VER_RANGE_900_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute(
            "area", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST,
            version.VER_RANGE_900_and_ABOVE), ["areas"])
        self.add(pyfos_rest_util.rest_attribute(
            "neighbor-port-index", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG,
            version.VER_RANGE_901_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute(
            "neighbor-switch-user-friendly-name", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG,
            version.VER_RANGE_901_and_ABOVE))
        # """
        # self.add(pyfos_rest_util.rest_attribute(
        #    "debug", pyfos_type.type_int,
        #    None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        # self.add(pyfos_rest_util.rest_attribute(
        #    "ishttps", pyfos_type.type_int,
        #    None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        # self.add(pyfos_rest_util.rest_attribute(
        #    "ip_addr", pyfos_type.type_int,
        #    None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        # self.add(pyfos_rest_util.rest_attribute(
        #    "version", pyfos_type.type_int,
        #    None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        # self.add(pyfos_rest_util.rest_attribute(
        #    "vfid", pyfos_type.type_int,
        #    None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        # self.add(pyfos_rest_util.rest_attribute(
        #    "credential", pyfos_type.type_int,
        #    None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        # """
        self.load(dictvalues, 1)


class fibrechannel_statistics(pyfos_rest_util.rest_object):
    """Class of FC port statistics

    Important class members:

        +-----------------------------------+-------------------------------+-----------------------------------------------+
        | Attribute name                    | Description                   |Frequstly used methods                         |
        +===================================+===============================+===============================================+
        | name                              | name of port                  |:func:`set_name`                               |
        |                                   |                               |:func:`peek_name`                              |
        +-----------------------------------+-------------------------------+-----------------------------------------------+
        | sampling-interval                 | sampling interval in secs     |:func:`peek_sampling_interval`                 |
        +-----------------------------------+-------------------------------+-----------------------------------------------+
        | time-generated                    | timestamp of stats generation |:func:`peek_time_generated`                    |
        +-----------------------------------+-------------------------------+-----------------------------------------------+
        | reset-statistics                  | reset the stats to zero       |:func:`set_reset_statistics`                   |
        |                                   |                               |:func:`peek_reset_statistics`                  |
        +-----------------------------------+-------------------------------+-----------------------------------------------+
        | in-octets                         | ingress octets                |:func:`peek_in_octets`                         |
        +-----------------------------------+-------------------------------+-----------------------------------------------+
        | out-octets                        | egress octets                 |:func:`peek_out_octets`                        |
        +-----------------------------------+-------------------------------+-----------------------------------------------+
        | in-multicast-pkts                 | ingress multicast packets     |:func:`peek_in_multicast_pkts`                 |
        +-----------------------------------+-------------------------------+-----------------------------------------------+
        | out-multicast-pkts                | egress multicast packets      |:func:`peek_out_multicast_pkts`                |
        +-----------------------------------+-------------------------------+-----------------------------------------------+
        | in-link-resets                    | ingress link resets           |:func:`peek_in_link_resets`                    |
        +-----------------------------------+-------------------------------+-----------------------------------------------+
        | out-link-resets                   | egress link resets            |:func:`peek_out_link_resets`                   |
        +-----------------------------------+-------------------------------+-----------------------------------------------+
        | in-offline-sequences              | ingress offline sequences     |:func:`peek_in_offline_sequences`              |
        +-----------------------------------+-------------------------------+-----------------------------------------------+
        | out-offline-sequences             | egress offline sequences      |:func:`peek_out_offline_sequences`             |
        +-----------------------------------+-------------------------------+-----------------------------------------------+
        | invalid-ordered-sets              | invalid ordered sets          |:func:`peek_invalid_ordered_sets`              |
        +-----------------------------------+-------------------------------+-----------------------------------------------+
        | frames-too-long                   | number of too long frames     |:func:`peek_frames_too_long`                   |
        +-----------------------------------+-------------------------------+-----------------------------------------------+
        | truncated-frames                  | truncated frames              |:func:`peek_truncated_frames`                  |
        +-----------------------------------+-------------------------------+-----------------------------------------------+
        | address-errors                    | address errors                |:func:`peek_address_errors`                    |
        +-----------------------------------+-------------------------------+-----------------------------------------------+
        | delimiter-errors                  | delimiter errors              |:func:`peek_delimiter_errors`                  |
        +-----------------------------------+-------------------------------+-----------------------------------------------+
        | encoding-disparity-errors         | encoding disparity errors     |:func:`peek_encoding_disparity_errors`         |
        +-----------------------------------+-------------------------------+-----------------------------------------------+
        | too-many-rdys                     | too many RDYs                 |:func:`peek_too_many_rdys`                     |
        +-----------------------------------+-------------------------------+-----------------------------------------------+
        | in-crc-errors                     | total ingress CRC errors      |:func:`peek_in_crc_errors`                     |
        +-----------------------------------+-------------------------------+-----------------------------------------------+
        | crc-errors                        | CRC errors                    |:func:`peek_crc_errors`                        |
        +-----------------------------------+-------------------------------+-----------------------------------------------+
        | bad-eofs-received                 | ingress bad EOFs              |:func:`peek_bad_eofs_received`                 |
        +-----------------------------------+-------------------------------+-----------------------------------------------+
        | encoding-errors-outside-frame     | encoding err outside of frames|:func:`peek_encoding_errors_outside_frame`     |
        +-----------------------------------+-------------------------------+-----------------------------------------------+
        | multicast-timeouts                | multicast timeouts            |:func:`peek_multicast_timeouts`                |
        +-----------------------------------+-------------------------------+-----------------------------------------------+
        | in-lcs                            | ingress LCS                   |:func:`peek_in_lcs`                            |
        +-----------------------------------+-------------------------------+-----------------------------------------------+
        | in-frame-rate                     | ingress frame rate            |:func:`peek_in_frame_rate`                     |
        +-----------------------------------+-------------------------------+-----------------------------------------------+
        | out-frame-rate                    | egress frame rate             |:func:`peek_out_frame_rate`                    |
        +-----------------------------------+-------------------------------+-----------------------------------------------+
        | in-max-frame-rate                 | ingress max frame rate        |:func:`peek_in_max_frame_rate`                 |
        +-----------------------------------+-------------------------------+-----------------------------------------------+
        | out-max-frame-rate                | egress max frame rate         |:func:`peek_out_max_frame_rate`                |
        +-----------------------------------+-------------------------------+-----------------------------------------------+
        | in-rate                           | ingress byte rate             |:func:`peek_in_rate`                           |
        +-----------------------------------+-------------------------------+-----------------------------------------------+
        | out-rate                          | egress byte rate              |:func:`peek_out_rate`                          |
        +-----------------------------------+-------------------------------+-----------------------------------------------+
        | in-peak-rate                      | ingress peak rate             |:func:`peek_in_peak_rate`                      |
        +-----------------------------------+-------------------------------+-----------------------------------------------+
        | out-peak-rate                     | egress peak rate              |:func:`peek_out_peak_rate`                     |
        +-----------------------------------+-------------------------------+-----------------------------------------------+
        | in-frames                         | ingress frames                |:func:`peek_in_frames`                         |
        +-----------------------------------+-------------------------------+-----------------------------------------------+
        | out-frames                        | egress frames                 |:func:`peek_out_frames`                        |
        +-----------------------------------+-------------------------------+-----------------------------------------------+
        | bb-credit-zero                    | bb credit zero events         |:func:`peek_bb_credit_zero`                    |
        +-----------------------------------+-------------------------------+-----------------------------------------------+
        | input-buffer-full                 | input buffer full events      |:func:`peek_input_buffer_full`                 |
        +-----------------------------------+-------------------------------+-----------------------------------------------+
        | f-busy-frames                     | F_BSY frames                  |:func:`peek_f_busy_frames`                     |
        +-----------------------------------+-------------------------------+-----------------------------------------------+
        | p-busy-frames                     | P_BSY frames                  |:func:`peek_p_busy_frames`                     |
        +-----------------------------------+-------------------------------+-----------------------------------------------+
        | f-rjt-frames                      | F_RJT frames                  |:func:`peek_f_rjt_frames`                      |
        +-----------------------------------+-------------------------------+-----------------------------------------------+
        | p-rjt-frames                      | P_RJT frames                  |:func:`peek_p_rjt_frames`                      |
        +-----------------------------------+-------------------------------+-----------------------------------------------+
        | class-1-frames                    | class 1 frames                |:func:`peek_class_1_frames`                    |
        +-----------------------------------+-------------------------------+-----------------------------------------------+
        | class-2-frames                    | class 2 frames                |:func:`peek_class_2_frames`                    |
        +-----------------------------------+-------------------------------+-----------------------------------------------+
        | class-3-frames                    | class 3 frames                |:func:`peek_class_3_frames`                    |
        +-----------------------------------+-------------------------------+-----------------------------------------------+
        | class-3-discards                  | classs 3 discards             |:func:`peek_class_3_discards`                  |
        +-----------------------------------+-------------------------------+-----------------------------------------------+
        | link-failures                     | link failures                 |:func:`peek_link_failures`                     |
        +-----------------------------------+-------------------------------+-----------------------------------------------+
        | invalid-transmission-words        | invalid transmission words    |:func:`peek_invalid_transmission_words`        |
        +-----------------------------------+-------------------------------+-----------------------------------------------+
        | primitive-sequence-protocol-error | primitive sequence proto err  |:func:`peek_primitive_sequence_protocol_error` |
        +-----------------------------------+-------------------------------+-----------------------------------------------+
        | loss-of-signal                    | loss of signal                |:func:`peek_loss_of_signal`                    |
        +-----------------------------------+-------------------------------+-----------------------------------------------+
        | loss-of-sync                      | loss of sync                  |:func:`peek_loss_of_sync`                      |
        +-----------------------------------+-------------------------------+-----------------------------------------------+
        | class3-in-discards                | class 3 ingress discards      |:func:`peek_class3_in_discards`                |
        +-----------------------------------+-------------------------------+-----------------------------------------------+
        | class3-out-discards               | class 3 egress discards       |:func:`peek_class3_out_discards`               |
        +-----------------------------------+-------------------------------+-----------------------------------------------+
        | pcs-block-errors                  | PCS block errors              |:func:`peek_pcs_block_errors`                  |
        +-----------------------------------+-------------------------------+-----------------------------------------------+

    *Object methods*

        .. classmethod:: get(session, name=None)

            Returns a :class:`fibrechannel_statistics` object or
            a list of objects filled with attributes gathered
            from switch. If optional name is given, either an
            object matching the name of the port is returned
            or an empty object is returned if no match is found.

            Each object can be printed using :func:`pyfos_util.response_print`
            and individual attributes accessed
            through peek methods.

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: a :class:`fibrechannel_statistics`
                object if name is given or a list of objects
                if there are more than one

    *Attribute methods*

        .. method:: set_name(name)

            Sets port name in the object.

            :param name: port name to be set within the object
            :rtype: None or dictionary of error information

        .. method:: peek_name()

            Reads port name in the object.

            :rtype: None or port name

        .. method:: peek_sampling_interval()

            Reads sampling interval in seconds in the object.

            :rtype: None or sampling interval

        .. method:: peek_time_generated()

            Reads time generated, which indicates when statistics
            were captured, in the object.

            :rtype: None or time generated

        .. method:: set_reset_statistics(name)

            Sets reset mode in the object.

            :param name: port name to be set within the object
            :rtype: None or dictionary of error information

        .. method:: peek_reset_statistics()

            Reads reset mode in the object. It should alwasy be 0.

            :rtype: None or 0

        .. method:: peek_in_octets()

            Reads number of ingress octets in the object.

            :rtype: None or number of ingress octets

        .. method:: peek_out_octets()

            Reads number of egress octets in the object.

            :rtype: None or number of egress octets

        .. method:: peek_in_multicast_pkts()

            Reads number of ingress multicast packets in the object.

            :rtype: None or number of ingress multicast packets

        .. method:: peek_out_multicast_pkts()

            Reads number of egress multicast packets in the object.

            :rtype: None or number of egress multicast packets

        .. method:: peek_in_link_resets()

            Reads number of ingress link resets in the object.

            :rtype: None or number of ingress link resets

        .. method:: peek_out_link_resets()

            Reads number of egress link resets in the object.

            :rtype: None or number of egress link resets

        .. method:: peek_in_offline_sequences()

            Reads number of ingress offline sequences in the object.

            :rtype: None or number of ingress offline sequences

        .. method:: peek_out_offline_sequences()

            Reads number of egress offline sequences in the object.

            :rtype: None or number of egress offline sequences

        .. method:: peek_invalid_ordered_sets()

            Reads number of invalid ordered sets in the object.

            :rtype: None or number of invalid ordered sets

        .. method:: peek_frames_too_long()

            Reads number of frames too long in the object.

            :rtype: None or number of frames too long

        .. method:: peek_truncated_frames()

            Reads number of truncated frames in the object.

            :rtype: None or number of truncated frames

        .. method:: peek_address_errors()

            Reads number of address errors in the object.

            :rtype: None or number of address errors

        .. method:: peek_delimiter_errors()

            Reads number of delimiter errors in the object.

            :rtype: None or number of delimiter errors

        .. method:: peek_encoding_disparity_errors()

            Reads number of encoding disparity errors in the object.

            :rtype: None or number of encoding disparity errors

        .. method:: peek_too_many_rdys()

            Reads number of too many rdys in the object.

            :rtype: None or number of too many rdys

        .. method:: peek_in_crc_errors()

            Reads number of ingress CRC errors in the object.

            :rtype: None or number of ingress CRC errors

        .. method:: peek_crc_errors()

            Reads number of crc errors in the object.

            :rtype: None or number of crc errors

        .. method:: peek_bad_eofs_received()

            Reads number of bad EOFs in the object.

            :rtype: None or number of bad EOFs

        .. method:: peek_encoding_errors_outside_frame()

            Reads number of encoding errors outside of frame in the object.

            :rtype: None or number of encoding errors outside of frame

        .. method:: peek_multicast_timeouts()

            Reads number of multicast timeouts in the object.

            :rtype: None or number of multicast timeouts

        .. method:: peek_in_lcs()

            Reads number of ingress LCS in the object.

            :rtype: None or number of ingress LCS

        .. method:: peek_in_frame_rate()

            Reads ingress frame rate in the object.

            :rtype: None or ingress frame rate

        .. method:: peek_out_frame_rate()

            Reads egress frame rate in the object.

            :rtype: None or egress frame rate

        .. method:: peek_in_max_frame_rate()

            Reads ingress max frame rate in the object.

            :rtype: None or ingress max frame rate

        .. method:: peek_out_max_frame_rate()

            Reads egress max frame rate in the object.

            :rtype: None or egress max frame rate

        .. method:: peek_in_rate()

            Reads ingress rate in the object.

            :rtype: None or ingress rate

        .. method:: peek_out_rate()

            Reads egress rate in the object.

            :rtype: None or egress rate

        .. method:: peek_in_peak_rate()

            Reads ingress peak rate in the object.

            :rtype: None or ingress peak rate

        .. method:: peek_out_peak_rate()

            Reads number of egress peak rate in the object.

            :rtype: None or egress peak rate

        .. method:: peek_in_frames()

            Reads number of ingress frames in the object.

            :rtype: None or number of ingress frames

        .. method:: peek_out_frames()

            Reads number of egress frames in the object.

            :rtype: None or number of egress frames

        .. method:: peek_bb_credit_zero()

            Reads number of times when bb credit went to zero in the object.

            :rtype: None or number of times when bb credit went to zero

        .. method:: peek_input_buffer_full()

            Reads number of times when input buffer wass full in the object.

            :rtype: None or number of times when input buffer was full

        .. method:: peek_f_busy_frames()

            Reads number of f busy frames in the object.

            :rtype: None or number of f busy frames

        .. method:: peek_p_busy_frames()

            Reads number of p busy frames in the object.

            :rtype: None or number of p busy frames

        .. method:: peek_f_rjt_frames()

            Reads number of f reject frames in the object.

            :rtype: None or number of f reject frames

        .. method:: peek_p_rjt_frames()

            Reads number of p reject frames in the object.

            :rtype: None or number of p reject frames

        .. method:: peek_class_1_frames()

            Reads number of class 1 frames in the object.

            :rtype: None or number of class 1 frames

        .. method:: peek_class_2_frames()

            Reads number of class 2 frames sets in the object.

            :rtype: None or number of class 2 frames

        .. method:: peek_class_3_frames()

            Reads number of class 3 frames in the object.

            :rtype: None or number of class 3 frames

        .. method:: peek_class_3_discards()

            Reads number of class 3 discards in the object.

            :rtype: None or number of class 3 discards

        .. method:: peek_link_failures()

            Reads number of link failures in the object.

            :rtype: None or number of link failures

        .. method:: peek_invalid_transmission_words()

            Reads number of invalid transmission words in the object.

            :rtype: None or number of invalid transmission words

        .. method:: peek_primitive_sequence_protocol_error()

            Reads number of primitive sequence protocl errors in the object.

            :rtype: None or number of primitive sequence protocol errors

        .. method:: peek_loss_of_signal()

            Reads number of loss of signal events in the object.

            :rtype: None or number of loss of signal events

        .. method:: peek_loss_of_sync()

            Reads number of loss of sync events in the object.

            :rtype: None or number of loss of sync events

        .. method:: peek_class3_in_discards()

            Reads number of class 3 ingress discards in the object.

            :rtype: None or number of class 3 ingress discards

        .. method:: peek_class3_out_discards()

            Reads number of class 3 egress discards in the object.

            :rtype: None or number of class 3 egress discards

        .. method:: peek_pcs_block_errors()

            Reads number of pcs block errors in the object.

            :rtype: None or number of pcs block errors

        .. method:: peek_remote_link_failures()

            Reads number of number of link failures at remote port.

            :rtype: None or number of link failures

        .. method:: peek_remote_invalid_transmission_words()

            Reads number of invalid transmission words received at remote port

            :rtype: None or number of invalid transmission words

        .. method:: peek_primitive_sequence_protocol_error()

            Reads number of primitive sequence protocol errors detected at
            remote port

            :rtype: None or number of primitive sequence protocol errors

        .. method:: peek_remote_loss_of_signal()

            Reads number of instances of signal loss detected at remote port.

            :rtype: None or number of instances of signal loss

        .. method:: peek_remote_loss_of_sync()

            Reads number of instances of synchronization loss detected at
            remote port.

            :rtype: None or number of instances of synchronization loss

        .. method:: peek_remote_crc_errors()

            Reads number of frames received with invalid CRC at remote port.

            :rtype: None or number of frames received with invalid CRC

        .. method:: peek_remote_fec_uncorrected()

            Reads number of frames uncorrected by FEC block.

            :rtype: None or number of frames uncorrected by FEC block

        .. method:: peek_remote_buffer_credit_info_bb_credit()

            Reads number of credits available to the attached devices.

            :rtype: None or number of credits available

        .. method:: peek_remote_buffer_credit_info_peer_bb_credit()

           Reads number of credits available to the switch port.

           :rtype: None or number of credits available to the switch port


        """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.port_stats,
                         "/rest/running/brocade-interface/" +
                         "fibrechannel-statistics")

        self.add(pyfos_rest_util.rest_attribute(
            "name", pyfos_type.type_wwn,
            None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute(
            "sampling-interval", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "time-generated", pyfos_type.type_wwn,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "reset-statistics", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "in-octets", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "out-octets", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "in-multicast-pkts", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "out-multicast-pkts", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "in-link-resets", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "out-link-resets", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "in-offline-sequences", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "out-offline-sequences", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "invalid-ordered-sets", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "frames-too-long", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "truncated-frames", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "address-errors", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "delimiter-errors", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "encoding-disparity-errors", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "too-many-rdys", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "in-crc-errors", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "crc-errors", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "bad-eofs-received", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "encoding-errors-outside-frame", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "multicast-timeouts", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "in-lcs", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "in-frame-rate", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "out-frame-rate", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "in-max-frame-rate", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "out-max-frame-rate", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "in-rate", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "out-rate", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "in-peak-rate", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "out-peak-rate", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "in-frames", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "out-frames", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "bb-credit-zero", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "input-buffer-full", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "f-busy-frames", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "p-busy-frames", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "f-rjt-frames", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "p-rjt-frames", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "class-1-frames", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "class-2-frames", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "class-3-frames", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "class-3-discards", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "link-failures", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "invalid-transmission-words", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "primitive-sequence-protocol-error", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "loss-of-signal", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "loss-of-sync", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "class3-in-discards", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "class3-out-discards", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "pcs-block-errors", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "remote-link-failures", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "remote-invalid-transmission-words", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "remote-primitive-sequence-protocol-error", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "remote-loss-of-signal", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "remote-loss-of-sync", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "remote-crc-errors", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "remote-fec-uncorrected", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "remote-buffer-credit-info", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute(
            "bb-credit", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
            ["remote-buffer-credit-info"])
        self.add(pyfos_rest_util.rest_attribute(
            "peer-bb-credit", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
            ["remote-buffer-credit-info"])

        self.load(dictvalues, 1)


class gigabitethernet(pyfos_rest_util.rest_object):

    """Class of gigabitethernet

    *Description gigabitethernet*

        The list of gigabitethernet interfaces on the device.
        System-controlled interfaces created by the system are always present
        in this list, whether they are configured or not.

    Important class members of gigabitethernet:

        +--------------------------------+--------------------------------------------------------+--------------------------------------------------+
        | Attribute Name                 | Description                                            |  Frequently Used Methods                         |
        +================================+========================================================+==================================================+
        | name                           | The name of the interface.                             | :func:`peek_name`                                |
        |                                |                                                        | :func:`set_name`                                 |
        +--------------------------------+--------------------------------------------------------+--------------------------------------------------+
        | enabled-state                  | Enabled or disabled state of the                       | :func:`peek_enabled_state`                       |
        |                                | brocade-interface-types: 0 : Disabled 1 : Enabled      | :func:`set_enabled_state`                        |
        +--------------------------------+--------------------------------------------------------+--------------------------------------------------+
        | protocol                       | The GE port protocol configuration used by Extension   | :func:`peek_protocol`                            |
        |                                | blade/Switch during deployment. When GE port           | :func:`set_protocol`                             |
        |                                | protocol is configured for LAN, the GE port is         |                                                  |
        |                                | connected on the LAN side for Extending LAN IP         |                                                  |
        |                                | traffic over Extension tunnels using IP QOS            |                                                  |
        |                                | priorities. When the GE port protocol is configured    |                                                  |
        |                                | for WAN then the GE ports are connected on the WAN     |                                                  |
        |                                | side and are used for configuring the FCIP/Extension   |                                                  |
        |                                | tunnels using them. In case of chassis system if the   |                                                  |
        |                                | slot is powered off or in faulty state then the leaf   |                                                  |
        |                                | will be skipped in display. Supported values: LAN :    |                                                  |
        |                                | GE port is configured for LAN side connections. WAN    |                                                  |
        |                                | : GE port is configured for WAN side connections.      |                                                  |
        +--------------------------------+--------------------------------------------------------+--------------------------------------------------+
        | persistent-disable             | Indicates if the port is persistently disabled or      | :func:`peek_persistent_disable`                  |
        |                                | persistently enabled  1 : persistently disabled 0 :    | :func:`set_persistent_disable`                   |
        |                                | persistently enabled                                   |                                                  |
        +--------------------------------+--------------------------------------------------------+--------------------------------------------------+
        | portchannel-member-timeout     | The dynamic portchannel member timeout of the          | :func:`peek_portchannel_member_timeout`          |
        |                                | gigabit-ethernet interface. default long.              | :func:`set_portchannel_member_timeout`           |
        +--------------------------------+--------------------------------------------------------+--------------------------------------------------+
        | auto-negotiation-enabled       | Auto-negotiation is enabled by default in 1G mode.     | :func:`peek_auto_negotiation_enabled`            |
        |                                | In 10G mode it is disabled and not supported. When     | :func:`set_auto_negotiation_enabled`             |
        |                                | the port is set for 1G mode, you can disable           |                                                  |
        |                                | auto-negotiation. In case of chassis system if the     |                                                  |
        |                                | slot is powered off or in faulty state then the leaf   |                                                  |
        |                                | will be skipped in display. Supported values: true :   |                                                  |
        |                                | Auto negotiation mode for GE port is enabled. false    |                                                  |
        |                                | : Auto negotiation mode for GE port is disabled.       |                                                  |
        +--------------------------------+--------------------------------------------------------+--------------------------------------------------+
        | lldp-enabled-state             | LLDP state of the port Possible values are: true -     | :func:`peek_lldp_enabled_state`                  |
        |                                | LLDP is enabled on the port false - LLDP is disabled   | :func:`set_lldp_enabled_state`                   |
        |                                | on the port                                            |                                                  |
        +--------------------------------+--------------------------------------------------------+--------------------------------------------------+
        | lldp-profile                   | LLDP profile name configured on the port. Blank        | :func:`peek_lldp_profile`                        |
        |                                | lldp-profile means LLDP profile is not configured on   | :func:`set_lldp_profile`                         |
        |                                | this port. In such case, lldp global parameters are    |                                                  |
        |                                | in use for this port. To configure a new profile or    |                                                  |
        |                                | change existing profile on the port, user should       |                                                  |
        |                                | perform a PATCH operation with the profile name. To    |                                                  |
        |                                | remove the profile from the port, user should          |                                                  |
        |                                | perform a PATCH operation with NULL string.            |                                                  |
        +--------------------------------+--------------------------------------------------------+--------------------------------------------------+
        | speed                          | For PHY types that may operate at various speeds,      | :func:`peek_speed`                               |
        |                                | this leaf allows the interface to be forced to         | :func:`set_speed`                                |
        |                                | operate at a particular speed. Without any explicit    |                                                  |
        |                                | configuration, gigabitethernet interfaces run at the   |                                                  |
        |                                | maximum capable speed.                                 |                                                  |
        +--------------------------------+--------------------------------------------------------+--------------------------------------------------+
        | extension-vlans                | List of extension vlans configured on this port        | :func:`peek_extension_vlans`                     |
        |                                |                                                        | :func:`set_extension_vlans`                      |
        +--------------------------------+--------------------------------------------------------+--------------------------------------------------+
        | mac-address                    | MAC Address for the interface.                         | :func:`peek_mac_address`                         |
        |                                |                                                        |                                                  |
        +--------------------------------+--------------------------------------------------------+--------------------------------------------------+
        | operational-status             | Operational status of the port: 1 : Online 2 :         | :func:`peek_operational_status`                  |
        |                                | Offline                                                |                                                  |
        +--------------------------------+--------------------------------------------------------+--------------------------------------------------+
        | portchannel-name               | The name of the portchannel that the                   | :func:`peek_portchannel_name`                    |
        |                                | gigabit-ethernet interface belongs to. This will be    |                                                  |
        |                                | NULL in case the port is not portchannel member        |                                                  |
        +--------------------------------+--------------------------------------------------------+--------------------------------------------------+
        | extension-vlans                | List of extension vlans configured on this port        | :func:`peek_extension_vlans`                     |
        |                                |                                                        | :func:`set_extension_vlans`                      |
        +--------------------------------+--------------------------------------------------------+--------------------------------------------------+
        | vlan                           | Extension vlans configured on this port                | :func:`peek_extension_vlans_vlan`                |
        |                                |                                                        |                                                  |
        +--------------------------------+--------------------------------------------------------+--------------------------------------------------+

    *Object functions for gigabitethernet*

    .. function:: get()

        Get the instances of class "gigabitethernet from switch. The object
         can be printed using :func:`pyfos_utils.response_print`.

        :param session: The session handler returned by
         :func:`pyfos_auth.login`.

        :rtype: A dictionary of errors or a success response.


    *Class functions for gigabitethernet*

        .. function:: peek_name()

            Reads the value assigned to name in the object.

            :rtype: None on error and a value on success.


        .. function:: set_name(value)

            Set the value of name in the object.

            :rtype: A dictionary of error or a success response and a value
             with "name" as the key


        .. function:: peek_enabled_state()

            Reads the value assigned to enabled-state in the object.

            :rtype: None on error and a value on success.


        .. function:: set_enabled_state(value)

            Set the value of enabled-state in the object.

            :rtype: A dictionary of error or a success response and a value
             with "enabled-state" as the key


        .. function:: peek_protocol()

            Reads the value assigned to protocol in the object.

            :rtype: None on error and a value on success.


        .. function:: set_protocol(value)

            Set the value of protocol in the object.

            :rtype: A dictionary of error or a success response and a value
             with "protocol" as the key


        .. function:: peek_persistent_disable()

            Reads the value assigned to persistent-disable in the object.

            :rtype: None on error and a value on success.


        .. function:: set_persistent_disable(value)

            Set the value of persistent-disable in the object.

            :rtype: A dictionary of error or a success response and a value
             with "persistent-disable" as the key


        .. function:: peek_portchannel_member_timeout()

            Reads the value assigned to portchannel-member-timeout in the
             object.

            :rtype: None on error and a value on success.


        .. function:: set_portchannel_member_timeout(value)

            Set the value of portchannel-member-timeout in the object.

            :rtype: A dictionary of error or a success response and a value
             with "portchannel-member-timeout" as the key


        .. function:: peek_auto_negotiation_enabled()

            Reads the value assigned to auto-negotiation-enabled in the
             object.

            :rtype: None on error and a value on success.


        .. function:: set_auto_negotiation_enabled(value)

            Set the value of auto-negotiation-enabled in the object.

            :rtype: A dictionary of error or a success response and a value
             with "auto-negotiation-enabled" as the key


        .. function:: peek_lldp_enabled_state()

            Reads the value assigned to lldp-enabled-state in the object.

            :rtype: None on error and a value on success.


        .. function:: set_lldp_enabled_state(value)

            Set the value of lldp-enabled-state in the object.

            :rtype: A dictionary of error or a success response and a value
             with "lldp-enabled-state" as the key


        .. function:: peek_lldp_profile()

            Reads the value assigned to lldp-profile in the object.

            :rtype: None on error and a value on success.


        .. function:: set_lldp_profile(value)

            Set the value of lldp-profile in the object.

            :rtype: A dictionary of error or a success response and a value
             with "lldp-profile" as the key


        .. function:: peek_speed()

            Reads the value assigned to speed in the object.

            :rtype: None on error and a value on success.


        .. function:: set_speed(value)

            Set the value of speed in the object.

            :rtype: A dictionary of error or a success response and a value
             with "speed" as the key


        .. function:: peek_extension_vlans()

            Reads the value assigned to extension-vlans in the object.

            :rtype: None on error and a value on success.


        .. function:: set_extension_vlans(value)

            Set the value of extension-vlans in the object.

            :rtype: A dictionary of error or a success response and a value
             with "extension-vlans" as the key


        .. function:: peek_mac_address()

            Reads the value assigned to mac-address in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_operational_status()

            Reads the value assigned to operational-status in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_portchannel_name()

            Reads the value assigned to portchannel-name in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_extension_vlans()

            Reads the value assigned to extension-vlans in the object.

            :rtype: None on error and a value on success.


        .. function:: set_extension_vlans(value)

            Set the value of extension-vlans in the object.

            :rtype: A dictionary of error or a success response and a value
             with "extension-vlans" as the key


        .. function:: peek_extension_vlans_vlan()

            Reads the value assigned to vlan in the object.

            :rtype: None on error and a value on success.


    """

    def __init__(self, dictvalues=None):

        clsuri = "/rest" + "/running" + "/brocade-interface" +\
                 "/gigabitethernet"
        clstype = pyfos_rest_util.rest_obj_type.gige
        super().__init__(clstype, clsuri)

        self.add(pyfos_rest_util.rest_attribute("name", pyfos_type.type_str,
                 None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute("enabled-state",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("protocol",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG,
                 version.VER_RANGE_900_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute("persistent-disable",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("portchannel-member-timeout",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG,
                 version.VER_RANGE_900_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute("auto-negotiation-enabled",
                 pyfos_type.type_bool, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG,
                 version.VER_RANGE_900_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute("lldp-enabled-state",
                 pyfos_type.type_bool, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG,
                 version.VER_RANGE_900_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute("lldp-profile",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG,
                 version.VER_RANGE_900_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute("speed", pyfos_type.type_int,
                 None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("mac-address",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("operational-status",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("portchannel-name",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG,
                 version.VER_RANGE_900_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute("extension-vlans",
                 pyfos_type.type_na, dict(),
                 pyfos_rest_util.REST_ATTRIBUTE_CONTAINER,
                 version.VER_RANGE_900_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute("vlan", pyfos_type.type_na,
                 None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST_NOT_CONFIG,
                 version.VER_RANGE_900_and_ABOVE), ['extension-vlans'])
        self.load(dictvalues, 1)


class gigabitethernet_statistics(pyfos_rest_util.rest_object):

    """Class of gigabitethernet_statistics

    *Description gigabitethernet_statistics*

        A list of interface-related statistics for gigabitethernet port.

    Important class members of gigabitethernet_statistics:

        +--------------------------+---------------------------------+-------------------------------------------------+
        | Attribute Name           | Description                     |  Frequently Used Methods                        |
        +==========================+=================================+=================================================+
        | name                     | The name of the interface.      | :func:`peek_name`                               |
        |                          |                                 | :func:`set_name`                                |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | reset-statistics         | Write-only leaf and will not    | :func:`peek_reset_statistics`                   |
        |                          | be returned in GET request.     | :func:`set_reset_statistics`                    |
        |                          | Set it to 1 to reset            |                                                 |
        |                          | statistical counters in PATCH   |                                                 |
        |                          | request.                        |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | crc-error                | The total number of Cyclic      | :func:`peek_crc_error`                          |
        |                          | Redundancy Check (CRC)          |                                                 |
        |                          | errors.                         |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | out-pkts                 | The total number of packets     | :func:`peek_out_pkts`                           |
        |                          | transmitted out of the          |                                                 |
        |                          | interface.                      |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | out-multicast-pkts       | The total number of multicast   | :func:`peek_out_multicast_pkts`                 |
        |                          | packets transmitted out of      |                                                 |
        |                          | the interface.                  |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | out-vlan-pkts            | The total number of vlan        | :func:`peek_out_vlan_pkts`                      |
        |                          | packets transmitted out of      |                                                 |
        |                          | the interface.                  |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | out-octets               | The total number of octets      | :func:`peek_out_octets`                         |
        |                          | transmitted out of the          |                                                 |
        |                          | interface.                      |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | out-pause-pkts           | The total number of pause       | :func:`peek_out_pause_pkts`                     |
        |                          | packets transmitted out of      |                                                 |
        |                          | the interface.                  |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | in-unicast-pkts          | The number of unicast packets   | :func:`peek_in_unicast_pkts`                    |
        |                          | received on the interface.      |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | in-broadcast-pkts        | The number of broadcast         | :func:`peek_in_broadcast_pkts`                  |
        |                          | packets received on the         |                                                 |
        |                          | interface.                      |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | in-multicast-pkts        | The number of multicast         | :func:`peek_in_multicast_pkts`                  |
        |                          | packets received on the         |                                                 |
        |                          | interface.                      |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | time-generated           | The time at which the           | :func:`peek_time_generated`                     |
        |                          | statistics were queried.        |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | out-unicast-pkts         | The total number of unicast     | :func:`peek_out_unicast_pkts`                   |
        |                          | packets transmitted out of      |                                                 |
        |                          | the interface.                  |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | in-vlan-pkts             | The total number of vlan        | :func:`peek_in_vlan_pkts`                       |
        |                          | packets received on the         |                                                 |
        |                          | interface.                      |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | out-broadcast-pkts       | The total number of broadcast   | :func:`peek_out_broadcast_pkts`                 |
        |                          | packets transmitted out of      |                                                 |
        |                          | the interface.                  |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | carrier-loss-error       | The total number of carrier     | :func:`peek_carrier_loss_error`                 |
        |                          | loss errors.                    |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | in-pkts                  | The number of packets           | :func:`peek_in_pkts`                            |
        |                          | received on the interface.      |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | in-octets                | The total number of octets      | :func:`peek_in_octets`                          |
        |                          | received on the interface.      |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | in-pause-pkts            | The total number of pause       | :func:`peek_in_pause_pkts`                      |
        |                          | packets received on the         |                                                 |
        |                          | interface.                      |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | jabber-error             | The total number of jabber      | :func:`peek_jabber_error`                       |
        |                          | errors.                         |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+

    *Object functions for gigabitethernet_statistics*

    .. function:: get()

        Get the instances of class "gigabitethernet_statistics from switch.
         The object can be printed using :func:`pyfos_utils.response_print`.

        :param session: The session handler returned by
         :func:`pyfos_auth.login`.

        :rtype: A dictionary of errors or a success response.


    *Class functions for gigabitethernet_statistics*

        .. function:: peek_name()

            Reads the value assigned to name in the object.

            :rtype: None on error and a value on success.


        .. function:: set_name(value)

            Set the value of name in the object.

            :rtype: A dictionary of error or a success response and a value
             with "name" as the key


        .. function:: peek_reset_statistics()

            Reads the value assigned to reset-statistics in the object.

            :rtype: None on error and a value on success.


        .. function:: set_reset_statistics(value)

            Set the value of reset-statistics in the object.

            :rtype: A dictionary of error or a success response and a value
             with "reset-statistics" as the key


        .. function:: peek_crc_error()

            Reads the value assigned to crc-error in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_out_pkts()

            Reads the value assigned to out-pkts in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_out_multicast_pkts()

            Reads the value assigned to out-multicast-pkts in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_out_vlan_pkts()

            Reads the value assigned to out-vlan-pkts in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_out_octets()

            Reads the value assigned to out-octets in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_out_pause_pkts()

            Reads the value assigned to out-pause-pkts in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_in_unicast_pkts()

            Reads the value assigned to in-unicast-pkts in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_in_broadcast_pkts()

            Reads the value assigned to in-broadcast-pkts in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_in_multicast_pkts()

            Reads the value assigned to in-multicast-pkts in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_time_generated()

            Reads the value assigned to time-generated in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_out_unicast_pkts()

            Reads the value assigned to out-unicast-pkts in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_in_vlan_pkts()

            Reads the value assigned to in-vlan-pkts in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_out_broadcast_pkts()

            Reads the value assigned to out-broadcast-pkts in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_carrier_loss_error()

            Reads the value assigned to carrier-loss-error in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_in_pkts()

            Reads the value assigned to in-pkts in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_in_octets()

            Reads the value assigned to in-octets in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_in_pause_pkts()

            Reads the value assigned to in-pause-pkts in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_jabber_error()

            Reads the value assigned to jabber-error in the object.

            :rtype: None on error and a value on success.


    """

    def __init__(self, dictvalues=None):

        clsuri = "/rest" + "/running" + "/brocade-interface" +\
                 "/gigabitethernet-statistics"
        clstype = pyfos_rest_util.rest_obj_type.gige_stats
        super().__init__(clstype, clsuri)

        self.add(pyfos_rest_util.rest_attribute("name", pyfos_type.type_str,
                 None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute("reset-statistics",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("crc-error",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("out-pkts",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("out-multicast-pkts",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("out-vlan-pkts",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("out-octets",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("out-pause-pkts",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("in-unicast-pkts",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("in-broadcast-pkts",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("in-multicast-pkts",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("time-generated",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("out-unicast-pkts",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("in-vlan-pkts",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("out-broadcast-pkts",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("carrier-loss-error",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("in-pkts",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("in-octets",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("in-pause-pkts",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("jabber-error",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.load(dictvalues, 1)


class extension_ip_interface(pyfos_rest_util.rest_object):

    """Class of extension_ip_interface

    *Description extension_ip_interface*

        Represents the IP interface defined on extension blade or system.

    Important class members of extension_ip_interface:

        +--------------------------+---------------------------------+-------------------------------------------------+
        | Attribute Name           | Description                     |  Frequently Used Methods                        |
        +==========================+=================================+=================================================+
        | name                     | The name of the interface.      | :func:`peek_name`                               |
        |                          |                                 | :func:`set_name`                                |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | dp-id                    | Extension Data Path Processor   | :func:`peek_dp_id`                              |
        |                          | ID associated with the IP       | :func:`set_dp_id`                               |
        |                          | interface. Based on platform    |                                                 |
        |                          | either it will have a single    |                                                 |
        |                          | DP or dual DP. In case of       |                                                 |
        |                          | single DP only DP0 is           |                                                 |
        |                          | supported, and in case of       |                                                 |
        |                          | dual DP both DP0 and DP1 are    |                                                 |
        |                          | supported 0 : DP0 1 : DP1.      |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | ip-address               | Specifies the source            | :func:`peek_ip_address`                         |
        |                          | IPv4/IPv6 address of the        | :func:`set_ip_address`                          |
        |                          | interface.                      |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | ip-prefix-length         | The prefix length operator      | :func:`peek_ip_prefix_length`                   |
        |                          | for the IP address. Once set,   | :func:`set_ip_prefix_length`                    |
        |                          | prefix length cannot be         |                                                 |
        |                          | changed.                        |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | vlan-id                  | Specifies the VLAN ID. This     | :func:`peek_vlan_id`                            |
        |                          | operand is optional.            | :func:`set_vlan_id`                             |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | mtu-size                 | Specifies the maximum           | :func:`peek_mtu_size`                           |
        |                          | transmission unit size. The     | :func:`set_mtu_size`                            |
        |                          | permitted range is 1280 Bytes   |                                                 |
        |                          | to 9216 Bytes or the special    |                                                 |
        |                          | value 1 which is equivalent     |                                                 |
        |                          | to 'auto' mode to enable PMTU   |                                                 |
        |                          | discovery. The discovered       |                                                 |
        |                          | value of MTU in 'auto' mode     |                                                 |
        |                          | can be found as a circuit       |                                                 |
        |                          | attribute.                      |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | status-flags             | IP interface Flags:  U = Up B   | :func:`peek_status_flags`                       |
        |                          | = Broadcast D = Debug L =       |                                                 |
        |                          | Loopback P = Point2Point R =    |                                                 |
        |                          | Running I = InUse N = NoArp     |                                                 |
        |                          | PR= Promiscous M = Multicast    |                                                 |
        |                          | S = StaticArp LU= LinkUp        |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+

    *Object functions for extension_ip_interface*

    .. function:: get()

        Get the instances of class "extension_ip_interface from switch. The
         object can be printed using :func:`pyfos_utils.response_print`.

        :param session: The session handler returned by
         :func:`pyfos_auth.login`.

        :rtype: A dictionary of errors or a success response.


    *Class functions for extension_ip_interface*

        .. function:: peek_dp_id()

            Reads the value assigned to dp-id in the object.

            :rtype: None on error and a value on success.


        .. function:: set_dp_id(value)

            Set the value of dp-id in the object.

            :rtype: A dictionary of error or a success response and a value
             with "dp-id" as the key


        .. function:: peek_ip_address()

            Reads the value assigned to ip-address in the object.

            :rtype: None on error and a value on success.


        .. function:: set_ip_address(value)

            Set the value of ip-address in the object.

            :rtype: A dictionary of error or a success response and a value
             with "ip-address" as the key


        .. function:: peek_name()

            Reads the value assigned to name in the object.

            :rtype: None on error and a value on success.


        .. function:: set_name(value)

            Set the value of name in the object.

            :rtype: A dictionary of error or a success response and a value
             with "name" as the key


        .. function:: peek_ip_prefix_length()

            Reads the value assigned to ip-prefix-length in the object.

            :rtype: None on error and a value on success.


        .. function:: set_ip_prefix_length(value)

            Set the value of ip-prefix-length in the object.

            :rtype: A dictionary of error or a success response and a value
             with "ip-prefix-length" as the key


        .. function:: peek_vlan_id()

            Reads the value assigned to vlan-id in the object.

            :rtype: None on error and a value on success.


        .. function:: set_vlan_id(value)

            Set the value of vlan-id in the object.

            :rtype: A dictionary of error or a success response and a value
             with "vlan-id" as the key


        .. function:: peek_mtu_size()

            Reads the value assigned to mtu-size in the object.

            :rtype: None on error and a value on success.


        .. function:: set_mtu_size(value)

            Set the value of mtu-size in the object.

            :rtype: A dictionary of error or a success response and a value
             with "mtu-size" as the key


        .. function:: peek_status_flags()

            Reads the value assigned to status-flags in the object.

            :rtype: None on error and a value on success.


    """

    def __init__(self, dictvalues=None):

        clsuri = "/rest" + "/running" + "/brocade-interface" +\
                 "/extension-ip-interface"
        clstype = pyfos_rest_util.rest_obj_type.ipif
        super().__init__(clstype, clsuri)

        self.add(pyfos_rest_util.rest_attribute("name", pyfos_type.type_str,
                 None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute("dp-id", pyfos_type.type_int,
                 None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute("ip-address",
                 pyfos_type.type_ip_addr, None,
                 pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute("ip-prefix-length",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG_MANDATORY))
        self.add(pyfos_rest_util.rest_attribute("vlan-id",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("mtu-size",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("status-flags",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.load(dictvalues, 1)


class portchannel(pyfos_rest_util.rest_object):

    """Class of portchannel

    *Description portchannel*

        The list of portchannel interfaces on the switch, their related
        configuration and operational state.

    Important class members of portchannel:

        +------------------------------------------+-------------------------------+-----------------------------------------------------------------+
        | Attribute Name                           | Description                   |  Frequently Used Methods                                        |
        +==========================================+===============================+=================================================================+
        | speed                                    | The speed of the              | :func:`peek_speed`                                              |
        |                                          | portchannel interface. The    |                                                                 |
        |                                          | speed of the portchannel is   |                                                                 |
        |                                          | the speed of its member       |                                                                 |
        |                                          | ports. speed is an            |                                                                 |
        |                                          | read-only parameter of a      |                                                                 |
        |                                          | port-channel. Note: The       |                                                                 |
        |                                          | speed of all members of a     |                                                                 |
        |                                          | portchannel must match.       |                                                                 |
        +------------------------------------------+-------------------------------+-----------------------------------------------------------------+
        | portchannel-type                         | The type of a portchannel     | :func:`set_portchannel_type`                                    |
        |                                          | interface. Portchannel Type   | :func:`peek_portchannel_type`                                   |
        |                                          | is a mandatory parameter      |                                                                 |
        |                                          | while the portchannel is      |                                                                 |
        |                                          | created. Possible values:     |                                                                 |
        |                                          | static  : Static              |                                                                 |
        |                                          | portchannel type. dynamic :   |                                                                 |
        |                                          | Dynamic portchannel type.     |                                                                 |
        +------------------------------------------+-------------------------------+-----------------------------------------------------------------+
        | gigabit-ethernet-member-ports/port       | The list of gigabit           | :func:`set_gigabit_ethernet_member_ports_port`                  |
        |                                          | ethernet interfaces that      | :func:`peek_gigabit_ethernet_member_ports_port`                 |
        |                                          | are members of the            |                                                                 |
        |                                          | portchannel.                  |                                                                 |
        +------------------------------------------+-------------------------------+-----------------------------------------------------------------+
        | primary-member-gigabit-ethernet-port     | The primary member            | :func:`peek_primary_member_gigabit_ethernet_port`               |
        |                                          | interface of the              |                                                                 |
        |                                          | portchannel.                  |                                                                 |
        +------------------------------------------+-------------------------------+-----------------------------------------------------------------+
        | name                                     | The portchannel name.         | :func:`set_name`                                                |
        |                                          |                               | :func:`peek_name`                                               |
        +------------------------------------------+-------------------------------+-----------------------------------------------------------------+
        | operational-status-enabled               | The portchannel operational   | :func:`peek_operational_status_enabled`                         |
        |                                          | status. The possible values   |                                                                 |
        |                                          | are: false : portchannel is   |                                                                 |
        |                                          | offline. true : portchannel   |                                                                 |
        |                                          | is online.                    |                                                                 |
        +------------------------------------------+-------------------------------+-----------------------------------------------------------------+
        | key                                      | The portchannel key. The      | :func:`set_key`                                                 |
        |                                          | portchannel key cannot be     | :func:`peek_key`                                                |
        |                                          | modified once the             |                                                                 |
        |                                          | portchannel is created. If    |                                                                 |
        |                                          | user does not provide the     |                                                                 |
        |                                          | key during portchannel        |                                                                 |
        |                                          | creation, the system will     |                                                                 |
        |                                          | auto-assign an available      |                                                                 |
        |                                          | key. The portchannel key is   |                                                                 |
        |                                          | unique across all             |                                                                 |
        |                                          | portchannel interfaces on     |                                                                 |
        |                                          | the switch.                   |                                                                 |
        +------------------------------------------+-------------------------------+-----------------------------------------------------------------+
        | auto-negotiation-enabled                 | Indicates the                 | :func:`set_auto_negotiation_enabled`                            |
        |                                          | auto-negotiation of the       | :func:`peek_auto_negotiation_enabled`                           |
        |                                          | FCIP portchannel. The         |                                                                 |
        |                                          | possible values are: false    |                                                                 |
        |                                          | : auto-negotiation is off.    |                                                                 |
        |                                          | true : auto-negotiation is    |                                                                 |
        |                                          | on.                           |                                                                 |
        +------------------------------------------+-------------------------------+-----------------------------------------------------------------+
        | lacp-system-mac-address                  | The LACP MAC address of the   | :func:`peek_lacp_system_mac_address`                            |
        |                                          | system.                       |                                                                 |
        +------------------------------------------+-------------------------------+-----------------------------------------------------------------+
        | admin-state-enabled                      | Indicates the admin state     | :func:`set_admin_state_enabled`                                 |
        |                                          | of the portchannel. The       | :func:`peek_admin_state_enabled`                                |
        |                                          | possible values are: false    |                                                                 |
        |                                          | : portchannel is disabled.    |                                                                 |
        |                                          | true : portchannel is         |                                                                 |
        |                                          | enabled.                      |                                                                 |
        +------------------------------------------+-------------------------------+-----------------------------------------------------------------+

    *Object functions for portchannel*

    .. function:: get()

        Get the instances of class "portchannel from switch. The object can be
         printed using :func:`pyfos_utils.response_print`.

        :param session: The session handler returned by
         :func:`pyfos_auth.login`.

        :rtype: A dictionary of errors or a success response.


    *Class functions for portchannel*

        .. function:: peek_speed()

            Reads the value assigned to speed in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_portchannel_type()

            Reads the value assigned to portchannel-type in the object.

            :rtype: None on error and a value on success.


        .. function:: set_portchannel_type(value)

            Set the value of portchannel-type in the object.

            :rtype: A dictionary of error or a success response and a value
             with "portchannel-type" as the key

        .. function:: peek_gigabit_ethernet_member_ports_port()

            Reads the value assigned to port in the object.

            :rtype: None on error and a value on success.


        .. function:: set_gigabit_ethernet_member_ports_port(value)

            Set the value of port in the object.

            :rtype: A dictionary of error or a success response and a value
             with "port" as the key


        .. function:: peek_primary_member_gigabit_ethernet_port()

            Reads the value assigned to primary-member-gigabit-ethernet-port
             in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_name()

            Reads the value assigned to name in the object.

            :rtype: None on error and a value on success.


        .. function:: set_name(value)

            Set the value of name in the object.

            :rtype: A dictionary of error or a success response and a value
             with "name" as the key

        .. function:: peek_operational_status_enabled()

            Reads the value assigned to operational-status-enabled in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_key()

            Reads the value assigned to key in the object.

            :rtype: None on error and a value on success.


        .. function:: set_key(value)

            Set the value of key in the object.

            :rtype: A dictionary of error or a success response and a value
             with "key" as the key


        .. function:: peek_auto_negotiation_enabled()

            Reads the value assigned to auto-negotiation-enabled in the
             object.

            :rtype: None on error and a value on success.


        .. function:: set_auto_negotiation_enabled(value)

            Set the value of auto-negotiation-enabled in the object.

            :rtype: A dictionary of error or a success response and a value
             with "auto-negotiation-enabled" as the key


        .. function:: peek_lacp_system_mac_address()

            Reads the value assigned to lacp-system-mac-address in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_admin_state_enabled()

            Reads the value assigned to admin-state-enabled in the object.

            :rtype: None on error and a value on success.


        .. function:: set_admin_state_enabled(value)

            Set the value of admin-state-enabled in the object.

            :rtype: A dictionary of error or a success response and a value
             with "admin-state-enabled" as the key


    """

    def __init__(self, dictvalues=None):

        clsuri = "/rest" + "/running" + "/brocade-interface" + "/portchannel"
        clstype = pyfos_rest_util.rest_obj_type.portchannel
        clsver = version.VER_RANGE_900_and_ABOVE
        super().__init__(clstype, clsuri, clsver)

        self.add(pyfos_rest_util.rest_attribute("name", pyfos_type.type_str,
                 None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute("speed", pyfos_type.type_int,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("portchannel-type",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "primary-member-gigabit-ethernet-port", pyfos_type.type_str,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("operational-status-enabled",
                 pyfos_type.type_bool, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("key", pyfos_type.type_int,
                 None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("auto-negotiation-enabled",
                 pyfos_type.type_bool, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("lacp-system-mac-address",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("admin-state-enabled",
                 pyfos_type.type_bool, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "gigabit-ethernet-member-ports", pyfos_type.type_na, dict(),
                 pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute("port", pyfos_type.type_na,
                 None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST),
                 ['gigabit-ethernet-member-ports'])
        self.load(dictvalues, 1)


class logical_e_port(pyfos_rest_util.rest_object):

    """Class of logical_e_port

    *Description logical_e_port*

        The list of logical E_Port interfaces on the device which form the
        logical inter switch link (lisl).

    Important class members:

        +-------------------------------+-----------------------------------------------------+------------------------------------------------------+
        | Attribute Name                | Description                                         |  Frequently Used Methods                             |
        +===============================+=====================================================+======================================================+
        | neighbor-node-wwn             | The neighbor node WWN logically connected to this   | :func:`peek_neighbor_node_wwn`                       |
        |                               | port.                                               |                                                      |
        +-------------------------------+-----------------------------------------------------+------------------------------------------------------+
        | associated-physical-ports     | List of physical E_Port(s) associated with          | :func:`peek_associated_physical_ports`               |
        |                               | logical E_Port                                      |                                                      |
        +-------------------------------+-----------------------------------------------------+------------------------------------------------------+
        | offline-reason                | Reason for logical E_Port Offline status.           | :func:`peek_offline_reason`                          |
        |                               |                                                     |                                                      |
        +-------------------------------+-----------------------------------------------------+------------------------------------------------------+
        | port-index                    | The unique port number on the switch for            | :func:`peek_port_index`                              |
        |                               | identifying a logical E_Port.                       |                                                      |
        +-------------------------------+-----------------------------------------------------+------------------------------------------------------+
        | operational-status            | Operational status of the the logical E_Port.       | :func:`peek_operational_status`                      |
        |                               |                                                     |                                                      |
        +-------------------------------+-----------------------------------------------------+------------------------------------------------------+
        | fabric-id                     | The virtual fabric identification (VFID) of the     | :func:`peek_fabric_id`                               |
        |                               | logical switch in which the logical E_Port is       |                                                      |
        |                               | created.                                            |                                                      |
        +-------------------------------+-----------------------------------------------------+------------------------------------------------------+


    *Object functions for logical_e_port*

    .. function:: get()

        Get the instances of class "logical_e_port" from switch. The object can
         be printed using :func:`pyfos_utils.response_print`.

        :param session: The session handler returned by
         :func:`pyfos_auth.login`.

        :rtype: A dictionary of errors or a success response.


    *Class functions for logical_e_port*

        .. function:: peek_neighbor_node_wwn()

            Reads the value assigned to neighbor-node-wwn in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_associated_physical_ports()

            Reads the value assigned to associated-physical-ports in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_offline_reason()

            Reads the value assigned to offline-reason in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_port_index()

            Reads the value assigned to port-index in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_operational_status()

            Reads the value assigned to operational-status in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_fabric_id()

            Reads the value assigned to fabric-id in the object.

            :rtype: None on error and a value on success.


     """

    def __init__(self, dictvalues=None):

        clsuri = "/rest" + "/running" + "/brocade-interface" +\
                 "/logical-e-port"
        clstype = pyfos_rest_util.rest_obj_type.logical_e_port
        clsver = version.VER_RANGE_900_and_ABOVE
        super().__init__(clstype, clsuri, clsver)

        self.add(pyfos_rest_util.rest_attribute(
            "port-index", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute(
            "fabric-id", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "operational-status", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "offline-reason", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "neighbor-node-wwn", pyfos_type.type_wwn,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "associated-physical-ports", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute(
            "port", pyfos_type.type_na,
            None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST),
            ["associated-physical-ports"])
        self.load(dictvalues, 1)

