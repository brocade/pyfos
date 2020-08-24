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


# traffic_control_list_show.py(pyGen v1.0.0)


"""

:mod:`traffic_control_list_show` - PyFOS util to show for\
 traffic_control_list
******************************************************************************\
*******************************************************************************
The:mod:`traffic_control_list_show` PyFOS util to show for\
 traffic_control_list


Represents traffic control lists in order to manage IP Extension LAN flows.

traffic_control_list_show: usage

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
    * --target-ve-port=TARGET-VE-PORT: The VE port of the extension-tunnel\
      used for allowing a LAN ingress traffic to be sent over the WAN.
    * --action=ACTION: Set the action for this TCL. The TCL can be programmed\
      to allow a traffic or deny the traffic.
    * --segment-preservation-enabled=SEGMENT-PRESERVATION-ENABLED: Is segment\
      preservation for this TCL enabled. Default: false, Values supported\
      are true/false.  false - Disabled true - Enabled
    * --port=PORT: The protocol port input filter for this TCL. The port\
      arguments can be specified as a single port or in case of multiple\
      ports a comma separated list of ports or else a range of ports can be\
      specified or a combination. example : 22 or 600-603 or 300,302,305
    * --traffic-control-list-name=TRAFFIC-CONTROL-LIST-NAME: Name of the\
      Traffic-Control-List.
    * --source-address=SOURCE-ADDRESS: Source IP address input filter for this\
      TCL.
    * --target-slot=TARGET-SLOT: In case of non-chassis system, the slot\
      number is always 0. In case of chassis system, it is the slot number\
      of chassis in which the extension blade is inserted in. In case of\
      chassis, slot number is non-zero value.
    * --target-dp-id=TARGET-DP-ID: Extension Data Path Processor ID. Based on\
      platform either it will have a single DP or dual DP. In case of single\
      DP only DP0 is supported, and in case of dual DP both DP0 and DP1 are\
      supported  0 : DP0 1 : DP1.
    * --l4-protocol=L4-PROTOCOL: The Layer 4 protocol input filter for this\
      TCL.  The value can be a well known protocol string value or otherwise\
      a L4 protocol number.  The 'any' protocol string is the default value\
      and is meant to match any L4 protocol value.  The valid range for L4\
      protocol is from 0-255.  The list of known protocol string values from\
      system are as below:  ICMP  ICMP6  TCP  UDP  VRRP
    * --target-qos=TARGET-QOS: QoS priority associated with an\
      extension-tunnel to be used to allow a LAN ingress traffic over WAN.
    * --reset-propagation-enabled=RESET-PROPAGATION-ENABLED: Is End to End\
      reset propagation for this TCL enabled. Default: false, Values\
      supported are true/false.  false - Disabled true - Enabled
    * --source-address-prefix-length=SOURCE-ADDRESS-PREFIX-LENGTH: The prefix\
      length operator for source IP address input filter.
    * --application=APPLICATION: The application input filter for this TCL.\
      This includes a list of known apps already present or a user defined\
      app-type name. The 'any' application type name is a special value to\
      identify any application.  Below are few examples of system defined\
      known application types:  CIFS  Data-Domain  FCIP  FTP  HTTP  HTTPS
    * --destination-address-prefix-length=DESTINATION-ADDRESS-PREFIX-LENGTH:\
      The prefix length operator for destination IP address input filter.
    * --hit-count=HIT-COUNT: Total number of times this TCL rule was hit.
    * --dscp=DSCP: The DSCP input filter for this TCL. The values supported\
      are from 0-63. The value 'any' is default value and is meant to match\
      any dscp value specified.
    * --cp-dp-synchronized=CP-DP-SYNCHRONIZED: Indicates whether an\
      admin-statatus-enabled TCL is synchronized between the CP->DP. In case\
      of error the value will be set to false  false - CP-DP synchronizing\
      failed. true - CP-DP is synchronized.
    * --vlan=VLAN: The VLAN input filter for this TCL. The values supported\
      are from 1-4095. The value 'any' is the default value and is meant to\
      match any vlan-id value specified.
    * --l2cos=L2COS: The L2CoS input filter for this TCL. The valid values are\
      from 0-7. The value 'any' is the default value and is meant to match\
      any value of l2CoS.
    * --destination-address=DESTINATION-ADDRESS: Destination IP address input\
      filter for this TCL.
    * --admin-state-enabled=ADMIN-STATE-ENABLED: Is TCL admin status enabled.\
      Default: false, Values supported are true/false.  false - Disabled\
      true - Enabled
    * --priority=PRIORITY: TCL priority provides an order of precedence to the\
      TCL rule within the overall TCL list. The priority 65535 is a special\
      priority associated or applicable to only the default TCL rule and no\
      other user configured TCL is allowed this value. The priority 0 is a\
      also treated as a special priority and is only to indicate that the\
      priority is not set. A valid user configured TCL priority must use a\
      value from 1 to 65534 only.
    * --non-terminated-enabled=NON-TERMINATED-ENABLED: Is non terminated\
      traffic for this TCL enabled. Default: false, Values supported are\
      true/false.  false - Disabled true - Enabled
* Output:
    * Python dictionary content with RESTCONF response data.


.. function:: traffic_control_list_show.show_traffic_control_list(session,\
target_ve_port, action, segment_preservation_enabled, port,\
traffic_control_list_name, source_address, target_slot, target_dp_id,\
l4_protocol, target_qos, reset_propagation_enabled,\
source_address_prefix_length, application,\
destination_address_prefix_length, hit_count, dscp, cp_dp_synchronized,\
vlan, l2cos, destination_address, admin_state_enabled, priority,\
non_terminated_enabled)

    *Show traffic_control_list*

    Example Usage of the Method::

            ret = traffic_control_list_show.show_traffic_control_list(session,\
 target_ve_port, action, segment_preservation_enabled, port,\
 traffic_control_list_name, source_address, target_slot, target_dp_id,\
 l4_protocol, target_qos, reset_propagation_enabled,\
 source_address_prefix_length, application,\
 destination_address_prefix_length, hit_count, dscp, cp_dp_synchronized,\
 vlan, l2cos, destination_address, admin_state_enabled, priority,\
 non_terminated_enabled)
            print(ret)

    Details::

        traffic_control_listObj = traffic_control_list()
        traffic_control_listObj.set_target_ve_port(target_ve_port)
        traffic_control_listObj.set_action(action)
       \
 traffic_control_listObj.set_segment_preservation_enabled(\
 segment_preservation_enabled)
        traffic_control_listObj.set_port(port)
       \
 traffic_control_listObj.set_traffic_control_list_name(\
 traffic_control_list_name)
        traffic_control_listObj.set_source_address(source_address)
        traffic_control_listObj.set_target_slot(target_slot)
        traffic_control_listObj.set_target_dp_id(target_dp_id)
        traffic_control_listObj.set_l4_protocol(l4_protocol)
        traffic_control_listObj.set_target_qos(target_qos)
       \
 traffic_control_listObj.set_reset_propagation_enabled(\
 reset_propagation_enabled)
       \
 traffic_control_listObj.set_source_address_prefix_length(\
 source_address_prefix_length)
        traffic_control_listObj.set_application(application)
       \
 traffic_control_listObj.set_destination_address_prefix_length(\
 destination_address_prefix_length)
        traffic_control_listObj.set_hit_count(hit_count)
        traffic_control_listObj.set_dscp(dscp)
        traffic_control_listObj.set_cp_dp_synchronized(cp_dp_synchronized)
        traffic_control_listObj.set_vlan(vlan)
        traffic_control_listObj.set_l2cos(l2cos)
        traffic_control_listObj.set_destination_address(destination_address)
        traffic_control_listObj.set_admin_state_enabled(admin_state_enabled)
        traffic_control_listObj.set_priority(priority)
       \
 traffic_control_listObj.set_non_terminated_enabled(non_terminated_enabled)
        ret = _show_traffic_control_list(session, traffic_control_listObj)
        print(ret)

    **Inputs**

    :param session: The session returned by the login.
    :param target_ve_port: The VE port of the extension-tunnel used for\
      allowing a LAN ingress traffic to be sent over the WAN.
    :param action: Set the action for this TCL. The TCL can be programmed to\
      allow a traffic or deny the traffic.
    :param segment_preservation_enabled: Is segment preservation for this TCL\
      enabled. Default: false, Values supported are true/false.  false -\
      Disabled true - Enabled
    :param port: The protocol port input filter for this TCL. The port\
      arguments can be specified as a single port or in case of multiple\
      ports a comma separated list of ports or else a range of ports can be\
      specified or a combination. example : 22 or 600-603 or 300,302,305
    :param traffic_control_list_name: Name of the Traffic-Control-List.
    :param source_address: Source IP address input filter for this TCL.
    :param target_slot: In case of non-chassis system, the slot number is\
      always 0. In case of chassis system, it is the slot number of chassis\
      in which the extension blade is inserted in. In case of chassis, slot\
      number is non-zero value.
    :param target_dp_id: Extension Data Path Processor ID. Based on platform\
      either it will have a single DP or dual DP. In case of single DP only\
      DP0 is supported, and in case of dual DP both DP0 and DP1 are\
      supported  0 : DP0 1 : DP1.
    :param l4_protocol: The Layer 4 protocol input filter for this TCL.  The\
      value can be a well known protocol string value or otherwise a L4\
      protocol number.  The 'any' protocol string is the default value and\
      is meant to match any L4 protocol value.  The valid range for L4\
      protocol is from 0-255.  The list of known protocol string values from\
      system are as below:  ICMP  ICMP6  TCP  UDP  VRRP
    :param target_qos: QoS priority associated with an extension-tunnel to be\
      used to allow a LAN ingress traffic over WAN.
    :param reset_propagation_enabled: Is End to End reset propagation for this\
      TCL enabled. Default: false, Values supported are true/false.  false -\
      Disabled true - Enabled
    :param source_address_prefix_length: The prefix length operator for source\
      IP address input filter.
    :param application: The application input filter for this TCL. This\
      includes a list of known apps already present or a user defined\
      app-type name. The 'any' application type name is a special value to\
      identify any application.  Below are few examples of system defined\
      known application types:  CIFS  Data-Domain  FCIP  FTP  HTTP  HTTPS
    :param destination_address_prefix_length: The prefix length operator for\
      destination IP address input filter.
    :param hit_count: Total number of times this TCL rule was hit.
    :param dscp: The DSCP input filter for this TCL. The values supported are\
      from 0-63. The value 'any' is default value and is meant to match any\
      dscp value specified.
    :param cp_dp_synchronized: Indicates whether an admin-statatus-enabled TCL\
      is synchronized between the CP->DP. In case of error the value will be\
      set to false  false - CP-DP synchronizing failed. true - CP-DP is\
      synchronized.
    :param vlan: The VLAN input filter for this TCL. The values supported are\
      from 1-4095. The value 'any' is the default value and is meant to\
      match any vlan-id value specified.
    :param l2cos: The L2CoS input filter for this TCL. The valid values are\
      from 0-7. The value 'any' is the default value and is meant to match\
      any value of l2CoS.
    :param destination_address: Destination IP address input filter for this\
      TCL.
    :param admin_state_enabled: Is TCL admin status enabled. Default: false,\
      Values supported are true/false.  false - Disabled true - Enabled
    :param priority: TCL priority provides an order of precedence to the TCL\
      rule within the overall TCL list. The priority 65535 is a special\
      priority associated or applicable to only the default TCL rule and no\
      other user configured TCL is allowed this value. The priority 0 is a\
      also treated as a special priority and is only to indicate that the\
      priority is not set. A valid user configured TCL priority must use a\
      value from 1 to 65534 only.
    :param non_terminated_enabled: Is non terminated traffic for this TCL\
      enabled. Default: false, Values supported are true/false.  false -\
      Disabled true - Enabled

    **Output**

    :rtype: None or one/more instance of class traffic_control_list on Success\
     or a dictionary with error.

"""


