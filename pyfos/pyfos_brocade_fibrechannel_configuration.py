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
:mod:`pyfos_brocade_fibrechannel_configuration` - PyFOS module to configure \
FC switches.
****************************************************************************\
*************
The :mod:`pyfos_brocade_fibrechannel_configuration` module provides REST \
support for the FC switch configure CLI.
"""

from pyfos import pyfos_rest_util
from pyfos.pyfos_type import pyfos_type
import pyfos.pyfos_version as version


class switch_configuration(pyfos_rest_util.rest_object):
    """Class of Configurable Parameters of a FC Switch

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
        |                | Address bits |:meth:`peek_area_mode`       |
        |                | for the area.|                             |
        +----------------+--------------+-----------------------------+

    *Object Methods*

        .. method:: get(session)

            Returns a :class:`switch_configuration` object with attributes
            from the switch.

            Each object can be printed using :func:`pyfos_util.response_print`,
            and individual attributes can be accessed through peek methods.

            :param session: The session handler returned by the
                :func:`pyfos_auth.login`.
            :rtype: A dictionary of errors or a
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
            :rtype: A dictionary of errors or success information.

    *Attribute Methods*

        .. method:: set_wwn_port_id_mode(mode)

            Sets the WWN-based PID in the object.

            :param mode: The mode configures the WWN-based PID in the object.

            :rtype: None or a dictionary of errors information.

        .. method:: peek_wwn_port_id_mode()

            Reads the enabled state of the WWN-based PID in the object.

            :rtype: True or False.

        .. method:: set_edge_hold_time(time)

            Sets the edge hold time in the object.

            :param time: The edge hold time in the switch to be set within
                         the object.

            :rtype: None or a dictionary of errors information.

        .. method:: peek_edge_hold_time()

            Reads the edge hold time in the object.

            :rtype: The edge hold time of the switch.

        .. method:: set_area_mode(mode)

            Sets the port address bit based on the area in the object.

            :param mode: The mode value for the PID area limit within
                         the object.

            :rtype: None or a dictionary of errors information.

        .. method:: peek_area_mode()

            Reads the mode of the port address bits in the object.

            :rtype: None or the mode of the port address of the switch.

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

        self.load(dictvalues, 1)


class f_port_login_settings(pyfos_rest_util.rest_object):
    """Class of configurable parameters of the FC switch corresponding to
    F_Port login

    Class Members:

+-------------------------+-----------+---------------------------------------+
|Attribute Name           |Description|Frequently Used Methods                |
+=========================+===========+=======================================+
|max-logins               |Sets the   |:meth:`set_max_logins`                 |
|                         |maximum    |:meth:`peek_max_logins`                |
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
|                         |in port.   |                                       |
+-------------------------+-----------+---------------------------------------+

    *Object Methods*

        .. method:: get(session)

            Returns a :class:`switch` object with attributes from the switch.

            Each object can be printed using :func:`pyfos_util.response_print`,
            and individual attributes can be accessed through peek methods.

            :param session: The session handler returned by the
                :func:`pyfos_auth.login`
            :rtype: A dictionary of errors or a
                :class:`switch` object

        .. method:: patch(session)

            Apply configurable attribute(s) within the object to the switch.

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
            :rtype: A dictionary of errors or success information.

    *Attribute Methods*

        .. method:: set_max_logins(value)

            Sets the switch-wide maximum logins in the object.

            :param value: The maximum number of logins within the object.
            :rtype: None or a dictionary of error information.

        .. method:: peek_max_logins()

            Reads the switch-wide maximum logins in the object.

            :rtype: None or a dictionary of errors information.

        .. method:: set_max_flogi_rate_per_switch(value)

            Sets the maximum FLOGI rate per switch in the object.

            :param value: The maximum FLOGI rate in the switch to be set
                          within the object.
            :rtype: None or a dictionary of errors information.

        .. method:: peek_max_flogi_rate_per_switch()

            Reads the maximum FLOGI rate per switch in the object.

            :rtype: None or a dictionary of errors information.

        .. method:: set_stage_interval(value)

            Sets the staging interval in the object.

            :param value: The stage interval to be set within the object.
            :rtype: None or a dictionary of errors information.

        .. method:: peek_stage_interval()

            Reads the staging interval in the object.

            :rtype: None or the staging interval in the object.

        .. method:: set_free_fdisc(value)

            Sets the number of FLOGIs allowed before staging in the object.

            :param value: The number of FLOGIs allowed before staging to be
                          set within the object.
            :rtype: None or a dictionary of errors information.

        .. method:: peek_free_fdisc()

            Reads the number of FLOGIs allowed before staging in the object.

            :rtype: None or the number of FLOGIs allowed before staging in
                    the switch.

        .. method:: set_enforce_login(value)

            Sets the enforcement for login precedence in the object.

            :param value: The enforcement for login precedence to be set
                          within the object.
            :rtype: None or a dictionary of errors information.

        .. method:: peek_enforce_login()

            Reads the enforcement for login precedence in the object.

            :rtype: None or the login type precedence in the switch.

        .. method:: set_max_flogi_rate_per_port(value)

            Sets the maximum FLOGI rate per port in the object.

            :param value: The maximum FLOGI rate per port to be set within
                          the object.
            :rtype: None or a dictionary of errors information.

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
            :rtype: A dictionary of errors or a
                :class:`port_configuration` object.

        .. method:: patch(session)

            Apply configurable attribute(s) within the object to the port
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
            :rtype: A dictionary of errors or success information.

    *Attribute Methods*

        .. method:: set_portname_mode(mode)

            Sets the portname-mode attribute in the object.

            :param mode: The port name mode.
            :rtype: None or a dictionary of errors information.

        .. method:: peek_portname_mode()

            Reads the portname-mode attribute in the object.

            :rtype: None or a port name mode.

        .. method:: set_dynamic_portname_format(portname_format)

            Sets the dynamic-port name-format attribute in the object.

            :param portname_format: the dynamic port name format.
            :rtype: None or a dictionary of errors information.

        .. method:: peek_dynamic_portname_format()

            Reads the dynamic-portname-format attribute in the object.

            :rtype: None or a dynamic port name format.

        .. method:: set_dynamic_d_port_enabled(value)

            Sets the dynamic-d-port-enabled attribute in the object.

            :param value: A boolean value.
            :rtype: None or a dictionary of errors information.

        .. method:: peek_dynamic_d_port_enabled()

            Reads the dynamic-d-port-enabled attribute in the object.

            :rtype: None or a dynamic D_Port-enabled value.

        .. method:: set_on_demand_d_port_enabled(value)

            Sets the on-demand-d-port-enabled attribute in the object.

            :param value: A boolean value.
            :rtype: None or a dictionary of errors information.

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
       to zoning

    Class Members:

+-------------------------+------------+-------------------------------------+
|Attribute Name           |Description |Frequently Used Methods              |
+=========================+============+=====================================+
|node-name-zoning-enabled |If the node |:meth:`set_node_name_zoning_enabled` |
|                         |name check  |:meth:`peek_node_name_zoning_enabled`|
|                         |is enabled  |                                     |
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
            :rtype: A dictionary of errors or a
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
            :rtype: A dictionary of errors or success information.

    *Attribute Methods*

        .. method:: set_node_name_zoning_enabled(value)

            Sets the node-name-zoning-enabled attribute in the object.

            :param value: A boolean value.
            :rtype: None or a dictionary of errors information.

        .. method:: peek_node_name_zoning_enabled()

            Reads the node-name-zoning-enabled attribute in the object.

            :rtype: None or the node-name-zoning-enabled value.

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

        self.load(dictvalues, 1)


class fabric(pyfos_rest_util.rest_object):
    """Class of configurable parameters of the FC switch

    Important class members:

