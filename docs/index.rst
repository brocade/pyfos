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


*PyFOS FC Support Modules*

.. toctree::
   :maxdepth: 2

   pyfos_brocade_access_gateway
   pyfos_brocade_fabric
   pyfos_brocade_fibrechannel
   pyfos_brocade_fibrechannel_diagnostics
   pyfos_brocade_fibrechannel_switch
   pyfos_brocade_zone
   pyfos_brocade_fdmi
   pyfos_brocade_fibrechannel_logical_switch
   pyfos_brocade_name_server

*PyFOS Extension Support Modules*

.. toctree::
   :maxdepth: 2

   pyfos_brocade_gigabitethernet
   pyfos_brocade_extension_ip_interface
   pyfos_brocade_extension_ip_route
   pyfos_brocade_extension_ipsec_policy
   pyfos_brocade_extension_tunnel

*PyFOS utils Modules*

.. toctree::
   :maxdepth: 2

   bulk_zoning
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
   extensionShell
   extension_tunnel_create
   extension_tunnel_modify
   extension_tunnel_delete
   extension_tunnel_show
   extension_tunnel_statistics_show
   extension_ipsec_policy_create
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
   zoning_pzone_create_add
   zoning_pzone_delete
   zoning_pzone_remove
   zoning_zone_create_add
   zoning_zone_delete
   zoning_zone_remove
   zone_allow_pair
   zone_allow_pair_to_peer

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

Indices and Tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
