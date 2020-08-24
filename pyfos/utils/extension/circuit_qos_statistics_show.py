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


# circuit_qos_statistics_show.py(pyGen v1.0.0)


"""

:mod:`circuit_qos_statistics_show` - PyFOS util to show for\
 circuit_qos_statistics
******************************************************************************\
*******************************************************************************
The:mod:`circuit_qos_statistics_show` PyFOS util to show for\
 circuit_qos_statistics


Represents circuit statistics for extension blade or system.

circuit_qos_statistics_show: usage

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
    * --out-tcp-packets=OUT-TCP-PACKETS: TCP packets sent.
    * --tcp-slow-starts=TCP-SLOW-STARTS: TCP slow starts.
    * --in-bytes=IN-BYTES: total octets received.
    * --duration=DURATION: Connection duration (in seconds).
    * --out-tcp-bytes=OUT-TCP-BYTES: Total TCP bytes sent.
    * --ha-type=HA-TYPE: Tunnel group HA type configuration.
    * --out-bytes=OUT-BYTES: total octets sent.
    * --tcp-out-of-order-packets=TCP-OUT-OF-ORDER-PACKETS: TCP total out of\
      order packets.
    * --flow-status=FLOW-STATUS: Flow control status:  false : flow control is\
      off true : flow control is on
    * --rtt=RTT: The round trip time.
    * --in-packets=IN-PACKETS: total packets received.
    * --tcp-retransmits=TCP-RETRANSMITS: TCP retransmits /lost packets.
    * --connection-count=CONNECTION-COUNT: Active connection count.
    * --priority=PRIORITY: QOS Priority value for the tunnel
    * --circuit-id=CIRCUIT-ID: Circuit identifier the allowed values are for 0\
      to 9.
    * --out-packets=OUT-PACKETS: Total TCP packets sent.
    * --in-bytes-average=IN-BYTES-AVERAGE: Total octets received per 30s\
      average.
    * --in-tcp-packets=IN-TCP-PACKETS: TCP packets received.
    * --operational-status=OPERATIONAL-STATUS: Circuit operational status.
    * --in-tcp-bytes=IN-TCP-BYTES: Total TCP bytes received.
    * --out-bytes-average=OUT-BYTES-AVERAGE: Total octets send per 30s\
      average.
    * --ve-port=VE-PORT: The name of the extension-tunnel interface.
* Output:
    * Python dictionary content with RESTCONF response data.


.. function:: circuit_qos_statistics_show.show_circuit_qos_statistics(session,\
out_tcp_packets, tcp_slow_starts, in_bytes, duration, out_tcp_bytes,\
ha_type, out_bytes, tcp_out_of_order_packets, flow_status, rtt, in_packets,\
tcp_retransmits, connection_count, priority, circuit_id, out_packets,\
in_bytes_average, in_tcp_packets, operational_status, in_tcp_bytes,\
out_bytes_average, ve_port)

    *Show circuit_qos_statistics*

    Example Usage of the Method::

            ret =\
 circuit_qos_statistics_show.show_circuit_qos_statistics(session,\
 out_tcp_packets, tcp_slow_starts, in_bytes, duration, out_tcp_bytes,\
 ha_type, out_bytes, tcp_out_of_order_packets, flow_status, rtt, in_packets,\
 tcp_retransmits, connection_count, priority, circuit_id, out_packets,\
 in_bytes_average, in_tcp_packets, operational_status, in_tcp_bytes,\
 out_bytes_average, ve_port)
            print(ret)

    Details::

        circuit_qos_statisticsObj = circuit_qos_statistics()
        circuit_qos_statisticsObj.set_out_tcp_packets(out_tcp_packets)
        circuit_qos_statisticsObj.set_tcp_slow_starts(tcp_slow_starts)
        circuit_qos_statisticsObj.set_in_bytes(in_bytes)
        circuit_qos_statisticsObj.set_duration(duration)
        circuit_qos_statisticsObj.set_out_tcp_bytes(out_tcp_bytes)
        circuit_qos_statisticsObj.set_ha_type(ha_type)
        circuit_qos_statisticsObj.set_out_bytes(out_bytes)
       \
 circuit_qos_statisticsObj.set_tcp_out_of_order_packets(\
 tcp_out_of_order_packets)
        circuit_qos_statisticsObj.set_flow_status(flow_status)
        circuit_qos_statisticsObj.set_rtt(rtt)
        circuit_qos_statisticsObj.set_in_packets(in_packets)
        circuit_qos_statisticsObj.set_tcp_retransmits(tcp_retransmits)
        circuit_qos_statisticsObj.set_connection_count(connection_count)
        circuit_qos_statisticsObj.set_priority(priority)
        circuit_qos_statisticsObj.set_circuit_id(circuit_id)
        circuit_qos_statisticsObj.set_out_packets(out_packets)
        circuit_qos_statisticsObj.set_in_bytes_average(in_bytes_average)
        circuit_qos_statisticsObj.set_in_tcp_packets(in_tcp_packets)
        circuit_qos_statisticsObj.set_operational_status(operational_status)
        circuit_qos_statisticsObj.set_in_tcp_bytes(in_tcp_bytes)
        circuit_qos_statisticsObj.set_out_bytes_average(out_bytes_average)
        circuit_qos_statisticsObj.set_ve_port(ve_port)
        ret = _show_circuit_qos_statistics(session, circuit_qos_statisticsObj)
        print(ret)

    **Inputs**

    :param session: The session returned by the login.
    :param out_tcp_packets: TCP packets sent.
    :param tcp_slow_starts: TCP slow starts.
    :param in_bytes: total octets received.
    :param duration: Connection duration (in seconds).
    :param out_tcp_bytes: Total TCP bytes sent.
    :param ha_type: Tunnel group HA type configuration.
    :param out_bytes: total octets sent.
    :param tcp_out_of_order_packets: TCP total out of order packets.
    :param flow_status: Flow control status:  false : flow control is off true\
      : flow control is on
    :param rtt: The round trip time.
    :param in_packets: total packets received.
    :param tcp_retransmits: TCP retransmits /lost packets.
    :param connection_count: Active connection count.
    :param priority: QOS Priority value for the tunnel
    :param circuit_id: Circuit identifier the allowed values are for 0 to 9.
    :param out_packets: Total TCP packets sent.
    :param in_bytes_average: Total octets received per 30s average.
    :param in_tcp_packets: TCP packets received.
    :param operational_status: Circuit operational status.
    :param in_tcp_bytes: Total TCP bytes received.
    :param out_bytes_average: Total octets send per 30s average.
    :param ve_port: The name of the extension-tunnel interface.

    **Output**

    :rtype: None or one/more instance of class circuit_qos_statistics on\
    Success  or a dictionary with error.

"""


