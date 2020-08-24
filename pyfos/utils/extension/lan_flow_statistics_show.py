#!/usr/bin/env python3


# Copyright © 2019-2020 Broadcom. All rights reserved.
# The term “Broadcom” refers to Broadcom Inc. and/or its subsidiaries.
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


# lan_flow_statistics_show.py(pyGen v1.0.0)


"""

:mod:`lan_flow_statistics_show` - PyFOS util to show for\
 lan_flow_statistics
******************************************************************************\
*******************************************************************************
The:mod:`lan_flow_statistics_show` PyFOS util to show for lan_flow_statistics


The LAN per-flow statistics.

lan_flow_statistics_show: usage

* Infrastructure Options:
    * -i,--ipaddr=IPADDR: The IP address of the FOS switch.
    * -L,--login=LOGIN: The login name.
    * -P,--password=PASSWORD: The password.
    * -f,--vfid=VFID: The VFID to which the request is directed.
    * -s,--secured=MODE: The HTTPS mode "self" or "CA" [Optional].
    * -v,--verbose: Verbose mode [Optional].
    * -a,--authtoken: AuthToken value or AuthTokenManager config\
    file[OPTIONAL].
    * -z,--nosession: Sessionless authentication based login[OPTIONAL].
    * --nocredential: No credential to be sent in the request[OPTIONAL].

* Util Script Options:
    * --out-bytes-wan-compression=OUT-BYTES-WAN-COMPRESSION: Total bytes sent\
      compression engine on WAN.
    * --in-packets-lan-session-manager=IN-PACKETS-LAN-SESSION-MANAGER: Total\
      packets received by LAN session manager.
    * --vlan-priority=VLAN-PRIORITY: Specifies the VLAN priority associated\
      with the flow.
    * --traffic-control-list-name=TRAFFIC-CONTROL-LIST-NAME: The\
      traffic-control-list name matching the flow filter to allow the\
      traffic.
    * --out-bytes-lan-session-manager=OUT-BYTES-LAN-SESSION-MANAGER: Total\
      bytes sent by LAN session manager.
    * --tcp-retransmits=TCP-RETRANSMITS: TCP retransmits /lost packets.
    * --zero-window-count=ZERO-WINDOW-COUNT: The count of TCP zero window\
      encountered.
    * --active-flow=ACTIVE-FLOW: Indicates that LAN flow is currently active. \
      true: The flow is active. false: The flow is not active.
    * --in-drops-lan-session-manager=IN-DROPS-LAN-SESSION-MANAGER: The number\
      of drops at the ingress from LAN session manager.
    * --destination-port=DESTINATION-PORT: Remote destination port number of\
      the LAN flow.
    * --in-bytes-average=IN-BYTES-AVERAGE: The throughput in bps for packets\
      received via an extension tunnel over WAN per 30s average.
    * --destination-ip-address=DESTINATION-IP-ADDRESS: Destination IP address\
      corresponding to the LAN flow.
    * --in-bytes-lan-session-manager=IN-BYTES-LAN-SESSION-MANAGER: Total bytes\
      received by LAN session manager.
    * --in-bytes-lan-compression=IN-BYTES-LAN-COMPRESSION: Total bytes\
      received by compression engine from LAN.
    * --out-tcp-packets=OUT-TCP-PACKETS: Total TCP packets sent.
    * --duplicate-acknowledgement=DUPLICATE-ACKNOWLEDGEMENT: TCP duplicate ACK\
      received.
    * --source-port=SOURCE-PORT: Source port number of the LAN flow.
    * --dp-id=DP-ID: Extension Data Path Processor ID associated with flow.\
      Based on platform either it will have a single DP or dual DP. In case\
      of single DP only DP0 is supported, and in case of dual DP both DP0\
      and DP1 are supported  0 : DP0 1 : DP1.
    * --in-bytes-wan-compression=IN-BYTES-WAN-COMPRESSION: Total bytes\
      received by compression engine from WAN.
    * --in-tcp-bytes=IN-TCP-BYTES: Total bytes received.
    * --vlan-id=VLAN-ID: Specifies the VLAN ID associated with the flow. When\
      not set, this value will show up as 0.
    * --out-packets-lan-session-manager=OUT-PACKETS-LAN-SESSION-MANAGER: Total\
      packets sent by LAN session manager.
    * --zero-window-maximum-duration=ZERO-WINDOW-MAXIMUM-DURATION: The maximum\
      of zero window duration encountered.
    * --source-ip-address=SOURCE-IP-ADDRESS: Source IP address corresponding\
      to the LAN flow.
    * --fast-retransmits=FAST-RETRANSMITS: TCP fast retransmits count.
    * --rtt=RTT: round trip time.
    * --ve-port=VE-PORT: The VE port of the extension-tunnel interface.
    * --hcl-flow=HCL-FLOW: Indicates that LAN flow is in HCL.  true: The flow\
      is in HCL. false: The flow is not in HCL.
    * --dscp=DSCP: DSCP value for the LAN flow.
    * --slot=SLOT: In case of non-chassis system, the slot number is always 0.\
      In case of chassis system, it is the slot number of chassis in which\
      the extension blade is inserted in. In case of chassis, slot number is\
      non-zero value.
    * --crc-errors=CRC-ERRORS: Number of CRC errors encountered.
    * --lan-interface=LAN-INTERFACE: The interface corresponding to the\
      traffic. This could be either a GE port or a LAG name associated with\
      the LAN flow.
    * --local-host-mss=LOCAL-HOST-MSS: The local-host-mss is the MSS of the\
      TCP connection at the LAN ingress side connected host.
    * --start-time=START-TIME: Indicates the LAN flow start time.
    * --out-tcp-bytes=OUT-TCP-BYTES: Total bytes sent.
    * --out-bytes-average=OUT-BYTES-AVERAGE: The throughput in bps for packets\
      sent over the extension tunnel on WAN per 30s average.
    * --slow-retransmits=SLOW-RETRANSMITS: TCP slow retransmits count.
    * --out-drops-lan-session-manager=OUT-DROPS-LAN-SESSION-MANAGER: The\
      number of drops at the egress from LAN session manager.
    * --out-bytes-lan-compression=OUT-BYTES-LAN-COMPRESSION: Total bytes sent\
      by compression engine on LAN.
    * --flow-index=FLOW-INDEX: flow index associated with the LAN flow. This\
      is a dynamic index associated with the LAN flow. Depending on the LAN\
      flow behavior the index may change and also can get reused after some\
      time but at any given time they will be unique.
    * --qos=QOS: The IP priority QOS associated with the flow.
    * --in-tcp-packets=IN-TCP-PACKETS: Total TCP packets received.
    * --tcp-out-of-order-packets=TCP-OUT-OF-ORDER-PACKETS: TCP total out of\
      order packets.
    * --end-time=END-TIME: Indicates the LAN flow end time.
    * --remote-host-mss=REMOTE-HOST-MSS: The remote-host-mss is the MSS of the\
      TCP connection at peer extension tunnel endpoint connected host to its\
      the LAN ingress side.
    * --protocol=PROTOCOL: Describes that the Layer 4 protocol of the flow.
* Output:
    * Python dictionary content with RESTCONF response data.


.. function:: lan_flow_statistics_show.show_lan_flow_statistics(session,\
out_bytes_wan_compression, in_packets_lan_session_manager, vlan_priority,\
traffic_control_list_name, out_bytes_lan_session_manager, tcp_retransmits,\
zero_window_count, active_flow, in_drops_lan_session_manager,\
destination_port, in_bytes_average, destination_ip_address,\
in_bytes_lan_session_manager, in_bytes_lan_compression, out_tcp_packets,\
duplicate_acknowledgement, source_port, dp_id, in_bytes_wan_compression,\
in_tcp_bytes, vlan_id, out_packets_lan_session_manager,\
zero_window_maximum_duration, source_ip_address, fast_retransmits, rtt,\
mapped_tunnel_ve_port, hcl_flow, dscp, slot, crc_errors, lan_interface,\
local_host_mss, start_time, out_tcp_bytes, out_bytes_average,\
slow_retransmits, out_drops_lan_session_manager, out_bytes_lan_compression,\
flow_index, mapped_tunnel_qos, in_tcp_packets, tcp_out_of_order_packets,\
end_time, remote_host_mss, protocol)

    *Show lan_flow_statistics*

    Example Usage of the Method::

            ret = lan_flow_statistics_show.show_lan_flow_statistics(session,\
 out_bytes_wan_compression, in_packets_lan_session_manager, vlan_priority,\
 traffic_control_list_name, out_bytes_lan_session_manager, tcp_retransmits,\
 zero_window_count, active_flow, in_drops_lan_session_manager,\
 destination_port, in_bytes_average, destination_ip_address,\
 in_bytes_lan_session_manager, in_bytes_lan_compression, out_tcp_packets,\
 duplicate_acknowledgement, source_port, dp_id, in_bytes_wan_compression,\
 in_tcp_bytes, vlan_id, out_packets_lan_session_manager,\
 zero_window_maximum_duration, source_ip_address, fast_retransmits, rtt,\
 mapped_tunnel_ve_port, hcl_flow, dscp, slot, crc_errors, lan_interface,\
 local_host_mss, start_time, out_tcp_bytes, out_bytes_average,\
 slow_retransmits, out_drops_lan_session_manager, out_bytes_lan_compression,\
 flow_index, mapped_tunnel_qos, in_tcp_packets, tcp_out_of_order_packets,\
 end_time, remote_host_mss, protocol)
            print(ret)

    Details::

        lan_flow_statisticsObj = lan_flow_statistics()
       \
 lan_flow_statisticsObj.set_out_bytes_wan_compression(\
 out_bytes_wan_compression)
       \
 lan_flow_statisticsObj.set_in_packets_lan_session_manager(\
 in_packets_lan_session_manager)
        lan_flow_statisticsObj.set_vlan_priority(vlan_priority)
       \
 lan_flow_statisticsObj.set_traffic_control_list_name(\
 traffic_control_list_name)
       \
 lan_flow_statisticsObj.set_out_bytes_lan_session_manager(\
 out_bytes_lan_session_manager)
        lan_flow_statisticsObj.set_tcp_retransmits(tcp_retransmits)
        lan_flow_statisticsObj.set_zero_window_count(zero_window_count)
        lan_flow_statisticsObj.set_active_flow(active_flow)
       \
 lan_flow_statisticsObj.set_in_drops_lan_session_manager(\
 in_drops_lan_session_manager)
        lan_flow_statisticsObj.set_destination_port(destination_port)
        lan_flow_statisticsObj.set_in_bytes_average(in_bytes_average)
       \
 lan_flow_statisticsObj.set_destination_ip_address(destination_ip_address)
       \
 lan_flow_statisticsObj.set_in_bytes_lan_session_manager(\
 in_bytes_lan_session_manager)
       \
 lan_flow_statisticsObj.set_in_bytes_lan_compression(\
 in_bytes_lan_compression)
        lan_flow_statisticsObj.set_out_tcp_packets(out_tcp_packets)
       \
 lan_flow_statisticsObj.set_duplicate_acknowledgement(\
 duplicate_acknowledgement)
        lan_flow_statisticsObj.set_source_port(source_port)
        lan_flow_statisticsObj.set_dp_id(dp_id)
       \
 lan_flow_statisticsObj.set_in_bytes_wan_compression(\
 in_bytes_wan_compression)
        lan_flow_statisticsObj.set_in_tcp_bytes(in_tcp_bytes)
        lan_flow_statisticsObj.set_vlan_id(vlan_id)
       \
 lan_flow_statisticsObj.set_out_packets_lan_session_manager(\
 out_packets_lan_session_manager)
       \
 lan_flow_statisticsObj.set_zero_window_maximum_duration(\
 zero_window_maximum_duration)
        lan_flow_statisticsObj.set_source_ip_address(source_ip_address)
        lan_flow_statisticsObj.set_fast_retransmits(fast_retransmits)
        lan_flow_statisticsObj.set_rtt(rtt)
       \
 lan_flow_statisticsObj.set_mapped_tunnel_ve_port(mapped_tunnel_ve_port)
        lan_flow_statisticsObj.set_hcl_flow(hcl_flow)
        lan_flow_statisticsObj.set_dscp(dscp)
        lan_flow_statisticsObj.set_slot(slot)
        lan_flow_statisticsObj.set_crc_errors(crc_errors)
        lan_flow_statisticsObj.set_lan_interface(lan_interface)
        lan_flow_statisticsObj.set_local_host_mss(local_host_mss)
        lan_flow_statisticsObj.set_start_time(start_time)
        lan_flow_statisticsObj.set_out_tcp_bytes(out_tcp_bytes)
        lan_flow_statisticsObj.set_out_bytes_average(out_bytes_average)
        lan_flow_statisticsObj.set_slow_retransmits(slow_retransmits)
       \
 lan_flow_statisticsObj.set_out_drops_lan_session_manager(\
 out_drops_lan_session_manager)
       \
 lan_flow_statisticsObj.set_out_bytes_lan_compression(\
 out_bytes_lan_compression)
        lan_flow_statisticsObj.set_flow_index(flow_index)
        lan_flow_statisticsObj.set_mapped_tunnel_qos(mapped_tunnel_qos)
        lan_flow_statisticsObj.set_in_tcp_packets(in_tcp_packets)
       \
 lan_flow_statisticsObj.set_tcp_out_of_order_packets(\
 tcp_out_of_order_packets)
        lan_flow_statisticsObj.set_end_time(end_time)
        lan_flow_statisticsObj.set_remote_host_mss(remote_host_mss)
        lan_flow_statisticsObj.set_protocol(protocol)
        ret = _show_lan_flow_statistics(session, lan_flow_statisticsObj)
        print(ret)

    **Inputs**

    :param session: The session returned by the login.
    :param out_bytes_wan_compression: Total bytes sent compression engine on\
      WAN.
    :param in_packets_lan_session_manager: Total packets received by LAN\
      session manager.
    :param vlan_priority: Specifies the VLAN priority associated with the\
      flow.
    :param traffic_control_list_name: The traffic-control-list name matching\
      the flow filter to allow the traffic.
    :param out_bytes_lan_session_manager: Total bytes sent by LAN session\
      manager.
    :param tcp_retransmits: TCP retransmits /lost packets.
    :param zero_window_count: The count of TCP zero window encountered.
    :param active_flow: Indicates that LAN flow is currently active.  true:\
      The flow is active. false: The flow is not active.
    :param in_drops_lan_session_manager: The number of drops at the ingress\
      from LAN session manager.
    :param destination_port: Remote destination port number of the LAN flow.
    :param in_bytes_average: The throughput in bps for packets received via an\
      extension tunnel over WAN per 30s average.
    :param destination_ip_address: Destination IP address corresponding to the\
      LAN flow.
    :param in_bytes_lan_session_manager: Total bytes received by LAN session\
      manager.
    :param in_bytes_lan_compression: Total bytes received by compression\
      engine from LAN.
    :param out_tcp_packets: Total TCP packets sent.
    :param duplicate_acknowledgement: TCP duplicate ACK received.
    :param source_port: Source port number of the LAN flow.
    :param dp_id: Extension Data Path Processor ID associated with flow. Based\
      on platform either it will have a single DP or dual DP. In case of\
      single DP only DP0 is supported, and in case of dual DP both DP0 and\
      DP1 are supported  0 : DP0 1 : DP1.
    :param in_bytes_wan_compression: Total bytes received by compression\
      engine from WAN.
    :param in_tcp_bytes: Total bytes received.
    :param vlan_id: Specifies the VLAN ID associated with the flow. When not\
      set, this value will show up as 0.
    :param out_packets_lan_session_manager: Total packets sent by LAN session\
      manager.
    :param zero_window_maximum_duration: The maximum of zero window duration\
      encountered.
    :param source_ip_address: Source IP address corresponding to the LAN flow.
    :param fast_retransmits: TCP fast retransmits count.
    :param rtt: round trip time.
    :param mapped_tunnel_ve_port: The VE port of the extension-tunnel\
      interface.
    :param hcl_flow: Indicates that LAN flow is in HCL.  true: The flow is in\
      HCL. false: The flow is not in HCL.
    :param dscp: DSCP value for the LAN flow.
    :param slot: In case of non-chassis system, the slot number is always 0.\
      In case of chassis system, it is the slot number of chassis in which\
      the extension blade is inserted in. In case of chassis, slot number is\
      non-zero value.
    :param crc_errors: Number of CRC errors encountered.
    :param lan_interface: The interface corresponding to the traffic. This\
      could be either a GE port or a LAG name associated with the LAN flow.
    :param local_host_mss: The local-host-mss is the MSS of the TCP connection\
      at the LAN ingress side connected host.
    :param start_time: Indicates the LAN flow start time.
    :param out_tcp_bytes: Total bytes sent.
    :param out_bytes_average: The throughput in bps for packets sent over the\
      extension tunnel on WAN per 30s average.
    :param slow_retransmits: TCP slow retransmits count.
    :param out_drops_lan_session_manager: The number of drops at the egress\
      from LAN session manager.
    :param out_bytes_lan_compression: Total bytes sent by compression engine\
      on LAN.
    :param flow_index: flow index associated with the LAN flow. This is a\
      dynamic index associated with the LAN flow. Depending on the LAN flow\
      behavior the index may change and also can get reused after some time\
      but at any given time they will be unique.
    :param mapped_tunnel_qos: The IP priority QOS associated with the flow.
    :param in_tcp_packets: Total TCP packets received.
    :param tcp_out_of_order_packets: TCP total out of order packets.
    :param end_time: Indicates the LAN flow end time.
    :param remote_host_mss: The remote-host-mss is the MSS of the TCP\
      connection at peer extension tunnel endpoint connected host to its the\
      LAN ingress side.
    :param protocol: Describes that the Layer 4 protocol of the flow.

    **Output**

    :rtype: None or one/more instance of class lan_flow_statistics on Success \
    or a dictionary with error.

"""


