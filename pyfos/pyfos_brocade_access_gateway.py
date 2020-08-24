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

:mod:`pyfos_brocade_access_gateway` - PyFOS module to provide \
        REST support for an Access Gateway.
***************************************************************\
**********************************************************
The :mod:`pyfos_brocade_access_gateway` module provides REST support \
        for an Access Gateway.

"""

from pyfos import pyfos_rest_util
from pyfos.pyfos_type import pyfos_type
import pyfos.pyfos_version as version


class port_group(pyfos_rest_util.rest_object):
    """ This class provides methods and options to retrieve
    and configure port groups. Port groups can be configured only
    when the port group AG policy is activated.

    Important Class Members:

        +------------------------------------------------+----------------------------------+--------------------------------------------------------------------------+
        | Attribute Name                                 | Description                      |Frequently Used Methods                                                   |
        +================================================+==================================+==========================================================================+
        | port-group-id                                  | The port group ID.               |:func:`set_port_group_id`                                                 |
        |                                                |                                  |:func:`peek_port_group_id`                                                |
        +------------------------------------------------+----------------------------------+--------------------------------------------------------------------------+
        | port-group-name                                | The port group name.             |:func:`set_port_group_name`                                               |
        |                                                |                                  |:func:`peek_port_group_name`                                              |
        +------------------------------------------------+----------------------------------+--------------------------------------------------------------------------+
        | port-group-n-ports/n-port                      | The N_Ports present in the port  |:func:`set_port_group_n_ports_n_port`                                     |
        |                                                | group.                           |:func:`peek_port_group_n_ports_n_port`                                    |
        +------------------------------------------------+----------------------------------+--------------------------------------------------------------------------+
        | port-group-f-ports/f-port                      | The F_Ports present in the port  |:func:`set_port_group_f_ports_f_port`                                     |
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
            object with values for all attributes.
            The object can be printed using :func:`pyfos_utils.response_print`.

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary of error or a \
                :class:`port_group` object.

        .. method:: post()

            Creates an entry or adds members. The required fields are set
            within the object using the attribute's set method.
            This method is used to create a new port group with a group
            of N_Ports or to add N_Ports or F_Ports to an existing port group.

            Example Usage of the Method to Create a New Port Group:

            .. code-block:: python

                portgroup_obj =
                    pyfos_brocade_access_gateway.port_group()
                portgroup_obj.set_port_group_id(1)
                portgroup_obj.set_port_group_n_ports_n_port("0/40;0/41")
                portgroup_obj.post(session)

            The above example will add N_Ports if the port group with ID 1
            exists already.

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary of errors or a success response.

        .. method:: patch()

            Replaces entry members. The required fields are set within the \
            object using the attribute's set method. This command is used to
            replace the existing member N_Ports or F_Ports, the
            rename port group, and the enable or disable port group modes.

            Example Usage of the Method to Enable Load Balancing Mode in \
            a Port Group:

            .. code-block:: python

                portgroup_obj =
                    pyfos_brocade_access_gateway.port_group()
                portgroup_obj.set_port_group_id(1)
                portgroup_obj.set_port_group_mode_load_balancing_mode_enabled(1)
                portgroup_obj.patch(session)

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary of errors or a success response.

        .. method:: delete()

            Deletes an entry or entry members. The required fields are
            set within the object using the attribute's
            set method. This command is used to delete a port group
            or to delete the existing members from N_Ports or F_Ports.

            Example Usage of the Method to Delete Port Group 1:

            .. code-block:: python

                portgroup_obj =
                    pyfos_brocade_access_gateway.port_group()
                portgroup_obj.set_port_group_id(1)
                portgroup_obj.delete(session)

            Example Usage of the Method to Delete N_Ports from Port Group 1:

            .. code-block:: python

                portgroup_obj =
                    pyfos_brocade_access_gateway.port_group()
                portgroup_obj.set_port_group_id(1)
                portgroup_obj.set_port_group_n_ports_n_port("0/40;0/41")
                portgroup_obj.delete(session)

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary of errors or a success response.

    *Attribute Methods*

        .. method:: set_port_group_id(pgid)

            Sets the port group identifier (PGID) in the object.

            :param pgid: The port group identifier.
            :rtype: A dictionary of errors or a success response.

        .. method:: peek_port_group_id()

            Reads the port group identifier in the object.

            :rtype: None or the PGID.

        .. method:: set_port_group_name(name)

            Sets the port group name in the object.

            :param name: The name of the port group.
            :rtype: A dictionary of errors or a success response.

        .. method:: peek_port_group_name()

            Reads the port group name in the object.

            :rtype: None or the port group name.

        .. method:: set_port_group_n_ports_n_port (nport_list)

            Sets a list of N_Ports in the port group object.

            :param nport_list: List of N_Port members of the port group.
            :rtype: A dictionary of errors or a success response.

        .. method:: peek_port_group_n_ports_n_port()

            Reads a list of N_Ports in the port group object.

            :rtype: None or a list of N_Port members.

        .. method:: set_port_group_f_ports_f_port (fport_list)

            Sets a list of F_Ports in the port group object.

            :param nport_list: A list of F_Port members of the port group.
            :rtype: A dictionary of errors or a success response.

        .. method:: peek_port_group_f_ports_f_port()

            Reads a list of F_Ports in the port group object.

            :rtype: None or a list of port members.

        .. method:: set_port_group_mode_load_balancing_mode_enabled(enable)

            Enables or disables load balancing mode in the port group.

            :param enable: Enables (1) or disables (0) load balancing mode.
            :rtype: A dictionary of errors or a success response.

        .. method:: peek_port_group_mode_load_balancing_mode_enabled()

            Reads the load balancing mode status in the port group object.

            :rtype: None or the load balancing mode status.

        .. method:: set_port_group_mode_multiple_fabric_name_monitoring_mode_enabled(enable)

            Enables or disables multiple fabric name monitoring mode
            in the port group.

            :param enable: Enables (1) or disables (0) multiple \
                           fabric name monitoring mode.
            :rtype: A dictionary of errors or a success response.

        .. method:: peek_port_group_mode_multiple_fabric_name_monitoring_mode_enabled()

            Reads the multiple fabric name monitoring mode status in
            the port group object.

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
            "port-group-name", pyfos_type.type_str,
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
        | f-port                                    | The F_Port interface.            |:func:`set_f_port`                                                        |
        |                                           |                                  |:func:`peek_f_port`                                                       |
        +-------------------------------------------+----------------------------------+--------------------------------------------------------------------------+
        | online-status                             | The F_Port online status.        |:func:`peek_online_status`                                                |
        |                                           |                                  |                                                                          |
        +-------------------------------------------+----------------------------------+--------------------------------------------------------------------------+
        | f-port-info/fcid                          | The Fibre Channel ID of          |:func:`peek_f_port_info_fcid`                                             |
        |                                           | the F_Port.                      |                                                                          |
        +-------------------------------------------+----------------------------------+--------------------------------------------------------------------------+
        | f-port-info/attached-port-wwn             | The attached WWN of              |:func:`peek_f_port_info_attached_port_wwn`                                |
        |                                           | the F_Port.                      |                                                                          |
        +-------------------------------------------+----------------------------------+--------------------------------------------------------------------------+
        | f-port-info/n-port                        | The N_Port currently mapped to   |:func:`peek_f_port_info_n_port`                                           |
        |                                           | by the F_Port.                   |                                                                          |
        +-------------------------------------------+----------------------------------+--------------------------------------------------------------------------+
        | f-port-info/login-exceeded                | Whether login is exceeded on the |:func:`peek_f_port_info_login_exceeded`                                   |
        |                                           | F_Port.                          |                                                                          |
        +-------------------------------------------+----------------------------------+--------------------------------------------------------------------------+

    *Object Methods*

        .. method:: get()

            Returns an :class:`f_port_list`
            object with values for all attributes. The f-port-info
            attributes are available only for online F_Ports.
            The object can be printed using :func:`pyfos_utils.response_print`.

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary of errors or
                :class:`f_port_list` objects.

            Example Usage of the Method to Get Information for All F_Ports:

            .. code-block:: python

                fport_obj = pyfos_brocade_access_gateway.f_port_list()
                fport_obj.get(session, None)

            Example Usage of the Method to Get Information for a
            Specific F_Port "0/8":

            .. code-block:: python

                fport_obj = pyfos_brocade_access_gateway.f_port_list()
                fport_obj.get(session, "0/8")


    *Attribute Methods*

        .. method:: set_f_port(f-port)

            Sets the F_Port in the object.

            :param f-port: The F_Port interface.
            :rtype: A dictionary of errors or a success response.

        .. method:: peek_f_port()

            Reads the F_Port in the object.

            :rtype: None or the F_Port.

        .. method:: peek_online_status()

            Reads the F_Port online status in the object.

            :rtype: 0 (Offline) or 1 (Online).

        .. method:: peek_f_port_info_fcid()

            Reads the Fibre Channel ID of the online F_Port.

            :rtype: None or the Fibre Channel ID.

        .. method:: peek_f_port_info_attached_port_wwn()

            Reads the WWN of the port attached to the F_Port.

            :rtype: None or the port WWN.

        .. method:: peek_f_port_info_n_port()

            Reads the currently mapped N_Port of the F_Port.

            :rtype: None or the N_Port interface.

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
            "online-status", pyfos_type.type_str,
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
    """This class provides methods to retrieve and configure Access Gateway
    policies.

    Important Class Members:

        +------------------------------------------------+----------------------------------+----------------------------------------------------------------+
        | Attribute Name                                 | Description                      |Frequently Used Methods                                         |
        +================================================+==================================+================================================================+
        | port-group-policy-enabled                      | Enables/disables the port group  |:func:`set_port_group_policy_enabled`                           |
        |                                                | policy.                          |:func:`peek_port_group_policy_enabled`                          |
        +------------------------------------------------+----------------------------------+----------------------------------------------------------------+
        | auto-policy-enabled                            | Enables/disables the auto        |:func:`set_auto_policy_enabled`                                 |
        |                                                | policy.                          |:func:`peek_auto_policy_enabled`                                |
        +------------------------------------------------+----------------------------------+----------------------------------------------------------------+

    *Object Methods*

        .. method:: get()

            Returns a :class:`policy`
            object with values for all attributes.
            The object can be printed using :func:`pyfos_utils.response_print`.

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary of errors or a
                :class:`policy` object.

        .. method:: patch()

            Replaces entry members. The required fields are set within the object
            using the attribute's set method. This command is used to
            enable or disable Access Gateway policies.

            Example Usage of the Method to Enable the Port
            Group Policy on an AG:

            .. code-block:: python

                policy_obj =
                    pyfos_brocade_access_gateway.policy()
                policy_obj.set_port_group_policy_enabled(1)
                policy_obj.patch(session)

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary of errors or a success response.

    *Attribute Methods*

        .. method:: set_port_group_policy_enabled(enable)

            Enables or disables the port group policy.

            :param enable: Enables (1) or disables (0) the port group policy.
            :rtype: A dictionary of errors or a success response.

        .. method:: peek_port_group_policy_enabled()

            Reads the current state of the port group policy.

            :rtype: 0 (disabled) or 1 (enabled).

        .. method:: set_auto_policy_enabled(enable)

            Enables or disables the auto policy.

            :param enable: Enables (1) or disables (0) the auto policy.
            :rtype: A dictionary of errors or a success response.

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
            "auto-policy-enabled", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.load(dictvalues, 1)


class n_port_settings(pyfos_rest_util.rest_object):
    """This class provides options to set the N_Port settings.

    Important Class Members:

        +------------------------------------------------+----------------------------------+----------------------------------------------------------------+
        | Attribute Name                                 | Description                      |Frequently Used Methods                                         |
        +================================================+==================================+================================================================+
        | reliability-counter                            | Reads or sets the reliability    |:func:`set_reliability_counter`                                 |
        |                                                | counter for an N_Port.           |:func:`peek_reliability_counter`                                |
        +------------------------------------------------+----------------------------------+----------------------------------------------------------------+

    *Object Methods*

        .. method:: get()

            Returns an :class:`n_port_settings`
            object with values for all attributes.
            The object can be printed using :func:`pyfos_utils.response_print`.

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary of errors or the
                :class:`n_port_settings` object.

        .. method:: patch()

            Replaces entry members. The required fields are set within \
            the object using the attribute's set method. This method is used to
            set the N_Port settings, for example, the reliability counter.

            Example Usage of the Method to Set the Reliability Counter to 20:

            .. code-block:: python

                nportsettings_obj =
                    pyfos_brocade_access_gateway.n_port_settings()
                nportsettings_obj.set_reliability_counter(20)
                nportsettings_obj.patch(session)

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary of errors or a success response.

    *Attribute Methods*

        .. method:: set_reliability_counter(count)

            Sets the N_Port reliability counter.

            :param count: The N_Port reliability count value to be set.
            :rtype: A dictionary of errors or a success response.

        .. method:: peek_reliability_counter()

            Reads the current count of the N_Port reliability counter.

            :rtype: The counter value.

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
    """This class provides options to display and configure \
N_Port-to-F_Port mapping.

    Important Class Members:

        +------------------------------------------------+-----------------------------------+------------------------------------------------------------+
        | Attribute Name                                 | Description                       |Frequently Used Methods                                     |
        +================================================+===================================+============================================================+
        | n-port                                         | The N_Port interface.             |:func:`set_n_port`                                          |
        |                                                |                                   |:func:`peek_n_port`                                         |
        +------------------------------------------------+-----------------------------------+------------------------------------------------------------+
        | failover-enabled                               | The N_Port failover               |:func:`peek_failover_enabled`                               |
        |                                                | configuration.                    |:func:`set_failover_enabled`                                |
        +------------------------------------------------+-----------------------------------+------------------------------------------------------------+
        | failback-enabled                               | The N_Port failback               |:func:`peek_failback_enabled`                               |
        |                                                | configuration.                    |:func:`set_failback_enabled`                                |
        +------------------------------------------------+-----------------------------------+------------------------------------------------------------+
        | configured-f-port-list/f-port                  | The mapped F_Ports.               |:func:`peek_configured_f_port_list_f_port`                  |
        |                                                |                                   |:func:`set_configured_f_port_list_f_port`                   |
        +------------------------------------------------+-----------------------------------+------------------------------------------------------------+
        | static-f-port-list/f-port                      | The statically mapped F_Ports.    |:func:`peek_static_f_port_list_f_port`                      |
        |                                                |                                   |:func:`set_static_f_port_list_f_port`                       |
        +------------------------------------------------+-----------------------------------+------------------------------------------------------------+
        | online-status                                  | The online status of the N_Port.  |:func:`peek_online_status`                                  |
        +------------------------------------------------+-----------------------------------+------------------------------------------------------------+
        | reliable-status                                |The reliable status of the N_Port. |:func:`peek_reliable_status`                                |
        +------------------------------------------------+-----------------------------------+------------------------------------------------------------+
        | n-port-info/attached-fabric-name               | The WWN of the attached fabric.   |:func:`peek_n_port_info_attached_fabric_name`               |
        +------------------------------------------------+-----------------------------------+------------------------------------------------------------+
        | n-port-info/attached-port-wwn                  | The WWN of the attached port.     |:func:`peek_n_port_info_attached_port_wwn`                  |
        +------------------------------------------------+-----------------------------------+------------------------------------------------------------+
        | n-port-info/n-port-fcid                        | The FCID of the N_Port.           |:func:`peek_n_port_info_n_port_fcid`                        |
        +------------------------------------------------+-----------------------------------+------------------------------------------------------------+
        | n-port-info/attached-switch-user-friendly-name | The attached switch's user        |:func:`peek_n_port_info_attached_switch_user_friendly_name` |
        |                                                | friendly name.                    |                                                            |
        +------------------------------------------------+-----------------------------------+------------------------------------------------------------+
        | n-port-info/attached-switch-f-port             | The fabric switch name of         |:func:`peek_n_port_info_attached_switch_f_port`             |
        |                                                | the port attached to the N_Port.  |                                                            |
        +------------------------------------------------+-----------------------------------+------------------------------------------------------------+
        | n-port-info/attached-switch-ip-address         | The attached switch out-of-band   |:func:`peek_n_port_info_attached_switch_ip_address`         |
        |                                                | IP address.                       |                                                            |
        |                                                |                                   |                                                            |
        +------------------------------------------------+-----------------------------------+------------------------------------------------------------+
        | preferred-f-ports/preferred-f-port             | preferred N_Port for the F_Ports  |:func:`peek_preferred_f_ports_preferred_f_port`             |
        |                                                |                                   |:func:`set_preferred_f_ports_preferred_f_port`              |
        +------------------------------------------------+-----------------------------------+------------------------------------------------------------+

    *Object Methods*

        .. method:: get(session)

            Returns an :class:`n_port_map` object or a list of objects
            filled with attributes gathered from the Access Gateway. If the
            optional N_Port is given, either an object matching the name of the
            port is returned or an empty object is returned
            if no match is found.

            Each object can be printed using :func:`pyfos_util.response_print`,
            and individual attributes can be accessed through peek methods.

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: An :class:`n_port_map` object if there is
                only one N_Port configured in the switch or
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


            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary of errors or success information.

        .. method:: post(session)

            Adds members to a list attribute of the object. This method is used
            to add a specified list of F_Ports (configured and static)
            to a given N_Port.

            Example Usage of the Method to Create New Mappings::

                # initialize the Access Gateway object
                nport = pyfos_brocade_access_gateway.n_port_map();
                # set the failover-enabled attribute to
                # enable failover for N_Port 0/47 on the Access Gateway
                nport.set_n_port("0/47")
                new_nport.set_configured_f_port_list_f_port("0/1;0/2");
                result = new_nport.post(session)


            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary of errors or a success response.

        .. method:: delete(session)

            Deletes members from a list attribute of the object.
            This method is used to remove or clear the specified list of
            configured and static F_Ports from the mapping for N_Port.

            Example Usage of the Method to Create New Mappings::

                # initialize the Access Gateway object
                nport = pyfos_brocade_access_gateway.n_port_map();
                # set the failover-enabled attribute to
                # enable failover for N_Port 0/47 on the switch
                nport.set_n_port("0/47")
                new_nport.set_configured_f_port_list_f_port("0/1;0/2");
                result = new_nport.delete(session)


            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary of errors or a success response.

    *Attribute Methods*

        .. method:: set_n_port(name)

            Sets the port name in the object.

            :param name: The port name to be set within the object.
            :rtype: None or a dictionary of error information.

        .. method:: peek_n_port()

            Reads the port name in the object.

            :rtype: None or the N_Port name.

        .. method:: set_failover_enabled(newmode)

            Sets the failover-enabled state in the object.

            :param newmode: The new mode to be set within the object.
            :rtype: None or a dictionary of error information.

        .. method:: peek_failover_enabled()

            Reads the failover-enabled state in the object.

            :rtype: None or the failover state of the N_Port.

        .. method:: set_failback_enabled(newmode)

            Sets the failback-enabled state in the object.

            :param newmode: The new mode to be set within the object.
            :rtype: None or a dictionary of error information.

        .. method:: peek_failback_enabled()

            Reads the failback-enabled state in the object.

            :rtype: None or the failback state of the N_Port.

        .. method:: set_configured_f_port_list_f_port(fport_list)

            Sets a list of configured F_Port mappings for the
            N_Port in the object.

            :param fport_list: A list of F_Ports to be mapped.
            :rtype: None or a dictionary of error information.

        .. method:: peek_configured_f_port_list_f_port()

            Gets a list of configured F_Port mappings for the
            N_Port in the object.

            :rtype: None or a list of mapped F_Ports.

        .. method:: set_static_f_port_list_fport(fport_list)

            Sets a list of static F_Port mappings for the
            N_Port in the object.

            :param fport_list: A list of F_Ports to be mapped statically.
            :rtype: None or a dictionary of error information.

        .. method:: peek_static_f_port_list_fport()

            Gets a list of static F_Port mappings for the N_Port in the object.

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

        .. method:: set_preferred_f_ports_preferred_f_port(fport_list)

            Sets the preferred N_Port for the F_Ports in the object.

            :param fport_list: A list of F_Ports to be mapped statically.
            :rtype: None or a dictionary of error information.

        .. method:: peek_preferred_f_ports_preferred_f_port()

            Gets the preferred N_Port for the F_Ports in the object.

            :rtype: None or a list of preferred F_Ports.


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
            "n-port-fcid", pyfos_type.type_str,
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
        self.add(pyfos_rest_util.rest_attribute(
            "preferred-f-ports", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute(
            "preferred-f-port", pyfos_type.type_na,
            None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST),
            ["preferred-f-ports"])

        self.load(dictvalues, 1)


class device_list(pyfos_rest_util.rest_object):
    """This class provides information about the devices logged in to the \
