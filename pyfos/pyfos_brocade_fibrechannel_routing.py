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

# pyfos_brocade_fibrechannel_routing.py(pyGen v1.0.0)

"""

:mod:`pyfos_brocade_fibrechannel_routing` - PyFOS module provides REST \
support for FC Router switch
******************************************************************************\
*******************************************************************************
The :mod:`pyfos_brocade_fibrechannel_routing` provides REST support for \
FC Router switch
"""


# Start module imports
from pyfos import pyfos_rest_util
from pyfos.pyfos_type import pyfos_type
from pyfos import pyfos_version as version
# End module imports


class lsan_zone(pyfos_rest_util.rest_object):

    """Class of lsan_zone

    *Description lsan_zone*

        Displays the list of LSAN zone members in a particular zone.

    Important class members of lsan_zone:

        +--------------------------+---------------------------------+-------------------------------------------------+
        | Attribute Name           | Description                     |  Frequently Used Methods                        |
        +==========================+=================================+=================================================+
        | member                   | The member of the zone          | :func:`peek_members_member`                     |
        |                          |                                 |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | members                  | Contains the list of LSAN       | :func:`peek_members`                            |
        |                          | zone members of a particular    |                                                 |
        |                          | zone                            |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | zone-name                | The name of the zone            | :func:`peek_zone_name`                          |
        |                          |                                 |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | edge-fabric-id           | The ID of the fabric in which   | :func:`peek_edge_fabric_id`                     |
        |                          | the LSAN zone was created       |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+

    *Object functions for lsan_zone*

    .. function:: get()

        Get the instances of class "lsan_zone from switch. The object can be
         printed using :func:`pyfos_utils.response_print`.

        :param session: The session handler returned by
         :func:`pyfos_auth.login`.

        :rtype: A dictionary of errors or a success response.


    *Class functions for lsan_zone*

        .. function:: peek_members_member()

            Reads the value assigned to member in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_members()

            Reads the value assigned to members in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_zone_name()

            Reads the value assigned to zone-name in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_edge_fabric_id()

            Reads the value assigned to edge-fabric-id in the object.

            :rtype: None on error and a value on success.


    """

    def __init__(self, dictvalues=None):

        clsuri = "/rest" + "/running" + "/brocade-fibrechannel-routing" +\
                 "/lsan-zone"
        clstype = pyfos_rest_util.rest_obj_type.lsan_zone
        clsver = version.VER_RANGE_900_and_ABOVE
        super().__init__(clstype, clsuri, clsver)

        self.add(pyfos_rest_util.rest_attribute("zone-name",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("edge-fabric-id",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("members", pyfos_type.type_na,
                 dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute("member", pyfos_type.type_na,
                 None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST),
                 ['members'])
        self.load(dictvalues, 1)


class lsan_device(pyfos_rest_util.rest_object):

    """Class of lsan_device

    *Description lsan_device*

        Displays the information of each device.

    Important class members of lsan_device:

        +--------------------------+---------------------------------+-------------------------------------------------+
        | Attribute Name           | Description                     |  Frequently Used Methods                        |
        +==========================+=================================+=================================================+
        | proxy-pid                | The proxy pid of the device.    | :func:`peek_proxy_pid`                          |
        |                          |                                 |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | device-status            | States include:  configured     | :func:`peek_device_status`                      |
        |                          | - Device is configured to be    |                                                 |
        |                          | in an LSAN, but the device      |                                                 |
        |                          | is neither imported nor         |                                                 |
        |                          | exists in this fabric           |                                                 |
        |                          | initializing - Device is in     |                                                 |
        |                          | an intermediate state. It is    |                                                 |
        |                          | not yet imported into the       |                                                 |
        |                          | fabric. exist- Device exists    |                                                 |
        |                          | in this fabric (the fabric      |                                                 |
        |                          | of the zone entry).             |                                                 |
        |                          | imported   - Device has been    |                                                 |
        |                          | imported (proxy created) into   |                                                 |
        |                          | this fabric.                    |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | device-wwn               | The WWN of the device.          | :func:`peek_device_wwn`                         |
        |                          |                                 |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | imported-fabric-id       | The fabric in which the         | :func:`peek_imported_fabric_id`                 |
        |                          | devices are imported.           |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | physical-pid             | The port ID of the device in    | :func:`peek_physical_pid`                       |
        |                          | source fabric.                  |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | source-fabric-id         | The fabric in which the         | :func:`peek_source_fabric_id`                   |
        |                          | device are physically           |                                                 |
        |                          | present.                        |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+

    *Object functions for lsan_device*

    .. function:: get()

        Get the instances of class "lsan_device from switch. The object can be
         printed using :func:`pyfos_utils.response_print`.

        :param session: The session handler returned by
         :func:`pyfos_auth.login`.

        :rtype: A dictionary of errors or a success response.


    *Class functions for lsan_device*

        .. function:: peek_proxy_pid()

            Reads the value assigned to proxy-pid in the object.

            :rtype: None on error and a value on success.


       .. function:: peek_device_status()

            Reads the value assigned to device-status in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_device_wwn()

            Reads the value assigned to device-wwn in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_imported_fabric_id()

            Reads the value assigned to imported-fabric-id in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_physical_pid()

            Reads the value assigned to physical-pid in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_source_fabric_id()

            Reads the value assigned to source-fabric-id in the object.

            :rtype: None on error and a value on success.


    """

    def __init__(self, dictvalues=None):

        clsuri = "/rest" + "/running" + "/brocade-fibrechannel-routing" +\
                 "/lsan-device"
        clstype = pyfos_rest_util.rest_obj_type.lsan_device
        clsver = version.VER_RANGE_900_and_ABOVE
        super().__init__(clstype, clsuri, clsver)

        self.add(pyfos_rest_util.rest_attribute("proxy-pid",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("device-status",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("device-wwn",
                 pyfos_type.type_wwn, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("imported-fabric-id",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("physical-pid",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("source-fabric-id",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.load(dictvalues, 1)


class edge_fabric_alias(pyfos_rest_util.rest_object):

    """Class of edge_fabric_alias

    *Description edge_fabric_alias*

        Displays edge fabric id's corresponding alias name

    Important class members of edge_fabric_alias:

        +--------------------------+---------------------------------+-------------------------------------------------+
        | Attribute Name           | Description                     |  Frequently Used Methods                        |
        +==========================+=================================+=================================================+
        | edge-fabric-id           | The ID of the fabric in which   | :func:`set_edge_fabric_id`                      |
        |                          | the LSAN zone was created       | :func:`peek_edge_fabric_id`                     |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | alias-name               | Alias name of the specific      | :func:`set_alias_name`                          |
        |                          | edge fabric id.                 | :func:`peek_alias_name`                         |
        +--------------------------+---------------------------------+-------------------------------------------------+

    *Object functions for edge_fabric_alias*

    .. function:: get()

        Get the instances of class "edge_fabric_alias from switch. The object
         can be printed using :func:`pyfos_utils.response_print`.

        :param session: The session handler returned by
         :func:`pyfos_auth.login`.

        :rtype: A dictionary of errors or a success response.

    .. function:: post()

        Creates an entry or adds members. The required fields are set
        within the object using the attribute's set method.
        This method is used to create a new edge fabric alias name for
        the given edge fabric id.

        Example Usage of the post function to create edge fabric alias name:

        .. code-block:: python

            edge_fabric_aliasObj = edge_fabric_alias()
            edge_fabric_aliasObj.set_edge_fabric_id(edge_fabric_id)
            edge_fabric_aliasObj.set_alias_name(alias_name)
            edge_fabric_aliasObj.post(session)

        The above function will create edge fabric alias name for the
        provided edge fabrc id.

        :param session: The session handler returned by
         :func:`pyfos_auth.login`.

        :rtype: A dictionary of errors or a success response.

    .. function:: patch()

        Replaces entry members. The required fields are set within the
        object using the attribute's set method.
        This method is used to replace the existing edge fabric alias name of
        an edge fabric id.

        Example Usage of the patch function to modify edge fabric alias name:

        .. code-block:: python

            edge_fabric_aliasObj = edge_fabric_alias()
            edge_fabric_aliasObj.set_edge_fabric_id(edge_fabric_id)
            edge_fabric_aliasObj.set_alias_name(alias_name)
            edge_fabric_aliasObj.patch(session)

        The above function will replace the edge fabric alias name for the
        provided edge fabrc id with the newly provided alias name.

        :param session: The session handler returned by
         :func:`pyfos_auth.login`.

        :rtype: A dictionary of errors or a success response.

    .. function:: delete()

        Deletes an entry or entry members.. The required fields are set within
        the object using the attribute's set method.
        This method is used to delete the edge fabric alias name for the
        given  edge fabric id.

        Example Usage of the delete function to delete edge fabric alias name:

        .. code-block:: python

            edge_fabric_aliasObj = edge_fabric_alias()
            edge_fabric_aliasObj.set_edge_fabric_id(edge_fabric_id)
            edge_fabric_aliasObj.set_alias_name(alias_name)
            edge_fabric_aliasObj.delete(session)

        The above function will delete the edge fabric alias name for the
        given edge fabrc id.

        :param session: The session handler returned by
         :func:`pyfos_auth.login`.

        :rtype: A dictionary of errors or a success response.

    *Class functions for edge_fabric_alias*

        .. function:: peek_edge_fabric_id()

            Reads the value assigned to edge-fabric-id in the object.

            :rtype: None on error and a value on success.


        .. function:: set_edge_fabric_id(value)

            Set the value of edge-fabric-id in the object.

            :rtype: A dictionary of error or a success response and a value
             with "edge-fabric-id" as the key


        .. function:: peek_alias_name()

            Reads the value assigned to alias-name in the object.

            :rtype: None on error and a value on success.


        .. function:: set_alias_name(value)

            Set the value of alias-name in the object.

            :rtype: A dictionary of error or a success response and a value
             with "alias-name" as the key


    """

    def __init__(self, dictvalues=None):

        clsuri = "/rest" + "/running" + "/brocade-fibrechannel-routing" +\
                 "/edge-fabric-alias"
        clstype = pyfos_rest_util.rest_obj_type.edge_fabric_alias
        clsver = version.VER_RANGE_900_and_ABOVE
        super().__init__(clstype, clsuri, clsver)

        self.add(pyfos_rest_util.rest_attribute("edge-fabric-id",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute("alias-name",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.load(dictvalues, 1)


class routing_configuration(pyfos_rest_util.rest_object):

    """Class of routing_configuration

    *Description routing_configuration*

        Generic FCR configuration parameters.

    Important class members of routing_configuration:

        +--------------------------+---------------------------------+-------------------------------------------------+
        | Attribute Name           | Description                     |  Frequently Used Methods                        |
        +==========================+=================================+=================================================+
        | shortest-ifl             | Enables or disables the         | :func:`set_shortest_ifl`                        |
        |                          | shortest IFL mode in FC         | :func:`peek_shortest_ifl`                       |
        |                          | Router. When the shortest IFL   |                                                 |
        |                          | mode is enabled, FC Router      |                                                 |
        |                          | can choose a lowest-cost IFL    |                                                 |
        |                          | path in the backbone fabric.    |                                                 |
        |                          | TRUE : Enables the shortest     |                                                 |
        |                          | IFL mode FALSE : Disables the   |                                                 |
        |                          | shortest IFL mode               |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | tag                      | Accepts only the LSANs from     | :func:`set_lsan_enforce_tags_tag`               |
        |                          | the edge fabric that matches    | :func:`peek_lsan_enforce_tags_tag`              |
        |                          | the specified tag string into   |                                                 |
        |                          | the local FCR database. A       |                                                 |
        |                          | valid tag is a string of a      |                                                 |
        |                          | maximum of eight characters.    |                                                 |
        |                          | The maximum configurable        |                                                 |
        |                          | enforce tags is eight. In       |                                                 |
        |                          | case speed tag is configured,   |                                                 |
        |                          | only seven enforce tags can     |                                                 |
        |                          | be configured. Empty tags are   |                                                 |
        |                          | not allowed.                    |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | backbone-fabric-id       | Specifies the Backbone Fabric   | :func:`set_backbone_fabric_id`                  |
        |                          | ID. It uniquely identifies a    | :func:`peek_backbone_fabric_id`                 |
        |                          | fabric in FC Router             |                                                 |
        |                          | configurations. The backbone    |                                                 |
        |                          | fabric is the fabric attached   |                                                 |
        |                          | to the U_Ports of the switch,   |                                                 |
        |                          | for example, E_Ports or         |                                                 |
        |                          | F_Ports. The backbone fabric    |                                                 |
        |                          | ID must be unique across all    |                                                 |
        |                          | fabrics connected to the FC     |                                                 |
        |                          | Router.                         |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | lsan-speed-tag           | Allows the FCR to always        | :func:`set_lsan_speed_tag`                      |
        |                          | import these target devices     | :func:`peek_lsan_speed_tag`                     |
        |                          | to the hosts specified in the   |                                                 |
        |                          | LSANs that match the speed      |                                                 |
        |                          | tag. Only one speed tag is      |                                                 |
        |                          | allowed per FC router. Empty    |                                                 |
        |                          | tags are not allowed.           |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | maximum-lsan-count       | The default maximum LSAN        | :func:`set_maximum_lsan_count`                  |
        |                          | count is set to 3000. User      | :func:`peek_maximum_lsan_count`                 |
        |                          | can modify this LSAN count      |                                                 |
        |                          | value. The valid values are     |                                                 |
        |                          | 3000, 5000 and 7500.            |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+

    *Object functions for routing_configuration*

    .. function:: get()

        Get the instances of class "routing_configuration from switch. The
         object can be printed using :func:`pyfos_utils.response_print`.

        :param session: The session handler returned by
         :func:`pyfos_auth.login`.

        :rtype: A dictionary of errors or a success response.

    .. function:: post()

        Creates an entry or adds members. The required fields are set
        within the object using the attribute's set method.
        This method is used to create a new lsan enforce tag.

        Example Usage of the post function to create lsan enforce tag:

        .. code-block:: python

            routing_configurationObj = routing_configuration()
            routing_configurationObj.set_lsan_enforce_tags_tag(lsan_enforce_tags_tag)
            routing_configurationObj.post(session)

        The above function will create lsan enforce tag.

        :param session: The session handler returned by
         :func:`pyfos_auth.login`.

        :rtype: A dictionary of errors or a success response.

    .. function:: patch()

        Replaces entry members.. The required fields are set within the
        object using the attribute's set method.
        This method is used to modify the backbone fabric id of the FCR
        switch.

        Example Usage of the patch function to modify backbone fabric id:

        .. code-block:: python

            routing_configurationObj = routing_configuration()
            routing_configurationObj.set_backbone_fabric_id(backbone_fabric_id)
            routing_configurationObj.patch(session)

        The above function will modify the backbone fabric id of the FCR
        switch.

        :param session: The session handler returned by
         :func:`pyfos_auth.login`.

        :rtype: A dictionary of errors or a success response.

    .. function:: delete()

        Deletes an entry or entry members. The required fields are set
        within the object using the attribute's set method.
        This method is used to delete lsan enforce tag.

        Example Usage of the function to delete lsan enforce tag:

        .. code-block:: python

            routing_configurationObj = routing_configuration()
            routing_configurationObj.set_lsan_enforce_tags_tag(lsan_enforce_tags_tag)
            routing_configurationObj.delete(session)

        The above function will delete lsan enforce tag.

        :param session: The session handler returned by
         :func:`pyfos_auth.login`.

        :rtype: A dictionary of errors or a success response.

    *Class functions for routing_configuration*

        .. function:: peek_shortest_ifl()

            Reads the value assigned to shortest-ifl in the object.

            :rtype: None on error and a value on success.


        .. function:: set_shortest_ifl(value)

            Set the value of shortest-ifl in the object.

            :rtype: A dictionary of error or a success response and a value
             with "shortest-ifl" as the key


        .. function:: peek_lsan_enforce_tags_tag()

            Reads the value assigned to tag in the object.

            :rtype: None on error and a value on success.


        .. function:: set_lsan_enforce_tags_tag(value)

            Set the value of tag in the object.

            :rtype: A dictionary of error or a success response and a value
             with "tag" as the key


        .. function:: peek_backbone_fabric_id()

            Reads the value assigned to backbone-fabric-id in the object.

            :rtype: None on error and a value on success.


        .. function:: set_backbone_fabric_id(value)

            Set the value of backbone-fabric-id in the object.

            :rtype: A dictionary of error or a success response and a value
             with "backbone-fabric-id" as the key


        .. function:: peek_lsan_speed_tag()

            Reads the value assigned to lsan-speed-tag in the object.

            :rtype: None on error and a value on success.


        .. function:: set_lsan_speed_tag(value)

            Set the value of lsan-speed-tag in the object.

            :rtype: A dictionary of error or a success response and a value
             with "lsan-speed-tag" as the key


        .. function:: peek_maximum_lsan_count()

            Reads the value assigned to maximum-lsan-count in the object.

            :rtype: None on error and a value on success.


        .. function:: set_maximum_lsan_count(value)

            Set the value of maximum-lsan-count in the object.

            :rtype: A dictionary of error or a success response and a value
             with "maximum-lsan-count" as the key


    """

    def __init__(self, dictvalues=None):

        clsuri = "/rest" + "/running" + "/brocade-fibrechannel-routing" +\
                 "/routing-configuration"
        clstype = pyfos_rest_util.rest_obj_type.routing_configuration
        clsver = version.VER_RANGE_900_and_ABOVE
        super().__init__(clstype, clsuri, clsver)

        self.add(pyfos_rest_util.rest_attribute("shortest-ifl",
                 pyfos_type.type_bool, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("backbone-fabric-id",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("lsan-speed-tag",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("maximum-lsan-count",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("lsan-enforce-tags",
                 pyfos_type.type_na, dict(),
                 pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute("tag", pyfos_type.type_na,
                 None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST),
                 ['lsan-enforce-tags'])
        self.load(dictvalues, 1)
