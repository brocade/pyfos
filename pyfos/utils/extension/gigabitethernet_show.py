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


# gigabitethernet_show.py(pyGen v1.0.0)


"""

:mod:`gigabitethernet_show` - PyFOS util to show for gigabitethernet
*******************************************************************************
The:mod:`gigabitethernet_show` PyFOS util to show for gigabitethernet


The list of gigabitethernet interfaces on the device. System-controlled\
 interfaces created by the system are always present in this list, whether\
 they are configured or not.

gigabitethernet_show: usage

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
    * --enabled-state=ENABLED-STATE: Enabled or disabled state of the\
      brocade-interface-types:  0 : Disabled 1 : Enabled
    * --protocol=PROTOCOL: The GE port protocol configuration used by\
      Extension blade/Switch during deployment. When GE port protocol is\
      configured for LAN, the GE port is connected on the LAN side for\
      Extending LAN IP traffic over Extension tunnels using IP QOS\
      priorities. When the GE port protocol is configured for WAN then the\
      GE ports are connected on the WAN side and are used for configuring\
      the FCIP/Extension tunnels using them. In case of chassis system if\
      the slot is powered off or in faulty state then the leaf will be\
      skipped in display.  Supported values:  LAN : GE port is configured\
      for LAN side connections.  WAN : GE port is configured for WAN side\
      connections.
    * --persistent-disable=PERSISTENT-DISABLE: Indicates if the port is\
      persistently disabled or persistently enabled   1 : persistently\
      disabled  0 : persistently enabled
    * --mac-address=MAC-ADDRESS: MAC Address for the interface.
    * --operational-status=OPERATIONAL-STATUS: Operational status of the port:\
       1 : Online 2 : Offline
    * --portchannel-member-timeout=PORTCHANNEL-MEMBER-TIMEOUT: The dynamic\
      portchannel member timeout of the gigabit-ethernet interface. default\
      long.
    * --name=NAME: The name of the interface.
    * --auto-negotiation-enabled=AUTO-NEGOTIATION-ENABLED: Auto-negotiation is\
      enabled by default in 1G mode. In 10G mode it is disabled and not\
      supported. When the port is set for 1G mode, you can disable\
      auto-negotiation. In case of chassis system if the slot is powered off\
      or in faulty state then the leaf will be skipped in display. \
      Supported values:  true : Auto negotiation mode for GE port is\
      enabled.  false : Auto negotiation mode for GE port is disabled.
    * --lldp-enabled-state=LLDP-ENABLED-STATE: LLDP state of the port Possible\
      values are:  true  - LLDP is enabled on the port  false  - LLDP is\
      disabled on the port
    * --lldp-profile=LLDP-PROFILE: LLDP profile name configured on the port.\
      Blank lldp-profile means LLDP profile is not configured on this port.\
      In such case, lldp global parameters are in use for this port. To\
      configure a new profile or change existing profile on the port, user\
      should perform a PATCH operation with the profile name. To remove the\
      profile from the port, user should perform a PATCH operation with NULL\
      string.
    * --vlan=VLAN: Extension vlans configured on this port
    * --portchannel-name=PORTCHANNEL-NAME: The name of the portchannel that\
      the gigabit-ethernet interface belongs to. This will be NULL in case\
      the port is not portchannel member
    * --speed=SPEED: For PHY types that may operate at various speeds, this\
      leaf allows the interface to be forced to operate at a particular\
      speed.  Without any explicit configuration, gigabitethernet interfaces\
      run at the maximum capable speed.
* Output:
    * Python dictionary content with RESTCONF response data.


.. function:: gigabitethernet_show.show_gigabitethernet(session,\
enabled_state, protocol, persistent_disable, mac_address,\
operational_status, portchannel_member_timeout, name,\
auto_negotiation_enabled, lldp_enabled_state, lldp_profile,\
extension_vlans_vlan, portchannel_name, speed)

    *Show gigabitethernet*

    Example Usage of the Method::

            ret = gigabitethernet_show.show_gigabitethernet(session,\
 enabled_state, protocol, persistent_disable, mac_address,\
 operational_status, portchannel_member_timeout, name,\
 auto_negotiation_enabled, lldp_enabled_state, lldp_profile,\
 extension_vlans_vlan, portchannel_name, speed)
            print(ret)

    Details::

        gigabitethernetObj = gigabitethernet()
        gigabitethernetObj.set_enabled_state(enabled_state)
        gigabitethernetObj.set_protocol(protocol)
        gigabitethernetObj.set_persistent_disable(persistent_disable)
        gigabitethernetObj.set_mac_address(mac_address)
        gigabitethernetObj.set_operational_status(operational_status)
       \
 gigabitethernetObj.set_portchannel_member_timeout(\
 portchannel_member_timeout)
        gigabitethernetObj.set_name(name)
       \
 gigabitethernetObj.set_auto_negotiation_enabled(auto_negotiation_enabled)
        gigabitethernetObj.set_lldp_enabled_state(lldp_enabled_state)
        gigabitethernetObj.set_lldp_profile(lldp_profile)
        gigabitethernetObj.set_extension_vlans_vlan(extension_vlans_vlan)
        gigabitethernetObj.set_portchannel_name(portchannel_name)
        gigabitethernetObj.set_speed(speed)
        ret = _show_gigabitethernet(session, gigabitethernetObj)
        print(ret)

    **Inputs**

    :param session: The session returned by the login.
    :param enabled_state: Enabled or disabled state of the\
      brocade-interface-types:  0 : Disabled 1 : Enabled
    :param protocol: The GE port protocol configuration used by Extension\
      blade/Switch during deployment. When GE port protocol is configured\
      for LAN, the GE port is connected on the LAN side for Extending LAN IP\
      traffic over Extension tunnels using IP QOS priorities. When the GE\
      port protocol is configured for WAN then the GE ports are connected on\
      the WAN side and are used for configuring the FCIP/Extension tunnels\
      using them. In case of chassis system if the slot is powered off or in\
      faulty state then the leaf will be skipped in display.  Supported\
      values:  LAN : GE port is configured for LAN side connections.  WAN :\
      GE port is configured for WAN side connections.
    :param persistent_disable: Indicates if the port is persistently disabled\
      or persistently enabled   1 : persistently disabled  0 : persistently\
      enabled
    :param mac_address: MAC Address for the interface.
    :param operational_status: Operational status of the port:  1 : Online 2 :\
      Offline
    :param portchannel_member_timeout: The dynamic portchannel member timeout\
      of the gigabit-ethernet interface. default long.
    :param name: The name of the interface.
    :param auto_negotiation_enabled: Auto-negotiation is enabled by default in\
      1G mode. In 10G mode it is disabled and not supported. When the port\
      is set for 1G mode, you can disable auto-negotiation. In case of\
      chassis system if the slot is powered off or in faulty state then the\
      leaf will be skipped in display.  Supported values:  true : Auto\
      negotiation mode for GE port is enabled.  false : Auto negotiation\
      mode for GE port is disabled.
    :param lldp_enabled_state: LLDP state of the port Possible values are: \
      true  - LLDP is enabled on the port  false  - LLDP is disabled on the\
      port
    :param lldp_profile: LLDP profile name configured on the port. Blank\
      lldp-profile means LLDP profile is not configured on this port. In\
      such case, lldp global parameters are in use for this port. To\
      configure a new profile or change existing profile on the port, user\
      should perform a PATCH operation with the profile name. To remove the\
      profile from the port, user should perform a PATCH operation with NULL\
      string.
    :param extension_vlans_vlan: Extension vlans configured on this port
    :param portchannel_name: The name of the portchannel that the\
      gigabit-ethernet interface belongs to. This will be NULL in case the\
      port is not portchannel member
    :param speed: For PHY types that may operate at various speeds, this leaf\
      allows the interface to be forced to operate at a particular speed. \
      Without any explicit configuration, gigabitethernet interfaces run at\
      the maximum capable speed.

    **Output**

    :rtype: None or one/more instance of class gigabitethernet on Success  or\
    a dictionary with error.

"""


