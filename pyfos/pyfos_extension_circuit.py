# Copyright 2017 Brocade Communications Systems, Inc.  All rights reserved.
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

:mod:`pyfos_extension_circuit` - PyFOS module to provide rest support for Extension Circuit objects.
*********************************************************************************************************
The :mod:`pyfos_extension_circuit` provides a REST support for Extension  Circuit objects.
"""
import pyfos.pyfos_rest_util as pyfos_rest_util
from pyfos.pyfos_type import pyfos_type

class extension_circuit(pyfos_rest_util.rest_object):
        """Class of extension_circuit 

        Important class members:
            
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | Attribute name                | Description                   |Frequently used functions                        |
            +===============================+===============================+=================================================+
            | name                          | The slot/port name of VE port |:func:`peek_name`                                |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | name                          | The slot/port name of VE port |:func:`set_name`                                 |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | circuit-id                    | Circuit ID                    |:func:`peek_circuit_id`                          |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | circuit-id                    | Circuit ID                    |:func:`set_circuit_id`                           |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | local-ip-address              | Ciruit local IP address       |:func:`peek_local_ip_address`                    |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | local-ip-address              | Ciruit local IP address       |:func:`set_local_ip_address`                     |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | remote-ip-address             | Ciruit remote IP address      |:func:`peek_remote_ip_address`                   |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | remote-ip-address             | Ciruit remote IP address      |:func:`set_remote_ip_address`                    |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | local-ha-ip-address           | Ciruit local HA IP address    |:func:`peek_local_ha_ip_address`                 |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | local-ha-ip-address           | Ciruit local HA IP address    |:func:`set_local_ha_ip_address`                  |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | remote-ha-ip-address          | Ciruit remote HA IP address   |:func:`peek_remote_ha_ip_address`                |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | remote-ha-ip-address          | Ciruit remote HA IP address   |:func:`set_remote_ha_ip_address`                 |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | metric                        | Circuit metric value          |:func:`peek_metric`                              |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | metric                        | Circuit metric value          |:func:`set_metric`                               |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | admin-enabled                 | The admin enabled tnl state   |:func:`peek_admin_enabled`                       |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | admin-enabled                 | The admin enabled tnl state   |:func:`set_admin_enabled`                        |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | circuit-status                | The Circuit status            |:func:`peek_circuit_status`                      |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | path-mtu-discovered           | Path MTU discovered           |:func:`peek_path_mtu_discovered`                 |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | failover-group-id             | Circuit Failover group ID     |:func:`peek_failover_group_id`                   |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | failover-group-id             | Circuit Failover group ID     |:func:`set_failover_group_id`                    |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | minimum-communication-rate    | Min Comm rate of circuit      |:func:`peek_minimum_communication_rate`          |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | minimum-communication-rate    | Min Comm rate of circuit      |:func:`set_minimum_communication_rate`           |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | maximum-communication-rate    | Max Comm rate of circuit      |:func:`peek_maximum_communication_rate`          |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | maximum-communication-rate    | Max Comm rate of circuit      |:func:`set_maximum_communication_rate`           |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | vlan-id                       | The Circuit vlan ID           |:func:`peek_vlan_id`                             |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | l2-cos                        | l2cos                         |:func:`peek_l2_cos`                              |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | l2-cos                        | l2cos                         |:func:`set_l2_cos`                               |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | priority-control              | control priority              |:func:`peek_l2_cos_priority_control`             |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | priority-control              | control priority              |:func:`set_l2_cos_priority_control`              |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | fc-priority-high              | FC QOS High                   |:func:`peek_l2_cos_fc_priority_high`             |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | fc-priority-high              | FC QOS High                   |:func:`set_l2_cos_fc_priority_high`              |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | fc-priority-medium            | FC QOS High                   |:func:`peek_l2_cos_fc_priority_medium`           |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | fc-priority-medium            | FC QOS Medium                 |:func:`set_l2_cos_fc_priority_medium`            |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | fc-priority-low               | FC QOS Low                    |:func:`peek_l2_cos_fc_priority_low`              |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | fc-priority-low               | FC QOS Low                    |:func:`set_l2_cos_fc_priority_low`               |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | ip-priority-high              | IP QOS High                   |:func:`peek_l2_cos_ip_priority_high`             |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | ip-priority-high              | IP QOS High                   |:func:`set_l2_cos_ip_priority_high`              |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | ip-priority-medium            | IP QOS Medium                 |:func:`peek_l2_cos_ip_priority_medium`           |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | ip-priority-medium            | IP QOS Medium                 |:func:`set_l2_cos_ip_priority_medium`            |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | ip-priority-low               | IP QOS Low                    |:func:`peek_l2_cos_ip_priority_low`              | 
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | ip-priority-low               | IP QOS LOw                    |:func:`set_l2_cos_ip_priority_low`               |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | dscp                          | dscp                          |:func:`peek_dscp`                                |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | dscp                          | dscp                          |:func:`set_dscp`                                 |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | priority-control              | control priority              |:func:`peek_dscp_priority_control`               |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | priority-control              | control priority              |:func:`set_dscp_priority_control`                |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | fc-priority-high              | FC QOS High                   |:func:`peek_dscp_fc_priority_high`               |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | fc-priority-high              | FC QOS High                   |:func:`set_dscp_fc_priority_high`                |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | fc-priority-medium            | FC QOS High                   |:func:`peek_dscp_fc_priority_medium`             |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | fc-priority-medium            | FC QOS Medium                 |:func:`set_dscp_fc_priority_medium`              |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | fc-priority-low               | FC QOS Low                    |:func:`peek_dscp_fc_priority_low`                |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | fc-priority-low               | FC QOS Low                    |:func:`set_dscp_fc_priority_low`                 |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | ip-priority-high              | IP QOS High                   |:func:`peek_dscp_ip_priority_high`               |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | ip-priority-high              | IP QOS High                   |:func:`set_dscp_ip_priority_high`                |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | ip-priority-medium            | IP QOS Medium                 |:func:`peek_dscp_ip_priority_medium`             |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | ip-priority-medium            | IP QOS Medium                 |:func:`set_dscp_ip_priority_medium`              |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | ip-priority-low               | IP QOS Low                    |:func:`peek_dscp_ip_priority_low`                | 
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | ip-priority-low               | IP QOS LOw                    |:func:`set_dscp_ip_priority_low`                 |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | arl-algorithm-mode            | ARL alogirithm                |:func:`peek_arl_algorithm_mode`                  |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | arl-algorithm-mode            | ARL algorithm                 |:func:`set_arl_algorithm_mode`                   |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | keep-alive-timeout            | Keep alive timeout            |:func:`peek_keep_alive_timeout`                  |
            +-------------------------------+-------------------------------+-------------------------------------------------+

            
        *Object functions*

            .. function:: get()

                Fill the object with values for all the attributes. Once filled, the object can be printed
                using :func:`pyfos_utils.response_print`

                :param session: session handler returned by :func:`pyfos_auth.login`
                :rtype: dictionary of error or success response

        *Attribute functions*

            .. function:: peek_name()

                Reads name from the tunnel object.
                        
                :rtype: None on error and value on success

            .. function:: peek_circuit_id()

                Reads circuit ID from the circuit object.
                        
                :rtype: None on error and value on success

            .. function:: peek_local_ip_address()

                Reads local IP address from the circuit object.
                        
                :rtype: None on error and value on success

            .. function:: peek_remote_ip_address()

                Reads remote IP address from the circuit object.
                        
                :rtype: None on error and value on success

            .. function:: peek_local_ha_ip_address()

                Reads local HA IP address from the circuit object.
                        
                :rtype: None on error and value on success

            .. function:: peek_remote_ha_ip_address()

                Reads remote HA IP address from the circuit object.
                        
                :rtype: None on error and value on success

            .. function:: peek_metric()

                Reads metric from the circuit object.
                        
                :rtype: None on error and value on success

            .. function:: peek_admin_enabled()

                Reads admin enabled from the circuit object.
                        
                :rtype: None on error and value on success

            .. function:: peek_circuit_status()

                Reads ciruit status from the circuit object.
                        
                :rtype: None on error and value on success

            .. function:: peek_path_mtu_discovered()

                Reads path MTU discovered from the circuit object.
                        
                :rtype: None on error and value on success

            .. function:: peek_failover_group_id()

                Reads failover group id from the circuit object.
                        
                :rtype: None on error and value on success

            .. function:: peek_minimum_communication_rate()

                Reads minimum communication rate from the circuit object.
                        
                :rtype: None on error and value on success

            .. function:: peek_maximum_communication_rate()

                Reads maximum communication rate from the circuit object.
                        
                :rtype: None on error and value on success

            .. function:: peek_vlan_id()

                Reads vlan-id from the circuit object.
                        
                :rtype: None on error and value on success
                
            .. function:: peek_l2_cos()

                Reads l2 cos from the circuit object.
                        
                :rtype: None on error and value on success

            .. function:: peek_l2_cos_priority_control()

                Reads priority control l2 cos from the circuit object.
                        
                :rtype: None on error and value on success

            .. function:: peek_l2_cos_fc_priority_high()

                Reads FC high l2 cos from the circuit object.
                        
                :rtype: None on error and value on success

            .. function:: peek_l2_cos_fc_priority_medium()

                Reads FC medium l2 cos from the circuit object.
                        
                :rtype: None on error and value on success

            .. function:: peek_l2_cos_fc_priority_low()

                Reads FC low l2 cos from the circuit object.
                        
                :rtype: None on error and value on success

            .. function:: peek_l2_cos_ip_priority_high()

                Reads IP high l2 cos from the circuit object.
                        
                :rtype: None on error and value on success

            .. function:: peek_l2_cos_ip_priority_medium()

                Reads IP medium l2 cos from the circuit object.
                        
                :rtype: None on error and value on success

            .. function:: peek_l2_cos_ip_priority_low()

                Reads IP low l2 cos from the circuit object.
                        
                :rtype: None on error and value on success

            .. function:: peek_dscp()

                Reads dscp value from the circuit object.
                        
                :rtype: None on error and value on success

            .. function:: peek_dscp_priority_control()

                Reads priority control dscp value from the circuit object.
                        
                :rtype: None on error and value on success

            .. function:: peek_dscp_fc_priority_high()

                Reads FC high dscp value from the circuit object.
                        
                :rtype: None on error and value on success

            .. function:: peek_dscp_fc_priority_medium()

                Reads FC medium dscp value from the circuit object.
                        
                :rtype: None on error and value on success
                
            .. function:: peek_dscp_fc_priority_low()

                Reads FC low dscp value from the circuit object.
                        
                :rtype: None on error and value on success

            .. function:: peek_dscp_ip_priority_high()

                Reads IP High dscp value from the circuit object.
                        
                :rtype: None on error and value on success

            .. function:: peek_dscp_ip_priority_medium()

                Reads IP medium dscp value from the circuit object.
                        
                :rtype: None on error and value on success

            .. function:: peek_dscp_ip_priority_low()

                Reads IP low dscp value from the circuit object.
                        
                :rtype: None on error and value on success

            .. function:: peek_arl_algorithm_mode()

                Reads ARL algorithm from the circuit object.
                        
                :rtype: None on error and value on success

            .. function:: peek_keep_alive_timeout()

                Reads keep alive timeout from the circuit object.
                        
                :rtype: None on error and value on success
                
            .. function:: set_name(name)

                Set the name in the tunnel object.
                        
                :rtype: dictionary of error or success response and value with "name" as key

            .. function:: set_circuit_id(ciruitID)

                Set the circuit ID in the circuit object.
                        
                :rtype: dictionary of error or success response and value with "circuit-id" as key

            .. function:: set_local_ip_address(localIP)

                Set the local circuit IP address in the circuit object.
                        
                :rtype: dictionary of error or success response and value with "local-ip-address" as key

            .. function:: set_remote_ip_address(remoteIP)

                Set the Remote circuit IP address in the circuit object.
                        
                :rtype: dictionary of error or success response and value with "remote-ip-address" as key

            .. function:: set_local_ha_ip_address(localHAIP)

                Set the local HA circuit IP address in the circuit object.
                        
                :rtype: dictionary of error or success response and value with "local-ha-ip-address" as key

            .. function:: set_remote_ha_ip_address(remoteHAIP)

                Set the Remote HA circuit IP address in the circuit object.
                        
                :rtype: dictionary of error or success response and value with "remote-ha-ip-address" as key
                
            .. function:: set_metric(metric)

                Set the metric in the circuit object.
                        
                :rtype: dictionary of error or success response and value with "metric" as key

            .. function:: set_admin_enabled(adminState)

                Set the admin enabled in the circuit object.
                        
                :rtype: dictionary of error or success response and value with "admin-enabled" as key

            .. function:: set_failover_group_id(failoverGroup)

                Set the failover group id in the circuit object.
                        
                :rtype: dictionary of error or success response and value with "failover-group-id" as key

            .. function:: set_minimum_communication_rate(minCommRate)

                Set the min comm rate in the circuit object.
                        
                :rtype: dictionary of error or success response and value with "minimum-communication-rate" as key

            .. function:: set_maximum_communication_rate(maxCommRate)

                Set the max comm rate in the circuit object.
                        
                :rtype: dictionary of error or success response and value with "maximum-communication-rate" as key

            .. function:: set_l2_cos(l2cos)

                Set the l2 cos in the circuit object.
                        
                :rtype: dictionary of error or success response and value with "l2-cos" as key
                
            .. function:: set_l2_cos_priority_control(controll2Cos)

                Set the priority control l2 cos in the circuit object.
                        
                :rtype: dictionary of error or success response and value with "priority-control" as key

            .. function:: set_l2_cos_fc_priority_high(fcHighl2Cos)

                Set the FC high l2 cos in the circuit object.
                        
                :rtype: dictionary of error or success response and value with "fc-priority-high" as key

            .. function:: set_l2_cos_fc_priority_medium(fcMedl2Cos)

                Set the FC medium l2 cos in the circuit object.
                        
                :rtype: dictionary of error or success response and value with "fc-priority-medium" as key

            .. function:: set_l2_cos_fc_priority_low(fcLowl2Cos)

                Set the FC low l2 cos in the circuit object.
                        
                :rtype: dictionary of error or success response and value with "fc-priority-low" as key
                
            .. function:: set_l2_cos_ip_priority_high(ipHighl2Cos)

                Set the IP high l2 cos in the circuit object.
                        
                :rtype: dictionary of error or success response and value with "ip-priority-high" as key

            .. function:: set_l2_cos_ip_priority_medium(ipMediuml2Cos)

                Set the IP medium l2 cos in the circuit object.
                        
                :rtype: dictionary of error or success response and value with "ip-priority-medium" as key
                
            .. function:: set_l2_cos_ip_priority_low(iplowl2Cos)

                Set the IP low l2 cos in the circuit object.
                        
                :rtype: dictionary of error or success response and value with "ip-priority-low" as key
                
            .. function:: set_dscp(dscp)

                Set the dscp in the circuit object.
                        
                :rtype: dictionary of error or success response and value with "l2-cos" as key
                
            .. function:: set_dscp_priority_control(controldscp)

                Set the priority control l2 cos in the circuit object.
                        
                :rtype: dictionary of error or success response and value with "priority-control" as key

            .. function:: set_dscp_fc_priority_high(fcHighdscp)

                Set the FC high l2 cos in the circuit object.
                        
                :rtype: dictionary of error or success response and value with "fc-priority-high" as key

            .. function:: set_dscp_fc_priority_medium(fcMeddscp)

                Set the FC medium l2 cos in the circuit object.
                        
                :rtype: dictionary of error or success response and value with "fc-priority-medium" as key

            .. function:: set_dscp_fc_priority_low(fcLowdscp)

                Set the FC low l2 cos in the circuit object.
                        
                :rtype: dictionary of error or success response and value with "fc-priority-low" as key
                
            .. function:: set_dscp_ip_priority_high(ipHighdscp)

                Set the IP high l2 cos in the circuit object.
                        
                :rtype: dictionary of error or success response and value with "ip-priority-high" as key

            .. function:: set_dscp_ip_priority_medium(ipMediumdscp)

                Set the IP medium l2 cos in the circuit object.
                        
                :rtype: dictionary of error or success response and value with "ip-priority-medium" as key
                
            .. function:: set_dscp_ip_priority_low(iplowdscp)

                Set the IP low l2 cos in the circuit object.
                        
                :rtype: dictionary of error or success response and value with "ip-priority-low" as key
                
            .. function:: set_arl_algorithm_mode(arlAlgorithmMode)

                Set the ARL algorithm in the circuit object.
                        
                :rtype: dictionary of error or success response and value with "arl-algorithm-mode" as key
                
        """
        def __init__(self, dictvalues={}):
            super().__init__(pyfos_rest_util.rest_obj_type.circuit, "/rest/running/brocade-extension-tunnel/extension-circuit")
            self.add(pyfos_rest_util.rest_attribute("name", pyfos_type.type_str, None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
            self.add(pyfos_rest_util.rest_attribute("circuit-id", pyfos_type.type_str, None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
            self.add(pyfos_rest_util.rest_attribute("local-ip-address", pyfos_type.type_str, None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
            self.add(pyfos_rest_util.rest_attribute("remote-ip-address", pyfos_type.type_str, None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
            self.add(pyfos_rest_util.rest_attribute("metric", pyfos_type.type_str, None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
            self.add(pyfos_rest_util.rest_attribute("failover-group-id", pyfos_type.type_str, None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
            self.add(pyfos_rest_util.rest_attribute("admin-enabled", pyfos_type.type_str, None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
            self.add(pyfos_rest_util.rest_attribute("path-mtu-discovered", pyfos_type.type_str, None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
            self.add(pyfos_rest_util.rest_attribute("minimum-communication-rate", pyfos_type.type_str, None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
            self.add(pyfos_rest_util.rest_attribute("maximum-communication-rate", pyfos_type.type_str, None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
            self.add(pyfos_rest_util.rest_attribute("keep-alive-timeout", pyfos_type.type_str, None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
            self.add(pyfos_rest_util.rest_attribute("vlan-id", pyfos_type.type_str, None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

            self.add(pyfos_rest_util.rest_attribute("l2-cos", pyfos_type.type_na, dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
            self.add(pyfos_rest_util.rest_attribute("priority-control", pyfos_type.type_str, None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG), ["l2-cos"])
            self.add(pyfos_rest_util.rest_attribute("fc-priority-high", pyfos_type.type_str, None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG), ["l2-cos"])
            self.add(pyfos_rest_util.rest_attribute("fc-priority-medium", pyfos_type.type_str, None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG), ["l2-cos"])
            self.add(pyfos_rest_util.rest_attribute("fc-priority-low", pyfos_type.type_str, None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG), ["l2-cos"])
            self.add(pyfos_rest_util.rest_attribute("ip-priority-high", pyfos_type.type_str, None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG), ["l2-cos"])
            self.add(pyfos_rest_util.rest_attribute("ip-priority-medium", pyfos_type.type_str, None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG), ["l2-cos"])
            self.add(pyfos_rest_util.rest_attribute("ip-priority-low", pyfos_type.type_str, None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG), ["l2-cos"])

            self.add(pyfos_rest_util.rest_attribute("dscp", pyfos_type.type_na, dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
            self.add(pyfos_rest_util.rest_attribute("priority-control", pyfos_type.type_str, None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG), ["dscp"])
            self.add(pyfos_rest_util.rest_attribute("fc-priority-high", pyfos_type.type_str, None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG), ["dscp"])
            self.add(pyfos_rest_util.rest_attribute("fc-priority-medium", pyfos_type.type_str, None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG), ["dscp"])
            self.add(pyfos_rest_util.rest_attribute("fc-priority-low", pyfos_type.type_str, None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG), ["dscp"])
            self.add(pyfos_rest_util.rest_attribute("ip-priority-high", pyfos_type.type_str, None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG), ["dscp"])
            self.add(pyfos_rest_util.rest_attribute("ip-priority-medium", pyfos_type.type_str, None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG), ["dscp"])
            self.add(pyfos_rest_util.rest_attribute("ip-priority-low", pyfos_type.type_str, None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG), ["dscp"])
            
            
            self.add(pyfos_rest_util.rest_attribute("circuit-status", pyfos_type.type_str, None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
            self.add(pyfos_rest_util.rest_attribute("local-ha-ip-address", pyfos_type.type_str, None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
            self.add(pyfos_rest_util.rest_attribute("remote-ha-ip-address", pyfos_type.type_str, None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
            self.add(pyfos_rest_util.rest_attribute("arl-algorithm-mode", pyfos_type.type_str, None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
            
            self.load(dictvalues, 1)




class extension_circuit_statistics(pyfos_rest_util.rest_object):
        """Class of extension_circuit_statistics 

        Important class members:
            
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | Attribute name                | Description                   |Frequently used functions                        |
            +===============================+===============================+=================================================+
            | name                          | The slot/port name of GE port |:func:`peek_name`                                |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | name                          | The slot/port name of GE port |:func:`set_name`                                 |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | circuit-id                    | Circuit ID                    |:func:`peek_circuit_id`                          |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | circuit-id                    | Circuit ID                    |:func:`set_circuit_id`                           |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | flow-status                   | The IPv4/IPv6 address         |:func:`peek_flow_status`                         |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | operational-status            | Data-path Processor ID        |:func:`peek_operational_status`                  |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | connection-count              | The prefix length of IP       |:func:`peek_connection_count`                    |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | duration                      | The maximum transmission unit |:func:`peek_duration`                            |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | metric                        | Circuit metric value          |:func:`peek_metric`                              |
            +-------------------------------+-------------------------------+-------------------------------------------------+
        
        *Object functions*

            .. function:: get()

                Fill the object with values for all the attributes. Once filled, the object can be printed
                using :func:`pyfos_utils.response_print`

                :param session: session handler returned by :func:`pyfos_auth.login`
                :rtype: dictionary of error or success response

        *Attribute functions*

            .. function:: peek_name()

                Reads name from the circuit stats object.
                        
                :rtype: None on error and value on success

            .. function:: peek_circuit_id()

                Reads circuit ID from the circuit stats object.
                        
                :rtype: None on error and value on success
                
            .. function:: peek_flow_status()

                Reads flow status from the circuit stats object.
                        
                :rtype: None on error and value on success

            .. function:: peek_operational_status()

                Reads the operation status from the circuit stats object.
                        
                :rtype: None on error and value on success

            .. function:: peek_connection_count()

                Reads the connection count from the circuit stats object.
                        
                :rtype: None on error and value on success

            .. function:: peek_duration()

                Reads the duration for from the circuit stats object
                        
                :rtype: None on error and value on success

            .. function:: peek_metric()

                Reads metric from the circuit stats object.
                        
                :rtype: None on error and value on success              

            .. function:: set_name(name)

                Set the name in the object.
                        
                :rtype: dictionary of error or success response and value with "name" as key

            .. function:: set_circuit_id(circuitID)

                Set the circuit ID name in the circuit stats object.
                        
                :rtype: dictionary of error or success response and value with "circuit-id" as key
                
        """
        def __init__(self, dictvalues={}):
            super().__init__(pyfos_rest_util.rest_obj_type.circuit_stats, "/rest/running/brocade-extension-tunnel/extension-circuit-statistics")
            self.add(pyfos_rest_util.rest_attribute("name", pyfos_type.type_str, None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
            self.add(pyfos_rest_util.rest_attribute("circuit-id", pyfos_type.type_str, None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
            self.add(pyfos_rest_util.rest_attribute("flow-status", pyfos_type.type_str, None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
            self.add(pyfos_rest_util.rest_attribute("operational-status", pyfos_type.type_str, None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
            self.add(pyfos_rest_util.rest_attribute("metric", pyfos_type.type_str, None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
            self.add(pyfos_rest_util.rest_attribute("connection-count", pyfos_type.type_str, None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
            self.add(pyfos_rest_util.rest_attribute("duration", pyfos_type.type_str, None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))          
            self.load(dictvalues, 1)

