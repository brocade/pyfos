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

# Used to document the utils scripts mapping to pyfos objects
import pyfos.pyfos_rest_util as rest_util
import pyfos.pyfos_type as pyfos_type

# pylint: disable=W0105
"""
UTILS Dictionary start
"""

brcd_utils_dict = dict()

brcd_utils_dict.update({
    "zoning_alias": {
        "defined_configuration":
            ["alias_alias_name",
             "alias_member_entry_alias_entry_name"]
    },
    "zoning_cfg_enable": {
        "effective_configuration":
            ["cfg_name"]
    },
    "zoning_cfg": {
        "defined_configuration":
            ["cfg_cfg_name",
             "cfg_member_zone_zone_name"]
    },
    "zoning_pzone": {
        "defined_configuration":
            ["zone_zone_name",
             "zone_member_entry_principal_entry_name",
             "zone_member_entry_entry_name"]
    },
    "zoning_zone": {
        "defined_configuration":
            ["zone_zone_name",
             "zone_member_entry_entry_name"]
    },
})

brcd_utils_dict.update({
    "logical_switch": {
        "fibrechannel-logical-switch":
            ["base_switch_enabled",
             "ficon_mode_enabled",
             "logical_isl_enabled",
             "port_member_list_port_member",
             "ge_port_member_list_port_member"]
    },
})

brcd_utils_dict.update({
    "time_zone": {
        "time-zone":
            ["name",
             "gmt_offset_hours",
             "gmt_offset_minutes"]
    },
    "clock_server": {
        "clock-server":
            ["ntp_server_address"]
    }
})

brcd_utils_dict.update({
    "radius_server": {
        "radius-server":
            ["server",
             "port",
             "timeout",
             "secret",
             "authentication",
             "position",
             "encryption_type"]
    },
    "tacacs_server": {
        "tacacs-server":
            ["server",
             "port",
             "timeout",
             "secret",
             "authentication",
             "position",
             "encryption_type"]
    },
    "ldap_server": {
        "ldap-server":
            ["server",
             "port",
             "timeout",
             "domain",
             "position",
             "tls_mode"]
    },
    "auth_spec": {
        "auth-spec":
            ["authentication_mode",
             "activate_no_log_out",
             "primary_auth_log_messages"]
    },
    "ipfilter_policy": {
        "ipfilter-policy":
            ["name",
             "ip_version",
             "action",
             "clone_destination_policy_name"]
    },
    "ipfilter_rule": {
        "ipfilter-rule":
            ["policy_name",
             "index",
             "source_ip",
             "destination_start_port",
             "destination_end_port",
             "protocol",
             "permission",
             "traffic_type",
             "destination_ip"]
    },
    "sec_crypto_cfg": {
        "sec-crypto-cfg":
            None
    },
    "sec_crypto_cfg_template": {
        "sec-crypto-cfg-template":
            ["name"]
    },
    "sec_crypto_cfg_template_action": {
        "sec-crypto-cfg-template-action":
            ["template_name",
             "remote_user_name",
             "action",
             "remote_host_ip",
             "remote_user_password",
             "remote_directory",
             "file_transfer_protocol_type"]
    },
    "ldap_role_map": {
        "ldap-role-map":
            ["ldap_role",
             "switch_role",
             "home_virtual_fabric",
             "chassis_access_role",
             "map_attributes_virtual_fabric_role_id"]
    },
    "password_cfg": {
        "password-cfg":
            ["minimum_length",
             "character_set",
             "user_name_allowed",
             "minimum_lower_case_character",
             "minimum_upper_case_character",
             "minimum_numeric_character",
             "minimum_special_character",
             "past_password_history",
             "minimum_password_age",
             "maximum_password_age",
             "warn_on_expire",
             "lock_out_threshold",
             "lock_out_duration",
             "admin_lock_out_enabled",
             "repeat_character_limit",
             "sequence_character_limit",
             "password_config_changed",
             "reverse_user_name_allowed",
             "hash_type",
             "manual_hash_enabled",
             "enforce_expire",
             "minimum_difference",
             "password_action"]
    },
    "user_specific_password_cfg": {
        "user-specific-password-cfg":
            ["minimum_password_age",
             "maximum_password_age",
             "warn_on_expire",
             "enforce_expire",
             "hash_type"]
    },
    "user_config": {
        "user-config":
            ["name",
             "password",
             "role",
             "account_description",
             "account_enabled",
             "password_change_enforced",
             "account_locked",
             "access_start_time",
             "access_end_time",
             "home_virtual_fabric",
             "chassis_access_role",
             "virtual_fabric_role_id_list"]
    },
    "sshutil": {
        "sshutil":
            ["allow_user_name",
             "rekey_interval"]
    },
    "sshutil_key": {
        "sshutil-key":
            ["algorithm_type",
             "key_type",
             "passphrase"]
    },
    "sshutil_public_key": {
        "sshutil-public-key":
            ["user_name"]
    },
    "sshutil_public_key_action": {
        "sshutil-public-key-action":
            ["user_name",
             "public_key_name",
             "remote_host_ip",
             "remote_directory",
             "remote_user_name",
             "remote_user_password",
             "algorithm_type",
             "action"]
    },
    "password": {
        "password":
            ["user_name",
             "old_password",
             "new_password"]
    },
    "security_certificate": {
        "security-certificate":
            ["certificate_entity",
             "certificate_type"]
    },
    "security_certificate_generate": {
        "security-certificate-generate":
            ["certificate_entity",
             "certificate_type",
             "algorithm_type",
             "key_size",
             "hash_type",
             "years",
             "country_name",
             "state_name",
             "locality_name",
             "organization_name",
             "unit_name",
             "domain_name"]
    },
    "security_certificate_action": {
        "security-certificate-action":
            ["certificate_entity",
             "certificate_type",
             "certificate_name",
             "operation",
             "remote_host_ip",
             "protocol",
             "remote_directory",
             "remote_user_name",
             "remote_user_password"]
    },
})

brcd_utils_dict.update({
    "nport_map": {
        "n-port-map":
            None
    },
    "nport_settings": {
        "n-port-settings":
            None
    },
    "fport_list": {
        "f-port-list":
            None
    },
    "port_group": {
        "port-group":
            None
    },
    "seccertmgmt_extension": {
        "security-certificate-extension":
            None
    },
})

brcd_utils_dict.update({
    "powersupply": {
        "power-supply":
            None
    },
    "blade_extncfg": {
        "blade":
            ["extension-app-mode",
             "extension-ve-mode",
             "extension-ge-mode",
             "slot-number"]
    },
    "fan": {
        "fan":
            None
    },
    "blade": {
        "blade":
            None
    },
    "wwn": {
        "wwn":
            None
    },
    "sensor": {
        "sensor":
            None
    },
    "history": {
        "history-log":
            None
    },
})

brcd_utils_dict.update({
    "chassis": {
        "chassis":
            None
    },
    "chassis_name": {
        "chassis":
            ["chassis-user-friendly-name"]
    },
    "chassis_vf_enabled": {
        "chassis":
            ["vf-enabled"]
    },
    "chassis_fcr_enabled": {
        "chassis":
            ["fcr-enabled"]
    },
})

brcd_utils_dict.update({
    "media": {
        "media_rdp":
            None
    },
})

brcd_utils_dict.update({
    "name_server": {
        "fibrechannel-name-server":
            None
    },
})

brcd_utils_dict.update({
    "port_dport": {
        "fibrechannel-diagnostics":
            None
    },
    "port": {
        "fibrechannel":
            None
    },
    "logical_e_port": {
        "logical_e_port":
            None
    },
})

brcd_utils_dict.update({
    "switch": {
        "fibrechannel-switch":
            None
    }
})

brcd_utils_dict.update({
    "fdmi": {
        "hba":
            None
    }
})

brcd_utils_dict.update({
    "configure_dport": {
        "port-configuration":
            None
    },
    "configure_fabric": {
        "fabric":
            None
    },
    "configure_port": {
        "port-configuration":
            None
    },
    "configure_zone": {
        "zone-configuration":
            None
    }
})

brcd_utils_dict.update({
    "dns_config": {
        "fibrechannel-switch":
            ["dns_servers_dns_server",
             "domain_name"]
    }
})

brcd_utils_dict.update({
    "switch_ip_config": {
        "fibrechannel-switch":
            ["ip_address_ip_address",
             "ip_static_gateway_list_ip_static_gateway",
             "subnet_mask"]
    }
})

brcd_utils_dict.update({
    "syslog": {
        "syslog-server":
            ["server",
             "port",
             "secure-mode"]
    }
})

brcd_utils_dict.update({
    "syslog_facility": {
        "log-setting":
            ["syslog-facility-level"]
    }
})

brcd_utils_dict.update({
    "clear_log": {
        "log-setting":
            ["clear-log"]
    }
})

brcd_utils_dict.update({
    "port_trunk_area": {
        "trunk_area":
            ["trunk_index",
             "trunk_members_trunk_member"]
    }
})

brcd_utils_dict.update({
    "trunk_perf": {
        "performance":
            ["group"]
    }
})

brcd_utils_dict.update({
    "trunk_show": {
        "trunk":
            ["group",
             "source_port"]
    }
})

brcd_utils_dict.update({
   "maps_policy": {"maps-policy": ["name", "rule_list", "is_active_policy"]}
})

brcd_utils_dict.update({
    "maps_group": {
        "group":
            ["name",
             "group_type",
             "group_type",
             "group_feature",
             "members"]
    }
})

brcd_utils_dict.update({
    "maps_rule": {
        "rule":
            ["name",
             "monitoring_system",
             "time_base",
             "logical_operator",
             "threshold_value",
             "group_name",
             "actions"]
    }
})

brcd_utils_dict.update({
    "maps_config": {
        "maps-config":
            ["actions",
             "decommission_cfg",
             "recipient_address_list",
             "sender_address",
             "relay_ip_address"]
    }
})

brcd_utils_dict.update({
    "maps_paused_cfg": {
        "paused-cfg":
            ["group_type",
             "members"]
    }
})

brcd_utils_dict.update({
    "maps_dashboard_misc": {
        "dashboard-misc":
            ["clear_data"]
    }
})

brcd_utils_dict.update({
    "maps_get_ssp_report": {
        "switch-status-policy-report":
            None
    },
})

brcd_utils_dict.update({
    "monitoring_system_matrix": {
        "monitoring-system-matrix":
            None
    },
})

brcd_utils_dict.update({
    "maps_system_resources": {
        "system-resources":
            None
    },
})

brcd_utils_dict.update({
    "maps_dashboard_rule": {
        "dashboard-rule":
            None
    },
})

brcd_utils_dict.update({
    "fabric": {
        "fabric-switch":
            None
    },
    "access_gateway": {
         "access-gateway": None
    },

})

brcd_utils_dict.update({
    "snmp_system": {
        "system":
            None
    },
})

brcd_utils_dict.update({
    "snmp_mib_capability": {
        "mib-capability":
            None
    },
})