# Start utils imports
import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_interface import gigabitethernet

from pyfos.utils import brcd_util
# End module imports


def _show_gigabitethernet(session, gigabitethernetObj):
    objlist = gigabitethernet.get(session)
    gigabitethernetlist = list()
    if isinstance(objlist, gigabitethernet):
        objlist = [objlist]
    if isinstance(objlist, list):
        for i in range(len(objlist)):
            if gigabitethernetObj.peek_enabled_state() is not None and\
               gigabitethernetObj.peek_enabled_state() !=\
               objlist[i].peek_enabled_state():
                continue
            if gigabitethernetObj.peek_protocol() is not None and\
               gigabitethernetObj.peek_protocol() !=\
               objlist[i].peek_protocol():
                continue
            if gigabitethernetObj.peek_persistent_disable() is not None and\
               gigabitethernetObj.peek_persistent_disable() !=\
               objlist[i].peek_persistent_disable():
                continue
            if gigabitethernetObj.peek_mac_address() is not None and\
               gigabitethernetObj.peek_mac_address() !=\
               objlist[i].peek_mac_address():
                continue
            if gigabitethernetObj.peek_operational_status() is not None and\
               gigabitethernetObj.peek_operational_status() !=\
               objlist[i].peek_operational_status():
                continue
            if gigabitethernetObj.peek_portchannel_member_timeout() is not\
               None and gigabitethernetObj.peek_portchannel_member_timeout()\
               != objlist[i].peek_portchannel_member_timeout():
                continue
            if gigabitethernetObj.peek_name() is not None and\
               gigabitethernetObj.peek_name() != objlist[i].peek_name():
                continue
            if gigabitethernetObj.peek_auto_negotiation_enabled() is not None\
               and gigabitethernetObj.peek_auto_negotiation_enabled() !=\
               objlist[i].peek_auto_negotiation_enabled():
                continue
            if gigabitethernetObj.peek_lldp_enabled_state() is not None and\
               gigabitethernetObj.peek_lldp_enabled_state() !=\
               objlist[i].peek_lldp_enabled_state():
                continue
            if gigabitethernetObj.peek_lldp_profile() is not None and\
               gigabitethernetObj.peek_lldp_profile() !=\
               objlist[i].peek_lldp_profile():
                continue
            if gigabitethernetObj.peek_extension_vlans_vlan() != [] and\
               gigabitethernetObj.peek_extension_vlans_vlan() !=\
               objlist[i].peek_extension_vlans_vlan():
                continue
            if gigabitethernetObj.peek_portchannel_name() is not None and\
               gigabitethernetObj.peek_portchannel_name() !=\
               objlist[i].peek_portchannel_name():
                continue
            if gigabitethernetObj.peek_speed() is not None and\
               gigabitethernetObj.peek_speed() != objlist[i].peek_speed():
                continue
            gigabitethernetlist.append(objlist[i])
    else:
        return objlist
    return gigabitethernetlist


