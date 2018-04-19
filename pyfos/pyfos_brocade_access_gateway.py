# Copyright © 2018 Broadcom.  All rights reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.
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

:mod:`pyfos_brocade_access_gateway` - PyFOS Module to Provide \
        REST Support for Access Gateway.
*******************************************************************************************************
The :mod:`pyfos_brocade_access_gateway` module provides REST support \
        for the Access Gateway.

"""

import pyfos.pyfos_rest_util as pyfos_rest_util
from pyfos.pyfos_type import pyfos_type
import pyfos.pyfos_version as version


class port_group(pyfos_rest_util.rest_object):
    """ This class provides methods/options to retrieve
    and configure port groups. The port groups can be configured
    provided that the port-group AG policy is activated.

    Important Class Members:

        +------------------------------------------------+----------------------------------+--------------------------------------------------------------------------+
        | Attribute Name                                 | Description                      |Frequently Used Methods                                                   |
        +================================================+==================================+==========================================================================+
        | port-group-id                                  | Port group ID.                   |:func:`set_port_group_id`                                                 |
        |                                                |                                  |:func:`peek_port_group_id`                                                |
        +------------------------------------------------+----------------------------------+--------------------------------------------------------------------------+
        | port-group-name                                | Port group name.                 |:func:`set_port_group_name`                                               |
        |                                                |                                  |:func:`peek_port_group_name`                                              |
        +------------------------------------------------+----------------------------------+--------------------------------------------------------------------------+
        | port-group-n-ports/n-port                      | N_Ports present in the port      |:func:`set_port_group_n_ports_n_port`                                     |
        |                                                | group.                           |:func:`peek_port_group_n_ports_n_port`                                    |
        +------------------------------------------------+----------------------------------+--------------------------------------------------------------------------+
        | port-group-f-ports/f-port                      | F_Ports present in the port      |:func:`set_port_group_f_ports_f_port`                                     |
        |                                                | group.                           |:func:`peek_port_group_f_ports_f_port`                                    |
        +------------------------------------------------+----------------------------------+--------------------------------------------------------------------------+
        | port-group-mode/                               | Whether load balancing mode is   |:func:`set_port_group_mode_load_balancing_mode_enabled`                   |
        |   load-balancing-mode-enabled                  | enabled in the port group.       |:func:`peek_port_group_mode_load_balancing_mode_enabled`                  |
        +------------------------------------------------+----------------------------------+--------------------------------------------------------------------------+
        | port-group-mode/                               | Whether multiple fabric name     |:func:`set_port_group_mode_multiple_fabric_name_monitoring_mode_enabled`  |
        |   multiple-fabric-name-monitoring-mode-enabled | monitoring mode is enabled in    |:func:`peek_port_group_mode_multiple_fabric_name_monitoring_mode_enabled` |
        |                                                | the port group.                  |                                                                          |
        +------------------------------------------------+----------------------------------+--------------------------------------------------------------------------+

    *Object Methods*

        .. method:: get()

            Returns the :class:`port_group`
            object with values for all the attributes.
            The object can be printed using :func:`pyfos_utils.response_print`.

            :param session: Session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: Dictionary of error or
                :class:`port_group` object.

        .. method:: post()

            Creates an entry or adds members. Fields involved are set
            within the object using the attribute's set method.
            This method is used to create a new port group with a group
            of N_Ports or to add N_Ports or F_Ports to an existing port group.

            Example usage of the method to create a new port group:

            .. code-block:: python

                portgroup_obj =
                    pyfos_brocade_access_gateway.port_group()
                portgroup_obj.set_port_group_id(1)
                portgroup_obj.set_port_group_n_ports_n_port("0/40;0/41")
                portgroup_obj.post(session)

            The above example will add N_Ports if the port group with ID 1
            exists already.

            :param session: Session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: Dictionary of error or success response.

        .. method:: patch()

            Replace entry members. Fields involved are set within the object
            using the attribute's set method. This command is used to
            replace the existing member N_Ports or F_Ports, the
            rename port group, and the enable or disable port group modes.

            Example usage of the method to enable load balancing mode in a PG:

            .. code-block:: python

                portgroup_obj =
                    pyfos_brocade_access_gateway.port_group()
                portgroup_obj.set_port_group_id(1)
                portgroup_obj.set_port_group_mode_load_balancing_mode_enabled(1)
                portgroup_obj.patch(session)

            :param session: Session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: Dictionary of error or success response.

        .. method:: delete()

            Deletes an entry or entry members. Fields involved are
            set within the object using the attribute's
            set method. This command is used to delete a port group
            or to delete the existing members from N_Ports or F_Ports.

            Example usage of the method to delete port group 1:

            .. code-block:: python

                portgroup_obj =
                    pyfos_brocade_access_gateway.port_group()
                portgroup_obj.set_port_group_id(1)
                portgroup_obj.delete(session)

            Example usage of the method to delete N_Ports from port group 1:

            .. code-block:: python

                portgroup_obj =
                    pyfos_brocade_access_gateway.port_group()
                portgroup_obj.set_port_group_id(1)
                portgroup_obj.set_port_group_n_ports_n_port("0/40;0/41")
                portgroup_obj.delete(session)

            :param session: Session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: Dictionary of error or success response.

    *Attribute Methods*

        .. method:: set_port_group_id(pgid)

            Sets the pgid in the object.

            :param pgid: Port-group identifier.
            :rtype: Dictionary of error or success response.

        .. method:: peek_port_group_id()

            Reads the port-group identifier in the object.

            :rtype: None or the pgid.

        .. method:: set_port_group_name(name)

            Sets the port-group name in the object.

            :param name: Name of the port group.
            :rtype: Dictionary of error or success response.

        .. method:: peek_port_group_name()

            Reads the port-group name in the object.

            :rtype: None or the port-group name.

        .. method:: set_port_group_n_ports_n_port (nport_list)

            Sets a list of N_Ports in the port-group object.

            :param nport_list: List of N_Port members of the port-group.
            :rtype: Dictionary of error or success response.

        .. method:: peek_port_group_n_ports_n_port()

            Reads a list of N_Ports in the port-group object.

            :rtype: None or a list of N_Port members.

        .. method:: set_port_group_f_ports_f_port (fport_list)

            Sets a list of F_Ports in the port-group object.

            :param nport_list: List of F_Port members of the port-group.
            :rtype: Dictionary of error or success response.

        .. method:: peek_port_group_f_ports_f_port()

            Reads a list of F_Ports in the port-group object.

            :rtype: None or a list of _Port members.

        .. method:: set_port_group_mode_load_balancing_mode_enabled(enable)

            Enables or disables the load balancing mode in the port-group.

            :param enable: Load balancing mode enabled(1) or disabled(0).
            :rtype: Dictionary of error or success response.

        .. method:: peek_port_group_mode_load_balancing_mode_enabled()

            Reads the load balancing mode status in the port-group object.

            :rtype: None or the load balancing mode status.

        .. method:: set_port_group_mode_multiple_fabric_name_monitoring_mode_enabled(enable)

            Enables or disables multiple fabric name monitoring mode
            in the port-group.

            :param enable: Multiple fabric name monitoring mode enabled(1)
                           or disabled(0).
            :rtype: Dictionary of error or success response.

        .. method:: peek_port_group_mode_multiple_fabric_name_monitoring_mode_enabled()

            Reads the multiple fabric name monitoring mode status in
            the port-group object.

            :rtype: None or the multiple fabric name monitoring mode status.
        """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.ag_portgroup,
                         "/rest/running/brocade-access-gateway/port-group",
                         version.VER_RANGE_820a_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "port-group-id", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute(
            "port-group-name",  pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "port-group-n-ports", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute(
            "n-port", pyfos_type.type_na,
            None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST),
            ["port-group-n-ports"])
        self.add(pyfos_rest_util.rest_attribute(
            "port-group-f-ports", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute(
            "f-port", pyfos_type.type_na,
            None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST),
            ["port-group-f-ports"])
        self.add(pyfos_rest_util.rest_attribute(
            "port-group-mode", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute(
            "load-balancing-mode-enabled", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG), ["port-group-mode"])
        self.add(pyfos_rest_util.rest_attribute(
            "multiple-fabric-name-monitoring-mode-enabled",
            pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG), ["port-group-mode"])

        self.load(dictvalues, 1)


class f_port_list(pyfos_rest_util.rest_object):
    """This class provides F_Port information on an Access Gateway.

    Important Class Members:

        +-------------------------------------------+----------------------------------+--------------------------------------------------------------------------+
        | Attribute Name                            | Description                      |Frequently Used Methods                                                   |
        +===========================================+==================================+==========================================================================+
        | f-port                                    | F_Port interface                 |:func:`set_f_port`                                                        |
        |                                           |                                  |:func:`peek_f_port`                                                       |
        +-------------------------------------------+----------------------------------+--------------------------------------------------------------------------+
        | online-status                             | F_Port online status.            |:func:`peek_online_status`                                                |
        |                                           |                                  |                                                                          |
        +-------------------------------------------+----------------------------------+--------------------------------------------------------------------------+
        | f-port-info/fcid                          | Fibre Channel ID of the F_Port   |:func:`peek_f_port_info_fcid`                                             |
        |                                           |                                  |                                                                          |
        +-------------------------------------------+----------------------------------+--------------------------------------------------------------------------+
        | f-port-info/attached-port-wwn             | Attached port WWN of the F_Port. |:func:`peek_f_port_info_attached_port_wwn`                                |
        |                                           |                                  |                                                                          |
        +-------------------------------------------+----------------------------------+--------------------------------------------------------------------------+
        | f-port-info/n-port                        | N_Port currently mapped to       |:func:`peek_f_port_info_n_port`                                           |
        |                                           | by the F_Port                    |                                                                          |
        +-------------------------------------------+----------------------------------+--------------------------------------------------------------------------+
        | f-port-info/login-exceeded                | Whether login exceeded on the    |:func:`peek_f_port_info_login_exceeded`                                   |
        |                                           | F_Port                           |                                                                          |
        +-------------------------------------------+----------------------------------+--------------------------------------------------------------------------+

    *Object Methods*

        .. method:: get()

            Returns :class:`f_port_list`
            object with values for all attributes. The f-port-info
            attributes are available only for the online F_Ports.
            The object can be printed using :func:`pyfos_utils.response_print`.

            :param session: Session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: Dictionary of errors or
                :class:`f_port_list` objects.

            Example usage of the method to get information for all F_Ports:

            .. code-block:: python

                fport_obj = pyfos_brocade_access_gateway.f_port_list()
                fport_obj.get(session, None)

            Example usage of the method to get information for a
            specific F_Port, say "0/8":

            .. code-block:: python

                fport_obj = pyfos_brocade_access_gateway.f_port_list()
                fport_obj.get(session, "0/8")


    *Attribute Methods*

        .. method:: set_f_port(f-port)

            Sets F_Port in the object.

            :param f-port: F_Port interface.
            :rtype: Dictionary of error or success response.

        .. method:: peek_f_port()

            Reads F_Port in the object.

            :rtype: None or F_Port.

        .. method:: peek_online_status()

            Reads F_Port online status in the object.

            :rtype: 0 (Offline) or 1 (Online).

        .. method:: peek_f_port_info_fcid()

            Reads Fibre Channel ID of the online F_Port.

            :rtype: None or Fibre Channel ID.

        .. method:: peek_f_port_info_attached_port_wwn()

            Reads the WWN of the port attached to the F_Port.

            :rtype: None or the port WWN.

        .. method:: peek_f_port_info_n_port()

            Reads the current mapped N_Port of the F_Port.

            :rtype: None or N_Port interface.

        .. method:: peek_f_port_info_login_exceeded()

            Reads whether the logins were exceeded on the F_Port.

            :rtype: None or 0 (login not exceeded) or 1 (login exceeded).

        """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.ag_fportlist,
                         "/rest/running/brocade-access-gateway/f-port-list",
                         version.VER_RANGE_820a_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "f-port", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute(
            "online-status",  pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "f-port-info", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute(
            "n-port", pyfos_type.type_na,
            None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST), ["f-port-info"])
        self.add(pyfos_rest_util.rest_attribute(
            "login-exceeded", pyfos_type.type_na,
            None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST), ["f-port-info"])

        self.load(dictvalues, 1)


class policy(pyfos_rest_util.rest_object):
    """This class provides methods to retrieve/configure the Access Gateway
    policies.

    Important Class Members:

        +------------------------------------------------+----------------------------------+----------------------------------------------------------------+
        | Attribute Name                                 | Description                      |Frequently Used Methods                                         |
        +================================================+==================================+================================================================+
        | port-group-policy-enabled                      | Enables/Disables the port group  |:func:`set_port_group_policy_enabled`                           |
        |                                                | policy.                          |:func:`peek_port_group_policy_enabled`                          |
        +------------------------------------------------+----------------------------------+----------------------------------------------------------------+
        | auto-policy-enabled                            | Enables/Disables the auto        |:func:`set_auto_policy_enabled`                                 |
        |                                                | policy.                          |:func:`peek_auto_policy_enabled`                                |
        +------------------------------------------------+----------------------------------+----------------------------------------------------------------+

    *Object Methods*

        .. method:: get()

            Returns :class:`policy`
            object with values for all attributes.
            The object can be printed using :func:`pyfos_utils.response_print`.

            :param session: Session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: Dictionary of error or
                :class:`policy` object.

        .. method:: patch()

            Replaces entry members. Fields involved are set within the object
            using the attribute's set method. This command is used to
            enable or disable the Access Gateway policies.

            Example usage of the method to enable the port
            group policy on an AG:

            .. code-block:: python

                policy_obj =
                    pyfos_brocade_access_gateway.policy()
                policy_obj.set_port_group_policy_enabled(1)
                policy_obj.patch(session)

            :param session: Session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: Dictionary of error or success response.

    *Attribute Methods*

        .. method:: set_port_group_policy_enabled(enable)

            Enables or disables the portgroup policy.

            :param enable: Set to 1 to enable and 0 to disable
                           the portgroup policy.
            :rtype: Dictionary of error or success response.

        .. method:: peek_port_group_policy_enabled()

            Reads the current state of the port group policy.

            :rtype: 0 (disabled) or 1 (enabled).

        .. method:: set_auto_policy_enabled(enable)

            Enables or disables the auto policy.

            :param enable: Set to 1 to enable and 0 to disable auto policy.
            :rtype: Dictionary of error or success response.

        .. method:: peek_auto_policy_enabled()

            Reads the current state of the auto policy.

            :rtype: 0 (disabled) or 1 (enabled).
        """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.ag_policy,
                         "/rest/running/brocade-access-gateway/policy",
                         version.VER_RANGE_820a_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "port-group-policy-enabled", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute(
            "auto-policy-enabled",  pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.load(dictvalues, 1)


class n_port_settings(pyfos_rest_util.rest_object):
    """This class provides options to set the N_Port settings.

    Important Class Members:

        +------------------------------------------------+----------------------------------+----------------------------------------------------------------+
        | Attribute Name                                 | Description                      |Frequently Used Methods                                         |
        +================================================+==================================+================================================================+
        | reliability-counter                            | Reads/Sets the reliability       |:func:`set_reliability_counter`                                 |
        |                                                | counter for a N_Port.            |:func:`peek_reliability_counter`                                |
        +------------------------------------------------+----------------------------------+----------------------------------------------------------------+

    *Object Methods*

        .. method:: get()

            Returns :class:`n_port_settings`
            object with values for all the attributes.
            The object can be printed using :func:`pyfos_utils.response_print`.

            :param session: Session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: Dictionary of error or
                :class:`n_port_settings` object.

        .. method:: patch()

            Replaces entry members. Fields involved are set within the object
            using the attribute's set method. This method is used to
            set the N_Port settings, for example, reliability counter.

            Example usage of the method to set the reliability counter to 20:

            .. code-block:: python

                nportsettings_obj =
                    pyfos_brocade_access_gateway.n_port_settings()
                nportsettings_obj.set_reliability_counter(20)
                nportsettings_obj.patch(session)

            :param session: Session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: Dictionary of error or success response.

    *Attribute Methods*

        .. method:: set_reliability_counter(count)

            Sets the N_Port reliability counter.

            :param count: The N_Port reliability count value to be set.
            :rtype: Dictionary of error or success response.

        .. method:: peek_reliability_counter()

            Reads the current count of N_Port reliability counter.

            :rtype: Counter value.

        """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.ag_nportsettings,
                         "/rest/running/brocade-access-gateway/n-port-settings"
                         "", version.VER_RANGE_820a_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "reliability-counter", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_KEY))

        self.load(dictvalues, 1)


class n_port_map(pyfos_rest_util.rest_object):
    """This class provides options to display and configure N_Port-to
    -F_Port mapping.

    Important Class Members:

        +------------------------------------------------+-----------------------------------+------------------------------------------------------------+
        | Attribute Name                                 | Description                       |Frequently Used Methods                                     |
        +================================================+===================================+============================================================+
        | n-port                                         | N_Port interface                  |:func:`set_n_port`                                          |
        |                                                |                                   |:func:`peek_n_port`                                         |
        +------------------------------------------------+-----------------------------------+------------------------------------------------------------+
        | failover-enabled                               | N_Port failover configuration     |:func:`peek_failover_enabled`                               |
        |                                                |                                   |:func:`set_failover_enabled`                                |
        +------------------------------------------------+-----------------------------------+------------------------------------------------------------+
        | failback-enabled                               | N_Port failback configuration     |:func:`peek_failback_enabled`                               |
        |                                                |                                   |:func:`set_failback_enabled`                                |
        +------------------------------------------------+-----------------------------------+------------------------------------------------------------+
        | configured-f-port-list/f-port                  | Mapped F_Ports                    |:func:`peek_configured_f_port_list_f_port`                  |
        |                                                |                                   |:func:`set_configured_f_port_list_f_port`                   |
        +------------------------------------------------+-----------------------------------+------------------------------------------------------------+
        | static-f-port-list/f-port                      | Statically mapped F_Ports         |:func:`peek_static_f_port_list_f_port`                      |
        |                                                |                                   |:func:`set_static_f_port_list_f_port`                       |
        +------------------------------------------------+-----------------------------------+------------------------------------------------------------+
        | online-status                                  | Online status of the N_Port       |:func:`peek_online_status`                                  |
        +------------------------------------------------+-----------------------------------+------------------------------------------------------------+
        | reliable-status                                | Reliable status of the N_Port     |:func:`peek_reliable_status`                                |
        +------------------------------------------------+-----------------------------------+------------------------------------------------------------+
        | n-port-info/attached-fabric-name               | WWN of the attached fabric        |:func:`peek_n_port_info_attached_fabric_name`               |
        +------------------------------------------------+-----------------------------------+------------------------------------------------------------+
        | n-port-info/attached-port-wwn                  | WWN of the attached port          |:func:`peek_n_port_info_attached_port_wwn`                  |
        +------------------------------------------------+-----------------------------------+------------------------------------------------------------+
        | n-port-info/n-port-fcid                        | Fibre Channel ID of the N_Port    |:func:`peek_n_port_info_n_port_fcid`                        |
        +------------------------------------------------+-----------------------------------+------------------------------------------------------------+
        | n-port-info/attached-switch-user-friendly-name | The attached switch's user        |:func:`peek_n_port_info_attached_switch_user_friendly_name` |
        |                                                | friendly name                     |                                                            |
        +------------------------------------------------+-----------------------------------+------------------------------------------------------------+
        | n-port-info/attached-switch-f-port             | Fabric switchpPort name of the    |:func:`peek_n_port_info_attached_switch_f_port`             |
        |                                                | port attached to the N_Port       |                                                            |
        +------------------------------------------------+-----------------------------------+------------------------------------------------------------+
        | n-port-info/attached-switch-ip-address         | The attached switch out-of-band   |:func:`peek_n_port_info_attached_switch_ip_address`         |
        |                                                | IP address                        |                                                            |
        +------------------------------------------------+-----------------------------------+------------------------------------------------------------+

    *Object Methods*

        .. method:: get(session)

            Returns :class:`n_port_map` object or a list of objects
            filled with attributes gathered from the Access Gateway. If the
            optional N_Port is given, either an object matching the name of the
            port is returned or an empty object is returned
            if no match is found.

            Each object can be printed using :func:`pyfos_util.response_print`
            and individual attributes can be accessed through peek methods.

            :param session: Session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: An :class:`n_port_map` object if there is
                only one N_Port Configured in the switch or
                a list of objects if there are more than one.

        .. method:: patch(session)

            Applies configurable attribute(s) within the object to
            an N_Port map of the Access Gateway. This method configures a
            specified list of F_Ports to be mapped (static/configured) to
            a given N_Port. This new map configuration will overwrite
            any existing map configuration for the specified N_Port.
            Also, this method is used to update the failover and failback
            configuration for a given N_Port.

            *The following is an example using individual sets:*

            .. code-block:: python

                # initialize the Access Gateway object
                nport = pyfos_brocade_access_gateway.n_port_map();
                # set the failover-enabled attribute to
                # enable failover for N_Port 0/47 on the Access Gateway
                nport.set_n_port("0/47")
                nport.set_failover_enabled("1")
                # execute the HTTP patch method to apply the object to the
                # switch connected through the session
                nport.patch(session)


            :param session: Session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary of error or success information.

        .. method:: post(session)

            Add members to a list attribute of the object. This method is used
            to add a specified list of F_Ports (configured and static)
            to a given N_Port.

            Example usage of the method to create a new mappings::

                # initialize the Access Gateway object
                nport = pyfos_brocade_access_gateway.n_port_map();
                # set the failover-enabled attribute to
                # enable failover for N_Port 0/47 on the Access Gateway
                nport.set_n_port("0/47")
                new_nport.set_configured_f_port_list_f_port("0/1;0/2");
                result = new_nport.post(session)


            :param session: Session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: Dictionary of error or success response.

        .. method:: delete(session)

            Deletes members from a list attribute of the object.
            This method is used to remove/clear the specified list of
            configured and static F_Ports from the mapping for N_Port.

            Example usage of the method to create a new mappings::

                # initialize the Access Gateway object
                nport = pyfos_brocade_access_gateway.n_port_map();
                # set the failover-enabled attribute to
                # enable failover for N_Port 0/47 on the switch
                nport.set_n_port("0/47")
                new_nport.set_configured_f_port_list_f_port("0/1;0/2");
                result = new_nport.delete(session)


            :param session: Session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: Dictionary of error or success response.

    *Attribute Methods*

        .. method:: set_n_port(name)

            Sets the port name in the object.

            :param name: Port name to be set within the object.
            :rtype: None or dictionary of error information.

        .. method:: peek_n_port()

            Reads the port name in the object.

            :rtype: None or the N_Port name.

        .. method:: set_failover_enabled(newmode)

            Sets the failover-enabled state in the object.

            :param newmode: New mode to be set within the object.
            :rtype: None or dictionary of error information.

        .. method:: peek_failover_enabled()

            Reads the failover-enabled state in the object.

            :rtype: None or the failover state of the N_Port.

        .. method:: set_failback_enabled(newmode)

            Sets the failback-enabled state in the object.

            :param newmode: New mode to be set within the object.
            :rtype: None or dictionary of error information.

        .. method:: peek_failback_enabled()

            Reads the failback-enabled state in the object.

            :rtype: None or the failback state of the N_Port.

        .. method:: set_configured_f_port_list_f_port(fport_list)

            Sets a list of configured F_Port mappings for the
            N_Port in the object.

            :param fport_list: List of F_Ports to be mapped.
            :rtype: None or dictionary of error information.

        .. method:: peek_configured_f_port_list_f_port()

            Gets a list of configured F_Port mappings for the
            N_Port in the object.

            :rtype: None or a list of mapped F_Ports.

        .. method:: set_static_f_port_list_fport(fport_list)

            Sets a list of static F_Port mappings for the
            N_Port in the object.

            :param fport_list: List of F_Ports to be mapped statically.
            :rtype: None or dictionary of error information.

        .. method:: peek_static_f_port_list_fport()

            Gets a list of static F_Port mappings for N_Port in the object.

            :rtype: None or a list of statically mapped F_Ports.

        .. method:: peek_online_status()

            Gets the online status of the N_Port in the object.

            :rtype: None or the online status of the N_Port.

        .. method:: peek_reliable_status()

            Gets the reliable status of the N_Port in the object.

            :rtype: None or the reliable status of N_Port.

        .. method:: peek_n_port_info_attached_fabric_name()

            Gets the WWN of the fabric attached to the N_Port.

            :rtype: None or the WWN of the fabric attached to the N_Port.

        .. method:: peek_n_port_info_attached_port_wwn()

            Gets the WWN of the port attached to the N_Port.

            :rtype: None or the WWN of the port attached to the N_Port.

        .. method:: peek_n_port_info_n_port_fcid()

            Gets the Fibre Channel ID of the N_Port.

            :rtype: None or the Fibre Channel ID of the N_Port.

        .. method:: peek_n_port_info_attached_switch_user_friendly_name()

            Gets the name of the fabric switch attached to the N_Port.

            :rtype: None or the name of the fabric switch.

        .. method:: peek_n_port_info_attached_switch_f_port()

            Gets the fabric switch port name of the
            port attached to the N_Port.

            :rtype: None or the fabric switch port name.

        .. method:: peek_n_port_info_attached_switch_ip_address()

            Gets the out-of-band IP addresses of the fabric switch
            attached to the N_Port.

            :rtype: None or the out-of-band IP addresses of the fabric switch.


        """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.ag_nportmap,
                         "/rest/running/brocade-access-gateway/n-port-map",
                         version.VER_RANGE_820a_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "n-port", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute(
            "failover-enabled", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "failback-enabled", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "online-status", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "reliable-status", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "n-port-info", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute(
            "attached-fabric-name", pyfos_type.type_wwn,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG), ["n-port-info"])
        self.add(pyfos_rest_util.rest_attribute(
            "attached-port-wwn", pyfos_type.type_wwn,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG), ["n-port-info"])
        self.add(pyfos_rest_util.rest_attribute(
            "n-port-fcid", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG), ["n-port-info"])
        self.add(pyfos_rest_util.rest_attribute(
            "attached-switch-user-friendly-name", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG), ["n-port-info"])
        self.add(pyfos_rest_util.rest_attribute(
            "attached-switch-f-port", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG), ["n-port-info"])
        self.add(pyfos_rest_util.rest_attribute(
            "attached-switch-ip-address", pyfos_type.type_ip_addr,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG), ["n-port-info"])
        self.add(pyfos_rest_util.rest_attribute(
            "configured-f-port-list", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute(
            "f-port", pyfos_type.type_na,
            None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST),
            ["configured-f-port-list"])
        self.add(pyfos_rest_util.rest_attribute(
            "static-f-port-list", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute(
            "f-port", pyfos_type.type_na,
            None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST),
            ["static-f-port-list"])

        self.load(dictvalues, 1)
