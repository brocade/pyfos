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


# wan_statistics_show.py(pyGen v1.0.0)


"""

:mod:`wan_statistics_show` - PyFOS util to show for wan_statistics
*******************************************************************************
The:mod:`wan_statistics_show` PyFOS util to show for wan_statistics


Represents TCP WAN statistics for extension blade or system.

wan_statistics_show: usage

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
    * --priority=PRIORITY: QOS Priority value for the tunnel
    *\
      --out-unacknowledged-packets-sequence=OUT-UNACKNOWLEDGED-PACKETS-\
      SEQUENCE: Source unacknowledged packets sequence.
    * --in-queued-packets-next-sequence=IN-QUEUED-PACKETS-NEXT-SEQUENCE: TCP\
      queued packets next sequence number received.
    * --slow-starts=SLOW-STARTS: TCP slow starts.
    *\
      --out-queued-packets-minimum-sequence=OUT-QUEUED-PACKETS-MINIMUM-\
      SEQUENCE: Source TCP queued packets minimum sequence number.
    * --in-window-size=IN-WINDOW-SIZE: Receiver window size.
    * --in-queued-packets-minimum-sequence=IN-QUEUED-PACKETS-MINIMUM-SEQUENCE:\
      TCP queued packets minimum sequence number received.
    * --out-packets=OUT-PACKETS: Total TCP packets sent.
    * --connection-id=CONNECTION-ID: TCP connection identifier associated with\
      the WAN TCP connection. The TCP connection identifier may change in\
      case of connection going down or establishment. These are not\
      persistent identifiers associated with the connection.
    * --in-window-size-maximum=IN-WINDOW-SIZE-MAXIMUM: Receiver maximum window\
      size.
    * --operation-mode=OPERATION-MODE: TCP operation mode algorithm used for\
      connection.
    * --arl-current=ARL-CURRENT: ARL current value
    * --out-queued-packets-next-sequence=OUT-QUEUED-PACKETS-NEXT-SEQUENCE:\
      Source TCP queued packets next sequence number.
    * --fast-retransmits=FAST-RETRANSMITS: TCP fast retransmits
    * --slow-retransmits=SLOW-RETRANSMITS: TCP slow retransmits
    * --in-packets=IN-PACKETS: Total TCP packets received.
    *\
      --out-queued-packets-maximum-sequence=OUT-QUEUED-PACKETS-MAXIMUM-\
      SEQUENCE: Source TCP queued packets maximum sequence number.
    * --out-window-size=OUT-WINDOW-SIZE: Source window size.
    * --in-queued-out-of-order=IN-QUEUED-OUT-OF-ORDER: TCP queued out of order\
      packets received.
    * --arl-next-reset-algorithm=ARL-NEXT-RESET-ALGORITHM: ARL next reset\
      algorithm.
    * --circuit-id=CIRCUIT-ID: Circuit identifier.
    * --rtt-variance=RTT-VARIANCE: variance in round trip time.
    * --in-bytes=IN-BYTES: Total bytes received.
    * --maximum-fast-retransmits=MAXIMUM-FAST-RETRANSMITS: TCP maximum fast\
      retransmits
    * --source-port=SOURCE-PORT: TCP source port number
    * --destination-port=DESTINATION-PORT: TCP remote destination port number
    * --retransmits=RETRANSMITS: TCP retransmits
    * --in-queued-out-of-order-maximum=IN-QUEUED-OUT-OF-ORDER-MAXIMUM: TCP\
      total out of order packets received.
    * --rtt-maximum=RTT-MAXIMUM: maximum round trip time.
    * --retransmit-timeout=RETRANSMIT-TIMEOUT: TCP retransmits timeout
    * --duplicate-acknowledgement=DUPLICATE-ACKNOWLEDGEMENT: TCP duplicate\
      acknowledgement received.
    * --out-in-flight-packets=OUT-IN-FLIGHT-PACKETS: Source in flight packets.
    * --maximum-retransmits=MAXIMUM-RETRANSMITS: TCP maximum retransmits
    * --in-queued-out-of-order-total=IN-QUEUED-OUT-OF-ORDER-TOTAL: TCP total\
      out of order packets received.
    * --connection-mss=CONNECTION-MSS: TCP connection MSS.
    * --rtt=RTT: round trip time.
    * --ve-port=VE-PORT: The name of the interface.
    * --arl-maximum=ARL-MAXIMUM: ARL maximum value
    * --in-queued-packets-maximum-sequence=IN-QUEUED-PACKETS-MAXIMUM-SEQUENCE:\
      TCP queued packets maximum sequence number received.
    * --out-bytes=OUT-BYTES: Total bytes sent.
    * --in-window-scale=IN-WINDOW-SCALE: Receiver negotiated window scale.
    * --congestion-window=CONGESTION-WINDOW: The congestion window is the\
      maximum data that can be sent before an ACK is received.
    * --in-queued-packets=IN-QUEUED-PACKETS: TCP queued packets received.
    * --out-window-scale=OUT-WINDOW-SCALE: Source window scaling shift count.
    * --rtt-variance-maximum=RTT-VARIANCE-MAXIMUM: Maximum variance in round\
      trip time.
    * --arl-minimum=ARL-MINIMUM: ARL minimum value
    * --slow-start-threshold=SLOW-START-THRESHOLD: Source slow start\
      threshold.
    * --ha-type=HA-TYPE: Tunnel HA type configuration.
* Output:
    * Python dictionary content with RESTCONF response data.


.. function:: wan_statistics_show.show_wan_statistics(session, priority,\
out_unacknowledged_packets_sequence, in_queued_packets_next_sequence,\
slow_starts, out_queued_packets_minimum_sequence, in_window_size,\
in_queued_packets_minimum_sequence, out_packets, connection_id,\
in_window_size_maximum, operation_mode, arl_current,\
out_queued_packets_next_sequence, fast_retransmits, slow_retransmits,\
in_packets, out_queued_packets_maximum_sequence, out_window_size,\
in_queued_out_of_order, arl_next_reset_algorithm, circuit_id, rtt_variance,\
in_bytes, maximum_fast_retransmits, source_port, destination_port,\
retransmits, in_queued_out_of_order_maximum, rtt_maximum,\
retransmit_timeout, duplicate_acknowledgement, out_in_flight_packets,\
maximum_retransmits, in_queued_out_of_order_total, connection_mss, rtt,\
ve_port, arl_maximum, in_queued_packets_maximum_sequence, out_bytes,\
in_window_scale, congestion_window, in_queued_packets, out_window_scale,\
rtt_variance_maximum, arl_minimum, slow_start_threshold, ha_type)

    *Show wan_statistics*

    Example Usage of the Method::

            ret = wan_statistics_show.show_wan_statistics(session, priority,\
 out_unacknowledged_packets_sequence, in_queued_packets_next_sequence,\
 slow_starts, out_queued_packets_minimum_sequence, in_window_size,\
 in_queued_packets_minimum_sequence, out_packets, connection_id,\
 in_window_size_maximum, operation_mode, arl_current,\
 out_queued_packets_next_sequence, fast_retransmits, slow_retransmits,\
 in_packets, out_queued_packets_maximum_sequence, out_window_size,\
 in_queued_out_of_order, arl_next_reset_algorithm, circuit_id, rtt_variance,\
 in_bytes, maximum_fast_retransmits, source_port, destination_port,\
 retransmits, in_queued_out_of_order_maximum, rtt_maximum,\
 retransmit_timeout, duplicate_acknowledgement, out_in_flight_packets,\
 maximum_retransmits, in_queued_out_of_order_total, connection_mss, rtt,\
 ve_port, arl_maximum, in_queued_packets_maximum_sequence, out_bytes,\
 in_window_scale, congestion_window, in_queued_packets, out_window_scale,\
 rtt_variance_maximum, arl_minimum, slow_start_threshold, ha_type)
            print(ret)

    Details::

        wan_statisticsObj = wan_statistics()
        wan_statisticsObj.set_priority(priority)
       \
 wan_statisticsObj.set_out_unacknowledged_packets_sequence(\
 out_unacknowledged_packets_sequence)
       \
 wan_statisticsObj.set_in_queued_packets_next_sequence(\
 in_queued_packets_next_sequence)
        wan_statisticsObj.set_slow_starts(slow_starts)
       \
 wan_statisticsObj.set_out_queued_packets_minimum_sequence(\
 out_queued_packets_minimum_sequence)
        wan_statisticsObj.set_in_window_size(in_window_size)
       \
 wan_statisticsObj.set_in_queued_packets_minimum_sequence(\
 in_queued_packets_minimum_sequence)
        wan_statisticsObj.set_out_packets(out_packets)
        wan_statisticsObj.set_connection_id(connection_id)
        wan_statisticsObj.set_in_window_size_maximum(in_window_size_maximum)
        wan_statisticsObj.set_operation_mode(operation_mode)
        wan_statisticsObj.set_arl_current(arl_current)
       \
 wan_statisticsObj.set_out_queued_packets_next_sequence(\
 out_queued_packets_next_sequence)
        wan_statisticsObj.set_fast_retransmits(fast_retransmits)
        wan_statisticsObj.set_slow_retransmits(slow_retransmits)
        wan_statisticsObj.set_in_packets(in_packets)
       \
 wan_statisticsObj.set_out_queued_packets_maximum_sequence(\
 out_queued_packets_maximum_sequence)
        wan_statisticsObj.set_out_window_size(out_window_size)
        wan_statisticsObj.set_in_queued_out_of_order(in_queued_out_of_order)
       \
 wan_statisticsObj.set_arl_next_reset_algorithm(arl_next_reset_algorithm)
        wan_statisticsObj.set_circuit_id(circuit_id)
        wan_statisticsObj.set_rtt_variance(rtt_variance)
        wan_statisticsObj.set_in_bytes(in_bytes)
       \
 wan_statisticsObj.set_maximum_fast_retransmits(maximum_fast_retransmits)
        wan_statisticsObj.set_source_port(source_port)
        wan_statisticsObj.set_destination_port(destination_port)
        wan_statisticsObj.set_retransmits(retransmits)
       \
 wan_statisticsObj.set_in_queued_out_of_order_maximum(\
 in_queued_out_of_order_maximum)
        wan_statisticsObj.set_rtt_maximum(rtt_maximum)
        wan_statisticsObj.set_retransmit_timeout(retransmit_timeout)
       \
 wan_statisticsObj.set_duplicate_acknowledgement(duplicate_acknowledgement)
        wan_statisticsObj.set_out_in_flight_packets(out_in_flight_packets)
        wan_statisticsObj.set_maximum_retransmits(maximum_retransmits)
       \
 wan_statisticsObj.set_in_queued_out_of_order_total(\
 in_queued_out_of_order_total)
        wan_statisticsObj.set_connection_mss(connection_mss)
        wan_statisticsObj.set_rtt(rtt)
        wan_statisticsObj.set_ve_port(ve_port)
        wan_statisticsObj.set_arl_maximum(arl_maximum)
       \
 wan_statisticsObj.set_in_queued_packets_maximum_sequence(\
 in_queued_packets_maximum_sequence)
        wan_statisticsObj.set_out_bytes(out_bytes)
        wan_statisticsObj.set_in_window_scale(in_window_scale)
        wan_statisticsObj.set_congestion_window(congestion_window)
        wan_statisticsObj.set_in_queued_packets(in_queued_packets)
        wan_statisticsObj.set_out_window_scale(out_window_scale)
        wan_statisticsObj.set_rtt_variance_maximum(rtt_variance_maximum)
        wan_statisticsObj.set_arl_minimum(arl_minimum)
        wan_statisticsObj.set_slow_start_threshold(slow_start_threshold)
        wan_statisticsObj.set_ha_type(ha_type)
        ret = _show_wan_statistics(session, wan_statisticsObj)
        print(ret)

    **Inputs**

    :param session: The session returned by the login.
    :param priority: QOS Priority value for the tunnel
    :param out_unacknowledged_packets_sequence: Source unacknowledged packets\
      sequence.
    :param in_queued_packets_next_sequence: TCP queued packets next sequence\
      number received.
    :param slow_starts: TCP slow starts.
    :param out_queued_packets_minimum_sequence: Source TCP queued packets\
      minimum sequence number.
    :param in_window_size: Receiver window size.
    :param in_queued_packets_minimum_sequence: TCP queued packets minimum\
      sequence number received.
    :param out_packets: Total TCP packets sent.
    :param connection_id: TCP connection identifier associated with the WAN\
      TCP connection. The TCP connection identifier may change in case of\
      connection going down or establishment. These are not persistent\
      identifiers associated with the connection.
    :param in_window_size_maximum: Receiver maximum window size.
    :param operation_mode: TCP operation mode algorithm used for connection.
    :param arl_current: ARL current value
    :param out_queued_packets_next_sequence: Source TCP queued packets next\
      sequence number.
    :param fast_retransmits: TCP fast retransmits
    :param slow_retransmits: TCP slow retransmits
    :param in_packets: Total TCP packets received.
    :param out_queued_packets_maximum_sequence: Source TCP queued packets\
      maximum sequence number.
    :param out_window_size: Source window size.
    :param in_queued_out_of_order: TCP queued out of order packets received.
    :param arl_next_reset_algorithm: ARL next reset algorithm.
    :param circuit_id: Circuit identifier.
    :param rtt_variance: variance in round trip time.
    :param in_bytes: Total bytes received.
    :param maximum_fast_retransmits: TCP maximum fast retransmits
    :param source_port: TCP source port number
    :param destination_port: TCP remote destination port number
    :param retransmits: TCP retransmits
    :param in_queued_out_of_order_maximum: TCP total out of order packets\
      received.
    :param rtt_maximum: maximum round trip time.
    :param retransmit_timeout: TCP retransmits timeout
    :param duplicate_acknowledgement: TCP duplicate acknowledgement received.
    :param out_in_flight_packets: Source in flight packets.
    :param maximum_retransmits: TCP maximum retransmits
    :param in_queued_out_of_order_total: TCP total out of order packets\
      received.
    :param connection_mss: TCP connection MSS.
    :param rtt: round trip time.
    :param ve_port: The name of the interface.
    :param arl_maximum: ARL maximum value
    :param in_queued_packets_maximum_sequence: TCP queued packets maximum\
      sequence number received.
    :param out_bytes: Total bytes sent.
    :param in_window_scale: Receiver negotiated window scale.
    :param congestion_window: The congestion window is the maximum data that\
      can be sent before an ACK is received.
    :param in_queued_packets: TCP queued packets received.
    :param out_window_scale: Source window scaling shift count.
    :param rtt_variance_maximum: Maximum variance in round trip time.
    :param arl_minimum: ARL minimum value
    :param slow_start_threshold: Source slow start threshold.
    :param ha_type: Tunnel HA type configuration.

    **Output**

    :rtype: None or one/more instance of class wan_statistics on Success  or a\
    dictionary with error.

"""