+-----------------------------+------------+---------------------------------------+
| Attribute Name              |Description |Frequently Used Methods                |
+=============================+============+=======================================+
| insistent-domain-id-enabled |Sets the    |meth:`set_insistent_domain_id_enabled` |
|                             |consistent  |meth:`peek_insistent_domain_id_enabled`|
|                             |domain ID   |                                       |
|                             |mode.       |                                       |
+-----------------------------+------------+---------------------------------------+

    *Object Methods*

        .. method:: get(session)

            Returns a :class:`fabric` object with attributes from the switch.

            Each object can be printed using :func:`pyfos_util.response_print`,
            and individual attributes can be accessed through peek methods.

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary of errors or a
                :class:`fabric` object.

        .. method:: patch(session)

            Apply configurable attribute(s) within the object to the fabric.

            *Example Using Individual Sets:*

            .. code-block:: python

                # initialize the fabric object
                fabric_obj = pyfos_brocade_fibrechannel_configuration.fabric()
                # set the idid mode attribute to enable the
                # insistent domain on the switch
                fabric_obj.set_insistent_domain_id_enabled(True)
                # execute HTTP patch command to apply the object to the
                # switch connected through session
                fabric_obj.patch(session)

            *Example of Combining Object Initialization \
                     and Attribute Sets:*

            .. code-block:: python

                # initialize the fabric object and
                # set the insistent-domain-id-enabled attribute
                fabric_obj = pyfos_brocade_fibrechannel_configuration.fabric(
                    {"insistent-domain-id-enabled" : True})
                # execute HTTP patch command to apply the object to the
                # switch connected through session
                fabric_obj.patch(session)

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: a dictionary of error or success information

    *Attribute Methods*

        .. method:: set_insistent_domain_id_enabled(mode)

            Sets the Insistent Domain ID feature.

            :param mode: The mode value configures the IDID feature.

            :rtype: None or a dictionary of errors information.

        .. method:: peek_insistent_domain_id_enabled()

            Reads the status of the Insistent Domain ID feature.

            :rtype: True or False

        """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.fabric,
                         "/rest/running/brocade-fibrechannel-configuration/"
                         "fabric",
                         version.VER_RANGE_821_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "insistent-domain-id-enabled", pyfos_type.type_bool,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.load(dictvalues, 1)