# Start utils imports
import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_extension import traffic_control_list

from pyfos.utils import brcd_util
# End module imports


def _show_traffic_control_list(session, traffic_control_listObj):
    objlist = traffic_control_list.get(session)
    traffic_control_listlist = list()
    if isinstance(objlist, traffic_control_list):
        objlist = [objlist]
    if isinstance(objlist, list):
        for i in range(len(objlist)):
            if traffic_control_listObj.peek_target_ve_port() is not None and\
               traffic_control_listObj.peek_target_ve_port() !=\
               objlist[i].peek_target_ve_port():
                continue
            if traffic_control_listObj.peek_action() is not None and\
               traffic_control_listObj.peek_action() !=\
               objlist[i].peek_action():
                continue
            if traffic_control_listObj.peek_segment_preservation_enabled() is\
               not None and\
               traffic_control_listObj.peek_segment_preservation_enabled()\
               != objlist[i].peek_segment_preservation_enabled():
                continue
            if traffic_control_listObj.peek_port() is not None and\
               traffic_control_listObj.peek_port() != objlist[i].peek_port():
                continue
            if traffic_control_listObj.peek_traffic_control_list_name() is not\
               None and\
               traffic_control_listObj.peek_traffic_control_list_name() !=\
               objlist[i].peek_traffic_control_list_name():
                continue
            if traffic_control_listObj.peek_source_address() is not None and\
               traffic_control_listObj.peek_source_address() !=\
               objlist[i].peek_source_address():
                continue
            if traffic_control_listObj.peek_target_slot() is not None and\
               traffic_control_listObj.peek_target_slot() !=\
               objlist[i].peek_target_slot():
                continue
            if traffic_control_listObj.peek_target_dp_id() is not None and\
               traffic_control_listObj.peek_target_dp_id() !=\
               objlist[i].peek_target_dp_id():
                continue
            if traffic_control_listObj.peek_l4_protocol() is not None and\
               traffic_control_listObj.peek_l4_protocol() !=\
               objlist[i].peek_l4_protocol():
                continue
            if traffic_control_listObj.peek_target_qos() is not None and\
               traffic_control_listObj.peek_target_qos() !=\
               objlist[i].peek_target_qos():
                continue
            if traffic_control_listObj.peek_reset_propagation_enabled() is not\
               None and\
               traffic_control_listObj.peek_reset_propagation_enabled() !=\
               objlist[i].peek_reset_propagation_enabled():
                continue
            if traffic_control_listObj.peek_source_address_prefix_length() is\
               not None and\
               traffic_control_listObj.peek_source_address_prefix_length()\
               != objlist[i].peek_source_address_prefix_length():
                continue
            if traffic_control_listObj.peek_application() is not None and\
               traffic_control_listObj.peek_application() !=\
               objlist[i].peek_application():
                continue
            if\
               traffic_control_listObj.\
               peek_destination_address_prefix_length() is not None and\
               traffic_control_listObj.\
               peek_destination_address_prefix_length() !=\
               objlist[i].peek_destination_address_prefix_length():
                continue
            if traffic_control_listObj.peek_hit_count() is not None and\
               traffic_control_listObj.peek_hit_count() !=\
               objlist[i].peek_hit_count():
                continue
            if traffic_control_listObj.peek_dscp() is not None and\
               traffic_control_listObj.peek_dscp() != objlist[i].peek_dscp():
                continue
            if traffic_control_listObj.peek_cp_dp_synchronized() is not None\
               and traffic_control_listObj.peek_cp_dp_synchronized() !=\
               objlist[i].peek_cp_dp_synchronized():
                continue
            if traffic_control_listObj.peek_vlan() is not None and\
               traffic_control_listObj.peek_vlan() != objlist[i].peek_vlan():
                continue
            if traffic_control_listObj.peek_l2cos() is not None and\
               traffic_control_listObj.peek_l2cos() !=\
               objlist[i].peek_l2cos():
                continue
            if traffic_control_listObj.peek_destination_address() is not None\
               and traffic_control_listObj.peek_destination_address() !=\
               objlist[i].peek_destination_address():
                continue
            if traffic_control_listObj.peek_admin_state_enabled() is not None\
               and traffic_control_listObj.peek_admin_state_enabled() !=\
               objlist[i].peek_admin_state_enabled():
                continue
            if traffic_control_listObj.peek_priority() is not None and\
               traffic_control_listObj.peek_priority() !=\
               objlist[i].peek_priority():
                continue
            if traffic_control_listObj.peek_non_terminated_enabled() is not\
               None and\
               traffic_control_listObj.peek_non_terminated_enabled() !=\
               objlist[i].peek_non_terminated_enabled():
                continue
            traffic_control_listlist.append(objlist[i])
    else:
        return objlist
    return traffic_control_listlist