# Start utils imports
import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_extension import lan_flow_statistics

from pyfos.utils import brcd_util
# End module imports


def _show_lan_flow_statistics(session, lan_flow_statisticsObj):
    objlist = lan_flow_statistics.get(session)
    lan_flow_statisticslist = list()
    if isinstance(objlist, lan_flow_statistics):
        objlist = [objlist]
    if isinstance(objlist, list):
        for i in range(len(objlist)):
            if lan_flow_statisticsObj.peek_out_bytes_wan_compression() is not\
               None and\
               lan_flow_statisticsObj.peek_out_bytes_wan_compression() !=\
               objlist[i].peek_out_bytes_wan_compression():
                continue
            if lan_flow_statisticsObj.peek_in_packets_lan_session_manager() is\
               not None and\
               lan_flow_statisticsObj.peek_in_packets_lan_session_manager()\
               != objlist[i].peek_in_packets_lan_session_manager():
                continue
            if lan_flow_statisticsObj.peek_vlan_priority() is not None and\
               lan_flow_statisticsObj.peek_vlan_priority() !=\
               objlist[i].peek_vlan_priority():
                continue
            if lan_flow_statisticsObj.peek_traffic_control_list_name() is not\
               None and\
               lan_flow_statisticsObj.peek_traffic_control_list_name() !=\
               objlist[i].peek_traffic_control_list_name():
                continue
            if lan_flow_statisticsObj.peek_out_bytes_lan_session_manager() is\
               not None and\
               lan_flow_statisticsObj.peek_out_bytes_lan_session_manager()\
               != objlist[i].peek_out_bytes_lan_session_manager():
                continue
            if lan_flow_statisticsObj.peek_tcp_retransmits() is not None and\
               lan_flow_statisticsObj.peek_tcp_retransmits() !=\
               objlist[i].peek_tcp_retransmits():
                continue
            if lan_flow_statisticsObj.peek_zero_window_count() is not None and\
               lan_flow_statisticsObj.peek_zero_window_count() !=\
               objlist[i].peek_zero_window_count():
                continue
            if lan_flow_statisticsObj.peek_active_flow() is not None and\
               lan_flow_statisticsObj.peek_active_flow() !=\
               objlist[i].peek_active_flow():
                continue
            if lan_flow_statisticsObj.peek_in_drops_lan_session_manager() is\
               not None and\
               lan_flow_statisticsObj.peek_in_drops_lan_session_manager() !=\
               objlist[i].peek_in_drops_lan_session_manager():
                continue
            if lan_flow_statisticsObj.peek_destination_port() is not None and\
               lan_flow_statisticsObj.peek_destination_port() !=\
               objlist[i].peek_destination_port():
                continue
            if lan_flow_statisticsObj.peek_in_bytes_average() is not None and\
               lan_flow_statisticsObj.peek_in_bytes_average() !=\
               objlist[i].peek_in_bytes_average():
                continue
            if lan_flow_statisticsObj.peek_destination_ip_address() is not\
               None and lan_flow_statisticsObj.peek_destination_ip_address()\
               != objlist[i].peek_destination_ip_address():
                continue
            if lan_flow_statisticsObj.peek_in_bytes_lan_session_manager() is\
               not None and\
               lan_flow_statisticsObj.peek_in_bytes_lan_session_manager() !=\
               objlist[i].peek_in_bytes_lan_session_manager():
                continue
            if lan_flow_statisticsObj.peek_in_bytes_lan_compression() is not\
               None and\
               lan_flow_statisticsObj.peek_in_bytes_lan_compression() !=\
               objlist[i].peek_in_bytes_lan_compression():
                continue
            if lan_flow_statisticsObj.peek_out_tcp_packets() is not None and\
               lan_flow_statisticsObj.peek_out_tcp_packets() !=\
               objlist[i].peek_out_tcp_packets():
                continue
            if lan_flow_statisticsObj.peek_duplicate_acknowledgement() is not\
               None and\
               lan_flow_statisticsObj.peek_duplicate_acknowledgement() !=\
               objlist[i].peek_duplicate_acknowledgement():
                continue
            if lan_flow_statisticsObj.peek_source_port() is not None and\
               lan_flow_statisticsObj.peek_source_port() !=\
               objlist[i].peek_source_port():
                continue
            if lan_flow_statisticsObj.peek_dp_id() is not None and\
               lan_flow_statisticsObj.peek_dp_id() !=\
               objlist[i].peek_dp_id():
                continue
            if lan_flow_statisticsObj.peek_in_bytes_wan_compression() is not\
               None and\
               lan_flow_statisticsObj.peek_in_bytes_wan_compression() !=\
               objlist[i].peek_in_bytes_wan_compression():
                continue
            if lan_flow_statisticsObj.peek_in_tcp_bytes() is not None and\
               lan_flow_statisticsObj.peek_in_tcp_bytes() !=\
               objlist[i].peek_in_tcp_bytes():
                continue
            if lan_flow_statisticsObj.peek_vlan_id() is not None and\
               lan_flow_statisticsObj.peek_vlan_id() !=\
               objlist[i].peek_vlan_id():
                continue
            if lan_flow_statisticsObj.peek_out_packets_lan_session_manager()\
               is not None and\
               lan_flow_statisticsObj.peek_out_packets_lan_session_manager()\
               != objlist[i].peek_out_packets_lan_session_manager():
                continue
            if lan_flow_statisticsObj.peek_zero_window_maximum_duration() is\
               not None and\
               lan_flow_statisticsObj.peek_zero_window_maximum_duration() !=\
               objlist[i].peek_zero_window_maximum_duration():
                continue
            if lan_flow_statisticsObj.peek_source_ip_address() is not None and\
               lan_flow_statisticsObj.peek_source_ip_address() !=\
               objlist[i].peek_source_ip_address():
                continue
            if lan_flow_statisticsObj.peek_fast_retransmits() is not None and\
               lan_flow_statisticsObj.peek_fast_retransmits() !=\
               objlist[i].peek_fast_retransmits():
                continue
            if lan_flow_statisticsObj.peek_rtt() is not None and\
               lan_flow_statisticsObj.peek_rtt() != objlist[i].peek_rtt():
                continue
            if lan_flow_statisticsObj.peek_mapped_tunnel_ve_port() is not None\
               and lan_flow_statisticsObj.peek_mapped_tunnel_ve_port() !=\
               objlist[i].peek_mapped_tunnel_ve_port():
                continue
            if lan_flow_statisticsObj.peek_hcl_flow() is not None and\
               lan_flow_statisticsObj.peek_hcl_flow() !=\
               objlist[i].peek_hcl_flow():
                continue
            if lan_flow_statisticsObj.peek_dscp() is not None and\
               lan_flow_statisticsObj.peek_dscp() != objlist[i].peek_dscp():
                continue
            if lan_flow_statisticsObj.peek_slot() is not None and\
               lan_flow_statisticsObj.peek_slot() != objlist[i].peek_slot():
                continue
            if lan_flow_statisticsObj.peek_crc_errors() is not None and\
               lan_flow_statisticsObj.peek_crc_errors() !=\
               objlist[i].peek_crc_errors():
                continue
            if lan_flow_statisticsObj.peek_lan_interface() is not None and\
               lan_flow_statisticsObj.peek_lan_interface() !=\
               objlist[i].peek_lan_interface():
                continue
            if lan_flow_statisticsObj.peek_local_host_mss() is not None and\
               lan_flow_statisticsObj.peek_local_host_mss() !=\
               objlist[i].peek_local_host_mss():
                continue
            if lan_flow_statisticsObj.peek_start_time() is not None and\
               lan_flow_statisticsObj.peek_start_time() !=\
               objlist[i].peek_start_time():
                continue
            if lan_flow_statisticsObj.peek_out_tcp_bytes() is not None and\
               lan_flow_statisticsObj.peek_out_tcp_bytes() !=\
               objlist[i].peek_out_tcp_bytes():
                continue
            if lan_flow_statisticsObj.peek_out_bytes_average() is not None and\
               lan_flow_statisticsObj.peek_out_bytes_average() !=\
               objlist[i].peek_out_bytes_average():
                continue
            if lan_flow_statisticsObj.peek_slow_retransmits() is not None and\
               lan_flow_statisticsObj.peek_slow_retransmits() !=\
               objlist[i].peek_slow_retransmits():
                continue
            if lan_flow_statisticsObj.peek_out_drops_lan_session_manager() is\
               not None and\
               lan_flow_statisticsObj.peek_out_drops_lan_session_manager()\
               != objlist[i].peek_out_drops_lan_session_manager():
                continue
            if lan_flow_statisticsObj.peek_out_bytes_lan_compression() is not\
               None and\
               lan_flow_statisticsObj.peek_out_bytes_lan_compression() !=\
               objlist[i].peek_out_bytes_lan_compression():
                continue
            if lan_flow_statisticsObj.peek_flow_index() is not None and\
               lan_flow_statisticsObj.peek_flow_index() !=\
               objlist[i].peek_flow_index():
                continue
            if lan_flow_statisticsObj.peek_mapped_tunnel_qos() is not None and\
               lan_flow_statisticsObj.peek_mapped_tunnel_qos() !=\
               objlist[i].peek_mapped_tunnel_qos():
                continue
            if lan_flow_statisticsObj.peek_in_tcp_packets() is not None and\
               lan_flow_statisticsObj.peek_in_tcp_packets() !=\
               objlist[i].peek_in_tcp_packets():
                continue
            if lan_flow_statisticsObj.peek_tcp_out_of_order_packets() is not\
               None and\
               lan_flow_statisticsObj.peek_tcp_out_of_order_packets() !=\
               objlist[i].peek_tcp_out_of_order_packets():
                continue
            if lan_flow_statisticsObj.peek_end_time() is not None and\
               lan_flow_statisticsObj.peek_end_time() !=\
               objlist[i].peek_end_time():
                continue
            if lan_flow_statisticsObj.peek_remote_host_mss() is not None and\
               lan_flow_statisticsObj.peek_remote_host_mss() !=\
               objlist[i].peek_remote_host_mss():
                continue
            if lan_flow_statisticsObj.peek_protocol() is not None and\
               lan_flow_statisticsObj.peek_protocol() !=\
               objlist[i].peek_protocol():
                continue
            lan_flow_statisticslist.append(objlist[i])
    else:
        return objlist
    return lan_flow_statisticslist


