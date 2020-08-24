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

:mod:`pyfos_brocade_fibrechannel_switch` - PyFOS module to provide REST \
        support for an FC switch.
*********************************************************************************************************
The :mod:`pyfos_brocade_fibrechannel_switch` provides a REST support for \
        an FC switch.

"""

from pyfos import pyfos_rest_util
from pyfos.pyfos_type import pyfos_type
import pyfos.pyfos_version as version

UNDEFINED = 0
ENABLE = 2
DISABLE = 3
TESTING = 7


class fibrechannel_switch(pyfos_rest_util.rest_object):
    """Class of FC Switch

    Important Class Members:

        +------------------------------------+-------------------------------+------------------------------------------------------+
        | Attribute Name                     | Description                   |Frequently Used Methods                               |
        +====================================+===============================+======================================================+
        | name                               | The WWN name of switch.       |:meth:`set_name`                                      |
        |                                    |                               |:meth:`peek_name`                                     |
        +------------------------------------+-------------------------------+------------------------------------------------------+
        | domain-id                          | The domain ID of the switch.  |:meth:`peek_domain_id`                                |
        +------------------------------------+-------------------------------+------------------------------------------------------+
        | user-friendly-name                 | The user friendly name of     |:meth:`set_user_friendly_name`                        |
        |                                    | the switch.                   |:meth:`peek_user_friendly_name`                       |
        +------------------------------------+-------------------------------+------------------------------------------------------+
        | fcid                               | The FCID of the switch.       |:meth:`peek_fcid`                                     |
        +------------------------------------+-------------------------------+------------------------------------------------------+
        | vf-id                              | The VFID of the switch.       |:meth:`peek_vf_id`                                    |
        +------------------------------------+-------------------------------+------------------------------------------------------+
        | principal                          | Whether principal or not.     |:meth:`peek_principal`                                |
        +------------------------------------+-------------------------------+------------------------------------------------------+
        | enabled-state                      | Enabled or disabled state.    |:meth:`set_enabled_state`                             |
        |                                    |                               |:meth:`peek_enabled_state`                            |
        +------------------------------------+-------------------------------+------------------------------------------------------+
        | up-time                            | The uptime of the switch.     |:meth:`peek_up_time`                                  |
        +------------------------------------+-------------------------------+------------------------------------------------------+
        | model                              | The model of the switch.      |:meth:`peek_model`                                    |
        +------------------------------------+-------------------------------+------------------------------------------------------+
        | firmware-version                   |The FOS version of the switch. |:meth:`peek_firmware_version`                         |
        +------------------------------------+-------------------------------+------------------------------------------------------+
        | ip-address/ip-address              | A list of IPv4/IPv6           |:meth:`set_ip_address_ip_address`                     |
        |                                    | addresses.                    |:meth:`peek_ip_address_ip_address`                    |
        |                                    |                               |                                                      |
        +------------------------------------+-------------------------------+------------------------------------------------------+
        | ip-static-gateway-list/            | IPv4 and IPv6 static gateway  |:meth:`set_ip_static_gateway_list_ip_static_gateway`  |
        | ip-static-gateway                  | addresses for the switch IP.  |:meth:`peek_ip_static_gateway_list_ip_static_gateway` |
        +------------------------------------+-------------------------------+------------------------------------------------------+
        | subnet-mask                        | IPv4 subnet mask of the       |:meth:`set_subnet_mask`                               |
        |                                    | switch IP network.            |:meth:`peek_subnet_mask`                              |
        +------------------------------------+-------------------------------+------------------------------------------------------+
        | domain-name                        |The DNS domain name of switch. |:meth:`set_domain_name`                               |
        |                                    |                               |:meth:`peek_domain_name`                              |
        +------------------------------------+-------------------------------+------------------------------------------------------+
        | dns-servers/dns-server             | A list of addresses of DNS    |:meth:`set_dns_servers_dns_server`                    |
        |                                    | servers containing the map    |:meth:`peek_dns_servers_dns_server`                   |
        |                                    | of switch domain names to     |                                                      |
        |                                    | IPv4/IPv6 addresses.          |                                                      |
        +------------------------------------+-------------------------------+------------------------------------------------------+
        | fabric-user-friendly-name          | The user friendly name of     |:meth:`set_fabric_user_friendly_name`                 |
        |                                    | the fabric.                   |:meth:`peek_fabric_user_friendly_name`                |
        +------------------------------------+-------------------------------+------------------------------------------------------+
        | ag-mode                            | Enables or disables AG mode.  |:meth:`set_ag_mode`                                   |
        |                                    |                               |:meth:`peek_ag_mode`                                  |
        +------------------------------------+-------------------------------+------------------------------------------------------+
        | banner                             | The login banner message.     |:meth:`set_banner`                                    |
        |                                    |                               |:meth:`peek_banner`                                   |
        +------------------------------------+-------------------------------+------------------------------------------------------+
        | is-enabled-state                   | Enabled or disabled state.    |:meth:`set_is_enabled_state`                          |
        |                                    |                               |:meth:`peek_is_enabled_state`                         |
        +------------------------------------+-------------------------------+------------------------------------------------------+
        | operational-status                 | Current state of the switch.  |:meth:`peek_operational_status`                       |
        +------------------------------------+-------------------------------+------------------------------------------------------+
        | in-order-delivery-enabled          | Enables or disables the In    |:meth:`set_in_order_delivery_enabled`                 |
        |                                    | Order Delivery (IOD)          |:meth:`peek_in_order_delivery_enabled`                |
        |                                    | capability for switch.        |                                                      |
        +------------------------------------+-------------------------------+------------------------------------------------------+
        | dynamic-load-sharing               | Current state of the          |:meth:`set_dynamic_load_sharing`                      |
        |                                    | dynamic-load-sharing (DLS)    |:meth:`peek_dynamic_load_sharing`                     |
        |                                    | state for switch.             |                                                      |
        +------------------------------------+-------------------------------+------------------------------------------------------+
        | advanced-performance-tuning-policy | Current policy for the        |:meth:`set_advanced_performance_tuning_policy`        |
        |                                    | Advanced Performance Tuning   |:meth:`peek_advanced_performance_tuning_policy`       |
        |                                    | control of the switch.        |                                                      |
        +------------------------------------+-------------------------------+------------------------------------------------------+
        | lacp-system-priority               | The LACP system priority of   |:meth:`set_lacp_system_priority`                      |
        |                                    | the switch. This is used for  |:meth:`peek_lacp_system_priority`                     |
        |                                    | determining the system that is|                                                      |
        |                                    | responsible for resolving     |                                                      |
        |                                    | conflicts in the choice of LAG|                                                      |
        |                                    | groups.A lower numerical value|                                                      |
        |                                    | has a higher prioity          |                                                      |
        +------------------------------------+-------------------------------+------------------------------------------------------+
        | lacp-system-mac-address            | The LACP system MAC address of|:meth:`peek_lacp_system_mac_address`                  |
        |                                    | of the switch.                |                                                      |
        +------------------------------------+-------------------------------+------------------------------------------------------+

    *Object methods*

        .. method:: get(session, name=None)

            Returns a :class:`fibrechannel_switch` object or a list of
            objects with attributes gathered from the switch. \
            If an optional name is given, returns either an object
            matching the WWN of the switch or an empty object.

            Each object can be printed using :func:`pyfos_util.response_print`,
            and individual attributes can be accessed through peek methods.

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A :class:`fibrechannel_switch` object if there
                is only one switch within the fabric or a list of
                objects if there is more than one switch.

        .. method:: patch(session)

            Applies configurable attribute(s) within the object to the switch.

            *Below Is an Example Using Individual Sets:*

            .. code-block:: python

                # initialize the switch object
                switch = pyfos_switch.fibrechannel_switch()
                # set the enabled-state attribute to enable the switch
                switch.set_enabled_state(pyfos_switch.ENABLE)
                # execute HTTP patch command to apply the object to the
                # switch connected through session
                switch.patch(session)

            *Below Is an Example of Combining Object \
                    Initialization and Attribute Sets:*

            .. code-block:: python

                # initialize the switch object and
                # set the enable-state attribute
                switch = pyfos_switch.fibrechannel_switch(
                    {"enabled-state" : pyfos_switch.ENABLE})
                # execute HTTP patch command to apply the object to the
                # switch connected through session
                switch.patch(session)

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary of errors or success information.

    *Attribute Methods*

        .. method:: set_name(name)

            Sets the name in the object.

            :param name: The WWN of the switch to be set within the object.
            :rtype: None or a dictionary of error information.

        .. method:: peek_name()

            Reads the name in the object.

            :rtype: None or the WWN of the switch.

        .. method:: set_domain_id(did)

            Sets the domain ID in the object.

            :param did: The DID of the switch to be set within the object.
            :rtype: None or a dictionary of error information.

        .. method:: peek_domain_id()

            Reads the domain ID in the object.

            :rtype: None or the domain ID of the switch.

        .. method:: set_user_friendly_name(name)

            Sets the user friendly name in the object.

            :rtype: None or a dictionary of error information.

        .. method:: peek_user_friendly_name()

            Reads the user friendly name in the object.

            :rtype: None or the user friendly name of the switch.

        .. method:: peek_fcid()

            Reads the FCID in the object.

            :rtype: None or the FCID of the switch.

        .. method:: peek_vf_id()

            Reads the VFID in the object.

            :rtype: None or the VFID of the switch.

        .. method:: peek_principal()

            Reads the boolean value to determine if the switch is
            the principal switch or not in the object.

            :rtype: None, True, or False.

        .. method:: set_enabled_state(newstate)

            Sets the enabled state to :data:`ENABLE` or
                :data:`DISABLE` in the object.

            :rtype: None or a dictionary of error information.

        .. method:: peek_enabled_state()

            Reads the enabled state of the switch in the object.

            :rtype: None or an enabled state of :data:`ENABLE`,
                :data:`DISABLE`, :data:`UNDEFINED`, or :data:`TESTING`.

        .. method:: peek_up_time()

            Reads the uptime of the switch in the object.

            :rtype: None or the uptime of the switch.

        .. method:: peek_model()

            Reads the model of the switch in the object.

            :rtype: None or the model of the switch.

        .. method:: peek_firmware_version()

            Reads the FOS firmware version of the switch in the object.

            :rtype: None or the FOS firmware version of the switch.

        .. method:: set_ip_address_ip_address(ipaddress)

            Sets using a new list of IP addresses.

            :rtype: None or a dictionary of error information.

        .. method:: peek_ip_address_ip_address()

            Reads a list of IP addresses of the switch in the object.

            :rtype: None or a list of IP addresses.

        .. method:: set_ip_static_gateway_list_ip_static_gateway \