def show_traffic_control_list(session, target_ve_port=None, action=None,
                              segment_preservation_enabled=None, port=None,
                              traffic_control_list_name=None,
                              source_address=None, target_slot=None,
                              target_dp_id=None, l4_protocol=None,
                              target_qos=None,
                              reset_propagation_enabled=None,
                              source_address_prefix_length=None,
                              application=None,
                              destination_address_prefix_length=None,
                              hit_count=None, dscp=None,
                              cp_dp_synchronized=None, vlan=None, l2cos=None,
                              destination_address=None,
                              admin_state_enabled=None, priority=None,
                              non_terminated_enabled=None):
    traffic_control_listObj = traffic_control_list()
    traffic_control_listObj.set_target_ve_port(target_ve_port)
    traffic_control_listObj.set_action(action)
    traffic_control_listObj.set_port(port)
    traffic_control_listObj.set_source_address(source_address)
    traffic_control_listObj.set_target_slot(target_slot)
    traffic_control_listObj.set_target_dp_id(target_dp_id)
    traffic_control_listObj.set_l4_protocol(l4_protocol)
    traffic_control_listObj.set_target_qos(target_qos)
    traffic_control_listObj.set_application(application)
    traffic_control_listObj.set_hit_count(hit_count)
    traffic_control_listObj.set_dscp(dscp)
    traffic_control_listObj.set_cp_dp_synchronized(cp_dp_synchronized)
    traffic_control_listObj.set_vlan(vlan)
    traffic_control_listObj.set_l2cos(l2cos)
    traffic_control_listObj.set_destination_address(destination_address)
    traffic_control_listObj.set_admin_state_enabled(admin_state_enabled)
    traffic_control_listObj.set_priority(priority)
    traffic_control_listObj.set_non_terminated_enabled(non_terminated_enabled)
    traffic_control_listObj.set_destination_address_prefix_length(
                             destination_address_prefix_length)
    traffic_control_listObj.set_source_address_prefix_length(
                             source_address_prefix_length)
    traffic_control_listObj.set_segment_preservation_enabled(
                             segment_preservation_enabled)
    traffic_control_listObj.set_traffic_control_list_name(
                             traffic_control_list_name)
    traffic_control_listObj.set_reset_propagation_enabled(
                             reset_propagation_enabled)
    return _show_traffic_control_list(session, traffic_control_listObj)


