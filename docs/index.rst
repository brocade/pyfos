.. pyfos documentation master file, created by
   sphinx-quickstart on Tue Jan 10 15:21:41 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to PyFOS' Documentation!
=================================

PyFOS contains open source Python modules to facilitate mangement of FOS switches.

*PyFOS Infrastructure Modules*

.. toctree::
   :maxdepth: 2

   pyfos_auth
   pyfos_rest_util
   pyfos_util

*PyFOS Manager Modules*

.. toctree::
   :maxdepth: 2

   pyfos_config_manager
   pyfos_class_manager
   pyfos_rule_manager

*PyFOS FC Support Modules*

.. toctree::
   :maxdepth: 2

   pyfos_brocade_access_gateway
   pyfos_brocade_fabric
   pyfos_brocade_fibrechannel_configuration
   pyfos_brocade_fibrechannel_diagnostics
   pyfos_brocade_fibrechannel_switch
   pyfos_brocade_fibrechannel_trunk
   pyfos_brocade_zone
   pyfos_brocade_fdmi
   pyfos_brocade_fibrechannel_logical_switch
   pyfos_brocade_interface
   pyfos_brocade_license
   pyfos_brocade_name_server
   pyfos_brocade_security
   pyfos_brocade_chassis
   pyfos_brocade_media
   pyfos_brocade_fru
   pyfos_brocade_logging
   pyfos_brocade_maps
   pyfos_brocade_time
   pyfos_brocade_license
   pyfos_brocade_snmp
   pyfos_brocade_module_version

*PyFOS Operation Support Modules*

.. toctree::
   :maxdepth: 2

   pyfos_brocade_operation_firmwarecleaninstall
   pyfos_brocade_operation_firmwaredownload
   pyfos_brocade_operation_license 
   pyfos_brocade_operation_supportsave
   pyfos_brocade_operation_show_status

*PyFOS Logging utils Modules*

.. toctree::
   :maxdepth: 2

   log_quiet_control_show
   log_quiet_control_modify
   log_setting_keep_alive_period_show
   log_setting_keep_alive_period_set
   raslog_show
   raslog_message_enabled_set
   raslog_module_show
   raslog_module_set
   raslog_current_severity_set
   raslog_syslog_enabled_set
   syslog_show
   syslog_modify
   syslog_create
   syslog_delete
   syslog_facility_modify
   syslog_facility_show
   audit_show
   audit_modify

*PyFOS Configuration utils Modules*

.. toctree::
   :maxdepth: 2

   switch_configuration_show
   switch_configuration_modify
   f_port_login_settings_show
   f_port_login_settings_modify
   dns_config_show
   dns_config_modify
   switch_ip_config_show
   switch_ip_config_modify
   configure_fabric_show
   configure_fabric_modify

*PyFOS Extension Support Modules*

.. toctree::
   :maxdepth: 2

   pyfos_brocade_extension_ip_interface
   pyfos_brocade_extension_ip_route
   pyfos_brocade_extension_ipsec_policy
   pyfos_brocade_extension_tunnel

*PyFOS utils Modules*

.. toctree::
   :maxdepth: 2

   bulk_zoning
   configure_port_show
   configure_port_name_set
   configure_dport_mode_modify
   configure_zone_show
   device_find
   extension_ip_interface_create
   extension_ip_interface_modify
   extension_ip_interface_delete
   extension_ip_interface_show
   extension_ip_route_create
   extension_ip_route_modify
   extension_ip_route_delete
   extension_circuit_create
   extension_circuit_delete
   extension_circuit_modify
   extension_circuit_show
   extension_circuit_statistics_show
   extension_circuit_statistics_pktloss_show
   extensionShell
   extension_tunnel_create
   extension_tunnel_modify
   extension_tunnel_delete
   extension_tunnel_show
   extension_tunnel_statistics_show
   extension_ipsec_policy_create
   extension_ipsec_policy_modify
   extension_ipsec_policy_delete
   extension_ipsec_policy_show
   fabric_show
   fdmi_show
   gigabitethernet_enabled_state_set
   gigabitethernet_show
   gigabitethernet_speed_set
   gigabitethernet_statistics_show
   name_server_show
   port_avail_show.rst
   port_dport_run.rst
   port_name_set.rst
   port_show.rst
   port_state_set.rst
   port_mirror_state_set.rst
   port_credit_recovery_state_set.rst
   port_fault_delay_state_set.rst
   port_isl_mode_state_set.rst
   port_los_tov_state_set.rst
   port_npiv_state_set.rst
   port_sim_state_set.rst
   port_trunk_state_set.rst
   port_resilience_set.rst
   port_stats_show.rst
   switch_ag_mode_set.rst
   switch_name_set
   switch_show
   switch_config_apply
   switch_config_diff
   switch_config_dump
   zoning_alias_create_add
   zoning_alias_delete
   zoning_alias_remove
   zoning_cfg_abort
   zoning_cfg_clear
   zoning_cfg_create_add
   zoning_cfg_delete
   zoning_cfg_disable
   zoning_cfg_enable
   zoning_cfg_remove
   zoning_cfg_save
   zoning_cfg_show
   zoning_def_zone
   zoning_hanging_zone_find
   zoning_pzone_create_add
   zoning_pzone_delete
   zoning_pzone_remove
   zoning_zone_create_add
   zoning_zone_delete
   zoning_zone_remove
   zone_allow_pair
   zone_allow_pair_to_peer
   license_show

