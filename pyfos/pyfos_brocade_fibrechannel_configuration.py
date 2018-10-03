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
:mod:`pyfos_brocade_fibrechannel_configuration` - PyFOS module for configure.
*******************************************************************************
The :mod:`pyfos_brocade_fibrechannel_configuration` provides REST support for \
        FC switch configure CLI.
"""

import pyfos.pyfos_rest_util as pyfos_rest_util
from pyfos.pyfos_type import pyfos_type
import pyfos.pyfos_version as version


class switch_configuration(pyfos_rest_util.rest_object):
    """Class of configurable parameters of FC switch

    Important class members:

        +----------------+--------------+-----------------------------+
        | Attribute name | Description  |Frequently used methods      |
        +================+==============+=============================+
        |wwn-port-id-mode| WWN flag for |:meth:`set_wwn_port_id_mode` |
        |                | PID in switch|:meth:`peek_wwn_port_id_mode`|
        +----------------+--------------+-----------------------------+
        |edge-hold-time  | Time duration|:meth:`set_edge_hold_time`   |
        |                | for frames   |:meth:`peek_edge_hold_time`  |
        +----------------+--------------+-----------------------------+
        |area-mode       | The address  |:meth:`set_area_mode`        |
        |                | bits for area|:meth:`peek_area_mode`       |
        +----------------+--------------+-----------------------------+

    *Object methods*

        .. method:: get(session)

            Returns a :class:`switch_configuration` object with attributes
            from switch.

            Each object can be printed using :func:`pyfos_util.response_print`
            and individual attributes accessed through peek methods.

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary of error or a
                :class:`switch` object

        .. method:: patch(session)

            Apply configurable attribute(s) within the object to switch.

            *Below is an example using individual sets:*

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

            *Below is an example of combining object \
                    initialization and attribute sets:*

            .. code-block:: python

                # initialize the switch object and
                # set the enable-state attribute
                switch_obj =
                pyfos_brocade_fibrechannel_configuration.switch_configuration(
                    {"wwn-port-id-mode" : True})
                # execute HTTP patch command to apply the object to the
                # switch connected through session
                switch_obj.patch(session)

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: a dictionary of error or success information

    *Attribute methods*

        .. method:: set_wwn_port_id_mode(mode)

            Sets wwn based pid in the object.

            :param mode: Mode value configures wwn based pid within the object

            :rtype: None or dictionary of error information

        .. method:: peek_wwn_port_id_mode()

            Reads the enabled stated of wwn based pid in the object.

            :rtype: True or False

        .. method:: set_edge_hold_time(time)

            Sets edge hold time in the object.

            :param time: Edge hold time in the switch to be set within the
                         object

            :rtype: None or dictionary of error information

        .. method:: peek_edge_hold_time()

            Reads edge hold time in the object.

            :rtype: Edge hold time of the switch

        .. method:: set_area_mode(mode)

            Sets the port address bit based on area in the object.

            :param mode: Mode value for area limit for pid within the object

            :rtype: None or dictionary of error information

        .. method:: peek_area_mode()

            Reads the mode of port address bits in the object.

            :rtype: None or mode of port address of the switch

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
    """Class of configurable parameters of FC switch corresponding to
    f-port login

    Class members:

+-------------------------+-----------+---------------------------------------+
|Attribute name           |Description|Frequently used methods                |
+=========================+===========+=======================================+
|max-logins               |Maximum    |:meth:`set_max_logins`                 |
|                         |logins     |:meth:`peek_max_logins`                |
+-------------------------+-----------+---------------------------------------+
|max-flogi-rate-per-switch|FLOGIs rate|:meth:`set_max_flogi_rate_per_switch`  |
|                         |in switch  |:meth:`peek_max_flogi_rate_per_switch` |
+-------------------------+-----------+---------------------------------------+
|stage-interval           |Stage      |:meth:`set_stage_interval`             |
|                         |Interval   |:meth:`peek_stage_interval`            |
+-------------------------+-----------+---------------------------------------+
|free-fdisc               |Allowed    |:meth:`set_free_fdisc`                 |
|                         |FDISC      |:meth:`peek_free_fdisc`                |
+-------------------------+-----------+---------------------------------------+
|enforce-login            |Login type |:meth:`set_enforce_login`              |
|                         |precedence |:meth:`peek_enforce_login`             |
+-------------------------+-----------+---------------------------------------+
|max-flogi-rate-per-port  |FLOGIs rate|:meth:`set_max_flogi_rate_per_port`    |
|                         |in port    |:meth:`peek_max_flogi_rate_per_port`   |
+-------------------------+-----------+---------------------------------------+

    *Object methods*

        .. method:: get(session)

            Returns a :class:`switch` object with attributes from switch.

            Each object can be printed using :func:`pyfos_util.response_print`
            and individual attributes accessed through peek methods.

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary of error or a
                :class:`switch` object

        .. method:: patch(session)

            Apply configurable attribute(s) within the object to switch.

            *Below is an example using individual sets:*

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

            *Below is an example of combining object \
                    initialization and attribute sets:*

            .. code-block:: python

                # initialize the switch object and
                # set the max-logins attribute
                obj =
                pyfos_brocade_fibrechannel_configuration.f_port_login_settings(
                    {"max-logins" : 1})
                # execute HTTP patch command to apply the object to the
                # switch connected through session
                obj.patch(session)

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: a dictionary of error or success information

    *Attribute methods*

        .. method:: set_max_logins(value)

            Sets switch-wide maximum logins in the object.

            :param value: Max no. of logins within the object
            :rtype: None or dictionary of error information

        .. method:: peek_max_logins()

            Reads the switch-wide maximum logins in the object.

            :rtype: None or dictionary of error information

        .. method:: set_max_flogi_rate_per_switch(value)

            Sets max flogi rate per switch in the object.

            :param value: Max flogi rate in the switch to be set within the
                          object
            :rtype: None or dictionary of error information

        .. method:: peek_max_flogi_rate_per_switch()

            Reads max flogi rate per switch in the object.

            :rtype: None or dictionary of error information

        .. method:: set_stage_interval(value)

            Sets the staging interval in the object.

            :param value: Stage Interval to be set within the object
            :rtype: None or dictionary of error information

        .. method:: peek_stage_interval()

            Reads the staging interval in the object.

            :rtype: None or the staging interval in the object.

        .. method:: set_free_fdisc(value)

            Sets the No. of flogis allowed before staging in the object.

            :param value: No. of flogis allowed before staging to be set
                            within the object
            :rtype: None or dictionary of error information

        .. method:: peek_free_fdisc()

            Reads the No. of flogis allowed before staging in the object.

            :rtype: None or the No. of flogis allowed before staging in
                    the switch

        .. method:: set_enforce_login(value)

            Sets the enforcement for login precedence in the object.

            :param value: The enforcement for login precedence to be set
                          within the object
            :rtype: None or dictionary of error information

        .. method:: peek_enforce_login()

            Reads the enforcement for login precedence in the object.

            :rtype: None or the login type precedence in the switch

        .. method:: set_max_flogi_rate_per_port(value)

            Sets the max flogi rate per port in the object.

            :param value: Max flogi rate per port to be set within the object
            :rtype: None or dictionary of error information

        .. method:: peek_max_flogi_rate_per_port()

            Reads the max flogi rate per port in the object.

            :rtype: None or the max flogi rate per port in the switch

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
    """Class of configurable parameters of FC switch corresponding to ports

    Class members:

+------------------------+-------------+--------------------------------------+
| Attribute name         | Description |Frequently used methods               |
+========================+=============+======================================+
|portname-mode           | Current     |:meth:`set_portname_mode`             |
|                        | portname    |:meth:`peek_portname_mode`            |
|                        | mode        |                                      |
+------------------------+-------------+--------------------------------------+
|dynamic-portname-format | Format of   |:meth:`set_dynamic_portname_format`   |
|                        | dynamic     |:meth:`peek_dynamic_portname_format`  |
|                        | portname    |                                      |
+------------------------+-------------+--------------------------------------+
|dynamic-d-port-enabled  | If dynamic  |:meth:`set_dynamic_d_port_enabled`    |
|                        | D-port is   |:meth:`peek_dynamic_d_port_enabled`   |
|                        | enabled     |                                      |
+------------------------+-------------+--------------------------------------+
|on-demand-d-port-enabled| If on-demand|:meth:`set_on_demand_d_port_enabled`  |
|                        | D-port is   |:meth:`peek_on_demand_d_port_enabled` |
|                        | enabled     |                                      |
+------------------------+-------------+--------------------------------------+

    *Object methods*

        .. method:: get(session)

            Returns a :class:`port_configuration` object with attributes from
            port configuration

            Each object can be printed using :func:`pyfos_util.response_print`
            and individual attributes accessed through peek methods.

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary of error or a
                :class:`port_configuration` object

        .. method:: patch(session)

            Apply configurable attribute(s) within the object to port
            configuraiton.

            *Below is an example using individual sets:*

            .. code-block:: python

                # Initialize the port_configuration object
                obj =
                pyfos_brocade_fibrechannel_configuration.port_configuration()
                # Set the portname-mode attribute
                obj.set_portname_mode('default')
                # Execute HTTP patch command to apply the object to the
                # switch connected through session
                obj.patch(session)

            *Below is an example of combining object \
                    initialization and attribute sets:*

            .. code-block:: python

                # Initialize the port_configuration object and
                # set the portname-mode attribute
                obj =
                pyfos_brocade_fibrechannel_configuration.port_configuration(
                    {"portname-mode" : 'default'})
                # Execute HTTP patch command to apply the object to the
                # switch connected through session
                obj.patch(session)

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: a dictionary of error or success information

    *Attribute methods*

        .. method:: set_portname_mode(mode)

            Sets portname-mode attribute in the object.

            :param mode: portname mode
            :rtype: None or dictionary of error information

        .. method:: peek_portname_mode()

            Reads portname-mode attribute in the object.

            :rtype: None or portname mode

        .. method:: set_dynamic_portname_format(portname_format)

            Sets dynamic-portname-format attribute in the object.

            :param portname_format: dynamic portname format
            :rtype: None or dictionary of error information

        .. method:: peek_dynamic_portname_format()

            Reads dynamic-portname-format attribute in the object.

            :rtype: None or dynamic portname format

        .. method:: set_dynamic_d_port_enabled(value)

            Sets dynamic-d-port-enabled attribute in the object.

            :param value: boolean value
            :rtype: None or dictionary of error information

        .. method:: peek_dynamic_d_port_enabled()

            Reads dynamic-d-port-enabled attribute in the object.

            :rtype: None or dynamic D-port enabled value.

        .. method:: set_on_demand_d_port_enabled(value)

            Sets on-demand-d-port-enabled attribute in the object.

            :param value: boolean value
            :rtype: None or dictionary of error information

        .. method:: peek_on_demand_d_port_enabled()

            Reads on-demand-d-port-enabled attribute in the object.

            :rtype: None or on-demand D-port enabled value

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
    """Class of configurable parameters of FC switch corresponding to zoning

    Class members:

+--------------------------+------------+-------------------------------------+
| Attribute name           | Description|Frequently used methods              |
+==========================+============+=====================================+
| node-name-zoning-enabled | If node    |:meth:`set_node_name_zoning_enabled` |
|                          | name check |:meth:`peek_node_name_zoning_enabled`|
|                          | is enabled |                                     |
|                          | for zoning |                                     |
+--------------------------+------------+-------------------------------------+

    *Object methods*

        .. method:: get(session)

            Returns a :class:`zone_configuration` object with attributes from
            zone configuration

            Each object can be printed using :func:`pyfos_util.response_print`
            and individual attributes accessed through peek methods.

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary of error or a
                :class:`zone_configuration` object

        .. method:: patch(session)

            Apply configurable attribute(s) within the object to zone
            configuraiton.

            *Below is an example using individual sets:*

            .. code-block:: python

                # Initialize the zone_configuration object
                obj =
                pyfos_brocade_fibrechannel_configuration.zone_configuration()
                # Set the node-name-zoning-enabled attribute
                obj.set_node_name_zoning_enabled('true')
                # Execute HTTP patch command to apply the object to the
                # switch connected through session
                obj.patch(session)

            *Below is an example of combining object \
                    initialization and attribute sets:*

            .. code-block:: python

                # Initialize the zone_configuration object and
                # set the node-name-zoning-enabled attribute
                obj =
                pyfos_brocade_fibrechannel_configuration.node-name-zoning-enabled(
                    {"node-name-zoning-enabled" : 'true'})
                # Execute HTTP patch command to apply the object to the
                # switch connected through session
                obj.patch(session)

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: a dictionary of error or success information

    *Attribute methods*

        .. method:: set_node_name_zoning_enabled(value)

            Sets node-name-zoning-enabled attribute in the object.

            :param value: boolean value
            :rtype: None or dictionary of error information

        .. method:: peek_node_name_zoning_enabled()

            Reads node-name-zoning-enabled attribute in the object.

            :rtype: None or node name zoning enabled value.

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
    """Class of configurable parameters of FC switch

    Important class members:

+-----------------------------+------------+---------------------------------------+
| Attribute name              |Description |Frequently used methods                |
+=============================+============+=======================================+
| insistent-domain-id-enabled |set         |meth:`set_insistent_domain_id_enabled` |
|                             |consistent  |meth:`peek_insistent_domain_id_enabled`|
|                             |domain id   |                                       |
|                             |mode.       |                                       |
+-----------------------------+------------+---------------------------------------+

    *Object methods*

        .. method:: get(session)

            Returns a :class:`fabric` object with attributes from switch.

            Each object can be printed using :func:`pyfos_util.response_print`
            and individual attributes accessed through peek methods.

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary of error or a
                :class:`fabric` object

        .. method:: patch(session)

            Apply configurable attribute(s) within the object to fabric.

            *Below is an example using individual sets:*

            .. code-block:: python

                # initialize the fabric object
                fabric_obj = pyfos_brocade_fibrechannel_configuration.fabric()
                # set the idid mode attribute to enable the
                # insistent domain on the switch
                fabric_obj.set_insistent_domain_id_enabled(True)
                # execute HTTP patch command to apply the object to the
                # switch connected through session
                fabric_obj.patch(session)

            *Below is an example of combining object \
                    initialization and attribute sets:*

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

    *Attribute methods*

        .. method:: set_insistent_domain_id_enabled(mode)

            Sets the Insistent Domain ID feature.

            :param mode: Mode value configures idid feature.

            :rtype: None or dictionary of error information

        .. method:: peek_insistent_domain_id_enabled()

            Reads the status of the Insistent domain id feature.

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