brcd_utils_dict.update({
    "snmp_trap_capability": {
        "trap-capability":
            None
    },
})

brcd_utils_dict.update({
    "snmp_v1_account": {
        "v1-account":
            None
    },
})

brcd_utils_dict.update({
    "snmp_v1_trap": {
        "v1-trap":
            None
    },
})

brcd_utils_dict.update({
    "snmp_v3_account": {
        "v3-account":
            None
    },
})

brcd_utils_dict.update({
    "snmp_v3_trap": {
        "v3-trap":
            None
    },
})

brcd_utils_dict.update({
    "snmp_access_control": {
        "access-control":
            None
    },
})

brcd_utils_dict.update({
    "fabric_traffic_controller": {
        "fabric-traffic-controller":
            None
    },
})

brcd_utils_dict.update({
    "fabric_operation_parameters": {
        "build-fabric":
            None
    }
})

brcd_utils_dict.update({
    "zone_operation_parameters": {
        "zone-object":
            None
    }
})

brcd_utils_dict.update({
    "routing_configuration": {
        "routing-configuration":
            ["maximum_lsan_count",
             "backbone_fabric_id",
             "shortest_ifl",
             "lsan_enforce_tags_tag",
             "lsan_speed_tag"]
    },
})

brcd_utils_dict.update({
    "edge_fabric_alias": {
        "edge-fabric-alias":
            ["edge_fabric_id",
             "alias_name"]
    },
})

brcd_utils_dict.update({
    "lsan_zone": {
        "lsan-zone":
            None
    },
})

brcd_utils_dict.update({
    "lsan_device": {
        "lsan-device":
            None
    },
})
# Used to document the CLI options
brcd_utils_cli_dict = dict()

"""
Utils Dictionary END
"""


def getcustomcli(name):
    # pylint: disable=W0603
    global brcd_utils_cli_dict
    if name in brcd_utils_cli_dict.keys():
        return brcd_utils_cli_dict[name]
    return None


# """
# CLI Dictionary
# """
brcd_utils_cli_dict.update({
    "effective-configuration": {
        "cfg_name": {
            "help": "set \"cfg-name\"",
            "loption": "name",
            "optional": 0,
            "soption": None,
            "value": 0
        }
    },
    "defined-configuration": {
        "alias_alias_name": {
            "help": "set \"alias-name\"",
            "loption": "name",
            "optional": 0,
            "soption": None
        },
        "alias_member_entry_alias_entry_name": {
            "help": "set \"alias-entry-name\"",
            "loption": "members",
            "optional": 0,
            "soption": None
        },
        "cfg_cfg_name": {
            "help": "set \"cfg-name\"",
            "loption": "name",
            "optional": 0,
            "soption": None
        },
        "cfg_member_zone_zone_name": {
            "help": "set \"zone-name\"",
            "loption": "members",
            "optional": 0,
            "soption": None
        },
        "zone_member_entry_entry_name": {
            "help": "set \"entry-name\"",
            "loption": "members",
            "optional": 0,
            "soption": None
        },
        "zone_member_entry_principal_entry_name": {
            "help": "set \"principal-entry-name\"",
            "loption": "pmembers",
            "optional": 0,
            "soption": None
        },
        "zone_zone_name": {
            "help": "set \"zone-name\"",
            "loption": "name",
            "optional": 0,
            "soption": None
        },
    }
})

brcd_utils_cli_dict.update({
    "gigabitethernet": {
        "enabled_state": {
            "help": "The GE port \"enabled-state\"<0|1>",
            "loption": "enabled-state",
            "optional": 0,
            "soption": "e"
        },
        "name": {
            "help": "The GE slot/port or \"name\".",
            "loption": "name",
            "optional": 0,
            "soption": "n"
        },
        "persistent_disable": {
            "help": "The GE port \"persistent-disable\" value <0|1>",
            "loption": "persistent-disable",
            "optional": 0,
            "soption": "d"
        },
        "speed": {
            "help": "The GE port \"speed\" <10000000000|1000000000>.",
            "loption": "speed",
            "optional": 0,
            "soption": None
        }
    }
})
brcd_utils_cli_dict.update({
    "extension-circuit": {
        "admin_enabled": {
            "help": "set \"admin-enabled\" state of the circuit",
            "loption": "admin-enabled",
            "optional": 1,
            "soption": "a"
        },
        "circuit_id": {
            "help": "set \"circuit-id\" of the circuit",
            "loption": "circuit-id",
            "optional": 0,
            "soption": "c"
        },
        "failover_group_id": {
            "help": "set \"failover-group-id\" for the circuit",
            "loption": "failover-group",
            "optional": 1,
            "soption": "g"
        },
        "local_ha_ip_address": {
            "help": "set \"local-ha-ip-address\" of the Circuit",
            "loption": "local-ha-ip",
            "optional": 0,
            "soption": None
        },
        "local_ip_address": {
            "help": "set \"local-ip-address\" of the Ciruit",
            "loption": "local-ip",
            "optional": 0,
            "soption": "S"
        },
        "maximum_communication_rate": {
            "help": "set \"maximum-communication-rate\" in Kbps",
            "loption": "max-comm-rate",
            "optional": 0,
            "soption": "B"
        },
        "metric": {
            "help": "set \"metric\" for the circuit",
            "loption": "metric",
            "optional": 1,
            "soption": "x"
        },
        "minimum_communication_rate": {
            "help": "set \"minimum-communication-rate\" in Kbps",
            "loption": "min-comm-rate",
            "optional": 0,
            "soption": "b"
        },
        "name": {
            "help": "set \"name\" or slot/port of the circuit",
            "loption": "name",
            "optional": 0,
            "soption": "n"
        },
        "remote_ha_ip_address": {
            "help": "set \"remote-ha-ip-address\" of the circuit",
            "loption": "remote-ha-ip",
            "optional": 1,
            "soption": None
        },
        "remote_ip_address": {
            "help": "set \"remote-ip-address\" of the circuit",
            "loption": "remote-ip",
            "optional": 0,
            "soption": "D"
        }
    }
})
brcd_utils_cli_dict.update({
    "extension-tunnel": {
        "admin_enabled": {
            "help": "set \"admin-enabled\"",
            "loption": "admin-enabled",
            "optional": 0,
            "soption": "a"
        },
        "compression_protocol_fc_compression": {
            "help": "set \"fc-compression\"",
            "loption": "fc-compression",
            "optional": 0,
            "soption": None
        },
        "compression_protocol_ip_compression": {
            "help": "set \"ip-compression\"",
            "loption": "ip-compression",
            "optional": 0,
            "soption": None
        },
        "compression_tunnel": {
            "help": "set \"compression-tunnel\"",
            "loption": "compression-tunnel",
            "optional": 0,
            "soption": "c"
        },
        "fast_write_enabled": {
            "help": "set \"fast-write-enabled\"",
            "loption": "fast-write-enabled",
            "optional": 0,
            "soption": "f"
        },
        "ip_extension": {
            "help": "set \"ip-extension\"",
            "loption": "ip-extension",
            "optional": 0,
            "soption": None
        },
        "ipsec_enabled": {
            "help": "set \"ipsec-enabled\"",
            "loption": "ipsec-enabled",
            "optional": 0,
            "soption": None
        },
        "ipsec_policy": {
            "help": "set \"ipsec-policy\"",
            "loption": "ipsec-policy",
            "optional": 0,
            "soption": None
        },
        "load_level": {
            "help": "set \"load-level\"",
            "loption": "load-level",
            "optional": 0,
            "soption": "l"
        },
        "name": {
            "help": "set \"name\"",
            "loption": "name",
            "optional": 0,
            "soption": "n"
        },
        "tape_read": {
            "help": "set \"tape-read\"",
            "loption": "tape-read",
            "optional": 0,
            "soption": None
        },
        "tape_write": {
            "help": "set \"tape-write\"",
            "loption": "tape-write",
            "optional": 0,
            "soption": None
        },
        "user_friendly_name": {
            "help": "set \"user-friendly-name\"",
            "loption": "user-friendly-name",
            "optional": 0,
            "soption": None
        }
    }
})

brcd_utils_cli_dict.update({
    "extension-ip-interface": {
        "dp_id": {
            "help": "set \"dp-id\"",
            "loption": "dp-id",
            "optional": 0,
            "soption": "d"
        },
        "ip_address": {
            "help": "set \"ip-address\"",
            "loption": "ip-address",
            "optional": 0,
            "soption": None
        },
        "ip_prefix_length": {
            "help": "set \"ip-prefix-length\"",
            "loption": "ip-prefix-length",
            "optional": 0,
            "soption": "p"
        },
        "mtu_size": {
            "help": "set \"mtu-size\"",
            "loption": "mtu-size",
            "optional": 1,
            "soption": "m"
        },
        "name": {
            "help": "set \"name\"",
            "loption": "name",
            "optional": 0,
            "soption": "n"
        },
        "vlan_id": {
            "help": "set \"vlan-id\"",
            "loption": "vlan-id",
            "optional": 1,
            "soption": None
        }
    }
})

