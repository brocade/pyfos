#!/usr/bin/env python3

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

:mod:`switch_config_obj` - PyFOS util for specific config op use case.
***********************************************************************************
The :mod:`switch_config_obj` lists objects and its procesing handlers

This module lists objects and its processing handlers for switch
config scripts.

"""

import pyfos.pyfos_brocade_access_gateway as access_gateway
import pyfos.pyfos_brocade_chassis as chassis
import pyfos.pyfos_brocade_extension_ip_interface as extension_ip_interface
import pyfos.pyfos_brocade_extension_ip_route as extension_ip_route
import pyfos.pyfos_brocade_extension_ipsec_policy as extension_ipsec_policy
import pyfos.pyfos_brocade_extension_tunnel as extension_tunnel
import pyfos.pyfos_brocade_fabric as fabric
import pyfos.pyfos_brocade_fdmi as fdmi
import pyfos.pyfos_brocade_fibrechannel_configuration as configuration
import pyfos.pyfos_brocade_fibrechannel_diagnostics as diagnostics
import pyfos.pyfos_brocade_fibrechannel_logical_switch as logical_switch
import pyfos.pyfos_brocade_fibrechannel as fibrechannel
import pyfos.pyfos_brocade_fibrechannel_switch as switch
import pyfos.pyfos_brocade_fru as fru
import pyfos.pyfos_brocade_gigabitethernet as gigabitethernet
import pyfos.pyfos_brocade_logging as logging
import pyfos.pyfos_brocade_media as media
import pyfos.pyfos_brocade_name_server as name_server
import pyfos.pyfos_brocade_security as system_security
import pyfos.pyfos_brocade_fibrechannel_trunk as trunk
import pyfos.pyfos_brocade_zone as zone
import switch_config_util


objects_to_process = [
    {
        "obj_name": access_gateway.port_group,
    },
    {
        "obj_name": access_gateway.f_port_list,
    },
    {
        "obj_name": access_gateway.policy,
    },
    {
        "obj_name": access_gateway.n_port_settings,
    },
    {
        "obj_name": access_gateway.n_port_map,
    },
    {
        "obj_name": access_gateway.device_list,
    },
    {
        "obj_name": chassis.chassis,
    },
    {
        "obj_name": chassis.ha_status,
    },
    {
        "obj_name": extension_ip_interface.extension_ip_interface,
    },
    {
        "obj_name": extension_ip_route.extension_ip_route,
    },
    {
        "obj_name": extension_ipsec_policy.extension_ipsec_policy,
    },
    {
        "obj_name": extension_tunnel.extension_tunnel,
    },
    {
        "obj_name": extension_tunnel.extension_tunnel_statistics,
    },
    {
        "obj_name": extension_tunnel.extension_circuit,
    },
    {
        "obj_name": extension_tunnel.extension_circuit_statistics,
    },
    {
        "obj_name": fabric.fabric_switch,
    },
    {
        "obj_name": fdmi.hba,
    },
    {
        "obj_name": fdmi.port,
    },
    {
        "obj_name": configuration.switch_configuration,
    },
    {
        "obj_name": configuration.f_port_login_settings,
    },
    {
        "obj_name": diagnostics.fibrechannel_diagnostics,
    },
    {
        "obj_name": logical_switch.fibrechannel_logical_switch,
    },
    {
        "obj_name": fibrechannel.fibrechannel,
    },
    {
        "obj_name": fibrechannel.fibrechannel_statistics,
    },
    {
        "obj_name": switch.fibrechannel_switch,
    },
    {
        "obj_name": fru.fan,
    },
    {
        "obj_name": fru.power_supply,
    },
    {
        "obj_name": fru.blade,
    },
    {
        "obj_name": gigabitethernet.gigabitethernet,
    },
    {
        "obj_name": gigabitethernet.gigabitethernet_statistics,
    },
    {
        "obj_name": logging.raslog,
    },
    {
        "obj_name": logging.raslog_module,
    },
    {
        "obj_name": logging.log_quiet_control,
    },
    {
        "obj_name": logging.log_setting,
    },
    {
        "obj_name": logging.audit,
    },
    {
        "obj_name": logging.syslog_server,
    },
    {
        "obj_name": media.media_rdp,
    },
    {
        "obj_name": name_server.fibrechannel_name_server,
    },
    {
        "obj_name": system_security.radius_server,
    },
    {
        "obj_name": system_security.tacacs_server,
    },
    {
        "obj_name": system_security.ldap_server,
    },
    {
        "obj_name": system_security.auth_spec,
    },
    {
        "obj_name": system_security.ipfilter_policy,
    },
    {
        "obj_name": system_security.ipfilter_rule,
    },
    {
        "obj_name": system_security.sec_crypto_cfg,
    },
    {
        "obj_name": system_security.sec_crypto_cfg_template,
    },
    {
        "obj_name": system_security.sec_crypto_cfg_template_action,
    },
    {
        "obj_name": system_security.ldap_role_map,
    },
    {
        "obj_name": system_security.password_cfg,
    },
    {
        "obj_name": system_security.user_specific_password_cfg,
    },
    {
        "obj_name": system_security.user_config,
    },
    {
        "obj_name": system_security.sshutil,
    },
    {
        "obj_name": system_security.sshutil_key,
    },
    {
        "obj_name": system_security.sshutil_public_key_action,
    },
    {
        "obj_name": system_security.sshutil_public_key,
    },
    {
        "obj_name": system_security.password,
    },
    {
        "obj_name": system_security.security_certificate,
    },
    {
        "obj_name": system_security.security_certificate_generate,
    },
    {
        "obj_name": system_security.security_certificate_action,
    },
    {
        "obj_name": trunk.trunk,
    },
    {
        "obj_name": trunk.performance,
    },
    {
        "obj_name": trunk.trunk_area,
    },
    {
        "obj_name": zone.defined_configuration,
        "writer": switch_config_util.write_defined_zone_object,
        "reader": switch_config_util.read_defined_zone_object,
        "after_patch_post_delete": switch_config_util.save_change_defined_zone_object,
    },
    {
        "obj_name": zone.effective_configuration,
        "writer": switch_config_util.write_effective_zone_object,
        "reader": switch_config_util.read_effective_zone_object,
        "during_patch": switch_config_util.during_patch_effective_zone_object,
        "after_patch_post_delete": switch_config_util.save_change_effective_zone_object,
    },
]