# Start utils imports
import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_extension_tunnel import circuit_qos_statistics

from pyfos.utils import brcd_util
# End module imports


def _show_circuit_qos_statistics(session, circuit_qos_statisticsObj):
    objlist = circuit_qos_statistics.get(session)
    circuit_qos_statisticslist = list()
    if isinstance(objlist, circuit_qos_statistics):
        objlist = [objlist]
    if isinstance(objlist, list):
        for i in range(len(objlist)):
            if circuit_qos_statisticsObj.peek_out_tcp_packets() is not None\
               and circuit_qos_statisticsObj.peek_out_tcp_packets() !=\
               objlist[i].peek_out_tcp_packets():
                continue
            if circuit_qos_statisticsObj.peek_tcp_slow_starts() is not None\
               and circuit_qos_statisticsObj.peek_tcp_slow_starts() !=\
               objlist[i].peek_tcp_slow_starts():
                continue
            if circuit_qos_statisticsObj.peek_in_bytes() is not None and\
               circuit_qos_statisticsObj.peek_in_bytes() !=\
               objlist[i].peek_in_bytes():
                continue
            if circuit_qos_statisticsObj.peek_duration() is not None and\
               circuit_qos_statisticsObj.peek_duration() !=\
               objlist[i].peek_duration():
                continue
            if circuit_qos_statisticsObj.peek_out_tcp_bytes() is not None and\
               circuit_qos_statisticsObj.peek_out_tcp_bytes() !=\
               objlist[i].peek_out_tcp_bytes():
                continue
            if circuit_qos_statisticsObj.peek_ha_type() is not None and\
               circuit_qos_statisticsObj.peek_ha_type() !=\
               objlist[i].peek_ha_type():
                continue
            if circuit_qos_statisticsObj.peek_out_bytes() is not None and\
               circuit_qos_statisticsObj.peek_out_bytes() !=\
               objlist[i].peek_out_bytes():
                continue
            if circuit_qos_statisticsObj.peek_tcp_out_of_order_packets() is\
               not None and\
               circuit_qos_statisticsObj.peek_tcp_out_of_order_packets() !=\
               objlist[i].peek_tcp_out_of_order_packets():
                continue
            if circuit_qos_statisticsObj.peek_flow_status() is not None and\
               circuit_qos_statisticsObj.peek_flow_status() !=\
               objlist[i].peek_flow_status():
                continue
            if circuit_qos_statisticsObj.peek_rtt() is not None and\
               circuit_qos_statisticsObj.peek_rtt() != objlist[i].peek_rtt():
                continue
            if circuit_qos_statisticsObj.peek_in_packets() is not None and\
               circuit_qos_statisticsObj.peek_in_packets() !=\
               objlist[i].peek_in_packets():
                continue
            if circuit_qos_statisticsObj.peek_tcp_retransmits() is not None\
               and circuit_qos_statisticsObj.peek_tcp_retransmits() !=\
               objlist[i].peek_tcp_retransmits():
                continue
            if circuit_qos_statisticsObj.peek_connection_count() is not None\
               and circuit_qos_statisticsObj.peek_connection_count() !=\
               objlist[i].peek_connection_count():
                continue
            if circuit_qos_statisticsObj.peek_priority() is not None and\
               circuit_qos_statisticsObj.peek_priority() !=\
               objlist[i].peek_priority():
                continue
            if circuit_qos_statisticsObj.peek_circuit_id() is not None and\
               circuit_qos_statisticsObj.peek_circuit_id() !=\
               objlist[i].peek_circuit_id():
                continue
            if circuit_qos_statisticsObj.peek_out_packets() is not None and\
               circuit_qos_statisticsObj.peek_out_packets() !=\
               objlist[i].peek_out_packets():
                continue
            if circuit_qos_statisticsObj.peek_in_bytes_average() is not None\
               and circuit_qos_statisticsObj.peek_in_bytes_average() !=\
               objlist[i].peek_in_bytes_average():
                continue
            if circuit_qos_statisticsObj.peek_in_tcp_packets() is not None and\
               circuit_qos_statisticsObj.peek_in_tcp_packets() !=\
               objlist[i].peek_in_tcp_packets():
                continue
            if circuit_qos_statisticsObj.peek_operational_status() is not None\
               and circuit_qos_statisticsObj.peek_operational_status() !=\
               objlist[i].peek_operational_status():
                continue
            if circuit_qos_statisticsObj.peek_in_tcp_bytes() is not None and\
               circuit_qos_statisticsObj.peek_in_tcp_bytes() !=\
               objlist[i].peek_in_tcp_bytes():
                continue
            if circuit_qos_statisticsObj.peek_out_bytes_average() is not None\
               and circuit_qos_statisticsObj.peek_out_bytes_average() !=\
               objlist[i].peek_out_bytes_average():
                continue
            if circuit_qos_statisticsObj.peek_ve_port() is not None and\
               circuit_qos_statisticsObj.peek_ve_port() !=\
               objlist[i].peek_ve_port():
                continue
            circuit_qos_statisticslist.append(objlist[i])
    else:
        return objlist
    return circuit_qos_statisticslist


