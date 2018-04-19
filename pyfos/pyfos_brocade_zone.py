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

:mod:`pyfos_brocade_zone` - PyFOS module to provide rest \
        support for Zoning.
*********************************************************************************************************
The :mod:`pyfos_brocade_zone` provides a REST support for \
        Zoning.

"""

import pyfos.pyfos_rest_util as pyfos_rest_util
from pyfos.pyfos_type import pyfos_type

CFG_ACTION_SAVE = 1
CFG_ACTION_DISABLE = 2
CFG_ACTION_CLEAR = 3
CFG_ACTION_ABORT = 4

CFG = "CFG"
ZONE = "ZONE"
PEER_ZONE = "PEER_ZONE"
ALIAS = "ALIAS"

ZONE_TYPE_DEFAULT = 0
ZONE_TYPE_PEER = 1
ZONE_TYPE_TDZ = 2

ZONE_DEFAULT_NO_ACCESS = 'd__efault__Cfg'

DEF_ZONE_NONE = 0
DEF_ZONE_ALL = 1


class defined_configuration(pyfos_rest_util.rest_object):
    """Class of defined zone configuration

    Important class members:

        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | Attribute name                    | Description                   |Frequently used methods                                |
        +===================================+===============================+=======================================================+
        | cfg                               | a list of cfg 		    |:func:`set_cfg`                                        |
        |                                   |                               |:func:`peek_cfg`                                       |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | cfg-name                          | name of cfg                   |:func:`set_cfg_cfg_name`                               |
        |                                   |                               |:func:`peek_cfg_cfg_name`                              |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | member_zone/zone-name             | list of zone members in cfg   |:func:`set_cfg_member_zone_zone_name`                  |
        |                                   |                               |:func:`peek_cfg_member_zone_zone_name`                 |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | zone                              | a list of zone 		    |:func:`set_zone`                                       |
        |                                   |                               |:func:`peek_zone`                                      |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | zone-name                         | name of zone                  |:func:`set_zone_zone_name`                             |
        |                                   |                               |:func:`peek_zone_zone_name`                            |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | zone-type                         | type of zone                  |:func:`set_zone_zone_type`                             |
        |                                   |                               |:func:`peek_zone_zone_type`                            |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | member-entry/entry-name           | list of device members in zone|:func:`set_zone_member_entry_entry_name`               |
        |                                   |                               |:func:`peek_zone_member_entry_entry_name`              |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | member-entry/principal-entry-name | list of principal device      |:func:`set_zone_member_entry_principal_entry_name`     |
        |                                   | members in zone               |:func:`peek_zone_member_entry_principal_entry_name`    |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | alias                             | a list of alias 		    |:func:`set_alias`                                      |
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
            Type of 0 indicate normal Zone while
            type of 1 indicates Peer Zone.

            :param zone_type: zone type
            :rtype: dictionary of error or success response

        .. method:: peek_zone_zone_type()

            Reads zone type in the object.

            :rtype: None or zone type

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
        super().__init__(pyfos_rest_util.rest_obj_type.zone_defined,
                         "/rest/running/zoning/defined-configuration")

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
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG), ["zone"])
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
        | member-entry/entry-name           | device entry list         |:func:`peek_enabled_zone_member_entry_entry_name`          |
        +-----------------------------------+---------------------------+-----------------------------------------------------------+
        | embmer-entry/principal-entry-name | principal device entry    |:func:`peek_enabled_zone_member_entry_principal_entry_name`|
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

            :rtype: None or transactdion buffer size

        .. method:: peek_transaction_token()

            Reads transaction token in the object.

            :rtype: None or transactdion token

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

            Reads zone type in the object.

            :rtype: None or zone type

        .. method:: peek_enabled_zone_member_entry_entry_name()

            Reads list of zone member devices in the object.

            :rtype: None or list of devices

        .. method:: peek_enabled_zone_member_entry_principal_entry_name()

            Reads list of zone member principal devices in the object.

            :rtype: None or list of devices

    """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.zone_effective,
                         "/rest/running/zoning/effective-configuration")

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
            "default-zone-access",  pyfos_type.type_int,
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
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER_LIST))
        self.add(pyfos_rest_util.rest_attribute(
            "zone-name", pyfos_type.type_zoning_name,
            None, pyfos_rest_util.REST_ATTRIBUTE_KEY), ["enabled-zone"])
        self.add(pyfos_rest_util.rest_attribute(
            "zone-type", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG), ["enabled-zone"])
        self.add(pyfos_rest_util.rest_attribute(
            "member-entry", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER),
            ["enabled-zone"])
        self.add(pyfos_rest_util.rest_attribute(
            "entry-name", [pyfos_type.type_wwn, pyfos_type.type_domain_port],
            None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST),
            ["enabled-zone", "member-entry"])
        self.add(pyfos_rest_util.rest_attribute(
            "principal-entry-name",
            [pyfos_type.type_wwn, pyfos_type.type_domain_port],
            None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST),
            ["enabled-zone", "member-entry"])

        self.load(dictvalues, 1)
