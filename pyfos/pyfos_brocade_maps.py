#!/usr/bin/env python3

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
:mod:`pyfos_brocade_maps` - PyFOS module to provide rest support \
for MAPS.
******************************************************************\
****************************************
The :mod:`pyfos_brocade_maps` provides a REST support for MAPS.

"""

import pyfos.pyfos_rest_util as pyfos_rest_util
from pyfos.pyfos_type import pyfos_type
import pyfos.pyfos_version as version


class maps_policy(pyfos_rest_util.rest_object):
    """
        This class Manages policies - create and manage monitoring policies.
        A MAPS policy is a set of rules that define thresholds for measures
        and actions to take when a threshold is triggered. When you enable a
        policy, all of the rules in the policy are in effect. A switch can have
        multiple policies.

    Important class members:

        +-------------------------------------------+----------------------------------+----------------------------------------------+
        | Attribute name                            | Description                      |Frequently used methods                       |
        +===========================================+==================================+==============================================+
        | name                                      | Represents the policy name       |:func:`set_name`                              |
        |                                           |                                  |:func:`peek_name`                             |
        +-------------------------------------------+----------------------------------+----------------------------------------------+
        | rule-list/rule                            | List of rules in the policy      |:func:`set_rule_list_rule`                    |
        |                                           |                                  |:func:`peek_rule_list_rule`                   |
        +-------------------------------------------+----------------------------------+----------------------------------------------+
        | is-predefined-policy                      | Represents policy is active      |:func:`peek_is_predefined_policy`             |
        |                                           | or non-active                    |                                              |
        +-------------------------------------------+----------------------------------+----------------------------------------------+
        | is-active-policy                          | Represents policy is predefined  |:func:`set_is_active_policy`                  |
        |                                           | or user-defined                  |:func:`peek_is_active_policy`                 |
        +-------------------------------------------+----------------------------------+----------------------------------------------+

    *Object methods*

        .. staticmethod:: get(session)

            Return a :class:`maps_policy` object if group name is provided.
            Else returns all the objects of the :class:`maps_policy`

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: :class:`maps_policy` object. Dictionary in case of error.
                objects if there are more than one. Dictionary in case of error.

        .. method:: post(session)

            This method is used to create a MAPS policy and add rules to existing policy.
            If rules list is empty then an empty MAPS policy(without any rules) will be created.
            If policy is already present, then in post session rules will be added into policy.

            Example usage of the method to create new policy on switch

            .. code-block:: python

                # initialize the object
                maps_pol = pyfos_brocade_maps.maps_policy()
                # set the policy name
                maps_pol.set_name("policy1")
                # execute HTTP post command to apply the object to the
                # switch connected through session
                maps_pol.post(session)

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary of error or success response

        .. method:: patch(session)

            Updates the list of rules in a policy with the input rules. Note when
            patch operation is executed all the rules will be replaced by the ones
            provided in the CLI.
            For adding rules to an existing policy, post operation to be used.
            For deleting rules from an existing policy, delete operation to be used.

        .. method:: delete(session)

            This method is used to delete MAPS policy and rules present in the policy.
            If rule list is empty then MAPS policy is deleted.
            If rule list is not empty then rules will be deleted from the policy.

            Example usage of the method to delete MAPS policy

            .. code-block:: python

                # initialize the object
                maps_pol = pyfos_brocade_maps.maps_policy()
                # set the policy name
                maps_pol.set_name("policy1")
                # execute HTTP post command to apply the object to the
                # switch connected through session
                maps_pol.delete(session)

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary of error or success response

    *Attribute methods*

        .. method:: set_name()

            sets the MAPS policy name

            :rtype: dictionary in case of error or success response

        .. method:: peek_name()

            gets the MAPS policy name

            :rtype: dictionary in case of error or success response

        .. method:: set_rule_list_rule()

            sets the list of rules in rule-list container which will be part of
            a MAPS policy

            :rtype: dictionary in case of error or success response

        .. method:: peek_rule_list_rule()

            get the list of rules configured in a policy

            :rtype: dictionary in case of error or success response

        .. method:: peek_is_predefined_policy()

            Returns whether policy is pre-defined or not

            :rtype: dictionary in case of error or success response

        .. method:: peek_is_active_policy()

            Returns whether policy is active or not

            :rtype: dictionary in case of error or success response

        .. method:: set_is_active_policy()

            Set the Policy name and when PATCH operation is performed, then
            specified MAPS policy will be enabled.

            :rtype: dictionary in case of error or success response

    """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.maps_policy,
                         "/rest/running/brocade-maps/maps-policy",
                         version.VER_RANGE_821_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "name", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_KEY))

        self.add(pyfos_rest_util.rest_attribute(
            "rule-list",  pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))

        self.add(pyfos_rest_util.rest_attribute(
            "rule",  pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST), ["rule-list"])

        self.add(pyfos_rest_util.rest_attribute(
            "is-predefined-policy", pyfos_type.type_bool,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "is-active-policy", pyfos_type.type_bool,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.load(dictvalues, 1)


class group(pyfos_rest_util.rest_object):
    """
        This class manages the groups. Use this module to create and  modify groups of
        elements that  are  to be monitored using the same set of thresholds.
        For example, you can create a group of ports that behave in a similar
        manner, such as UNIX ports or long-distance ports. The elements in a
        group must be of the same type:  ports,  circuits,  or  SFP.
        By creating a group of similar elements, you can manage these elements
        as a single  entity.

    Important class members:

        +-------------------------------------------+----------------------------------+----------------------------------------------+
        | Attribute name                            | Description                      |Frequently used methods                       |
        +===========================================+==================================+==============================================+
        | name                                      | Represents the group name        |:func:`set_name`                              |
        |                                           |                                  |:func:`peek_name`                             |
        +-------------------------------------------+----------------------------------+----------------------------------------------+
        | group-type                                | Represents the group type        |:func:`set_group_type`                        |
        |                                           |                                  |:func:`peek_group_type`                       |
        +-------------------------------------------+----------------------------------+----------------------------------------------+
        | group-feature                             | Represents the group feature     |:func:`set_group_feature`                     |
        |                                           |                                  |:func:`peek_group_feature`                    |
        +-------------------------------------------+----------------------------------+----------------------------------------------+
        | feature-pattern                           | Represents the feature pattern   |:func:`set_feature_pattern`                   |
        |                                           |                                  |:func:`peek_feature_pattern`                  |
        +-------------------------------------------+----------------------------------+----------------------------------------------+
        | is-predefined                             | Returns true if group is         |:func:`peek_is_predefined`                    |
        |                                           | pre-defined group                |                                              |
        +-------------------------------------------+----------------------------------+----------------------------------------------+
        | is-modifiable                             | Indicates whether group is       |:func:`peek_is_modifiable`                    |
        |                                           | modifiable or not                |                                              |
        +-------------------------------------------+----------------------------------+----------------------------------------------+
        | members/member                            | Members - for example list of    |:func:`set_members_member`                    |
        |                                           | ports, sfps or circuits          |:func:`peek_members_member`                   |
        +-------------------------------------------+----------------------------------+----------------------------------------------+

    *Object methods*

        .. staticmethod:: get(session)

            Return a :class:`group` object if group name is provided.
            Else returns all the objects of the :class:`group`

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: :class:`group` object. Dictionary in case of error.
                objects if there are more than one. Dictionary in case of error.

        .. method:: post(session)

            This method is used to create MAPS group on switch.
            post method is also used to create dynamic groups.
            If group is already present then post method is used for adding members
            to the group.

            Example usage of the method to create new group on switch

            .. code-block:: python

                # initialize the object
                maps_grp = pyfos_brocade_maps.group()
                # set the policy name
                maps_grp.set_name("group1")
                # execute HTTP post command to apply the object to the
                # switch connected through session
                maps_grp.post(session)

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary of error or success response

        .. method:: patch(session)

            patch method is used for updating dynamic groups only.
            for static groups, adding members, post operation to be used.
            for static groups, deleting members, delete operations to be used.

        .. method:: delete(session)

            This method is used to delete MAPS group if members are empty.
            If members are present, then this operation deletes members from group.

            Example usage of the method to delete MAPS group

            .. code-block:: python

                # initialize the object
                maps_grp = pyfos_brocade_maps.group()
                # set the group name
                maps_grp.set_name("group1")
                # execute HTTP post command to apply the object to the
                # switch connected through session
                maps_grp.delete(session)

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary of error or success response

    *Attribute methods*

        .. method:: set_name()

            sets the MAPS group name

            :rtype: dictionary in case of error or success response

        .. method:: peek_name()

            gets the MAPS group name

            :rtype: dictionary in case of error or success response

        .. method:: set_group_type()

            sets the group type. Group type can be PORT, SFP or CIRCUITS.

            :rtype: dictionary in case of error or success response

        .. method:: peek_group_type()

            get the group type.

            :rtype: dictionary in case of error or success response

        .. method:: set_group_feature()

            sets the dynamic group feature. There are two types of Group in MAPS.
            Dynamic group and static groups. If this feature is set then group is
            considered as Dynamic group.

            :rtype: dictionary in case of error or success response

        .. method:: peek_group_feature()

            Returns the dynamic group feature configured.

            :rtype: dictionary in case of error or success response

        .. method:: set_feature_pattern()

            sets the dynamic group feature pattern. it can be port-name or node-wwn

            :rtype: dictionary in case of error or success response

        .. method:: peek_feature_pattern()

            Returns the dynamic group feature configured.

            :rtype: dictionary in case of error or success response

        .. method:: peek_is_predefined()

            Returns true if the group is pre-defined.
            There are two types of group, pre-defined and user-defined.
            pre-defined groups are the ones defined default by the switch.
            user-defined groups are the ones defined/configured by user.

            :rtype: dictionary in case of error or success response

        .. method:: peek_is_modifiable()

            Returns true if group is modifiable

            :rtype: dictionary in case of error or success response

        .. method:: set_members_member()

            Sets list of members to be monitored as part of the group.

            :rtype: dictionary in case of error or success response

        .. method:: peek_members_member()

            Gets list of members that are monitored as part of the group.

            :rtype: dictionary in case of error or success response

    """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.group,
                         "/rest/running/brocade-maps/group",
                         version.VER_RANGE_821_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "name", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_KEY))

        self.add(pyfos_rest_util.rest_attribute(
            "group-type",  pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "group-feature",  pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "feature-pattern",  pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "is-predefined", pyfos_type.type_bool,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "is-modifiable", pyfos_type.type_bool,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "members", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))

        self.add(pyfos_rest_util.rest_attribute(
            "member",  pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST), ["members"])

        self.load(dictvalues, 1)


class rule(pyfos_rest_util.rest_object):
    """
        Manages the rules. Use this module to configure and manage MAPS
        monitoring rules and to display the configured rules. A rule associates a
        condition  with  actions that must be triggered when the specified
        condition is evaluated to be true. When you modify a rule, the rule does not
        take effect until you enable the policy. If the rule is part of the enabled
        policy, you must re-enable the policy for the rule to take effect.

    Important class members:

        +----------------------------------+-------------------------------------------+----------------------------------------------+
        | Attribute name                   | Description                               |Frequently used methods                       |
        +==================================+===========================================+==============================================+
        | name                             | Represents the rule name                  |:func:`set_name`                              |
        |                                  |                                           |:func:`peek_name`                             |
        +----------------------------------+-------------------------------------------+----------------------------------------------+
        | is-rule-on-rule                  | Represents the rule type                  |:func:`set_is_rule_on_rule`                   |
        |                                  |                                           |:func:`peek_is_rule_on_rule`                  |
        +----------------------------------+-------------------------------------------+----------------------------------------------+
        | monitoring-system                | Represents the stats or error being       |:func:`set_monitoring_system`                 |
        |                                  | monitored. example CRC, ITW, PS_STATE     |:func:`peek_monitoring_system`                |
        +----------------------------------+-------------------------------------------+----------------------------------------------+
        | time-base                        | Represents timebase in the rule           |:func:`set_time_base`                         |
        |                                  |                                           |:func:`peek_time_base`                        |
        +----------------------------------+-------------------------------------------+----------------------------------------------+
        | logical-operator                 | Represents logical operators              |:func:`set_logical_operator`                  |
        |                                  |                                           |:func:`peek_logical_operator`                 |
        +----------------------------------+-------------------------------------------+----------------------------------------------+
        | threshold-value                  | Represents threshold value                |:func:`set_threshold_value`                   |
        |                                  |                                           |:func:`peek_threshold_value`                  |
        +----------------------------------+-------------------------------------------+----------------------------------------------+
        | group-name                       | Represents group name. example - ALL_PORTS|:func:`set_group_name`                        |
        |                                  |                                           |:func:`peek_group_name`                       |
        +----------------------------------+-------------------------------------------+----------------------------------------------+
        | actions/action                   | Represents actions list                   |:func:`set_actions_action`                    |
        |                                  |                                           |:func:`peek_actions_action`                   |
        +----------------------------------+-------------------------------------------+----------------------------------------------+
        | is-predefined                    | Returns true if the rule is system defined|:func:`peek_is_predefined`                    |
        |                                  |                                           |                                              |
        +----------------------------------+-------------------------------------------+----------------------------------------------+
        | event-severity                   | Represents user configured severity -     |:func:`set_event_severity`                    |
        |                                  | warning, error, critical, info.           |:func:`peek_event_severity`                   |
        +----------------------------------+-------------------------------------------+----------------------------------------------+
        | toggle-time                      | Represents port toggle time               |:func:`set_toggle_time`                       |
        |                                  |                                           |:func:`peek_toggle_time`                      |
        +----------------------------------+-------------------------------------------+----------------------------------------------+
        | quiet-time                       | Represents quiet time (QT) - means rule   |:func:`set_quiet_time`                        |
        |                                  | does not get trigger until QT expires     |:func:`peek_quiet_time`                       |
        +----------------------------------+-------------------------------------------+----------------------------------------------+
        | quiet-time-clear                 | Represents operation to clear             |:func:`set_quiet_time_clear`                  |
        |                                  | quiet-time-out.                           |:func:`peek_quiet_time_clear`                 |
        +----------------------------------+-------------------------------------------+----------------------------------------------+
        | un-quarantine-timeout            | Represents un-quarantine timeout          |:func:`set_un_quarantine_timeout`             |
        |                                  |                                           |:func:`peek_un_quarantine_timeout`            |
        +----------------------------------+-------------------------------------------+----------------------------------------------+
        | un-quarantine-clear              | Represents opearation to clear the        |:func:`set_un_quarantine_clear`               |
        |                                  | un-quarantine-timeout                     |:func:`peek_un_quarantine_clear`              |
        +----------------------------------+-------------------------------------------+----------------------------------------------+

    *Object methods*

        .. staticmethod:: get(session)

            Return a :class:`rule` object if rule name is provided.
            Else returns all the objects of the :class:`rule`

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: :class:`rule` object. Dictionary in case of error.
                objects if there are more than one. Dictionary in case of error.

        .. method:: post(session)

            Creates a MAPS rule. Fields involved are set
            within the object using attribute's set method.
            This method is used to create new rule on switch

            Example usage of the method to create new rule on switch

            .. code-block:: python

                # initialize the object
                maps_Rule = pyfos_brocade_maps.rule()
                # set the rule name
                maps_Rule.set_name("rule1")
                # set group to be monitored
                maps_Rule.set_group_name("ALL_PORTS")
                # set the monitoring stat
                maps_Rule.set_monitoring_system("CRC")
                # set the interval for monitoring
                maps_Rule.set_time_base("min")
                # set the condition for threshold
                maps_Rule.set_logical_operator("g")
                # set the threshold value
                maps_Rule.set_threshold_value("100")
                # set the action to be triggered
                maps_Rule.set_actions_action("raslog")
                # execute HTTP post command to apply the object to the
                # switch connected through session
                maps_Rule.post(session)

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary of error or success response

        .. method:: patch(session)

            This method is to update the rule, can be used to modify threshold
            values, or interval of monitoring etc..
            If a rule which is part of active policy is changed, then
            policy has to be re-activated for the rule to take effect

            Example usage of the method to update existing rule on switch

            .. code-block:: python

                # initialize the object
                maps_Rule = pyfos_brocade_maps.rule()
                # set the rule name
                maps_Rule.set_name("rule1")
                # set group to be monitored
                maps_Rule.set_group_name("ALL_PORTS")
                # set the monitoring stat
                maps_Rule.set_monitoring_system("CRC")
                # set the interval for monitoring
                maps_Rule.set_time_base("min")
                # set the condition for threshold
                maps_Rule.set_logical_operator("g")
                # set the threshold value
                maps_Rule.set_threshold_value("200")
                # set the action to be triggered
                maps_Rule.set_actions_action("raslog")
                # execute HTTP post command to apply the object to the
                # switch connected through session
                maps_Rule.patch(session)

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary of error or success response

        .. method:: delete(session)

            Deletes a MAPS group. Fields involved are
            set within the object using attribute's
            set method. This method is used to delete a MAPS group

            Example usage of the method to delete MAPS group

            .. code-block:: python

                # initialize the object
                maps_Rule = pyfos_brocade_maps.rule()
                # set the rule name
                maps_Rule.set_name("rule1")
                # execute HTTP post command to apply the object to the
                # switch connected through session
                maps_Rule.delete(session)

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary of error or success response

    *Attribute methods*

        .. method:: set_name()

            sets the MAPS rule name

            :rtype: dictionary in case of error or success response

        .. method:: peek_name()

            gets the MAPS rule name

            :rtype: dictionary in case of error or success response

        .. method:: set_is_rule_on_rule()

            sets "is-rule-on-rule" flag
            This flag has to be set while creating RoR rules.

            :rtype: dictionary in case of error or success response

        .. method:: peek_is_rule_on_rule()

            returns the value of RoR flag

            :rtype: dictionary in case of error or success response

        .. method:: set_monitoring_system()

            sets the monitoring stat

            :rtype: dictionary in case of error or success response

        .. method:: peek_monitoring_system()

            gets the monitoring stat for the given rule.

            :rtype: dictionary in case of error or success response

        .. method:: set_time_base()

            sets the time base which is the interval for monitoring

            :rtype: dictionary in case of error or success response

        .. method:: peek_time_base()

            get the time base configured for the rule

            :rtype: dictionary in case of error or success response

        .. method:: set_logical_operator()

            set the logical operator, the condition for which threshold will be met

            :rtype: dictionary in case of error or success response

        .. method:: peek_logical_operator()

            get the condition on which threshold will be met

            :rtype: dictionary in case of error or success response

        .. method:: set_threshold_value()

            sets the threshold value

            :rtype: dictionary in case of error or success response

        .. method:: peek_threshold_value()

            get the threshold value configured.

            :rtype: dictionary in case of error or success response

        .. method:: set_group_name()

            set the group name.

            :rtype: dictionary in case of error or success response

        .. method:: peek_group_name()

            get the group name

            :rtype: dictionary in case of error or success response

        .. method:: set_actions_action()

            set the list of actions which will be triggered when rule violation happens

            :rtype: dictionary in case of error or success response

        .. method:: peek_actions_action()

            get the list of actions which will be triggered when rule violation happens

            :rtype: dictionary in case of error or success response

        .. method:: peek_is_predefined()

            returns true if the rule is system defined.
            returns false if the rule is user defined

            :rtype: dictionary in case of error or success response

        .. method:: set_event_severity()

            sets the event severity.
            Possible values are "[critical | error | warning | info] | default"

            :rtype: dictionary in case of error or success response

        .. method:: peek_event_severity()

            get the event severity configured.

            :rtype: dictionary in case of error or success response

        .. method:: set_toggle_time()

            sets the toggle time

            :rtype: dictionary in case of error or success response

        .. method:: peek_toggle_time()

            gets the toggle time configured

            :rtype: dictionary in case of error or success response

        .. method:: set_quiet_time()

            sets the quiet time. If quiet time is configured, then reporting of
            rule violations will be done only after the expiry of quiet time.

            :rtype: dictionary in case of error or success response

        .. method:: peek_quiet_time()

            get the quiet time configured.

            :rtype: dictionary in case of error or success response

        .. method:: set_quiet_time_clear()

            updates the flag to clear quiet time

            :rtype: dictionary in case of error or success response

        .. method:: peek_quiet_time_clear()

            gets quiet time clear

            :rtype: dictionary in case of error or success response

        .. method:: set_un_quarantine_timeout()

            sets un-quarantine timeout value

            :rtype: dictionary in case of error or success response

        .. method:: peek_un_quarantine_timeout()

            returns the un-quarantine timeout value configured.

            :rtype: dictionary in case of error or success response

        .. method:: set_un_quarantine_clear()

            sets un-quarantine-clear

            :rtype: dictionary in case of error or success response

        .. method:: peek_un_quarantine_clear()

            returns the flag un-quarantine-clear

            :rtype: dictionary in case of error or success response

    """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.rule,
                         "/rest/running/brocade-maps/rule",
                         version.VER_RANGE_821_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "name", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_KEY))

        self.add(pyfos_rest_util.rest_attribute(
            "is-rule-on-rule",  pyfos_type.type_bool,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "monitoring-system",  pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "time-base",  pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "logical-operator", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "threshold-value", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "group-name", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "actions",  pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))

        self.add(pyfos_rest_util.rest_attribute(
            "action",  pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST), ["actions"])

        self.add(pyfos_rest_util.rest_attribute(
            "is-predefined", pyfos_type.type_bool,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "event-severity", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "toggle-time", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "quiet-time", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "quiet-time-clear", pyfos_type.type_bool,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "un-quarantine-timeout", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "un-quarantine-clear", pyfos_type.type_bool,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.load(dictvalues, 1)


class maps_config(pyfos_rest_util.rest_object):

    """
        Manages the MAPS behavior for the switch. Use  this  module  to
                perform the following MAPS functions:

        1. Define the list of allowable actions that can be taken on the switch
                when a threshold is triggered.
        2. Configure  e-mail  address  to  which  the alerts must be delivered.
        3. Delete all user-defined MAPS  configurations  related  to rules, groups,
                policies, and so on.
        4. Display MAPS settings.

    Important class members:

        +------------------------------------------+-------------------------------------------+--------------------------------------------------------+
        | Attribute name                           | Description                               |Frequently used methods                                 |
        +==========================================+===========================================+========================================================+
        | actions/action                           | Represents global actions list            |:func:`set_actions_action`                              |
        |                                          |                                           |:func:`peek_actions_action`                             |
        +------------------------------------------+-------------------------------------------+--------------------------------------------------------+
        | decommission-cfg                         | Represents the decommission behavior      |:func:`set_decommission_cfg`                            |
        |                                          | - default or impair.                      |:func:`peek_decommission_cfg`                           |
        +------------------------------------------+-------------------------------------------+--------------------------------------------------------+
        | recipient-address-list/recipient-address | Represents recipient email addresses      |:func:`set_recipient_address_list_recipient_address`    |
        |                                          |                                           |:func:`peek_recipient_address_list_recipient_address`   |
        +------------------------------------------+-------------------------------------------+--------------------------------------------------------+
        | sender-address                           | Represents sender email address           |:func:`set_sender_address`                              |
        |                                          |                                           |:func:`peek_sender_address`                             |
        +------------------------------------------+-------------------------------------------+--------------------------------------------------------+
        | domain-name                              | Represents domain name                    |:func:`set_domain_name`                                 |
        |                                          |                                           |:func:`peek_domain_name`                                |
        +------------------------------------------+-------------------------------------------+--------------------------------------------------------+
        | relay-ip-address                         | Represents relay IP address               |:func:`set_relay_ip_address`                            |
        |                                          |                                           |:func:`peek_relay_ip_address`                           |
        +------------------------------------------+-------------------------------------------+--------------------------------------------------------+
        | test-email/subject                       | configure subject for sending test email  |:func:`set_test_email_subject`                          |
        |                                          |                                           |:func:`peek_test_email_subject`                         |
        +------------------------------------------+-------------------------------------------+--------------------------------------------------------+
        | test-email/body                          | configure body for sending test email     |:func:`set_test_email_body`                             |
        |                                          |                                           |:func:`peek_test_email_body`                            |
        +------------------------------------------+-------------------------------------------+--------------------------------------------------------+

    *Object methods*

        .. staticmethod:: get(session)

            Return a :class:`maps_config` object.

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: :class:`rule` object. Dictionary in case of error.
                objects if there are more than one. Dictionary in case of error.

        .. staticmethod:: patch(session)

            patch method is used to update any member of maps-config class.
            Example usage of the method

            .. code-block:: python

                # initialize the object
                maps_config_obj = pyfos_brocade_maps.maps_config()
                # set the rule name
                maps_config_obj.set_sender_address("temp1@broadcom.com")
                # patch operation
                maps_config_obj.patch(session)

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary of error or success response

    *Attribute methods*

        .. method:: set_actions_action()

            set the list of global actions

            :rtype: dictionary in case of error or success response

        .. method:: peek_actions_action()

            get the list of global actions

            :rtype: dictionary in case of error or success response

        .. method:: set_decommission_cfg()

            set the decommission behavior - default or impair

            :rtype: dictionary in case of error or success response

        .. method:: peek_decommission_cfg()

            get the decommission behavior - default or impair

            :rtype: dictionary in case of error or success response

        .. method:: set_recipient_address_list_recipient_address()

            configure the recipient email address, max count is 5

            :rtype: dictionary in case of error or success response

        .. method:: peek_recipient_address_list_recipient_address()

            get the configured list of recipient email address.

            :rtype: dictionary in case of error or success response

        .. method:: set_sender_address()

            configure sender email address

            :rtype: dictionary in case of error or success response

        .. method:: peek_sender_address()

            get the configured sender email address

            :rtype: dictionary in case of error or success response

        .. method:: set_domain_name()

            configure domain name

            :rtype: dictionary in case of error or success response

        .. method:: peek_domain_name()

            get the configured domain name

            :rtype: dictionary in case of error or success response

        .. method:: set_relay_ip_address()

            configure relay ip address

            :rtype: dictionary in case of error or success response

        .. method:: peek_relay_ip_address()

            get the configured relay ip address

            :rtype: dictionary in case of error or success response

        .. method:: set_test_email_subject()

            set the subject for test email

            :rtype: dictionary in case of error or success response

        .. method:: peek_test_email_subject()

            get the configured subject for test email

            :rtype: dictionary in case of error or success response

        .. method:: set_test_email_body()

            configures the email body for test email

            :rtype: dictionary in case of error or success response

        .. method:: peek_test_email_body()

            get the configured email body for test email

            :rtype: dictionary in case of error or success response

    """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.maps_config,
                         "/rest/running/brocade-maps/maps-config",
                         version.VER_RANGE_821_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "actions",  pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))

        self.add(pyfos_rest_util.rest_attribute(
            "action",  pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST), ["actions"])

        self.add(pyfos_rest_util.rest_attribute(
            "decommission-cfg", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "recipient-address-list",  pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))

        self.add(pyfos_rest_util.rest_attribute(
            "recipient-address",  pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST),
            ["recipient-address-list"])

        self.add(pyfos_rest_util.rest_attribute(
            "sender-address",  pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "domain-name",  pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "relay-ip-address", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "test-email",  pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))

        self.add(pyfos_rest_util.rest_attribute(
            "subject",  pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST), ["test-email"])

        self.add(pyfos_rest_util.rest_attribute(
            "test-email",  pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))

        self.add(pyfos_rest_util.rest_attribute(
            "body",  pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST), ["test-email"])

        self.load(dictvalues, 1)


class switch_status_policy_report(pyfos_rest_util.rest_object):
    """
        Manages the switch status policy report. Use this module to retrieve
        the SSP state. SSP provides the overall status of the switch. If the
        over all status is not healthy, then module provides the contributing
        factors.

    Important class members:

        +-------------------------------------+------------------------------------------+----------------------------------------------------+
        | Attribute name                      | Description                              |Frequently used methods                             |
        +=====================================+==========================================+====================================================+
        | switch-health                       | Represents switch state. Switch health   |:func:`peek_switch_health`                          |
        |                                     | represents switch operating health       |                                                    |
        +-------------------------------------+------------------------------------------+----------------------------------------------------+
        | power-supply-health                 | Represents state of power supplies       |:func:`peek_power_supply_health`                    |
        |                                     |                                          |                                                    |
        +-------------------------------------+------------------------------------------+----------------------------------------------------+
        | fan-health                          | Represents state of fans                 |:func:`peek_fan_health`                             |
        |                                     |                                          |                                                    |
        +-------------------------------------+------------------------------------------+----------------------------------------------------+
        | wwn-health                          | Represents state of WWNs cards           |:func:`peek_wwn_health`                             |
        |                                     |                                          |                                                    |
        +-------------------------------------+------------------------------------------+----------------------------------------------------+
        | temperature-sensor-health           | Represents state of temperature sensors  |:func:`peek_temperature_sensor_health`              |
        |                                     |                                          |                                                    |
        +-------------------------------------+------------------------------------------+----------------------------------------------------+
        | ha-health                           | Represents state of high availability    |:func:`peek_ha_health`                              |
        |                                     | state - means both CPs are in sync       |                                                    |
        +-------------------------------------+------------------------------------------+----------------------------------------------------+
        | control-processor-health            | Represents state of CPs                  |:func:`peek_control_processor_health`               |
        |                                     |                                          |                                                    |
        +-------------------------------------+------------------------------------------+----------------------------------------------------+
        | core-blade-health                   | Represents state of core blades          |:func:`peek_core_blade_health`                      |
        |                                     |                                          |                                                    |
        +-------------------------------------+------------------------------------------+----------------------------------------------------+
        | blade-health                        | Represents state of AP blades            |:func:`peek_blade_health`                           |
        |                                     |                                          |                                                    |
        +-------------------------------------+------------------------------------------+----------------------------------------------------+
        | flash-health                        | Represents flash usage state. Flash usage|:func:`peek_flash_health`                           |
        |                                     | could be above threshold or limit        |                                                    |
        +-------------------------------------+------------------------------------------+----------------------------------------------------+
        | marginal-port-health                | Represents the mariginal ports state     |:func:`peek_marginal_port_health`                   |
        |                                     |                                          |                                                    |
        +-------------------------------------+------------------------------------------+----------------------------------------------------+
        | faulty-port-health                  | Represents the faulty ports state        |:func:`peek_faulty_port_health`                     |
        |                                     |                                          |                                                    |
        +-------------------------------------+------------------------------------------+----------------------------------------------------+
        | missing-sfp-health                  | Represents the missing SFPs state        |:func:`peek_missing_sfp_health`                     |
        |                                     |                                          |                                                    |
        +-------------------------------------+------------------------------------------+----------------------------------------------------+
        | error-port-health                   | Represents the error ports state         |:func:`peek_error_port_health`                      |
        |                                     |                                          |                                                    |
        +-------------------------------------+------------------------------------------+----------------------------------------------------+
        | expired-certificate-health          | Represents the expired certificate state |:func:`peek_expired_certificate_health`             |
        |                                     |                                          |                                                    |
        +-------------------------------------+------------------------------------------+----------------------------------------------------+
        | airflow-mismatch-health             | Represents the air flow mismatch state   |:func:`peek_airflow_mismatch_health`                |
        |                                     |                                          |                                                    |
        +-------------------------------------+------------------------------------------+----------------------------------------------------+

    *Object methods*

        .. staticmethod:: get(session)

            Return a :class:`switch_status_policy_report` object.
            individual attributes accessed through peek methods

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: :class:`switch_status_policy_report` object. Dictionary in case of error.

    *Attribute methods*

        .. method:: peek_switch_health()

            Reads the switch state

            :rtype: dictionary in case of error or success response

        .. method:: peek_power_supply_health()

            Reads the state of power supplies

            :rtype: dictionary in case of error or success response

        .. method:: peek_fan_health()

            Reads the state of fans

            :rtype: dictionary in case of error or success response

        .. method:: peek_wwn_health()

            Reads the state of WWNs cards

            :rtype: dictionary in case of error or success response

        .. method:: peek_temperature_sensor_health()

            Reads the state of temperature sensors

            :rtype: dictionary in case of error or success response

        .. method:: peek_ha_health()

            Reads the state of high availability state - means both CPs are in sync

            :rtype: dictionary in case of error or success response

        .. method:: peek_control_processor_health()

            Reads the state of CPs

            :rtype: dictionary in case of error or success response

        .. method:: peek_core_blade_health()

            Reads the state of core blades

            :rtype: dictionary in case of error or success response

        .. method:: peek_blade_health()

            Reads the state of AP blades

            :rtype: dictionary in case of error or success response

        .. method:: peek_flash_health()

            Reads the flash usage state

            :rtype: dictionary in case of error or success response

        .. method:: peek_marginal_port_health()

            Reads the mariginal ports state

            :rtype: dictionary in case of error or success response

        .. method:: peek_faulty_port_health()

            Reads the faulty ports state

            :rtype: dictionary in case of error or success response

        .. method:: peek_missing_sfp_health()

            Reads the missing SFPs state

            :rtype: dictionary in case of error or success response

        .. method:: peek_error_port_health()

            Reads the error ports state

            :rtype: dictionary in case of error or success response

        .. method:: peek_expired_certificate_health()

            Reads the expired certificate state

            :rtype: dictionary in case of error or success response

        .. method:: peek_airflow_mismatch_health()

           Reads the air flow mismatch state

            :rtype: dictionary in case of error or success response

    """

    def __init__(self, dictvalues={}):
        super().__init__(
                     pyfos_rest_util.rest_obj_type.switch_status_policy_report,
                     "/rest/running/brocade-maps/"
                     "switch-status-policy-report",
                     version.VER_RANGE_821_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "switch-health", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "power-supply-health", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "fan-health", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "wwn-health", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "temperature-sensor-health", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "ha-health", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "control-processor-health", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "core-blade-health", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "blade-health", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "flash-health", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "marginal-port-health", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "faulty-port-health", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "missing-sfp-health", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "error-port-health", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "expired-certificate-health", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "airflow-mismatch-health", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.load(dictvalues, 1)


class monitoring_system_matrix(pyfos_rest_util.rest_object):
    """
        Represents list of monitoring systems. Each monitoring sytem can support
        different time bases or actions, thresholds. Certain monitoring systems
        are supported on certain system - for example circuit or tunnel monitoring
        systems are supported on extension platforms.

    Important class members:

        +------------------------------------------------+-------------------------------------------+-----------------------------------------------------------+
        | Attribute name                                 | Description                               |Frequently used methods                                    |
        +================================================+===========================================+===========================================================+
        | monitoring-system                              | Represents monitoring system name         |:func:`peek_monitoring_system`                             |
        |                                                |                                           |                                                           |
        +------------------------------------------------+-------------------------------------------+-----------------------------------------------------------+
        | dashboard-category                             | Represents dashboard category of the      |:func:`peek_dashbroad_category`                            |
        |                                                | monitoring system                         |                                                           |
        +------------------------------------------------+-------------------------------------------+-----------------------------------------------------------+
        | group-type                                     | Represents group type                     |:func:`peek_group_type`                                    |
        |                                                |                                           |                                                           |
        +------------------------------------------------+-------------------------------------------+-----------------------------------------------------------+
        | base-time-bases/time-base                      | Represents the timebases supported        |:func:`peek_base_time_bases_time_base`                     |
        |                                                |                                           |                                                           |
        +------------------------------------------------+-------------------------------------------+-----------------------------------------------------------+
        | rule-on-rule-time-bases/rule-on-rule-time-base | Represents supported time bases for rule  |:func:`peek_rule_on_rule_time_bases_rule_on_rule_time_base`|
        |                                                | on rules                                  |                                                           |
        +------------------------------------------------+-------------------------------------------+-----------------------------------------------------------+
        | is-read-only                                   | true for Read only monitoring systems     |:func:`peek_is_read_only`                                  |
        |                                                |                                           |                                                           |
        +------------------------------------------------+-------------------------------------------+-----------------------------------------------------------+
        | monitored-logical-switch                       | monitoring can be in all the logical      |:func:`peek_monitored_logical_switch`                      |
        |                                                | switches or only in default logical switch|                                                           |
        +------------------------------------------------+-------------------------------------------+-----------------------------------------------------------+
        | is-rule-on-rule-supported                      | true if Rule-on-rule supported            |:func:`peek_is_rule_on_rule_supported`                     |
        |                                                |                                           |                                                           |
        +------------------------------------------------+-------------------------------------------+-----------------------------------------------------------+
        | is-quiet-time-supported                        | true if Quiet time feature supported      |:func:`peek_is_quiet_time_supported`                       |
        |                                                |                                           |                                                           |
        +------------------------------------------------+-------------------------------------------+-----------------------------------------------------------+
        | minimum-quiet-time                             | Quiet time feature supported              |:func:`peek_minimum_quiet_time`                            |
        |                                                |                                           |                                                           |
        +------------------------------------------------+-------------------------------------------+-----------------------------------------------------------+
        | monitoring-type                                | Monitorting type of the monitoring systems|:func:`peek_monitoring_type`                               |
        |                                                |                                           |                                                           |
        +------------------------------------------------+-------------------------------------------+-----------------------------------------------------------+
        | data-type                                      | Represents the unit of the data           |:func:`peek_data_type`                                     |
        |                                                |                                           |                                                           |
        +------------------------------------------------+-------------------------------------------+-----------------------------------------------------------+
        | description                                    | Description of the monitoring system      |:func:`peek_description`                                   |
        |                                                |                                           |                                                           |
        +------------------------------------------------+-------------------------------------------+-----------------------------------------------------------+
        | actions/action                                 | Represents global actions list            |:func:`peek_actions_action`                                |
        |                                                |                                           |                                                           |
        +------------------------------------------------+-------------------------------------------+-----------------------------------------------------------+
        | unit                                           | Represents data unit                      |:func:`peek_unit`                                          |
        |                                                |                                           |                                                           |
        +------------------------------------------------+-------------------------------------------+-----------------------------------------------------------+
        | data-range                                     | Represents data range                     |:func:`peek_data_range`                                    |
        |                                                |                                           |                                                           |
        +------------------------------------------------+-------------------------------------------+-----------------------------------------------------------+
        | logical-operators/logical-operator             | Supported logical operator                |:func:`peek_logical_operators_logical_operator`            |
        |                                                |                                           |                                                           |
        +------------------------------------------------+-------------------------------------------+-----------------------------------------------------------+

    *Object methods*

        .. staticmethod:: get(session)

            Return all :class:`monitoring_system_matrix` objects.
            individual attributes accessed through peek methods

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: :class:`monitoring_system_matrix` object. Dictionary in case of error.

    *Attribute methods*

        .. method:: peek_monitoring_system()

            Represents the monitoring system name. Ex: CRC, SEC_LV

            :rtype: dictionary in case of error or success response

        .. method:: peek_dashbroad_category()

            Represents dashboard category of the monitoring system

            :rtype: dictionary in case of error or success response

        .. method:: peek_group_type()

            Represents group type

            :rtype: dictionary in case of error or success response

        .. method:: peek_base_time_bases_time_base()

            Represents the timebases supported

            :rtype: dictionary in case of error or success response

        .. method:: peek_rule_on_rule_time_bases_rule_on_rule_time_base()

            Represents supported time bases for rule on rules.

            :rtype: dictionary in case of error or success response

        .. method:: peek_is_read_only()

            returns true for Read only monitoring systems

            :rtype: dictionary in case of error or success response

        .. method:: peek_monitored_logical_switch()

            returns "all-logical-switches" if it is monitored on all logical switches
            returns "default-switch-only" if it is monitored on default logical switch

            :rtype: dictionary in case of error or success response

        .. method:: peek_is_rule_on_rule_supported()

            returns true if Rule-on-rule supported

            :rtype: dictionary in case of error or success response

        .. method:: peek_is_quiet_time_supported()

            returns true if Quiet time feature supported

            :rtype: dictionary in case of error or success response

        .. method:: peek_minimum_quiet_time()

            Quiet time feature supported

            :rtype: dictionary in case of error or success response

        .. method:: peek_monitoring_type()

            returns monitorting type of the monitoring systems

            :rtype: dictionary in case of error or success response

        .. method:: peek_data_type()

            Represents the unit of the data

            :rtype: dictionary in case of error or success response

        .. method:: peek_description()

            Description of the monitoring system

            :rtype: dictionary in case of error or success response

        .. method:: peek_actions_action()

            Represents global actions list

            :rtype: dictionary in case of error or success response

        .. method:: peek_unit()

            Represents data unit

            :rtype: dictionary in case of error or success response

        .. method:: peek_data_range()

            Represents data range

            :rtype: dictionary in case of error or success response

        .. method:: peek_logical_operators_logical_operator()

            returns supported logical operator

            :rtype: dictionary in case of error or success response

    """

    def __init__(self, dictvalues={}):
        super().__init__(
                pyfos_rest_util.rest_obj_type.monitoring_system_matrix,
                "/rest/running/brocade-maps/monitoring-system-matrix",
                version.VER_RANGE_821_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "monitoring-system", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "dashboard-category", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "group-type", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "base-time-bases", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))

        self.add(pyfos_rest_util.rest_attribute(
            "time-base", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST),
            ["base-time-bases"])

        self.add(pyfos_rest_util.rest_attribute(
            "rule-on-rule-time-bases", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))

        self.add(pyfos_rest_util.rest_attribute(
            "rule-on-rule-time-base", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST),
            ["rule-on-rule-time-bases"])

        self.add(pyfos_rest_util.rest_attribute(
            "is-read-only", pyfos_type.type_bool,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "monitored-logical-switch", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "is-rule-on-rule-supported", pyfos_type.type_bool,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "is-quiet-time-supported", pyfos_type.type_bool,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "minimum-quiet-time", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "monitoring-type", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "data-type", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "description", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "actions", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))

        self.add(pyfos_rest_util.rest_attribute(
            "action", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST), ["actions"])

        self.add(pyfos_rest_util.rest_attribute(
            "unit", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "data-range", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "logical-operators", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))

        self.add(pyfos_rest_util.rest_attribute(
            "logical-operator", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST),
            ["logical-operators"])

        self.load(dictvalues, 1)


class paused_cfg(pyfos_rest_util.rest_object):
    """
        This class Manages pause and continue feature of MAPS. Use this module to pause
        monitoring of any element or group of elements.
        Manages only port, SFP, and circuit to pause or resume monitoring.

    Important class members:

        +-------------------------------+----------------------------------+----------------------------------------------+
        | Attribute name                | Description                      |Frequently used methods                       |
        +===============================+==================================+==============================================+
        | group-type                    | Represents group type for pausing|:func:`set_group_type`                        |
        |                               | or resuming monitoring           |:func:`peek_group_type`                       |
        +-------------------------------+----------------------------------+----------------------------------------------+
        | members/member                | members for pausing or resuming  |:func:`set_members_member`                    |
        |                               | monitoring                       |:func:`peek_members_member`                   |
        +-------------------------------+----------------------------------+----------------------------------------------+

    *Object methods*

        .. staticmethod:: get(session)

            Return a :class:`paused_cfg` object.
            returns list of all the members which are currently paused for monitoring.

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: :class:`paused_cfg` object. Dictionary in case of error.

        .. staticmethod:: post(session)

            members specified will be paused from monitoring.
            members can be "fc-port", "sfp" or "circuit".

        .. staticmethod:: delete(session)

            members specified will continue with monitoring.
            members can be "fc-port", "sfp" or "circuit".

    *Attribute methods*

        .. method:: set_group_type()

            Represents group Type - can be "fc-port", "sfp" or "circuit".

            :rtype: dictionary in case of error or success response

        .. method:: peek_group_type()

            get the configured group type

            :rtype: dictionary in case of error or success response

        .. method:: set_members_member()

            list of members which will be either paused or resumed for monitoring

            :rtype: dictionary in case of error or success response

        .. method:: peek_members_member()

            get the list of members

            :rtype: dictionary in case of error or success response

    """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.paused_cfg,
                         "/rest/running/brocade-maps/paused-cfg",
                         version.VER_RANGE_821_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "group-type", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_KEY))

        self.add(pyfos_rest_util.rest_attribute(
            "members",  pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))

        self.add(pyfos_rest_util.rest_attribute(
            "member",  pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST), ["members"])

        self.load(dictvalues, 1)


class system_resources(pyfos_rest_util.rest_object):
    """
        Manages the system resources - flash, RAM, and CPU usage. Usage is not
        real time and delayed up to 2 minutes.

    Important class members:

        +-------------------------------+----------------------------------+----------------------------------------------+
        | Attribute name                | Description                      |Frequently used methods                       |
        +===============================+==================================+==============================================+
        | cpu-usage                     | Represents CPU usage             |:func:`peek_cpu_usage`                        |
        |                               |                                  |                                              |
        +-------------------------------+----------------------------------+----------------------------------------------+
        | memory-usage                  | Represents memory usage          |:func:`peek_memory_usage`                     |
        |                               |                                  |                                              |
        +-------------------------------+----------------------------------+----------------------------------------------+
        | total-memory                  | Represents total memory          |:func:`peek_total_memory`                     |
        |                               |                                  |                                              |
        +-------------------------------+----------------------------------+----------------------------------------------+
        | flash-usage                   | Represents flash usage           |:func:`peek_flash_usage`                      |
        |                               |                                  |                                              |
        +-------------------------------+----------------------------------+----------------------------------------------+

    *Object methods*

        .. staticmethod:: get(session)

            Return a :class:`system_resources` object.
            Returns usage of system resources.

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: :class:`system_resources` object. Dictionary in case of error.

    *Attribute methods*

        .. method:: peek_cpu_usage()

            Returns CPU usage

            :rtype: dictionary in case of error or success response

        .. method:: peek_memory_usage()

            Returns Memory usage

            :rtype: dictionary in case of error or success response

        .. method:: peek_total_memory()

            Returns Total memory

            :rtype: dictionary in case of error or success response

        .. method:: peek_flash_usage()

            Returns Flash usage

            :rtype: dictionary in case of error or success response

    """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.system_resources,
                         "/rest/running/brocade-maps/system-resources",
                         version.VER_RANGE_821_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "cpu-usage", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "memory-usage", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "total-memory", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "flash-usage", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.load(dictvalues, 1)


class dashboard_misc(pyfos_rest_util.rest_object):
    """
        Represents dashboard's misc intomation such as starttime and operation.

    Important class members:

        +-------------------------------+----------------------------------+----------------------------------------------+
        | Attribute name                | Description                      |Frequently used methods                       |
        +===============================+==================================+==============================================+
        | maps-start-time               | MAPS monitoring start time       |:func:`peek_maps_start_time`                  |
        |                               |                                  |                                              |
        +-------------------------------+----------------------------------+----------------------------------------------+
        | clear-data                    | Represents operation to clear the|:func:`set_clear_data`                        |
        |                               | dashboard data                   |:func:`peek_clear_data`                       |
        +-------------------------------+----------------------------------+----------------------------------------------+

    *Object methods*

        .. staticmethod:: get(session)

            Return a :class:`dashboard_misc` object.
            Returns dashboard miscellaneous information such as maps start time

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: :class:`dashboard_misc` object. Dictionary in case of error.

        .. staticmethod:: patch(session)

            Clears the MAPS dashboard information when clear-data attribute is set.

            :rtype: Success or dictionary in case of error.

    *Attribute methods*

        .. method:: peek_maps_start_time()

            Returns Monitoring start time. MAPS is restartable service so the start time
            could be different than system up time

            :rtype: dictionary in case of error or success response

        .. method:: set_clear_data()

            Represents operation to clear the dashboard data. True - clears the
            data and false - no action.

            :rtype: dictionary in case of error or success response

        .. method:: peek_clear_data()

            Returns the value of clear-data

            :rtype: dictionary in case of error or success response

    """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.dashboard_misc,
                         "/rest/running/brocade-maps/dashboard-misc",
                         version.VER_RANGE_821_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "maps-start-time", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "clear-data", pyfos_type.type_bool,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.load(dictvalues, 1)


class dashboard_rule(pyfos_rest_util.rest_object):
    """
        Manages the dashboard. Use this module to view the events or
        rules triggered and the objects on which the rules were triggered over a
        specified period of time, and to clear the  dashboard data.

        User can get triggered rules list for the last 7 days. Rule list is
        needed to get the complete picture of switch operation. Data provides
        two views of operating state - state since mid night and last 7 days.
        For both the views user needs complete details of the each rules
        triggered and all the rules data.

    Important class members:

        +-------------------------------+--------------------------------------+----------------------------------------------+
        | Attribute name                | Description                          |Frequently used methods                       |
        +===============================+======================================+==============================================+
        | category                      | Represents dashboard category        |:func:`peek_category`                         |
        |                               |                                      |                                              |
        +-------------------------------+--------------------------------------+----------------------------------------------+
        | name                          | Represents rule name                 |:func:`peek_name`                             |
        |                               |                                      |                                              |
        +-------------------------------+--------------------------------------+----------------------------------------------+
        | triggered-count               | Represents the total rule count      |:func:`peek_triggered_count`                  |
        |                               | triggered for the category           |                                              |
        +-------------------------------+--------------------------------------+----------------------------------------------+
        | time-stamp                    | Represents last triggered time       |:func:`peek_time_stamp`                       |
        |                               |                                      |                                              |
        +-------------------------------+--------------------------------------+----------------------------------------------+
        | repetition-count              | Represents rule repetition count     |:func:`peek_repetition_count`                 |
        |                               |                                      |                                              |
        +-------------------------------+--------------------------------------+----------------------------------------------+
        | objects/object                | Represents objects violated the rule |:func:`peek_objects_object`                   |
        |                               | - for example ports, circuits        |                                              |
        +-------------------------------+--------------------------------------+----------------------------------------------+

    *Object methods*

        .. staticmethod:: get(session)

            Return a :class:`dashboard_rule` object.
            Returns the maps dashborad information, switch summary for last 7 days.
            and the rule violations affecting health.

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: :class:`dashboard_rule` object. Dictionary in case of error.

    *Attribute methods*

        .. method:: peek_category()

            returns the dashboard category

            :rtype: dictionary in case of error or success response

        .. method:: peek_name()

            gives the rule name

            :rtype: dictionary in case of error or success response

        .. method:: peek_triggered_count()

            represents the total rule count triggered for the category

            :rtype: dictionary in case of error or success response

        .. method:: peek_time_stamp()

            Represents last triggered time

            :rtype: dictionary in case of error or success response

        .. method:: peek_repetition_count()

            Represents rule repetition count i.e., how many times a rule has
            been triggered. Same rule could be triggered multiple times for
            same or different objects. For example defALL_D_PORTSCRC_10 might
            triggered 20 times in an hour for the same or different objects -
            in this case repetition-count would be 20

            :rtype: dictionary in case of error or success response

        .. method:: peek_objects_object()

            Represents objects violated the rule - for example ports, circuits

            :rtype: dictionary in case of error or success response

    """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.dashboard_rule,
                         "/rest/running/brocade-maps/dashboard-rule",
                         version.VER_RANGE_821_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "category", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "name", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "triggered-count", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "time-stamp", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "repetition-count", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "objects",  pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))

        self.add(pyfos_rest_util.rest_attribute(
            "object",  pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST), ["objects"])

        self.load(dictvalues, 1)
