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

:mod:`pyfos_brocade_gigabitethernet` - PyFOS module for GigE port objects.
*******************************************************************************
The :mod:`pyfos_brocade_gigabitethernet` provides REST support for GigE objects.
"""
import pyfos.pyfos_rest_util as pyfos_rest_util
from pyfos.pyfos_type import pyfos_type


class gigabitethernet(pyfos_rest_util.rest_object):
        """
        Important class members:

                +-------------------------------+-------------------------------+---------------------------------------+
                | Attribute name                | Description                   |Frequently used functions              |
                +===============================+===============================+=======================================+
                | name                          | The slot/port name of GE port |:func:`peek_name`                      |
                +-------------------------------+-------------------------------+---------------------------------------+
                | name                          | The slot/port name of GE port |:func:`set_name`                       |
                +-------------------------------+-------------------------------+---------------------------------------+
                | enabled-state                 | The state of the GiGE port    |:func:`peek_enabled_state`             |
                +-------------------------------+-------------------------------+---------------------------------------+
                | enabled-state                 | The state of the GiGE port    |:func:`set_enabled_state`              |
                +-------------------------------+-------------------------------+---------------------------------------+
                | speed                         | The speed of GiGE port        |:func:`peek_speed`                     |
                +-------------------------------+-------------------------------+---------------------------------------+
                | speed                         | The speed of GiGE port        |:func:`set_speed`                      |
                +-------------------------------+-------------------------------+---------------------------------------+
                | mac-address                   | The mac-address of GiGE port  |:func:`peek_mac_address`               |
                +-------------------------------+-------------------------------+---------------------------------------+
                | operational-status            | GiGE port operational-status  |:func:`peek_operational_status`        |
                +-------------------------------+-------------------------------+---------------------------------------+
                | persistent-disable            | GiGE port persistent disabled |:func:`peek_persistent_disable`        |
                +-------------------------------+-------------------------------+---------------------------------------+
                | persistent-disable            | GiGE port persistent disabled |:func:`set_persistent_disable`         |
                +-------------------------------+-------------------------------+---------------------------------------+


            *Attribute functions*

                .. function:: peek_name()

                    Reads name from the GiGE port object.

                    :rtype: None on error and value on success

                .. function:: peek_enabled_state()

                    Reads enabled state from GiGE port object.

                    :rtype: None on error and value on success

                .. function:: peek_speed()

                    Reads the speed from the GiGE port Object.

                    :rtype: None on error and value on success

                .. function:: peek_mac_address()

                    Reads the mac address from the GiGE port object.

                    :rtype: None on error and value on success

                .. function:: peek_operational_status()

                    Reads operational status from the GiGE port object.

                    :rtype: None on error and value on success

                .. function:: peek_persistent_disable()

                    Reads persistent disable state from the GiGE port object.

                    :rtype: None on error and value on success

                .. function:: set_name(name)

                    Set the name in the GiGE port object.

                    :rtype: dictionary of error or success response\
                    and value with "name" as key

                .. function:: set_enabled_state(enabled)

                    Set the enabled state in the GiGE port object.

                    :rtype: dictionary of error or success response\
                     and value with "ip-address" as key

                .. function:: set_speed(speed)

                    Set the Speed in the GiGE port object.

                    :rtype: dictionary of error or success response\
                     and value with "dp-id" as key

                .. function:: set_persistent_disable(disabled)

                    Set the persistent disabled in the GiGE port object..

                    :rtype: dictionary of error or success response and
                     value with "ip-prefix-length" as key

        """
        def __init__(self, dictvalues={}):
            super().__init__(pyfos_rest_util.rest_obj_type.gige,
                             "/rest/running/brocade-interface/"
                             "gigabitethernet")
            self.add(pyfos_rest_util.rest_attribute("name",
                     pyfos_type.type_str, None,
                     pyfos_rest_util.REST_ATTRIBUTE_KEY))
            self.add(pyfos_rest_util.rest_attribute("enabled-state",
                     pyfos_type.type_str, None,
                     pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
            self.add(pyfos_rest_util.rest_attribute("speed",
                     pyfos_type.type_str, None,
                     pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
            self.add(pyfos_rest_util.rest_attribute("mac-address",
                     pyfos_type.type_str, None,
                     pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
            self.add(pyfos_rest_util.rest_attribute("operational-status",
                     pyfos_type.type_str, None,
                     pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
            self.add(pyfos_rest_util.rest_attribute("persistent-disable",
                     pyfos_type.type_str, None,
                     pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
            self.load(dictvalues, 1)


class gigabitethernet_statistics(pyfos_rest_util.rest_object):
        """
           Important class members:

                +-------------------------------+-------------------------------+---------------------------------------+
                | Attribute name                | Description                   |Frequently used functions              |
                +===============================+===============================+=======================================+
                | name                          | The slot/port name of GE port |:func:`peek_name`                      |
                +-------------------------------+-------------------------------+---------------------------------------+
                | name                          | The slot/port name of GE port |:func:`set_name`                       |
                +-------------------------------+-------------------------------+---------------------------------------+
                | reset-statistics              | Reset the GigE statistic      |:func:`peek_reset_statistics`          |
                +-------------------------------+-------------------------------+---------------------------------------+
                | reset-statistics              | Reset the GigE statistic      |:func:`set_reset_statistics`           |
                +-------------------------------+-------------------------------+---------------------------------------+
                | out-pkts                      | The total out packets         |:func:`peek_out_pkts`                  |
                +-------------------------------+-------------------------------+---------------------------------------+
                | out-octets                    | The total out octets          |:func:`peek_out_octets`                |
                +-------------------------------+-------------------------------+---------------------------------------+
                | out-unicast-pkts              | The total out unicast pkts    |:func:`peek_out_unicast_pkts`          |
                +-------------------------------+-------------------------------+---------------------------------------+
                | out-multicast-pkts            | The total out multicast pkts  |:func:`peek_out_multicast_pkts`        |
                +-------------------------------+-------------------------------+---------------------------------------+
                | out-broadcast-pkts            | The total out broadcast pkts  |:func:`peek_out_broadcast_pkts`        |
                +-------------------------------+-------------------------------+---------------------------------------+
                | out-vlan-pkts                 | The total out vlan pkts       |:func:`peek_out_vlan_pkts`             |
                +-------------------------------+-------------------------------+---------------------------------------+
                | out-pause-pkts                | The total out pause pkts      |:func:`peek_out_pause_pkts`            |
                +-------------------------------+-------------------------------+---------------------------------------+
                | in-pkts                       | The total in packets          |:func:`peek_in_pkts`                   |
                +-------------------------------+-------------------------------+---------------------------------------+
                | in-octets                     | The total in octets           |:func:`peek_in_octets`                 |
                +-------------------------------+-------------------------------+---------------------------------------+
                | in-unicast-pkts               | The total in unicast pkts     |:func:`peek_in_unicast_pkts`           |
                +-------------------------------+-------------------------------+---------------------------------------+
                | in-multicast-pkts             | The total in multicast pkts   |:func:`peek_in_multicast_pkts`         |
                +-------------------------------+-------------------------------+---------------------------------------+
                | in-broadcast-pkts             | The total in broadcast pkts   |:func:`peek_in_broadcast_pkts`         |
                +-------------------------------+-------------------------------+---------------------------------------+
                | in-vlan-pkts                  | The total in vlan pkts        |:func:`peek_in_vlan_pkts`              |
                +-------------------------------+-------------------------------+---------------------------------------+
                | in-pause-pkts                 | The total in pause pkts       |:func:`peek_in_pause_pkts`             |
                +-------------------------------+-------------------------------+---------------------------------------+
                | carrier-loss-error            | The total carrier loss err    |:func:`peek_carrier_loss_error`        |
                +-------------------------------+-------------------------------+---------------------------------------+
                | crc-error                     | The total crc err             |:func:`peek_crc_error`                 |
                +-------------------------------+-------------------------------+---------------------------------------+
                | jabber-error                  | The total jabber err          |:func:`peek_jabber_error`              |
                +-------------------------------+-------------------------------+---------------------------------------+
                | time-generated                | The time stats were generated |:func:`peek_time_generated`            |
                +-------------------------------+-------------------------------+---------------------------------------+


            *Attribute functions*

                .. function:: peek_name()

                    Reads name from the GiGE port stats object.

                    :rtype: None on error and value on success

                .. function:: peek_reset_statistics()

                    Reads reset statistics state from GiGE port stats object.

                    :rtype: None on error and value on success

                .. function:: peek_out_pkts()

                    Reads the outgoing packets from the GiGE port stats object.

                    :rtype: None on error and value on success

                .. function:: peek_out_octets()

                    Reads the outgoing octets from the GiGE port stats object.

                    :rtype: None on error and value on success

                .. function:: peek_out_unicast_pkts()

                    Reads outgoing unicast packets from the GiGE port
                    stats object.

                    :rtype: None on error and value on success

                .. function:: peek_out_multicast_pkts()

                    Reads outgoing multicast packets from the GiGE
                    port stats object.

                    :rtype: None on error and value on success

                .. function:: peek_out_broadcast_pkts()

                    Reads outgoing broadcast packets from
                    GiGE port stats object.

                    :rtype: None on error and value on success

                .. function:: peek_out_vlan_pkts()

                    Reads the outgoing vlan packets from the
                    GiGE port stats object

                    :rtype: None on error and value on success

                .. function:: peek_out_pause_pkts()

                    Reads the outgoing pause packets from the
                    GiGE port stats object.

                    :rtype: None on error and value on success

                .. function:: peek_in_pkts()

                    Reads the incoming packets from the GiGE port
                    stats object

                    :rtype: None on error and value on success

                .. function:: peek_in_octets()

                    Reads the incoming octets from the GiGE port
                    stats object.

                    :rtype: None on error and value on success

                .. function:: peek_in_unicast_pkts()

                    Reads incoming unicast packets from the GiGE port
                    stats object.

                    :rtype: None on error and value on success

                .. function:: peek_in_multicast_pkts()

                    Reads incoming multicast packets from the GiGE port
                    stats object.

                    :rtype: None on error and value on success

                .. function:: peek_in_broadcast_pkts()

                    Reads incoming broadcast packets from GiGE port
                    stats object.

                    :rtype: None on error and value on success

                .. function:: peek_in_vlan_pkts()

                    Reads the incomin vlan packets from the GiGE port
                    stats object

                    :rtype: None on error and value on success

                .. function:: peek_in_pause_pkts()

                    Reads the incoming pause packets from the GiGE port
                    stats object.

                    :rtype: None on error and value on success

                .. function:: peek_carrier_loss_error()

                    Reads total carrier loss errors from the GiGE port
                    stats object.

                    :rtype: None on error and value on success

                .. function:: peek_crc_error()

                    Reads total CRC errors from the GiGE port
                    stats object.

                    :rtype: None on error and value on success

                .. function:: peek_jabber_error()

                    Reads total jabber errors from the GiGE port
                    stats object.

                    :rtype: None on error and value on success

                .. function:: peek_time_generated()

                    Reads the generation time of GiGE port
                    stats object.

                    :rtype: None on error and value on success

                .. function:: set_name(name)

                    Set the name in the GiGE port stats object.

                    :rtype: dictionary of error or success response
                     and value with "name" as key

                .. function:: set_reset_statistics(reset)

                    Set the reset statistics in the GiGE port stats object.

                    :rtype: dictionary of error or success response and
                     value with "reset-statistics" as key
        """
        def __init__(self, dictvalues={}):
            super().__init__(pyfos_rest_util.rest_obj_type.gige_stats,
                             "/rest/running/brocade-interface/"
                             "gigabitethernet-statistics")
            self.add(pyfos_rest_util.rest_attribute("name",
                     pyfos_type.type_str, None,
                     pyfos_rest_util.REST_ATTRIBUTE_KEY))
            self.add(pyfos_rest_util.rest_attribute("out-pkts",
                     pyfos_type.type_str, None,
                     pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
            self.add(pyfos_rest_util.rest_attribute("out-octets",
                     pyfos_type.type_str, None,
                     pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
            self.add(pyfos_rest_util.rest_attribute("out-unicast-pkts",
                     pyfos_type.type_str, None,
                     pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
            self.add(pyfos_rest_util.rest_attribute("out-multicast-pkts",
                     pyfos_type.type_str, None,
                     pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
            self.add(pyfos_rest_util.rest_attribute("out-broadcast-pkts",
                     pyfos_type.type_str, None,
                     pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
            self.add(pyfos_rest_util.rest_attribute("out-vlan-pkts",
                     pyfos_type.type_str, None,
                     pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
            self.add(pyfos_rest_util.rest_attribute("out-pause-pkts",
                     pyfos_type.type_str, None,
                     pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
            self.add(pyfos_rest_util.rest_attribute("in-pkts",
                     pyfos_type.type_str, None,
                     pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
            self.add(pyfos_rest_util.rest_attribute("in-octets",
                     pyfos_type.type_str, None,
                     pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
            self.add(pyfos_rest_util.rest_attribute("in-unicast-pkts",
                     pyfos_type.type_str, None,
                     pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
            self.add(pyfos_rest_util.rest_attribute("in-multicast-pkts",
                     pyfos_type.type_str, None,
                     pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
            self.add(pyfos_rest_util.rest_attribute("in-broadcast-pkts",
                     pyfos_type.type_str, None,
                     pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
            self.add(pyfos_rest_util.rest_attribute("in-vlan-pkts",
                     pyfos_type.type_str, None,
                     pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
            self.add(pyfos_rest_util.rest_attribute("in-pause-pkts",
                     pyfos_type.type_str, None,
                     pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
            self.add(pyfos_rest_util.rest_attribute("carrier-loss-error",
                     pyfos_type.type_str, None,
                     pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
            self.add(pyfos_rest_util.rest_attribute("crc-error",
                     pyfos_type.type_str, None,
                     pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
            self.add(pyfos_rest_util.rest_attribute("jabber-error",
                     pyfos_type.type_str, None,
                     pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
            self.add(pyfos_rest_util.rest_attribute("reset-statistics",
                     pyfos_type.type_str, None,
                     pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
            self.add(pyfos_rest_util.rest_attribute("time-generated",
                     pyfos_type.type_str, None,
                     pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
            self.load(dictvalues, 1)