(ip-static-gateway-list)

            Sets the new IPv4/IPv6 static gateway addresses for the switch.

            :rtype: None or a dictionary of error information.

        .. method:: peek_ip_static_gateway_list_ip_static_gateway()

            Reads the static gateway IP addresses set for the switch.

            :rtype: None or a list of IPv4 and IPv6 static gateway addresses.

        .. method:: set_subnet_mask(subnet_mask)

            Sets the new subnet mask of the switch.

            :rtype: None or a dictionary of error information.

        .. method:: peek_subnet_mask()

            Reads the subnet mask of the switch.

            :rtype: None or the subnet mask.

        .. method:: set_domain_name(domain_name)

            Sets the domain name of the switch in DNS.

            :rtype: None or a dictionary of error information.

        .. method:: peek_domain_name()

            Reads the DNS domain name of the switch in the object.

            :rtype: None or the domain name.

        .. method:: set_dns_servers_dns_server(dns-servers)

            Sets the DNS servers for the switch with their \
            IPv4/IPv6 addresses.

            :rtype: None or a dictionary of error information.

        .. method:: peek_dns_servers_dns_server()

            Reads the IP address of the DNS servers set for the switch.

            :rtype: None or a list of IP addresses.

        .. method:: set_fabric_user_friendly_name(name)

            Sets the fabric user friendly name in the object.

            :rtype: None or a dictionary of error information.

        .. method:: peek_fabric_user_friendly_name()

            Reads the fabric user friendly name in the object.

            :rtype: None or the fabric user friendly name of the switch.

        .. method:: set_ag_mode(value)

            Sets the AG mode enabled state of the switch.

            :rtype: None or a dictionary of error information.

        .. method:: peek_ag_mode()

            Reads the Access Gateway mode in the object.

            :rtype: None or the AG mode of the switch.

        .. method:: set_banner(value)

           Sets the banner message displayed during login.

           :rtype: None or a dictionary of error information.

        .. method:: peek_banner()

           Reads the banner message displayed during login.

           :rtype: None or the login banner message.

        .. method:: set_is_enabled_state(newstate)

            Sets the enabled state to :data:`ENABLE` or
                :data:`DISABLE` in the object.

            :rtype: None or a dictionary of error information.

        .. method:: peek_is_enabled_state()

            Reads the enabled state of the switch in the object.

            :rtype: None or enabled state of :data:`ENABLE`,
                :data:`DISABLE`.

        .. method:: peek_operational_status()

            Reads the state of the switch in the object.

            :rtype: None or enabled state of :data:`ENABLE`,
                :data:`DISABLE`, :data:`UNDEFINED`, or :data:`TESTING`.

        .. method:: set_in_order_delivery_enabled(newstate)

            Enables or disables the In Order Delivery (IOD) feature of
                a switch in the object.

            :param newstate: A boolean state to enable or disable  the IOD
                feature.
            :rtype: None or a dictionary of error information.

        .. method:: peek_in_order_delivery_enabled()

            Reads the In Order Delivery (IOD) feature's state of a switch
                in the object.

            :rtype: None or enabled state of :data:`ENABLE`,
                :data:`DISABLE`.

        .. method:: set_dynamic_load_sharing(newcapability)

            Sets the dynamic-load-sharing (DLS) capability of a switch
                in the object.

            :param newcapability: One of the following strings for the desired
                capability: :data:`disabled`, :data:`dls`,
                :data:`lossless-dls`, or :data:`two-hop-lossless-dls`.

            :rtype: None or a dictionary of error information.

        .. method:: peek_dynamic_load_sharing()

            Reads the dynamic-load-sharing capability of a switch in
                the object.

            :rtype: None or the string :data:`disabled`, :data:`dls`,
                :data:`lossless-dls`, or :data:`two-hop-lossless-dls`.

        .. method:: set_advanced_performance_tuning_policy(newpolicy)

            Sets the Advanced Performance Tuning (APT) policy used by the
                switch in the object.

            :param newpolicy: One of the following supported policies:
                :data:`port-based`, :data:`device-based` (FICON support only),
                or :data:`exchange-based`.

            :rtype: None or a dictionary of error information.

        .. method:: peek_advanced_performance_tuning_policy()

            Reads the current Advanced Performance Tuning (APT) policy
                of switch in the object.

            :rtype: None or the string :data:`port-based`,
                :data:`device-based`, or :data:`exchange-based`.

        .. method:: set_lacp_system_priority(sysPriority)

            Sets the system priority of lacp.

            :rtype: None or a dictionary of error information.

        .. method:: peek_lacp_system_priority()

            Reads the lacp system priority value from the switch Object

            :rtype: None on error and value on success

        .. method:: peek_lacp_system_mac_address()

            Reads the LACP system MAC address from the switch Object

            :rtype: None on error and value on success
         """

    def __init__(self, dictvalues={}):
        urilist = list([dict({'URIVER': version.VER_RANGE_820_TO_821A,
                              'URI': "/rest/running/switch/" +
                              "fibrechannel-switch"}),
                        dict({'URIVER': version.VER_RANGE_821b_and_ABOVE,
                              'URI': "/rest/running/brocade-fibrechannel" +
                              "-switch/fibrechannel-switch"})])
        super().__init__(pyfos_rest_util.rest_obj_type.switch, urilist)
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
        self.add(pyfos_rest_util.rest_attribute(
            "is-enabled-state", pyfos_type.type_bool,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG,
            version.VER_RANGE_821b_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute(
            "operational-status", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG,
            version.VER_RANGE_821b_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute(
            "dynamic-load-sharing", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG,
            version.VER_RANGE_900_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute(
            "in-order-delivery-enabled", pyfos_type.type_bool,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG,
            version.VER_RANGE_900_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute(
            "advanced-performance-tuning-policy", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG,
            version.VER_RANGE_900_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute(
            "lacp-system-priority", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG,
            version.VER_RANGE_900_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute(
            "lacp-system-mac-address", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG,
            version.VER_RANGE_900_and_ABOVE))

        self.load(dictvalues, 1)


class topology_domain(pyfos_rest_util.rest_object):
    """Class representing each domain in the fabric that is reachable from
    the queried switch, and the results of the most recent Fabric Shortest
    Path First calculation detailing how the queried switch reaches the
    specified destination domain.

    Important Class Members:

        +---------------------------+--------------------------------+----------------------------------------+
        | Attribute Name            | Description                    |Frequently Used Methods                 |
        +===========================+================================+========================================+
        | domain-id                 | Destination fabric domain.     | :meth:`peek_domain_id`                 |
        +---------------------------+--------------------------------+----------------------------------------+
        | path-count                | The number of lowest, equal    | :meth:`peek_path_count`                |
        |                           | cost paths available.          |                                        |
        +---------------------------+--------------------------------+----------------------------------------+
        | metric                    | Lowest path cost of the in-use | :meth:`peek_metric`                    |
        |                           | paths to reach the domain.     |                                        |
        +---------------------------+--------------------------------+----------------------------------------+
        | is-local-translate-domain | If the destination domain is   | :meth:`peek_is_local_translate_domain` |
        |                           | reachable via a local EX-Port. |                                        |
        +---------------------------+--------------------------------+----------------------------------------+
        | out-ports                 | The local ports used for       | :meth:`peek_out_ports`                 |
        |                           | routing traffic to the domain. |                                        |
        +---------------------------+--------------------------------+----------------------------------------+

    *Object methods*

        .. method:: get(session, domain_id=None)

            Returns a :class:`topology_domain` object with details from the
            switch, list of :class:`topology_domain` objects, or a dictionary
            with error information. If the optional :class:`domain_id`
            parameter is given, the corresponding :class:`topology_domain`
            object is returned, or a dict of error information.

            Each object can be printed using :func:`pyfos_util.response_print`,
            and individual attributes can be accessed through peek methods.

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :param domain_id: The destination domain for which to get local
                out ports to use for reaching the domain. Defaults to None.
            :type domain_id: int, optional
            :rtype: A :class:`topology_domain` object, list of
                :class:`topology_domain` objects, or dictionary with error
                information.

    *Attribute Methods*

        .. method:: peek_domain_id()

            Gets the domain ID in the object.

            :rtype: None or an integer of the domain ID

        .. method:: peek_path_count()

            Gets the number of lowest, equal cost paths available as of the
            last Fabric Shortest Path First calculations.

            :rtype: None or an integer of the number of paths

        .. method:: peek_metric()

            Gets the path cost associated with routing to domain.

            :rtype: None or an integer of the path cost.

        .. method:: peek_is_local_translate_domain

            Gets a flag indicating if the domain is reachable via a local
            EX-Port.

            :rtype: None or boolean

        .. method:: peek_out_ports()

            Gets the list of local ports that are programmed for routing \
            traffic to the domain.

            :rtype: A dictionary with a list of the out ports as strings
        """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.fabric_topology_domain,
                         "/rest/running/brocade-fibrechannel-switch/" +
                         "topology-domain",
                         version.VER_RANGE_900_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "domain-id", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute(
            "path-count", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "metric", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "is-local-translate-domain", pyfos_type.type_bool,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "out-ports", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute(
            "port", pyfos_type.type_na,
            None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST),
            ['out-ports'])

        self.load(dictvalues, 1)


class topology_route(pyfos_rest_util.rest_object):
    """Class containing a mapping of how the switch's ports are routed, as
    ingress ports, to their corresponding egress ports for frames destined
    to the specified destination domain. Reports the greatest number of hops
    across all the equal cost paths to reach the specified destination domain.

    Important Class Members:

        +----------------+-----------------------------------+----------------------------------------+
        | Attribute Name | Description                       | Frequently Used Methods                |
        +================+===================================+========================================+
        | domain-id      | Destination fabric domain for the | :meth:`peek_domain_id`                 |
        |                | shown routes.                     |                                        |
        +----------------+-----------------------------------+----------------------------------------+
        | hop-count      | Greatest number of hops among all | :meth:`peek_hop_count`                 |
        |                | equal cost paths used by this     |                                        |
        |                | switch to reach the domain.       |                                        |
        +----------------+-----------------------------------+----------------------------------------+
        | out-port       | The egress port for these ingress | :meth:`peek_out_port`                  |
        |                | ports, for traffic to the domain. |                                        |
        +----------------+-----------------------------------+----------------------------------------+
        | in-ports       | The switch's ports that are       | :meth:`peek_in_ports`                  |
        |                | routed this out-port for frames   |                                        |
        |                | destined to the domain.           |                                        |
        +----------------+-----------------------------------+----------------------------------------+

    *Object methods*

        .. method:: get(session)

            Returns a list of :class:`topology_route` objects, an empty
            :class:`topology_route` object, or a dictionary with error
            information.

            Each object can be printed using :func:`pyfos_util.response_print`,
            and individual attributes can be accessed through peek methods.

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A list of :class:`topology_route` objects, an empty
                :class:`topology_route` object, or dictionary with error
                information.

    *Attribute Methods*

        .. method:: peek_domain_id()

            Gets the domain ID for the object.

            :rtype: None or an integer of the domain ID.

        .. method:: peek_hop_count()

            Gets the number of hops to the destination domain from the
            object. This is the largest number of hops across all equal cost
            paths to reach the domain.

            :rtype: None or an integer of the number of hops.

        .. method:: peek_out_port()

            Gets the out-port or egress port that these ingress ports are
            utilizing.

            :rtype: None or the out-port as an integer.

        .. method:: peek_in_ports()

            Gets the list of local ports that are utilizing this out-port.

            :rtype: A dictionary with a list of the out ports as strings
        """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.fabric_topology_route,
                         "/rest/running/brocade-fibrechannel-switch/" +
                         "topology-route",
                         version.VER_RANGE_900_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "domain-id", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "hop-count", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "out-port", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "in-ports", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute(
            "port", pyfos_type.type_na,
            None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST),
            ['in-ports'])

        self.load(dictvalues, 1)