def show_circuit_qos_statistics(session, out_tcp_packets=None,
                                tcp_slow_starts=None, in_bytes=None,
                                duration=None, out_tcp_bytes=None,
                                ha_type=None, out_bytes=None,
                                tcp_out_of_order_packets=None,
                                flow_status=None, rtt=None, in_packets=None,
                                tcp_retransmits=None, connection_count=None,
                                priority=None, circuit_id=None,
                                out_packets=None, in_bytes_average=None,
                                in_tcp_packets=None, operational_status=None,
                                in_tcp_bytes=None, out_bytes_average=None,
                                ve_port=None):
    circuit_qos_statisticsObj = circuit_qos_statistics()
    circuit_qos_statisticsObj.set_out_tcp_packets(out_tcp_packets)
    circuit_qos_statisticsObj.set_tcp_slow_starts(tcp_slow_starts)
    circuit_qos_statisticsObj.set_in_bytes(in_bytes)
    circuit_qos_statisticsObj.set_duration(duration)
    circuit_qos_statisticsObj.set_out_tcp_bytes(out_tcp_bytes)
    circuit_qos_statisticsObj.set_ha_type(ha_type)
    circuit_qos_statisticsObj.set_out_bytes(out_bytes)
    circuit_qos_statisticsObj.set_tcp_out_of_order_packets(
                              tcp_out_of_order_packets)
    circuit_qos_statisticsObj.set_flow_status(flow_status)
    circuit_qos_statisticsObj.set_rtt(rtt)
    circuit_qos_statisticsObj.set_in_packets(in_packets)
    circuit_qos_statisticsObj.set_tcp_retransmits(tcp_retransmits)
    circuit_qos_statisticsObj.set_connection_count(connection_count)
    circuit_qos_statisticsObj.set_priority(priority)
    circuit_qos_statisticsObj.set_circuit_id(circuit_id)
    circuit_qos_statisticsObj.set_out_packets(out_packets)
    circuit_qos_statisticsObj.set_in_bytes_average(in_bytes_average)
    circuit_qos_statisticsObj.set_in_tcp_packets(in_tcp_packets)
    circuit_qos_statisticsObj.set_operational_status(operational_status)
    circuit_qos_statisticsObj.set_in_tcp_bytes(in_tcp_bytes)
    circuit_qos_statisticsObj.set_out_bytes_average(out_bytes_average)
    circuit_qos_statisticsObj.set_ve_port(ve_port)
    return _show_circuit_qos_statistics(session, circuit_qos_statisticsObj)