def show_gigabitethernet(session, enabled_state=None, protocol=None,
                         persistent_disable=None, mac_address=None,
                         operational_status=None,
                         portchannel_member_timeout=None, name=None,
                         auto_negotiation_enabled=None,
                         lldp_enabled_state=None, lldp_profile=None,
                         extension_vlans_vlan=None, portchannel_name=None,
                         speed=None):
    gigabitethernetObj = gigabitethernet()
    gigabitethernetObj.set_enabled_state(enabled_state)
    gigabitethernetObj.set_protocol(protocol)
    gigabitethernetObj.set_persistent_disable(persistent_disable)
    gigabitethernetObj.set_mac_address(mac_address)
    gigabitethernetObj.set_operational_status(operational_status)
    gigabitethernetObj.set_portchannel_member_timeout(
                       portchannel_member_timeout)
    gigabitethernetObj.set_name(name)
    gigabitethernetObj.set_auto_negotiation_enabled(auto_negotiation_enabled)
    gigabitethernetObj.set_lldp_enabled_state(lldp_enabled_state)
    gigabitethernetObj.set_lldp_profile(lldp_profile)
    gigabitethernetObj.set_extension_vlans_vlan(extension_vlans_vlan)
    gigabitethernetObj.set_portchannel_name(portchannel_name)
    gigabitethernetObj.set_speed(speed)
    return _show_gigabitethernet(session, gigabitethernetObj)


def validate(gigabitethernetObj):
    if gigabitethernetObj.peek_enabled_state() is None or\
       gigabitethernetObj.peek_protocol() is None or\
       gigabitethernetObj.peek_persistent_disable() is None or\
       gigabitethernetObj.peek_mac_address() is None or\
       gigabitethernetObj.peek_operational_status() is None or\
       gigabitethernetObj.peek_portchannel_member_timeout() is None or\
       gigabitethernetObj.peek_name() is None or\
       gigabitethernetObj.peek_auto_negotiation_enabled() is None or\
       gigabitethernetObj.peek_lldp_enabled_state() is None or\
       gigabitethernetObj.peek_lldp_profile() is None or\
       gigabitethernetObj.peek_extension_vlans_vlan() == [] or\
       gigabitethernetObj.peek_portchannel_name() is None or\
       gigabitethernetObj.peek_speed() is None:
        return 0
    return 0


def main(argv):
    filters = ["enabled_state", "protocol", "persistent_disable",
               "mac_address", "operational_status",
               "portchannel_member_timeout", "name",
               "auto_negotiation_enabled", "lldp_enabled_state",
               "lldp_profile", "extension_vlans_vlan", "portchannel_name",
               "speed"]
    inputs = brcd_util.parse(argv, gigabitethernet, filters, validate)
    session = brcd_util.getsession(inputs)
    result = _show_gigabitethernet(session, inputs['utilobject'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
