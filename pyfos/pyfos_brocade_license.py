
# Copyright 2018 Brocade Communications Systems, Inc.  All rights reserved.
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

:mod:`pyfos_brocade_license` - PyFOS module to provide rest support for\
Licenses installed on the specific switch in the fabric.
**************************************************************************\
**************************************************************************
The :mod:`pyfos_brocade_license` provides the REST support for License.

"""

from pyfos import pyfos_rest_util
from pyfos.pyfos_type import pyfos_type
import pyfos.pyfos_version as version


# pylint: disable=W0622
class license(pyfos_rest_util.rest_object):
    """Class of licenses installed on a switch

    Important class members:


        +---------------------------+------------------------------+----------------------------------------------------------+
        | Attribute name            | Description                  |Frequently used methods                                   |
        +===========================+==============================+==========================================================+
        | name                      | The license key for one or   |:meth:`peek_name`                                         |
        |                           | morefeatures installed on    |                                                          |
        |                           | the switch                   |                                                          |
        +---------------------------+------------------------------+----------------------------------------------------------+
        | features/feature          | The list of features that    |:meth:`peek_features_feature`                             |
        |                           | that are integrated in a     |                                                          |
        |                           | single license key           |                                                          |
        +---------------------------+------------------------------+----------------------------------------------------------+
        | capacity                  | The capacity of the license  |:meth:`peek_capacity`                                     |
        |                           | installed on the switch.This |                                                          |
        |                           | field is displayed  only for |                                                          |
        |                           | the capacity based license   |                                                          |
        |                           | in the output.               |                                                          |
        +---------------------------+------------------------------+----------------------------------------------------------+
        | consumed                  | The number of consumed slots |:meth:`peek_consumed`                                     |
        |                           | of the license installed     |                                                          |
        |                           | on the switch.               |                                                          |
        +---------------------------+------------------------------+----------------------------------------------------------+
        | configured-blade-slots/   | The list of Configured Blade |:meth:`peek_configured_blade_slots_configured_blade_slot` |
        | configured-blade-slot     | Slots of the specific license|                                                          |
        |                           | installed on the switch.     |                                                          |
        +---------------------------+------------------------------+----------------------------------------------------------+
        | expiration-date           | The expiry date of the       |:meth:`peek_expiration_date`                              |
        |                           | specific license installed   |                                                          |
        |                           | on the system.               |                                                          |
        |                           | the format of the date       |                                                          |
        |                           | is 'MM/DD/YYYY'.             |                                                          |
        +---------------------------+------------------------------+----------------------------------------------------------+

    *Object methods*

        .. classmethod:: get(session)

            Returns a :class:`license` object filled with attributes
            gathered throuth the session passed in. Each object can be printed
            using :func:`pyfos_util.response_print` and individual attributes
            accessed through peek methods.

            :param session: session handler returned by
                :func:`utils.brcd_util.getsession`
            :rtype: a :class:`license` object

    *Attribute methods*


        .. method:: peek_name()

            Reads the license key string from the license Object

            :rtype: None on error and value on success


        .. method:: peek_features_feature()

            Reads the list of features from the license Object

            :rtype: None on error and value on success


        .. method:: peek_capacity()

            Reads the capacity from the license Object

            :rtype: None on error and value on success


        .. method:: peek_consumed()

            Reads the consumed slots from the license Object

            :rtype: None on error and value on success


        .. method:: peek_configured_blade_slots_configured_blade_slot()

            Reads the configured blade slots from the license Object

            :rtype: None on error and value on success


        .. method:: peek_expiration_date()

            Reads the expiration date from the license Object

            :rtype: None on error and value on success

    """
    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.license,
                         "/rest/running/brocade-license/license",
                         version.VER_RANGE_821b_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute("name",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute("features",
                 pyfos_type.type_na, dict(),
                 pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute("feature",
                 pyfos_type.type_na, None,
                 pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST), ["features"])
        self.add(pyfos_rest_util.rest_attribute("capacity",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("consumed",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("configured-blade-slots",
                 pyfos_type.type_na, dict(),
                 pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute("configured-blade-slot",
                 pyfos_type.type_na, None,
                 pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST),
                 ["configured-blade-slots"])
        self.add(pyfos_rest_util.rest_attribute("expiration-date",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.load(dictvalues, 1)
