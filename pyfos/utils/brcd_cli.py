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
    }
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

# Used to document the CLI options
brcd_utils_cli_dict = dict()

"""
Utils Dictionary END
"""


def getcustomcli(name):
    global brcd_utils_cli_dict
    if name in brcd_utils_cli_dict.keys():
        return (brcd_utils_cli_dict[name])
    return None


"""
CLI Dictionary
"""
brcd_utils_cli_dict.update({
    "effective-configuration": {
        "cfg_name": {
            "help": "set \"cfg-name\"",
            "loption": "name",
            "optional": 0,
            "soption": None,
            "value": 0
        }
    }
})

brcd_utils_cli_dict.update({
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
        "port_group_n_ports_n_port": {
            "help": "N-port members of the port group",
            "loption": "n-port",
            "optional": 0,
            "soption": None
        },
        "port_group_f_ports_f_port": {
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
        "configured_f_port_list_f_port": {
            "help": "List of mapped F-ports",
            "loption": "config-f-ports",
            "optional": 1,
            "soption": None
        },
        "static_f_port_list_f_port": {
            "help": "List of statically mapped F-ports",
            "loption": "static-f-ports",
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