# Start utils imports
import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_extension_tunnel import wan_statistics

from pyfos.utils import brcd_util
# End module imports


def _show_wan_statistics(session, wan_statisticsObj):
    objlist = wan_statistics.get(session)
    wan_statisticslist = list()
    if isinstance(objlist, wan_statistics):
        objlist = [objlist]
    if isinstance(objlist, list):
        for i in range(len(objlist)):
            if wan_statisticsObj.peek_priority() is not None and\
               wan_statisticsObj.peek_priority() !=\
               objlist[i].peek_priority():
                continue
            if wan_statisticsObj.peek_out_unacknowledged_packets_sequence() is\
               not None and\
               wan_statisticsObj.peek_out_unacknowledged_packets_sequence()\
               != objlist[i].peek_out_unacknowledged_packets_sequence():
                continue
            if wan_statisticsObj.peek_in_queued_packets_next_sequence() is not\
               None and\
               wan_statisticsObj.peek_in_queued_packets_next_sequence() !=\
               objlist[i].peek_in_queued_packets_next_sequence():
                continue
            if wan_statisticsObj.peek_slow_starts() is not None and\
               wan_statisticsObj.peek_slow_starts() !=\
               objlist[i].peek_slow_starts():
                continue
            if wan_statisticsObj.peek_out_queued_packets_minimum_sequence() is\
               not None and\
               wan_statisticsObj.peek_out_queued_packets_minimum_sequence()\
               != objlist[i].peek_out_queued_packets_minimum_sequence():
                continue
            if wan_statisticsObj.peek_in_window_size() is not None and\
               wan_statisticsObj.peek_in_window_size() !=\
               objlist[i].peek_in_window_size():
                continue
            if wan_statisticsObj.peek_in_queued_packets_minimum_sequence() is\
               not None and\
               wan_statisticsObj.peek_in_queued_packets_minimum_sequence()\
               != objlist[i].peek_in_queued_packets_minimum_sequence():
                continue
            if wan_statisticsObj.peek_out_packets() is not None and\
               wan_statisticsObj.peek_out_packets() !=\
               objlist[i].peek_out_packets():
                continue
            if wan_statisticsObj.peek_connection_id() is not None and\
               wan_statisticsObj.peek_connection_id() !=\
               objlist[i].peek_connection_id():
                continue
            if wan_statisticsObj.peek_in_window_size_maximum() is not None and\
               wan_statisticsObj.peek_in_window_size_maximum() !=\
               objlist[i].peek_in_window_size_maximum():
                continue
            if wan_statisticsObj.peek_operation_mode() is not None and\
               wan_statisticsObj.peek_operation_mode() !=\
               objlist[i].peek_operation_mode():
                continue
            if wan_statisticsObj.peek_arl_current() is not None and\
               wan_statisticsObj.peek_arl_current() !=\
               objlist[i].peek_arl_current():
                continue
            if wan_statisticsObj.peek_out_queued_packets_next_sequence() is\
               not None and\
               wan_statisticsObj.peek_out_queued_packets_next_sequence() !=\
               objlist[i].peek_out_queued_packets_next_sequence():
                continue
            if wan_statisticsObj.peek_fast_retransmits() is not None and\
               wan_statisticsObj.peek_fast_retransmits() !=\
               objlist[i].peek_fast_retransmits():
                continue
            if wan_statisticsObj.peek_slow_retransmits() is not None and\
               wan_statisticsObj.peek_slow_retransmits() !=\
               objlist[i].peek_slow_retransmits():
                continue
            if wan_statisticsObj.peek_in_packets() is not None and\
               wan_statisticsObj.peek_in_packets() !=\
               objlist[i].peek_in_packets():
                continue
            if wan_statisticsObj.peek_out_queued_packets_maximum_sequence() is\
               not None and\
               wan_statisticsObj.peek_out_queued_packets_maximum_sequence()\
               != objlist[i].peek_out_queued_packets_maximum_sequence():
                continue
            if wan_statisticsObj.peek_out_window_size() is not None and\
               wan_statisticsObj.peek_out_window_size() !=\
               objlist[i].peek_out_window_size():
                continue
            if wan_statisticsObj.peek_in_queued_out_of_order() is not None and\
               wan_statisticsObj.peek_in_queued_out_of_order() !=\
               objlist[i].peek_in_queued_out_of_order():
                continue
            if wan_statisticsObj.peek_arl_next_reset_algorithm() is not None\
               and wan_statisticsObj.peek_arl_next_reset_algorithm() !=\
               objlist[i].peek_arl_next_reset_algorithm():
                continue
            if wan_statisticsObj.peek_circuit_id() is not None and\
               wan_statisticsObj.peek_circuit_id() !=\
               objlist[i].peek_circuit_id():
                continue
            if wan_statisticsObj.peek_rtt_variance() is not None and\
               wan_statisticsObj.peek_rtt_variance() !=\
               objlist[i].peek_rtt_variance():
                continue
            if wan_statisticsObj.peek_in_bytes() is not None and\
               wan_statisticsObj.peek_in_bytes() !=\
               objlist[i].peek_in_bytes():
                continue
            if wan_statisticsObj.peek_maximum_fast_retransmits() is not None\
               and wan_statisticsObj.peek_maximum_fast_retransmits() !=\
               objlist[i].peek_maximum_fast_retransmits():
                continue
            if wan_statisticsObj.peek_source_port() is not None and\
               wan_statisticsObj.peek_source_port() !=\
               objlist[i].peek_source_port():
                continue
            if wan_statisticsObj.peek_destination_port() is not None and\
               wan_statisticsObj.peek_destination_port() !=\
               objlist[i].peek_destination_port():
                continue
            if wan_statisticsObj.peek_retransmits() is not None and\
               wan_statisticsObj.peek_retransmits() !=\
               objlist[i].peek_retransmits():
                continue
            if wan_statisticsObj.peek_in_queued_out_of_order_maximum() is not\
               None and\
               wan_statisticsObj.peek_in_queued_out_of_order_maximum() !=\
               objlist[i].peek_in_queued_out_of_order_maximum():
                continue
            if wan_statisticsObj.peek_rtt_maximum() is not None and\
               wan_statisticsObj.peek_rtt_maximum() !=\
               objlist[i].peek_rtt_maximum():
                continue
            if wan_statisticsObj.peek_retransmit_timeout() is not None and\
               wan_statisticsObj.peek_retransmit_timeout() !=\
               objlist[i].peek_retransmit_timeout():
                continue
            if wan_statisticsObj.peek_duplicate_acknowledgement() is not None\
               and wan_statisticsObj.peek_duplicate_acknowledgement() !=\
               objlist[i].peek_duplicate_acknowledgement():
                continue
            if wan_statisticsObj.peek_out_in_flight_packets() is not None and\
               wan_statisticsObj.peek_out_in_flight_packets() !=\
               objlist[i].peek_out_in_flight_packets():
                continue
            if wan_statisticsObj.peek_maximum_retransmits() is not None and\
               wan_statisticsObj.peek_maximum_retransmits() !=\
               objlist[i].peek_maximum_retransmits():
                continue
            if wan_statisticsObj.peek_in_queued_out_of_order_total() is not\
               None and\
               wan_statisticsObj.peek_in_queued_out_of_order_total() !=\
               objlist[i].peek_in_queued_out_of_order_total():
                continue
            if wan_statisticsObj.peek_connection_mss() is not None and\
               wan_statisticsObj.peek_connection_mss() !=\
               objlist[i].peek_connection_mss():
                continue
            if wan_statisticsObj.peek_rtt() is not None and\
               wan_statisticsObj.peek_rtt() != objlist[i].peek_rtt():
                continue
            if wan_statisticsObj.peek_ve_port() is not None and\
               wan_statisticsObj.peek_ve_port() != objlist[i].peek_ve_port():
                continue
            if wan_statisticsObj.peek_arl_maximum() is not None and\
               wan_statisticsObj.peek_arl_maximum() !=\
               objlist[i].peek_arl_maximum():
                continue
            if wan_statisticsObj.peek_in_queued_packets_maximum_sequence() is\
               not None and\
               wan_statisticsObj.peek_in_queued_packets_maximum_sequence()\
               != objlist[i].peek_in_queued_packets_maximum_sequence():
                continue
            if wan_statisticsObj.peek_out_bytes() is not None and\
               wan_statisticsObj.peek_out_bytes() !=\
               objlist[i].peek_out_bytes():
                continue
            if wan_statisticsObj.peek_in_window_scale() is not None and\
               wan_statisticsObj.peek_in_window_scale() !=\
               objlist[i].peek_in_window_scale():
                continue
            if wan_statisticsObj.peek_congestion_window() is not None and\
               wan_statisticsObj.peek_congestion_window() !=\
               objlist[i].peek_congestion_window():
                continue
            if wan_statisticsObj.peek_in_queued_packets() is not None and\
               wan_statisticsObj.peek_in_queued_packets() !=\
               objlist[i].peek_in_queued_packets():
                continue
            if wan_statisticsObj.peek_out_window_scale() is not None and\
               wan_statisticsObj.peek_out_window_scale() !=\
               objlist[i].peek_out_window_scale():
                continue
            if wan_statisticsObj.peek_rtt_variance_maximum() is not None and\
               wan_statisticsObj.peek_rtt_variance_maximum() !=\
               objlist[i].peek_rtt_variance_maximum():
                continue
            if wan_statisticsObj.peek_arl_minimum() is not None and\
               wan_statisticsObj.peek_arl_minimum() !=\
               objlist[i].peek_arl_minimum():
                continue
            if wan_statisticsObj.peek_slow_start_threshold() is not None and\
               wan_statisticsObj.peek_slow_start_threshold() !=\
               objlist[i].peek_slow_start_threshold():
                continue
            if wan_statisticsObj.peek_ha_type() is not None and\
               wan_statisticsObj.peek_ha_type() != objlist[i].peek_ha_type():
                continue
            wan_statisticslist.append(objlist[i])
    else:
        return objlist
    return wan_statisticslist


