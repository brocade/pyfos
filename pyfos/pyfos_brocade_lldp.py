#!/usr/bin/env python3


# Copyright © 2019 Broadcom. All rights reserved.
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


# pyfos_brocade_lldp.py(pyGen v1.0.0)


"""

:mod:`pyfos_brocade_lldp` - PyFOS module Proprietary Link Level Discovery\
Protocol (LLDP) entry container. This container contains LLDP configuration,\
operational state and statistics.
******************************************************************************\
******************************************************************************\
*******************************************************************************
The :mod:`pyfos_brocade_lldp` The PyFOS module support Proprietary Link Level\
Discovery Protocol (LLDP) entry container. This container contains LLDP\
configuration, operational state and statistics.
"""


# Start module imports
from pyfos import pyfos_rest_util
from pyfos.pyfos_type import pyfos_type
from pyfos import pyfos_version as version
# End module imports


class lldp_neighbor(pyfos_rest_util.rest_object):

    """Class of lldp_neighbor

    *Description lldp_neighbor*

        The list of LLDP neighbor devices connected to the switch.

    Important class members of lldp_neighbor:

        +---------------------------+-------------------------------+--------------------------------------------------+
        | Attribute Name            | Description                   |  Frequently Used Methods                         |
        +===========================+===============================+==================================================+
        | remaining-life            | The remaining life of the     | :func:`set_remaining_life`                       |
        |                           | LLDP neighbor.                | :func:`peek_remaining_life`                      |
        +---------------------------+-------------------------------+--------------------------------------------------+
        | system-name               | The system name of the LLDP   | :func:`set_system_name`                          |
        |                           | neighbor.                     | :func:`peek_system_name`                         |
        +---------------------------+-------------------------------+--------------------------------------------------+
        | chassis-id                | The chassis ID of the LLDP    | :func:`set_chassis_id`                           |
        |                           | neighbor.                     | :func:`peek_chassis_id`                          |
        +---------------------------+-------------------------------+--------------------------------------------------+
        | slot-port                 | The local interface name.     | :func:`set_slot_port`                            |
        |                           |                               | :func:`peek_slot_port`                           |
        +---------------------------+-------------------------------+--------------------------------------------------+
        | remote-interface-name     | The remote interface name     | :func:`set_remote_interface_name`                |
        |                           | of the LLDP neighbor device   | :func:`peek_remote_interface_name`               |
        |                           | connected to local switch     |                                                  |
        |                           | ethernet interface.           |                                                  |
        +---------------------------+-------------------------------+--------------------------------------------------+
        | dead-interval             | The dead interval of the      | :func:`set_dead_interval`                        |
        |                           | the LLDP neighbor.            | :func:`peek_dead_interval`                       |
        +---------------------------+-------------------------------+--------------------------------------------------+

    *Object functions for lldp_neighbor*

    .. function:: get()

        Get the instances of class "lldp_neighbor from switch. The object can
         be printed using :func:`pyfos_utils.response_print`.

        :param session: The session handler returned by
         :func:`pyfos_auth.login`.

        :rtype: A dictionary of errors or a success response.


    *Class functions for lldp_neighbor*

        .. function:: peek_remaining_life()

            Reads the value assigned to remaining-life in the object.

            :rtype: None on error and a value on success.


        .. function:: set_remaining_life(value)

            Set the value of remaining-life in the object.

            :rtype: A dictionary of error or a success response and a value
             with "remaining-life" as the key


        .. function:: peek_system_name()

            Reads the value assigned to system-name in the object.

            :rtype: None on error and a value on success.


        .. function:: set_system_name(value)

            Set the value of system-name in the object.

            :rtype: A dictionary of error or a success response and a value
             with "system-name" as the key


        .. function:: peek_chassis_id()

            Reads the value assigned to chassis-id in the object.

            :rtype: None on error and a value on success.


        .. function:: set_chassis_id(value)

            Set the value of chassis-id in the object.

            :rtype: A dictionary of error or a success response and a value
             with "chassis-id" as the key


        .. function:: peek_slot_port()

            Reads the value assigned to slot-port in the object.

            :rtype: None on error and a value on success.


        .. function:: set_slot_port(value)

            Set the value of slot-port in the object.

            :rtype: A dictionary of error or a success response and a value
             with "slot-port" as the key


        .. function:: peek_remote_interface_name()

            Reads the value assigned to remote-interface-name in the object.

            :rtype: None on error and a value on success.


        .. function:: set_remote_interface_name(value)

            Set the value of remote-interface-name in the object.

            :rtype: A dictionary of error or a success response and a value
             with "remote-interface-name" as the key


        .. function:: peek_dead_interval()

            Reads the value assigned to dead-interval in the object.

            :rtype: None on error and a value on success.


        .. function:: set_dead_interval(value)

            Set the value of dead-interval in the object.

            :rtype: A dictionary of error or a success response and a value
             with "dead-interval" as the key


    """

    def __init__(self, dictvalues=None):

        clsuri = "/rest" + "/running" + "/brocade-lldp" + "/lldp-neighbor"
        clstype = pyfos_rest_util.rest_obj_type.lldp_neighbor
        clsver = version.VER_RANGE_900_and_ABOVE
        super().__init__(clstype, clsuri, clsver)

        self.add(pyfos_rest_util.rest_attribute("slot-port",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute("remaining-life",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("system-name",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("chassis-id",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("remote-interface-name",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("dead-interval",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.load(dictvalues, 1)


class lldp_global(pyfos_rest_util.rest_object):

    """Class of lldp_global

    *Description lldp_global*

        The LLDP switch level configuration and operational parameters.

    Important class members of lldp_global:

        +--------------------------+---------------------------------+-------------------------------------------------+
        | Attribute Name           | Description                     |  Frequently Used Methods                        |
        +==========================+=================================+=================================================+
        | tx-interval              | The LLDP Tx interval of the     | :func:`set_tx_interval`                         |
        |                          | switch. Default value is 30     | :func:`peek_tx_interval`                        |
        |                          | seconds                         |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | system-description       | The LLDP system description     | :func:`set_system_description`                  |
        |                          | of the switch.                  | :func:`peek_system_description`                 |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | multiplier               | The LLDP timeout multiplier     | :func:`set_multiplier`                          |
        |                          | value. Default value is 4       | :func:`peek_multiplier`                         |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | system-name              | The LLDP system name of the     | :func:`set_system_name`                         |
        |                          | switch.                         | :func:`peek_system_name`                        |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | tlv                      | The list of optional TLVs       | :func:`set_optional_tlvs_tlv`                   |
        |                          | enabled on the switch. The      | :func:`peek_optional_tlvs_tlv`                  |
        |                          | dcbx, fcoe-app, fcoe-lls,       |                                                 |
        |                          | sys-name and port-desc TLVs     |                                                 |
        |                          | are enabled by default and      |                                                 |
        |                          | user can disable them if        |                                                 |
        |                          | required. The dcbx TLV should   |                                                 |
        |                          | be enabled beforehand to        |                                                 |
        |                          | enable fcoe-app and fcoe-lls    |                                                 |
        |                          | TLVs.                           |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | enabled-state            | The LLDP protocol state of      | :func:`set_enabled_state`                       |
        |                          | the switch. The possible        | :func:`peek_enabled_state`                      |
        |                          | values are: true : LLDP is      |                                                 |
        |                          | enabled on the switch false :   |                                                 |
        |                          | LLDP is disabled on the         |                                                 |
        |                          | switch Default value is true.   |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | tlv                      | The list of mandatory LLDP      | :func:`set_mandatory_tlvs_tlv`                  |
        |                          | TLVs (chassis-id, port-id and   | :func:`peek_mandatory_tlvs_tlv`                 |
        |                          | time-to-live) which cannot be   |                                                 |
        |                          | modified.                       |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+

    *Object functions for lldp_global*

    .. function:: get()

        Get the instances of class "lldp_global from switch. The object can be
         printed using :func:`pyfos_utils.response_print`.

        :param session: The session handler returned by
         :func:`pyfos_auth.login`.

        :rtype: A dictionary of errors or a success response.


    *Class functions for lldp_global*

        .. function:: peek_tx_interval()

            Reads the value assigned to tx-interval in the object.

            :rtype: None on error and a value on success.


        .. function:: set_tx_interval(value)

            Set the value of tx-interval in the object.

            :rtype: A dictionary of error or a success response and a value
             with "tx-interval" as the key


        .. function:: peek_system_description()

            Reads the value assigned to system-description in the object.

            :rtype: None on error and a value on success.


        .. function:: set_system_description(value)

            Set the value of system-description in the object.

            :rtype: A dictionary of error or a success response and a value
             with "system-description" as the key


        .. function:: peek_multiplier()

            Reads the value assigned to multiplier in the object.

            :rtype: None on error and a value on success.


        .. function:: set_multiplier(value)

            Set the value of multiplier in the object.

            :rtype: A dictionary of error or a success response and a value
             with "multiplier" as the key


        .. function:: peek_system_name()

            Reads the value assigned to system-name in the object.

            :rtype: None on error and a value on success.


        .. function:: set_system_name(value)

            Set the value of system-name in the object.

            :rtype: A dictionary of error or a success response and a value
             with "system-name" as the key


        .. function:: peek_optional_tlvs_tlv()

            Reads the value assigned to tlv in the object.

            :rtype: None on error and a value on success.


        .. function:: set_optional_tlvs_tlv(value)

            Set the value of tlv in the object.

            :rtype: A dictionary of error or a success response and a value
             with "tlv" as the key


        .. function:: peek_enabled_state()

            Reads the value assigned to enabled-state in the object.

            :rtype: None on error and a value on success.


        .. function:: set_enabled_state(value)

            Set the value of enabled-state in the object.

            :rtype: A dictionary of error or a success response and a value
             with "enabled-state" as the key


        .. function:: peek_mandatory_tlvs_tlv()

            Reads the value assigned to tlv in the object.

            :rtype: None on error and a value on success.


        .. function:: set_mandatory_tlvs_tlv(value)

            Set the value of tlv in the object.

            :rtype: A dictionary of error or a success response and a value
             with "tlv" as the key


    """

    def __init__(self, dictvalues=None):

        clsuri = "/rest" + "/running" + "/brocade-lldp" + "/lldp-global"
        clstype = pyfos_rest_util.rest_obj_type.lldp_global
        clsver = version.VER_RANGE_900_and_ABOVE
        super().__init__(clstype, clsuri, clsver)

        self.add(pyfos_rest_util.rest_attribute("tx-interval",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("system-description",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("multiplier",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("system-name",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("enabled-state",
                 pyfos_type.type_bool, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("mandatory-tlvs",
                 pyfos_type.type_na, dict(),
                 pyfos_rest_util.REST_ATTRIBUTE_CONTAINER_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("optional-tlvs",
                 pyfos_type.type_na, dict(),
                 pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute("tlv", pyfos_type.type_na,
                 None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST),
                 ['optional-tlvs'])
        self.add(pyfos_rest_util.rest_attribute("tlv", pyfos_type.type_na,
                 None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST),
                 ['mandatory-tlvs'])
        self.load(dictvalues, 1)


class lldp_profile(pyfos_rest_util.rest_object):

    """Class of lldp_profile

    *Description lldp_profile*

        The LLDP profile.

    Important class members of lldp_profile:

        +--------------------------+---------------------------------+-------------------------------------------------+
        | Attribute Name           | Description                     |  Frequently Used Methods                        |
        +==========================+=================================+=================================================+
        | tx-interval              | The Transmit interval value     | :func:`set_tx_interval`                         |
        |                          | of the LLDP profile.            | :func:`peek_tx_interval`                        |
        |                          | Tx-interval value -1            |                                                 |
        |                          | indicates that it will be       |                                                 |
        |                          | derived from lldp global        |                                                 |
        |                          | tx-interval value.              |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | name                     | The LLDP profile name.          | :func:`set_name`                                |
        |                          |                                 | :func:`peek_name`                               |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | multiplier               | The LLDP timeout multiplier     | :func:`set_multiplier`                          |
        |                          | value of the LLDP profile.      | :func:`peek_multiplier`                         |
        |                          | Multiplier value -1 indicates   |                                                 |
        |                          | that it will be derived from    |                                                 |
        |                          | lldp global multiplier value.   |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | tlv                      | List of enabled TLVs for the    | :func:`set_enabled_tlvs_tlv`                    |
        |                          | LLDP profile. Empty             | :func:`peek_enabled_tlvs_tlv`                   |
        |                          | enabled-tlvs indicates that     |                                                 |
        |                          | the tlvs will be derived from   |                                                 |
        |                          | lldp global optional-tlvs.      |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+

    *Object functions for lldp_profile*

    .. function:: get()

        Get the instances of class "lldp_profile from switch. The object can
         be printed using :func:`pyfos_utils.response_print`.

        :param session: The session handler returned by
         :func:`pyfos_auth.login`.

        :rtype: A dictionary of errors or a success response.


    *Class functions for lldp_profile*

        .. function:: peek_tx_interval()

            Reads the value assigned to tx-interval in the object.

            :rtype: None on error and a value on success.


        .. function:: set_tx_interval(value)

            Set the value of tx-interval in the object.

            :rtype: A dictionary of error or a success response and a value
             with "tx-interval" as the key


        .. function:: peek_name()

            Reads the value assigned to name in the object.

            :rtype: None on error and a value on success.


        .. function:: set_name(value)

            Set the value of name in the object.

            :rtype: A dictionary of error or a success response and a value
             with "name" as the key


        .. function:: peek_multiplier()

            Reads the value assigned to multiplier in the object.

            :rtype: None on error and a value on success.


        .. function:: set_multiplier(value)

            Set the value of multiplier in the object.

            :rtype: A dictionary of error or a success response and a value
             with "multiplier" as the key


        .. function:: peek_enabled_tlvs_tlv()

            Reads the value assigned to tlv in the object.

            :rtype: None on error and a value on success.


        .. function:: set_enabled_tlvs_tlv(value)

            Set the value of tlv in the object.

            :rtype: A dictionary of error or a success response and a value
             with "tlv" as the key


    """

    def __init__(self, dictvalues=None):

        clsuri = "/rest" + "/running" + "/brocade-lldp" + "/lldp-profile"
        clstype = pyfos_rest_util.rest_obj_type.lldp_profile
        clsver = version.VER_RANGE_900_and_ABOVE
        super().__init__(clstype, clsuri, clsver)

        self.add(pyfos_rest_util.rest_attribute("name", pyfos_type.type_str,
                 None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute("tx-interval",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("multiplier",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("enabled-tlvs",
                 pyfos_type.type_na, dict(),
                 pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute("tlv", pyfos_type.type_na,
                 None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST),
                 ['enabled-tlvs'])
        self.load(dictvalues, 1)


class lldp_statistics(pyfos_rest_util.rest_object):

    """Class of lldp_statistics

    *Description lldp_statistics*

        The LLDP protocol specific Tx, Rx and Error statistics of the port/s.

    Important class members of lldp_statistics:

        +--------------------------+---------------------------------+-------------------------------------------------+
        | Attribute Name           | Description                     |  Frequently Used Methods                        |
        +==========================+=================================+=================================================+
        | frames-discarded         | The number of LLDP discarded    | :func:`set_frames_discarded`                    |
        |                          | frames.                         | :func:`peek_frames_discarded`                   |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | tlv-unrecognized         | The number of unrecognized      | :func:`set_tlv_unrecognized`                    |
        |                          | LLDP TLVs.                      | :func:`peek_tlv_unrecognized`                   |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | slot-port                | Port name.                      | :func:`set_slot_port`                           |
        |                          |                                 | :func:`peek_slot_port`                          |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | error-frames             | The number of LLDP error        | :func:`set_error_frames`                        |
        |                          | frames                          | :func:`peek_error_frames`                       |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | out-frames               | The number of LLDP out          | :func:`set_out_frames`                          |
        |                          | frames.                         | :func:`peek_out_frames`                         |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | tlv-discarded            | The number of discarded LLDP    | :func:`set_tlv_discarded`                       |
        |                          | TLVs.                           | :func:`peek_tlv_discarded`                      |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | in-frames                | The number of LLDP In frames.   | :func:`set_in_frames`                           |
        |                          |                                 | :func:`peek_in_frames`                          |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | frames-aged-out          | The number of LLDP aged out     | :func:`set_frames_aged_out`                     |
        |                          | frames.                         | :func:`peek_frames_aged_out`                    |
        +--------------------------+---------------------------------+-------------------------------------------------+

    *Object functions for lldp_statistics*

    .. function:: get()

        Get the instances of class "lldp_statistics from switch. The object
         can be printed using :func:`pyfos_utils.response_print`.

        :param session: The session handler returned by
         :func:`pyfos_auth.login`.

        :rtype: A dictionary of errors or a success response.


    *Class functions for lldp_statistics*

        .. function:: peek_frames_discarded()

            Reads the value assigned to frames-discarded in the object.

            :rtype: None on error and a value on success.


        .. function:: set_frames_discarded(value)

            Set the value of frames-discarded in the object.

            :rtype: A dictionary of error or a success response and a value
             with "frames-discarded" as the key


        .. function:: peek_tlv_unrecognized()

            Reads the value assigned to tlv-unrecognized in the object.

            :rtype: None on error and a value on success.


        .. function:: set_tlv_unrecognized(value)

            Set the value of tlv-unrecognized in the object.

            :rtype: A dictionary of error or a success response and a value
             with "tlv-unrecognized" as the key


        .. function:: peek_slot_port()

            Reads the value assigned to slot-port in the object.

            :rtype: None on error and a value on success.


        .. function:: set_slot_port(value)

            Set the value of slot-port in the object.

            :rtype: A dictionary of error or a success response and a value
             with "slot-port" as the key


        .. function:: peek_error_frames()

            Reads the value assigned to error-frames in the object.

            :rtype: None on error and a value on success.


        .. function:: set_error_frames(value)

            Set the value of error-frames in the object.

            :rtype: A dictionary of error or a success response and a value
             with "error-frames" as the key


        .. function:: peek_out_frames()

            Reads the value assigned to out-frames in the object.

            :rtype: None on error and a value on success.


        .. function:: set_out_frames(value)

            Set the value of out-frames in the object.

            :rtype: A dictionary of error or a success response and a value
             with "out-frames" as the key


        .. function:: peek_tlv_discarded()

            Reads the value assigned to tlv-discarded in the object.

            :rtype: None on error and a value on success.


        .. function:: set_tlv_discarded(value)

            Set the value of tlv-discarded in the object.

            :rtype: A dictionary of error or a success response and a value
             with "tlv-discarded" as the key


        .. function:: peek_in_frames()

            Reads the value assigned to in-frames in the object.

            :rtype: None on error and a value on success.


        .. function:: set_in_frames(value)

            Set the value of in-frames in the object.

            :rtype: A dictionary of error or a success response and a value
             with "in-frames" as the key


        .. function:: peek_frames_aged_out()

            Reads the value assigned to frames-aged-out in the object.

            :rtype: None on error and a value on success.


        .. function:: set_frames_aged_out(value)

            Set the value of frames-aged-out in the object.

            :rtype: A dictionary of error or a success response and a value
             with "frames-aged-out" as the key


    """

    def __init__(self, dictvalues=None):

        clsuri = "/rest" + "/running" + "/brocade-lldp" + "/lldp-statistics"
        clstype = pyfos_rest_util.rest_obj_type.lldp_statistics
        clsver = version.VER_RANGE_900_and_ABOVE
        super().__init__(clstype, clsuri, clsver)

        self.add(pyfos_rest_util.rest_attribute("slot-port",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute("frames-discarded",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("tlv-unrecognized",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("error-frames",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("out-frames",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("tlv-discarded",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("in-frames",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("frames-aged-out",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.load(dictvalues, 1)
