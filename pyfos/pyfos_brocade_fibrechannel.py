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

:mod:`pyfos_brocade_fibrechannel` - PyFOS module to provide \
        rest support for FC ports.
*********************************************************************************************************
The :mod:`pyfos_brocade_fibrechannel` provides a REST support \
        for FC ports.

"""

import pyfos.pyfos_rest_util as pyfos_rest_util
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

    Important class members:

        +-------------------------------+-------------------------------+----------------------------------------+
        | Attribute name                | Description                   |Frequstly used methods                  |
        +===============================+===============================+========================================+
        | name                          | name of port                  |:func:`set_name`                        |
        |                               |                               |:func:`peek_name`                       |
        +-------------------------------+-------------------------------+----------------------------------------+
        | wwn                           | WWN of port                   |:func:`peek_wwn`                        |
        +-------------------------------+-------------------------------+----------------------------------------+
        | operational-status            | current operational status    |:func:`peek_operational_status`         |
        +-------------------------------+-------------------------------+----------------------------------------+
        | enabled_state                 | enabled state of port         |:func:`set_enabled_state`               |
        |                               |                               |:func:`peek_enabled_state`              |
        +-------------------------------+-------------------------------+----------------------------------------+
        | user-friendly-name            | string name of port           |:func:`set_user_friendly_name`          |
        |                               |                               |:func:`peek_user_friendly_name`         |
        +-------------------------------+-------------------------------+----------------------------------------+
        | speed                         | speed of port                 |:func:`set_speed`                       |
        |                               |                               |:func:`peek_speed`                      |
        +-------------------------------+-------------------------------+----------------------------------------+
        | auto-negotiate                | indicate if auto negotiate is |:func:`peek_auto_negotiate`             |
        |                               | enabled or not                |                                        |
        +-------------------------------+-------------------------------+----------------------------------------+
        | g-port-locked                 | indicate locked to G_Port     |:func:`set_g_port_locked`               |
        |                               |                               |:func:`peek_g_port_locked`              |
        +-------------------------------+-------------------------------+----------------------------------------+
        | e-port-disable                | indicate E_Port disabled      |:func:`set_e_port_disable`              |
        |                               |                               |:func:`peek_e_port_disable`             |
        +-------------------------------+-------------------------------+----------------------------------------+
        | d-port-enable                 | indicate D_Port enabled       |:func:`set_d_port_enable`               |
        |                               |                               |:func:`peek_d_port_enable`              |
        +-------------------------------+-------------------------------+----------------------------------------+
        | persistent-disable            | indicate persistently disabled|:func:`set_persistent_disable`          |
        |                               | port                          |:func:`peek_persistent_disable`         |
        +-------------------------------+-------------------------------+----------------------------------------+
        | neighboar/wwn                 | list of neighbors' WWNs       |:func:`peek_neighbor_wwn`               |
        +-------------------------------+-------------------------------+----------------------------------------+
        | fcid                          | FCID of port                  |:func:`peek_fcid`                       |
        +-------------------------------+-------------------------------+----------------------------------------+
        | port-type                     | type of port                  |:func:`peek_port_type`                  |
        +-------------------------------+-------------------------------+----------------------------------------+
        | qos-enabled                   | indicate QoS mode             |:func:`set_qos_enabled`                 |
        |                               |                               |:func:`peek_qos_enabled`                |
        +-------------------------------+-------------------------------+----------------------------------------+
        | compression-configured        | indicate compression mode     |:func:`set_compression_configured`      |
        |                               |                               |:func:`peek_compression_configured`     |
        +-------------------------------+-------------------------------+----------------------------------------+
        | compression-active            | indicate active compression   |:func:`peek_compression_active`         |
        +-------------------------------+-------------------------------+----------------------------------------+
        | encryption-active             | indicate active encryption    |:func:`peek_encryption_active`          |
        +-------------------------------+-------------------------------+----------------------------------------+
        | target-driven-zoning-enable   | target driven zoning mode     |:func:`set_target_driven_zoning_enable` |
        |                               |                               |:func:`peek_target_driven_zoning_enable`|
        +-------------------------------+-------------------------------+----------------------------------------+
        | mirror-port-enabled           | mirrorport  mode              |:func:`set_mirror_port_enabled`         |
        |                               |                               |:func:`peek_mirror_port_enabled`        |
        +-------------------------------+-------------------------------+----------------------------------------+
        | sim-port-enabled              | sim port mode                 |:func:`set_sim_port_enabled`            |
        |                               |                               |:func:`peek_sim_port_enabled`           |
        +-------------------------------+-------------------------------+----------------------------------------+
        | isl-ready-mode-enabled        | isl ready mode                |:func:`set_isl_ready_mode_enabled`      |
        |                               |                               |:func:`peek_isl_ready_mode_enabled`     |
        +-------------------------------+-------------------------------+----------------------------------------+
        | trunk-port-enabled            | trunk-port-enabled            |:func:`set_trunk_port_enabled`          |
        |                               |                               |:func:`peek_trunk_port_enabled`         |
        +-------------------------------+-------------------------------+----------------------------------------+
        | long-distance                 | long distance                 |:func:`peek_long_distance`              |
        +-------------------------------+-------------------------------+----------------------------------------+
        | vc-link-init                  | vc link init                  |:func:`peek_vc_link_init`               |
        +-------------------------------+-------------------------------+----------------------------------------+
        | ex-port-enabled               | ex port mode                  |:func:`set_ex_port_enabled`             |
        |                               |                               |:func:`peek_ex_port_enabled`            |
        +-------------------------------+-------------------------------+----------------------------------------+
        | npiv-enabled                  | Npiv Enabled                  |:func:`set_npiv_enabled`                |
        |                               |                               |:func:`peek_npiv_enabled`               |
        +-------------------------------+-------------------------------+----------------------------------------+
        | npiv-pp-limit                 | Npiv pp-limit                 |:func:`set_npiv_pp_limit`               |
        |                               |                               |:func:`peek_npiv_pp_limit`              |
        +-------------------------------+-------------------------------+----------------------------------------+
        | rate-limit-enabled            | Rate Limit                    |:func:`set_rate_limit_enabled`          |
        |                               |                               |:func:`peek_rate_limit_enabled`         |
        +-------------------------------+-------------------------------+----------------------------------------+
        | csctl-mode-enabled            | csctl mode                    |:func:`set_csctl_mode_enabled`          |
        |                               |                               |:func:`peek_csctl_mode_enabled`         |
        +-------------------------------+-------------------------------+----------------------------------------+
        | port-autodisable-enabled      | sim port mode                 |:func:`set_port_autodisable_enabled`    |
        |                               |                               |:func:`peek_port_autodisable_enabled`   |
        +-------------------------------+-------------------------------+----------------------------------------+
        | e-port-credit                 | e-port-credit                 |:func:`set_e_port_credit`               |
        |                               |                               |:func:`peek_e_port_credit`              |
        +-------------------------------+-------------------------------+----------------------------------------+
        | octet-speed-combo             | octet-speed-combo             |:func:`set_octet_speed_combo`           |
        |                               |                               |:func:`peek_octet_speed_combo`          |
        +-------------------------------+-------------------------------+----------------------------------------+
        | non-dfe-enabled               | non-dfe enabled               |:func:`set_non_dfe_enabled`             |
        |                               |                               |:func:`peek_non_dfe_enabled`            |
        +-------------------------------+-------------------------------+----------------------------------------+
        | fec-enabled                   | fec mode                      |:func:`set_fec_enabled`                 |
        |                               |                               |:func:`peek_fec_enabled`                |
        +-------------------------------+-------------------------------+----------------------------------------+
        | via-tts-fec-enabled           | via-tts-fec mode              |:func:`set_via_tts_fec_enabled`         |
        |                               |                               |:func:`peek_via_tts_fec_enabled`        |
        +-------------------------------+-------------------------------+----------------------------------------+
        | npiv-flogi-logout-enabled     | npiv-flogi-logout mode        |:func:`set_npiv_flogi_logout_enabled`   |
        |                               |                               |:func:`peek_npiv_flogi_logout_enabled`  |
        +-------------------------------+-------------------------------+----------------------------------------+
        | f-port-buffers                | f-port-buffers                |:func:`set_f_port_buffers`              |
        |                               |                               |:func:`peek_f_port_buffers`             |
        +-------------------------------+-------------------------------+----------------------------------------+
        | fault-delay-enabled           | fault-delay mode              |:func:`set_fault_delay_enabled`         |
        |                               |                               |:func:`peek_fault_delay_enabled`        |
        +-------------------------------+-------------------------------+----------------------------------------+
        | credit-recovery-enabled       | credit recovery mode          |:func:`set_credit_recovery_enabled`     |
        |                               |                               |:func:`peek_credit_recovery_enabled`    |
        +-------------------------------+-------------------------------+----------------------------------------+
        | rscn-suppression-enabled      | rscn suppression mode         |:func:`set_rscn_suppression_enabled`    |
        |                               |                               |:func:`peek_rscn_suppression_enabled`   |
        +-------------------------------+-------------------------------+----------------------------------------+
        | los-tov-mode-enabled          | los tov mode mode             |:func:`set_los_tov_mode_enabled`        |
        |                               |                               |:func:`peek_los_tov_mode_enabled`       |
        +-------------------------------+-------------------------------+----------------------------------------+
        | credit-recovery-active        | credit recovery active state  |:func:`peek_credir_recovery_active`     |
        +-------------------------------+-------------------------------+----------------------------------------+
        | fec-active                    | fec active state              |:func:`peek_fec_active`                 |
        +-------------------------------+-------------------------------+----------------------------------------+

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

        """
        self.add(pyfos_rest_util.rest_attribute(
            "debug", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "ishttps", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "ip_addr", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "version", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "vfid", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "credential", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        """
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

        self.load(dictvalues, 1)