def show_wan_statistics(session, priority=None,
                        out_unacknowledged_packets_sequence=None,
                        in_queued_packets_next_sequence=None,
                        slow_starts=None,
                        out_queued_packets_minimum_sequence=None,
                        in_window_size=None,
                        in_queued_packets_minimum_sequence=None,
                        out_packets=None, connection_id=None,
                        in_window_size_maximum=None, operation_mode=None,
                        arl_current=None,
                        out_queued_packets_next_sequence=None,
                        fast_retransmits=None, slow_retransmits=None,
                        in_packets=None,
                        out_queued_packets_maximum_sequence=None,
                        out_window_size=None, in_queued_out_of_order=None,
                        arl_next_reset_algorithm=None, circuit_id=None,
                        rtt_variance=None, in_bytes=None,
                        maximum_fast_retransmits=None, source_port=None,
                        destination_port=None, retransmits=None,
                        in_queued_out_of_order_maximum=None,
                        rtt_maximum=None, retransmit_timeout=None,
                        duplicate_acknowledgement=None,
                        out_in_flight_packets=None, maximum_retransmits=None,
                        in_queued_out_of_order_total=None,
                        connection_mss=None, rtt=None, ve_port=None,
                        arl_maximum=None,
                        in_queued_packets_maximum_sequence=None,
                        out_bytes=None, in_window_scale=None,
                        congestion_window=None, in_queued_packets=None,
                        out_window_scale=None, rtt_variance_maximum=None,
                        arl_minimum=None, slow_start_threshold=None,
                        ha_type=None):
    wan_statisticsObj = wan_statistics()
    wan_statisticsObj.set_priority(priority)
    wan_statisticsObj.set_out_unacknowledged_packets_sequence(
                      out_unacknowledged_packets_sequence)
    wan_statisticsObj.set_in_queued_packets_next_sequence(
                      in_queued_packets_next_sequence)
    wan_statisticsObj.set_slow_starts(slow_starts)
    wan_statisticsObj.set_out_queued_packets_minimum_sequence(
                      out_queued_packets_minimum_sequence)
    wan_statisticsObj.set_in_window_size(in_window_size)
    wan_statisticsObj.set_in_queued_packets_minimum_sequence(
                      in_queued_packets_minimum_sequence)
    wan_statisticsObj.set_out_packets(out_packets)
    wan_statisticsObj.set_connection_id(connection_id)
    wan_statisticsObj.set_in_window_size_maximum(in_window_size_maximum)
    wan_statisticsObj.set_operation_mode(operation_mode)
    wan_statisticsObj.set_arl_current(arl_current)
    wan_statisticsObj.set_out_queued_packets_next_sequence(
                      out_queued_packets_next_sequence)
    wan_statisticsObj.set_fast_retransmits(fast_retransmits)
    wan_statisticsObj.set_slow_retransmits(slow_retransmits)
    wan_statisticsObj.set_in_packets(in_packets)
    wan_statisticsObj.set_out_queued_packets_maximum_sequence(
                      out_queued_packets_maximum_sequence)
    wan_statisticsObj.set_out_window_size(out_window_size)
    wan_statisticsObj.set_in_queued_out_of_order(in_queued_out_of_order)
    wan_statisticsObj.set_arl_next_reset_algorithm(arl_next_reset_algorithm)
    wan_statisticsObj.set_circuit_id(circuit_id)
    wan_statisticsObj.set_rtt_variance(rtt_variance)
    wan_statisticsObj.set_in_bytes(in_bytes)
    wan_statisticsObj.set_maximum_fast_retransmits(maximum_fast_retransmits)
    wan_statisticsObj.set_source_port(source_port)
    wan_statisticsObj.set_destination_port(destination_port)
    wan_statisticsObj.set_retransmits(retransmits)
    wan_statisticsObj.set_in_queued_out_of_order_maximum(
                      in_queued_out_of_order_maximum)
    wan_statisticsObj.set_rtt_maximum(rtt_maximum)
    wan_statisticsObj.set_retransmit_timeout(retransmit_timeout)
    wan_statisticsObj.set_duplicate_acknowledgement(duplicate_acknowledgement)
    wan_statisticsObj.set_out_in_flight_packets(out_in_flight_packets)
    wan_statisticsObj.set_maximum_retransmits(maximum_retransmits)
    wan_statisticsObj.set_in_queued_out_of_order_total(
                      in_queued_out_of_order_total)
    wan_statisticsObj.set_connection_mss(connection_mss)
    wan_statisticsObj.set_rtt(rtt)
    wan_statisticsObj.set_ve_port(ve_port)
    wan_statisticsObj.set_arl_maximum(arl_maximum)
    wan_statisticsObj.set_in_queued_packets_maximum_sequence(
                      in_queued_packets_maximum_sequence)
    wan_statisticsObj.set_out_bytes(out_bytes)
    wan_statisticsObj.set_in_window_scale(in_window_scale)
    wan_statisticsObj.set_congestion_window(congestion_window)
    wan_statisticsObj.set_in_queued_packets(in_queued_packets)
    wan_statisticsObj.set_out_window_scale(out_window_scale)
    wan_statisticsObj.set_rtt_variance_maximum(rtt_variance_maximum)
    wan_statisticsObj.set_arl_minimum(arl_minimum)
    wan_statisticsObj.set_slow_start_threshold(slow_start_threshold)
    wan_statisticsObj.set_ha_type(ha_type)
    return _show_wan_statistics(session, wan_statisticsObj)