def show_lan_flow_statistics(session, out_bytes_wan_compression=None,
                             in_packets_lan_session_manager=None,
                             vlan_priority=None,
                             traffic_control_list_name=None,
                             out_bytes_lan_session_manager=None,
                             tcp_retransmits=None, zero_window_count=None,
                             active_flow=None,
                             in_drops_lan_session_manager=None,
                             destination_port=None, in_bytes_average=None,
                             destination_ip_address=None,
                             in_bytes_lan_session_manager=None,
                             in_bytes_lan_compression=None,
                             out_tcp_packets=None,
                             duplicate_acknowledgement=None,
                             source_port=None, dp_id=None,
                             in_bytes_wan_compression=None,
                             in_tcp_bytes=None, vlan_id=None,
                             out_packets_lan_session_manager=None,
                             zero_window_maximum_duration=None,
                             source_ip_address=None, fast_retransmits=None,
                             rtt=None, mapped_tunnel_ve_port=None,
                             hcl_flow=None, dscp=None, slot=None,
                             crc_errors=None, lan_interface=None,
                             local_host_mss=None, start_time=None,
                             out_tcp_bytes=None, out_bytes_average=None,
                             slow_retransmits=None,
                             out_drops_lan_session_manager=None,
                             out_bytes_lan_compression=None, flow_index=None,
                             mapped_tunnel_qos=None, in_tcp_packets=None,
                             tcp_out_of_order_packets=None, end_time=None,
                             remote_host_mss=None, protocol=None):
    lan_flow_statisticsObj = lan_flow_statistics()
    lan_flow_statisticsObj.set_out_bytes_wan_compression(
                           out_bytes_wan_compression)
    lan_flow_statisticsObj.set_in_packets_lan_session_manager(
                           in_packets_lan_session_manager)
    lan_flow_statisticsObj.set_vlan_priority(vlan_priority)
    lan_flow_statisticsObj.set_traffic_control_list_name(
                           traffic_control_list_name)
    lan_flow_statisticsObj.set_out_bytes_lan_session_manager(
                           out_bytes_lan_session_manager)
    lan_flow_statisticsObj.set_tcp_retransmits(tcp_retransmits)
    lan_flow_statisticsObj.set_zero_window_count(zero_window_count)
    lan_flow_statisticsObj.set_active_flow(active_flow)
    lan_flow_statisticsObj.set_in_drops_lan_session_manager(
                           in_drops_lan_session_manager)
    lan_flow_statisticsObj.set_destination_port(destination_port)
    lan_flow_statisticsObj.set_in_bytes_average(in_bytes_average)
    lan_flow_statisticsObj.set_destination_ip_address(destination_ip_address)
    lan_flow_statisticsObj.set_in_bytes_lan_session_manager(
                           in_bytes_lan_session_manager)
    lan_flow_statisticsObj.set_in_bytes_lan_compression(
                           in_bytes_lan_compression)
    lan_flow_statisticsObj.set_out_tcp_packets(out_tcp_packets)
    lan_flow_statisticsObj.set_duplicate_acknowledgement(
                           duplicate_acknowledgement)
    lan_flow_statisticsObj.set_source_port(source_port)
    lan_flow_statisticsObj.set_dp_id(dp_id)
    lan_flow_statisticsObj.set_in_bytes_wan_compression(
                           in_bytes_wan_compression)
    lan_flow_statisticsObj.set_in_tcp_bytes(in_tcp_bytes)
    lan_flow_statisticsObj.set_vlan_id(vlan_id)
    lan_flow_statisticsObj.set_out_packets_lan_session_manager(
                           out_packets_lan_session_manager)
    lan_flow_statisticsObj.set_zero_window_maximum_duration(
                           zero_window_maximum_duration)
    lan_flow_statisticsObj.set_source_ip_address(source_ip_address)
    lan_flow_statisticsObj.set_fast_retransmits(fast_retransmits)
    lan_flow_statisticsObj.set_rtt(rtt)
    lan_flow_statisticsObj.set_mapped_tunnel_ve_port(mapped_tunnel_ve_port)
    lan_flow_statisticsObj.set_hcl_flow(hcl_flow)
    lan_flow_statisticsObj.set_dscp(dscp)
    lan_flow_statisticsObj.set_slot(slot)
    lan_flow_statisticsObj.set_crc_errors(crc_errors)
    lan_flow_statisticsObj.set_lan_interface(lan_interface)
    lan_flow_statisticsObj.set_local_host_mss(local_host_mss)
    lan_flow_statisticsObj.set_start_time(start_time)
    lan_flow_statisticsObj.set_out_tcp_bytes(out_tcp_bytes)
    lan_flow_statisticsObj.set_out_bytes_average(out_bytes_average)
    lan_flow_statisticsObj.set_slow_retransmits(slow_retransmits)
    lan_flow_statisticsObj.set_out_drops_lan_session_manager(
                           out_drops_lan_session_manager)
    lan_flow_statisticsObj.set_out_bytes_lan_compression(
                           out_bytes_lan_compression)
    lan_flow_statisticsObj.set_flow_index(flow_index)
    lan_flow_statisticsObj.set_mapped_tunnel_qos(mapped_tunnel_qos)
    lan_flow_statisticsObj.set_in_tcp_packets(in_tcp_packets)
    lan_flow_statisticsObj.set_tcp_out_of_order_packets(
                           tcp_out_of_order_packets)
    lan_flow_statisticsObj.set_end_time(end_time)
    lan_flow_statisticsObj.set_remote_host_mss(remote_host_mss)
    lan_flow_statisticsObj.set_protocol(protocol)
    return _show_lan_flow_statistics(session, lan_flow_statisticsObj)