def validate(circuit_qos_statisticsObj):
    if circuit_qos_statisticsObj.peek_out_tcp_packets() is None or\
       circuit_qos_statisticsObj.peek_tcp_slow_starts() is None or\
       circuit_qos_statisticsObj.peek_in_bytes() is None or\
       circuit_qos_statisticsObj.peek_duration() is None or\
       circuit_qos_statisticsObj.peek_out_tcp_bytes() is None or\
       circuit_qos_statisticsObj.peek_ha_type() is None or\
       circuit_qos_statisticsObj.peek_out_bytes() is None or\
       circuit_qos_statisticsObj.peek_tcp_out_of_order_packets() is None or\
       circuit_qos_statisticsObj.peek_flow_status() is None or\
       circuit_qos_statisticsObj.peek_rtt() is None or\
       circuit_qos_statisticsObj.peek_in_packets() is None or\
       circuit_qos_statisticsObj.peek_tcp_retransmits() is None or\
       circuit_qos_statisticsObj.peek_connection_count() is None or\
       circuit_qos_statisticsObj.peek_priority() is None or\
       circuit_qos_statisticsObj.peek_circuit_id() is None or\
       circuit_qos_statisticsObj.peek_out_packets() is None or\
       circuit_qos_statisticsObj.peek_in_bytes_average() is None or\
       circuit_qos_statisticsObj.peek_in_tcp_packets() is None or\
       circuit_qos_statisticsObj.peek_operational_status() is None or\
       circuit_qos_statisticsObj.peek_in_tcp_bytes() is None or\
       circuit_qos_statisticsObj.peek_out_bytes_average() is None or\
       circuit_qos_statisticsObj.peek_ve_port() is None:
        return 0
    return 0


def main(argv):
    filters = ["out_tcp_packets", "tcp_slow_starts", "in_bytes", "duration",
               "out_tcp_bytes", "ha_type", "out_bytes",
               "tcp_out_of_order_packets", "flow_status", "rtt",
               "in_packets", "tcp_retransmits", "connection_count",
               "priority", "circuit_id", "out_packets", "in_bytes_average",
               "in_tcp_packets", "operational_status", "in_tcp_bytes",
               "out_bytes_average", "ve_port"]
    inputs = brcd_util.parse(argv, circuit_qos_statistics, filters, validate)
    session = brcd_util.getsession(inputs)
    result = _show_circuit_qos_statistics(session, inputs['utilobject'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