brcd_utils_cli_dict.update({
    "extension-ip-route": {
        "dp_id": {
            "help": "set \"dp-id\"",
            "loption": "dp-id",
            "optional": 0,
            "soption": "d"
        },
        "ip_address": {
            "help": "set \"ip-address\"",
            "loption": "ip-address",
            "optional": 0,
            "soption": None
        },
        "ip_gateway": {
            "help": "set \"ip-gateway\"",
            "loption": "ip-gateway",
            "optional": 0,
            "soption": "g"
        },
        "ip_prefix_length": {
            "help": "set \"ip-prefix-length\"",
            "loption": "ip-prefix-length",
            "optional": 0,
            "soption": "p"
        },
        "name": {
            "help": "set \"name\"",
            "loption": "name",
            "optional": 0,
            "soption": "n"
        }
    }
})
brcd_utils_cli_dict.update({
    "port-group": {
        "port_group_id": {
            "help": "Port group ID",
            "loption": "id",
            "optional": 0,
            "soption": None
        },
        "port_group_name": {
            "help": "Port group name",
            "loption": "name",
            "optional": 1,
            "soption": None
        },
        "port_group_n_ports": {
            "help": "N-port members of the port group",
            "loption": "n-port",
            "optional": 0,
            "soption": None
        },
        "port_group_f_ports": {
            "help": "F-port members of the port group",
            "loption": "f-port",
            "optional": 0,
            "soption": None
        },
        "port_group_mode_load_balancing_mode_enabled": {
            "help": "Load balancing mode <0|1>",
            "loption": "lb-mode",
            "optional": 0,
            "soption": None
        },
        "port_group_mode_multiple_fabric_name_monitoring_mode_enabled": {
            "help": "Multiple fabric name monitoring mode <0|1>",
            "loption": "mfnm-mode",
            "optional": 0,
            "soption": None
        }
    }
})
brcd_utils_cli_dict.update({
    "policy": {
        "port_group_policy_enabled": {
            "help": "Port group policy <0|1>",
            "loption": "port-group",
            "optional": 0,
            "soption": None
        },
        "auto_policy_enabled": {
            "help": "Auto policy <0|1>",
            "loption": "auto",
            "optional": 1,
            "soption": None
        },
    }
})
brcd_utils_cli_dict.update({
    "fibrechannel": {
        "pod_license_state": {
            "help": "Set  \"released | reserved\" as a \
value for \"pod-license-state\".",
            "loption": "pod_license_state",
            "optional": 1,
            "soption": None
        },
        "enable": {
            "help":  "--enable",
            "loption": "enable",
            "optional": 0,
        },
        "disable": {
            "help":  "--disable",
            "loption": "disable",
            "optional": 0,
        },
        "name": {
            "help": "Port in slot/port.",
            "loption": "name",
            "optional": 0,
            "soption": "n"
        },
        "persistent_disable": {
            "help": "The Port \"persistent-disable\" value <0|1>",
            "loption": "persistent-disable",
            "optional": 0,
            "soption": "d"
        },
        "mirror_port_enabled": {
            "help": "Set \"mirror-port-enabled\" <0|1>",
            "loption": "mirror_enabled",
            "optional": 0,
            "soption": "m"
        },
        "encryption_enabled": {
            "help": "Set \"encryption-enabled\" <0|1>",
            "loption": "enc_enabled",
            "optional": 0,
        },
        "compression_configured": {
            "help": "Set \"compression-configured\" <0|1>",
            "loption": "comp_enabled",
            "optional": 0,
        },
        "enabled_state": {
            "help": "\"enable | disable\" <1|0>",
            "loption": "enabled_state",
            "optional": 0,
            "soption": "e"
        },
        "fault_delay_enabled": {
            "help": "Set \"fault-delay-enabled\" <0|1>",
            "loption": "fault_delay_enabled",
            "optional": 0,
        },
        "sim_port_enabled": {
            "help": "Set \"sim-port-enabled\" <0|1>",
            "loption": "sim_enabled",
            "optional": 0,
        },
        "trunk_port_enabled": {
            "help": "Set \"trunk-port-enabled\" <0|1>",
            "loption": "trunk_port_enabled",
            "optional": 0,
        },
        "isl_ready_mode_enabled": {
            "help": "Set \"isl-ready-mode-enabled\" <0|1>",
            "loption": "isl_ready_enabled",
            "optional": 0,
        },
        "npiv_enabled": {
            "help": "Set \"npiv-enabled\" <0|1>",
            "loption": "npiv_enabled",
            "optional": 0,
        },
        "port_autodisable_enabled": {
            "help": "Set \"port-autodisable-enabled\" <0|1>",
            "loption": "autodisable_enabled",
            "optional": 0,
        },
        "credit_recovery_enabled": {
            "help": "Set \"credit_recovery_enabled\" <0|1>",
            "loption": "credit_recovery_enabled",
            "optional": 0,
        },
        "los_tov_mode_enabled": {
            "help": "Set \"los-tov-mode-enabled\" <0|1>",
            "loption": "los_tov_enabled",
            "optional": 0,
        },
        "ex_port_enabled": {
            "help": "Set \"ex_port_enabled\" <0|1>",
            "loption": "exportstate",
            "optional": 0,
        },
        "edge_fabric_id": {
            "help": "Set the fabric id for edge switch",
            "loption": "edgefid",
            "optional": 0,
        },
        "preferred_front_domain_id": {
            "help": "Set the preffered front domain id",
            "loption": "frontdomid",
            "optional": 0,
        },
    }
})
brcd_utils_cli_dict.update({
    "n-port-map": {
        "n_port": {
            "help": "N-Port Name",
            "loption": "n-port",
            "optional": 0,
            "soption": None
        },
        "configured_f_port_list": {
            "help": "List of mapped F-ports",
            "loption": "config-f-ports",
            "optional": 1,
            "soption": None
        },
        "static_f_port_list": {
            "help": "List of statically mapped F-ports",
            "loption": "static-f-ports",
            "optional": 1,
            "soption": None
        },
        "preferred_f_ports": {
            "help": "List of preferred mapped F-ports",
            "loption": "preferred-f-port",
            "optional": 1,
            "soption": None
        },
        "failback_enabled": {
            "help": "Failback mode of N-port <0|1>",
            "loption": "failback",
            "optional": 1,
            "soption": None
        },
        "failover_enabled": {
            "help": "Failover mode of N-port <0|1>",
            "loption": "failover",
            "optional": 1,
            "soption": None
        }
    }
})
brcd_utils_cli_dict.update({
    "fibrechannel-name-server": {
        "port_id": {
            "help": "Port ID. [OPTIONAL]",
            "loption": "port-id",
            "optional": 1,
            "soption": None
        }
    }
})
brcd_utils_cli_dict.update({
    "hba": {
        "hba_id": {
            "help": "HBA ID. [OPTIONAL]",
            "loption": "hba-id",
            "optional": 1,
            "soption": None
        }
    }
})
brcd_utils_cli_dict.update({
    "port-configuration": {
        "portname_mode": {
            "help": "Portname mode",
            "loption": "portname-mode",
            "optional": 1,
            "soption": None
        },
        "dynamic_portname_format": {
            "help": "Dynamic portname format [OPTIONAL]",
            "loption": "dynamic-portname-format",
            "optional": 1,
            "soption": None
        },
        "dynamic_d_port_enabled": {
            "help": "Dynamic D-port mode",
            "loption": "dynamic-d-port-enabled",
            "optional": 0,
            "soption": None
        },
        "on_demand_d_port_enabled": {
            "help": "On Demand D-port mode",
            "loption": "on-demand-d-port-enabled",
            "optional": 0,
            "soption": None
        }
    },
    "zone-configuration": {
        "node_name_zoning_enabled": {
            "help": "Enable node name zoning",
            "loption": "node-name-zoning-enabled",
            "optional": 1,
            "soption": "n"
        },
        "fabric_lock_timeout": {
            "help": "Set the zone fabric lock timeout",
            "loption": "timeout",
            "optional": 1,
            "soption": "t"
        }
    }
})

brcd_utils_cli_dict.update({
    "fabric": {
        "insistent_domain_id_enabled": {
            "help": "\tSet consistent domain ID of the switch",
            "loption": "insistent-domain-id-enabled",
            "optional": 0,
            "soption": None
        },
        "principal_selection_enabled": {
            "help": "\tSets principal selection mode in the switch",
            "loption": "principal-selection-enabled",
            "optional": 0,
            "soption": None
        },
        "principal_priority": {
            "help": "\tSet priority value for principal switch selection",
            "loption": "principal-priority",
            "optional": 0,
            "soption": None
        }
    }
})

brcd_utils_cli_dict.update({
   "access-gateway": {
           "switch_wwn": {
            "help": "switch wwn",
            "loption": "wwn",
            "optional": 0,
            "soption": None
           },
           "user_friendly_name": {
            "help": "user name",
            "loption": "name",
            "optional": 0,
            "soption": None
           },
           "firmware_version": {
            "help": "version",
            "loption": "version",
            "optional": 0,
            "soption": None
           },
           "ip-addresses": {
            "help": "ip address",
            "loption": "ip",
            "optional": 0,
            "soption": None
           },
           "is-edge-ag": {
            "help": "edge ag",
            "loption": "edge",
            "optional": 0,
            "soption": None
           },
    }
})