def validate(lan_flow_statisticsObj):
    if lan_flow_statisticsObj.peek_out_bytes_wan_compression() is None or\
       lan_flow_statisticsObj.peek_in_packets_lan_session_manager() is None\
       or lan_flow_statisticsObj.peek_vlan_priority() is None or\
       lan_flow_statisticsObj.peek_traffic_control_list_name() is None or\
       lan_flow_statisticsObj.peek_out_bytes_lan_session_manager() is None\
       or lan_flow_statisticsObj.peek_tcp_retransmits() is None or\
       lan_flow_statisticsObj.peek_zero_window_count() is None or\
       lan_flow_statisticsObj.peek_active_flow() is None or\
       lan_flow_statisticsObj.peek_in_drops_lan_session_manager() is None or\
       lan_flow_statisticsObj.peek_destination_port() is None or\
       lan_flow_statisticsObj.peek_in_bytes_average() is None or\
       lan_flow_statisticsObj.peek_destination_ip_address() is None or\
       lan_flow_statisticsObj.peek_in_bytes_lan_session_manager() is None or\
       lan_flow_statisticsObj.peek_in_bytes_lan_compression() is None or\
       lan_flow_statisticsObj.peek_out_tcp_packets() is None or\
       lan_flow_statisticsObj.peek_duplicate_acknowledgement() is None or\
       lan_flow_statisticsObj.peek_source_port() is None or\
       lan_flow_statisticsObj.peek_dp_id() is None or\
       lan_flow_statisticsObj.peek_in_bytes_wan_compression() is None or\
       lan_flow_statisticsObj.peek_in_tcp_bytes() is None or\
       lan_flow_statisticsObj.peek_vlan_id() is None or\
       lan_flow_statisticsObj.peek_out_packets_lan_session_manager() is None\
       or lan_flow_statisticsObj.peek_zero_window_maximum_duration() is None\
       or lan_flow_statisticsObj.peek_source_ip_address() is None or\
       lan_flow_statisticsObj.peek_fast_retransmits() is None or\
       lan_flow_statisticsObj.peek_rtt() is None or\
       lan_flow_statisticsObj.peek_mapped_tunnel_ve_port() is None or\
       lan_flow_statisticsObj.peek_hcl_flow() is None or\
       lan_flow_statisticsObj.peek_dscp() is None or\
       lan_flow_statisticsObj.peek_slot() is None or\
       lan_flow_statisticsObj.peek_crc_errors() is None or\
       lan_flow_statisticsObj.peek_lan_interface() is None or\
       lan_flow_statisticsObj.peek_local_host_mss() is None or\
       lan_flow_statisticsObj.peek_start_time() is None or\
       lan_flow_statisticsObj.peek_out_tcp_bytes() is None or\
       lan_flow_statisticsObj.peek_out_bytes_average() is None or\
       lan_flow_statisticsObj.peek_slow_retransmits() is None or\
       lan_flow_statisticsObj.peek_out_drops_lan_session_manager() is None\
       or lan_flow_statisticsObj.peek_out_bytes_lan_compression() is None or\
       lan_flow_statisticsObj.peek_flow_index() is None or\
       lan_flow_statisticsObj.peek_mapped_tunnel_qos() is None or\
       lan_flow_statisticsObj.peek_in_tcp_packets() is None or\
       lan_flow_statisticsObj.peek_tcp_out_of_order_packets() is None or\
       lan_flow_statisticsObj.peek_end_time() is None or\
       lan_flow_statisticsObj.peek_remote_host_mss() is None or\
       lan_flow_statisticsObj.peek_protocol() is None:
        return 0
    return 0


