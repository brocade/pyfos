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

:mod:`pyfos_brocade_fabric` - PyFOS module to provide rest support for Fabric.
*********************************************************************************************************
The :mod:`pyfos_brocade_fabric` provides a REST support for Fabric.

"""

import pyfos.pyfos_rest_util as pyfos_rest_util
from pyfos.pyfos_type import pyfos_type


class fabric_switch(pyfos_rest_util.rest_object):
    """Class of fabric

    Important class members:

        +---------------------------+------------------------------+---------------------------------------+
        | Attribute name            | Description                  |Frequstly used methods                 |
        +===========================+==============================+=======================================+
        | name                      | name of switch               |:meth:`peek_name`                      |
        +---------------------------+------------------------------+---------------------------------------+
        | switch-user-friendly-name | user friendly name of switch |:meth:`peek_switch_user_friendly_name` |
        +---------------------------+------------------------------+---------------------------------------+
        | chassis-wwn               | WWN of switch                |:meth:`peek_chassis_wwn`               |
        +---------------------------+------------------------------+---------------------------------------+
        | chassis-user-friendly-name| user friendly name of chassis|:meth:`peek_chassis_user_friendly_name`|
        +---------------------------+------------------------------+---------------------------------------+
        | domain-id                 | domain id of switch          |:meth:`peek_domain_id`                 |
        +---------------------------+------------------------------+---------------------------------------+
        | principal                 | indicate if principal or not |:meth:`peek_principal`                 |
        +---------------------------+------------------------------+---------------------------------------+
        | fcid                      | FCID of switch               |:meth:`peek_fcid`                      |
        +---------------------------+------------------------------+---------------------------------------+
        | ip-address                | IPv4 address of switch       |:meth:`peek_ip_address`                |
        +---------------------------+------------------------------+---------------------------------------+
        | fcip-address              | IPv4 address of FC switch    |:meth:`peek_fcip_address`              |
        +---------------------------+------------------------------+---------------------------------------+
        | ipv6-address              | IPv6 address of switch       |:meth:`peek_ipv6_address`              |
        +---------------------------+------------------------------+---------------------------------------+
        | firmware-version          | FOS version of switch        |:meth:`peek_firmware_version`          |
        +---------------------------+------------------------------+---------------------------------------+
        | fcid-hex                  | switch FCID in hex string    |:meth:`peek_fcid_hex`                  |
        +---------------------------+------------------------------+---------------------------------------+

    *Object methods*

        .. method:: get(session)

            Returns a :class:`fabric_switch` object or a list of objects
            filled with attributes gathered throuth the session passed in.
            Each object can be printed using :func:`pyfos_util.response_print`
            and individual attributes accessed through peek methods.

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: a :class:`fabric_switch` object if there is
                only one switch within fabric or
                a list of objects if there are more than one

    *Attribute methods*

        .. method:: peek_name()

            Reads name in the object.

            :rtype: None or name of the switch

        .. method:: peek_switch_user_friendly_name()

            Reads user friendly name in the object.

            :rtype: None or user friendly name of the switch

        .. method:: peek_chassis_wwn()

            Reads chassis wwn in the object.

            :rtype: None or chassis WWN of the switch

        .. method:: peek_chassis_user_friendly_name()

            Reads chassis user frienldy name in the object.

            :rtype: None or chassis user friendnly name

        .. method:: peek_domain_id()

            Reads Domain ID in the object.

            :rtype: None or Domain ID of the switch

        .. method:: peek_principal()

            Reads boolean value of the switch being Principal or
            not in the object.

            :rtype: None, True or False

        .. method:: peek_fcid()

            Reads FCID in the object.

            :rtype: None or FCID of the switch

        .. method:: peek_ip_address()

            Reads IP address in the object.

            :rtype: None or IP address of the switch

        .. method:: peek_fcip_address()

            Reads FC IP address in the object.

            :rtype: None or FC IP address of the switch

        .. method:: peek_ipv6_address()

            Reads IPv6 address in the object.

            :rtype: None or IPv6 address of the switch

        .. method:: peek_firmware_version()

            Reads FOS firmware version in the object.

            :rtype: None or FOS firmware version of the switch

        .. method:: peek_fcid_hex()

            Reads switch FCID in hex string in the object.

            :rtype: None or FCID of the switch in hex string

        """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.fabric,
                         "/rest/running/fabric/fabric-switch")

        self.add(pyfos_rest_util.rest_attribute(
            "name", pyfos_type.type_wwn,
            None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute(
            "switch-user-friendly-name", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "chassis-wwn", pyfos_type.type_wwn,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "chassis-user-friendly-name", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "domain-id", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "principal", pyfos_type.type_bool,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "fcid", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "ip-address", pyfos_type.type_ip_addr,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "fcip-address", pyfos_type.type_ip_addr,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "ipv6-address", pyfos_type.type_ipv6_addr,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "firmware-version", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "fcid-hex", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.load(dictvalues, 1)