Access Gateway.

    Important Class Members:

        +-------------------------------------------+----------------------------------+--------------------------------------------------------------------------+
        | Attribute Name                            | Description                      |Frequently Used Methods                                                   |
        +===========================================+==================================+==========================================================================+
        | wwn                                       | The port WWN of the device.      |:func:`peek_wwn`                                                          |
        |                                           |                                  |                                                                          |
        +-------------------------------------------+----------------------------------+--------------------------------------------------------------------------+
        | fcid                                      | The Fibre Channel ID of          |:func:`peek_fcid`                                                         |
        |                                           | the device.                      |                                                                          |
        +-------------------------------------------+----------------------------------+--------------------------------------------------------------------------+
        | f-port                                    | The F_Port to which the device   |:func:`peek_f_port`                                                       |
        |                                           | is connected.                    |                                                                          |
        +-------------------------------------------+----------------------------------+--------------------------------------------------------------------------+
        | n-port                                    | The N_Port to which the device   |:func:`peek_n_port`                                                       |
        |                                           | F_Port is mapped.                |                                                                          |
        +-------------------------------------------+----------------------------------+--------------------------------------------------------------------------+

    *Object Methods*

        .. method:: get()

            Returns a :class:`device_list`
            object with values for all attributes.
            The object can be printed using :func:`pyfos_utils.response_print`.

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary of errors or a \
                :class:`device_list` object.

            Example Usage of the Method to Get Information for All WWNs:

            .. code-block:: python

                wwn_obj = pyfos_brocade_access_gateway.device_list()
                wwn_obj.get(session, None)

            Example Usage of the Method to Get Information for a
            Specific WWN "30:08:09:27:f8:8b:74:62":

            .. code-block:: python

                device_obj = pyfos_brocade_access_gateway.device_list()
                device_obj.get(session, "30:08:09:27:f8:8b:74:62")


    *Attribute Methods*


        .. method:: peek_wwn()

            Reads the WWN in the object.

            :rtype: None or the WWN.


        .. method:: peek_fcid()

            Reads the Fibre Channel ID of the device.

            :rtype: None or the Fibre Channel ID.


        .. method:: peek_nport()

            Reads the currently mapped N_Port of the F_Port.

            :rtype: None or the N_Port.

        .. method:: peek_fport()

            Reads the F_Port in the object.

            :rtype: None or the F_Port.

        """

    def __init__(self):
        dictvalues = {}
        super().__init__(pyfos_rest_util.rest_obj_type.ag_device_list,
                         "/rest/running/brocade-access-gateway/device-list",
                         version.VER_RANGE_821_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "wwn", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute(
            "fcid", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "f-port", pyfos_type.type_int,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "n-port", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.load(dictvalues, 1)