brcd_utils_cli_dict.update({
    "fibrechannel-logical-switch": {
        "fabric_id": {
            "help": "set Fabric ID of LS this action is targeting",
            "loption": "fabric-id",
            "optional": 0,
            "soption": None
        },
        "base_switch_enabled": {
            "help": "set base switch mode <0|1>",
            "loption": "base",
            "optional": 1,
            "soption": None
        },
        "logical_isl_enabled": {
            "help": "set logical ISL state <0|1>",
            "loption": "lislenable",
            "optional": 1,
            "soption": None
        },
        "ficon_mode_enabled": {
            "help": "set FICON mode <0|1>",
            "loption": "ficon",
            "optional": 1,
            "soption": None
        },
        "port_member_list_port_member": {
            "help": "set port members of the logical switch <\"3/4;3/5\">",
            "loption": "ports",
            "optional": 1,
            "soption": None
        },
        "ge_port_member_list_port_member": {
            "help": "GE port members of the logical switch <\"3/4;3/5\">",
            "loption": "geports",
            "optional": 1,
            "soption": None
        }
    }
})
brcd_utils_cli_dict.update({
    "sshutil": {
        "allow_user_name": {
            "help": "allow-user-name",
            "loption": "allow-user-name",
            "optional": 1,
            "soption": None
        },
        "rekey_interval": {
            "help": "rekey duration",
            "loption": "rekey-interval",
            "optional": 1,
            "soption": None
        },
    }
})
brcd_utils_cli_dict.update({
    "sshutil-key": {
        "algorithm_type": {
            "help": "algorithm type",
            "loption": "algorithm-type",
            "optional": 1,
            "soption": None
        },
        "key_type": {
            "help": "key type(public-private-key or host-key)",
            "loption": "key-type",
            "optional": 1,
            "soption": None
        },
        "passphrase": {
            "help": "passphrase for creating public-private key pair",
            "loption": "passphrase",
            "optional": 0,
            "soption": None
        }
    }
})
brcd_utils_cli_dict.update({
    "sshutil-public-key": {
        "user_name": {
            "help": "user-name",
            "loption": "user-name",
            "optional": 1,
            "soption": None
        },
    }
})
brcd_utils_cli_dict.update({
    "sshutil-public-key-action": {
        "user_name": {
            "help": "user-name",
            "loption": "user-name",
            "optional": 1,
            "soption": None
        },
        "public_key_name": {
            "help": "public key name with a .pub extension",
            "loption": "public-key-name",
            "optional": 1,
            "soption": None
        },
        "remote_host_ip": {
            "help": "remote host ip address",
            "loption": "remote-host-ip",
            "optional": 1,
            "soption": None
        },
        "remote_directory": {
            "help": "remote directory name",
            "loption": "remote-dir",
            "optional": 1,
            "soption": None
        },
        "remote_user_name": {
            "help": "remote host's user name",
            "loption": "remote-user-name",
            "optional": 1,
            "soption": None
        },
        "remote_user_password": {
            "help": "remote host's password",
            "loption": "remote-user-password",
            "optional": 1,
            "soption": None
        },
        "algorithm_type": {
            "help": "algorithm type",
            "loption": "algorithm-type",
            "optional": 1,
            "soption": None
        },
        "action": {
            "help": "operation to perform",
            "loption": "action",
            "optional": 1,
            "soption": None
        }
    }
})
brcd_utils_cli_dict.update({
    "password": {
        "user_name": {
            "help": "user-name",
            "loption": "user-name",
            "optional": 1,
            "soption": None
        },
        "old_password": {
            "help": "existing password in base64",
            "loption": "old-password",
            "optional": 1,
            "soption": None
        },
        "new_password": {
            "help": "new password in base64",
            "loption": "new-password",
            "optional": 1,
            "soption": None
        },
    }
})
brcd_utils_cli_dict.update({
    "security_certificate": {
        "certificate_entity": {
            "help": "CSR/switch/CA-client/CA-server certificate",
            "loption": "certificate-entity",
            "optional": 1,
            "soption": None
        },
        "certificate_type": {
            "help": "Certificate type",
            "loption": "certificate-type",
            "optional": 1,
            "soption": None
        },
    }
})
brcd_utils_cli_dict.update({
    "security_certificate_generate": {
        "certificate_entity": {
            "help": "CSR/switch/CA-client/CA-server certificate",
            "loption": "certificate-entity",
            "optional": 1,
            "soption": None
        },
        "certificate_type": {
            "help": "Certificate type",
            "loption": "certificate-type",
            "optional": 1,
            "soption": None
        },
        "algorithm_type": {
            "help": "algorithm type",
            "loption": "algorithm-type",
            "optional": 1,
            "soption": None
        },
        "key_size": {
            "help": "size of the key",
            "loption": "key-size",
            "optional": 1,
            "soption": None
        },
        "hash_type": {
            "help": "hash type",
            "loption": "hash-type",
            "optional": 1,
            "soption": None
        },
        "years": {
            "help": "certificate validity",
            "loption": "years",
            "optional": 1,
            "soption": None
        },
        "country_name": {
            "help": "country name",
            "loption": "country-name",
            "optional": 1,
            "soption": None
        },
        "state_name": {
            "help": "state name",
            "loption": "state-name",
            "optional": 1,
            "soption": None
        },
        "locality_name": {
            "help": "locality name",
            "loption": "locality-name",
            "optional": 1,
            "soption": None
        },
        "organization_name": {
            "help": "organization name",
            "loption": "organization-name",
            "optional": 1,
            "soption": None
        },
        "unit_name": {
            "help": "unit name",
            "loption": "unit-name",
            "optional": 1,
            "soption": None
        },
        "domain_name": {
            "help": "domain name",
            "loption": "domain-name",
            "optional": 1,
            "soption": None
        },
    }
})
brcd_utils_cli_dict.update({
    "security_certificate_action": {
        "certificate_entity": {
            "help": "CSR/switch/CA-client/CA-server certificate",
            "loption": "certificate-entity",
            "optional": 1,
            "soption": None
        },
        "certificate_type": {
            "help": "Certificate type",
            "loption": "certificate-type",
            "optional": 1,
            "soption": None
        },
        "certificate_name": {
            "help": "certificate name",
            "loption": "certificate-name",
            "optional": 1,
            "soption": None
        },
        "operation": {
            "help": "seccertmgmt operation",
            "loption": "operation",
            "optional": 1,
            "soption": None
        },
        "remote_host_ip": {
            "help": "remote host ip address",
            "loption": "remote-host-ip",
            "optional": 1,
            "soption": None
        },
        "protocol": {
            "help": "remote connection protocol",
            "loption": "protocol",
            "optional": 1,
            "soption": None
        },
        "remote_directory": {
            "help": "remote directory name",
            "loption": "remote-dir",
            "optional": 1,
            "soption": None
        },
        "remote_user_name": {
            "help": "remote host's user name",
            "loption": "remote-user-name",
            "optional": 1,
            "soption": None
        },
        "remote_user_password": {
            "help": "remote host's password",
            "loption": "remote-user-password",
            "optional": 1,
            "soption": None
        },
    }
})
brcd_utils_cli_dict.update({
    "fibrechannel-switch": {
        "ag_mode": {
            "help": "set ag-mode (enable = 3, disable = 1)",
            "loption": "ag-mode",
            "optional": 0,
            "soption": None
        },
        "dns_servers_dns_server": {
            "help": "\tSet list of maximum 2 DNS servers in IP Address;" +
            "IP Address format",
            "loption": "dns-servers",
            "optional": 1,
            "soption": "d"
        },
        "domain_name": {
            "help": "\tSet domain name of the switch",
            "loption": "domain-name",
            "optional": 1,
            "soption": "n"
        },
        "ip_address_ip_address": {
            "help": "\tSet list of maximum 2 addresses in IP Address;" +
            "IP Address format",
            "loption": "addresses",
            "optional": 1,
            "soption": None
        },
        "ip_static_gateway_list_ip_static_gateway": {
            "help": "\tSet list of maximum 2 gateways in IP Address;" +
            "IP Address format",
            "loption": "gateways",
            "optional": 1,
            "soption": "g"
        },
        "subnet_mask": {
            "help": "\tSet subnet mask for the switch",
            "loption": "mask",
            "optional": 1,
            "soption": "m"
        }
    }
})
brcd_utils_cli_dict.update({
    "chassis": {
        "chassis_user_friendly_name": {
            "help": "set user friendly name",
            "loption": "user-name",
            "optional": 0,
            "soption": None
        },
        "vf_enabled": {
            "help": "set VF enabled-state (enable=true, disable=false)",
            "loption": "vf-enabled",
            "optional": 0,
            "soption": None
        },
        "fcr_enabled": {
            "help": "set FCR enabled-state (enable=true, disable=false)",
            "loption": "fcr-enabled",
            "optional": 0,
            "soption": None
        },
    }
})
brcd_utils_cli_dict.update({
    "media-rdp": {
        "name": {
            "help": "Port in Interface/slot/port.",
            "loption": "name",
            "optional": 0,
            "soption": None
        },
    }
})
brcd_utils_cli_dict.update({
    "trunk_area": {
        "trunk_index": {
            "help": "Trunk Index of trunk group",
            "loption": "trunk_index",
            "optional": 0,
            "soption": None
        },
        "trunk_members": {
            "help": "Trunk members of trunk group slot/port format",
            "loption": "trunk_members",
            "optional": 0,
            "soption": None
        },
    }
})

brcd_utils_cli_dict.update({
    "trunk": {
        "group": {
            "help": "Trunk Index of trunk group",
            "loption": "group",
            "optional": 0,
            "soption": None
        },
        "source_port": {
            "help": "Source port of the trunk group",
            "loption": "source_port",
            "optional": 0,
            "soption": None
        },
    }
})

brcd_utils_cli_dict.update({
    "performance": {
        "group": {
            "help": "Trunk Index of trunk group",
            "loption": "group",
            "optional": 0,
            "soption": None
        },
    }
})

brcd_utils_cli_dict.update({
    "auth-spec": {
        "authentication_mode": {
            "help": "Authentication mode for RADIUS, TACACS+ and LDAP",
            "loption": "authentication-mode",
            "optional": 0,
            "soption": None
        },
        "activate_no_log_out": {
            "help": "Enable/disable log out session after changing mode",
            "loption": "activate-no-log-out",
            "optional": 0,
            "soption": None
        },
        "primary_auth_log_messages": {
            "help": "Enable/disable messages for authentication failure",
            "loption": "primary-auth-log-messages",
            "optional": 0,
            "soption": None
        },
    }
})

brcd_utils_cli_dict.update({
    "radius-server": {
        "server": {
            "help": "Set an IP address or a server name in " +
            "dot-decimal notation",
            "loption": "server",
            "optional": 1,
            "soption": None
        },
        "port": {
            "help": "Set the RADIUS server port number",
            "loption": "port",
            "optional": 1,
            "soption": None
        },
        "timeout": {
            "help": "Set the response timeout for the RADIUS server",
            "loption": "timeout",
            "optional": 1,
            "soption": None
        },
        "secret": {
            "help": "Set a common secret between the switch and the" +
            " RADIUS  server",
            "loption": "secret",
            "optional": 1,
            "soption": None
        },
        "authentication": {
            "help": "Set the remote authentication protocol for the" +
            " RADIUS server",
            "loption": "authentication",
            "optional": 1,
            "soption": None
        },
        "position": {
            "help": "Set the position to which RADIUS server" +
            " needs to be moved",
            "loption": "position",
            "optional": 1,
            "soption": None
        },
        "encryption_type": {
            "help": "Set the Encryption algorithm type for" +
            " the RADIUS server.",
            "loption": "encryption-type",
            "optional": 1,
            "soption": None
        },
    }
})

brcd_utils_cli_dict.update({
    "tacacs-server": {
        "server": {
            "help": "Set an IP address or a server name in" +
            " dot-decimal notation",
            "loption": "server",
            "optional": 1,
            "soption": None
        },
        "port": {
            "help": "Set the TACACS+ server port number",
            "loption": "port",
            "optional": 1,
            "soption": None
        },
        "timeout": {
            "help": "Set the response timeout for the TACACS+ server",
            "loption": "timeout",
            "optional": 1,
            "soption": None
        },
        "secret": {
            "help": "Set a common secret between the switch and" +
            " the TACACS+ server",
            "loption": "secret",
            "optional": 1,
            "soption": None
        },
        "authentication": {
            "help": "Set the remote authentication protocol for" +
            " the TACACS+ server",
            "loption": "authentication",
            "optional": 1,
            "soption": None
        },
        "position": {
            "help": "Set the position to which TACACS+ server" +
            " needs to be moved",
            "loption": "position",
            "optional": 1,
            "soption": None
        },
        "encryption_type": {
            "help": "Set the Encryption algorithm type for the TACACS+ server",
            "loption": "encryption-type",
            "optional": 1,
            "soption": None
        },
    }
})

brcd_utils_cli_dict.update({
    "ldap-server": {
        "server": {
            "help": "Set an IP address or a server name in" +
            " dot-decimal notation",
            "loption": "server",
            "optional": 1,
            "soption": None
        },
        "port": {
            "help": "Set the LDAP server port number",
            "loption": "port",
            "optional": 1,
            "soption": None
        },
        "timeout": {
            "help": "Set the response timeout for the LDAP server",
            "loption": "timeout",
            "optional": 1,
            "soption": None
        },
        "domain": {
            "help": "Set the name of the active directory domain",
            "loption": "domain",
            "optional": 1,
            "soption": None
        },
        "position": {
            "help": "Set the position to which LDAP server needs to be moved",
            "loption": "position",
            "optional": 1,
            "soption": None
        },
        "tls_mode": {
            "help": "Set the TLS mode for the LDAP server",
            "loption": "tls-mode",
            "optional": 1,
            "soption": None
        },
    }
})

brcd_utils_cli_dict.update({
    "ldap-role-map": {
        "ldap_role": {
            "help": "Set the LDAP role to be mapped to a switch role",
            "loption": "ldap-role",
            "optional": 1,
            "soption": None
        },
        "switch_role": {
            "help": "Set the switch role to which the LDAP role is mapped",
            "loption": "switch-role",
            "optional": 1,
            "soption": None
        },
        "home_virtual_fabric": {
            "help": "Set the account's home Fabric ID",
            "loption": "home-id",
            "optional": 1,
            "soption": None
        },
        "chassis_access_role": {
            "help": "Set the account's access permissions regarding" +
            " chassis-level commands",
            "loption": "chassis-access-role",
            "optional": 1,
            "soption": None
        },
        "map_attributes_virtual_fabric_role_id": {
            "help": "Set the attributes to an existing LDAP role",
            "loption": "map-attributes",
            "optional": 1,
            "soption": None
        },
    }
})

