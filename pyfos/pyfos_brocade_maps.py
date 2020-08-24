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
:mod:`pyfos_brocade_maps` - PyFOS module to provide REST support \
for MAPS.
******************************************************************\
****************************************
The :mod:`pyfos_brocade_maps` module provides REST support for MAPS.

"""

from pyfos import pyfos_rest_util
from pyfos.pyfos_type import pyfos_type
import pyfos.pyfos_version as version


class maps_policy(pyfos_rest_util.rest_object):
    """
        This class manages policies.
        A MAPS policy is a set of rules that define thresholds for measures
        and actions to take when a threshold is triggered. When you enable a
        policy, all of the rules in the policy are in effect. A switch can have
        multiple policies.

    Important Class Members:

        +-------------------------------------------+----------------------------------+----------------------------------------------+
        | Attribute Name                            | Description                      |Frequently Used Methods                       |
        +===========================================+==================================+==============================================+
        | name                                      | The policy name.                 |:func:`set_name`                              |
        |                                           |                                  |:func:`peek_name`                             |
        +-------------------------------------------+----------------------------------+----------------------------------------------+
        | rule-list/rule                            | List of rules in the policy.     |:func:`set_rule_list_rule`                    |
        |                                           |                                  |:func:`peek_rule_list_rule`                   |
        +-------------------------------------------+----------------------------------+----------------------------------------------+
        | is-predefined-policy                      | Whether the policy is predefined |:func:`peek_is_predefined_policy`             |
        |                                           | or user-defined.                 |                                              |
        +-------------------------------------------+----------------------------------+----------------------------------------------+
        | is-active-policy                          | Whether the policy is active     |:func:`set_is_active_policy`                  |
        |                                           | or non-active.                   |:func:`peek_is_active_policy`                 |
        +-------------------------------------------+----------------------------------+----------------------------------------------+

    *Object Methods*

        .. staticmethod:: get(session)

            Returns a :class:`maps_policy` object if a group name is provided.
            Otherwise, returns all objects of the :class:`maps_policy`.

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A :class:`maps_policy` object. A dictionary in case \
                of error objects if there are more than one.

        .. method:: post(session)

            Creates a MAPS policy and adds rules to an existing policy.
            If the rules list is empty, then an empty MAPS policy (without \
            any rules) is created.
            If the policy is already present, then use a POST operation to \
            add rules to the policy.

            Example Usage of the Method to Create a New Policy on the Switch

            .. code-block:: python

                # initialize the object
                maps_pol = pyfos_brocade_maps.maps_policy()
                # set the policy name
                maps_pol.set_name("policy1")
                # execute HTTP post command to apply the object to the
                # switch connected through session
                maps_pol.post(session)

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary of errors or a success response.

        .. method:: patch(session)

            Updates the list of rules in a policy with the input rules. Note \
            that when you use the PATCH operation, all rules are replaced by \
            the ones provided in the CLI.
            To add rules to an existing policy, use the POST operation.
            To delete rules from an existing policy, use the DELETE operation.

        .. method:: delete(session)

            Deletes the MAPS policy or any rules present in the policy.
            If the rule list is empty, deletes the MAPS policy.
            If the rule list is not empty, deletes the rules from the policy.

            Example Usage of the Method to Delete MAPS Policy

            .. code-block:: python

                # initialize the object
                maps_pol = pyfos_brocade_maps.maps_policy()
                # set the policy name
                maps_pol.set_name("policy1")
                # execute HTTP post command to apply the object to the
                # switch connected through session
                maps_pol.delete(session)

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary of errors or a success response.

    *Attribute Methods*

        .. method:: set_name()

            Sets the MAPS policy name.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_name()

            Gets the MAPS policy name.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_rule_list_rule()

            Sets the list of rules in a rule list container that will be part \
            of a MAPS policy.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_rule_list_rule()

            Gets the list of rules configured in a policy.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_is_predefined_policy()

            Returns whether the policy is pre-defined or not.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_is_active_policy()

            Returns whether the policy is active or not.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_is_active_policy()

            Sets the policy name; when a PATCH operation is performed, \
            the specified MAPS policy is enabled.

            :rtype: A dictionary in case of error or a success response.

    """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.maps_policy,
                         "/rest/running/brocade-maps/maps-policy",
                         version.VER_RANGE_821_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "name", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_KEY))

        self.add(pyfos_rest_util.rest_attribute(
            "rule-list", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))

        self.add(pyfos_rest_util.rest_attribute(
            "rule", pyfos_type.type_na,
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
        This class manages the groups. Use this module to create and modify
        groups of elements that  are  to be monitored using the same set of
        thresholds.
        For example, you can create a group of ports that behave in a similar
        manner, such as UNIX ports or long-distance ports. The elements in a
        group must be of the same type: ports, circuits, or SFP.
        By creating a group of similar elements, you can manage these elements
        as a single  entity.

    Important Class Members:

        +-------------------------------------------+----------------------------------+----------------------------------------------+
        | Attribute name                            | Description                      |Frequently used methods                       |
        +===========================================+==================================+==============================================+
        | name                                      | The group name.                  |:func:`set_name`                              |
        |                                           |                                  |:func:`peek_name`                             |
        +-------------------------------------------+----------------------------------+----------------------------------------------+
        | group-type                                | The group type.                  |:func:`set_group_type`                        |
        |                                           |                                  |:func:`peek_group_type`                       |
        +-------------------------------------------+----------------------------------+----------------------------------------------+
        | group-feature                             | The group feature.               |:func:`set_group_feature`                     |
        |                                           |                                  |:func:`peek_group_feature`                    |
        +-------------------------------------------+----------------------------------+----------------------------------------------+
        | feature-pattern                           | The feature pattern.             |:func:`set_feature_pattern`                   |
        |                                           |                                  |:func:`peek_feature_pattern`                  |
        +-------------------------------------------+----------------------------------+----------------------------------------------+
        | is-predefined                             | Returns true if the group is     |:func:`peek_is_predefined`                    |
        |                                           | a predefined group.              |                                              |
        +-------------------------------------------+----------------------------------+----------------------------------------------+
        | is-modifiable                             | Indicates whether the group is   |:func:`peek_is_modifiable`                    |
        |                                           | modifiable or not.               |                                              |
        +-------------------------------------------+----------------------------------+----------------------------------------------+
        | members/member                            | A list of members (for example a |:func:`set_members_member`                    |
        |                                           | list of ports, SFPs,             |:func:`peek_members_member`                   |
        |                                           | or circuits).                    |                                              |
        +-------------------------------------------+----------------------------------+----------------------------------------------+

    *Object Methods*

        .. staticmethod:: get(session)

            Returns a :class:`group` object if a group name is provided.
            Otherwise, returns all objects of the :class:`group`.

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A :class:`group` object. A dictionary in case of error
                objects if there are more than one.

        .. method:: post(session)

            Creates a MAPS group on the switch.
            Use the POST operation to create dynamic groups.
            If the group already exists, use the POST operation to add members
            to the group.

            Example Usage of the Method to Create a New Group on the Switch

            .. code-block:: python

                # initialize the object
                maps_grp = pyfos_brocade_maps.group()
                # set the policy name
                maps_grp.set_name("group1")
                # execute HTTP post command to apply the object to the
                # switch connected through session
                maps_grp.post(session)

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary of errors or a success response.

        .. method:: patch(session)

            Use the PATCH operation to update dynamic groups only.
            For static groups, use the POST operation to add members.
            For static groups, use the DELETE operation to delete members.

        .. method:: delete(session)

            Deletes a MAPS group if there are no members.
            If members are present, then this operation deletes members \
            from the group.

            Example Usage of the Method to Delete a MAPS Group

            .. code-block:: python

                # initialize the object
                maps_grp = pyfos_brocade_maps.group()
                # set the group name
                maps_grp.set_name("group1")
                # execute HTTP post command to apply the object to the
                # switch connected through session
                maps_grp.delete(session)

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary of errors or a success response.

    *Attribute Methods*

        .. method:: set_name()

            Sets the MAPS group name.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_name()

            Gets the MAPS group name.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_group_type()

            Sets the group type. Group type can be PORT, SFP, or CIRCUITS.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_group_type()

            Gets the group type.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_group_feature()

            Sets the dynamic group feature. There are two types of groups in \
            MAPS (dynamic groups and static groups). If this feature is set, \
            then the group is considered to be a dynamic group.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_group_feature()

            Returns the dynamic group feature configured.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_feature_pattern()

            Sets the dynamic group feature pattern. It can be a port name \
            or node WWN.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_feature_pattern()

            Returns the dynamic group feature configured.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_is_predefined()

            Returns true if the group is pre-defined.
            There are two types of groups, pre-defined and user-defined.
            Pre-defined groups are defined by default by the switch.
            User-defined groups are defined or configured by a user.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_is_modifiable()

            Returns true if you can modify the group.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_members_member()

            Sets a list of members to be monitored as part of the group.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_members_member()

            Gets a list of members to be monitored as part of the group.

            :rtype: A dictionary in case of error or a success response.

    """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.group,
                         "/rest/running/brocade-maps/group",
                         version.VER_RANGE_821_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "name", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_KEY))

        self.add(pyfos_rest_util.rest_attribute(
            "group-type", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "group-feature", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "feature-pattern", pyfos_type.type_str,
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
            "member", pyfos_type.type_na,
            None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST), ["members"])

        self.load(dictvalues, 1)


