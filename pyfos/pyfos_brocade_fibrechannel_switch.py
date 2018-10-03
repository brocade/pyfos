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

"""

:mod:`pyfos_brocade_fibrechannel_switch` - PyFOS module to provide rest \
        support for FC switch.
*********************************************************************************************************
The :mod:`pyfos_brocade_fibrechannel_switch` provides a REST support for \
        FC switch.

"""

import pyfos.pyfos_rest_util as pyfos_rest_util
from pyfos.pyfos_type import pyfos_type
import pyfos.pyfos_version as version

UNDEFINED = 0
ENABLE = 2
DISABLE = 3
TESTING = 7


class fibrechannel_switch(pyfos_rest_util.rest_object):
    """Class of FC switch

    Important class members:

        +-------------------------------+-------------------------------+------------------------------------------------------+
        | Attribute name                | Description                   |Frequently used methods                               |
        +===============================+===============================+======================================================+
        | name                          | WWN name of switch            |:meth:`set_name`                                      |
        |                               |                               |:meth:`peek_name`                                     |
        +-------------------------------+-------------------------------+------------------------------------------------------+
        | domain-id                     | domain id of switch           |:meth:`peek_domain_id`                                |
        +-------------------------------+-------------------------------+------------------------------------------------------+
        | user-friendly-name            | user friendly name of switch  |:meth:`set_user_friendly_name`                        |
        |                               |                               |:meth:`peek_user_friendly_name`                       |
        +-------------------------------+-------------------------------+------------------------------------------------------+
        | fcid                          | FCID of switch                |:meth:`peek_fcid`                                     |
        +-------------------------------+-------------------------------+------------------------------------------------------+
        | vf-id                         | VFID of switch                |:meth:`peek_vf_id`                                    |
        +-------------------------------+-------------------------------+------------------------------------------------------+
        | principal                     | indicate if principal or not  |:meth:`peek_principal`                                |
        +-------------------------------+-------------------------------+------------------------------------------------------+
        | enabled-state                 | Enabled or disabled state     |:meth:`set_enabled_state`                             |
        |                               |                               |:meth:`peek_enabled_state`                            |
        +-------------------------------+-------------------------------+------------------------------------------------------+
        +-------------------------------+-------------------------------+------------------------------------------------------+
        | up-time                       | Uptime of the switch          |:meth:`peek_up_time`                                  |
        +-------------------------------+-------------------------------+------------------------------------------------------+
        | model                         | Model of the switch           |:meth:`peek_model`                                    |
        +-------------------------------+-------------------------------+------------------------------------------------------+
        | firmware-version              | FOS version of switch         |:meth:`peek_firmware_version`                         |
        +-------------------------------+-------------------------------+------------------------------------------------------+
        | ip-address/ip-address         | List of IPv4/IPv6 address     |:meth:`set_ip_address_ip_address`                     |
        |                               | note the same name of         |:meth:`peek_ip_address_ip_address`                    |
        |                               | leaf list elements            |                                                      |
        +-------------------------------+-------------------------------+------------------------------------------------------+
        | ip-static-gateway-list/       | IPv4 and IPv6 static gateway  |:meth:`set_ip_static_gateway_list_ip_static_gateway`  |
        | ip-static-gateway             | addresses for the switch IP   |:meth:`peek_ip_static_gateway_list_ip_static_gateway` |
        +-------------------------------+-------------------------------+------------------------------------------------------+
        | subnet-mask                   | IPv4 subnet mask of the       |:meth:`set_subnet_mask`                               |
        |                               | switch IP network             |:meth:`peek_subnet_mask`                              |
        +-------------------------------+-------------------------------+------------------------------------------------------+
        | domain-name                   | DNS domain name of switch     |:meth:`set_domain_name`                               |
        |                               |                               |:meth:`peek_domain_name`                              |
        +-------------------------------+-------------------------------+------------------------------------------------------+
        | dns-servers/dns-server        | List of addresses of DNS      |:meth:`set_dns_servers_dns_server`                    |
        |                               | servers containing the map    |:meth:`peek_dns_servers_dns_server`                   |
        |                               | of switch domain name to      |                                                      |
        |                               | ipv4/ipv6 addresses.          |                                                      |
        +-------------------------------+-------------------------------+------------------------------------------------------+
        | fabric-user-friendly-name     | user friendly name of fabric  |:meth:`set_fabric_user_friendly_name`                 |
        |                               |                               |:meth:`peek_fabric_user_friendly_name`                |
        +-------------------------------+-------------------------------+------------------------------------------------------+
        | ag-mode                       | Enable or disable ag mode     |:meth:`set_ag_mode`                                   |
        |                               |                               |:meth:`peek_ag_mode`                                  |
        +-------------------------------+-------------------------------+------------------------------------------------------+
        | banner                        | Banner message while login    |:meth:`set_banner`                                    |
        |                               |                               |:meth:`peek_banner`                                   |
        +-------------------------------+-------------------------------+------------------------------------------------------+

        .. method:: get(session, name=None)

            Returns a :class:`fibrechannel_switch` object or a list of
            objects filled with attributes gathered
            from switch. If optional name is given, either an object
            matching the WWN of the switch is returned
            or an empty object is returned.

            Each object can be printed using :func:`pyfos_util.response_print`
            and individual attributes accessed through peek methods.

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: a :class:`fibrechannel_switch` object if there
                is only one switch within fabric or a list of
                objects if there are more than one

        .. method:: patch(session)

            Apply configurable attribute(s) within the object to switch.

            *Below is an example using individual sets:*

            .. code-block:: python

                # initialize the switch object
                switch = pyfos_switch.fibrechannel_switch()
                # set the enabled-state attribute to enable the switch
                switch.set_enabled_state(pyfos_switch.ENABLE)
                # execute HTTP patch command to apply the object to the
                # switch connected through session
                switch.patch(session)

            *Below is an example of combining object \
                    initialization and attribute sets:*

            .. code-block:: python

                # initialize the switch object and
                # set the enable-state attribute
                switch = pyfos_switch.fibrechannel_switch(
                    {"enabled-state" : pyfos_switch.ENABLE})
                # execute HTTP patch command to apply the object to the
                # switch connected through session
                switch.patch(session)

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: a dictionary of error or success information

    *Attribute methods*

        .. method:: set_name(name)

            Sets name in the object.

            :param name: WWN of the switch to be set within the object
            :rtype: None or dictionary of error information

        .. method:: peek_name()

            Reads name in the object.

            :rtype: None or WWN of the switch

        .. method:: set_domain_id(did)

            Sets Domain ID in the object.

            :param name: DID of the switch to be set within the object
            :rtype: None or dictionary of error information

        .. method:: peek_domain_id()

            Reads Domain ID in the object.

            :rtype: None or Domain ID of the switch

        .. method:: set_user_friendly_name(name)

            Sets user friendly name in the object.

            :rtype: None or dictionary of error information

        .. method:: peek_user_friendly_name()

            Reads user friendly name in the object.

            :rtype: None or user friendly name of the switch

        .. method:: peek_fcid()

            Reads FCID in the object.

            :rtype: None or FCID of the switch

        .. method:: peek_vf_id()

            Reads VFID in the object.

            :rtype: None or VFID of the switch

        .. method:: peek_principal()

            Reads boolean value as to if the switch is
            Principal switch or not in the object.

            :rtype: None, True, or False

        .. method:: set_enabled_state(newstate)

            Sets enabled state to :data:`ENABLE` or
                :data:`DISABLE` in the object.

            :rtype: None or dictionary of error information

        .. method:: peek_enabled_state()

            Reads enabled state of the switch in the object.

            :rtype: None or enabled state of :data:`ENABLE`,
                :data:`DISABLE`, :data:`UNDEFINED`, or :data:`TESTING`

        .. method:: peek_up_time()

            Reads uptime of the switch in the object.

            :rtype: None or uptime of the switch

        .. method:: peek_model()

            Reads model of the switch in the object.

            :rtype: None or model of the switch

        .. method:: peek_firmware_version()

            Reads FOS firmware version of the switch in the object.

            :rtype: None or FOS firmware version of the switch

        .. method:: set_ip_address_ip_address(ipaddress)

            Sets using a new list of IP addresses

            :rtype: None or dictionary of error information

        .. method:: peek_ip_address_ip_address()

            Reads a list of IP addresses of the switch in the object.

            :rtype: None or a list of IP addresses

        .. method:: set_ip_static_gateway_list_ip_static_gateway \
(ip-static-gateway-list)

            Sets new IPv4, IPv6 static gateway addresses for the switch.

            :rtype: None or dictionary of error information

        .. method:: peek_ip_static_gateway_list_ip_static_gateway()

            Reads the static gateway IP addresses set for the switch.

            :rtype: None or list of IPv4 and IPv6 static gateway addresses

        .. method:: set_subnet_mask(subnet_mask)

            Sets new subnet mask of the switch

            :rtype: None or dictionary of error information

        .. method:: peek_subnet_mask()

            Reads subnet mask of the swich.

            :rtype: None or subnet mask

        .. method:: set_domain_name(domain_name)

            Sets new domain name of the switch in DNS

            :rtype: None or dictionary of error information

        .. method:: peek_domain_name()

            Reads domain name in DNS of the switch in the object.

            :rtype: None or domain name

        .. method:: set_dns_servers_dns_server(dns-servers)

            Sets new DNS Servers for the switch with their IPv4/IPv6 addresses.

            :rtype: None or dictionary of error information

        .. method:: peek_dns_servers_dns_server()

            Reads the IP address of DNS servers set for the switch.

            :rtype: None or list of IP addresses

        .. method:: set_fabric_user_friendly_name(name)

            Sets fabric user friendly name in the object.

            :rtype: None or dictionary of error information

        .. method:: peek_fabric_user_friendly_name()

            Reads fabric user friendly name in the object.

            :rtype: None or fabric user friendly name of the switch

        .. method:: set_ag_mode(value)

            Sets the ag-mode enabled state of the switch.

            :rtype: None or dictionary of error information

        .. method:: peek_ag_mode()

            Reads Access Gateway mode in the object.
            :rtype: None or AG mode of the switch

        .. method:: set_banner(value)

           Sets the Banner message while login

           :rtype: None or dictionary of error information

        .. method:: peek_banner()

           Reads the Banner message while login

           :rtype: None or Banner message while login
         """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.switch,
                         "/rest/running/switch/fibrechannel-switch")

        self.add(pyfos_rest_util.rest_attribute(
            "name", pyfos_type.type_wwn,
            None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute(
            "domain-id", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "user-friendly-name", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "fcid", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "vf-id", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "principal", pyfos_type.type_bool,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "enabled-state", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "up-time", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "model", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "firmware-version", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "ip-address", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute(
            "ip-address", pyfos_type.type_ip_addr,
            None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST), ["ip-address"])
        self.add(pyfos_rest_util.rest_attribute(
            "ip-static-gateway-list", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER,
            version.VER_RANGE_821_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute(
            "ip-static-gateway", pyfos_type.type_ip_addr,
            None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST,
            version.VER_RANGE_821_and_ABOVE),
            ["ip-static-gateway-list"])
        self.add(pyfos_rest_util.rest_attribute(
            "subnet-mask", pyfos_type.type_ip_addr,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG,
            version.VER_RANGE_821_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute(
            "domain-name", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG,
            version.VER_RANGE_821_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute(
            "dns-servers", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER,
            version.VER_RANGE_821_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute(
            "dns-server", pyfos_type.type_ip_addr,
            None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST,
            version.VER_RANGE_821_and_ABOVE), ["dns-servers"])
        self.add(pyfos_rest_util.rest_attribute(
            "fabric-user-friendly-name", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "ag-mode", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "fcid-hex", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "banner", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.load(dictvalues, 1)