brcd_utils_cli_dict.update({
    "password-cfg": {
        "minimum_length": {
            "help": "Set the minimum length of the password",
            "loption": "minimum-length",
            "optional": 1,
            "soption": None
        },
        "character_set": {
            "help": "Set the minimum criteria on the character set",
            "loption": "character-set",
            "optional": 1,
            "soption": None
        },
        "user_name_allowed": {
            "help": "Set to determine if the username is used in the password",
            "loption": "user-name-allowed",
            "optional": 1,
            "soption": None
        },
        "minimum_lower_case_character": {
            "help": "Set the minimum number of lowercase" +
            " alphabetic characters",
            "loption": "min-lower-case-char",
            "optional": 1,
            "soption": None
        },
        "minimum_upper_case_character": {
            "help": "Set the minimum number of uppercase" +
            " alphabetic characters",
            "loption": "min-upper-case-char",
            "optional": 1,
            "soption": None
        },
        "minimum_numeric_character": {
            "help": "Set the minimum number of numeric digits",
            "loption": "min-numeric-char",
            "optional": 1,
            "soption": None
        },
        "minimum_special_character": {
            "help": "Set the minimum number of punctuation characters",
            "loption": "min-special-char",
            "optional": 1,
            "soption": None
        },
        "past_password_history": {
            "help": "Set the number of past password values that are" +
            " disallowed",
            "loption": "past-password-history",
            "optional": 1,
            "soption": None
        },
        "minimum_password_age": {
            "help": "Set the minimum number of days before which the" +
            " password cannot be modified",
            "loption": "min-password-age",
            "optional": 1,
            "soption": None
        },
        "maximum_password_age": {
            "help": "Set the maximum number of days after which the" +
            " password should be modified",
            "loption": "max-password-age",
            "optional": 1,
            "soption": None
        },
        "warn_on_expire": {
            "help": "Set the number of days to display warning" +
            " message till password expiration",
            "loption": "warn-on-expire",
            "optional": 1,
            "soption": None
        },
        "lock_out_threshold": {
            "help": "Set the number of times a user can specify" +
            " an incorrect password",
            "loption": "lock-out-threshold",
            "optional": 1,
            "soption": None
        },
        "lock_out_duration": {
            "help": "Set the time to unlock automatically if already locked",
            "loption": "lock-out-duration",
            "optional": 1,
            "soption": None
        },
        "admin_lock_out_enabled": {
            "help": "Set the admin lockout policy",
            "loption": "admin-lock-out-enabled",
            "optional": 1,
            "soption": None
        },
        "repeat_character_limit": {
            "help": "Set the length of repeated character sequences",
            "loption": "repeat-char-limit",
            "optional": 1,
            "soption": None
        },
        "sequence_character_limit": {
            "help": "Set the the length of sequential character sequences",
            "loption": "sequence-character-limit",
            "optional": 1,
            "soption": None
        },
        "password_config_changed": {
            "help": "Set the account password policy status",
            "loption": "password-config-changed",
            "optional": 1,
            "soption": None
        },
        "reverse_user_name_allowed": {
            "help": "Set to determine whether the password is an exact" +
            " reverse username",
            "loption": "reverse-user-name-allowed",
            "optional": 1,
            "soption": None
        },
        "hash_type": {
            "help": "Set the hash type",
            "loption": "hash-type",
            "optional": 1,
            "soption": None
        },
        "manual_hash_enabled": {
            "help": "Set the password change due to hash type change" +
            " can be manual",
            "loption": "manual-hash-enabled",
            "optional": 1,
            "soption": None
        },
        "enforce_expire": {
            "help": "Set to expires the password for the specified user",
            "loption": "enforce-expire",
            "optional": 1,
            "soption": None
        },
        "minimum_difference": {
            "help": "Set the number of minium difference between old" +
            " and new password",
            "loption": "min-diff",
            "optional": 1,
            "soption": None
        },
        "password_action": {
            "help": "Set the action to perform",
            "loption": "password-action",
            "optional": 1,
            "soption": None
        },
    }
})

brcd_utils_cli_dict.update({
    "user-specific-password-cfg": {
        "minimum_password_age": {
            "help": "Set the minimum number of days before which the" +
            " password cannot be modified",
            "loption": "min-password-age",
            "optional": 1,
            "soption": None
        },
        "maximum_password_age": {
            "help": "Set the maximum number of days after which the" +
            " password should be modified",
            "loption": "max-password-age",
            "optional": 1,
            "soption": None
        },
        "warn_on_expire": {
            "help": "Set the number of days prior to password expiration",
            "loption": "warn-on-expire",
            "optional": 1,
            "soption": None
        },
        "enforce_expire": {
            "help": "Set to expires the password for the specified user",
            "loption": "enforce-expire",
            "optional": 1,
            "soption": None
        },
        "hash_type": {
            "help": "hash type",
            "loption": "hash-type",
            "optional": 1,
            "soption": None
        },
    }
})

brcd_utils_cli_dict.update({
    "user-config": {
        "name": {
            "help": "Set the login name of the account",
            "loption": "name",
            "optional": 1,
            "soption": None
        },
        "password": {
            "help": "Set a password for the account",
            "loption": "passwd",
            "optional": 1,
            "soption": None
        },
        "role": {
            "help": "Set the account's role",
            "loption": "role",
            "optional": 1,
            "soption": None
        },
        "account_description": {
            "help": "Set the description for the new account",
            "loption": "account-description",
            "optional": 1,
            "soption": None
        },
        "account_enabled": {
            "help": "Enable/disable a user account",
            "loption": "account-enabled",
            "optional": 1,
            "soption": None
        },
        "password_change_enforced": {
            "help": "Set to expires password",
            "loption": "password-change-enforced",
            "optional": 1,
            "soption": None
        },
        "account_locked": {
            "help": "Set to unlock the specified user" +
            " account if already locked",
            "loption": "account-locked",
            "optional": 1,
            "soption": None
        },
        "access_start_time": {
            "help": "Set the starting time the users can access",
            "loption": "access-start-time",
            "optional": 1,
            "soption": None
        },
        "access_end_time": {
            "help": "Set the ending time the users can access",
            "loption": "access-end-time",
            "optional": 1,
            "soption": None
        },
        "home_virtual_fabric": {
            "help": "Set the account's home Virtual Fabric",
            "loption": "home-virtual-fabric",
            "optional": 1,
            "soption": None
        },
        "chassis_access_role": {
            "help": "Set the account's access permissions" +
            " regarding chassis-level commands",
            "loption": "chassis-access-role",
            "optional": 1,
            "soption": None
        },
        "virtual_fabric_role_id_list": {
            "help": "Set the Virtual Fabrics role and ID to be added",
            "loption": "vf-role-id-list",
            "optional": 1,
            "soption": None
        },
    }
})

brcd_utils_cli_dict.update({
    "ipfilter-policy": {
        "name": {
            "help": "Set an IP filter policy name",
            "loption": "name",
            "optional": 1,
            "soption": None
        },
        "ip_version": {
            "help": "Set an IP filter policy with the type IPv4 or IPv6",
            "loption": "ip-version",
            "optional": 1,
            "soption": None
        },
        "action": {
            "help": "Set the action that must be taken on IpFilter policies",
            "loption": "action",
            "optional": 1,
            "soption": None
        },
        "clone_destination_policy_name": {
            "help": "Set the destination IPFilter policy name for" +
            " clone operation",
            "loption": "destination-policy-name",
            "optional": 1,
            "soption": None
        },
    }
})

brcd_utils_cli_dict.update({
    "ipfilter-rule": {
        "policy_name": {
            "help": "Set the name of the ipfilter policy whose rule" +
            " is to be accessed/modified",
            "loption": "policy-name",
            "optional": 1,
            "soption": None
        },
        "index": {
            "help": "Set the position of the ipfilter rule entry in" +
            " the ip filter table",
            "loption": "index",
            "optional": 1,
            "soption": None
        },
        "source_ip": {
            "help": "Set the source IP address",
            "loption": "source-ip",
            "optional": 1,
            "soption": None
        },
        "destination_start_port": {
            "help": "Set the starting destination port number of the range",
            "loption": "destination-start-port",
            "optional": 1,
            "soption": None
        },
        "destination_end_port": {
            "help": "Set the ending destination port number of the range",
            "loption": "destination-end-port",
            "optional": 1,
            "soption": None
        },
        "protocol": {
            "help": "Set the protocol type, for example, tcp or udp",
            "loption": "protocol",
            "optional": 1,
            "soption": None
        },
        "permission": {
            "help": "Set the permit or deny action associated with this rule",
            "loption": "permission",
            "optional": 1,
            "soption": None
        },
        "traffic_type": {
            "help": "Set the type of traffic that is allowed." +
            " e.g: Input/Forward",
            "loption": "traffic-type",
            "optional": 1,
            "soption": None
        },
        "destination_ip": {
            "help": "Set the destination IP address",
            "loption": "destination-ip",
            "optional": 1,
            "soption": None
        },
    }
})
brcd_utils_cli_dict.update({
    "sec-crypto-cfg-template": {
        "name": {
            "help": "Set the template name",
            "loption": "name",
            "optional": 1,
            "soption": None
        },
    }
})
brcd_utils_cli_dict.update({
    "sec-crypto-cfg-template-action": {
        "template_name": {
            "help": "Set the template name",
            "loption": "template-name",
            "optional": 1,
            "soption": None
        },
        "action": {
            "help": "Set the operation to perform",
            "loption": "action",
            "optional": 1,
            "soption": None
        },
        "remote_user_name": {
            "help": "Set the user name for the host",
            "loption": "user-name",
            "optional": 1,
            "soption": None
        },
        "remote_host_ip": {
            "help": "Set the remote host ip address",
            "loption": "host-ip",
            "optional": 1,
            "soption": None
        },
        "remote_user_password": {
            "help": "Set the remote user password",
            "loption": "remote-user-password",
            "optional": 1,
            "soption": None
        },
        "remote_directory": {
            "help": "Set the remote directory absolute path",
            "loption": "remote-directory",
            "optional": 1,
            "soption": None
        },
        "file_transfer_protocol_type": {
            "help": "Set the protocol as either SCP, SFTP, or FTP for file",
            "loption": "protocol-type",
            "optional": 1,
            "soption": None
        },
    }
})

brcd_utils_cli_dict.update({
    "sec-crypto-cfg": {
    }
})

brcd_utils_cli_dict.update({
    "time-zone": {
        "name": {
            "help": "Set the name of a time zone from the time zone database",
            "loption": "name",
            "optional": 1,
            "soption": None
        },
        "gmt_offset_hours": {
            "help": "Set the number of hours relative to GMT",
            "loption": "gmt-offset-hours",
            "optional": 1,
            "soption": None
        },
        "gmt_offset_minutes": {
            "help": "Set the number of minutes relative to hour offset",
            "loption": "gmt-offset-minutes",
            "optional": 1,
            "soption": None
        },
    }
})

