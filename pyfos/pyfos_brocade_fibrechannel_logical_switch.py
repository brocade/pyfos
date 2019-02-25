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

:mod:`pyfos_brocade_fibrechannel_logical_switch` - PyFOS module to \
        provide REST support for Logical Switch objects.
*****************************************************************************************************************************************
The :mod:`pyfos_brocade_fibrechannel_logical_switch` provides a REST \
        support for Logical switch objects.
"""
from pyfos import pyfos_rest_util
from pyfos.pyfos_type import pyfos_type
import pyfos.pyfos_version as version


class fibrechannel_logical_switch(pyfos_rest_util.rest_object):
    """Class of fibrechannel_logical_switch

    Important class members:

        +---------------------------------+--------------------------+---------------------------------------------+
        | Attribute name                  | Description              |Frequently used methods                      |
        +=================================+==========================+=============================================+
        | fabric-id                       | Fabric ID of logical     |:meth:`set_fabric_id`                        |
        |                                 | switch                   |:meth:`peek_fabric_id`                       |
        +---------------------------------+--------------------------+---------------------------------------------+
        | switch-wwn                      | Switch WWN of logical    |:meth:`peek_switch_wwn`                      |
        |                                 | switch                   |                                             |
        +---------------------------------+--------------------------+---------------------------------------------+
        | base-switch-enabled             | The logical switch is    |:meth:`set_base_switch_enabled`              |
        |                                 | enabled as base switch   |:meth:`peek_base_switch_enabled`             |
        +---------------------------------+--------------------------+---------------------------------------------+
        | default-switch-status           | Default switch status of |:meth:`peek_default_switch_status`           |
        |                                 | the logical switch       |                                             |
        +---------------------------------+--------------------------+---------------------------------------------+
        | logical-isl-enabled             | Logical ISLs are enabled |:meth:`set_logical_isl_enabled`              |
        |                                 | in the logical switch    |:meth:`peek_logical_isl_enabled`             |
        +---------------------------------+--------------------------+---------------------------------------------+
        | ficon-mode-enabled              | FICON mode is enabled    |:meth:`set_ficon_mode_enabled`               |
        |                                 | in the logical switch    |:meth:`peek_ficon_mode_enabled`              |
        +---------------------------------+--------------------------+---------------------------------------------+
        | port-member-list/port-member    | List of port members     |:meth:`set_port_member_list_port_member`     |
        |                                 | in the logical switch    |:meth:`peek_port_member_list_port_member`    |
        +---------------------------------+--------------------------+---------------------------------------------+
        | ge-port-member-list/port-member | List of GE port members  |:meth:`set_ge_port_member_list_port_member`  |
        |                                 | in the logical switch    |:meth:`peek_ge_port_member_list_port_member` |
        +---------------------------------+--------------------------+---------------------------------------------+

    *Object methods*

        .. method:: get(session)

            Returns a :class:`fibrechannel_logical_switch` object or a list
            of objects filled with values for all the attributes obtained
            using the session passed in. Each object can be printed using
            :meth:`pyfos_utils.response_print` and individual attributes
            accessed through peek methods.

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary of error or success response

        .. method:: post()

            Create an entry or add members. Fields involved are set
            within the object using attribute's set method.
            This method is used to create a new logical switch with a group
            of ports/GE ports or to add ports/GE ports to an existing
            logical switch. This method is also used to set initial values
            for base switch, FICON mode and logical ISL.

            Example usage of the method to create a new logical switch:

            .. code-block:: python

                ls_obj =
                    pyfos_brocade_fibrechannel_logical_switch.
                    fibrechannel_logical_switch()
                ls_obj.set_fabric_id(1)
                ls_obj.post(session)

            The above example creates a new logical switch having default
            values with fabric id 1.

            Example usage of the method to add port members to an existing
            logical switch with fabric id 5:

            .. code-block:: python

                ls_obj =
                    pyfos_brocade_fibrechannel_logical_switch.
                    fibrechannel_logical_switch()
                ls_obj.set_fabric_id(5)
                ls_obj.set_port_member_list_port_member("0/4;0/5")
                ls_obj.post(session)

            The above example will add ports if a logical switch with
            fabric id 5 exists already.

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary of error or success response

        .. method:: patch()

            Replace entry members. Fields involved are set within the
            object using attribute's set method. This command is used
            to replace the existing member ports or GE ports,
            modify base switch, FICON mode and logical ISL settings.

            Example usage of the method to enable FICON mode in
            a logical switch:

            .. code-block:: python

                ls_obj =
                    pyfos_brocade_fibrechannel_logical_switch.
                    fibrechannel_logical_switch()
                ls_obj.set_fabric_id(5)
                ls_obj.set_ficon_mode_enabled(1)
                ls_obj.patch(session)

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary of error or success response

        .. method:: delete()

            Delete an entry or entry members. Fields involved are
            set within the object using attribute's set method.
            This command is used to delete a logical switch or
            delete the existing port/GE port members.

            Example usage of the method to delete logical switch 1:

            .. code-block:: python

                ls_obj =
                    pyfos_brocade_fibrechannel_logical_switch.
                    fibrechannel_logical_switch()
                ls_obj.set_fabric_id(1)
                ls_obj.delete(session)

            Example usage of the method to delete ports from logical switch 1:

            .. code-block:: python

                ls_obj =
                    pyfos_brocade_fibrechannel_logical_switch.
                    fibrechannel_logical_switch()
                ls_obj.set_fabric_id(1)
                ls_obj.set_port_member_list_port_member("0/4;0/5")
                ls_obj.delete(session)

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary of error or success response

    *Attribute methods*

        .. method:: set_fabric_id(fabric-id)

            Sets Fabric ID in the object.

            :param fabric-id: Fabric ID to be set
            :rtype: None or dictionary of error information

        .. method:: peek_fabric_id()

            Reads Fabric ID from the object.

            :rtype: None on error and value on success

        .. method:: peek_switch_wwn()

            Reads Switch WWN from the object.

            :rtype: None on error and value on success

        .. method:: set_base_switch_enabled(newstate)

            Sets enabled state in the object.

            :param newstate: New base switch state to be set
            :rtype: None or dictionary of error information

        .. method:: peek_base_switch_enabled()

            Reads enabled state from the object.

            :rtype: None on error and value on success

        .. function:: peek_default_switch_status()

            Reads enabled state from the object.

            :rtype: None on error and value on success

        .. method:: set_logical_isl_enabled(newstate)

            Sets enabled state in the object.

            :param newstate: New logical ISL state to be set
            :rtype: None or dictionary of error information

        .. method:: peek_logical_isl_enabled()

            Reads enabled state from the object.

            :rtype: None on error and value on success

        .. method:: set_ficon_mode_enabled(newstate)

            Sets enabled state in the object.

            :param newstate: New FICON mode state to be set
            :rtype: None or dictionary of error information

        .. method:: peek_ficon_mode_enabled()

            Reads enabled state from the object.

            :rtype: None on error and value on success

        .. method:: set_port_member_list_port_member(port_list)

            Sets a list of port entries in port-member-list in the object.

            :param port_list: List of port members
            :rtype: None or dictionary of error information

        .. method:: peek_port_member_list_port_member()

            Reads a list of port entries in port-member-list from the object.

            :rtype: None on error and list of port members on success

        .. method:: set_ge_port_member_list_port_member(port_list)

            Sets a list of GE port entries in port-member-list in the object.

            :param port_list: List of GE port members
            :rtype: None or dictionary of error information

        .. method:: peek_ge_port_member_list_port_member()

            Reads a list of GE port entries in port-member-list from
            the object.

            :rtype: None on error and list of GE port members on success


        """
    def __init__(self, dictvalues={}):
        urilist = list([dict({'URIVER': version.VER_RANGE_820_TO_821A,
                              'URI': "/rest/running/logical-switch/" +
                              "fibrechannel-logical-switch"}),
                        dict({'URIVER': version.VER_RANGE_821b_and_ABOVE,
                              'URI': "/rest/running/brocade-fibrechannel-" +
                              "logical-switch/fibrechannel-logical-switch"})])
        super().__init__(
            pyfos_rest_util.rest_obj_type.logical_switch,
            urilist,
            version.VER_RANGE_820a_and_ABOVE)
        self.add(pyfos_rest_util.rest_attribute(
            "fabric-id", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute(
            "switch-wwn", pyfos_type.type_wwn,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "base-switch-enabled", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "default-switch-status", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "logical-isl-enabled", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "ficon-mode-enabled", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "port-member-list", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute(
            "port-member", pyfos_type.type_str,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST),
            ["port-member-list"])
        self.add(pyfos_rest_util.rest_attribute(
            "ge-port-member-list", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute(
            "port-member", pyfos_type.type_str,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST),
            ["ge-port-member-list"])

        self.load(dictvalues, 1)