def validate(wan_statisticsObj):
    if wan_statisticsObj.peek_priority() is None or\
       wan_statisticsObj.peek_out_unacknowledged_packets_sequence() is None\
       or wan_statisticsObj.peek_in_queued_packets_next_sequence() is None\
       or wan_statisticsObj.peek_slow_starts() is None or\
       wan_statisticsObj.peek_out_queued_packets_minimum_sequence() is None\
       or wan_statisticsObj.peek_in_window_size() is None or\
       wan_statisticsObj.peek_in_queued_packets_minimum_sequence() is None\
       or wan_statisticsObj.peek_out_packets() is None or\
       wan_statisticsObj.peek_connection_id() is None or\
       wan_statisticsObj.peek_in_window_size_maximum() is None or\
       wan_statisticsObj.peek_operation_mode() is None or\
       wan_statisticsObj.peek_arl_current() is None or\
       wan_statisticsObj.peek_out_queued_packets_next_sequence() is None or\
       wan_statisticsObj.peek_fast_retransmits() is None or\
       wan_statisticsObj.peek_slow_retransmits() is None or\
       wan_statisticsObj.peek_in_packets() is None or\
       wan_statisticsObj.peek_out_queued_packets_maximum_sequence() is None\
       or wan_statisticsObj.peek_out_window_size() is None or\
       wan_statisticsObj.peek_in_queued_out_of_order() is None or\
       wan_statisticsObj.peek_arl_next_reset_algorithm() is None or\
       wan_statisticsObj.peek_circuit_id() is None or\
       wan_statisticsObj.peek_rtt_variance() is None or\
       wan_statisticsObj.peek_in_bytes() is None or\
       wan_statisticsObj.peek_maximum_fast_retransmits() is None or\
       wan_statisticsObj.peek_source_port() is None or\
       wan_statisticsObj.peek_destination_port() is None or\
       wan_statisticsObj.peek_retransmits() is None or\
       wan_statisticsObj.peek_in_queued_out_of_order_maximum() is None or\
       wan_statisticsObj.peek_rtt_maximum() is None or\
       wan_statisticsObj.peek_retransmit_timeout() is None or\
       wan_statisticsObj.peek_duplicate_acknowledgement() is None or\
       wan_statisticsObj.peek_out_in_flight_packets() is None or\
       wan_statisticsObj.peek_maximum_retransmits() is None or\
       wan_statisticsObj.peek_in_queued_out_of_order_total() is None or\
       wan_statisticsObj.peek_connection_mss() is None or\
       wan_statisticsObj.peek_rtt() is None or\
       wan_statisticsObj.peek_ve_port() is None or\
       wan_statisticsObj.peek_arl_maximum() is None or\
       wan_statisticsObj.peek_in_queued_packets_maximum_sequence() is None\
       or wan_statisticsObj.peek_out_bytes() is None or\
       wan_statisticsObj.peek_in_window_scale() is None or\
       wan_statisticsObj.peek_congestion_window() is None or\
       wan_statisticsObj.peek_in_queued_packets() is None or\
       wan_statisticsObj.peek_out_window_scale() is None or\
       wan_statisticsObj.peek_rtt_variance_maximum() is None or\
       wan_statisticsObj.peek_arl_minimum() is None or\
       wan_statisticsObj.peek_slow_start_threshold() is None or\
       wan_statisticsObj.peek_ha_type() is None:
        return 0
    return 0