brcd_utils_cli_dict.update({
    "clock-server": {
        "ntp_server_address": {
            "help": "Set the NTP address(es)/LOCL",
            "loption": "ntp_server_address",
            "optional": 1,
            "soption": None
        },
    }
})

brcd_utils_cli_dict.update({
    "blade": {
        "slot_number": {
            "help": "set \"slot-number\"",
            "loption": "slot-number",
            "optional": 0,
            "soption": None,
            "value": 0
        },
        "extension_app_mode": {
            "help": "set \"extension-app-mode\"",
            "loption": "app-mode",
            "optional": 0,
            "soption": None,
            "value": 0
        },
        "extension_enabled": {
            "help": "set \"extension-enabled\"",
            "loption": "extension-enabled",
            "optional": 0,
            "soption": None,
            "value": 0
        },
        "extension_ge_mode": {
            "help": "set \"extension-ge-mode\"",
            "loption": "ge-mode",
            "optional": 0,
            "soption": None,
            "value": 0
        },
        "extension_ve_mode": {
            "help": "set \"extension-ve-mode\"",
            "loption": "ve-mode",
            "optional": 0,
            "soption": None,
            "value": 0
        },
    }
})

brcd_utils_cli_dict.update({
    "fan": {
        "unit_number": {
            "help": "set \"unit-number\"",
            "loption": "unit-number",
            "optional": 0,
            "soption": None,
            "value": 0
        },
    }
})

brcd_utils_cli_dict.update({
    "power-supply": {
        "unit_number": {
            "help": "set \"unit-number\"",
            "loption": "unit-number",
            "optional": 0,
            "soption": None,
            "value": 0
        },
    }
})

brcd_utils_cli_dict.update({
    "connection": {
        "host": {
            "help": "Set the remote  server ipaddress/domain-name",
            "loption": "host",
            "optional": 1,
            "soption": None
        },
        "protocol": {
            "help": "Set the protocol(ftp|scp|sftp) used for the remote " +
            "server connection",
            "loption": "protocol",
            "optional": 1,
            "soption": None
        },
        "remote_directory": {
            "help": "Set the remote directory path to copy the supportsave " +
            "files",
            "loption": "path",
            "optional": 1,
            "soption": None
        },
        "user_name": {
            "help": "Set the user name of the remote server",
            "loption": "user",
            "optional": 1,
            "soption": None
        },
        "password": {
            "help": "Set the remote user password in base64 format",
            "loption": "passwd",
            "optional": 1,
            "soption": None
        },
        "serial_mode": {
            "help": "Set to true/false to enable/disable legacy serial-mode " +
            "module supportsave collection",
            "loption": "serial-mode",
            "optional": 0,
            "soption": None
        },
        "port": {
            "help": "User defined port number can be configured only for " +
            "scp/sftp protocol",
            "loption": "port",
            "optional": 0,
            "soption": None
        }
    }
})

brcd_utils_cli_dict.update({
    "switch-configuration": {
        "edge_hold_time": {
            "help": "\tConfigures Edge hold time in seconds. [OPTIONAL]",
            "loption": "edge-hold-time",
            "optional": 1,
            "soption": None
        },
        "wwn_port_id_mode": {
            "help": "\tConfigures port id based on wwn. [OPTIONAL]",
            "loption": "wwn-mode",
            "optional": 1,
            "soption": None
        },
        "area_mode": {
            "help": "\tConfigures port id based on area. [OPTIONAL]",
            "loption": "area-mode",
            "optional": 1,
            "soption": None
        }
    }
})

brcd_utils_cli_dict.update({
    "f-port-login-settings": {
        "enforce_login": {
            "help": "\tConfigures the login type precedence" +
            " during collision for login. [OPTIONAL]",
            "loption": "enforce-login",
            "optional": 1,
            "soption": None
        },
        "free_fdisc": {
            "help": "\tConfigures freely allowed fdisc logins before " +
                    "staging. [OPTIONAL]",
            "loption": "free-fdisc",
            "optional": 1,
            "soption": None
        },
        "max_flogi_rate_per_port": {
            "help": "\tConfigures Max Logins per second in a port. [OPTIONAL]",
            "loption": "max-logins-port",
            "optional": 1,
            "soption": None
        },
        "max_flogi_rate_per_switch": {
            "help": "\tConfigures Max Logins per second in a switch." +
                    " [OPTIONAL]",
            "loption": "max-logins-switch",
            "optional": 1,
            "soption": None
        },
        "max_logins": {
            "help": "\tConfigures system wide Max logins. [OPTIONAL]",
            "loption": "max-logins",
            "optional": 1,
            "soption": None
        },
        "stage_interval": {
            "help": "\tConfigures stage interval time in milliseconds." +
                    " [OPTIONAL]",
            "loption": "stage-interval",
            "optional": 1,
            "soption": None
        }
    }
})

brcd_utils_cli_dict.update({
    "raslog": {
        "message_id": {
            "help": "\tSet Message Id. eg. <AUTH-1001>,<LOG-1001>,<CONF-1043>",
            "loption": "msg",
            "optional": 0,
            "soption": None
        },
        "message_enabled": {
            "help": "\tSet Message Status flag for the raslog <True|False>.",
            "loption": "enable",
            "optional": 1,
            "soption": None
        },
        "syslog_enabled": {
            "help": "\tSet Syslog Status flag for the raslog <True|False>.",
            "loption": "syslog-enable",
            "optional": 1,
            "soption": None
        },
        "current_severity": {
            "help": "\tSet Message Severity for the raslog." +
            " <default|info|warning|error|critical>",
            "loption": "severity",
            "optional": 1,
            "soption": None
        },
    }
})

brcd_utils_cli_dict.update({
    "raslog-module": {
        "module_id": {
            "help": "\tSet FOS Module Id eg. <AUTH>,<LOG>,<CONF>",
            "loption": "module-id",
            "optional": 0,
            "soption": None
        },
        "log_enabled": {
            "help": "\tSet Message Status flag for all the raslog of the" +
            " FOS Module <True|False>. ",
            "loption": "enable",
            "optional": 0,
            "soption": None
        },
    }
})

brcd_utils_cli_dict.update({
    "log-quiet-control": {
        "log_type": {
            "help": "\tSet Log type <audit|raslog>.",
            "loption": "log-type",
            "optional": 0,
            "soption": None
        },
        "quiet_enabled": {
            "help": "\tSet Quiet status flag <True|False>. ",
            "loption": "quiet",
            "optional": 0,
            "soption": None
        },
        "start_time": {
            "help": "\tSet quiet start time <hh:mm>. ",
            "loption": "stime",
            "optional": 1,
            "soption": None
        },
        "end_time": {
            "help": "\tSet quiet end time <hh:mm>. ",
            "loption": "etime",
            "optional": 1,
            "soption": None
        },
        "days_of_week_day": {
            "help": "\tSet days for quiet, eg. --dow \"mon;tue\". ",
            "loption": "dow",
            "optional": 1,
            "soption": None
        }
    }
})

brcd_utils_cli_dict.update({
    "log-setting": {
        "keep_alive_period": {
            "help": "\tSet alive period for log in hours. [0-24]",
            "loption": "alive",
            "optional": 1,
            "soption": None
        },
        "syslog_facility_level": {
            "help": "\tSet facility level. ",
            "loption": "syslog-facility-level",
            "optional": 1,
            "soption": None
        },
        "clear_log": {
            "help": "\tSet it to \"error-log\" to clear errdump, \
\"audit-log\" to clear auditdump, \"all\" to clear both errdump and auditdump",
            "loption": "clear-log",
            "optional": 1,
            "soption": "c"
        }
    }
})

brcd_utils_cli_dict.update({
    "syslog-server": {
        "server": {
            "help": "\tsyslog server address",
            "loption": "server",
            "optional": 0,
            "soption": None
        },
        "secure-mode": {
            "help": "\tEnables or disables secure syslog mode",
            "loption": "secure-mode",
            "optional": 1,
            "soption": None
        },
        "port": {
            "help": "\tsyslog server's port number",
            "loption": "port",
            "optional": 1,
            "soption": None
        }
    }
})
brcd_utils_cli_dict.update({
    "audit": {
        "audit_enabled": {
            "help": "\tEnable or disable audit log configuration (true,false)",
            "loption": "enable",
            "optional": 1,
            "soption": None
        },
        "severity_level": {
            "help": "\tConfigure severity level for audit " +
                    "(info,warning,error,critical)",
            "loption": "severity",
            "optional": 1,
            "soption": None
        },
        "filter_class_list_filter_class": {
            "help": "\tConfigure filter class for audit (zone,security," +
                    "configuration,firmware,fabric,ls,cli,maps)",
            "loption": "filter",
            "optional": 1,
            "soption": None
        }
     }
})

brcd_utils_cli_dict.update({
    "maps-policy": {
        "name": {
            "help": "Set the MAPS policy name",
            "loption": "name",
            "optional": 1,
            "soption": None
        },
        "rule_list": {
            "help": "Set the list of rules in the policy",
            "loption": "rule-list",
            "optional": 1,
            "soption": None
        },
        "is_active_policy": {
            "help": "Enables MAPS policy when set to true",
            "loption": "is-active-policy",
            "optional": 0,
            "soption": None
        },
    }
})

brcd_utils_cli_dict.update({
    "group": {
        "name": {
            "help": "Set the MAPS group name",
            "loption": "name",
            "optional": 1,
            "soption": None
        },
        "group_type": {
            "help": "Set the group type",
            "loption": "group-type",
            "optional": 1,
            "soption": None
        },
        "group_feature": {
            "help": "Set the group feature",
            "loption": "group-feature",
            "optional": 0,
            "soption": None
        },
        "feature_pattern": {
            "help": "Set the feature pattern",
            "loption": "feature-pattern",
            "optional": 0,
            "soption": None
        },
        "members": {
            "help": "Set the members",
            "loption": "members",
            "optional": 0,
            "soption": None
        },
    }
})