def main(argv):
    filters = ["out_bytes_wan_compression", "in_packets_lan_session_manager",
               "vlan_priority", "traffic_control_list_name",
               "out_bytes_lan_session_manager", "tcp_retransmits",
               "zero_window_count", "active_flow",
               "in_drops_lan_session_manager", "destination_port",
               "in_bytes_average", "destination_ip_address",
               "in_bytes_lan_session_manager", "in_bytes_lan_compression",
               "out_tcp_packets", "duplicate_acknowledgement", "source_port",
               "mapped_tunnel", "dp_id", "in_bytes_wan_compression",
               "in_tcp_bytes", "vlan_id", "out_packets_lan_session_manager",
               "zero_window_maximum_duration", "source_ip_address",
               "fast_retransmits", "rtt", "mapped_tunnel_ve_port",
               "hcl_flow", "dscp", "slot", "crc_errors", "lan_interface",
               "local_host_mss", "start_time", "out_tcp_bytes",
               "out_bytes_average", "slow_retransmits",
               "out_drops_lan_session_manager", "out_bytes_lan_compression",
               "flow_index", "mapped_tunnel_qos", "in_tcp_packets",
               "tcp_out_of_order_packets", "end_time", "remote_host_mss",
               "protocol"]
    inputs = brcd_util.parse(argv, lan_flow_statistics, filters, validate)
    session = brcd_util.getsession(inputs)
    result = _show_lan_flow_statistics(session, inputs['utilobject'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
