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

:mod:`pyfos_brocade_zone` - PyFOS module to provide rest \
        support for Zoning.
*********************************************************************************************************
The :mod:`pyfos_brocade_zone` provides a REST support for \
        Zoning.

"""

from pyfos import pyfos_rest_util
from pyfos.pyfos_type import pyfos_type
import pyfos.pyfos_version as version

CFG_ACTION_SAVE = 1
CFG_ACTION_DISABLE = 2
CFG_ACTION_CLEAR = 3
CFG_ACTION_ABORT = 4

CFG = "CFG"
ZONE = "ZONE"
PEER_ZONE = "PEER_ZONE"
ALIAS = "ALIAS"

# These ZONE_TYPE_XXXXX definitions are deprecated beginning in FOS 9.0.0.
# From FOS 9.0.0 and onwards, please use the ZONE_TYPE_STRING_XXXXX definitions.
ZONE_TYPE_DEFAULT = 0
ZONE_TYPE_PEER = 1
ZONE_TYPE_TDZ = 2

# These zone-type-string definitions are newly created in FOS 9.0.0
# and should be used in place of the above ZONE_TYPE_XXXXX definitions.
ZONE_TYPE_STRING_DEFAULT = "zone"
ZONE_TYPE_STRING_PEER = "user-created-peer-zone"
ZONE_TYPE_STRING_TDZ = "target-created-peer-zone"

ZONE_DEFAULT_NO_ACCESS = 'd__efault__Cfg'

DEF_ZONE_NONE = 0
DEF_ZONE_ALL = 1


class defined_configuration(pyfos_rest_util.rest_object):
    """Class of defined zone configuration

    Important class members:

        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | Attribute name                    | Description                   |Frequently used methods                                |
        +===================================+===============================+=======================================================+
        | cfg                               | a list of cfg                 |:func:`set_cfg`                                        |
        |                                   |                               |:func:`peek_cfg`                                       |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | cfg-name                          | name of cfg                   |:func:`set_cfg_cfg_name`                               |
        |                                   |                               |:func:`peek_cfg_cfg_name`                              |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | member_zone/zone-name             | list of zone members in cfg   |:func:`set_cfg_member_zone_zone_name`                  |
        |                                   |                               |:func:`peek_cfg_member_zone_zone_name`                 |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | zone                              | a list of zone                |:func:`set_zone`                                       |
        |                                   |                               |:func:`peek_zone`                                      |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | zone-name                         | name of zone                  |:func:`set_zone_zone_name`                             |
        |                                   |                               |:func:`peek_zone_zone_name`                            |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | zone-type                         | type of zone                  |:func:`set_zone_zone_type`                             |
        |                                   |                               |:func:`peek_zone_zone_type`                            |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | zone-type-string                  | type of zone                  |:func:`set_zone_zone_type_string`                      |
        |                                   |                               |:func:`peek_zone_zone_type_string`                     |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | member-entry/entry-name           | list of device members in zone|:func:`set_zone_member_entry_entry_name`               |
        |                                   |                               |:func:`peek_zone_member_entry_entry_name`              |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | member-entry/principal-entry-name | list of principal device      |:func:`set_zone_member_entry_principal_entry_name`     |
        |                                   | members in zone               |:func:`peek_zone_member_entry_principal_entry_name`    |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | alias                             | a list of alias               |:func:`set_alias`                                      |
        |                                   |                               |:func:`peek_alias`                                     |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | alias-name                        | name of alias                 |:func:`set_alias_alias_name`                           |
        |                                   |                               |:func:`peek_alias_alias_name`                          |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | member-entry/alias-entry-name     | list of entries in alias      |:func:`set_alias_member_entry_alias_entry_name`        |
        |                                   |                               |:func:`peek_alias_member_entry_alias_entry_name`       |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+

    *Object methods*

        .. method:: get()

            Return :class:`defined_configuration`
            object with values for all the attributes.
            The object can be printed using :func:`pyfos_utils.response_print`

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary of error or
                :class:`defined_configuration` object

        .. method:: post()

            Create an entry. Fields involved are set within the object using
            attribute's set method.  This command is used to create
            a new cfg, zone, or alias.

            Example usage of the method to create a new cfg::

                defined_configuration_obj =
                    pyfos_newzone.defined_configuration()
                defined_configuration_obj.set_cfg_cfg_name("newcfg")
                zones = {"zone1", "zone2"}
                defined_configuration_obj.set_cfg_member_zone_zone_name(zones)
                defined_configuration_obj.post(session)

            .. note:: refer to :class:`effective_configuration`
                for saving or enabling the change

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary of error or success response

        .. method:: patch()

            Replace entry members. Fields involved are set
            within the object using
            attribute's set method. This command is used to
            add to the existing members
            of cfg, zone or alias.

            Example usage of the method to add to an existing cfg::

                defined_configuration_obj =
                    pyfos_newzone.defined_configuration()
                defined_configuration_obj.set_cfg_cfg_name("newcfg")
                zones = {"zone3", "zone4"}
                defined_configuration_obj.set_cfg_member_zone_zone_name(zones)
                defined_configuration_obj.patch(session)

            .. note:: refer to :class:`effective_configuration`
                for saving or enabling the change

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary of error or success response

        .. method:: delete()

            Delete an entry or entry members. Fields involved are
            set within the object using attribute's
            set method. This command is used to delete an cfg, zone,
            or alias or delete the existing members
            of cfg, zone or alias.

            Example usage of the method to delete from an existing cfg::

                defined_configuration_obj =
                    pyfos_newzone.defined_configuration()
                defined_configuration_obj.set_cfg_cfg_name("newcfg")
                zones = {"zone3", "zone4"}
                defined_configuration_obj.set_cfg_member_zone_zone_name(zones)
                defined_configuration_obj.delete(session)

            Example usage of the method to delete an existing cfg::

                defined_configuration_obj =
                    pyfos_newzone.defined_configuration()
                defined_configuration_obj.set_cfg_cfg_name("newcfg")
                defined_configuration_obj.set_cfg_member_zone_zone_name(zones)
                defined_configuration_obj.delete(session)

            .. note:: refer to :class:`effective_configuration`
                for saving or enabling the change

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary of error or success response

    *Attribute methods*

        .. method:: set_cfg(cfg)

            Sets cfg in the object

            :param cfg: cfg dictionary of cfg name and list of members
            :rtype: dictionary of error or success response

        .. method:: peek_cfg()

            Reads cfg in the object.

            :rtype: None or cfg

        .. method:: set_cfg_cfg_name(cfg_name)

            Sets cfg_name in the object

            :param cfg_name: name of cfg
            :rtype: dictionary of error or success response

        .. method:: peek_cfg_cfg_name()

            Reads cfg_name in the object.

            :rtype: None or cfg name

        .. method:: set_cfg_member_zone_zone_name(zone_list)

            Sets a list of zone names in cfg in the object

            :param zone_list: list of mbmers zone names
            :rtype: dictionary of error or success response

        .. method:: peek_cfg_member_zone_zone_name()

            Reads a list of zone members in cfg in the object.

            :rtype: None or list of zone members

        .. method:: set_zone(zone)

            Sets zone in the object

            :param zone: zone dictionary of zone name,
                zone type and list of members
            :rtype: dictionary of error or success response

        .. method:: peek_zone()

            Reads zone in the object.

            :rtype: None or zone

        .. method:: set_zone_zone_name(zone_name)

            Sets zone name in the object

            :param zone_name: name of zone
            :rtype: dictionary of error or success response

        .. method:: peek_zone_zone_name()

            Reads zone name in the object.

            :rtype: None or zone name

        .. method:: set_zone_zone_type(zone_type)

            Sets zone type to default or peer zone in the object.
            A zone type of 0 indicates a normal zone while a zone
            type of 1 indicates a peer zone.

            :param zone_type: zone type
            :rtype: dictionary of error or success response

        .. method:: peek_zone_zone_type()

            Reads the zone type in the object.

            :rtype: None or zone type

        .. method:: set_zone_zone_type_string(zone_type_string)

            Sets the zone type string to default or peer zone in the object.
            A zone type string of 'zone' indicates a zone that is not a peer zone.
            A zone type string of 'user-created-peer-zone' indicates a peer zone.

            :param zone_type_string: zone type string
            :rtype: dictionary of error or success response

        .. method:: peek_zone_zone_type_string()

            Reads the zone type string in the object.

            :rtype: None or zone type string

        .. method:: set_zone_member_entry_entry_name(entry_list)

            Sets a list of device entries in zone in the object

            :param entry_list: list of member devices
            :rtype: dictionary of error or success response

        .. method:: peek_zone_member_entry_entry_name()

            Reads a list of device members in zone in the object.

            :rtype: None or list of device members

        .. method:: set_zone_member_entry_principal_entry_name(entry_list)

            Sets a list of principal device entries in zone in the object

            :param entry_list: list of member devices
            :rtype: dictionary of error or success response

        .. method:: peek_zone_member_entry_principal_entry_name()

            Reads a list of principal device members in zone in the object.

            :rtype: None or list of device members

        .. method:: set_alias(alias)

            Sets alias in the object

            :param alias: alias dictionary of alias name and list of members
            :rtype: dictionary of error or success response

        .. method:: peek_alias()

            Reads alias in the object.

            :rtype: None or alias

        .. method:: set_alias_alias_name(alias_name)

            Sets alias name in the object

            :param alias_name: name of alias
            :rtype: dictionary of error or success response

        .. method:: peek_alias_alias_name()

            Reads alias name in the object.

            :rtype: None or alias name

        .. method:: set_alias_member_entry_alias_entry_name(entry_list)

            Sets a list of alias members in zone in the object

            :param entry_list: list of alias members
            :rtype: dictionary of error or success response

        .. method:: peek_alias_member_entry_alias_entry_name()

            Reads a list of alias members in cfg in the object.

            :rtype: None or list of alias members

        """

    def __init__(self, dictvalues={}):
        urilist = list([dict({'URIVER': version.VER_RANGE_820_TO_821A,
                              'URI': "/rest/running/zoning/" +
                              "defined-configuration"}),
                        dict({'URIVER': version.VER_RANGE_821b_and_ABOVE,
                              'URI': "/rest/running/brocade-zone/" +
                              "defined-configuration"})])
        super().__init__(pyfos_rest_util.rest_obj_type.zone_defined, urilist)

        self.add(pyfos_rest_util.rest_attribute(
            "cfg", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER_LIST))
        self.add(pyfos_rest_util.rest_attribute(
            "cfg-name", pyfos_type.type_zoning_name,
            None, pyfos_rest_util.REST_ATTRIBUTE_KEY), ["cfg"])
        self.add(pyfos_rest_util.rest_attribute(
            "member-zone", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER), ["cfg"])
        self.add(pyfos_rest_util.rest_attribute(
            "zone-name", pyfos_type.type_zoning_name,
            None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST),
            ["cfg", "member-zone"])
        self.add(pyfos_rest_util.rest_attribute(
            "zone", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER_LIST))
        self.add(pyfos_rest_util.rest_attribute(
            "zone-name", pyfos_type.type_zoning_name,
            None, pyfos_rest_util.REST_ATTRIBUTE_KEY), ["zone"])
        self.add(pyfos_rest_util.rest_attribute(
            "zone-type", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG,
            version.VER_RANGE_820_TO_900), ["zone"])
        self.add(pyfos_rest_util.rest_attribute(
            "zone-type-string", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG,
            version.VER_RANGE_900_and_ABOVE), ["zone"])
        self.add(pyfos_rest_util.rest_attribute(
            "member-entry", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER), ["zone"])
        self.add(pyfos_rest_util.rest_attribute(
            "entry-name",
            [pyfos_type.type_zoning_name, pyfos_type.type_wwn,
                pyfos_type.type_domain_port],
            None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST),
            ["zone", "member-entry"])
        self.add(pyfos_rest_util.rest_attribute(
            "principal-entry-name",
            [pyfos_type.type_zoning_name, pyfos_type.type_wwn,
                pyfos_type.type_domain_port],
            None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST),
            ["zone", "member-entry"])
        self.add(pyfos_rest_util.rest_attribute(
            "alias", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER_LIST))
        self.add(pyfos_rest_util.rest_attribute(
            "alias-name", pyfos_type.type_zoning_name,
            None, pyfos_rest_util.REST_ATTRIBUTE_KEY), ["alias"])
        self.add(pyfos_rest_util.rest_attribute(
            "member-entry", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER),
            ["alias"])
        self.add(pyfos_rest_util.rest_attribute(
            "alias-entry-name",
            [pyfos_type.type_wwn, pyfos_type.type_domain_port],
            None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST),
            ["alias", "member-entry"])
        self.load(dictvalues, 1)


class effective_configuration(pyfos_rest_util.rest_object):
    """Class of effective zone configuration

    class members:

        +-----------------------------------+---------------------------+-----------------------------------------------------------+
        | Attribute name                    | Description               |Frequently used methods                                    |
        +===================================+===========================+===========================================================+
        | cfg-name                          | enabled cfg name          |:func:`set_cfg_name`                                       |
        |                                   |                           |:func:`peek_cfg_name`                                      |
        +-----------------------------------+---------------------------+-----------------------------------------------------------+
        | checksum                          | current db checksum       |:func:`peek_checksum`                                      |
        +-----------------------------------+---------------------------+-----------------------------------------------------------+
        | cfg-action                        | cfg actions to enable,    |:func:`set_cfg_action`                                     |
        |                                   | disable, clear, or save   |:func:`peek_cfg_action`                                    |
        +-----------------------------------+---------------------------+-----------------------------------------------------------+
        | default-zone-access               | default zone access to all|:func:`set_default_zone_access`                            |
        |                                   | or none                   |:func:`peek_default_zone_access`                           |
        +-----------------------------------+---------------------------+-----------------------------------------------------------+
        | db-avail                          | current db available size |:func:`peek_db_avail`                                      |
        +-----------------------------------+---------------------------+-----------------------------------------------------------+
        | db-max                            | current db max size       |:func:`peek_db_max`                                        |
        +-----------------------------------+---------------------------+-----------------------------------------------------------+
        | db-committed                      | current db committed size |:func:`peek_db_committed`                                  |
        +-----------------------------------+---------------------------+-----------------------------------------------------------+
        | db-transaction                    | current db pending trans  |:func:`peek_db_transaction`                                |
        |                                   | size                      |                                                           |
        +-----------------------------------+---------------------------+-----------------------------------------------------------+
        | db-transaction                    | current db pending trans  |:func:`peek_db_transaction`                                |
        |                                   | size                      |                                                           |
        +-----------------------------------+---------------------------+-----------------------------------------------------------+
        | transaction-token                 | current db pending trans  |:func:`peek_transaction_token`                             |
        |                                   | token                     |                                                           |
        +-----------------------------------+---------------------------+-----------------------------------------------------------+
        | db-chassis-wide-committed         | current db chassis size   |:func:`peek_db_chassis_wide_committed`                     |
        +-----------------------------------+---------------------------+-----------------------------------------------------------+
        | enabled-zone                      | list of enabled zones     |:func:`peek_enabled_zone`                                  |
        +-----------------------------------+---------------------------+-----------------------------------------------------------+
        | zone-name                         | name of zone              |:func:`peek_enabled_zone_zone_name`                        |
        +-----------------------------------+---------------------------+-----------------------------------------------------------+
        | zone-type                         | type of zone              |:func:`peek_enabled_zone_zone_type`                        |
        +-----------------------------------+---------------------------+-----------------------------------------------------------+
        | zone-type-string                  | type of zone              |:func:`peek_enabled_zone_zone_type_string`                 |
        +-----------------------------------+---------------------------+-----------------------------------------------------------+
        | member-entry/entry-name           | device entry list         |:func:`peek_enabled_zone_member_entry_entry_name`          |
        +-----------------------------------+---------------------------+-----------------------------------------------------------+
        | member-entry/principal-entry-name | principal device entry    |:func:`peek_enabled_zone_member_entry_principal_entry_name`|
        |                                   | list                      |                                                           |
        +-----------------------------------+---------------------------+-----------------------------------------------------------+

    *Object methods*

        .. method:: get()

            Return :class:`effective_configuration` object
            with values for all the attributes.
            The object can be printed using :func:`pyfos_utils.response_print`

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary of error or
                :class:`effective_configuration` object

        .. method:: patch()

            Apply changes. Fields involved are set within the object using
            attribute's set method.

            Example usage of the method to enable an cfg::

                current_effective_configuration =
                    pyfos_newzone.effective_configuration_get(session)

                effective_configuration_obj =
                    pyfos_newzone.effective_configuration()
                effective_configuration_obj.set_cfg_name("newcfg")
                effective_configuration_obj.set_checksum(
                    current_effective_configuration.peek_checksum())
                effective_configuration_obj.patch(session)

            Example usage of the method to save an cfg::

                current_effective_configuration =
                    pyfos_newzone.effective_configuration_get(session)

                effective_configuration_obj =
                    pyfos_newzone.effective_configuration()
                effective_configuration_obj.set_cfg_action(pyfos_zone.CFG_ACTION_SAVE)
                effective_configuration_obj.set_checksum(
                    current_effective_configuration.peek_checksum())
                effective_configuration_obj.patch(session)

            Example usage of set_cfg_action::

                effective_configuration_obj.set_cfg_action(pyfos_zone.CFG_ACTION_SAVE)
                effective_configuration_obj.set_cfg_action(pyfos_zone.CFG_DISABLE)
                effective_configuration_obj.set_cfg_action(pyfos_zone.CFG_CLEAR)
                effective_configuration_obj.set_cfg_action(pyfos_zone.CFG_ABORT)

            .. note:: cfg enable, save, and disable requires the
                current checksum to be passed

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary of error or success response

    *Attribute methods*

        .. method:: set_cfg_name(cfg_name)

            Sets cfg name in the object

            :param cfg_name: cfg name
            :rtype: dictionary of error or success response

        .. method:: peek_cfg_name()

            Reads cfg name in the object.

            :rtype: None or cfg name

        .. method:: peek_checksum()

            Reads checksum in the object.

            :rtype: None or checksum

        .. method:: set_cfg_action(cfg_action)

            Sets cfg action in the object

            :param cfg_action: cfg action such as enable,
                disable, save, or clear
            :rtype: dictionary of error or success response

        .. method:: peek_cfg_action()

            Reads cfg action in the object.

            :rtype: None or cfg action

        .. method:: set_default_zone_access(mode)

            Sets default zone access mode in the object.
            Mode of 1 is all access & 0 is no access.

            :param mode: default zone access mode
            :rtype: dictionary of error or success response

        .. method:: peek_default_zone_access()

            Reads default zone access mode in the object.
            Mode of 1 is all access & 0 is no access.

            :rtype: None or default zone access mode

        .. method:: peek_db_avail()

            Reads available db size in the object.

            :rtype: None or available db size

        .. method:: peek_db_max()

            Reads max db size in the object.

            :rtype: None or max db size

        .. method:: peek_db_committed()

            Reads committed db size in the object.

            :rtype: None or committed db size

        .. method:: peek_db_transaction()

            Reads transaction buffer size in the object.

            :rtype: None or transaction buffer size

        .. method:: peek_transaction_token()

            Reads transaction token in the object.

            :rtype: None or transaction token

        .. method:: peek_db_chassis_wide_committed()

            Reads chassis wide committed db size in the object.

            :rtype: None or db size

        .. method:: peek_enabled_zone()

            Reads list of enabled zones in the object.

            :rtype: None or list of enabled zones

        .. method:: peek_enabled_zone_zone_name()

            Reads zone name in the object.

            :rtype: None or zone name

        .. method:: peek_enabled_zone_zone_type()

            Reads the zone type in the object.

            :rtype: None or zone type

        .. method:: peek_enabled_zone_zone_type_string()

            Reads the zone type string in the object.

            :rtype: None or zone type string

        .. method:: peek_enabled_zone_member_entry_entry_name()

            Reads list of zone member devices in the object.

            :rtype: None or list of devices

        .. method:: peek_enabled_zone_member_entry_principal_entry_name()

            Reads list of zone member principal devices in the object.

            :rtype: None or list of devices

    """

    def __init__(self, dictvalues={}):
        urilist = list([dict({'URIVER': version.VER_RANGE_820_TO_821A,
                              'URI': "/rest/running/zoning/" +
                              "effective-configuration"}),
                        dict({'URIVER': version.VER_RANGE_821b_and_ABOVE,
                              'URI': "/rest/running/brocade-zone/" +
                              "effective-configuration"})])
        super().__init__(pyfos_rest_util.rest_obj_type.zone_effective, urilist)
        self.add(pyfos_rest_util.rest_attribute(
            "cfg-name", pyfos_type.type_zoning_name,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "checksum", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "cfg-action", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "default-zone-access", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "db-avail", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "db-max", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "db-committed", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "db-transaction", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "transaction-token", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "db-chassis-wide-committed", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "enabled-zone", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER_LIST_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "zone-name", pyfos_type.type_zoning_name,
            None, pyfos_rest_util.REST_ATTRIBUTE_KEY), ["enabled-zone"])
        self.add(pyfos_rest_util.rest_attribute(
            "zone-type", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG,
            version.VER_RANGE_820_TO_900), ["enabled-zone"])
        self.add(pyfos_rest_util.rest_attribute(
            "zone-type-string", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG,
            version.VER_RANGE_900_and_ABOVE), ["enabled-zone"])
        self.add(pyfos_rest_util.rest_attribute(
            "member-entry", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER_NOT_CONFIG),
            ["enabled-zone"])
        self.add(pyfos_rest_util.rest_attribute(
            "entry-name", [pyfos_type.type_wwn, pyfos_type.type_domain_port],
            None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST_NOT_CONFIG),
            ["enabled-zone", "member-entry"])
        self.add(pyfos_rest_util.rest_attribute(
            "principal-entry-name",
            [pyfos_type.type_wwn, pyfos_type.type_domain_port],
            None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST_NOT_CONFIG),
            ["enabled-zone", "member-entry"])

        self.load(dictvalues, 1)


class fabric_lock(pyfos_rest_util.rest_object):
    """Class containing the zoning fabric lock attributes

    class members:

        +----------------------------------+-------------------------------+---------------------------------------------+
        | Attribute name                   | Description                   |Frequently used methods                      |
        +==================================+===============================+=============================================+
        | lock-principal-domain-id         | the domain id that currently  |:func:`peek_lock_principal_domain_id`        |
        |                                  | holds the zone fabric lock    |                                             |
        +----------------------------------+-------------------------------+---------------------------------------------+
        | lock-principal-transaction-token | the token of the open zone    |:func:`peek_lock_principal_transaction_token`|
        |                                  | transaction on the current    |                                             |
        |                                  | lock principal domain id      |                                             |
        +----------------------------------+-------------------------------+---------------------------------------------+
        | timeout                          | the current zone fabric lock  |:func:`peek_timeout`                         |
        |                                  | timeout value of the current  |                                             |
        |                                  | open lock principal           |                                             |
        |                                  | transaction token             |                                             |
        +----------------------------------+-------------------------------+---------------------------------------------+
        | remaining-time                   | the remaining time of the open|:func:`peek_remaining_time`                  |
        |                                  | zone transaction owned by the |                                             |
        |                                  | lock principal domain id      |                                             |
        +----------------------------------+-------------------------------+---------------------------------------------+
        | client-role                      | role name of the client that  |:func:`peek_client_role`                     |
        |                                  | owns the zone fabric lock     |                                             |
        +----------------------------------+-------------------------------+---------------------------------------------+
        | client-user-name                 | user name of the client that  |:func:`peek_client_user_name`                |
        |                                  | owns the zone fabric lock     |                                             |
        +----------------------------------+-------------------------------+---------------------------------------------+
        | client-ip-address                | ip address of the client that |:func:`peek_client_ip_address`               |
        |                                  | owns the zone fabric lock     |                                             |
        +----------------------------------+-------------------------------+---------------------------------------------+
        | client-interface                 | interface used by the client  |:func:`peek_client_interface`                |
        |                                  | that owns the zone fabric lock|                                             |
        +----------------------------------+-------------------------------+---------------------------------------------+
        | client-application-namee         | application name used by the  |:func:`peek_client_application_name`         |
        |                                  | client that owns the zone     |                                             |
        |                                  | fabric lock                   |                                             |
        +----------------------------------+-------------------------------+---------------------------------------------+

    *Object methods*

        .. method:: get()

            Return :class:`fabric-lock` object
            with values for all the attributes.
            The object can be printed using :func:`pyfos_utils.response_print`

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary of error or
                :class:`fabric-lock` object

    *Attribute methods*

        .. method:: peek_lock_principal_domain_id()

            Reads the lock principal domain id that currently
            holds the zone fabric lock.

            :rtype: 0 or the lock principal domain id

        .. method:: peek_lock_principal_transaction_token()

            Reads the token of the open zone transaction on the current
            lock principal domain id.

            :rtype: None or the lock principal transaction token

        .. method:: peek_timeout()

            Reads the current zone fabric lock timeout value of the
            currently open lock principal transaction token

            :rtype: None or the timeout value

        .. method:: peek_remaining_time()

            Reads the remaining time of the open zone transaction
            owned by the lock principal domain id.

            :rtype: None or the remaining time

        .. method:: peek_client_role()

            Reads the role name of the client that owns the
            zone fabric lock.

            :rtype: None or the client role

        .. method:: peek_client_user_name()

            Reads the user name of the client that owns the
            zone fabric lock.

            :rtype: None or the client user name

        .. method:: peek_client_ip_address()

            Reads the ip address of the client that owns the
            zone fabric lock.

            :rtype: None or the client ip address

        .. method:: peek_client_interface()

            Reads the interface used by the client that owns the
            zone fabric lock.

            :rtype: None or the client interface

        .. method:: peek_client_application_name()

            Reads the application name of the client that owns the
            zone fabric lock.

            :rtype: None or the client application name

    """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.zone_fabric_lock,
                         "/rest/running/brocade-zone/fabric-lock",
                         version.VER_RANGE_900_and_ABOVE)
        self.add(pyfos_rest_util.rest_attribute(
            "lock-principal-domain-id", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "lock-principal-transaction-token", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "timeout", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "remaining-time", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "client-role", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "client-user-name", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "client-ip-address", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "client-interface", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "client-application-name", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.load(dictvalues, 1)