class rule(pyfos_rest_util.rest_object):
    """
        Manages the rules. Use this module to configure and manage MAPS
        monitoring rules and to display the configured rules. A rule associates a
        condition with actions that must be triggered when the specified
        condition is evaluated to be true. When you modify a rule, the rule does not
        take effect until you enable the policy. If the rule is part of the enabled
        policy, you must re-enable the policy for the rule to take effect.

    Important Class Members:

        +----------------------------------+-------------------------------------------+----------------------------------------------+
        | Attribute Name                   | Description                               |Frequently Used Methods                       |
        +==================================+===========================================+==============================================+
        | name                             | The rule name.                            |:func:`set_name`                              |
        |                                  |                                           |:func:`peek_name`                             |
        +----------------------------------+-------------------------------------------+----------------------------------------------+
        | is-rule-on-rule                  | The rule type.                            |:func:`set_is_rule_on_rule`                   |
        |                                  |                                           |:func:`peek_is_rule_on_rule`                  |
        +----------------------------------+-------------------------------------------+----------------------------------------------+
        | monitoring-system                | The stats or error being                  |:func:`set_monitoring_system`                 |
        |                                  | monitored (CRC, ITW, PS_STATE).           |:func:`peek_monitoring_system`                |
        +----------------------------------+-------------------------------------------+----------------------------------------------+
        | time-base                        | The time base in the rule.                |:func:`set_time_base`                         |
        |                                  |                                           |:func:`peek_time_base`                        |
        +----------------------------------+-------------------------------------------+----------------------------------------------+
        | logical-operator                 | The logical operator.                     |:func:`set_logical_operator`                  |
        |                                  |                                           |:func:`peek_logical_operator`                 |
        +----------------------------------+-------------------------------------------+----------------------------------------------+
        | threshold-value                  | The threshold value.                      |:func:`set_threshold_value`                   |
        |                                  |                                           |:func:`peek_threshold_value`                  |
        +----------------------------------+-------------------------------------------+----------------------------------------------+
        | group-name                       | The group name.                           |:func:`set_group_name`                        |
        |                                  |                                           |:func:`peek_group_name`                       |
        +----------------------------------+-------------------------------------------+----------------------------------------------+
        | actions/action                   | The actions list.                         |:func:`set_actions_action`                    |
        |                                  |                                           |:func:`peek_actions_action`                   |
        +----------------------------------+-------------------------------------------+----------------------------------------------+
        | is-predefined                    | Returns true if the rule is system        |:func:`peek_is_predefined`                    |
        |                                  | defined.                                  |                                              |
        +----------------------------------+-------------------------------------------+----------------------------------------------+
        | event-severity                   | The user configured severity:             |:func:`set_event_severity`                    |
        |                                  | warning, error, critical, info.           |:func:`peek_event_severity`                   |
        +----------------------------------+-------------------------------------------+----------------------------------------------+
        | toggle-time                      | The port toggle time.                     |:func:`set_toggle_time`                       |
        |                                  |                                           |:func:`peek_toggle_time`                      |
        +----------------------------------+-------------------------------------------+----------------------------------------------+
        | quiet-time                       | The quiet time (QT) - the rule            |:func:`set_quiet_time`                        |
        |                                  | is not triggered until QT expires.        |:func:`peek_quiet_time`                       |
        +----------------------------------+-------------------------------------------+----------------------------------------------+
        | quiet-time-clear                 | The operation to clear                    |:func:`set_quiet_time_clear`                  |
        |                                  | quiet-time-out.                           |:func:`peek_quiet_time_clear`                 |
        +----------------------------------+-------------------------------------------+----------------------------------------------+
        | un-quarantine-timeout            | The un-quarantine timeout.                |:func:`set_un_quarantine_timeout`             |
        |                                  |                                           |:func:`peek_un_quarantine_timeout`            |
        +----------------------------------+-------------------------------------------+----------------------------------------------+
        | un-quarantine-clear              | The operation to clear the                |:func:`set_un_quarantine_clear`               |
        |                                  | un-quarantine-timeout.                    |:func:`peek_un_quarantine_clear`              |
        +----------------------------------+-------------------------------------------+----------------------------------------------+

    *Object Methods*

        .. staticmethod:: get(session)

            Returns a :class:`rule` object if the rule name is provided.
            Otherwise, returns all  objects of the :class:`rule`.

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A :class:`rule` object. A dictionary in case of error \
                objects if there are more than one.

        .. method:: post(session)

            Creates a MAPS rule. The required fields are set
            within the object using the attribute's set method.
            This method is used to create a new rule on a switch.

            Example Usage of the Method to Create a New Rule on a Switch

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

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary of errors or a success response.

        .. method:: patch(session)

            Updates the rule to modify threshold values, the interval of \
            monitoring, and so on.
            If a rule that is part of an active policy is changed, the
            policy must be re-activated for the rule to take effect.

            Example Usage of the Method to Update an Existing Rule on a Switch

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

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary of errors or a success response.

        .. method:: delete(session)

            Deletes a MAPS group. The required fields are
            set within the object using the attribute's
            set method.

            Example Usage of the Method to Delete a MAPS Group

            .. code-block:: python

                # initialize the object
                maps_Rule = pyfos_brocade_maps.rule()
                # set the rule name
                maps_Rule.set_name("rule1")
                # execute HTTP post command to apply the object to the
                # switch connected through session
                maps_Rule.delete(session)

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary of errors or a success response.

    *Attribute Methods*

        .. method:: set_name()

            Sets the MAPS rule name.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_name()

            Gets the MAPS rule name.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_is_rule_on_rule()

            Sets the is-rule-on-rule flag.
            This flag must be set while creating RoR rules.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_is_rule_on_rule()

            Returns the value of the RoR flag.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_monitoring_system()

            Sets the monitoring statistic.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_monitoring_system()

            Gets the monitoring statistic for the given rule.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_time_base()

            Sets the time base, which is the interval for monitoring.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_time_base()

            Gets the time base configured for the rule.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_logical_operator()

            Sets the logical operator, the condition for which \
            the threshold is met.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_logical_operator()

            Gets the condition on which the threshold is met.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_threshold_value()

            Sets the threshold value.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_threshold_value()

            Gets the threshold value configured.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_group_name()

            Sets the group name.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_group_name()

            Gets the group name.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_actions_action()

            Sets the list of actions triggered when a rule violation occurs.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_actions_action()

            Gets the list of actions triggered when rule violation occurs.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_is_predefined()

            Returns true if the rule is system-defined.
            Returns false if the rule is user-defined.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_event_severity()

            Sets the event severity. Possible values
            are "[critical | error | warning | info] | default]".

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_event_severity()

            Gets the configured event severity.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_toggle_time()

            Sets the toggle time.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_toggle_time()

            Gets the configured toggle time.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_quiet_time()

            Sets the quiet time. If the quiet time is configured, then \
            reporting of rule violations will be done only after the expiry \
            of the quiet time.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_quiet_time()

            Gets the configured quiet time.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_quiet_time_clear()

            Updates the flag to clear the quiet time.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_quiet_time_clear()

            Gets quiet time clear.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_un_quarantine_timeout()

            Sets the un-quarantine timeout value.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_un_quarantine_timeout()

            Returns the configured un-quarantine timeout value.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_un_quarantine_clear()

            Sets the un-quarantine clear.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_un_quarantine_clear()

            Returns the un-quarantine clear flag.

            :rtype: A dictionary in case of error or a success response.

    """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.rule,
                         "/rest/running/brocade-maps/rule",
                         version.VER_RANGE_821_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "name", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_KEY))

        self.add(pyfos_rest_util.rest_attribute(
            "is-rule-on-rule", pyfos_type.type_bool,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "monitoring-system", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "time-base", pyfos_type.type_str,
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
            "actions", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))

        self.add(pyfos_rest_util.rest_attribute(
            "action", pyfos_type.type_na,
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
        Manages the MAPS behavior for the switch. Use this module to \
        perform the following MAPS functions:

        1. Define the list of allowable actions that can be taken on the switch
           when a threshold is triggered.
        2. Configure  the email  address  to  which  the alerts must be \
           delivered.
        3. Delete all user-defined MAPS  configurations  related  to rules, \
           groups, policies, and so on.
        4. Display MAPS settings.

    Important Class Members:

        +------------------------------------------+-------------------------------------------+--------------------------------------------------------+
        | Attribute name                           | Description                               |Frequently used methods                                 |
        +==========================================+===========================================+========================================================+
        | actions/action                           | The global actions list.                  |:func:`set_actions_action`                              |
        |                                          |                                           |:func:`peek_actions_action`                             |
        +------------------------------------------+-------------------------------------------+--------------------------------------------------------+
        | decommission-cfg                         | The decommission behavior:                |:func:`set_decommission_cfg`                            |
        |                                          | default or impair.                        |:func:`peek_decommission_cfg`                           |
        +------------------------------------------+-------------------------------------------+--------------------------------------------------------+
        | recipient-address-list/recipient-address | The recipient email addresses.            |:func:`set_recipient_address_list_recipient_address`    |
        |                                          |                                           |:func:`peek_recipient_address_list_recipient_address`   |
        +------------------------------------------+-------------------------------------------+--------------------------------------------------------+
        | sender-address                           | The sender email address.                 |:func:`set_sender_address`                              |
        |                                          |                                           |:func:`peek_sender_address`                             |
        +------------------------------------------+-------------------------------------------+--------------------------------------------------------+
        | domain-name                              | The domain name.                          |:func:`set_domain_name`                                 |
        |                                          |                                           |:func:`peek_domain_name`                                |
        +------------------------------------------+-------------------------------------------+--------------------------------------------------------+
        | relay-ip-address                         | The relay IP address.                     |:func:`set_relay_ip_address`                            |
        |                                          |                                           |:func:`peek_relay_ip_address`                           |
        +------------------------------------------+-------------------------------------------+--------------------------------------------------------+
        | test-email/subject                       | The subject for sending test email.       |:func:`set_test_email_subject`                          |
        |                                          |                                           |:func:`peek_test_email_subject`                         |
        +------------------------------------------+-------------------------------------------+--------------------------------------------------------+
        | test-email/body                          | The body for sending test email.          |:func:`set_test_email_body`                             |
        |                                          |                                           |:func:`peek_test_email_body`                            |
        +------------------------------------------+-------------------------------------------+--------------------------------------------------------+
        | quiet-time                               | The Global Quiet Time.                    |:func:`set_quiet_time`                                  |
        |                                          |                                           |:func:`peek_quiet_time`                                 |
        +------------------------------------------+-------------------------------------------+--------------------------------------------------------+

    *Object Methods*

        .. staticmethod:: get(session)

            Returns a :class:`maps_config` object.

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A :class:`rule` object. A dictionary in case of error
                objects if there are more than one.

        .. staticmethod:: patch(session)

            Uses the PATCH operation to update any member of the maps-config \
            class.

            Example Usage of the Method

            .. code-block:: python

                # initialize the object
                maps_config_obj = pyfos_brocade_maps.maps_config()
                # set the rule name
                maps_config_obj.set_sender_address("temp1@broadcom.com")
                # patch operation
                maps_config_obj.patch(session)

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary of errors or a success response.

    *Attribute Methods*

        .. method:: set_actions_action()

            Sets the list of global actions.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_actions_action()

            Gets the list of global actions.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_decommission_cfg()

            Sets the decommission behavior: default or impair.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_decommission_cfg()

            Gets the decommission behavior: default or impair.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_recipient_address_list_recipient_address()

            Configures the recipient email address; the maximum number is 5.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_recipient_address_list_recipient_address()

            Gets the configured list of recipient email address.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_sender_address()

            Configures the sender email address.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_sender_address()

            Gets the configured sender email addresses.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_domain_name()

            Configures the domain name.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_domain_name()

            Gets the configured domain name.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_relay_ip_address()

            Configures the relay IP address.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_relay_ip_address()

            Gets the configured relay IP address.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_test_email_subject()

            Sets the subject for the test email.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_test_email_subject()

            Gets the configured subject for the test email.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_test_email_body()

            Configures the body text for the test email.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_test_email_body()

            Gets the configured body text for the test email.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_quiet_time()

            Configures the global quiet time.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_quiet_time()

            Gets the configured global quiet time.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_f_port_fpi_profile()

            Configures the F-port FPI profile name.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_f_port_fpi_profile()

            Gets the configured F-port FPI profile name.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_e_port_fpi_profile()

            Configures the E-port FPI profile name.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_e_port_fpi_profile()

            Gets the configured global quiet time.
            Gets the configured E-port FPI profile name.

            :rtype: A dictionary in case of error or a success response.

    """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.maps_config,
                         "/rest/running/brocade-maps/maps-config",
                         version.VER_RANGE_821_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "actions", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))

        self.add(pyfos_rest_util.rest_attribute(
            "action", pyfos_type.type_na,
            None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST), ["actions"])

        self.add(pyfos_rest_util.rest_attribute(
            "decommission-cfg", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "recipient-address-list", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))

        self.add(pyfos_rest_util.rest_attribute(
            "recipient-address", pyfos_type.type_na,
            None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST),
            ["recipient-address-list"])

        self.add(pyfos_rest_util.rest_attribute(
            "sender-address", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "domain-name", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "relay-ip-address", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "test-email", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))

        self.add(pyfos_rest_util.rest_attribute(
            "subject", pyfos_type.type_na,
            None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST), ["test-email"])

        self.add(pyfos_rest_util.rest_attribute(
            "test-email", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))

        self.add(pyfos_rest_util.rest_attribute(
            "body", pyfos_type.type_na,
            None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST), ["test-email"])

        self.add(pyfos_rest_util.rest_attribute(
            "quiet-time", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "f-port-fpi-profile", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "e-port-fpi-profile", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.load(dictvalues, 1)


class switch_status_policy_report(pyfos_rest_util.rest_object):
    """
        Manages the switch status policy report. Use this module to retrieve
        the SSP state. The SSP provides the overall status of the switch. \
        If the overall status is not healthy, then this module provides the \
        contributing factors.

    Important Class Members:

        +-------------------------------------+------------------------------------------+----------------------------------------------------+
        | Attribute Name                      | Description                              |Frequently Used Methods                             |
        +=====================================+==========================================+====================================================+
        | switch-health                       | The switch state. The switch health      |:func:`peek_switch_health`                          |
        |                                     | represents the switch operating health.  |                                                    |
        +-------------------------------------+------------------------------------------+----------------------------------------------------+
        | power-supply-health                 | The state of the power supplies.         |:func:`peek_power_supply_health`                    |
        |                                     |                                          |                                                    |
        +-------------------------------------+------------------------------------------+----------------------------------------------------+
        | fan-health                          | The state of the fans.                   |:func:`peek_fan_health`                             |
        |                                     |                                          |                                                    |
        +-------------------------------------+------------------------------------------+----------------------------------------------------+
        | wwn-health                          | The state of the WWNs cards.             |:func:`peek_wwn_health`                             |
        |                                     |                                          |                                                    |
        +-------------------------------------+------------------------------------------+----------------------------------------------------+
        | temperature-sensor-health           | The state of the temperature sensors.    |:func:`peek_temperature_sensor_health`              |
        |                                     |                                          |                                                    |
        +-------------------------------------+------------------------------------------+----------------------------------------------------+
        | ha-health                           | The state of the high availability       |:func:`peek_ha_health`                              |
        |                                     | state: both CPs are in sync.             |                                                    |
        +-------------------------------------+------------------------------------------+----------------------------------------------------+
        | control-processor-health            | The state of the CPs.                    |:func:`peek_control_processor_health`               |
        |                                     |                                          |                                                    |
        +-------------------------------------+------------------------------------------+----------------------------------------------------+
        | core-blade-health                   | The state of the core blades.            |:func:`peek_core_blade_health`                      |
        |                                     |                                          |                                                    |
        +-------------------------------------+------------------------------------------+----------------------------------------------------+
        | blade-health                        | The state of the AP blades.              |:func:`peek_blade_health`                           |
        |                                     |                                          |                                                    |
        +-------------------------------------+------------------------------------------+----------------------------------------------------+
        | flash-health                        | The flash usage state. Flash usage       |:func:`peek_flash_health`                           |
        |                                     | could be above the threshold or limit.   |                                                    |
        +-------------------------------------+------------------------------------------+----------------------------------------------------+
        | marginal-port-health                | The state of the marginal ports.         |:func:`peek_marginal_port_health`                   |
        |                                     |                                          |                                                    |
        +-------------------------------------+------------------------------------------+----------------------------------------------------+
        | faulty-port-health                  | The state of the faulty ports state.     |:func:`peek_faulty_port_health`                     |
        |                                     |                                          |                                                    |
        +-------------------------------------+------------------------------------------+----------------------------------------------------+
        | missing-sfp-health                  | The state of the missing SFPs state.     |:func:`peek_missing_sfp_health`                     |
        |                                     |                                          |                                                    |
        +-------------------------------------+------------------------------------------+----------------------------------------------------+
        | error-port-health                   | The state of the error ports state.      |:func:`peek_error_port_health`                      |
        |                                     |                                          |                                                    |
        +-------------------------------------+------------------------------------------+----------------------------------------------------+
        | expired-certificate-health          | The expired certificate state.           |:func:`peek_expired_certificate_health`             |
        |                                     |                                          |                                                    |
        +-------------------------------------+------------------------------------------+----------------------------------------------------+
        | airflow-mismatch-health             | The air flow mismatch state.             |:func:`peek_airflow_mismatch_health`                |
        |                                     |                                          |                                                    |
        +-------------------------------------+------------------------------------------+----------------------------------------------------+
        | marginal-sfp-health                 | The state of marginal sfps.              |:func:`peek_marginal_sfp_health`                    |
        |                                     |                                          |                                                    |
        +-------------------------------------+------------------------------------------+----------------------------------------------------+

    *Object Methods*

        .. staticmethod:: get(session)

            Returns a :class:`switch_status_policy_report` object.
            Individual attributes can be accessed through peek methods.

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A :class:`switch_status_policy_report` object. \
                    A dictionary in case of error.

    *Attribute Methods*

        .. method:: peek_switch_health()

            Reads the switch state.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_power_supply_health()

            Reads the state of the power supplies.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_fan_health()

            Reads the state of the fans.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_wwn_health()

            Reads the state of the WWNs cards.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_temperature_sensor_health()

            Reads the state of the temperature sensors.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_ha_health()

            Reads the state of the high availability (both CPs in sync).

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_control_processor_health()

            Reads the state of the CPs.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_core_blade_health()

            Reads the state of the core blades.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_blade_health()

            Reads the state of the AP blades.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_flash_health()

            Reads the flash usage state.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_marginal_port_health()

            Reads the  state of the marginal ports.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_faulty_port_health()

            Reads the  state of the faulty ports.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_missing_sfp_health()

            Reads the  state of the missing SFPs.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_error_port_health()

            Reads the  state of the error ports.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_expired_certificate_health()

            Reads the expired certificate state.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_airflow_mismatch_health()

           Reads the air flow mismatch state.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_marginal_sfp_health()

           Reads the marginal sfp's health state.

            :rtype: A dictionary in case of error or a success response.

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

        self.add(pyfos_rest_util.rest_attribute(
            "marginal-sfp-health", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.load(dictvalues, 1)


class monitoring_system_matrix(pyfos_rest_util.rest_object):
    """
        Represents the list of monitoring systems. Each monitoring stem can \
        support different time bases, actions, or thresholds. Certain \
        monitoring systems are supported on certain systems (for example, \
        circuit or tunnel monitoring systems are supported on \
        extension platforms).

    Important Class Members:

        +------------------------------------------------+-------------------------------------------+-----------------------------------------------------------+
        | Attribute Name                                 | Description                               |Frequently Used Methods                                    |
        +================================================+===========================================+===========================================================+
        | monitoring-system                              | Represents the monitoring system name.    |:func:`peek_monitoring_system`                             |
        |                                                |                                           |                                                           |
        +------------------------------------------------+-------------------------------------------+-----------------------------------------------------------+
        | dashboard-category                             | Represents the dashboard category of the  |:func:`peek_dashbroad_category`                            |
        |                                                | monitoring system.                        |                                                           |
        +------------------------------------------------+-------------------------------------------+-----------------------------------------------------------+
        | group-type                                     | Represents the group type.                |:func:`peek_group_type`                                    |
        |                                                |                                           |                                                           |
        +------------------------------------------------+-------------------------------------------+-----------------------------------------------------------+
        | base-time-bases/time-base                      | The supported time bases.                 |:func:`peek_base_time_bases_time_base`                     |
        |                                                |                                           |                                                           |
        +------------------------------------------------+-------------------------------------------+-----------------------------------------------------------+
        | rule-on-rule-time-bases/rule-on-rule-time-base | Represents supported time bases for rule  |:func:`peek_rule_on_rule_time_bases_rule_on_rule_time_base`|
        |                                                | on rules.                                 |                                                           |
        +------------------------------------------------+-------------------------------------------+-----------------------------------------------------------+
        | is-read-only                                   | True for read-only monitoring systems.    |:func:`peek_is_read_only`                                  |
        |                                                |                                           |                                                           |
        +------------------------------------------------+-------------------------------------------+-----------------------------------------------------------+
        | monitored-logical-switch                       | Monitoring can be in all the logical      |:func:`peek_monitored_logical_switch`                      |
        |                                                | switches or only in the default logical   |                                                           |
        |                                                | switch.                                   |                                                           |
        +------------------------------------------------+-------------------------------------------+-----------------------------------------------------------+
        | is-rule-on-rule-supported                      | True if rule-on-rule is supported.        |:func:`peek_is_rule_on_rule_supported`                     |
        |                                                |                                           |                                                           |
        +------------------------------------------------+-------------------------------------------+-----------------------------------------------------------+
        | is-quiet-time-supported                        | True if the quiet time feature            |:func:`peek_is_quiet_time_supported`                       |
        |                                                | is supported.                             |                                                           |
        +------------------------------------------------+-------------------------------------------+-----------------------------------------------------------+
        | minimum-quiet-time                             | Quiet time feature supported.             |:func:`peek_minimum_quiet_time`                            |
        |                                                |                                           |                                                           |
        +------------------------------------------------+-------------------------------------------+-----------------------------------------------------------+
        | monitoring-type                                | Monitoring the type of monitoring         |:func:`peek_monitoring_type`                               |
        |                                                | systems.                                  |                                                           |
        +------------------------------------------------+-------------------------------------------+-----------------------------------------------------------+
        | data-type                                      | The unit of the data.                     |:func:`peek_data_type`                                     |
        |                                                |                                           |                                                           |
        +------------------------------------------------+-------------------------------------------+-----------------------------------------------------------+
        | description                                    | Description of the monitoring system.     |:func:`peek_description`                                   |
        |                                                |                                           |                                                           |
        +------------------------------------------------+-------------------------------------------+-----------------------------------------------------------+
        | actions/action                                 | Represents the global actions list.       |:func:`peek_actions_action`                                |
        |                                                |                                           |                                                           |
        +------------------------------------------------+-------------------------------------------+-----------------------------------------------------------+
        | unit                                           | Represents the data unit.                 |:func:`peek_unit`                                          |
        |                                                |                                           |                                                           |
        +------------------------------------------------+-------------------------------------------+-----------------------------------------------------------+
        | data-range                                     | Represents the data range.                |:func:`peek_data_range`                                    |
        |                                                |                                           |                                                           |
        +------------------------------------------------+-------------------------------------------+-----------------------------------------------------------+
        | logical-operators/logical-operator             | The supported logical operator.           |:func:`peek_logical_operators_logical_operator`            |
        |                                                |                                           |                                                           |
        +------------------------------------------------+-------------------------------------------+-----------------------------------------------------------+

    *Object Methods*

        .. staticmethod:: get(session)

            Returns all :class:`monitoring_system_matrix` objects.
            Individual attributes can be accessed through peek methods.

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A :class:`monitoring_system_matrix` object. \
                    A dictionary in case of error.

    *Attribute Methods*

        .. method:: peek_monitoring_system()

            Represents the monitoring system name (CRC, SEC_LV).

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_dashboard_category()

            Represents the dashboard category of the monitoring system.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_group_type()

            Represents the group type.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_base_time_bases_time_base()

            Represents the supported time bases.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_rule_on_rule_time_bases_rule_on_rule_time_base()

            Represents the supported time bases for rule on rules.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_is_read_only()

            Returns true for read-only monitoring systems.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_monitored_logical_switch()

            Returns "all-logical-switches" if it is monitored on all \
            logical switches.
            Returns "default-switch-only" if it is monitored on the default \
            logical switch.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_is_rule_on_rule_supported()

            Returns true if the rule-on-rule is supported.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_is_quiet_time_supported()

            Returns true if the quiet time feature is supported.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_minimum_quiet_time()

            The quiet time feature is supported.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_monitoring_type()

            Returns the monitoring type of the monitoring systems.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_data_type()

            Represents the unit of the data.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_description()

            Description of the monitoring system.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_actions_action()

            Represents the global actions list.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_unit()

            Represents the data unit.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_data_range()

            Represents the data range.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_logical_operators_logical_operator()

            Returns the supported logical operator.

            :rtype: A dictionary in case of error or a success response.

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
            "time-base", pyfos_type.type_na,
            None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST),
            ["base-time-bases"])

        self.add(pyfos_rest_util.rest_attribute(
            "rule-on-rule-time-bases", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))

        self.add(pyfos_rest_util.rest_attribute(
            "rule-on-rule-time-base", pyfos_type.type_na,
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
            "action", pyfos_type.type_na,
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
            "logical-operator", pyfos_type.type_na,
            None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST),
            ["logical-operators"])

        self.load(dictvalues, 1)


class paused_cfg(pyfos_rest_util.rest_object):
    """
        This class manages the pause and continue feature of MAPS. Use this \
        module to pause monitoring of any element or group of elements.
        Manages only port, SFP, and circuits to pause or resume monitoring.

    Important Class Members:

        +-------------------------------+----------------------------------+----------------------------------------------+
        | Attribute Name                | Description                      |Frequently Used Methods                       |
        +===============================+==================================+==============================================+
        | group-type                    | Represents the group type for    |:func:`set_group_type`                        |
        |                               | pausing or resuming monitoring.  |:func:`peek_group_type`                       |
        +-------------------------------+----------------------------------+----------------------------------------------+
        | members/member                | Members for pausing or resuming  |:func:`set_members_member`                    |
        |                               | monitoring.                      |:func:`peek_members_member`                   |
        +-------------------------------+----------------------------------+----------------------------------------------+

    *Object Methods*

        .. staticmethod:: get(session)

            Returns a :class:`paused_cfg` object.
            Returns a list of all members that are currently paused \
            for monitoring.

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A :class:`paused_cfg` object. \
                    A dictionary in case of error.

        .. staticmethod:: post(session)

            Specifies the members on which to pause monitoring.
            The members can be fc-port, sfp, or circuit.

        .. staticmethod:: delete(session)

            Specifies the members on which to resume monitoring.
            The members can be fc-port, sfp, or circuit.

    *Attribute Methods*

        .. method:: set_group_type()

            Represents the group type (fc-port, sfp, or circuit).

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_group_type()

            Gets the configured group type.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_members_member()

            A list of members on which to pause or resume monitoring.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_members_member()

            Gets a list of members.

            :rtype: A dictionary in case of error or a success response.

    """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.paused_cfg,
                         "/rest/running/brocade-maps/paused-cfg",
                         version.VER_RANGE_821_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "group-type", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_KEY))

        self.add(pyfos_rest_util.rest_attribute(
            "members", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))

        self.add(pyfos_rest_util.rest_attribute(
            "member", pyfos_type.type_na,
            None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST), ["members"])

        self.load(dictvalues, 1)


class system_resources(pyfos_rest_util.rest_object):
    """
        Manages the system resources: flash, RAM, and CPU usage. Usage is not
        real time and is delayed up to 2 minutes.

    Important Class Members:

        +-------------------------------+----------------------------------+----------------------------------------------+
        | Attribute Name                | Description                      |Frequently Used Methods                       |
        +===============================+==================================+==============================================+
        | cpu-usage                     | The CPU usage.                   |:func:`peek_cpu_usage`                        |
        |                               |                                  |                                              |
        +-------------------------------+----------------------------------+----------------------------------------------+
        | memory-usage                  | The memory usage.                |:func:`peek_memory_usage`                     |
        |                               |                                  |                                              |
        +-------------------------------+----------------------------------+----------------------------------------------+
        | total-memory                  | The total memory.                |:func:`peek_total_memory`                     |
        |                               |                                  |                                              |
        +-------------------------------+----------------------------------+----------------------------------------------+
        | flash-usage                   | The flash usage.                 |:func:`peek_flash_usage`                      |
        |                               |                                  |                                              |
        +-------------------------------+----------------------------------+----------------------------------------------+

    *Object Methods*

        .. staticmethod:: get(session)

            Returns a :class:`system_resources` object.
            Returns the usage of system resources.

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A :class:`system_resources` object. \
                    A dictionary in case of error.

    *Attribute Methods*

        .. method:: peek_cpu_usage()

            Returns the CPU usage.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_memory_usage()

            Returns the memory usage.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_total_memory()

            Returns the total memory.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_flash_usage()

            Returns the flash usage.

            :rtype: A dictionary in case of error or a success response.

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
        Represents the dashboard's miscellaneous information such as start time
        and operation.

    Important Class Members:

        +-------------------------------+----------------------------------+----------------------------------------------+
        | Attribute Name                | Description                      |Frequently Used Methods                       |
        +===============================+==================================+==============================================+
        | maps-start-time               | The MAPS monitoring start time.  |:func:`peek_maps_start_time`                  |
        |                               |                                  |                                              |
        +-------------------------------+----------------------------------+----------------------------------------------+
        | clear-data                    | The operation to clear the       |:func:`set_clear_data`                        |
        |                               | dashboard data.                  |:func:`peek_clear_data`                       |
        +-------------------------------+----------------------------------+----------------------------------------------+

    *Object Methods*

        .. staticmethod:: get(session)

            Returns a :class:`dashboard_misc` object.
            Returns the dashboard miscellaneous information \
            (such as maps start time).

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A :class:`dashboard_misc` object. \
                    A dictionary in case of error.

        .. staticmethod:: patch(session)

            Clears the MAPS dashboard information when the clear data \
            attribute is set.

            :rtype: Success or a dictionary in case of error.

    *Attribute Methods*

        .. method:: peek_maps_start_time()

            Returns the monitoring start time. MAPS is a restartable service, \
            so the start time can be different than the system uptime.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_clear_data()

            Represents the operation to clear the dashboard data. True clears \
            the data and false causes no action.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_clear_data()

            Returns the value of clear data.

            :rtype: A dictionary in case of error or a success response.

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
        rules triggered and the objects on which the rules were triggered over
        a specified period of time, and to clear the  dashboard data.

        Gets a triggered rules list for the last 7 days. The rule list is
        needed to get the complete picture of switch operation. Data provides
        two views of the operating state: the state since midnight and
        the last 7 days. For both views, you must complete the details of \
        each rule triggered and all  rules data.

    Important Class Members:

        +-------------------------------+--------------------------------------+----------------------------------------------+
        | Attribute Name                | Description                          |Frequently Used Methods                       |
        +===============================+======================================+==============================================+
        | category                      | The dashboard category.              |:func:`peek_category`                         |
        |                               |                                      |                                              |
        +-------------------------------+--------------------------------------+----------------------------------------------+
        | name                          | The rule name.                       |:func:`peek_name`                             |
        |                               |                                      |                                              |
        +-------------------------------+--------------------------------------+----------------------------------------------+
        | triggered-count               | The total rule count                 |:func:`peek_triggered_count`                  |
        |                               | triggered for the category.          |                                              |
        +-------------------------------+--------------------------------------+----------------------------------------------+
        | time-stamp                    | The last triggered time.             |:func:`peek_time_stamp`                       |
        |                               |                                      |                                              |
        +-------------------------------+--------------------------------------+----------------------------------------------+
        | repetition-count              | The rule repetition count.           |:func:`peek_repetition_count`                 |
        |                               |                                      |                                              |
        +-------------------------------+--------------------------------------+----------------------------------------------+
        | objects/object                | The objects that violated the rule   |:func:`peek_objects_object`                   |
        |                               | - for example ports, circuits.       |                                              |
        +-------------------------------+--------------------------------------+----------------------------------------------+

    *Object Methods*

        .. staticmethod:: get(session)

            Returns a :class:`dashboard_rule` object.
            Returns the MAPS dashboard information, the switch summary \
            for the last 7 days, and the rule violations affecting health.

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A :class:`dashboard_rule` object. \
                    A dictionary in case of error.

    *Attribute Methods*

        .. method:: peek_category()

            Returns the dashboard category.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_name()

            Gives the rule name.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_triggered_count()

            Represents the total rule count triggered for the category.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_time_stamp()

            Represents the last triggered time.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_repetition_count()

            Represents the rule repetition count (how many times a rule has
            been triggered). The same rule can be triggered multiple times for
            the same or different objects. For example, defALL_D_PORTSCRC_10 \
            might be triggered 20 times in an hour for the same or different \
            objects--in this case repetition-count would be 20.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_objects_object()

            Represents objects that violated the rule (for example, \
            ports, circuits).

            :rtype: A dictionary in case of error or a success response.

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
            "objects", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))

        self.add(pyfos_rest_util.rest_attribute(
            "object", pyfos_type.type_na,
            None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST), ["objects"])

        self.load(dictvalues, 1)


class credit_stall_dashboard(pyfos_rest_util.rest_object):

    """
        Credit stall dashboard provides information on ports.

    Important Class Members:

        +-------------------------------+----------------------------------+----------------------------------------------+
        | Attribute Name                | Description                      |Frequently Used Methods                       |
        +===============================+==================================+==============================================+
        | slot-port                     | slot and port information in     |:func:`peek_slot_port`                        |
        |                               | slot/port format.                |                                              |
        +-------------------------------+----------------------------------+----------------------------------------------+
        | timestamp                     | timestamp of the credit-stall    |:func:`peek_timestamp`                        |
        |                               | congestion data sample.          |                                              |
        +-------------------------------+----------------------------------+----------------------------------------------+
        | state                         | state of the credit-stall        |:func:`peek_state`                            |
        |                               | congestion data sample.          |                                              |
        +-------------------------------+----------------------------------+----------------------------------------------+
        | frequency                     | number of times port is in       |:func:`peek_frequency`                        |
        |                               | congestion state for given minute|                                              |
        +-------------------------------+----------------------------------+----------------------------------------------+

    *Object Methods*

        .. staticmethod:: get(session)

            Returns a :class:`credit_stall_dashboard` object.
            Returns the credit stall dashboard information.

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A :class:`credit_stall_dashboard` object. \
                    A dictionary in case of error.

    *Attribute Methods*

        .. method:: peek_slot_port()

            Returns the slot and port information in slot/port format.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_timestamp()

            Returns the timestamp of the credit-stall congestion data sample.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_state()

            Returns the state of the credit-stall congestion data sample.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_frequency()

            Returns the number of times port is in congestion state \
            for given minute.

            :rtype: A dictionary in case of error or a success response.

    """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.credit_stall_dashboard,
                         "/rest/running/brocade-maps/credit-stall-dashboard",
                         version.VER_RANGE_900_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "slot-port", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "timestamp", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "state", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "frequency", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.load(dictvalues, 1)


class oversubscription_dashboard(pyfos_rest_util.rest_object):

    """
        oversubscription dashboard gives the details of ports which
        are oversubscribed.

    Important Class Members:

        +-------------------------------+----------------------------------+----------------------------------------------+
        | Attribute Name                | Description                      |Frequently Used Methods                       |
        +===============================+==================================+==============================================+
        | slot-port                     | slot and port information in     |:func:`peek_slot_port`                        |
        |                               | slot/port format.                |                                              |
        +-------------------------------+----------------------------------+----------------------------------------------+
        | timestamp                     | timestamp of the oversubscription|:func:`peek_timestamp`                        |
        |                               | data sample.                     |                                              |
        +-------------------------------+----------------------------------+----------------------------------------------+
        | state                         | state of the oversubscription    |:func:`peek_state`                            |
        |                               | data sample.                     |                                              |
        +-------------------------------+----------------------------------+----------------------------------------------+

    *Object Methods*

        .. staticmethod:: get(session)

            Returns a :class:`oversubscription_dashboard` object.
            Returns the oversubscription dashboard information.

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A :class:`oversubscription_dashboard` object. \
                    A dictionary in case of error.

    *Attribute Methods*

        .. method:: peek_slot_port()

            Returns the slot and port information in slot/port format.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_timestamp()

            Returns the timestamp of the oversubscription data sample.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_state()

            Returns the state of the oversubscription data sample.

            :rtype: A dictionary in case of error or a success response.

    """

    def __init__(self, dictvalues={}):
        super().__init__(
                     pyfos_rest_util.rest_obj_type.oversubscription_dashboard,
                     "/rest/running/brocade-maps/"
                     "oversubscription-dashboard",
                     version.VER_RANGE_900_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "slot-port", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "timestamp", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "state", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.load(dictvalues, 1)


class dashboard_history(pyfos_rest_util.rest_object):

    """
        The historical data of various counters.

    Important Class Members:

        +-------------------------------+----------------------------------+----------------------------------------------+
        | Attribute Name                | Description                      |Frequently Used Methods                       |
        +===============================+==================================+==============================================+
        | category                      | logical grouping of the counters |:func:`peek_category`                         |
        |                               |                                  |                                              |
        +-------------------------------+----------------------------------+----------------------------------------------+
        | date                          | Date of the day when the         |:func:`peek_date`                             |
        |                               | counters' data was cached        |                                              |
        +-------------------------------+----------------------------------+----------------------------------------------+
        | crc-errors                    | group of ports on which CRC      |:func:`peek_crc_errors`                       |
        |                               | errors were detected.            |                                              |
        +-------------------------------+----------------------------------+----------------------------------------------+
        | itw-errors                    | group of ports on which ITW      |:func:`peek_itw_errors`                       |
        |                               | errors were detected.            |                                              |
        +-------------------------------+----------------------------------+----------------------------------------------+
        | link-failure                  | group of ports on which Link     |:func:`peek_link_failure`                     |
        |                               | failure errors were detected.    |                                              |
        +-------------------------------+----------------------------------+----------------------------------------------+
        | signal-loss                   | group of ports on which signal   |:func:`peek_signal_loss`                      |
        |                               | loss errors were detected.       |                                              |
        +-------------------------------+----------------------------------+----------------------------------------------+
        | protocol-errors               | group of ports on which          |:func:`peek_protocol_errors`                  |
        |                               | protocol errors were detected.   |                                              |
        +-------------------------------+----------------------------------+----------------------------------------------+
        | state-change                  | group of ports on which state    |:func:`peek_state_change`                     |
        |                               | changes were detected.           |                                              |
        +-------------------------------+----------------------------------+----------------------------------------------+
        | link-reset                    | group of ports on which link     |:func:`peek_link_reset`                       |
        |                               | reset were detected.             |                                              |
        +-------------------------------+----------------------------------+----------------------------------------------+
        | c3-tx-to                      | group of ports on which class 3  |:func:`peek_c3_tx_to`                         |
        |                               | frame timeouts were detected.    |                                              |
        +-------------------------------+----------------------------------+----------------------------------------------+
        | rx-perf                       | list of ports sorted based on    |:func:`peek_rx_perf`                          |
        |                               | percentage of RX BW used.        |                                              |
        +-------------------------------+----------------------------------+----------------------------------------------+
        | tx-perf                       | list of ports sorted based on    |:func:`peek_tx_perf`                          |
        |                               | percentage of TX BW used.        |                                              |
        +-------------------------------+----------------------------------+----------------------------------------------+
        | utilization                   | list of ports sorted based on    |:func:`peek_utilization`                      |
        |                               | percentage of total BW (RX + TX) |                                              |
        +-------------------------------+----------------------------------+----------------------------------------------+

    *Object Methods*

        .. staticmethod:: get(session)

            Returns a :class:`dashboard_history` object.
            Returns the dashboard history information.

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A :class:`dashboard_history` object. \
                    A dictionary in case of error.

    *Attribute Methods*

        .. method:: peek_category()

            Returns the dashboard category.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_date()

            Returns Date of the day when the counters were cached.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_crc_errors()

            Returns the group of ports on which CRC errors were detected.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_itw_errors()

            Returns the group of ports on which ITW errors were detected.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_port_loss()

            Returns the port loss.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_link_failure()

            Returns the group of ports on which Link failure errors \
            were detected.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_signal_loss()

            Returns the group of ports on which signal loss errors \
            were detected.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_protocol_errors()

            Returns the group of ports on which protocol errors were \
            detected.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_state_change()

            Returns the group of ports on which state changes were \
            detected.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_link_reset()

            Returns the group of ports on which link reset were detected.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_c3_tx_to()

            Returns the group of ports on which class 3 \
            frame timeout errors were detected.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_rx_perf()

            Returns list of ports sorted based on percentage of RX BW used.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_tx_perf()

            Returns list of ports sorted based on percentage of TX BW used.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_utilization()

            Returns list of ports sorted based on percentage of total \
            BW (RX + TX).

            :rtype: A dictionary in case of error or a success response.

    """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.dashboard_history,
                         "/rest/running/brocade-maps/dashboard-history",
                         version.VER_RANGE_900_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "category", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "date", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "crc-errors", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))

        self.add(pyfos_rest_util.rest_attribute(
            "port-data", pyfos_type.type_na,
            None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST), ["crc-errors"])

        self.add(pyfos_rest_util.rest_attribute(
            "itw-errors", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))

        self.add(pyfos_rest_util.rest_attribute(
            "port-data", pyfos_type.type_na,
            None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST), ["itw-errors"])

        self.add(pyfos_rest_util.rest_attribute(
            "port-loss", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))

        self.add(pyfos_rest_util.rest_attribute(
            "port-data", pyfos_type.type_na,
            None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST), ["port-loss"])

        self.add(pyfos_rest_util.rest_attribute(
            "link-failure", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))

        self.add(pyfos_rest_util.rest_attribute(
            "port-data", pyfos_type.type_na,
            None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST), ["link-failure"])

        self.add(pyfos_rest_util.rest_attribute(
            "signal-loss", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))

        self.add(pyfos_rest_util.rest_attribute(
            "port-data", pyfos_type.type_na,
            None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST), ["signal-loss"])

        self.add(pyfos_rest_util.rest_attribute(
            "protocol-errors", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))

        self.add(pyfos_rest_util.rest_attribute(
            "port-data", pyfos_type.type_na,
            None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST),
            ["protocol-errors"])

        self.add(pyfos_rest_util.rest_attribute(
            "state-change", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))

        self.add(pyfos_rest_util.rest_attribute(
            "port-data", pyfos_type.type_na,
            None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST), ["state-change"])

        self.add(pyfos_rest_util.rest_attribute(
            "link-reset", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))

        self.add(pyfos_rest_util.rest_attribute(
            "port-data", pyfos_type.type_na,
            None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST), ["link-reset"])

        self.add(pyfos_rest_util.rest_attribute(
            "c3-tx-to", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))

        self.add(pyfos_rest_util.rest_attribute(
            "port-data", pyfos_type.type_na,
            None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST), ["c3-tx-to"])

        self.add(pyfos_rest_util.rest_attribute(
            "rx-perf", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))

        self.add(pyfos_rest_util.rest_attribute(
            "port-data", pyfos_type.type_na,
            None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST), ["rx-perf"])

        self.add(pyfos_rest_util.rest_attribute(
            "tx-perf", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))

        self.add(pyfos_rest_util.rest_attribute(
            "port-data", pyfos_type.type_na,
            None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST), ["tx-perf"])

        self.add(pyfos_rest_util.rest_attribute(
            "utilization", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))

        self.add(pyfos_rest_util.rest_attribute(
            "port-data", pyfos_type.type_na,
            None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST), ["utilization"])

        self.load(dictvalues, 1)


class fpi_profile(pyfos_rest_util.rest_object):

    """

        The FPI profile. This container enables you to create and manage
        Fabric Performance Impact monitoring thresholds. The FPI Profile
        is a set of FPI states such as performance impact, frame loss
        and thresholds for each state are Transmit Queue Latency (TXQL),
        CREDIT-ZERO buffer. The FPI rules in MAPS policy gets the thresholds
        for each state from the active FPI profile.
        The FPI profile is per logical switch.

    Important Class Members:

        +------------------------------+----------------------------+-------------------------------------------------------------+
        | Attribute Name               | Description                |Frequently Used Methods                                      |
        +==============================+============================+=============================================================+
        | name                         | FPI profile name           |:func:`peek_name`                                            |
        |                              |                            |:func:`set_name`                                             |
        +------------------------------+----------------------------+-------------------------------------------------------------+
        | predefined-profile           | whether the profile is     |:func:`peek_predefined_profile`                              |
        |                              | predefined or user defined |                                                             |
        +------------------------------+----------------------------+-------------------------------------------------------------+
        | performance-impact/          | TXQL threshold in msec     |:func:`peek_performance_impact_transmit_queue_latency`       |
        | transmit-queue-latency       |                            |:func:`set_performance_impact_transmit_queue_latency`        |
        +------------------------------+----------------------------+-------------------------------------------------------------+
        | performance-impact/          | credit-zero buffer stats   |:func:`peek_performance_impact_credit_zero_percentage_1_sec` |
        | credit-zero-percentage-1-sec | threshold % in 1-second    |:func:`set_performance_impact_credit_zero_percentage_1_sec`  |
        +------------------------------+----------------------------+-------------------------------------------------------------+
        | performance-impact/          | credit-zero buffer stats   |:func:`peek_performance_impact_credit_zero_percentage_5_sec` |
        | credit-zero-percentage-5-sec | threshold % in 5-second    |:func:`set_performance_impact_credit_zero_percentage_5_sec`  |
        +------------------------------+----------------------------+-------------------------------------------------------------+
        | performance-impact/          | credit-zero buffer stats   |:func:`peek_performance_impact_credit_zero_percentage_10_sec`|
        | credit-zero-percentage-10-sec| threshold % in 10-second   |:func:`set_performance_impact_credit_zero_percentage_10_sec` |
        +------------------------------+----------------------------+-------------------------------------------------------------+
        | frame-loss/                  | TXQL threshold in msec     |:func:`peek_frame_loss_transmit_queue_latency`               |
        | transmit-queue-latency       |                            |:func:`set_frame_loss_transmit_queue_latency`                |
        +------------------------------+----------------------------+-------------------------------------------------------------+
        | port-oversubscription/       | TX utilization in          |:func:`peek_port_oversubscription_transmit_percentage`       |
        | transmit-percentage          | percentage                 |                                                             |
        +------------------------------+----------------------------+-------------------------------------------------------------+


    *Object Methods*

        .. staticmethod:: get(session)

            Returns a :class:`fpi_profile` object.
            Returns the dashboard history information.

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A :class:`fpi_profile` object. \
                    A dictionary in case of error.

        .. method:: post(session)

            Creates an user defined FPI profile with user configured
            values for Transmit Queue Latency(TXQL) threshold in milliseconds
            or credit-zero buffer stats threshold percentage in
            1-second or 5-second or 10-second.

        .. method:: patch(session)

            Updates an user defined FPI profile with user configured
            values for Transmit Queue Latency(TXQL) threshold in milliseconds
            or credit-zero buffer stats threshold percentage in
            1-second or 5-second or 10-second.

        .. method:: delete(session)

            Deletes the FPI profile.

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary of errors or a success response.


    *Attribute Methods*

        .. method:: peek_name()

           Returns the FPI profile name.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_name()

           Configure the FPI profile name.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_predefined_profile()

            Returns Whether the profile is predefined or user-defined.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_performance_impact_transmit_queue_latency()

            Returns The Transmit Queue latency(TXQL) threshold in milliseconds.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_performance_impact_transmit_queue_latency()

            Set the Transmit Queue latency(TXQL) threshold in milliseconds.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_performance_impact_credit_zero_percentage_1_sec()

            Returns The credit-zero buffer stats threshold percentage \
            in 1-second.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_performance_impact_credit_zero_percentage_1_sec()

            Set the credit-zero buffer stats threshold percentage in 1-second.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_performance_impact_credit_zero_percentage_5_sec()

            Returns The credit-zero buffer stats threshold percentage \
            in 5-second.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_performance_impact_credit_zero_percentage_5_sec()

            Set the credit-zero buffer stats threshold percentage in 5-second.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_performance_impact_credit_zero_percentage_10_sec()

            Returns The credit-zero buffer stats threshold percentage \
            in 10-second.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_performance_impact_credit_zero_percentage_10_sec()

            Set The credit-zero buffer stats threshold percentage in 10-second.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_frame_loss_transmit_queue_latency()

            Returns The Transmit Queue Latency(TXQL) threshold in milliseconds.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_frame_loss_transmit_queue_latency()

            Set The Transmit Queue Latency(TXQL) threshold in milliseconds.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_port_oversubscription_transmit_percentage()

            Returns The Transmit(TX) utilization in percentage.

            :rtype: A dictionary in case of error or a success response.

    """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.fpi_profile,
                         "/rest/running/brocade-maps/fpi-profile",
                         version.VER_RANGE_900_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "name", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "predefined-profile", pyfos_type.type_bool,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "performance-impact", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))

        self.add(pyfos_rest_util.rest_attribute(
            "transmit-queue-latency", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG),
            ["performance-impact"])

        self.add(pyfos_rest_util.rest_attribute(
            "credit-zero-percentage-1-sec", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG),
            ["performance-impact"])

        self.add(pyfos_rest_util.rest_attribute(
            "credit-zero-percentage-5-sec", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG),
            ["performance-impact"])

        self.add(pyfos_rest_util.rest_attribute(
            "credit-zero-percentage-10-sec", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG),
            ["performance-impact"])

        self.add(pyfos_rest_util.rest_attribute(
            "frame-loss", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))

        self.add(pyfos_rest_util.rest_attribute(
            "transmit-queue-latency", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG),
            ["frame-loss"])

        self.add(pyfos_rest_util.rest_attribute(
            "port-oversubscription", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))

        self.add(pyfos_rest_util.rest_attribute(
            "transmit-percentage", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
            ["port-oversubscription"])

        self.load(dictvalues, 1)
