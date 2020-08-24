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


# pyfos_brocade_license.py(pyGen v1.0.0)


"""

:mod:`pyfos_brocade_license` - PyFOS module for the licenses installed on\
 the switch.
******************************************************************************\
*******************************************************************************
The :mod:`pyfos_brocade_license` The PyFOS module support for the licenses\
 installed on the switch.
"""


# Start module imports
from pyfos import pyfos_rest_util
from pyfos.pyfos_type import pyfos_type
from pyfos import pyfos_version as version
# End module imports


class end_user_license_agreement(pyfos_rest_util.rest_object):

    """Class of end_user_license_agreement

    *Description end_user_license_agreement*

        Detailed view of End User License Agreement.

    Important class members of end_user_license_agreement:

        +--------------------------+---------------------------------+-------------------------------------------------+
        | Attribute Name           | Description                     |  Frequently Used Methods                        |
        +==========================+=================================+=================================================+
        | text                     | Contents of accepted Broacade   |                                                 |
        |                          | EULA (End User License          | :func:`peek_text`                               |
        |                          | Agreement).                     |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+

    *Object functions for end_user_license_agreement*

    .. function:: get()

        Get the instances of class "end_user_license_agreement from switch.
         The object can be printed using :func:`pyfos_utils.response_print`.

        :param session: The session handler returned by
         :func:`pyfos_auth.login`.

        :rtype: A dictionary of errors or a success response.


    *Class functions for end_user_license_agreement*

        .. function:: peek_text()

            Reads the value assigned to text in the object.

            :rtype: None on error and a value on success.


    """

    def __init__(self, dictvalues=None):

        clsuri = "/rest" + "/running" + "/brocade-license" +\
                 "/end-user-license-agreement"
        clstype = pyfos_rest_util.rest_obj_type.end_user_license_agreement
        clsver = version.VER_RANGE_900_and_ABOVE
        super().__init__(clstype, clsuri, clsver)

        self.add(pyfos_rest_util.rest_attribute("text", pyfos_type.type_str,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.load(dictvalues, 1)


class ports_on_demand_license_info(pyfos_rest_util.rest_object):

    """Class of ports_on_demand_license_info

    *Description ports_on_demand_license_info*

        Contains information related to ports-on-demand license reservations.

    Important class members of ports_on_demand_license_info:

        +-----------------------------------------------------+--------------------------------------------+-----------------------------------------------------------------------+
        | Attribute Name                                      | Description                                |  Frequently Used Methods                                              |
        +=====================================================+============================================+=======================================================================+
        | licensed-qsfp-port-count                            | Indicates number of QSFP ports assigned    |                                                                       |
        |                                                     | to the ports on demand license.            | :func:`peek_licensed_qsfp_port_count`                                 |
        +-----------------------------------------------------+--------------------------------------------+-----------------------------------------------------------------------+
        | port                                                | SFP-DD based port member assigned to       |                                                                       |
        |                                                     | ports-on-demand license.                   | :func:`peek_licensed_sfp_dd_port_members_port`                        |
        +-----------------------------------------------------+--------------------------------------------+-----------------------------------------------------------------------+
        | port                                                | QSFP based port member not assigned to     |                                                                       |
        |                                                     | base switch or ports on demand license.    | :func:`peek_unassigned_qsfp_port_members_port`                        |
        +-----------------------------------------------------+--------------------------------------------+-----------------------------------------------------------------------+
        | sfp-port-assigned-count                             | Total number of SFP based ports assigned   |                                                                       |
        |                                                     | to base switch allowance or installed      | :func:`peek_sfp_port_assigned_count`                                  |
        |                                                     | licenses.                                  |                                                                       |
        +-----------------------------------------------------+--------------------------------------------+-----------------------------------------------------------------------+
        | sfp-dd-count                                        | Total count of SFP Double Density (dd)     |                                                                       |
        |                                                     | based ports available on the switch.       | :func:`peek_sfp_dd_count`                                             |
        +-----------------------------------------------------+--------------------------------------------+-----------------------------------------------------------------------+
        | port                                                | Licensed SFP-DD port that is offline.      |                                                                       |
        |                                                     |                                            | :func:`peek_licensed_offline_sfp_dd_port_members_port`                |
        +-----------------------------------------------------+--------------------------------------------+-----------------------------------------------------------------------+
        | sfp-dd-port-base-switch-assigned-count              | Indicates number of SFP-DD ports           |                                                                       |
        |                                                     | assigned to base switch allowance          | :func:`peek_sfp_dd_port_base_switch_assigned_count`                   |
        +-----------------------------------------------------+--------------------------------------------+-----------------------------------------------------------------------+
        | unassigned-sfp-dd-port-members                      | Contains list of SFP-DD ports not          |                                                                       |
        |                                                     | assigned to base switch or ports on        | :func:`peek_unassigned_sfp_dd_port_members`                           |
        |                                                     | demand license.                            |                                                                       |
        +-----------------------------------------------------+--------------------------------------------+-----------------------------------------------------------------------+
        | sfp-port-license-allowance-count                    | Indicates maximum assignments              |                                                                       |
        |                                                     | provisioned by SFP based ports on demand   | :func:`peek_sfp_port_license_allowance_count`                         |
        |                                                     | license.                                   |                                                                       |
        +-----------------------------------------------------+--------------------------------------------+-----------------------------------------------------------------------+
        | licensed-sfp-dd-port-members                        | Contains list of SFP-DD ports assigned     |                                                                       |
        |                                                     | to ports-on-demand license.                | :func:`peek_licensed_sfp_dd_port_members`                             |
        +-----------------------------------------------------+--------------------------------------------+-----------------------------------------------------------------------+
        | sfp-dd-license-allowance-count                      | Indicates maximum assignments              |                                                                       |
        |                                                     | provisioned by SFP-DD ports on demand      | :func:`peek_sfp_dd_license_allowance_count`                           |
        |                                                     | license.                                   |                                                                       |
        +-----------------------------------------------------+--------------------------------------------+-----------------------------------------------------------------------+
        | licensed-sfp-dd-port-count                          | Indicates number of SFP-DD ports           |                                                                       |
        |                                                     | assigned to the ports on demand license.   | :func:`peek_licensed_sfp_dd_port_count`                               |
        +-----------------------------------------------------+--------------------------------------------+-----------------------------------------------------------------------+
        | licensed-offline-qsfp-port-members                  | Contains list of licensed QSFP ports       |                                                                       |
        |                                                     | that are offline.                          | :func:`peek_licensed_offline_qsfp_port_members`                       |
        +-----------------------------------------------------+--------------------------------------------+-----------------------------------------------------------------------+
        | sfp-port-count                                      | Total count of SFP based ports available   |                                                                       |
        |                                                     | on the switch.                             | :func:`peek_sfp_port_count`                                           |
        +-----------------------------------------------------+--------------------------------------------+-----------------------------------------------------------------------+
        | port                                                | Licensed QSFP port that is offline.        |                                                                       |
        |                                                     |                                            | :func:`peek_licensed_offline_qsfp_port_members_port`                  |
        +-----------------------------------------------------+--------------------------------------------+-----------------------------------------------------------------------+
        | sfp-dd-port-base-switch-members                     | Contains list of SFP-DD based ports        |                                                                       |
        |                                                     | assigned to base switch allowance.         | :func:`peek_sfp_dd_port_base_switch_members`                          |
        +-----------------------------------------------------+--------------------------------------------+-----------------------------------------------------------------------+
        | sfp-port-license-reservation-available-count        | Indicates license reservations available   |                                                                       |
        |                                                     | for use by unassigned SFP ports.           | :func:`peek_sfp_port_license_reservation_available_count`             |
        +-----------------------------------------------------+--------------------------------------------+-----------------------------------------------------------------------+
        | port                                                | SFP based port not assigned to base        |                                                                       |
        |                                                     | switch or port on demand license.          | :func:`peek_unassigned_sfp_port_members_port`                         |
        +-----------------------------------------------------+--------------------------------------------+-----------------------------------------------------------------------+
        | qsfp-port-base-switch-assigned-count                | Indicates number of QSFP ports assigned    |                                                                       |
        |                                                     | to base switch allowance                   | :func:`peek_qsfp_port_base_switch_assigned_count`                     |
        +-----------------------------------------------------+--------------------------------------------+-----------------------------------------------------------------------+
        | qsfp-license-allowance-count                        | Indicates maximum assignments              |                                                                       |
        |                                                     | provisioned by QSFP ports on demand        | :func:`peek_qsfp_license_allowance_count`                             |
        |                                                     | license.                                   |                                                                       |
        +-----------------------------------------------------+--------------------------------------------+-----------------------------------------------------------------------+
        | sfp-port-base-switch-allowance-count                | Indicates port assignments provisioned     |                                                                       |
        |                                                     | by base switch allowance.                  | :func:`peek_sfp_port_base_switch_allowance_count`                     |
        +-----------------------------------------------------+--------------------------------------------+-----------------------------------------------------------------------+
        | sfp-dd-port-on-demand-license                       | Specifies if Double Density (dd) ports     |                                                                       |
        |                                                     | on demand license is installed. true :     | :func:`peek_sfp_dd_port_on_demand_license`                            |
        |                                                     | Double Density ports on demand license     |                                                                       |
        |                                                     | installed. false : Double Density ports    |                                                                       |
        |                                                     | on demand license is not installed.        |                                                                       |
        +-----------------------------------------------------+--------------------------------------------+-----------------------------------------------------------------------+
        | port-on-demand-license                              | Specifies if ports on demand license is    |                                                                       |
        |                                                     | installed or not. true : Ports on demand   | :func:`peek_port_on_demand_license`                                   |
        |                                                     | license is installed. false : Ports on     |                                                                       |
        |                                                     | demand license is not installed.           |                                                                       |
        +-----------------------------------------------------+--------------------------------------------+-----------------------------------------------------------------------+
        | unassigned-sfp-port-members                         | Contains list of SFP ports not assigned    |                                                                       |
        |                                                     | to base switch or ports on demand          | :func:`peek_unassigned_sfp_port_members`                              |
        |                                                     | license.                                   |                                                                       |
        +-----------------------------------------------------+--------------------------------------------+-----------------------------------------------------------------------+
        | port                                                | SFP based port assigned to base switch     |                                                                       |
        |                                                     | allowance.                                 | :func:`peek_sfp_port_base_switch_members_port`                        |
        +-----------------------------------------------------+--------------------------------------------+-----------------------------------------------------------------------+
        | port                                                | Licensed SFP port that is offline.         |                                                                       |
        |                                                     |                                            | :func:`peek_licensed_offline_sfp_port_members_port`                   |
        +-----------------------------------------------------+--------------------------------------------+-----------------------------------------------------------------------+
        | port                                                | QSFP based port assigned to base switch    |                                                                       |
        |                                                     | allowance.                                 | :func:`peek_qsfp_port_base_switch_members_port`                       |
        +-----------------------------------------------------+--------------------------------------------+-----------------------------------------------------------------------+
        | licensed-sfp-port-members                           | Contains list of SFP ports assigned to     |                                                                       |
        |                                                     | ports-on-demand license.                   | :func:`peek_licensed_sfp_port_members`                                |
        +-----------------------------------------------------+--------------------------------------------+-----------------------------------------------------------------------+
        | qsfp-base-switch-allowance-count                    | Indicates port assignments provisioned     |                                                                       |
        |                                                     | by base switch allowance.                  | :func:`peek_qsfp_base_switch_allowance_count`                         |
        +-----------------------------------------------------+--------------------------------------------+-----------------------------------------------------------------------+
        | qsfp-port-assigned-count                            | Total number of QSFP based ports           |                                                                       |
        |                                                     | assigned to base switch allowance or       | :func:`peek_qsfp_port_assigned_count`                                 |
        |                                                     | installed licenses.                        |                                                                       |
        +-----------------------------------------------------+--------------------------------------------+-----------------------------------------------------------------------+
        | sfp-dd-port-license-reservation-available-count     | Indicates license reservations available   |                                                                       |
        |                                                     | for use by unassigned SFP-DD ports.        | :func:`peek_sfp_dd_port_license_reservation_available_count`          |
        +-----------------------------------------------------+--------------------------------------------+-----------------------------------------------------------------------+
        | sfp-dd-port-assigned-count                          | Total number of SFP-DD based ports         |                                                                       |
        |                                                     | assigned to base switch allowance or       | :func:`peek_sfp_dd_port_assigned_count`                               |
        |                                                     | installed licenses.                        |                                                                       |
        +-----------------------------------------------------+--------------------------------------------+-----------------------------------------------------------------------+
        | qsfp-port-license-reservation-available-count       | Indicates license reservations available   |                                                                       |
        |                                                     | for use by unassigned QSFP ports.          | :func:`peek_qsfp_port_license_reservation_available_count`            |
        +-----------------------------------------------------+--------------------------------------------+-----------------------------------------------------------------------+
        | port                                                | SFP-DD based port member assigned to       |                                                                       |
        |                                                     | base switch allowance.                     | :func:`peek_sfp_dd_port_base_switch_members_port`                     |
        +-----------------------------------------------------+--------------------------------------------+-----------------------------------------------------------------------+
        | qflex-port-on-demand-license                        | Specifies if Q-flex ports on demand        |                                                                       |
        |                                                     | license is installed. true : Q-flex        | :func:`peek_qflex_port_on_demand_license`                             |
        |                                                     | ports on demand license installed. false   |                                                                       |
        |                                                     | : Q-flex ports on demand license is not    |                                                                       |
        |                                                     | installed.                                 |                                                                       |
        +-----------------------------------------------------+--------------------------------------------+-----------------------------------------------------------------------+
        | qsfp-port-count                                     | Total count of QSFP based ports            |                                                                       |
        |                                                     | available on the switch.                   | :func:`peek_qsfp_port_count`                                          |
        +-----------------------------------------------------+--------------------------------------------+-----------------------------------------------------------------------+
        | licensed-offline-sfp-port-members                   | Contains list of licensed SFP ports that   |                                                                       |
        |                                                     | are offline.                               | :func:`peek_licensed_offline_sfp_port_members`                        |
        +-----------------------------------------------------+--------------------------------------------+-----------------------------------------------------------------------+
        | sfp-port-base-switch-members                        | Contains list of SFP based ports           |                                                                       |
        |                                                     | assigned to base switch allowance.         | :func:`peek_sfp_port_base_switch_members`                             |
        +-----------------------------------------------------+--------------------------------------------+-----------------------------------------------------------------------+
        | licensed-sfp-port-count                             | Indicates number of SFP ports assigned     |                                                                       |
        |                                                     | to the ports on demand license.            | :func:`peek_licensed_sfp_port_count`                                  |
        +-----------------------------------------------------+--------------------------------------------+-----------------------------------------------------------------------+
        | port                                                | SFP-DD based port member not assigned to   |                                                                       |
        |                                                     | base switch or ports on demand license.    | :func:`peek_unassigned_sfp_dd_port_members_port`                      |
        +-----------------------------------------------------+--------------------------------------------+-----------------------------------------------------------------------+
        | sfp-dd-base-switch-allowance-count                  | Indicates port assignments provisioned     |                                                                       |
        |                                                     | by base switch allowance.                  | :func:`peek_sfp_dd_base_switch_allowance_count`                       |
        +-----------------------------------------------------+--------------------------------------------+-----------------------------------------------------------------------+
        | licensed-offline-sfp-dd-port-members                | Contains list of licensed SFP-DD ports     |                                                                       |
        |                                                     | that are offline.                          | :func:`peek_licensed_offline_sfp_dd_port_members`                     |
        +-----------------------------------------------------+--------------------------------------------+-----------------------------------------------------------------------+
        | provisioned-sfp-port-count                          | Total number of SFP based ports            |                                                                       |
        |                                                     | provisioned for use in the switch.         | :func:`peek_provisioned_sfp_port_count`                               |
        +-----------------------------------------------------+--------------------------------------------+-----------------------------------------------------------------------+
        | provisioned-sfp-dd-port-count                       | Total number of SFP-DD based ports         |                                                                       |
        |                                                     | provisioned for use in the switch.         | :func:`peek_provisioned_sfp_dd_port_count`                            |
        +-----------------------------------------------------+--------------------------------------------+-----------------------------------------------------------------------+
        | sfp-port-base-switch-assigned-count                 | Indicates number of SFP ports assigned     |                                                                       |
        |                                                     | to base switch allowance.                  | :func:`peek_sfp_port_base_switch_assigned_count`                      |
        +-----------------------------------------------------+--------------------------------------------+-----------------------------------------------------------------------+
        | port                                                | SFP based port assigned to port on         |                                                                       |
        |                                                     | demand license.                            | :func:`peek_licensed_sfp_port_members_port`                           |
        +-----------------------------------------------------+--------------------------------------------+-----------------------------------------------------------------------+
        | unassigned-qsfp-port-members                        | Contains list of QSFP ports not assigned   |                                                                       |
        |                                                     | to base switch or ports on demand          | :func:`peek_unassigned_qsfp_port_members`                             |
        |                                                     | license.                                   |                                                                       |
        +-----------------------------------------------------+--------------------------------------------+-----------------------------------------------------------------------+
        | licensed-qsfp-port-members                          | Contains list of QSFP ports assigned to    |                                                                       |
        |                                                     | port on demand license.                    | :func:`peek_licensed_qsfp_port_members`                               |
        +-----------------------------------------------------+--------------------------------------------+-----------------------------------------------------------------------+
        | qsfp-port-base-switch-members                       | Contains list of QSFP based ports          |                                                                       |
        |                                                     | assigned to base switch allowance.         | :func:`peek_qsfp_port_base_switch_members`                            |
        +-----------------------------------------------------+--------------------------------------------+-----------------------------------------------------------------------+
        | port                                                | QSFP based port assigned to port on        |                                                                       |
        |                                                     | demand license.                            | :func:`peek_licensed_qsfp_port_members_port`                          |
        +-----------------------------------------------------+--------------------------------------------+-----------------------------------------------------------------------+
        | provisioned-qsfp-port-count                         | Total number of QSFP based ports           |                                                                       |
        |                                                     | provisioned for use in the switch.         | :func:`peek_provisioned_qsfp_port_count`                              |
        +-----------------------------------------------------+--------------------------------------------+-----------------------------------------------------------------------+

    *Object functions for ports_on_demand_license_info*

    .. function:: get()

        Get the instances of class "ports_on_demand_license_info from switch.
         The object can be printed using :func:`pyfos_utils.response_print`.

        :param session: The session handler returned by
         :func:`pyfos_auth.login`.

        :rtype: A dictionary of errors or a success response.


    *Class functions for ports_on_demand_license_info*

        .. function:: peek_licensed_qsfp_port_count()

            Reads the value assigned to licensed-qsfp-port-count in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_licensed_sfp_dd_port_members_port()

            Reads the value assigned to port in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_unassigned_qsfp_port_members_port()

            Reads the value assigned to port in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_sfp_port_assigned_count()

            Reads the value assigned to sfp-port-assigned-count in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_sfp_dd_count()

            Reads the value assigned to sfp-dd-count in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_licensed_offline_sfp_dd_port_members_port()

            Reads the value assigned to port in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_sfp_dd_port_base_switch_assigned_count()

            Reads the value assigned to
             sfp-dd-port-base-switch-assigned-count in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_unassigned_sfp_dd_port_members()

            Reads the value assigned to unassigned-sfp-dd-port-members in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_sfp_port_license_allowance_count()

            Reads the value assigned to sfp-port-license-allowance-count in
             the object.

            :rtype: None on error and a value on success.


        .. function:: peek_licensed_sfp_dd_port_members()

            Reads the value assigned to licensed-sfp-dd-port-members in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_sfp_dd_license_allowance_count()

            Reads the value assigned to sfp-dd-license-allowance-count in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_licensed_sfp_dd_port_count()

            Reads the value assigned to licensed-sfp-dd-port-count in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_licensed_offline_qsfp_port_members()

            Reads the value assigned to licensed-offline-qsfp-port-members in
             the object.

            :rtype: None on error and a value on success.



        .. function:: peek_sfp_port_count()

            Reads the value assigned to sfp-port-count in the object.

            :rtype: None on error and a value on success.



        .. function:: peek_licensed_offline_qsfp_port_members_port()

            Reads the value assigned to port in the object.

            :rtype: None on error and a value on success.



        .. function:: peek_sfp_dd_port_base_switch_members()

            Reads the value assigned to sfp-dd-port-base-switch-members in
             the object.

            :rtype: None on error and a value on success.


        .. function:: peek_sfp_port_license_reservation_available_count()

            Reads the value assigned to
             sfp-port-license-reservation-available-count in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_unassigned_sfp_port_members_port()

            Reads the value assigned to port in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_qsfp_port_base_switch_assigned_count()

            Reads the value assigned to qsfp-port-base-switch-assigned-count
             in the object.

            :rtype: None on error and a value on success.



        .. function:: peek_qsfp_license_allowance_count()

            Reads the value assigned to qsfp-license-allowance-count in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_sfp_port_base_switch_allowance_count()

            Reads the value assigned to sfp-port-base-switch-allowance-count
             in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_sfp_dd_port_on_demand_license()

            Reads the value assigned to sfp-dd-port-on-demand-license in the
             object.

            :rtype: None on error and a value on success.



        .. function:: peek_port_on_demand_license()

            Reads the value assigned to port-on-demand-license in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_unassigned_sfp_port_members()

            Reads the value assigned to unassigned-sfp-port-members in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_sfp_port_base_switch_members_port()

            Reads the value assigned to port in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_licensed_offline_sfp_port_members_port()

            Reads the value assigned to port in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_qsfp_port_base_switch_members_port()

            Reads the value assigned to port in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_licensed_sfp_port_members()

            Reads the value assigned to licensed-sfp-port-members in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_qsfp_base_switch_allowance_count()

            Reads the value assigned to qsfp-base-switch-allowance-count in
             the object.

            :rtype: None on error and a value on success.


        .. function:: peek_qsfp_port_assigned_count()

            Reads the value assigned to qsfp-port-assigned-count in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_sfp_dd_port_license_reservation_available_count()

            Reads the value assigned to
             sfp-dd-port-license-reservation-available-count in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_sfp_dd_port_assigned_count()

            Reads the value assigned to sfp-dd-port-assigned-count in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_qsfp_port_license_reservation_available_count()

            Reads the value assigned to
             qsfp-port-license-reservation-available-count in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_sfp_dd_port_base_switch_members_port()

            Reads the value assigned to port in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_qflex_port_on_demand_license()

            Reads the value assigned to qflex-port-on-demand-license in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_qsfp_port_count()

            Reads the value assigned to qsfp-port-count in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_licensed_offline_sfp_port_members()

            Reads the value assigned to licensed-offline-sfp-port-members in
             the object.

            :rtype: None on error and a value on success.


        .. function:: peek_sfp_port_base_switch_members()

            Reads the value assigned to sfp-port-base-switch-members in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_licensed_sfp_port_count()

            Reads the value assigned to licensed-sfp-port-count in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_unassigned_sfp_dd_port_members_port()

            Reads the value assigned to port in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_sfp_dd_base_switch_allowance_count()

            Reads the value assigned to sfp-dd-base-switch-allowance-count in
             the object.

            :rtype: None on error and a value on success.


        .. function:: peek_licensed_offline_sfp_dd_port_members()

            Reads the value assigned to licensed-offline-sfp-dd-port-members
             in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_provisioned_sfp_port_count()

            Reads the value assigned to provisioned-sfp-port-count in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_provisioned_sfp_dd_port_count()

            Reads the value assigned to provisioned-sfp-dd-port-count in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_sfp_port_base_switch_assigned_count()

            Reads the value assigned to sfp-port-base-switch-assigned-count
             in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_licensed_sfp_port_members_port()

            Reads the value assigned to port in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_unassigned_qsfp_port_members()

            Reads the value assigned to unassigned-qsfp-port-members in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_licensed_qsfp_port_members()

            Reads the value assigned to licensed-qsfp-port-members in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_qsfp_port_base_switch_members()

            Reads the value assigned to qsfp-port-base-switch-members in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_licensed_qsfp_port_members_port()

            Reads the value assigned to port in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_provisioned_qsfp_port_count()

            Reads the value assigned to provisioned-qsfp-port-count in the
             object.

            :rtype: None on error and a value on success.


    """

    def __init__(self, dictvalues=None):

        clsuri = "/rest" + "/running" + "/brocade-license" +\
                 "/ports-on-demand-license-info"
        clstype = pyfos_rest_util.rest_obj_type.ports_on_demand_license_info
        clsver = version.VER_RANGE_900_and_ABOVE
        super().__init__(clstype, clsuri, clsver)

        self.add(pyfos_rest_util.rest_attribute("licensed-qsfp-port-count",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("sfp-port-assigned-count",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("sfp-dd-count",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "sfp-dd-port-base-switch-assigned-count",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "sfp-port-license-allowance-count", pyfos_type.type_str,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "sfp-dd-license-allowance-count", pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("licensed-sfp-dd-port-count",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("sfp-port-count",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "sfp-port-license-reservation-available-count",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "qsfp-port-base-switch-assigned-count", pyfos_type.type_str,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "qsfp-license-allowance-count", pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "sfp-port-base-switch-allowance-count", pyfos_type.type_str,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "sfp-dd-port-on-demand-license", pyfos_type.type_bool, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("port-on-demand-license",
                 pyfos_type.type_bool, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "qsfp-base-switch-allowance-count", pyfos_type.type_str,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("qsfp-port-assigned-count",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "sfp-dd-port-license-reservation-available-count",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("sfp-dd-port-assigned-count",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "qsfp-port-license-reservation-available-count",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "qflex-port-on-demand-license", pyfos_type.type_bool, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("qsfp-port-count",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("licensed-sfp-port-count",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "sfp-dd-base-switch-allowance-count", pyfos_type.type_str,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("provisioned-sfp-port-count",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "provisioned-sfp-dd-port-count", pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "sfp-port-base-switch-assigned-count", pyfos_type.type_str,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("provisioned-qsfp-port-count",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "unassigned-sfp-dd-port-members", pyfos_type.type_na,
                 dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute(
                 "licensed-sfp-dd-port-members", pyfos_type.type_na, dict(),
                 pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute(
                 "licensed-offline-qsfp-port-members", pyfos_type.type_na,
                 dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute(
                 "sfp-dd-port-base-switch-members", pyfos_type.type_na,
                 dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute("unassigned-sfp-port-members",
                 pyfos_type.type_na, dict(),
                 pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute("licensed-sfp-port-members",
                 pyfos_type.type_na, dict(),
                 pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute(
                 "licensed-offline-sfp-port-members", pyfos_type.type_na,
                 dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute(
                 "sfp-port-base-switch-members", pyfos_type.type_na, dict(),
                 pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute(
                 "licensed-offline-sfp-dd-port-members", pyfos_type.type_na,
                 dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute(
                 "unassigned-qsfp-port-members", pyfos_type.type_na, dict(),
                 pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute("licensed-qsfp-port-members",
                 pyfos_type.type_na, dict(),
                 pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute(
                 "qsfp-port-base-switch-members", pyfos_type.type_na, dict(),
                 pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute("port", pyfos_type.type_na,
                 None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST),
                 ['licensed-sfp-dd-port-members'])
        self.add(pyfos_rest_util.rest_attribute("port", pyfos_type.type_na,
                 None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST),
                 ['unassigned-qsfp-port-members'])
        self.add(pyfos_rest_util.rest_attribute("port", pyfos_type.type_na,
                 None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST),
                 ['licensed-offline-sfp-dd-port-members'])
        self.add(pyfos_rest_util.rest_attribute("port", pyfos_type.type_na,
                 None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST),
                 ['licensed-offline-qsfp-port-members'])
        self.add(pyfos_rest_util.rest_attribute("port", pyfos_type.type_na,
                 None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST),
                 ['unassigned-sfp-port-members'])
        self.add(pyfos_rest_util.rest_attribute("port", pyfos_type.type_na,
                 None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST),
                 ['sfp-port-base-switch-members'])
        self.add(pyfos_rest_util.rest_attribute("port", pyfos_type.type_na,
                 None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST),
                 ['licensed-offline-sfp-port-members'])
        self.add(pyfos_rest_util.rest_attribute("port", pyfos_type.type_na,
                 None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST),
                 ['qsfp-port-base-switch-members'])
        self.add(pyfos_rest_util.rest_attribute("port", pyfos_type.type_na,
                 None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST),
                 ['sfp-dd-port-base-switch-members'])
        self.add(pyfos_rest_util.rest_attribute("port", pyfos_type.type_na,
                 None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST),
                 ['unassigned-sfp-dd-port-members'])
        self.add(pyfos_rest_util.rest_attribute("port", pyfos_type.type_na,
                 None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST),
                 ['licensed-sfp-port-members'])
        self.add(pyfos_rest_util.rest_attribute("port", pyfos_type.type_na,
                 None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST),
                 ['licensed-qsfp-port-members'])
        self.load(dictvalues, 1)


class license(pyfos_rest_util.rest_object):

    """Class of license

    *Description license*

        A list of licenses installed on the switch.

    Important class members of license:

        +-----------------------------+-----------------------------------------+--------------------------------------------------------------------+
        | Attribute Name              | Description                             |  Frequently Used Methods                                           |
        +=============================+=========================================+====================================================================+
        | features                    | A list of features that are             |                                                                    |
        |                             | integrated in a single license key      | :func:`peek_features`                                              |
        +-----------------------------+-----------------------------------------+--------------------------------------------------------------------+
        | generation-date             | The generation date for the license     |                                                                    |
        |                             | installed on the switch. The            | :func:`peek_generation_date`                                       |
        |                             | generation date for the license in      |                                                                    |
        |                             | 'MM/DD/YYYY' format. This leaf is       |                                                                    |
        |                             | valid only for serial number based      |                                                                    |
        |                             | licenses.                               |                                                                    |
        +-----------------------------+-----------------------------------------+--------------------------------------------------------------------+
        | expiration-date             | The expiration date for the license     |                                                                    |
        |                             | installed on the switch. The            | :func:`peek_expiration_date`                                       |
        |                             | expiration date for the license in      |                                                                    |
        |                             | 'MM/DD/YYYY' format. This attribute     |                                                                    |
        |                             | is displayed only when the time based   |                                                                    |
        |                             | license installed on the system.        |                                                                    |
        +-----------------------------+-----------------------------------------+--------------------------------------------------------------------+
        | consumed                    | The number of slots configured to use   |                                                                    |
        |                             | the license installed on the switch.    | :func:`peek_consumed`                                              |
        |                             | This leaf is displayed only for a       |                                                                    |
        |                             | slot-based license.                     |                                                                    |
        +-----------------------------+-----------------------------------------+--------------------------------------------------------------------+
        | feature                     | The name of the feature.                |                                                                    |
        |                             |                                         | :func:`peek_features_feature`                                      |
        +-----------------------------+-----------------------------------------+--------------------------------------------------------------------+
        | capacity                    | The capacity for the license            |                                                                    |
        |                             | installed on the switch. This           | :func:`peek_capacity`                                              |
        |                             | parameter is displayed only for a       |                                                                    |
        |                             | capacity-based license.                 |                                                                    |
        +-----------------------------+-----------------------------------------+--------------------------------------------------------------------+
        | active-firmware-version     | A human readable string identifying     |                                                                    |
        |                             | the running firmware version for the    | :func:`peek_active_firmware_version`                               |
        |                             | Trusted FOS (TruFOS) Certificate        |                                                                    |
        |                             | license installed on a switch.          |                                                                    |
        |                             | Example of running firmware version     |                                                                    |
        |                             | mentioned below.                        |                                                                    |
        |                             | '9.0.0','9.0.0+','9.0.0++','9.1.0-',    |                                                                    |
        |                             | '9.0.0--','9.0.0*,9.1.0+'               |                                                                    |
        +-----------------------------+-----------------------------------------+--------------------------------------------------------------------+
        | name                        | The representation of the license       |                                                                    |
        |                             | would be either license key or serial   | :func:`peek_name`                                                  |
        |                             | number. The license key is a string     |                                                                    |
        |                             | with alpha numeric characters and the   |                                                                    |
        |                             | License serial number is a string       |                                                                    |
        |                             | with the format of                      |                                                                    |
        |                             | 'FOS-XX-X-XX-XXXXXXXX'. Example of a    |                                                                    |
        |                             | license key and serial number           |                                                                    |
        |                             | mentioned below. License key:           |                                                                    |
        |                             | 'HP9ttZNSgmB4MCD3NmNWgQDWtAKBFtXtBSFJ   |                                                                    |
        |                             | F' Serial number:                       |                                                                    |
        |                             | 'FOS-00-0-02-11201234'                  |                                                                    |
        +-----------------------------+-----------------------------------------+--------------------------------------------------------------------+
        | target-firmware-version     | A human readable string identifying     |                                                                    |
        |                             | the target firmware version for the     | :func:`peek_target_firmware_version`                               |
        |                             | Trusted FOS (TruFOS) Certificate        |                                                                    |
        |                             | license installed on a switch.          |                                                                    |
        |                             | Example of target firmware version      |                                                                    |
        |                             | mentioned below.                        |                                                                    |
        |                             | '9.0.0','9.0.0+','9.0.0++','9.1.0-',    |                                                                    |
        |                             | '9.0.0--','9.0.0*,9.1.0+'               |                                                                    |
        +-----------------------------+-----------------------------------------+--------------------------------------------------------------------+
        | configured-blade-slot       | The configured blade slot details.      |                                                                    |
        |                             | This leaf is displayed only for a       | :func:`peek_configured_blade_slots_configured_blade_slot`          |
        |                             | slot based license.                     |                                                                    |
        +-----------------------------+-----------------------------------------+--------------------------------------------------------------------+
        | configured-blade-slots      | A list of slot numbers of the           |                                                                    |
        |                             | configured blade slots for the          | :func:`peek_configured_blade_slots`                                |
        |                             | license installed on the switch.        |                                                                    |
        +-----------------------------+-----------------------------------------+--------------------------------------------------------------------+
        | license-format              | To determine the specified license is   |                                                                    |
        |                             | certificate or key based.               | :func:`peek_license_format`                                        |
        +-----------------------------+-----------------------------------------+--------------------------------------------------------------------+

    *Object functions for license*

    .. function:: get()

        Get the instances of class "license from switch. The object can be
         printed using :func:`pyfos_utils.response_print`.

        :param session: The session handler returned by
         :func:`pyfos_auth.login`.

        :rtype: A dictionary of errors or a success response.


    *Class functions for license*

        .. function:: peek_features()

            Reads the value assigned to features in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_generation_date()

            Reads the value assigned to generation-date in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_expiration_date()

            Reads the value assigned to expiration-date in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_consumed()

            Reads the value assigned to consumed in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_features_feature()

            Reads the value assigned to feature in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_capacity()

            Reads the value assigned to capacity in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_active_firmware_version()

            Reads the value assigned to active-firmware-version in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_name()

            Reads the value assigned to name in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_target_firmware_version()

            Reads the value assigned to target-firmware-version in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_configured_blade_slots_configured_blade_slot()

            Reads the value assigned to configured-blade-slot in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_configured_blade_slots()

            Reads the value assigned to configured-blade-slots in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_license_format()

            Reads the value assigned to license-format in the
             object.

            :rtype: None on error and a value on success.

    """

    def __init__(self, dictvalues=None):

        clsuri = "/rest" + "/running" + "/brocade-license" + "/license"
        clstype = pyfos_rest_util.rest_obj_type.license
        clsver = version.VER_RANGE_821b_and_ABOVE
        super().__init__(clstype, clsuri, clsver)

        self.add(pyfos_rest_util.rest_attribute("name", pyfos_type.type_str,
                 None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute("generation-date",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG,
                 version.VER_RANGE_900_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute("expiration-date",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("consumed",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("capacity",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("active-firmware-version",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG,
                 version.VER_RANGE_900_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute("target-firmware-version",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG,
                 version.VER_RANGE_900_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute("features",
                 pyfos_type.type_na, dict(),
                 pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute("configured-blade-slots",
                 pyfos_type.type_na, dict(),
                 pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute("feature", pyfos_type.type_na,
                 None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST),
                 ['features'])
        self.add(pyfos_rest_util.rest_attribute("configured-blade-slot",
                 pyfos_type.type_na, None,
                 pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST),
                 ['configured-blade-slots'])
        self.add(pyfos_rest_util.rest_attribute("license-format",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG,
                 version.VER_RANGE_900a_and_ABOVE))
        self.load(dictvalues, 1)