brcd_utils_cli_dict.update({
    "rule": {
        "name": {
            "help": "Set the MAPS rule name",
            "loption": "name",
            "optional": 1,
            "soption": None
        },
        "monitoring_system": {
            "help": "Set the monitoring system",
            "loption": "monitoring-system",
            "optional": 1,
            "soption": None
        },
        "time_base": {
            "help": "Set the time base",
            "loption": "time-base",
            "optional": 1,
            "soption": None
        },
        "logical_operator": {
            "help": "Set the logical operator",
            "loption": "logical-operator",
            "optional": 1,
            "soption": None
        },
        "threshold_value": {
            "help": "Set the threshold value",
            "loption": "threshold-value",
            "optional": 1,
            "soption": None
        },
        "group_name": {
            "help": "Set the group name",
            "loption": "group-name",
            "optional": 1,
            "soption": None
        },
        "actions": {
            "help": "Set the list of actions",
            "loption": "actions",
            "optional": 1,
            "soption": None
        },
        "event_severity": {
            "help": "Set the event severity level",
            "loption": "event-severity",
            "optional": 0,
            "soption": None
        },
        "toggle_time": {
            "help": "Set the toggle time",
            "loption": "toggle-time",
            "optional": 0,
            "soption": None
        },
        "quiet_time": {
            "help": "Set the quiet time interval",
            "loption": "quiet-time",
            "optional": 0,
            "soption": None
        },
        "quiet_time_clear": {
            "help": "Clears quiet time interval if this flag is set",
            "loption": "quiet-time-clear",
            "optional": 0,
            "soption": None
        },
        "un_quarantine_timeout": {
            "help": "Set the unquarantine timeout value",
            "loption": "un-quarantine-timeout",
            "optional": 0,
            "soption": None
        },
        "un_quarantine_clear": {
            "help": "Clears the unquarantine timeout value" +
            " if this flag is set",
            "loption": "un-quarantine-clear",
            "optional": 0,
            "soption": None
        },
        "is_rule_on_rule": {
            "help": "This flag is set for creating RoR rules",
            "loption": "is-rule-on-rule",
            "optional": 0,
            "soption": None
        },
    }
})

brcd_utils_cli_dict.update({
    "maps-config": {
        "actions": {
            "help": "Set the MAPS global actions",
            "loption": "actions",
            "optional": 0,
            "soption": None
        },
        "decommission_cfg": {
            "help": "Set the decommision behaviour - default or impair",
            "loption": "decommission-cfg",
            "optional": 0,
            "soption": None
        },
        "recipient_address_list": {
            "help": "Set the recipient email address list",
            "loption": "recipient-address-list",
            "optional": 0,
            "soption": None
        },
        "sender_address": {
            "help": "Set the sender email address",
            "loption": "sender-address",
            "optional": 0,
            "soption": None
        },
        "domain_name": {
            "help": "Set the domain name",
            "loption": "domain-name",
            "optional": 0,
            "soption": None
        },
        "relay_ip_address": {
            "help": "Set the relay IP address",
            "loption": "relay-ip-address",
            "optional": 0,
            "soption": None
        },
        "test_email": {
            "help": "Set the subject and body for sending test mail",
            "loption": "test-email",
            "optional": 0,
            "soption": None
        },
    }
})

brcd_utils_cli_dict.update({
    "switch-status-policy-report": {
    }
})

brcd_utils_cli_dict.update({
    "monitoring-system-matrix": {
    }
})

brcd_utils_cli_dict.update({
    "paused-cfg": {
        "group_type": {
            "help": "Set the group type",
            "loption": "group-type",
            "optional": 1,
            "soption": None
        },
        "members": {
            "help": "Set the members",
            "loption": "members",
            "optional": 1,
            "soption": None
        },
    }
})

brcd_utils_cli_dict.update({
    "system-resources": {
    }
})

brcd_utils_cli_dict.update({
    "dashboard-misc": {
        "clear_data": {
            "help": "Clears DB data if this flag is set",
            "loption": "clear-data",
            "optional": 1,
            "soption": None
        },
    }
})

brcd_utils_cli_dict.update({
    "dashboard-rule": {
    }
})


brcd_utils_cli_dict.update({
    "system": {
        "description": {
            "help": "System description[OPTIONAL]",
            "loption": "sys-description",
            "optional": 1,
            "soption": None
        },
        "location": {
            "help": "System location[OPTIONAL]",
            "loption": "sys-location",
            "optional": 1,
            "soption": None
        },
        "contact": {
            "help": "System contact[OPTIONAL]",
            "loption": "sys-contact",
            "optional": 1,
            "soption": None
        },
        "informs_enabled": {
            "help": "Informs enabled <true|false>[OPTIONAL]",
            "loption": "informs-enabled",
            "optional": 1,
            "soption": None
        },
        "encryption_enabled": {
            "help": "Encryption enabled <true|false>[OPTIONAL]",
            "loption": "encryption-enabled",
            "optional": 1,
            "soption": None
        },
        "audit_interval": {
            "help": "Audit interval[OPTIONAL]",
            "loption": "audit-interval",
            "optional": 1,
            "soption": None
        },
        "default_config_default_control": {
            "help": "Defaulting the SNMP configuration values[OPTIONAL]",
            "loption": "default-config",
            "optional": 1,
            "soption": None
        },
        "security_get_level": {
            "help": "SNMP GET security level[OPTIONAL]",
            "loption": "sec-get-level",
            "optional": 1,
            "soption": None
        },
        "security_set_level": {
            "help": "SNMP SET security level[OPTIONAL]",
            "loption": "sec-set-level",
            "optional": 1,
            "soption": None
        },
        "snmpv1_enabled": {
            "help": "SNMPv1 is enabled <true|false>[OPTIONAL]",
            "loption": "snmpv1-enabled",
            "optional": 1,
            "soption": None
        },
    }
})


brcd_utils_cli_dict.update({
    "mib-capability": {
        "mib_name": {
            "help": "MIB name",
            "loption": "mib-name",
            "optional": 0,
            "soption": None
        },
        "is_mib_enabled_state": {
            "help": "Indicates the MIB state is enabled <true/false>",
            "loption": "mib-state",
            "optional": 0,
            "soption": None
        },
    }
})


brcd_utils_cli_dict.update({
    "trap-capability": {
        "trap_name": {
            "help": "Trap name",
            "loption": "trap-name",
            "optional": 0,
            "soption": None
        },
        "is_trap_enabled_state": {
            "help": "Indicates the Trap state is enabled <true/false>",
            "loption": "trap-state",
            "optional": 1,
            "soption": None
        },
        "severity": {
            "help": "Trap severity level[OPTIONAL]",
            "loption": "severity",
            "optional": 1,
            "soption": None
        },
    }
})


brcd_utils_cli_dict.update({
    "v1-account": {
        "index": {
            "help": "Index of SNMPv1 account",
            "loption": "index",
            "optional": 0,
            "soption": None
        },
        "community_name": {
            "help": "The community name",
            "loption": "community-name",
            "optional": 0,
            "soption": None
        },
    }
})


brcd_utils_cli_dict.update({
    "v1-trap": {
        "index": {
            "help": "Index of SNMPv1 host recipient",
            "loption": "index",
            "optional": 0,
            "soption": None
        },
        "host": {
            "help": "IP address of trap recipient",
            "loption": "host",
            "optional": 0,
            "soption": None
        },
        "trap_severity_level": {
            "help": "Severity level of trap recipient[OPTIONAL]",
            "loption": "severity-level",
            "optional": 1,
            "soption": None
        },
        "port_number": {
            "help": "The port number of trap recipient[OPTIONAL]",
            "loption": "port-number",
            "optional": 1,
            "soption": None
        },
    }
})


brcd_utils_cli_dict.update({
    "v3-account": {
        "index": {
            "help": "Index of SNMPv3 account",
            "loption": "index",
            "optional": 0,
            "soption": None
        },
        "user_name": {
            "help": "The snmpv3 user name",
            "loption": "user-name",
            "optional": 0,
            "soption": None
        },
        "authentication_protocol": {
            "help": "The snmpv3 user authentication protocol[OPTIONAL]",
            "loption": "authentication-protocol",
            "optional": 1,
            "soption": None
        },
        "privacy_protocol": {
            "help": "The snmpv3 user privacy protocol[OPTIONAL]",
            "loption": "privacy-protocol",
            "optional": 1,
            "soption": None
        },
        "authentication_password": {
            "help": "The snmpv3 user authentication password[OPTIONAL]",
            "loption": "authentication-password",
            "optional": 1,
            "soption": None
        },
        "privacy_password": {
            "help": "The snmpv3 user privacy password[OPTIONAL]",
            "loption": "privacy-password",
            "optional": 1,
            "soption": None
        },
        "manager_engine_id": {
            "help": "The SNMP manager engine id[OPTIONAL]",
            "loption": "manager-engine-id",
            "optional": 1,
            "soption": None
        },
    }
})


brcd_utils_cli_dict.update({
    "v3-trap": {
        "trap_index": {
            "help": "Index of SNMPv3 host recipient",
            "loption": "trap-index",
            "optional": 0,
            "soption": None
        },
        "usm_index": {
            "help": "Index of SNMPv3 account",
            "loption": "usm-index",
            "optional": 0,
            "soption": None
        },
        "host": {
            "help": "IP address of trap recipient",
            "loption": "host",
            "optional": 0,
            "soption": None
        },
        "trap_severity_level": {
            "help": "Severity level of trap recipient[OPTIONAL]",
            "loption": "severity-level",
            "optional": 1,
            "soption": None
        },
        "port_number": {
            "help": "The port number of trap recipient[OPTIONAL]",
            "loption": "port-number",
            "optional": 1,
            "soption": None
        },
        "informs_enabled": {
            "help": "Informs enabled for SNMPV3 notification[OPTIONAL]",
            "loption": "informs-enabled",
            "optional": 1,
            "soption": None
        },
    }
})


brcd_utils_cli_dict.update({
    "access-control": {
        "index": {
            "help": "Index of snmp access control list",
            "loption": "index",
            "optional": 0,
            "soption": None
        },
        "host": {
            "help": "The subnet area of the access host",
            "loption": "host",
            "optional": 0,
            "soption": None
        },
        "access_level": {
            "help": "The access level of the access control entry" +
                    " < ro/rw >[OPTIONAL]",
            "loption": "access-level",
            "optional": 1,
            "soption": None
        },
    }
})


brcd_utils_cli_dict.update({
    "error-log": {
        "message_id": {
            "help": "Filter and display error logs that match the \
message ID passed",
            "loption": "message-id",
            "optional": 1,
            "soption": "m"
        },
        "severity_level": {
            "help": "Filter and display error logs that match the \
severity level passed",
            "loption": "severity-level",
            "optional": 1,
            "soption": "l"
        },
        "slot_id": {
            "help": "Filter and display error logs that match the \
slot id passed",
            "loption": "slot-id",
            "optional": 1,
            "soption": None
        },
    }
})


brcd_utils_cli_dict.update({
    "supportftp": {
        "host": {
            "help": "\tConfigure IP address or DNS name of server",
            "loption": "host",
            "optional": 1,
            "soption": None
        },
        "user_name": {
            "help": "\tConfigure user name of account in server",
            "loption": "user-name",
            "optional": 0,
            "soption": "u"
        },
        "password": {
            "help": "\tConfigure password of account in server in Base64",
            "loption": "login-password",
            "optional": 0,
            "soption": "w"
        },
        "remote_directory": {
            "help": "\tConfigure directory path in server",
            "loption": "remote-directory",
            "optional": 0,
            "soption": "d"
        },
        "auto_enabled": {
            "help": "\tSet to true/false to enable/disable auto supportftp",
            "loption": "auto-enabled",
            "optional": 1,
            "soption": "a"
        },
        "protocol": {
            "help": "\tConfigure protocol(ftp/scp/sftp) used to transfer data",
            "loption": "protocol",
            "optional": 0,
            "soption": "p"
        },
        "port": {
            "help": "\tConfigure port(scp/sftp) used to transfer data",
            "loption": "port",
            "optional": 1,
            "soption": "o"
        },
        "connectivity_check_interval": {
            "help": "\tConfigure interval to check server connectivity",
            "loption": "check-interval",
            "optional": 1,
            "soption": "c"
        },
     }
})

