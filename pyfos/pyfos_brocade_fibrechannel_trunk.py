
# Copyright 2017-18 Brocade Communications Systems LLC.  All rights reserved.
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

:mod:`pyfos_brocade_fibrechannel_trunk` - PyFOS module to provide rest \
        support for Trunking.
*********************************************************************************************************
The :mod:`pyfos_brocade_fibrechannel_trunk` provides a REST support for \
        Trunking.

"""

import pyfos.pyfos_rest_util as pyfos_rest_util
from pyfos.pyfos_type import pyfos_type
import pyfos.pyfos_version as version


class trunk(pyfos_rest_util.rest_object):
    """
    Class for TrunkShow which shows E port trunk info.

    Important class members:

        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | Attribute name                    | Description                   |Frequently used methods                                |
        +===================================+===============================+=======================================================+
        | group				    | Group index for the Trunk	    |:func:`peek_group`  	                            |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | master                            | master port  of the Trunk     |:func:`peek_master`                                    |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | source-port                       | User-port numbers of the trunk|:func:`peek_source_port`                               |
        |                                   | of local switch               |                                                       |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | destination-port                  | User-port numbers of the trunk|:func:`peek_destination_port`                          |
        |                                   | of remote switch              |                                                       |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | neighbor-wwn                      | Fibre channel wwn of the      |:func:`peek_neighbor_wwn`                              |
        |                                   | neighbor switch               |                                                       |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | neighbor-switch-name              | user-friendly name of the     |:func:`peek_neighbor_switch_name`                      |
        |                                   | neighbor switch               |                                                       |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | neighbor-domain-id                | Domain-id of the neighbor     |:func:`peek_neighbor_domain_id` 	                    |
        |                                   | switch   		            |                                                       |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | deskew	                    | Link deskew of the trunk      |:func:`peek_deskew`	                            |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
    *Object methods*

        .. method:: get()

            Return :class:`trunk`
            Objects for all trunk groups gathered from the switch.
            When optional params group and source-port params are passed,either
            an object matching the group and source-port is returned
            or an empty object is returned if no match is found.
            When these optional params are passed, both should be set.
            The object can be printed using :func:`pyfos_utils.response_print`

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary of error or
                :class:`trunk` object


    *Attribute methods*

        .. method:: peek_group()

            Reads group in the object.

            :rtype: None or group

        .. method:: peek_master()

            Reads master in the object.

            :rtype: None or master

        .. method:: peek_source_port()

            Reads source port in the object.

            :rtype: None or source port

        .. method:: peek_destination_port()

            Reads destination port in the object.

            :rtype: None or destination port

        .. method:: peek_neighbor_wwn()

            Reads neighbor wwn in the object.

            :rtype: None or neighbor wwn

        .. method:: peek_neighbor_switch_name()

            Reads neighbor_switch_name in the object.

            :rtype: None or neighbor_switch_name

        .. method:: peek_neighbor_domain_id()

            Reads neighbor_domain_id in the object.

            :rtype: None or neighbor_domain_id

        .. method:: peek_deskew()

            Reads deskew in the object.

            :rtype: None or deskew
    """
    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.port_trunk_show,
                         "/rest/running/brocade-fibrechannel-trunk/trunk",
                         version.VER_RANGE_821_and_ABOVE)
        self.add(pyfos_rest_util.rest_attribute(
            "group", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute(
            "source-port", pyfos_type.type_na,
            None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute(
            "destination-port", pyfos_type.type_na,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "neighbor-wwn", pyfos_type.type_wwn,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "neighbor-switch-name", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "neighbor-domain-id", pyfos_type.type_na,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "master", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "deskew", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.load(dictvalues, 1)


class performance(pyfos_rest_util.rest_object):
    """
    Class for Trunk-performance which shows E port trunk performance info.

    Important class members:

        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | Attribute name                    | Description                   |Frequently used methods                                |
        +===================================+===============================+=======================================================+
        | group       		            | group-index for the trunk	    |:func:`peek_group`                               	    |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | tx-bandwidth                      | TX side b/w of the Trunk      |:func:`peek_tx_bandwidth`                              |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | tx-throughput                     |TX side frame transmission rate|:func:`peek_tx_throughput`                             |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | tx-percentage                     | TX side b/w percentage        |:func:`peek_tx_percentage`                             |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | rx-bandwidth                      | RX side b/w of the Trunk      |:func:`peek_rx_bandwidth`                              |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | rx-throughput                     |RX side frame transmission rate|:func:`peek_rx_throughput`                             |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | rx-percentage                     | RX side b/w percentage        |:func:`peek_rx_percentage`                             |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | txrx-bandwidth                    | TXRX side b/w of the Trunk    |:func:`peek_txrx_bandwidth`                            |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | txrx-throughput                   |TXRX frame transmission rate   |:func:`peek_txrx_throughput`                           |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | txrx-percentage                   | TXRX side b/w percentage      |:func:`peek_txrx_percentage`                           |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
    *Object methods*

        .. method:: get()

            Return :class:`performance`
            object with values for all the attributes.
            The object can be printed using :func:`pyfos_utils.response_print`

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary of error or
                :class:`performance` object


    *Attribute methods*

        .. method:: peek_group()

            Reads group in the object.

            :rtype: None or group

        .. method:: peek_tx_bandwidth()

            Reads tx_bandwidth in the object.

            :rtype: None or tx_bandwidth

        .. method:: peek_tx_throughput()

            Reads tx_throughput in the object.

            :rtype: None or tx_throughput

        .. method:: peek_tx_percentage()

            Reads tx_percentage in the object.

            :rtype: None or tx_percentage

        .. method:: peek_rx_bandwidth()

            Reads rx_bandwidth in the object.

            :rtype: None or rx_bandwidth

        .. method:: peek_rx_throughput()

            Reads rx_throughput in the object.

            :rtype: None or rx_throughput

        .. method:: peek_rx_percentage()

            Reads rx_percentage in the object.

            :rtype: None or rx_percentage

        .. method:: peek_txrx_bandwidth()

            Reads txrx_bandwidth in the object.

            :rtype: None or txrx_bandwidth

        .. method:: peek_txrx_throughput()

            Reads txrx_throughput in the object.

            :rtype: None or txrx_throughput

        .. method:: peek_txrx_percentage()

            Reads txrx_percentage in the object.

            :rtype: None or txrx_percentage

    """
    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.port_trunk_perf_show,
                         "/rest/running/brocade-fibrechannel-trunk/"
                         "performance",
                         version.VER_RANGE_821_and_ABOVE)
        self.add(pyfos_rest_util.rest_attribute(
            "group", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute(
            "tx-bandwidth", pyfos_type.type_na,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "tx-throughput", pyfos_type.type_na,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "tx-percentage", pyfos_type.type_na,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "rx-bandwidth", pyfos_type.type_na,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "rx-throughput", pyfos_type.type_na,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "rx-percentage", pyfos_type.type_na,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "txrx-bandwidth", pyfos_type.type_na,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "txrx-throughput", pyfos_type.type_na,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "txrx-percentage", pyfos_type.type_na,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.load(dictvalues, 1)


class trunk_area(pyfos_rest_util.rest_object):
    """
    Class for porttrunkarea which shows/configures porttrunkarea(F-port trunk).

    Important class members:

        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | Attribute name                    | Description                   |Frequently used methods                                |
        +===================================+===============================+=======================================================+
        | trunk-index                       | trunk-index for porttrunkarea |:func:`peek_trunk_index`                               |
        |                                   |                               |:func:`set_trunk_index`                                |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | trunk-members/trunk_member        | trunk-membes of the Trunk     |:func:`peek_trunk_members_trunk_member`                |
        |                                   |                               |:func:`set_trunk_members_trunk_member`                 |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | master-port                       | master port  of the Trunk     |:func:`peek_master_port`                               |
        |                                   |                               |                                                       |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | trunk-active			    | Trunk-active or not	    |:func:`peek_trunk_active`                              |
        |                                   |                               |                                                       |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+

    *Object methods*

        .. method:: get()

            Return :class:`trunk_area`
            object with values for all the attributes.
            The object can be printed using :func:`pyfos_utils.response_print`

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary of error or
                :class:`trunk_area` object
        .. method:: post()

            Create an entry. Fields involved are set within the object using
            attribute's set method.  This command is used to create
            a new F-port trunk group or add ports to the existing trunk-group.

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary of error or success response

        .. method:: delete()

            Delete an entry or entry members. Fields involved are
            set within the object using attribute's
            set method. This command is used to delete a trunk-group
            or delete the existing members
            of trunk-group. If all trunk-ports are specified then
            whole trunk-group is deleted.

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary of error or success response

    *Attribute methods*

        .. method:: set_trunk_index(trunk_index)

            Sets trunk_index in the object

            :param trunk_index
            :rtype: dictionary of error or success response

        .. method:: peek_trunk_index()

            Reads trunk_index in the object.

            :rtype: None or trunk_index

        .. method:: set_trunk_members_trunk_member(trunk_members)

            Sets trunk_members_trunk_member in the object

            :param trunk_members
            :rtype: dictionary of error or success response

        .. method:: peek_trunk_members_trunk_member()

            Reads trunk_members in the object.

            :rtype: None or trunk_members_trunk_member

        .. method:: peek_master_port()

            Reads master_port in the object.

            :rtype: None or master_port

        .. method:: peek_trunk_active()

            Reads trunk_active in the object.

            :rtype: None or trunk_active
    """
    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.port_trunk_area,
                         "/rest/running/brocade-fibrechannel-trunk/trunk-area",
                         version.VER_RANGE_821_and_ABOVE)
        self.add(pyfos_rest_util.rest_attribute(
            "trunk-index", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute(
            "trunk-members", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute(
            "trunk-member", pyfos_type.type_str,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST),
            ["trunk-members"])
        self.add(pyfos_rest_util.rest_attribute(
            "master-port", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "trunk-active", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.load(dictvalues, 1)