def validate(traffic_control_listObj):
    if traffic_control_listObj.peek_target_ve_port() is None or\
       traffic_control_listObj.peek_action() is None or\
       traffic_control_listObj.peek_segment_preservation_enabled() is None\
       or traffic_control_listObj.peek_port() is None or\
       traffic_control_listObj.peek_traffic_control_list_name() is None or\
       traffic_control_listObj.peek_source_address() is None or\
       traffic_control_listObj.peek_target_slot() is None or\
       traffic_control_listObj.peek_target_dp_id() is None or\
       traffic_control_listObj.peek_l4_protocol() is None or\
       traffic_control_listObj.peek_target_qos() is None or\
       traffic_control_listObj.peek_reset_propagation_enabled() is None or\
       traffic_control_listObj.peek_source_address_prefix_length() is None\
       or traffic_control_listObj.peek_application() is None or\
       traffic_control_listObj.peek_destination_address_prefix_length() is\
       None or traffic_control_listObj.peek_hit_count() is None or\
       traffic_control_listObj.peek_dscp() is None or\
       traffic_control_listObj.peek_cp_dp_synchronized() is None or\
       traffic_control_listObj.peek_vlan() is None or\
       traffic_control_listObj.peek_l2cos() is None or\
       traffic_control_listObj.peek_destination_address() is None or\
       traffic_control_listObj.peek_admin_state_enabled() is None or\
       traffic_control_listObj.peek_priority() is None or\
       traffic_control_listObj.peek_non_terminated_enabled() is None:
        return 0
    return 0


def main(argv):
    filters = ["target_ve_port", "action", "segment_preservation_enabled",
               "port", "traffic_control_list_name", "source_address",
               "target_slot", "target_dp_id", "l4_protocol", "target_qos",
               "reset_propagation_enabled", "source_address_prefix_length",
               "application", "destination_address_prefix_length",
               "hit_count", "dscp", "cp_dp_synchronized", "vlan", "l2cos",
               "destination_address", "admin_state_enabled", "priority",
               "non_terminated_enabled"]
    inputs = brcd_util.parse(argv, traffic_control_list, filters, validate)
    session = brcd_util.getsession(inputs)
    result = _show_traffic_control_list(session, inputs['utilobject'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