brcd_utils_cli_dict.update({
    "supportlink_profile": {
        "server": {
            "help": "\tConfigure IP address or DNS name of server",
            "loption": "server",
            "optional": 1,
            "soption": None
        },
        "port": {
            "help": "\tConfigure HTTPS port of server",
            "loption": "port",
            "optional": 1,
            "soption": "p"
        },
        "user_name": {
            "help": "\tConfigure user name of account in server",
            "loption": "user-name",
            "optional": 1,
            "soption": "u"
        },
        "start_date": {
            "help": "\tConfigure start date",
            "loption": "start-date",
            "optional": 1,
            "soption": "d"
        },
        "start_time": {
            "help": "\tConfigure start time",
            "loption": "start-time",
            "optional": 1,
            "soption": "t"
        },
        "end_time_period": {
            "help": "\tConfigure end time period",
            "loption": "end-time-period",
            "optional": 1,
            "soption": "o"
        },
        "retry_time": {
            "help": "\tConfigure retry time",
            "loption": "retry-time",
            "optional": 1,
            "soption": "r"
        },
        "period": {
            "help": "\tConfigure frequency/period",
            "loption": "period",
            "optional": 1,
            "soption": "i"
        },
        "collection_time": {
            "help": "\tConfigure collection time",
            "loption": "collection-time",
            "optional": 1,
            "soption": "c"
        },
        "group_tag": {
            "help": "\tConfigure group tag",
            "loption": "group-tag",
            "optional": 1,
            "soption": "g"
        },
        "proxy_server": {
            "help": "\tConfigure proxy server",
            "loption": "proxy-server",
            "optional": 1,
            "soption": "v"
        },
        "proxy_port": {
            "help": "\tConfigure proxy port",
            "loption": "proxy-port",
            "optional": 1,
            "soption": "x"
        },
        "proxy_user": {
            "help": "\tConfigure proxy user",
            "loption": "proxy-user",
            "optional": 1,
            "soption": "y"
        },
        "proxy_password": {
            "help": "\tConfigure proxy password",
            "loption": "proxy-password",
            "optional": 1,
            "soption": "w"
        },
        "proxy_protocol": {
            "help": "\tConfigure proxy protocol",
            "loption": "proxy-protocol",
            "optional": 1,
            "soption": "l"
        },
        "supportlink_enabled": {
            "help": "\tConfigure supportlink feature",
            "loption": "supportlink-enabled",
            "optional": 1,
            "soption": "e"
        },
     }
})

brcd_utils_cli_dict.update({
    "fabric-traffic-controller": {
        "n_port_id": {
            "help": "N_Port ID. [OPTIONAL]",
            "loption": "n-port-id",
            "optional": 1,
            "soption": None
        }
    }
})
brcd_utils_cli_dict.update({
    "sensor": {
        "id": {
            "help": "The sensor id [OPTIONAL]",
            "loption": "id",
            "optional": 0,
            "soption": None,
            "value": 0
        },
    }
})
brcd_utils_cli_dict.update({
    "wwn": {
        "unit_number": {
            "help": "set \"unit-number\"",
            "loption": "unit-number",
            "optional": 0,
            "soption": None,
            "value": 0
        },
    }
})
brcd_utils_cli_dict.update({
    "logical_e_port": {
        "port_index": {
            "help": "set \"port-index\"",
            "loption": "port-index",
            "optional": 0,
            "soption": None,
            "value": 0
            }
    }
})
pseudorestobjectclidict = dict()
pseudorestobjectclidict.update({
    "auth-token-manager":
    {
        "config": {
            "help": "The Configuration for Auth Token Manager to be used.",
            "loption": "config",
            "optional": 1,
            "soption": "c",
            "noarg": True,
            "valtype": pyfos_type.pyfos_type.type_str,
            "resttype": rest_util.REST_ATTRIBUTE_CONFIG
        },
        "migrate-config": {
            "help": "Configuration for Manager to migrate the AuthTokens.",
            "loption": "migrate-config",
            "optional": 1,
            "noarg": True,
            "soption": "m",
            "valtype": pyfos_type.pyfos_type.type_str,
            "resttype": rest_util.REST_ATTRIBUTE_CONFIG

        },
        "switch-user": {
            "help": "The switch user account associated with Auth Token.",
            "loption": "switch-user",
            "optional": 1,
            "soption": None,
            "noarg": True,
            "valtype": pyfos_type.pyfos_type.type_str,
            "resttype": rest_util.REST_ATTRIBUTE_CONFIG
        },
        "switch-ip-address": {
            "help": "The switch IP address associated with Auth Token.",
            "loption": "switch-ip-address",
            "optional": 1,
            "soption": None,
            "noarg": True,
            "valtype": pyfos_type.pyfos_type.type_str,
            "resttype": rest_util.REST_ATTRIBUTE_CONFIG
        },
        "switch-auth-token": {
            "help": "The switch Auth Token in base64 format.",
            "loption": "switch-auth-token",
            "optional": 1,
            "soption": None,
            "noarg": True,
            "valtype": pyfos_type.pyfos_type.type_str,
            "resttype": rest_util.REST_ATTRIBUTE_CONFIG
        },
    }
})
brcd_utils_cli_dict.update({
    "device": {
        "n_port_id": {
            "help": "The Fibre Channel ID (FCID) of the device",
            "loption": "n-port-id",
            "optional": 0,
            "soption": None
        },
        "n_port_wwn": {
            "help": "The world wide Port name (PWWN) of the device",
            "loption": "n-port-wwn",
            "optional": 0,
            "soption": None
        },
        "payload": {
            "help": "opaque payload and response buffer in base64 format",
            "loption": "payload",
            "optional": 0,
            "soption": None
        },
        "version": {
            "help": "Version Identifier for the remote device",
            "loption": "version",
            "optional": 1,
            "soption": None
        }
    }
})

brcd_utils_cli_dict.update({
    "fabric-operation-parameters": {
        "build_fabric": {
            "help": "Triggers build fabric operation",
            "loption": "build-fabric",
            "optional": 0,
            "soption": "b"
        }
    }
})
brcd_utils_cli_dict.update({
    "license-parameters": {
        "password": {
            "help": "The password for the remote server.The password must be \
base64 encoded.",
            "loption": "license-password",
            "optional": 1,
            "soption": None
        },
        "remote-directory": {
            "help": "The xml file path of the server from which the license \
file to be transferred.",
            "loption": "remote-directory",
            "optional": 1,
            "soption": None
        },
        "name": {
            "help": "The license key or serial number.",
            "loption": "name",
            "optional": 1,
            "soption": None
        },
        "protocol": {
            "help": "The transport protocol.",
            "loption": "protocol",
            "optional": 1,
            "soption": None
        },
        "host": {
            "help": "The ip address or host name of the remote server.",
            "loption": "host",
            "optional": 1,
            "soption": None
        },
        "user-name": {
            "help": "The user name of the remote server.",
            "loption": "user-name",
            "optional": 1,
            "soption": None
        },
        "action": {
            "help": "The Action against specified license. \
Input values are \"install | remove\".",
            "loption": "action",
            "optional": 1,
            "soption": None
        },
        "port": {
            "help": "User defined port number for scp and sftp \
protocols [OPTIONAL].",
            "loption": "port",
            "optional": 1,
            "soption": None
        },
        "license-payload": {
            "help": "To send entire license certificate content as a input. \
The license certificate payload must be base64 encoded value.",
            "loption": "license-payload",
            "optional": 1,
            "soption": None
        },
    }
})

brcd_utils_cli_dict.update({
    "license": {
        "name": {
            "help": "Set license key or serial number to get specific \
license details.",
            "loption": "name",
            "optional": 1,
            "soption": None
        },
    }
})


brcd_utils_cli_dict.update({
    "routing-configuration": {
        "maximum_lsan_count": {
            "help": "set max lsan count of router switch",
            "loption": "maximum-lsan-count",
            "optional": 1,
            "soption": None
        },
        "backbone_fabric_id": {
            "help": "set backbone fabric id of the router switch",
            "loption": "backbone-fabric-id",
            "optional": 1,
            "soption": None
        },
        "shortest_ifl": {
            "help": "set shortest IFL mode",
            "loption": "shortest-ifl",
            "optional": 1,
            "soption": None
        },
        "lsan_enforce_tags_tag": {
            "help": "set lsan enforce tag",
            "loption": "lsan-enforce-tag",
            "optional": 1,
            "soption": None
        },
        "lsan_speed_tag": {
            "help": "set lsan speed tag",
            "loption": "lsan-speed-tag",
            "optional": 1,
            "soption": None
        },
    }
})

brcd_utils_cli_dict.update({
    "edge-fabric-alias": {
        "edge_fabric_id": {
            "help": "set edge fabric ID",
            "loption": "edge-fabric-id",
            "optional": 1,
            "soption": None
        },
        "alias_name": {
            "help": "set alias name",
            "loption": "alias-name",
            "optional": 1,
            "soption": None
        },
    }
})

brcd_utils_cli_dict.update({
    "slot-test": {
                "slot_id": {
                    "help": "Set the slot number between which the" +
                    " test needs to be run.\n\t\t\t\t\t\t  255 Indicates" +
                    " all the slots in the chassis.",
                    "loption": "slot-id",
                    "optional": 1,
                    "soption": None
                },
        }
})

brcd_utils_cli_dict.update({
    "lsan-zone": {
    }
})

brcd_utils_cli_dict.update({
    "lsan-device": {
    }
})

brcd_utils_cli_dict.update({
    "zone-operation-parameters": {
        "zone_object": {
            "help": "Name of object to be expunged",
            "loption": "zone-object",
            "optional": 0,
            "soption": None
        }
    }
})

brcd_utils_cli_dict.update({
    "chassis-config-settings": {
        "ezserver_enabled": {
            "help": "set \"ezserver-enabled\" " +
            "<0/False/false|1/True/true>",
            "loption": "ezserver-enabled",
            "optional": 0,
            "soption": None,
            "value": 0
        },
        "firmware_synchronization_enabled": {
            "help": "set \"firmware-synchronization-enabled\" " +
            "<0/False/false|1/True/true>",
            "loption": "firmware-synchronization-enabled",
            "optional": 0,
            "soption": None,
            "value": 0
        },
        "http_session_ttl": {
            "help": "set \"http-session-ttl\" <60-432000>",
            "loption": "http-session-ttl",
            "optional": 0,
            "soption": None,
            "value": 0
        }
    }
})


def pseudorestcli(dictkey):
    if dictkey in pseudorestobjectclidict.keys():
        return dict({dictkey: pseudorestobjectclidict[dictkey]})
    return None