def main(argv):
    filters = ["priority", "out_unacknowledged_packets_sequence",
               "in_queued_packets_next_sequence", "slow_starts",
               "out_queued_packets_minimum_sequence", "in_window_size",
               "in_queued_packets_minimum_sequence", "out_packets",
               "connection_id", "in_window_size_maximum", "operation_mode",
               "arl_current", "out_queued_packets_next_sequence",
               "fast_retransmits", "slow_retransmits", "in_packets",
               "out_queued_packets_maximum_sequence", "out_window_size",
               "in_queued_out_of_order", "arl_next_reset_algorithm",
               "circuit_id", "rtt_variance", "in_bytes",
               "maximum_fast_retransmits", "source_port", "destination_port",
               "retransmits", "in_queued_out_of_order_maximum",
               "rtt_maximum", "retransmit_timeout",
               "duplicate_acknowledgement", "out_in_flight_packets",
               "maximum_retransmits", "in_queued_out_of_order_total",
               "connection_mss", "rtt", "ve_port", "arl_maximum",
               "in_queued_packets_maximum_sequence", "out_bytes",
               "in_window_scale", "congestion_window", "in_queued_packets",
               "out_window_scale", "rtt_variance_maximum", "arl_minimum",
               "slow_start_threshold", "ha_type"]
    inputs = brcd_util.parse(argv, wan_statistics, filters, validate)
    session = brcd_util.getsession(inputs)
    result = _show_wan_statistics(session, inputs['utilobject'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
