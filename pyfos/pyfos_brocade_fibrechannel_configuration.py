# Copyright 2018-2019 Brocade Communications Systems LLC.  All rights reserved.
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
:mod:`pyfos_brocade_fibrechannel_configuration` - PyFOS module to configure \
FC switches.
****************************************************************************\
*************
The :mod:`pyfos_brocade_fibrechannel_configuration` module provides REST \
support to configure FC switches.
"""

from pyfos import pyfos_rest_util
from pyfos.pyfos_type import pyfos_type
import pyfos.pyfos_version as version


class switch_configuration(pyfos_rest_util.rest_object):
    """Class of configurable parameters of a FC switch.

    Important Class Members:

        +----------------+--------------+-----------------------------+
        | Attribute Name | Description  |Frequently Used Methods      |
        +================+==============+=============================+
        |wwn-port-id-mode| Sets the WWN |:meth:`set_wwn_port_id_mode` |
        |                | flag for the |:meth:`peek_wwn_port_id_mode`|
        |                | PID in the   |                             |
        |                | switch.      |                             |
        +----------------+--------------+-----------------------------+
        |edge-hold-time  | Sets the time|:meth:`set_edge_hold_time`   |
        |                | duration for |:meth:`peek_edge_hold_time`  |
        |                | frames.      |                             |
        +----------------+--------------+-----------------------------+
        |area-mode       | Sets the     |:meth:`set_area_mode`        |
        |                | address bits |:meth:`peek_area_mode`       |
        |                | for the area.|                             |
        +----------------+--------------+-----------------------------+
        |trunk-enabled   | Sets the     |:meth:`set_trunk_enabled`    |
        |                | trunking mode|:meth:`peek_trunk_enabled`   |
        |                | for switch   |                             |
        +----------------+--------------+-----------------------------+
        |xisl-enabled    | Sets the     |:meth:`set_xisl_enabled`     |
        |                | xisl mode for|:meth:`peek_xisl_enabled`    |
        |                | the switch   |                             |
        +----------------+--------------+-----------------------------+

    *Object Methods*

        .. method:: get(session)

            Returns a :class:`switch_configuration` object with attributes
            from the switch.

            Each object can be printed using :func:`pyfos_util.response_print`,
            and individual attributes can be accessed through peek methods.

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary of error or a
                :class:`switch` object.

        .. method:: patch(session)

            Applies configurable attribute(s) within the object to the switch.

            *Example Using Individual Sets:*

            .. code-block:: python

                # initialize the switch object
                switch_obj =
                pyfos_brocade_fibrechannel_configuration.switch_configuration()
                # set the wwn-port-id-mode attribute to enable the
                # wwn based pid on the switch
                switch_obj.set_wwn_port_id_mode(True)
                # execute HTTP patch command to apply the object to the
                # switch connected through session
                switch_obj.patch(session)

            *Example of Combining Object Initialization \
                     and Attribute Sets:*

            .. code-block:: python

                # initialize the switch object and
                # set the enable-state attribute
                switch_obj =
                pyfos_brocade_fibrechannel_configuration.switch_configuration(
                    {"wwn-port-id-mode" : True})
                # execute HTTP patch command to apply the object to the
                # switch connected through session
                switch_obj.patch(session)

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary of error or success information.

    *Attribute Methods*

        .. method:: set_wwn_port_id_mode(mode)

            Sets the WWN-based PID in the object.

            :param mode: Configures the WWN-based PID in the object.

            :rtype: None or a dictionary of error information.

        .. method:: peek_wwn_port_id_mode()

            Reads the enabled state of the WWN-based PID in the object.

            :rtype: True or False.

        .. method:: set_edge_hold_time(time)

            Sets the edge hold time in the object.

            :param time: The edge hold time in the switch to be set within
                         the object.

            :rtype: None or a dictionary of error information.

        .. method:: peek_edge_hold_time()

            Reads the edge hold time in the object.

            :rtype: The edge hold time of the switch.

        .. method:: set_area_mode(mode)

            Sets the port address bit based on the area in the object.

            :param mode: The mode value for the PID area limit within
                         the object.

            :rtype: None or a dictionary of error information.

        .. method:: peek_area_mode()

            Reads the mode of the port address bits in the object.

            :rtype: None or the mode of the port address of the switch.

        .. method:: set_trunk_enabled(mode)

            Sets trunk enable/disable bit in the object.

            :param mode: True/False to enable/disable trunking on the switch.

            :rtype: None or a dictionary of error information.

        .. method:: peek_trunk_enabled()

            Reads trunk enable/disable leaf in the object.

            :rtype: True/False based on trunking enabled or not on the switch.

        .. method:: set_xisl_enabled(mode)

            Sets xisl enable/disable bit in the object.

            :param mode: True/False to enable/disable xisl mode on the switch.

            :rtype: None or a dictionary of error information.

        .. method:: peek_xisl_enabled()

            Reads xisl mode in the object.

            :rtype: True/False based on xisl enabled or not on the switch.
        """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.switch_configuration,
                         "/rest/running/brocade-fibrechannel-configuration/"
                         "switch-configuration",
                         version.VER_RANGE_821_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "wwn-port-id-mode", pyfos_type.type_bool,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "edge-hold-time", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "area-mode", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "trunk-enabled", pyfos_type.type_bool,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "xisl-enabled", pyfos_type.type_bool,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG,
            version.VER_RANGE_900_and_ABOVE))

        self.load(dictvalues, 1)


class f_port_login_settings(pyfos_rest_util.rest_object):
    """Class of configurable parameters of the FC switch corresponding to
    F_Port login.

    Class Members:

+-------------------------+-----------+---------------------------------------+
|Attribute Name           |Description|Frequently Used Methods                |
+=========================+===========+=======================================+
|max-logins               |Sets the   |:meth:`set_max_logins`                 |
|                         |maximum    |:meth:`peek_max_logins`                |
|                         |number of  |                                       |
|                         |logins.    |                                       |
+-------------------------+-----------+---------------------------------------+
|max-flogi-rate-per-switch|Sets the   |:meth:`set_max_flogi_rate_per_switch`  |
|                         |FLOGI rate |:meth:`peek_max_flogi_rate_per_switch` |
|                         |in the     |                                       |
|                         |switch.    |                                       |
+-------------------------+-----------+---------------------------------------+
|stage-interval           |Sets the   |:meth:`set_stage_interval`             |
|                         |stage      |:meth:`peek_stage_interval`            |
|                         |interval.  |                                       |
+-------------------------+-----------+---------------------------------------+
|free-fdisc               |Sets the   |:meth:`set_free_fdisc`                 |
|                         |allowed    |:meth:`peek_free_fdisc`                |
|                         |FDISC.     |                                       |
+-------------------------+-----------+---------------------------------------+
|enforce-login            |Sets the   |:meth:`set_enforce_login`              |
|                         |login type |:meth:`peek_enforce_login`             |
|                         |precedence.|                                       |
+-------------------------+-----------+---------------------------------------+
|max-flogi-rate-per-port  |Sets the   |:meth:`set_max_flogi_rate_per_port`    |
|                         |FLOGI rate |:meth:`peek_max_flogi_rate_per_port`   |
|                         |per port.  |                                       |
+-------------------------+-----------+---------------------------------------+

    *Object Methods*

        .. method:: get(session)

            Returns a :class:`switch` object with attributes from the switch.

            Each object can be printed using :func:`pyfos_util.response_print`,
            and individual attributes can be accessed through peek methods.

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary of error or a
                :class:`switch` object.

        .. method:: patch(session)

            Applies configurable attribute(s) within the object to the switch.

            *Example Using Individual Sets:*

            .. code-block:: python

                # initialize the switch object
                obj =
                pyfos_brocade_fibrechannel_configuration.f_port_login_settings()
                # set the enforce-login attribute to enable the
                # login type precedence on the switch
                obj.set_enforce_login(1)
                # execute HTTP patch command to apply the object to the
                # switch connected through session
                obj.patch(session)

            *Example of Combining Object Initialization \
                     and Attribute Sets:*

            .. code-block:: python

                # initialize the switch object and
                # set the max-logins attribute
                obj =
                pyfos_brocade_fibrechannel_configuration.f_port_login_settings(
                    {"max-logins" : 1})
                # execute HTTP patch command to apply the object to the
                # switch connected through session
                obj.patch(session)

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary of error or success information.

    *Attribute Methods*

        .. method:: set_max_logins(value)

            Sets the switch-wide maximum number of logins in the object.

            :param value: The maximum number of logins within the object.
            :rtype: None or a dictionary of error information.

        .. method:: peek_max_logins()

            Reads the switch-wide maximum logins in the object.

            :rtype: None or a dictionary of error information.

        .. method:: set_max_flogi_rate_per_switch(value)

            Sets the maximum FLOGI rate per switch in the object.

            :param value: The maximum FLOGI rate in the switch to be set
                          within the object.
            :rtype: None or a dictionary of error information.

        .. method:: peek_max_flogi_rate_per_switch()

            Reads the maximum FLOGI rate per switch in the object.

            :rtype: None or a dictionary of error information.

        .. method:: set_stage_interval(value)

            Sets the staging interval in the object.

            :param value: The stage interval to be set within the object.
            :rtype: None or a dictionary of error information.

        .. method:: peek_stage_interval()

            Reads the staging interval in the object.

            :rtype: None or the staging interval in the object.

        .. method:: set_free_fdisc(value)

            Sets the number of FLOGIs allowed before staging in the object.

            :param value: The number of FLOGIs allowed before staging to be
                          set within the object.
            :rtype: None or a dictionary of error information.

        .. method:: peek_free_fdisc()

            Reads the number of FLOGIs allowed before staging in the object.

            :rtype: None or the number of FLOGIs allowed before staging in
                    the switch.

        .. method:: set_enforce_login(value)

            Sets the enforcement for login precedence in the object.

            :param value: The enforcement for login precedence to be set
                          within the object.
            :rtype: None or a dictionary of error information.

        .. method:: peek_enforce_login()

            Reads the enforcement for login precedence in the object.

            :rtype: None or the login type precedence in the switch.

        .. method:: set_max_flogi_rate_per_port(value)

            Sets the maximum FLOGI rate per port in the object.

            :param value: The maximum FLOGI rate per port to be set within
                          the object.
            :rtype: None or a dictionary of error information.

        .. method:: peek_max_flogi_rate_per_port()

            Reads the maximum FLOGI rate per port in the object.

            :rtype: None or the maximum FLOGI rate per port in the switch.

        """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.f_port_login_settings,
                         "/rest/running/brocade-fibrechannel-configuration/"
                         "f-port-login-settings",
                         version.VER_RANGE_821_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "max-logins", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "max-flogi-rate-per-switch", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "stage-interval", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "free-fdisc", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "enforce-login", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "max-flogi-rate-per-port", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.load(dictvalues, 1)


class port_configuration(pyfos_rest_util.rest_object):
    """Class of configurable parameters of the FC switch corresponding
       to ports.

    Class Members:

+------------------------+-------------+--------------------------------------+
| Attribute Name         | Description |Frequently Used Methods               |
+========================+=============+======================================+
|portname-mode           |Sets the     |:meth:`set_portname_mode`             |
|                        |current port |:meth:`peek_portname_mode`            |
|                        |name mode.   |                                      |
+------------------------+-------------+--------------------------------------+
|dynamic-portname-format |Sets the     |:meth:`set_dynamic_portname_format`   |
|                        |format of    |:meth:`peek_dynamic_portname_format`  |
|                        |the dynamic  |                                      |
|                        |port name.   |                                      |
+------------------------+-------------+--------------------------------------+
|dynamic-d-port-enabled  |If dynamic   |:meth:`set_dynamic_d_port_enabled`    |
|                        |D_Port is    |:meth:`peek_dynamic_d_port_enabled`   |
|                        |enabled.     |                                      |
+------------------------+-------------+--------------------------------------+
|on-demand-d-port-enabled|If on-demand |:meth:`set_on_demand_d_port_enabled`  |
|                        |D_Port is    |:meth:`peek_on_demand_d_port_enabled` |
|                        |enabled.     |                                      |
+------------------------+-------------+--------------------------------------+

    *Object Methods*

        .. method:: get(session)

            Returns a :class:`port_configuration` object with attributes from
            the port configuration.

            Each object can be printed using :func:`pyfos_util.response_print`,
            and individual attributes can be accessed through peek methods.

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary of error or a
                :class:`port_configuration` object.

        .. method:: patch(session)

            Applies configurable attribute(s) within the object to the port
            configuration.

            *Example Using Individual Sets:*

            .. code-block:: python

                # Initialize the port_configuration object
                obj =
                pyfos_brocade_fibrechannel_configuration.port_configuration()
                # Set the portname-mode attribute
                obj.set_portname_mode('default')
                # Execute HTTP patch command to apply the object to the
                # switch connected through session
                obj.patch(session)

            *Example of Combining Object Initialization \
                     and Attribute Sets:*

            .. code-block:: python

                # Initialize the port_configuration object and
                # set the portname-mode attribute
                obj =
                pyfos_brocade_fibrechannel_configuration.port_configuration(
                    {"portname-mode" : 'default'})
                # Execute HTTP patch command to apply the object to the
                # switch connected through session
                obj.patch(session)

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary of error or success information.

    *Attribute Methods*

        .. method:: set_portname_mode(mode)

            Sets the portname-mode attribute in the object.

            :param mode: The port name mode.
            :rtype: None or a dictionary of error information.

        .. method:: peek_portname_mode()

            Reads the portname-mode attribute in the object.

            :rtype: None or a port name mode.

        .. method:: set_dynamic_portname_format(portname_format)

            Sets the dynamic-portname-format attribute in the object.

            :param portname_format: The dynamic port name format.
            :rtype: None or a dictionary of error information.

        .. method:: peek_dynamic_portname_format()

            Reads the dynamic-portname-format attribute in the object.

            :rtype: None or a dynamic port name format.

        .. method:: set_dynamic_d_port_enabled(value)

            Sets the dynamic-d-port-enabled attribute in the object.

            :param value: A boolean value.
            :rtype: None or a dictionary of error information.

        .. method:: peek_dynamic_d_port_enabled()

            Reads the dynamic-d-port-enabled attribute in the object.

            :rtype: None or a dynamic D_Port-enabled value.

        .. method:: set_on_demand_d_port_enabled(value)

            Sets the on-demand-d-port-enabled attribute in the object.

            :param value: A boolean value.
            :rtype: None or a dictionary of error information.

        .. method:: peek_on_demand_d_port_enabled()

            Reads the on-demand-d-port-enabled attribute in the object.

            :rtype: None or the on-demand D_Port-enabled value.

    """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.
                         fibrechannel_configuration_port,
                         "/rest/running/brocade-fibrechannel-configuration/"
                         "port-configuration",
                         version.VER_RANGE_821_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "portname-mode", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "dynamic-portname-format", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "dynamic-d-port-enabled", pyfos_type.type_bool,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "on-demand-d-port-enabled", pyfos_type.type_bool,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.load(dictvalues, 1)


class zone_configuration(pyfos_rest_util.rest_object):
    """Class of configurable parameters of the FC switch corresponding
       to zoning.

    Class Members:

+-------------------------+------------+-------------------------------------+
|Attribute Name           |Description |Frequently Used Methods              |
+=========================+============+=====================================+
|node-name-zoning-enabled |If the node |:meth:`set_node_name_zoning_enabled` |
|                         |name check  |:meth:`peek_node_name_zoning_enabled`|
|                         |is enabled  |                                     |
|                         |for zoning. |                                     |
+-------------------------+------------+-------------------------------------+
|fabric-lock-timeout      |Set the     |:meth:`set_fabric_lock_timeout`      |
|                         |fabric lock |:meth:`peek_fabric_lock_timeout`     |
|                         |timeout     |                                     |
|                         |for zoning. |                                     |
+-------------------------+------------+-------------------------------------+

    *Object Methods*

        .. method:: get(session)

            Returns a :class:`zone_configuration` object with attributes from
            the zone configuration.

            Each object can be printed using :func:`pyfos_util.response_print`,
            and individual attributes can be accessed through peek methods.

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary of error or a
                :class:`zone_configuration` object.

        .. method:: patch(session)

            Applies configurable attribute(s) within the object to the zone
            configuration.

            *Example Using Individual Sets:*

            .. code-block:: python

                # Initialize the zone_configuration object
                obj =
                pyfos_brocade_fibrechannel_configuration.zone_configuration()
                # Set the node-name-zoning-enabled attribute
                obj.set_node_name_zoning_enabled('true')
                # Execute HTTP patch command to apply the object to the
                # switch connected through session
                obj.patch(session)

            *Example of Combining Object Initialization \
                     and Attribute Sets:*

            .. code-block:: python

                # Initialize the zone_configuration object and
                # set the node-name-zoning-enabled attribute
                obj =
                pyfos_brocade_fibrechannel_configuration.node-name-zoning-enabled(
                    {"node-name-zoning-enabled" : 'true'})
                # Execute HTTP patch command to apply the object to the
                # switch connected through session
                obj.patch(session)

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary of error or success information.

    *Attribute Methods*

        .. method:: set_node_name_zoning_enabled(value)

            Sets the node-name-zoning-enabled attribute in the object.

            :param value: A boolean value.
            :rtype: None or a dictionary of error information.

        .. method:: peek_node_name_zoning_enabled()

            Reads the node-name-zoning-enabled attribute in the object.

            :rtype: None or the node-name-zoning-enabled value.

        .. method:: set_fabric_lock_timeout(value)

            Sets the fabric-lock-timeout attribute in the object.

            :param value: The fabric-lock-timeout value to be set within
                          the object.
            :rtype: None or a dictionary of error information.

        .. method:: peek_fabric_lock_timeout()

            Reads the fabric-lock-timeout attribute in the object.

            :rtype: None or the fabric-lock-timeout value.

        """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.
                         fibrechannel_configuration_zone,
                         "/rest/running/brocade-fibrechannel-configuration/"
                         "zone-configuration",
                         version.VER_RANGE_821_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "node-name-zoning-enabled", pyfos_type.type_bool,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "fabric-lock-timeout", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG,
            version.VER_RANGE_900_and_ABOVE))

        self.load(dictvalues, 1)


class fabric(pyfos_rest_util.rest_object):
    """Class of configurable parameters of the FC switch.

    Important Class Members:

+-----------------------------+------------+---------------------------------------+
| Attribute Name              |Description |Frequently Used Methods                |
+=============================+============+=======================================+
| insistent-domain-id-enabled |Sets the    |meth:`set_insistent_domain_id_enabled` |
|                             |consistent  |meth:`peek_insistent_domain_id_enabled`|
|                             |domain ID   |                                       |
|                             |mode.       |                                       |
+-----------------------------+------------+---------------------------------------+
| principal-selection-enabled |Enables or  |meth:`set_principal_selection_enabled` |
|                             |disables    |meth:`peek_principal_selection_enabled`|
|                             |principal   |                                       |
|                             |switch      |                                       |
|                             |selection.  |                                       |
+-----------------------------+------------+---------------------------------------+
| principal-priority          |Sets the    |meth:`set_principal_priority`          |
|                             |principal   |meth:`peek_principal_priority`         |
|                             |selection   |                                       |
|                             |priority of |                                       |
|                             |the switch  |                                       |
+-----------------------------+------------+---------------------------------------+

    *Object Methods*

        .. method:: get(session)

            Returns a :class:`fabric` object with attributes from the switch.

            Each object can be printed using :func:`pyfos_util.response_print`,
            and individual attributes can be accessed through peek methods.

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary of error or a
                :class:`fabric` object.

        .. method:: patch(session)

            Applies configurable attribute(s) within the object to the fabric.

            *Example Using Individual Sets:*

            .. code-block:: python

                # initialize the fabric object
                fabric_obj = pyfos_brocade_fibrechannel_configuration.fabric()
                # set the idid mode attribute to enable the
                # insistent domain on the switch
                fabric_obj.set_insistent_domain_id_enabled(True)
                # enable or disable principal selection mode
                # mode in the switch.
                fabric_obj.set_principal_selection_enabled(True)
                # set the priority value to select the principal
                # switch.
                fabric_obj.set_principal_priority(value)
                # execute HTTP patch command to apply the object to the
                # switch connected through session
                fabric_obj.patch(session)

            *Example of Combining Object Initialization \
                     and Attribute Sets:*

            .. code-block:: python

                # initialize the fabric object and
                # set the insistent-domain-id-enabled attribute
                fabric_obj = pyfos_brocade_fibrechannel_configuration.fabric(
                    {"insistent-domain-id-enabled" : True,
                     "principal-selection-enabled" : True,
                     "principal-priority" : value})
                # execute HTTP patch command to apply the object to the
                # switch connected through session
                fabric_obj.patch(session)

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary of error or success information.

    *Attribute Methods*

        .. method:: set_insistent_domain_id_enabled(mode)

            Sets the Insistent Domain ID feature.

            :param mode: The mode value configures the IDID feature.

            :rtype: None or a dictionary of error information.

        .. method:: peek_insistent_domain_id_enabled()

            Reads the status of the Insistent Domain ID feature.

            :rtype: True or False.


        .. method:: set_principal_selection_enabled(value)

            Set the value of principal-selection-enabled in the object.

            :rtype: A dictionary of error or a success response.

        .. method:: peek_principal_selection_enabled()

            Reads the value assigned to principal-selection-enabled in the
             object.

            :rtype: True or False.


        .. method:: set_principal_priority(value)

            Set the value of principal-priority in the object.

            :rtype: A dictionary of error or a success response.

        .. method:: peek_principal_priority()

            Reads the value assigned to principal-priority in the object.

            :rtype: None on error and a value on success.

        """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.fabric,
                         "/rest/running/brocade-fibrechannel-configuration/"
                         "fabric",
                         version.VER_RANGE_821_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "insistent-domain-id-enabled", pyfos_type.type_bool,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("principal-selection-enabled",
                 pyfos_type.type_bool, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("principal-priority",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.load(dictvalues, 1)


class chassis_config_settings(pyfos_rest_util.rest_object):
    """Class of configurable parameters of the FC switch corresponding
       to chassis configuration.

    Class Members:

+---------------------------------+-----------------+---------------------------------------------+
|Attribute Name                   |Description      |Frequently Used Methods             	  |
+=================================+=================+=============================================+
|firmware-synchronization-enabled |Enables          |:meth:`set_firmware_synchronization_enabled` |
|                                 |firmware syncing |:meth:`peek_firmware_synchronization_enabled`|
|                                 |from Active CP   |                                		  |
|                                 |to Standby CP    |            	                          |
|				  |Automatically    |                    	                  |
+---------------------------------+-----------------+---------------------------------------------+
|http-session-ttl                 |Denotes time-out |:meth:`set_http_session_ttl`         	  |
|                                 |value for BNA,   |:meth:`peek_http_session_ttl`	          |
|                                 |SANNav, REST,    |                      	                  |
|                                 |PyFOS in seconds.|                                             |
+---------------------------------+-----------------+---------------------------------------------+
|ezserver-enabled                 |Enables          |:meth:`set_ezserver_enabled`   		  |
|                                 |EZServer         |:meth:`peek_ezserver_enabled`		  |
|                                 |True - enable    |                                  		  |
|                                 |False - disable. |                                    	  |
+---------------------------------+-----------------+---------------------------------------------+

    *Object Methods*

        .. method:: get(session)

            Returns a :class:`chassis_config_settings` object with attributes from
            the chassis configuration.

            Each object can be printed using :func:`pyfos_util.response_print`,
            and individual attributes can be accessed through peek methods.

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary of error or a
                :class:`chassis_config_settings` object.

        .. method:: patch(session)

            Applies configurable attribute(s) within the object to the zone
            configuration.

            *Example Using Individual Sets:*

            .. code-block:: python

                # Initialize the zone_configuration object
                obj =
                pyfos_brocade_fibrechannel_configuration.chassis_config_settings()
                # Set the ezserver-enabled attribute
                obj.set_ezserver-enabled('true')
                # Execute HTTP patch command to apply the object to the
                # switch connected through session
                obj.patch(session)


            .. code-block:: python

                # Initialize the zone_configuration object and
                # set the node-name-zoning-enabled attribute
                obj =
                pyfos_brocade_fibrechannel_configuration.ezserver-enabled(
                    {"ezserver-enabled" : 'true'})
                # Execute HTTP patch command to apply the object to the
                # switch connected through session
                obj.patch(session)

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary of error or success information.

    *Attribute Methods*

q
        .. method:: set_firmware_synchronization_enabled(value)

            Enables Firmware synchronization automatically between Active and Standby CP's.

            :param value: A boolean value.
            :rtype: None or a dictionary of error information.

        .. method:: peek_firmware_synchronization_enabled()

            Reads the firmware-synchronization-enabled attribute in the object.

            :rtype: None or the firmware-synchronization-enabled value.

        .. method:: set_http_session_ttl(value)

            Sets the session timeout value for BNA, SANNav, REST, PyFOS in the object.

            :param value: The Session-timeout value to be set within
                          the object.
            :rtype: None or a dictionary of error information.

        .. method:: peek_http_session_ttl()

            Reads the session-timeout attribute in the object.

            :rtype: None or the session-timeout value.

        .. method:: set_ezserver_enabled(value)

            Sets the EZServer enabling attribute in the object.

            :param value: The ezserver value within
                          the object.
            :rtype: None or a dictionary of error information.

        .. method:: peek_ezserver_enabled()

            Reads the ezserver_enabled attribute in the object.

            :rtype: None or the ezserver-enabled value .

        """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.
                         fibrechannel_configuration_zone,
                         "/rest/running/brocade-fibrechannel-configuration/"
                         "chassis-config-settings",
                         version.VER_RANGE_821_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute("firmware-synchronization-enabled",
                 pyfos_type.type_bool, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "http-session-ttl", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("ezserver-enabled",
                 pyfos_type.type_bool, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.load(dictvalues, 1)
