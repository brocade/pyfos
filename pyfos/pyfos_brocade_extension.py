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


# pyfos_brocade_extension.py(pyGen v1.0.0)


"""

:mod:`pyfos_brocade_extension` - PyFOS module for management and\
 statistics for brocade extension.
******************************************************************************\
*******************************************************************************
The:mod:`pyfos_brocade_extension` The PyFOS module support for management and\
 statistics for brocade extension.
"""


# Start module imports
from pyfos import pyfos_rest_util
from pyfos.pyfos_type import pyfos_type
from pyfos import pyfos_version as version
# End module imports


class global_lan_statistics(pyfos_rest_util.rest_object):

    """Class of global_lan_statistics

    *Description global_lan_statistics*

        Represents global LAN DP statistics for extension blade or system.

    Important class members of global_lan_statistics:

        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | Attribute Name                                           | Description                      |  Frequently Used Methods                                                   |
        +==========================================================+==================================+============================================================================+
        | slot                                                     | In case of non-chassis system,   | :func:`peek_slot`                                                          |
        |                                                          | the slot number is always 0.     | :func:`set_slot`                                                           |
        |                                                          | In case of chassis system, it    |                                                                            |
        |                                                          | is the slot number of chassis    |                                                                            |
        |                                                          | in which the extension blade     |                                                                            |
        |                                                          | is inserted in. In case of       |                                                                            |
        |                                                          | chassis, slot number is          |                                                                            |
        |                                                          | non-zero value.                  |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | dp-id                                                    | Extension Data Path Processor    | :func:`peek_dp_id`                                                         |
        |                                                          | ID. Based on platform either     | :func:`set_dp_id`                                                          |
        |                                                          | it will have a single DP or      |                                                                            |
        |                                                          | dual DP. In case of single DP    |                                                                            |
        |                                                          | only DP0 is supported, and in    |                                                                            |
        |                                                          | case of dual DP both DP0 and     |                                                                            |
        |                                                          | DP1 are supported 0 : DP0 1 :    |                                                                            |
        |                                                          | DP1.                             |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | in-udp-packets-1500-bytes                                | Number of UDP packets received   | :func:`peek_in_udp_packets_1500_bytes`                                     |
        |                                                          | of size equal to & greater       |                                                                            |
        |                                                          | than 1024 bytes but less than    |                                                                            |
        |                                                          | 1500 bytes.                      |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | out-as-is-ip-pdu-drops                                   | Number of as-is Tx IP PDUs       | :func:`peek_out_as_is_ip_pdu_drops`                                        |
        |                                                          | dropped.                         |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | in-error-parity                                          | Number of Parity errors          | :func:`peek_in_error_parity`                                               |
        |                                                          | detected on Rx packets.          |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | active-tcp-connections                                   | Active TCP connection count.     | :func:`peek_active_tcp_connections`                                        |
        |                                                          |                                  |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | in-udp-pdus                                              | Number of UDP PDUs received      | :func:`peek_in_udp_pdus`                                                   |
        |                                                          | from host.                       |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | total-ipv6-packets                                       | Total IPv6 packets received -    | :func:`peek_total_ipv6_packets`                                            |
        |                                                          | IPv6 WQEs received by IP API     |                                                                            |
        |                                                          | layer.                           |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | syn-fail                                                 | Number of SYN packets dropped    | :func:`peek_syn_fail`                                                      |
        |                                                          | due to error.                    |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | out-tcp-bytes                                            | Total number of TCP bytes        | :func:`peek_out_tcp_bytes`                                                 |
        |                                                          | transmitted.                     |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | in-icmp-pdu-drops-due-to-stream-flow-control             | Number of ICMP PDU drop due to   | :func:`peek_in_icmp_pdu_drops_due_to_stream_flow_control`                  |
        |                                                          | stream flow control.             |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | in-udp-packets-128-bytes                                 | Number of UDP packets received   | :func:`peek_in_udp_packets_128_bytes`                                      |
        |                                                          | of size equal to & greater       |                                                                            |
        |                                                          | than 64 bytes but less than      |                                                                            |
        |                                                          | 128 bytes.                       |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | tcp-tcl-deny-connections                                 | Number of TCP connection         | :func:`peek_tcp_tcl_deny_connections`                                      |
        |                                                          | denied based on TCL deny rule.   |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | established-udp-connections                              | Number of UDP connections        | :func:`peek_established_udp_connections`                                   |
        |                                                          | opened since bootup.             |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | in-udp-tcl-lookup-fail-pdus                              | Number of UDP PDUs dropped due   | :func:`peek_in_udp_tcl_lookup_fail_pdus`                                   |
        |                                                          | to TCL lookup.                   |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | in-total-udp-pdu-drops                                   | Total UDP PDUs dropped due to    | :func:`peek_in_total_udp_pdu_drops`                                        |
        |                                                          | multiple reasons.                |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | in-error-tcp-checksum                                    | Number of TCP checksum errors    | :func:`peek_in_error_tcp_checksum`                                         |
        |                                                          | detected on Rx packets.          |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | in-udp-packets-256-bytes                                 | Number of UDP packets received   | :func:`peek_in_udp_packets_256_bytes`                                      |
        |                                                          | of size equal to & greater       |                                                                            |
        |                                                          | than 128 bytes but less than     |                                                                            |
        |                                                          | 256 bytes.                       |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | in-error-length                                          | Number of Length errors          | :func:`peek_in_error_length`                                               |
        |                                                          | detected on Rx packets.          |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | out-udp-packets-1500-bytes                               | Number of UDP packets            | :func:`peek_out_udp_packets_1500_bytes`                                    |
        |                                                          | transmitted of size equal to &   |                                                                            |
        |                                                          | greater than 1024 bytes but      |                                                                            |
        |                                                          | less than 1500 bytes.            |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | maximum-udp-connection-exceeded-on-egress                | Total UDP flows failed due to    | :func:`peek_maximum_udp_connection_exceeded_on_egress`                     |
        |                                                          | Maximum context on egress.       |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | in-total-icmp-pdu-drops                                  | Number of ICMP PDU drops.        | :func:`peek_in_total_icmp_pdu_drops`                                       |
        |                                                          |                                  |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | in-error-crc                                             | Number of CRC errors detected    | :func:`peek_in_error_crc`                                                  |
        |                                                          | on Rx packets.                   |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | out-udp-packets-64-bytes                                 | Number of UDP packets            | :func:`peek_out_udp_packets_64_bytes`                                      |
        |                                                          | transmitted of size less than    |                                                                            |
        |                                                          | 64 bytes.                        |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | drop-packets                                             | Number of LSM packet dropped     | :func:`peek_drop_packets`                                                  |
        |                                                          | in egress.                       |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | flow-control-on                                          | Flow control on from FTNL.       | :func:`peek_flow_control_on`                                               |
        |                                                          |                                  |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | active-tcp-connections-on-remote-backup                  | Active clone HCL TCP             | :func:`peek_active_tcp_connections_on_remote_backup`                       |
        |                                                          | connection count on Remote       |                                                                            |
        |                                                          | Backup tunnel.                   |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | flow-control-off                                         | Flow control off from FTNL.      | :func:`peek_flow_control_off`                                              |
        |                                                          |                                  |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | maximum-udp-connection-exceeded                          | Total UDP flows failed due to    | :func:`peek_maximum_udp_connection_exceeded`                               |
        |                                                          | Maximum context on ingress and   |                                                                            |
        |                                                          | egress.                          |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | out-pdu-preserve-on                                      | Number of times transmit with    | :func:`peek_out_pdu_preserve_on`                                           |
        |                                                          | PDU preserve ON.                 |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | maximum-tcp-connection-exceeded-as-client                | Maximum connection exceeded on   | :func:`peek_maximum_tcp_connection_exceeded_as_client`                     |
        |                                                          | listen connection allocation.    |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | in-as-is-ip-tcl-deny-pdus                                | non-terminated TCP,              | :func:`peek_in_as_is_ip_tcl_deny_pdus`                                     |
        |                                                          | non-batched UDP, Non-ICMP PDU    |                                                                            |
        |                                                          | dropped due to TCL deny          |                                                                            |
        |                                                          | status.                          |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | in-total-as-is-ip-pdu-drops                              | Total non-terminated TCP,        | :func:`peek_in_total_as_is_ip_pdu_drops`                                   |
        |                                                          | non-batched UDP, Non-ICMP PDU    |                                                                            |
        |                                                          | dropped in ingress.              |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | udp-packets-sent-as-is                                   | Total UDP packets sent as-is.    | :func:`peek_udp_packets_sent_as_is`                                        |
        |                                                          |                                  |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | in-tcp-bytes                                             | Total number of TCP bytes        | :func:`peek_in_tcp_bytes`                                                  |
        |                                                          | received.                        |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | in-udp-tcl-deny-pdus                                     | Number of UDP PDUs dropped due   | :func:`peek_in_udp_tcl_deny_pdus`                                          |
        |                                                          | to TCL deny.                     |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | out-udp-packets-1024-bytes                               | Number of UDP packets            | :func:`peek_out_udp_packets_1024_bytes`                                    |
        |                                                          | transmitted of size equal to &   |                                                                            |
        |                                                          | greater than 512 bytes but       |                                                                            |
        |                                                          | less than 1024 bytes.            |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | out-udp-packets-3000-bytes                               | Number of UDP packets            | :func:`peek_out_udp_packets_3000_bytes`                                    |
        |                                                          | transmitted of size equal to &   |                                                                            |
        |                                                          | greater than 1500 bytes but      |                                                                            |
        |                                                          | less than 3000 bytes.            |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | stale-reset-from-host                                    | Stale reset from host.           | :func:`peek_stale_reset_from_host`                                         |
        |                                                          |                                  |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | in-udp-packets-3000-bytes                                | Number of UDP packets received   | :func:`peek_in_udp_packets_3000_bytes`                                     |
        |                                                          | of size equal to & greater       |                                                                            |
        |                                                          | than 1500 bytes but less than    |                                                                            |
        |                                                          | 3000 bytes.                      |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | in-icmp-tcl-deny-pdus                                    | Number of ICMP PDUs dropped      | :func:`peek_in_icmp_tcl_deny_pdus`                                         |
        |                                                          | due to TCL returning deny        |                                                                            |
        |                                                          | status.                          |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | closed-udp-connections                                   | Number of UDP connections        | :func:`peek_closed_udp_connections`                                        |
        |                                                          | closed since bootup.             |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | tcp-tcl-lookup-fail                                      | Number of TCP connection         | :func:`peek_tcp_tcl_lookup_fail`                                           |
        |                                                          | denied based on TCL lookup       |                                                                            |
        |                                                          | failure.                         |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | in-as-is-ip-tcl-lookup-fail-pdus                         | non-terminated TCP,              | :func:`peek_in_as_is_ip_tcl_lookup_fail_pdus`                              |
        |                                                          | non-batched UDP, Non-ICMP PDU    |                                                                            |
        |                                                          | dropped due to TCL lookup        |                                                                            |
        |                                                          | failure.                         |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | established-tcp-connections                              | Total LAN TCP connections        | :func:`peek_established_tcp_connections`                                   |
        |                                                          | established.                     |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | in-udp-packets-6000-bytes                                | Number of UDP packets received   | :func:`peek_in_udp_packets_6000_bytes`                                     |
        |                                                          | of size equal to & greater       |                                                                            |
        |                                                          | than 4500 bytes but less than    |                                                                            |
        |                                                          | 6000 bytes.                      |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | closed-tcp-connections                                   | Total LAN TCP connections        | :func:`peek_closed_tcp_connections`                                        |
        |                                                          | closed.                          |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | in-pdu-preserve-on                                       | Number of packets received       | :func:`peek_in_pdu_preserve_on`                                            |
        |                                                          | with PDU preserve ON.            |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | in-udp-packets-1024-bytes                                | Number of UDP packets received   | :func:`peek_in_udp_packets_1024_bytes`                                     |
        |                                                          | of size equal to & greater       |                                                                            |
        |                                                          | than 512 bytes but less than     |                                                                            |
        |                                                          | 1024 bytes.                      |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | in-error-mac                                             | Number of MAC errors detected    | :func:`peek_in_error_mac`                                                  |
        |                                                          | on Rx packets.                   |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | in-udp-packets-4500-bytes                                | Number of UDP packets received   | :func:`peek_in_udp_packets_4500_bytes`                                     |
        |                                                          | of size equal to & greater       |                                                                            |
        |                                                          | than 3000 bytes but less than    |                                                                            |
        |                                                          | 4500 bytes.                      |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | out-udp-packets-4500-bytes                               | Number of UDP packets            | :func:`peek_out_udp_packets_4500_bytes`                                    |
        |                                                          | transmitted of size equal to &   |                                                                            |
        |                                                          | greater than 3000 bytes but      |                                                                            |
        |                                                          | less than 4500 bytes.            |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | maximum-tcp-connection-per-second-exceeded-as-client     | Maximum connection per second    | :func:`peek_maximum_tcp_connection_per_second_exceeded_as_client`          |
        |                                                          | exceeded on listen connection    |                                                                            |
        |                                                          | allocation.                      |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | udp-route-lookup-fail                                    | Drop of NT PDUs on egress due    | :func:`peek_udp_route_lookup_fail`                                         |
        |                                                          | to route lookup failure.         |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | in-as-is-ip-pdu-drops-due-to-stream-flow-control         | non-terminated TCP,              | :func:`peek_in_as_is_ip_pdu_drops_due_to_stream_flow_control`              |
        |                                                          | non-batched UDP, Non-ICMP PDU    |                                                                            |
        |                                                          | dropped due to stream flow       |                                                                            |
        |                                                          | control.                         |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | maximum-tcp-connection-exceeded-as-server                | Maximum connection exceeded      | :func:`peek_maximum_tcp_connection_exceeded_as_server`                     |
        |                                                          | during active connection         |                                                                            |
        |                                                          | allocation.                      |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | in-udp-pdu-drops-due-to-stream-flow-control              | Number of UDP PDUs dropped due   | :func:`peek_in_udp_pdu_drops_due_to_stream_flow_control`                   |
        |                                                          | to stream flow control.          |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | in-icmp-tcl-lookup-fail-pdus                             | Number of ICMP PDUs dropped      | :func:`peek_in_icmp_tcl_lookup_fail_pdus`                                  |
        |                                                          | due to TCL lookup failure.       |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | active-tcp-connections-on-local-backup                   | Active clone HCL TCP             | :func:`peek_active_tcp_connections_on_local_backup`                        |
        |                                                          | connection count on Local        |                                                                            |
        |                                                          | Backup tunnel.                   |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | syn-received                                             | Number of SYN packets            | :func:`peek_syn_received`                                                  |
        |                                                          | received.                        |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | out-udp-packets-256-bytes                                | Number of UDP packets            | :func:`peek_out_udp_packets_256_bytes`                                     |
        |                                                          | transmitted of size equal to &   |                                                                            |
        |                                                          | greater than 128 bytes but       |                                                                            |
        |                                                          | less than 256 bytes.             |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | drop-bytes                                               | LSM Tx TCP drop bytes.           | :func:`peek_drop_bytes`                                                    |
        |                                                          |                                  |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | udp-pdu-drops-due-to-pko-flow-control                    | Drop of NT PDUs on egress due    | :func:`peek_udp_pdu_drops_due_to_pko_flow_control`                         |
        |                                                          | to PKO flow control.             |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | in-udp-packets-512-bytes                                 | Number of UDP packets received   | :func:`peek_in_udp_packets_512_bytes`                                      |
        |                                                          | of size equal to & greater       |                                                                            |
        |                                                          | than 256 bytes but less than     |                                                                            |
        |                                                          | 512 bytes.                       |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | active-udp-connections                                   | Number of active NT UDP flows.   | :func:`peek_active_udp_connections`                                        |
        |                                                          |                                  |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | out-as-is-ip-pdus                                        | Number of as-is Tx IP PDUs.      | :func:`peek_out_as_is_ip_pdus`                                             |
        |                                                          |                                  |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | in-icmp-pdus                                             | Number of ICMP PDUs received.    | :func:`peek_in_icmp_pdus`                                                  |
        |                                                          |                                  |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | out-udp-packets-6000-bytes                               | Number of UDP packets            | :func:`peek_out_udp_packets_6000_bytes`                                    |
        |                                                          | transmitted of size equal to &   |                                                                            |
        |                                                          | greater than 4500 bytes but      |                                                                            |
        |                                                          | less than 6000 bytes.            |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | in-udp-packets-64-bytes                                  | Number of UDP packets received   | :func:`peek_in_udp_packets_64_bytes`                                       |
        |                                                          | of size less than 64 bytes.      |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | in-udp-packets-9000-bytes                                | Number of UDP packets received   | :func:`peek_in_udp_packets_9000_bytes`                                     |
        |                                                          | of size equal to & greater       |                                                                            |
        |                                                          | than 6000 bytes but less than    |                                                                            |
        |                                                          | 9000 bytes.                      |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | out-udp-packets-512-bytes                                | Number of UDP packets            | :func:`peek_out_udp_packets_512_bytes`                                     |
        |                                                          | transmitted of size equal to &   |                                                                            |
        |                                                          | greater than 256 bytes but       |                                                                            |
        |                                                          | less than 512 bytes.             |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | out-icmp-pdu-drops                                       | Number of Tx ICMP PDU dropped.   | :func:`peek_out_icmp_pdu_drops`                                            |
        |                                                          |                                  |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | in-as-is-ip-pdus                                         | non-terminated TCP,              | :func:`peek_in_as_is_ip_pdus`                                              |
        |                                                          | non-batched UDP, Non-ICMP PDU    |                                                                            |
        |                                                          | received.                        |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | out-udp-pdu-drops                                        | Number of Tx UDP PDUs dropped    | :func:`peek_out_udp_pdu_drops`                                             |
        |                                                          | due to different reasons.        |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | out-udp-packets-128-bytes                                | Number of UDP packets            | :func:`peek_out_udp_packets_128_bytes`                                     |
        |                                                          | transmitted of size equal to &   |                                                                            |
        |                                                          | greater than 64 bytes but less   |                                                                            |
        |                                                          | than 128 bytes.                  |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | in-error-ip-checksum                                     | Number of IP checksum errors     | :func:`peek_in_error_ip_checksum`                                          |
        |                                                          | detected on Rx packets.          |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | maximum-tcp-connection-per-second-exceeded-as-server     | Maximum connection per second    | :func:`peek_maximum_tcp_connection_per_second_exceeded_as_server`          |
        |                                                          | exceeded on listen connection    |                                                                            |
        |                                                          | allocation.                      |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | out-udp-packets-9000-bytes                               | Number of UDP packets            | :func:`peek_out_udp_packets_9000_bytes`                                    |
        |                                                          | transmitted of size equal to &   |                                                                            |
        |                                                          | greater than 6000 bytes but      |                                                                            |
        |                                                          | less than 9000 bytes.            |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | out-udp-pdus                                             | Number of Tx UDP PDU.            | :func:`peek_out_udp_pdus`                                                  |
        |                                                          |                                  |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+
        | out-icmp-pdus                                            | Number of Tx ICMP PDUs.          | :func:`peek_out_icmp_pdus`                                                 |
        |                                                          |                                  |                                                                            |
        +----------------------------------------------------------+----------------------------------+----------------------------------------------------------------------------+

    *Object functions for global_lan_statistics*

    .. function:: get()

        Get the instances of class "global_lan_statistics from switch. The
         object can be printed using :func:`pyfos_utils.response_print`.

        :param session: The session handler returned by
         :func:`pyfos_auth.login`.

        :rtype: A dictionary of errors or a success response.


    *Class functions for global_lan_statistics*

        .. function:: peek_slot()

            Reads the value assigned to slot in the object.

            :rtype: None on error and a value on success.


        .. function:: set_slot(value)

            Set the value of slot in the object.

            :rtype: A dictionary of error or a success response and a value
             with "slot" as the key


        .. function:: peek_dp_id()

            Reads the value assigned to dp-id in the object.

            :rtype: None on error and a value on success.


        .. function:: set_dp_id(value)

            Set the value of dp-id in the object.

            :rtype: A dictionary of error or a success response and a value
             with "dp-id" as the key


        .. function:: peek_in_udp_packets_1500_bytes()

            Reads the value assigned to in-udp-packets-1500-bytes in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_out_as_is_ip_pdu_drops()

            Reads the value assigned to out-as-is-ip-pdu-drops in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_in_error_parity()

            Reads the value assigned to in-error-parity in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_active_tcp_connections()

            Reads the value assigned to active-tcp-connections in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_in_udp_pdus()

            Reads the value assigned to in-udp-pdus in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_total_ipv6_packets()

            Reads the value assigned to total-ipv6-packets in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_syn_fail()

            Reads the value assigned to syn-fail in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_out_tcp_bytes()

            Reads the value assigned to out-tcp-bytes in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_in_icmp_pdu_drops_due_to_stream_flow_control()

            Reads the value assigned to
             in-icmp-pdu-drops-due-to-stream-flow-control in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_in_udp_packets_128_bytes()

            Reads the value assigned to in-udp-packets-128-bytes in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_tcp_tcl_deny_connections()

            Reads the value assigned to tcp-tcl-deny-connections in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_established_udp_connections()

            Reads the value assigned to established-udp-connections in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_in_udp_tcl_lookup_fail_pdus()

            Reads the value assigned to in-udp-tcl-lookup-fail-pdus in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_in_total_udp_pdu_drops()

            Reads the value assigned to in-total-udp-pdu-drops in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_in_error_tcp_checksum()

            Reads the value assigned to in-error-tcp-checksum in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_in_udp_packets_256_bytes()

            Reads the value assigned to in-udp-packets-256-bytes in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_in_error_length()

            Reads the value assigned to in-error-length in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_out_udp_packets_1500_bytes()

            Reads the value assigned to out-udp-packets-1500-bytes in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_maximum_udp_connection_exceeded_on_egress()

            Reads the value assigned to
             maximum-udp-connection-exceeded-on-egress in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_in_total_icmp_pdu_drops()

            Reads the value assigned to in-total-icmp-pdu-drops in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_in_error_crc()

            Reads the value assigned to in-error-crc in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_out_udp_packets_64_bytes()

            Reads the value assigned to out-udp-packets-64-bytes in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_drop_packets()

            Reads the value assigned to drop-packets in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_flow_control_on()

            Reads the value assigned to flow-control-on in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_active_tcp_connections_on_remote_backup()

            Reads the value assigned to
             active-tcp-connections-on-remote-backup in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_flow_control_off()

            Reads the value assigned to flow-control-off in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_maximum_udp_connection_exceeded()

            Reads the value assigned to maximum-udp-connection-exceeded in
             the object.

            :rtype: None on error and a value on success.


        .. function:: peek_out_pdu_preserve_on()

            Reads the value assigned to out-pdu-preserve-on in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_maximum_tcp_connection_exceeded_as_client()

            Reads the value assigned to
             maximum-tcp-connection-exceeded-as-client in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_in_as_is_ip_tcl_deny_pdus()

            Reads the value assigned to in-as-is-ip-tcl-deny-pdus in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_in_total_as_is_ip_pdu_drops()

            Reads the value assigned to in-total-as-is-ip-pdu-drops in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_udp_packets_sent_as_is()

            Reads the value assigned to udp-packets-sent-as-is in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_in_tcp_bytes()

            Reads the value assigned to in-tcp-bytes in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_in_udp_tcl_deny_pdus()

            Reads the value assigned to in-udp-tcl-deny-pdus in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_out_udp_packets_1024_bytes()

            Reads the value assigned to out-udp-packets-1024-bytes in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_out_udp_packets_3000_bytes()

            Reads the value assigned to out-udp-packets-3000-bytes in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_stale_reset_from_host()

            Reads the value assigned to stale-reset-from-host in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_in_udp_packets_3000_bytes()

            Reads the value assigned to in-udp-packets-3000-bytes in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_in_icmp_tcl_deny_pdus()

            Reads the value assigned to in-icmp-tcl-deny-pdus in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_closed_udp_connections()

            Reads the value assigned to closed-udp-connections in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_tcp_tcl_lookup_fail()

            Reads the value assigned to tcp-tcl-lookup-fail in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_in_as_is_ip_tcl_lookup_fail_pdus()

            Reads the value assigned to in-as-is-ip-tcl-lookup-fail-pdus in
             the object.

            :rtype: None on error and a value on success.


        .. function:: peek_established_tcp_connections()

            Reads the value assigned to established-tcp-connections in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_in_udp_packets_6000_bytes()

            Reads the value assigned to in-udp-packets-6000-bytes in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_closed_tcp_connections()

            Reads the value assigned to closed-tcp-connections in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_in_pdu_preserve_on()

            Reads the value assigned to in-pdu-preserve-on in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_in_udp_packets_1024_bytes()

            Reads the value assigned to in-udp-packets-1024-bytes in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_in_error_mac()

            Reads the value assigned to in-error-mac in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_in_udp_packets_4500_bytes()

            Reads the value assigned to in-udp-packets-4500-bytes in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_out_udp_packets_4500_bytes()

            Reads the value assigned to out-udp-packets-4500-bytes in the
             object.

            :rtype: None on error and a value on success.


        ..
           function:: peek_maximum_tcp_connection_per_second_exceeded_as_cli
           ent()

            Reads the value assigned to
             maximum-tcp-connection-per-second-exceeded-as-client in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_udp_route_lookup_fail()

            Reads the value assigned to udp-route-lookup-fail in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_in_as_is_ip_pdu_drops_due_to_stream_flow_control(
           )

            Reads the value assigned to
             in-as-is-ip-pdu-drops-due-to-stream-flow-control in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_maximum_tcp_connection_exceeded_as_server()

            Reads the value assigned to
             maximum-tcp-connection-exceeded-as-server in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_in_udp_pdu_drops_due_to_stream_flow_control()

            Reads the value assigned to
             in-udp-pdu-drops-due-to-stream-flow-control in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_in_icmp_tcl_lookup_fail_pdus()

            Reads the value assigned to in-icmp-tcl-lookup-fail-pdus in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_active_tcp_connections_on_local_backup()

            Reads the value assigned to
             active-tcp-connections-on-local-backup in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_syn_received()

            Reads the value assigned to syn-received in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_out_udp_packets_256_bytes()

            Reads the value assigned to out-udp-packets-256-bytes in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_drop_bytes()

            Reads the value assigned to drop-bytes in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_udp_pdu_drops_due_to_pko_flow_control()

            Reads the value assigned to udp-pdu-drops-due-to-pko-flow-control
             in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_in_udp_packets_512_bytes()

            Reads the value assigned to in-udp-packets-512-bytes in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_active_udp_connections()

            Reads the value assigned to active-udp-connections in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_out_as_is_ip_pdus()

            Reads the value assigned to out-as-is-ip-pdus in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_in_icmp_pdus()

            Reads the value assigned to in-icmp-pdus in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_out_udp_packets_6000_bytes()

            Reads the value assigned to out-udp-packets-6000-bytes in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_in_udp_packets_64_bytes()

            Reads the value assigned to in-udp-packets-64-bytes in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_in_udp_packets_9000_bytes()

            Reads the value assigned to in-udp-packets-9000-bytes in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_out_udp_packets_512_bytes()

            Reads the value assigned to out-udp-packets-512-bytes in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_out_icmp_pdu_drops()

            Reads the value assigned to out-icmp-pdu-drops in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_in_as_is_ip_pdus()

            Reads the value assigned to in-as-is-ip-pdus in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_out_udp_pdu_drops()

            Reads the value assigned to out-udp-pdu-drops in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_out_udp_packets_128_bytes()

            Reads the value assigned to out-udp-packets-128-bytes in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_in_error_ip_checksum()

            Reads the value assigned to in-error-ip-checksum in the object.

            :rtype: None on error and a value on success.


        ..
           function:: peek_maximum_tcp_connection_per_second_exceeded_as_ser
           ver()

            Reads the value assigned to
             maximum-tcp-connection-per-second-exceeded-as-server in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_out_udp_packets_9000_bytes()

            Reads the value assigned to out-udp-packets-9000-bytes in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_out_udp_pdus()

            Reads the value assigned to out-udp-pdus in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_out_icmp_pdus()

            Reads the value assigned to out-icmp-pdus in the object.

            :rtype: None on error and a value on success.


    """

    def __init__(self, dictvalues=None):

        clsuri = "/rest" + "/running" + "/brocade-extension" +\
                 "/global-lan-statistics"
        clstype = pyfos_rest_util.rest_obj_type.global_lan_statistics
        clsver = version.VER_RANGE_900_and_ABOVE
        super().__init__(clstype, clsuri, clsver)

        self.add(pyfos_rest_util.rest_attribute("slot", pyfos_type.type_int,
                 None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute("dp-id", pyfos_type.type_int,
                 None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute("in-udp-packets-1500-bytes",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("out-as-is-ip-pdu-drops",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("in-error-parity",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("active-tcp-connections",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("in-udp-pdus",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("total-ipv6-packets",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("syn-fail",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("out-tcp-bytes",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "in-icmp-pdu-drops-due-to-stream-flow-control",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("in-udp-packets-128-bytes",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("tcp-tcl-deny-connections",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("established-udp-connections",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("in-udp-tcl-lookup-fail-pdus",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("in-total-udp-pdu-drops",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("in-error-tcp-checksum",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("in-udp-packets-256-bytes",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("in-error-length",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("out-udp-packets-1500-bytes",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "maximum-udp-connection-exceeded-on-egress",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("in-total-icmp-pdu-drops",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("in-error-crc",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("out-udp-packets-64-bytes",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("drop-packets",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("flow-control-on",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "active-tcp-connections-on-remote-backup",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("flow-control-off",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "maximum-udp-connection-exceeded", pyfos_type.type_int,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("out-pdu-preserve-on",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "maximum-tcp-connection-exceeded-as-client",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("in-as-is-ip-tcl-deny-pdus",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("in-total-as-is-ip-pdu-drops",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("udp-packets-sent-as-is",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("in-tcp-bytes",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("in-udp-tcl-deny-pdus",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("out-udp-packets-1024-bytes",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("out-udp-packets-3000-bytes",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("stale-reset-from-host",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("in-udp-packets-3000-bytes",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("in-icmp-tcl-deny-pdus",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("closed-udp-connections",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("tcp-tcl-lookup-fail",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "in-as-is-ip-tcl-lookup-fail-pdus", pyfos_type.type_int,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("established-tcp-connections",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("in-udp-packets-6000-bytes",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("closed-tcp-connections",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("in-pdu-preserve-on",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("in-udp-packets-1024-bytes",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("in-error-mac",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("in-udp-packets-4500-bytes",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("out-udp-packets-4500-bytes",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "maximum-tcp-connection-per-second-exceeded-as-client",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("udp-route-lookup-fail",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "in-as-is-ip-pdu-drops-due-to-stream-flow-control",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "maximum-tcp-connection-exceeded-as-server",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "in-udp-pdu-drops-due-to-stream-flow-control",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "in-icmp-tcl-lookup-fail-pdus", pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "active-tcp-connections-on-local-backup",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("syn-received",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("out-udp-packets-256-bytes",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("drop-bytes",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "udp-pdu-drops-due-to-pko-flow-control",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("in-udp-packets-512-bytes",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("active-udp-connections",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("out-as-is-ip-pdus",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("in-icmp-pdus",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("out-udp-packets-6000-bytes",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("in-udp-packets-64-bytes",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("in-udp-packets-9000-bytes",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("out-udp-packets-512-bytes",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("out-icmp-pdu-drops",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("in-as-is-ip-pdus",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("out-udp-pdu-drops",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("out-udp-packets-128-bytes",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("in-error-ip-checksum",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "maximum-tcp-connection-per-second-exceeded-as-server",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("out-udp-packets-9000-bytes",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("out-udp-pdus",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("out-icmp-pdus",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.load(dictvalues, 1)


class lan_flow_statistics(pyfos_rest_util.rest_object):

    """Class of lan_flow_statistics

    *Description lan_flow_statistics*

        The LAN per-flow statistics.

    Important class members of lan_flow_statistics:

        +-------------------------------------+----------------------------------------------+-------------------------------------------------------+
        | Attribute Name                      | Description                                  |  Frequently Used Methods                              |
        +=====================================+==============================================+=======================================================+
        | dp-id                               | Extension Data Path Processor ID             | :func:`peek_dp_id`                                    |
        |                                     | associated with flow. Based on platform      | :func:`set_dp_id`                                     |
        |                                     | either it will have a single DP or dual      |                                                       |
        |                                     | DP. In case of single DP only DP0 is         |                                                       |
        |                                     | supported, and in case of dual DP both DP0   |                                                       |
        |                                     | and DP1 are supported 0 : DP0 1 : DP1.       |                                                       |
        +-------------------------------------+----------------------------------------------+-------------------------------------------------------+
        | slot                                | In case of non-chassis system, the slot      | :func:`peek_slot`                                     |
        |                                     | number is always 0. In case of chassis       | :func:`set_slot`                                      |
        |                                     | system, it is the slot number of chassis     |                                                       |
        |                                     | in which the extension blade is inserted     |                                                       |
        |                                     | in. In case of chassis, slot number is       |                                                       |
        |                                     | non-zero value.                              |                                                       |
        +-------------------------------------+----------------------------------------------+-------------------------------------------------------+
        | flow-index                          | flow index associated with the LAN flow.     | :func:`peek_flow_index`                               |
        |                                     | This is a dynamic index associated with      | :func:`set_flow_index`                                |
        |                                     | the LAN flow. Depending on the LAN flow      |                                                       |
        |                                     | behavior the index may change and also can   |                                                       |
        |                                     | get reused after some time but at any        |                                                       |
        |                                     | given time they will be unique.              |                                                       |
        +-------------------------------------+----------------------------------------------+-------------------------------------------------------+
        | out-bytes-wan-compression           | Total bytes sent compression engine on       | :func:`peek_out_bytes_wan_compression`                |
        |                                     | WAN.                                         |                                                       |
        +-------------------------------------+----------------------------------------------+-------------------------------------------------------+
        | in-packets-lan-session-manager      | Total packets received by LAN session        | :func:`peek_in_packets_lan_session_manager`           |
        |                                     | manager.                                     |                                                       |
        +-------------------------------------+----------------------------------------------+-------------------------------------------------------+
        | vlan-priority                       | Specifies the VLAN priority associated       | :func:`peek_vlan_priority`                            |
        |                                     | with the flow.                               |                                                       |
        +-------------------------------------+----------------------------------------------+-------------------------------------------------------+
        | traffic-control-list-name           | The traffic-control-list name matching the   | :func:`peek_traffic_control_list_name`                |
        |                                     | flow filter to allow the traffic.            |                                                       |
        +-------------------------------------+----------------------------------------------+-------------------------------------------------------+
        | out-bytes-lan-session-manager       | Total bytes sent by LAN session manager.     | :func:`peek_out_bytes_lan_session_manager`            |
        |                                     |                                              |                                                       |
        +-------------------------------------+----------------------------------------------+-------------------------------------------------------+
        | tcp-retransmits                     | TCP retransmits /lost packets.               | :func:`peek_tcp_retransmits`                          |
        |                                     |                                              |                                                       |
        +-------------------------------------+----------------------------------------------+-------------------------------------------------------+
        | zero-window-count                   | The count of TCP zero window encountered.    | :func:`peek_zero_window_count`                        |
        |                                     |                                              |                                                       |
        +-------------------------------------+----------------------------------------------+-------------------------------------------------------+
        | active-flow                         | Indicates that LAN flow is currently         | :func:`peek_active_flow`                              |
        |                                     | active. true: The flow is active. false:     |                                                       |
        |                                     | The flow is not active.                      |                                                       |
        +-------------------------------------+----------------------------------------------+-------------------------------------------------------+
        | in-drops-lan-session-manager        | The number of drops at the ingress from      | :func:`peek_in_drops_lan_session_manager`             |
        |                                     | LAN session manager.                         |                                                       |
        +-------------------------------------+----------------------------------------------+-------------------------------------------------------+
        | destination-port                    | Remote destination port number of the LAN    | :func:`peek_destination_port`                         |
        |                                     | flow.                                        |                                                       |
        +-------------------------------------+----------------------------------------------+-------------------------------------------------------+
        | in-bytes-average                    | The throughput in bps for packets received   | :func:`peek_in_bytes_average`                         |
        |                                     | via an extension tunnel over WAN per 30s     |                                                       |
        |                                     | average.                                     |                                                       |
        +-------------------------------------+----------------------------------------------+-------------------------------------------------------+
        | destination-ip-address              | Destination IP address corresponding to      | :func:`peek_destination_ip_address`                   |
        |                                     | the LAN flow.                                |                                                       |
        +-------------------------------------+----------------------------------------------+-------------------------------------------------------+
        | in-bytes-lan-session-manager        | Total bytes received by LAN session          | :func:`peek_in_bytes_lan_session_manager`             |
        |                                     | manager.                                     |                                                       |
        +-------------------------------------+----------------------------------------------+-------------------------------------------------------+
        | in-bytes-lan-compression            | Total bytes received by compression engine   | :func:`peek_in_bytes_lan_compression`                 |
        |                                     | from LAN.                                    |                                                       |
        +-------------------------------------+----------------------------------------------+-------------------------------------------------------+
        | out-tcp-packets                     | Total TCP packets sent.                      | :func:`peek_out_tcp_packets`                          |
        |                                     |                                              |                                                       |
        +-------------------------------------+----------------------------------------------+-------------------------------------------------------+
        | duplicate-acknowledgement           | TCP duplicate ACK received.                  | :func:`peek_duplicate_acknowledgement`                |
        |                                     |                                              |                                                       |
        +-------------------------------------+----------------------------------------------+-------------------------------------------------------+
        | source-port                         | Source port number of the LAN flow.          | :func:`peek_source_port`                              |
        |                                     |                                              |                                                       |
        +-------------------------------------+----------------------------------------------+-------------------------------------------------------+
        | in-bytes-wan-compression            | Total bytes received by compression engine   | :func:`peek_in_bytes_wan_compression`                 |
        |                                     | from WAN.                                    |                                                       |
        +-------------------------------------+----------------------------------------------+-------------------------------------------------------+
        | in-tcp-bytes                        | Total bytes received.                        | :func:`peek_in_tcp_bytes`                             |
        |                                     |                                              |                                                       |
        +-------------------------------------+----------------------------------------------+-------------------------------------------------------+
        | vlan-id                             | Specifies the VLAN ID associated with the    | :func:`peek_vlan_id`                                  |
        |                                     | flow. When not set, this value will show     |                                                       |
        |                                     | up as 0.                                     |                                                       |
        +-------------------------------------+----------------------------------------------+-------------------------------------------------------+
        | out-packets-lan-session-manager     | Total packets sent by LAN session manager.   | :func:`peek_out_packets_lan_session_manager`          |
        |                                     |                                              |                                                       |
        +-------------------------------------+----------------------------------------------+-------------------------------------------------------+
        | zero-window-maximum-duration        | The maximum of zero window duration          | :func:`peek_zero_window_maximum_duration`             |
        |                                     | encountered.                                 |                                                       |
        +-------------------------------------+----------------------------------------------+-------------------------------------------------------+
        | source-ip-address                   | Source IP address corresponding to the LAN   | :func:`peek_source_ip_address`                        |
        |                                     | flow.                                        |                                                       |
        +-------------------------------------+----------------------------------------------+-------------------------------------------------------+
        | fast-retransmits                    | TCP fast retransmits count.                  | :func:`peek_fast_retransmits`                         |
        |                                     |                                              |                                                       |
        +-------------------------------------+----------------------------------------------+-------------------------------------------------------+
        | rtt                                 | round trip time.                             | :func:`peek_rtt`                                      |
        |                                     |                                              |                                                       |
        +-------------------------------------+----------------------------------------------+-------------------------------------------------------+
        | hcl-flow                            | Indicates that LAN flow is in HCL. true:     | :func:`peek_hcl_flow`                                 |
        |                                     | The flow is in HCL. false: The flow is not   |                                                       |
        |                                     | in HCL.                                      |                                                       |
        +-------------------------------------+----------------------------------------------+-------------------------------------------------------+
        | dscp                                | DSCP value for the LAN flow.                 | :func:`peek_dscp`                                     |
        |                                     |                                              |                                                       |
        +-------------------------------------+----------------------------------------------+-------------------------------------------------------+
        | crc-errors                          | Number of CRC errors encountered.            | :func:`peek_crc_errors`                               |
        |                                     |                                              |                                                       |
        +-------------------------------------+----------------------------------------------+-------------------------------------------------------+
        | lan-interface                       | The interface corresponding to the           | :func:`peek_lan_interface`                            |
        |                                     | traffic. This could be either a GE port or   |                                                       |
        |                                     | a LAG name associated with the LAN flow.     |                                                       |
        +-------------------------------------+----------------------------------------------+-------------------------------------------------------+
        | local-host-mss                      | The local-host-mss is the MSS of the TCP     | :func:`peek_local_host_mss`                           |
        |                                     | connection at the LAN ingress side           |                                                       |
        |                                     | connected host.                              |                                                       |
        +-------------------------------------+----------------------------------------------+-------------------------------------------------------+
        | start-time                          | Indicates the LAN flow start time.           | :func:`peek_start_time`                               |
        |                                     |                                              |                                                       |
        +-------------------------------------+----------------------------------------------+-------------------------------------------------------+
        | out-tcp-bytes                       | Total bytes sent.                            | :func:`peek_out_tcp_bytes`                            |
        |                                     |                                              |                                                       |
        +-------------------------------------+----------------------------------------------+-------------------------------------------------------+
        | out-bytes-average                   | The throughput in bps for packets sent       | :func:`peek_out_bytes_average`                        |
        |                                     | over the extension tunnel on WAN per 30s     |                                                       |
        |                                     | average.                                     |                                                       |
        +-------------------------------------+----------------------------------------------+-------------------------------------------------------+
        | slow-retransmits                    | TCP slow retransmits count.                  | :func:`peek_slow_retransmits`                         |
        |                                     |                                              |                                                       |
        +-------------------------------------+----------------------------------------------+-------------------------------------------------------+
        | out-drops-lan-session-manager       | The number of drops at the egress from LAN   | :func:`peek_out_drops_lan_session_manager`            |
        |                                     | session manager.                             |                                                       |
        +-------------------------------------+----------------------------------------------+-------------------------------------------------------+
        | out-bytes-lan-compression           | Total bytes sent by compression engine on    | :func:`peek_out_bytes_lan_compression`                |
        |                                     | LAN.                                         |                                                       |
        +-------------------------------------+----------------------------------------------+-------------------------------------------------------+
        | in-tcp-packets                      | Total TCP packets received.                  | :func:`peek_in_tcp_packets`                           |
        |                                     |                                              |                                                       |
        +-------------------------------------+----------------------------------------------+-------------------------------------------------------+
        | tcp-out-of-order-packets            | TCP total out of order packets.              | :func:`peek_tcp_out_of_order_packets`                 |
        |                                     |                                              |                                                       |
        +-------------------------------------+----------------------------------------------+-------------------------------------------------------+
        | end-time                            | Indicates the LAN flow end time.             | :func:`peek_end_time`                                 |
        |                                     |                                              |                                                       |
        +-------------------------------------+----------------------------------------------+-------------------------------------------------------+
        | remote-host-mss                     | The remote-host-mss is the MSS of the TCP    | :func:`peek_remote_host_mss`                          |
        |                                     | connection at peer extension tunnel          |                                                       |
        |                                     | endpoint connected host to its the LAN       |                                                       |
        |                                     | ingress side.                                |                                                       |
        +-------------------------------------+----------------------------------------------+-------------------------------------------------------+
        | protocol                            | Describes that the Layer 4 protocol of the   | :func:`peek_protocol`                                 |
        |                                     | flow.                                        |                                                       |
        +-------------------------------------+----------------------------------------------+-------------------------------------------------------+
        | mapped-tunnel                       | The interface used for extension-tunnel.     | :func:`peek_mapped_tunnel`                            |
        |                                     |                                              |                                                       |
        +-------------------------------------+----------------------------------------------+-------------------------------------------------------+
        | ve-port                             | The VE port of the extension-tunnel          | :func:`peek_mapped_tunnel_ve_port`                    |
        |                                     | interface.                                   |                                                       |
        +-------------------------------------+----------------------------------------------+-------------------------------------------------------+
        | qos                                 | The IP priority QOS associated with the      | :func:`peek_mapped_tunnel_qos`                        |
        |                                     | flow.                                        |                                                       |
        +-------------------------------------+----------------------------------------------+-------------------------------------------------------+

    *Object functions for lan_flow_statistics*

    .. function:: get()

        Get the instances of class "lan_flow_statistics from switch. The
         object can be printed using :func:`pyfos_utils.response_print`.

        :param session: The session handler returned by
         :func:`pyfos_auth.login`.

        :rtype: A dictionary of errors or a success response.


    *Class functions for lan_flow_statistics*

        .. function:: peek_dp_id()

            Reads the value assigned to dp-id in the object.

            :rtype: None on error and a value on success.


        .. function:: set_dp_id(value)

            Set the value of dp-id in the object.

            :rtype: A dictionary of error or a success response and a value
             with "dp-id" as the key


        .. function:: peek_slot()

            Reads the value assigned to slot in the object.

            :rtype: None on error and a value on success.


        .. function:: set_slot(value)

            Set the value of slot in the object.

            :rtype: A dictionary of error or a success response and a value
             with "slot" as the key


        .. function:: peek_flow_index()

            Reads the value assigned to flow-index in the object.

            :rtype: None on error and a value on success.


        .. function:: set_flow_index(value)

            Set the value of flow-index in the object.

            :rtype: A dictionary of error or a success response and a value
             with "flow-index" as the key


        .. function:: peek_out_bytes_wan_compression()

            Reads the value assigned to out-bytes-wan-compression in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_in_packets_lan_session_manager()

            Reads the value assigned to in-packets-lan-session-manager in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_vlan_priority()

            Reads the value assigned to vlan-priority in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_traffic_control_list_name()

            Reads the value assigned to traffic-control-list-name in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_out_bytes_lan_session_manager()

            Reads the value assigned to out-bytes-lan-session-manager in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_tcp_retransmits()

            Reads the value assigned to tcp-retransmits in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_zero_window_count()

            Reads the value assigned to zero-window-count in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_active_flow()

            Reads the value assigned to active-flow in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_in_drops_lan_session_manager()

            Reads the value assigned to in-drops-lan-session-manager in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_destination_port()

            Reads the value assigned to destination-port in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_in_bytes_average()

            Reads the value assigned to in-bytes-average in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_destination_ip_address()

            Reads the value assigned to destination-ip-address in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_in_bytes_lan_session_manager()

            Reads the value assigned to in-bytes-lan-session-manager in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_in_bytes_lan_compression()

            Reads the value assigned to in-bytes-lan-compression in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_out_tcp_packets()

            Reads the value assigned to out-tcp-packets in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_duplicate_acknowledgement()

            Reads the value assigned to duplicate-acknowledgement in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_source_port()

            Reads the value assigned to source-port in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_in_bytes_wan_compression()

            Reads the value assigned to in-bytes-wan-compression in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_in_tcp_bytes()

            Reads the value assigned to in-tcp-bytes in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_vlan_id()

            Reads the value assigned to vlan-id in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_out_packets_lan_session_manager()

            Reads the value assigned to out-packets-lan-session-manager in
             the object.

            :rtype: None on error and a value on success.


        .. function:: peek_zero_window_maximum_duration()

            Reads the value assigned to zero-window-maximum-duration in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_source_ip_address()

            Reads the value assigned to source-ip-address in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_fast_retransmits()

            Reads the value assigned to fast-retransmits in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_rtt()

            Reads the value assigned to rtt in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_hcl_flow()

            Reads the value assigned to hcl-flow in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_dscp()

            Reads the value assigned to dscp in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_crc_errors()

            Reads the value assigned to crc-errors in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_lan_interface()

            Reads the value assigned to lan-interface in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_local_host_mss()

            Reads the value assigned to local-host-mss in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_start_time()

            Reads the value assigned to start-time in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_out_tcp_bytes()

            Reads the value assigned to out-tcp-bytes in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_out_bytes_average()

            Reads the value assigned to out-bytes-average in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_slow_retransmits()

            Reads the value assigned to slow-retransmits in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_out_drops_lan_session_manager()

            Reads the value assigned to out-drops-lan-session-manager in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_out_bytes_lan_compression()

            Reads the value assigned to out-bytes-lan-compression in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_in_tcp_packets()

            Reads the value assigned to in-tcp-packets in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_tcp_out_of_order_packets()

            Reads the value assigned to tcp-out-of-order-packets in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_end_time()

            Reads the value assigned to end-time in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_remote_host_mss()

            Reads the value assigned to remote-host-mss in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_protocol()

            Reads the value assigned to protocol in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_mapped_tunnel()

            Reads the value assigned to mapped-tunnel in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_mapped_tunnel_ve_port()

            Reads the value assigned to ve-port in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_mapped_tunnel_qos()

            Reads the value assigned to qos in the object.

            :rtype: None on error and a value on success.


    """

    def __init__(self, dictvalues=None):

        clsuri = "/rest" + "/running" + "/brocade-extension" +\
                 "/lan-flow-statistics"
        clstype = pyfos_rest_util.rest_obj_type.lan_flow_statistics
        clsver = version.VER_RANGE_900_and_ABOVE
        super().__init__(clstype, clsuri, clsver)

        self.add(pyfos_rest_util.rest_attribute("dp-id", pyfos_type.type_int,
                 None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute("slot", pyfos_type.type_int,
                 None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute("flow-index",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute("out-bytes-wan-compression",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "in-packets-lan-session-manager", pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("vlan-priority",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("traffic-control-list-name",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "out-bytes-lan-session-manager", pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("tcp-retransmits",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("zero-window-count",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("active-flow",
                 pyfos_type.type_bool, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "in-drops-lan-session-manager", pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("destination-port",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("in-bytes-average",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("destination-ip-address",
                 pyfos_type.type_ip_addr, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "in-bytes-lan-session-manager", pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("in-bytes-lan-compression",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("out-tcp-packets",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("duplicate-acknowledgement",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("source-port",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("in-bytes-wan-compression",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("in-tcp-bytes",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("vlan-id",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "out-packets-lan-session-manager", pyfos_type.type_int,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "zero-window-maximum-duration", pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("source-ip-address",
                 pyfos_type.type_ip_addr, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("fast-retransmits",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("rtt", pyfos_type.type_int,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("hcl-flow",
                 pyfos_type.type_bool, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("dscp", pyfos_type.type_int,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("crc-errors",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("lan-interface",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("local-host-mss",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("start-time",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("out-tcp-bytes",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("out-bytes-average",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("slow-retransmits",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "out-drops-lan-session-manager", pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("out-bytes-lan-compression",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("in-tcp-packets",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("tcp-out-of-order-packets",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("end-time",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("remote-host-mss",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("protocol",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("mapped-tunnel",
                 pyfos_type.type_na, dict(),
                 pyfos_rest_util.REST_ATTRIBUTE_CONTAINER_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("ve-port",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
                 ['mapped-tunnel'])
        self.add(pyfos_rest_util.rest_attribute("qos", pyfos_type.type_str,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
                 ['mapped-tunnel'])
        self.load(dictvalues, 1)


class traffic_control_list(pyfos_rest_util.rest_object):

    """Class of traffic_control_list

    *Description traffic_control_list*

        Represents traffic control lists in order to manage IP Extension LAN
        flows.

    Important class members of traffic_control_list:

        +---------------------------------------+------------------------------------------+---------------------------------------------------------+
        | Attribute Name                        | Description                              |  Frequently Used Methods                                |
        +=======================================+==========================================+=========================================================+
        | traffic-control-list-name             | Name of the Traffic-Control-List.        | :func:`peek_traffic_control_list_name`                  |
        |                                       |                                          | :func:`set_traffic_control_list_name`                   |
        +---------------------------------------+------------------------------------------+---------------------------------------------------------+
        | target-ve-port                        | The VE port of the extension-tunnel      | :func:`peek_target_ve_port`                             |
        |                                       | used for allowing a LAN ingress          | :func:`set_target_ve_port`                              |
        |                                       | traffic to be sent over the WAN.         |                                                         |
        +---------------------------------------+------------------------------------------+---------------------------------------------------------+
        | action                                | Set the action for this TCL. The TCL     | :func:`peek_action`                                     |
        |                                       | can be programmed to allow a traffic     | :func:`set_action`                                      |
        |                                       | or deny the traffic.                     |                                                         |
        +---------------------------------------+------------------------------------------+---------------------------------------------------------+
        | segment-preservation-enabled          | Is segment preservation for this TCL     | :func:`peek_segment_preservation_enabled`               |
        |                                       | enabled. Default: false, Values          | :func:`set_segment_preservation_enabled`                |
        |                                       | supported are true/false. false -        |                                                         |
        |                                       | Disabled true - Enabled                  |                                                         |
        +---------------------------------------+------------------------------------------+---------------------------------------------------------+
        | port                                  | The protocol port input filter for       | :func:`peek_port`                                       |
        |                                       | this TCL. The port arguments can be      | :func:`set_port`                                        |
        |                                       | specified as a single port or in case    |                                                         |
        |                                       | of multiple ports a comma separated      |                                                         |
        |                                       | list of ports or else a range of ports   |                                                         |
        |                                       | can be specified or a combination.       |                                                         |
        |                                       | example : 22 or 600-603 or 300,302,305   |                                                         |
        +---------------------------------------+------------------------------------------+---------------------------------------------------------+
        | source-address                        | Source IP address input filter for       | :func:`peek_source_address`                             |
        |                                       | this TCL.                                | :func:`set_source_address`                              |
        +---------------------------------------+------------------------------------------+---------------------------------------------------------+
        | target-slot                           | In case of non-chassis system, the       | :func:`peek_target_slot`                                |
        |                                       | slot number is always 0. In case of      | :func:`set_target_slot`                                 |
        |                                       | chassis system, it is the slot number    |                                                         |
        |                                       | of chassis in which the extension        |                                                         |
        |                                       | blade is inserted in. In case of         |                                                         |
        |                                       | chassis, slot number is non-zero         |                                                         |
        |                                       | value.                                   |                                                         |
        +---------------------------------------+------------------------------------------+---------------------------------------------------------+
        | target-dp-id                          | Extension Data Path Processor ID.        | :func:`peek_target_dp_id`                               |
        |                                       | Based on platform either it will have    | :func:`set_target_dp_id`                                |
        |                                       | a single DP or dual DP. In case of       |                                                         |
        |                                       | single DP only DP0 is supported, and     |                                                         |
        |                                       | in case of dual DP both DP0 and DP1      |                                                         |
        |                                       | are supported 0 : DP0 1 : DP1.           |                                                         |
        +---------------------------------------+------------------------------------------+---------------------------------------------------------+
        | l4-protocol                           | The Layer 4 protocol input filter for    | :func:`peek_l4_protocol`                                |
        |                                       | this TCL. The value can be a well        | :func:`set_l4_protocol`                                 |
        |                                       | known protocol string value or           |                                                         |
        |                                       | otherwise a L4 protocol number. The      |                                                         |
        |                                       | 'any' protocol string is the default     |                                                         |
        |                                       | value and is meant to match any L4       |                                                         |
        |                                       | protocol value. The valid range for L4   |                                                         |
        |                                       | protocol is from 0-255. The list of      |                                                         |
        |                                       | known protocol string values from        |                                                         |
        |                                       | system are as below: ICMP ICMP6 TCP      |                                                         |
        |                                       | UDP VRRP                                 |                                                         |
        +---------------------------------------+------------------------------------------+---------------------------------------------------------+
        | target-qos                            | QoS priority associated with an          | :func:`peek_target_qos`                                 |
        |                                       | extension-tunnel to be used to allow a   | :func:`set_target_qos`                                  |
        |                                       | LAN ingress traffic over WAN.            |                                                         |
        +---------------------------------------+------------------------------------------+---------------------------------------------------------+
        | reset-propagation-enabled             | Is End to End reset propagation for      | :func:`peek_reset_propagation_enabled`                  |
        |                                       | this TCL enabled. Default: false,        | :func:`set_reset_propagation_enabled`                   |
        |                                       | Values supported are true/false. false   |                                                         |
        |                                       | - Disabled true - Enabled                |                                                         |
        +---------------------------------------+------------------------------------------+---------------------------------------------------------+
        | source-address-prefix-length          | The prefix length operator for source    | :func:`peek_source_address_prefix_length`               |
        |                                       | IP address input filter.                 | :func:`set_source_address_prefix_length`                |
        +---------------------------------------+------------------------------------------+---------------------------------------------------------+
        | application                           | The application input filter for this    | :func:`peek_application`                                |
        |                                       | TCL. This includes a list of known       | :func:`set_application`                                 |
        |                                       | apps already present or a user defined   |                                                         |
        |                                       | app-type name. The 'any' application     |                                                         |
        |                                       | type name is a special value to          |                                                         |
        |                                       | identify any application. Below are      |                                                         |
        |                                       | few examples of system defined known     |                                                         |
        |                                       | application types: CIFS Data-Domain      |                                                         |
        |                                       | FCIP FTP HTTP HTTPS                      |                                                         |
        +---------------------------------------+------------------------------------------+---------------------------------------------------------+
        | destination-address-prefix-length     | The prefix length operator for           | :func:`peek_destination_address_prefix_length`          |
        |                                       | destination IP address input filter.     | :func:`set_destination_address_prefix_length`           |
        +---------------------------------------+------------------------------------------+---------------------------------------------------------+
        | dscp                                  | The DSCP input filter for this TCL.      | :func:`peek_dscp`                                       |
        |                                       | The values supported are from 0-63.      | :func:`set_dscp`                                        |
        |                                       | The value 'any' is default value and     |                                                         |
        |                                       | is meant to match any dscp value         |                                                         |
        |                                       | specified.                               |                                                         |
        +---------------------------------------+------------------------------------------+---------------------------------------------------------+
        | vlan                                  | The VLAN input filter for this TCL.      | :func:`peek_vlan`                                       |
        |                                       | The values supported are from 1-4095.    | :func:`set_vlan`                                        |
        |                                       | The value 'any' is the default value     |                                                         |
        |                                       | and is meant to match any vlan-id        |                                                         |
        |                                       | value specified.                         |                                                         |
        +---------------------------------------+------------------------------------------+---------------------------------------------------------+
        | l2cos                                 | The L2CoS input filter for this TCL.     | :func:`peek_l2cos`                                      |
        |                                       | The valid values are from 0-7. The       | :func:`set_l2cos`                                       |
        |                                       | value 'any' is the default value and     |                                                         |
        |                                       | is meant to match any value of l2CoS.    |                                                         |
        +---------------------------------------+------------------------------------------+---------------------------------------------------------+
        | destination-address                   | Destination IP address input filter      | :func:`peek_destination_address`                        |
        |                                       | for this TCL.                            | :func:`set_destination_address`                         |
        +---------------------------------------+------------------------------------------+---------------------------------------------------------+
        | admin-state-enabled                   | Is TCL admin status enabled. Default:    | :func:`peek_admin_state_enabled`                        |
        |                                       | false, Values supported are              | :func:`set_admin_state_enabled`                         |
        |                                       | true/false. false - Disabled true -      |                                                         |
        |                                       | Enabled                                  |                                                         |
        +---------------------------------------+------------------------------------------+---------------------------------------------------------+
        | priority                              | TCL priority provides an order of        | :func:`peek_priority`                                   |
        |                                       | precedence to the TCL rule within the    | :func:`set_priority`                                    |
        |                                       | overall TCL list. The priority 65535     |                                                         |
        |                                       | is a special priority associated or      |                                                         |
        |                                       | applicable to only the default TCL       |                                                         |
        |                                       | rule and no other user configured TCL    |                                                         |
        |                                       | is allowed this value. The priority 0    |                                                         |
        |                                       | is a also treated as a special           |                                                         |
        |                                       | priority and is only to indicate that    |                                                         |
        |                                       | the priority is not set. A valid user    |                                                         |
        |                                       | configured TCL priority must use a       |                                                         |
        |                                       | value from 1 to 65534 only.              |                                                         |
        +---------------------------------------+------------------------------------------+---------------------------------------------------------+
        | non-terminated-enabled                | Is non terminated traffic for this TCL   | :func:`peek_non_terminated_enabled`                     |
        |                                       | enabled. Default: false, Values          | :func:`set_non_terminated_enabled`                      |
        |                                       | supported are true/false. false -        |                                                         |
        |                                       | Disabled true - Enabled                  |                                                         |
        +---------------------------------------+------------------------------------------+---------------------------------------------------------+
        | hit-count                             | Total number of times this TCL rule      | :func:`peek_hit_count`                                  |
        |                                       | was hit.                                 |                                                         |
        +---------------------------------------+------------------------------------------+---------------------------------------------------------+
        | cp-dp-synchronized                    | Indicates whether an                     | :func:`peek_cp_dp_synchronized`                         |
        |                                       | admin-statatus-enabled TCL is            |                                                         |
        |                                       | synchronized between the CP->DP. In      |                                                         |
        |                                       | case of error the value will be set to   |                                                         |
        |                                       | false false - CP-DP synchronizing        |                                                         |
        |                                       | failed. true - CP-DP is synchronized.    |                                                         |
        +---------------------------------------+------------------------------------------+---------------------------------------------------------+

    *Object functions for traffic_control_list*

    .. function:: get()

        Get the instances of class "traffic_control_list from switch. The
         object can be printed using :func:`pyfos_utils.response_print`.

        :param session: The session handler returned by
         :func:`pyfos_auth.login`.

        :rtype: A dictionary of errors or a success response.


    *Class functions for traffic_control_list*

        .. function:: peek_traffic_control_list_name()

            Reads the value assigned to traffic-control-list-name in the
             object.

            :rtype: None on error and a value on success.


        .. function:: set_traffic_control_list_name(value)

            Set the value of traffic-control-list-name in the object.

            :rtype: A dictionary of error or a success response and a value
             with "traffic-control-list-name" as the key


        .. function:: peek_target_ve_port()

            Reads the value assigned to target-ve-port in the object.

            :rtype: None on error and a value on success.


        .. function:: set_target_ve_port(value)

            Set the value of target-ve-port in the object.

            :rtype: A dictionary of error or a success response and a value
             with "target-ve-port" as the key


        .. function:: peek_action()

            Reads the value assigned to action in the object.

            :rtype: None on error and a value on success.


        .. function:: set_action(value)

            Set the value of action in the object.

            :rtype: A dictionary of error or a success response and a value
             with "action" as the key


        .. function:: peek_segment_preservation_enabled()

            Reads the value assigned to segment-preservation-enabled in the
             object.

            :rtype: None on error and a value on success.


        .. function:: set_segment_preservation_enabled(value)

            Set the value of segment-preservation-enabled in the object.

            :rtype: A dictionary of error or a success response and a value
             with "segment-preservation-enabled" as the key


        .. function:: peek_port()

            Reads the value assigned to port in the object.

            :rtype: None on error and a value on success.


        .. function:: set_port(value)

            Set the value of port in the object.

            :rtype: A dictionary of error or a success response and a value
             with "port" as the key


        .. function:: peek_source_address()

            Reads the value assigned to source-address in the object.

            :rtype: None on error and a value on success.


        .. function:: set_source_address(value)

            Set the value of source-address in the object.

            :rtype: A dictionary of error or a success response and a value
             with "source-address" as the key


        .. function:: peek_target_slot()

            Reads the value assigned to target-slot in the object.

            :rtype: None on error and a value on success.


        .. function:: set_target_slot(value)

            Set the value of target-slot in the object.

            :rtype: A dictionary of error or a success response and a value
             with "target-slot" as the key


        .. function:: peek_target_dp_id()

            Reads the value assigned to target-dp-id in the object.

            :rtype: None on error and a value on success.


        .. function:: set_target_dp_id(value)

            Set the value of target-dp-id in the object.

            :rtype: A dictionary of error or a success response and a value
             with "target-dp-id" as the key


        .. function:: peek_l4_protocol()

            Reads the value assigned to l4-protocol in the object.

            :rtype: None on error and a value on success.


        .. function:: set_l4_protocol(value)

            Set the value of l4-protocol in the object.

            :rtype: A dictionary of error or a success response and a value
             with "l4-protocol" as the key


        .. function:: peek_target_qos()

            Reads the value assigned to target-qos in the object.

            :rtype: None on error and a value on success.


        .. function:: set_target_qos(value)

            Set the value of target-qos in the object.

            :rtype: A dictionary of error or a success response and a value
             with "target-qos" as the key


        .. function:: peek_reset_propagation_enabled()

            Reads the value assigned to reset-propagation-enabled in the
             object.

            :rtype: None on error and a value on success.


        .. function:: set_reset_propagation_enabled(value)

            Set the value of reset-propagation-enabled in the object.

            :rtype: A dictionary of error or a success response and a value
             with "reset-propagation-enabled" as the key


        .. function:: peek_source_address_prefix_length()

            Reads the value assigned to source-address-prefix-length in the
             object.

            :rtype: None on error and a value on success.


        .. function:: set_source_address_prefix_length(value)

            Set the value of source-address-prefix-length in the object.

            :rtype: A dictionary of error or a success response and a value
             with "source-address-prefix-length" as the key


        .. function:: peek_application()

            Reads the value assigned to application in the object.

            :rtype: None on error and a value on success.


        .. function:: set_application(value)

            Set the value of application in the object.

            :rtype: A dictionary of error or a success response and a value
             with "application" as the key


        .. function:: peek_destination_address_prefix_length()

            Reads the value assigned to destination-address-prefix-length in
             the object.

            :rtype: None on error and a value on success.


        .. function:: set_destination_address_prefix_length(value)

            Set the value of destination-address-prefix-length in the
             object.

            :rtype: A dictionary of error or a success response and a value
             with "destination-address-prefix-length" as the key


        .. function:: peek_dscp()

            Reads the value assigned to dscp in the object.

            :rtype: None on error and a value on success.


        .. function:: set_dscp(value)

            Set the value of dscp in the object.

            :rtype: A dictionary of error or a success response and a value
             with "dscp" as the key


        .. function:: peek_vlan()

            Reads the value assigned to vlan in the object.

            :rtype: None on error and a value on success.


        .. function:: set_vlan(value)

            Set the value of vlan in the object.

            :rtype: A dictionary of error or a success response and a value
             with "vlan" as the key


        .. function:: peek_l2cos()

            Reads the value assigned to l2cos in the object.

            :rtype: None on error and a value on success.


        .. function:: set_l2cos(value)

            Set the value of l2cos in the object.

            :rtype: A dictionary of error or a success response and a value
             with "l2cos" as the key


        .. function:: peek_destination_address()

            Reads the value assigned to destination-address in the object.

            :rtype: None on error and a value on success.


        .. function:: set_destination_address(value)

            Set the value of destination-address in the object.

            :rtype: A dictionary of error or a success response and a value
             with "destination-address" as the key


        .. function:: peek_admin_state_enabled()

            Reads the value assigned to admin-state-enabled in the object.

            :rtype: None on error and a value on success.


        .. function:: set_admin_state_enabled(value)

            Set the value of admin-state-enabled in the object.

            :rtype: A dictionary of error or a success response and a value
             with "admin-state-enabled" as the key


        .. function:: peek_priority()

            Reads the value assigned to priority in the object.

            :rtype: None on error and a value on success.


        .. function:: set_priority(value)

            Set the value of priority in the object.

            :rtype: A dictionary of error or a success response and a value
             with "priority" as the key


        .. function:: peek_non_terminated_enabled()

            Reads the value assigned to non-terminated-enabled in the
             object.

            :rtype: None on error and a value on success.


        .. function:: set_non_terminated_enabled(value)

            Set the value of non-terminated-enabled in the object.

            :rtype: A dictionary of error or a success response and a value
             with "non-terminated-enabled" as the key


        .. function:: peek_hit_count()

            Reads the value assigned to hit-count in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_cp_dp_synchronized()

            Reads the value assigned to cp-dp-synchronized in the object.

            :rtype: None on error and a value on success.


    """

    def __init__(self, dictvalues=None):

        clsuri = "/rest" + "/running" + "/brocade-extension" +\
                 "/traffic-control-list"
        clstype = pyfos_rest_util.rest_obj_type.traffic_control_list
        clsver = version.VER_RANGE_900_and_ABOVE
        super().__init__(clstype, clsuri, clsver)

        self.add(pyfos_rest_util.rest_attribute("traffic-control-list-name",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute("target-ve-port",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("action", pyfos_type.type_str,
                 None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "segment-preservation-enabled", pyfos_type.type_bool, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("port", pyfos_type.type_str,
                 None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("source-address",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("target-slot",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("target-dp-id",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("l4-protocol",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("target-qos",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("reset-propagation-enabled",
                 pyfos_type.type_bool, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "source-address-prefix-length", pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("application",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "destination-address-prefix-length", pyfos_type.type_int,
                 None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("dscp", pyfos_type.type_str,
                 None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("vlan", pyfos_type.type_str,
                 None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("l2cos", pyfos_type.type_str,
                 None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("destination-address",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("admin-state-enabled",
                 pyfos_type.type_bool, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("priority",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("non-terminated-enabled",
                 pyfos_type.type_bool, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("hit-count",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("cp-dp-synchronized",
                 pyfos_type.type_bool, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.load(dictvalues, 1)


class dp_hcl_status(pyfos_rest_util.rest_object):

    """Class of dp_hcl_status

    *Description dp_hcl_status*

        Represents the HCL status on extension datapath process.

    Important class members of dp_hcl_status:

        +-----------------------------+------------------------------+-------------------------------------------------+
        | Attribute Name              | Description                  |  Frequently Used Methods                        |
        +=============================+==============================+=================================================+
        | dp-id                       | Extension Data Path          | :func:`peek_dp_id`                              |
        |                             | Processor ID. Based on       | :func:`set_dp_id`                               |
        |                             | platform either it will      |                                                 |
        |                             | have a single DP or dual     |                                                 |
        |                             | DP. In case of single DP     |                                                 |
        |                             | only DP0 is supported, and   |                                                 |
        |                             | in case of dual DP both      |                                                 |
        |                             | DP0 and DP1 are supported    |                                                 |
        |                             | 0 : DP0 1 : DP1.             |                                                 |
        +-----------------------------+------------------------------+-------------------------------------------------+
        | slot                        | The slot number of for the   | :func:`peek_slot`                               |
        |                             | datapath processor.          | :func:`set_slot`                                |
        +-----------------------------+------------------------------+-------------------------------------------------+
        | ip-hcl-stage                | The current DP HCL stage     | :func:`peek_ip_hcl_stage`                       |
        |                             | for IP protocol.             |                                                 |
        +-----------------------------+------------------------------+-------------------------------------------------+
        | firmware-version            | A human readable string      | :func:`peek_firmware_version`                   |
        |                             | identifying the firmware     |                                                 |
        |                             | version running on the       |                                                 |
        |                             | datapath process of the      |                                                 |
        |                             | switch/blade.                |                                                 |
        +-----------------------------+------------------------------+-------------------------------------------------+
        | state                       | The current DP HCL state     | :func:`peek_state`                              |
        |                             |                              |                                                 |
        +-----------------------------+------------------------------+-------------------------------------------------+
        | svi-swapped                 | Is the SVI swapped for HCL   | :func:`peek_svi_swapped`                        |
        |                             | processing                   |                                                 |
        +-----------------------------+------------------------------+-------------------------------------------------+
        | dp-communication-status     | The current state of DP-DP   | :func:`peek_dp_communication_status`            |
        |                             | communication                |                                                 |
        +-----------------------------+------------------------------+-------------------------------------------------+
        | status                      | The current DP status.       | :func:`peek_status`                             |
        |                             |                              |                                                 |
        +-----------------------------+------------------------------+-------------------------------------------------+
        | fc-hcl-stage                | The current DP HCL stage     | :func:`peek_fc_hcl_stage`                       |
        |                             | for FC protocol.             |                                                 |
        +-----------------------------+------------------------------+-------------------------------------------------+

    *Object functions for dp_hcl_status*

    .. function:: get()

        Get the instances of class "dp_hcl_status from switch. The object can
         be printed using :func:`pyfos_utils.response_print`.

        :param session: The session handler returned by
         :func:`pyfos_auth.login`.

        :rtype: A dictionary of errors or a success response.


    *Class functions for dp_hcl_status*

        .. function:: peek_dp_id()

            Reads the value assigned to dp-id in the object.

            :rtype: None on error and a value on success.


        .. function:: set_dp_id(value)

            Set the value of dp-id in the object.

            :rtype: A dictionary of error or a success response and a value
             with "dp-id" as the key


        .. function:: peek_slot()

            Reads the value assigned to slot in the object.

            :rtype: None on error and a value on success.


        .. function:: set_slot(value)

            Set the value of slot in the object.

            :rtype: A dictionary of error or a success response and a value
             with "slot" as the key


        .. function:: peek_ip_hcl_stage()

            Reads the value assigned to ip-hcl-stage in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_firmware_version()

            Reads the value assigned to firmware-version in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_state()

            Reads the value assigned to state in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_svi_swapped()

            Reads the value assigned to svi-swapped in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_dp_communication_status()

            Reads the value assigned to dp-communication-status in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_status()

            Reads the value assigned to status in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_fc_hcl_stage()

            Reads the value assigned to fc-hcl-stage in the object.

            :rtype: None on error and a value on success.


    """

    def __init__(self, dictvalues=None):

        clsuri = "/rest" + "/running" + "/brocade-extension" +\
                 "/dp-hcl-status"
        clstype = pyfos_rest_util.rest_obj_type.dp_hcl_status
        clsver = version.VER_RANGE_900_and_ABOVE
        super().__init__(clstype, clsuri, clsver)

        self.add(pyfos_rest_util.rest_attribute("dp-id", pyfos_type.type_int,
                 None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute("slot", pyfos_type.type_int,
                 None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute("ip-hcl-stage",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("firmware-version",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("state", pyfos_type.type_str,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("svi-swapped",
                 pyfos_type.type_bool, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("dp-communication-status",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("status", pyfos_type.type_str,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("fc-hcl-stage",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.load(dictvalues, 1)