*PyFOS Access Gateway Mode utils Modules*

.. toctree::
   :maxdepth: 2

   fport_list_show
   nport_map_add
   nport_map_del
   nport_map_modify
   nport_map_show
   nport_settings_modify
   nport_settings_show
   policy_modify
   policy_show
   port_group_fport_add
   port_group_create_add
   port_group_del
   port_group_mode
   port_group_remove
   port_group_show

*PyFOS Logical Switch utils Modules*

.. toctree::
   :maxdepth: 2

   logical_switch_create
   logical_switch_delete
   logical_switch_modify
   logical_switch_show

*PyFOS System Security utils modules:*

.. toctree::
   :maxdepth: 2

   sshutil_key_show
   sshutil_key_create
   sshutil_modify
   sshutil_key_delete
   sshutil_public_key_show
   sshutil_public_key_delete
   sshutil_public_key_modify
   seccertmgmt_show
   seccertmgmt_create
   seccertmgmt_action
   seccertmgmt_delete
   passwd_modify
   auth_spec_show
   auth_spec_set
   radius_server_show
   radius_server_create
   radius_server_set
   radius_server_delete
   tacacs_server_show
   tacacs_server_create
   tacacs_server_set
   tacacs_server_delete
   ldap_server_show
   ldap_server_create
   ldap_server_set
   ldap_server_delete
   ldap_role_map_show
   ldap_role_map_create
   ldap_role_map_set
   ldap_role_map_delete
   password_cfg_show
   password_cfg_set
   user_specific_password_cfg_show
   user_specific_password_cfg_create
   user_specific_password_cfg_set
   user_specific_password_cfg_delete
   time_zone_show
   time_zone_set
   time_zone_name_set
   clock_server_show
   clock_server_set
   ipfilter_policy_show
   ipfilter_policy_create
   ipfilter_policy_clone_set
   ipfilter_policy_activate_set
   ipfilter_policy_delete
   ipfilter_rule_show
   ipfilter_rule_create
   ipfilter_rule_delete
   seccryptocfg_show
   seccryptocfgtemplate_show
   seccryptocfg_export
   seccryptocfg_import
   seccryptocfg_apply_set
   seccryptocfg_verify
   seccryptocfg_delete
   user_config_show
   user_config_create
   user_config_set
   user_config_delete

*PyFOS Chassis utils modules:*

.. toctree::
   :maxdepth: 2

   ha_status_show
   chassis_show
   chassis_name_set
   chassis_vf_enabled_set

*PyFOS Media utils modules:*

.. toctree::
   :maxdepth: 2

   media_rdp_show

*PyFOS Fru utils modules:*

.. toctree::
   :maxdepth: 2

   fan_show
   powersupply_show
   blade_show
   blade_extncfg_set

*PyFOS Trunk utils Modules:*

.. toctree::
   :maxdepth: 2

   port_trunk_area_create_add
   port_trunk_area_delete
   port_trunk_area_show_all
   port_trunk_area_show
   trunk_perf_show_all
   trunk_perf_show
   trunk_show_all
   trunk_show

*PyFOS MAPS utils modules:*

.. toctree::
   :maxdepth: 2

   maps_policy_create
   maps_policy_patch
   maps_policy_delete
   maps_policy_show
   maps_policy_enable
   maps_group_create
   maps_group_delete
   maps_group_show
   maps_group_patch
   maps_rule_create
   maps_rule_delete
   maps_rule_update
   maps_rule_show
   monitoring_system_matrix
   maps_config_patch
   maps_config_show
   maps_paused_cfg_post
   maps_paused_cfg_delete
   maps_paused_cfg_show
   maps_system_resources_show
   maps_dashboard_misc_show
   maps_dashboard_misc_patch
   maps_dashboard_rule_show
   maps_get_ssp_report


 
*PyFOS Operation utils Modules:*

.. toctree::
   :maxdepth: 2

   firmwarecleaninstall
   firmwaredownload
   license_install
   license_remove
   supportsave

*PyFOS Snmp utils Modules*

.. toctree::
   :maxdepth: 2

   snmp_system_show
   snmp_system_modify
   snmp_mib_capability_show
   snmp_mib_capability_modify
   snmp_trap_capability_show
   snmp_trap_capability_modify
   snmp_v1_account_show
   snmp_v1_account_modify
   snmp_v1_trap_show
   snmp_v1_trap_modify
   snmp_v3_account_show
   snmp_v3_account_modify
   snmp_v3_trap_show
   snmp_v3_trap_modify
   snmp_access_control_show
   snmp_access_control_modify

*PyFOS Version Module:*

.. toctree::
   :maxdepth: 2

   module_version_show

Indices and tables

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
