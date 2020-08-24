# Copyright 2018 Brocade Communications Systems LLC. All rights reserved.
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

    :mod:`pyfos_brocade_chassis` - PyFOS module to provide REST \
    support for Chassis objects.
    **********************************************************************************************
    The :mod:`pyfos_brocade_chassis` provides a REST support for \
     Chassis objects.

"""

from pyfos import pyfos_rest_util
from pyfos.pyfos_type import pyfos_type
import pyfos.pyfos_version as version


class chassis(pyfos_rest_util.rest_object):
    """This class provides information of the Chassis

    Important class members:

        +-----------------------------+-------------------------------+----------------------------------------+
        | Attribute name              | Description                   |Frequently used methods                 |
        +=============================+===============================+========================================+
        | chassis-user-friendly-name  | user friendly name of chassis |:meth:`set_chassis_user_friendly_name`  |
        |                             |                               |:meth:`peek_chassis_user_friendly_name` |
        +-----------------------------+-------------------------------+----------------------------------------+
        | chassis-wwn                 | WWN of chassis                |:meth:`peek_chassis_wwn`                |
        +-----------------------------+-------------------------------+----------------------------------------+
        | license-id                  | License ID of chassis         |:meth:`peek_license_id`                 |
        +-----------------------------+-------------------------------+----------------------------------------+
        | serial-number               | Serial number of chassis      |:meth:`peek_serial_number`              |
        +-----------------------------+-------------------------------+----------------------------------------+
        | manufacturer                | Manufacturer of chassis       |:meth:`peek_manufacturer`               |
        +-----------------------------+-------------------------------+----------------------------------------+
        | part-number                 | Part number of chassis        |:meth:`peek_part_number`                |
        +-----------------------------+-------------------------------+----------------------------------------+
        | max-blades-supported        | Maximum number of blades      |:meth:`peek_max_blades_supported`       |
        |                             | supported by chassis          |                                        |
        +-----------------------------+-------------------------------+----------------------------------------+
        | vendor-serial-number        | Externally supplied serial    |:meth:`peek_vendor_serial_number`       |
        |                             | number of chassis             |                                        |
        +-----------------------------+-------------------------------+----------------------------------------+
        | vendor-part-number          | Externally supplied part      |:meth:`peek_vendor_part_number`         |
        |                             | number of chassis             |                                        |
        +-----------------------------+-------------------------------+----------------------------------------+
        | product-name                | Name by which chassis is      |:meth:`peek_product_name`               |
        |                             | generally known               |                                        |
        +-----------------------------+-------------------------------+----------------------------------------+
        | vendor-revision-number      | supplier revision number      |:meth:`peek_vendor_revision_number`     |
        +-----------------------------+-------------------------------+----------------------------------------+
        | vf-enabled                  | VF enabled or disabled state  |:meth:`set_vf_enabled`                  |
        |                             |                               |:meth:`peek_vf_enabled`                 |
        +-----------------------------+-------------------------------+----------------------------------------+
        | vf-supported                | VF supported or not           |:meth:`peek_vf_supported`               |
        +-----------------------------+-------------------------------+----------------------------------------+
        | fcr-enabled                 | FCR enabled or disabled state |:meth:`set_fcr_enabled`                 |
        |                             |                               |:meth:`peek_fcr_enabled`                |
        +-----------------------------+-------------------------------+----------------------------------------+
        | fcr-supported               | FCR supported or not          |:meth:`peek_fcr_supported`              |
        +-----------------------------+-------------------------------+----------------------------------------+


    *Object methods*

        .. classmethod:: get(session)

            Returns a :class:`chassis` object filled with values for all
            the attributes obtained using the session passed in.

            Each object can be printed using :func:`pyfos_util.response_print`
            and individual attributes accessed through peek methods.

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary of error or
                :class:`chassis` object

        .. method:: patch(session)

            Replace entry members. Fields involved are set within the object
            using attribute's set method. This command is used to
            set the chassis name.

            Example usage of the method to set the chassis user friendly name:

            .. code-block:: python

                chassis_obj = pyfos_brocade_chassis.chassis()
                chassis_obj.set_chassis_user_friendly_name(name)
                chassis_obj.set_vf_enabled(true)
                chassis_obj.patch(session)

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary of error or success response

    *Attribute methods*

    .. method:: set_chassis_user_friendly_name(name)

        Sets chassis user friendly name in the object.

        :param name: user friendly name of the chassis
        :rtype: None or dictionary of error information

    .. method:: peek_chassis_user_friendly_name()

        Reads user friendly name from the object.

        :rtype: None or user friendly name of the chassis

    .. method:: peek_chassis_wwn()

        Reads chassis WWN from the object.

        :rtype: None or chassis WWN

    .. method:: peek_license_id()

        Reads License ID from the object.

        :rtype: None or License ID

    .. method:: peek_serial_number()

        Reads serial number from the object.

        :rtype: None or serial number of the Chassis

    .. method:: peek_manufacturer()

        Reads manufacturer from the object.

        :rtype: None or manufacturer of the Chassis

    .. method:: peek_part_number()

        Reads part number from the object.

        :rtype: None or part number of the Chassis

    .. method:: peek_max_blades_supported()

        Reads maximum number of blades supported from the object.

        :rtype: None or maximum number of blades supported

    .. method:: peek_vendor_serial_number()

        Reads vendor serial number from the object.

        :rtype: None or vendor serial number of the Chassis

    .. method:: peek_vendor_part_number()

        Reads vendor part number from the object.

        :rtype: None or vendor part number of the Chassis

    .. method:: peek_vendor_revision_number()

        Reads vendor revision number from the object.

        :rtype: None or vendor revision number of the Chassis

    .. method:: peek_product_name()

        Reads product name from the object.

        :rtype: None or product name of the Chassis

    .. method:: set_vf_enabled(newstate)

        Sets VF enabled state of the chassis in the object.

        :param newstate: VF enabled state of the chassis
        :rtype: None or dictionary of error information

    .. method:: peek_vf_enabled()

        Reads VF enabled state of the chassis in the object.

        :rtype: None or VF enabled state of the chassis

    .. method:: peek_vf_supported()

        Reads VF supported state of the chassis in the object.

        :rtype: None or VF supported state of the chassis

    .. method:: set_fcr_enabled(value)

        Sets the value of fcr-enabled in the object.

        :rtype: A dictionary of error or a success response and
         a value with "fcr-enabled" as the key

    .. method:: peek_fcr_enabled()

        Reads the value assigned to fcr-enabled in the object.

        :rtype: None on error and a value on success.

    .. method:: peek_fcr_supported()

        Reads the value assigned to fcr-supported in the object.

        :rtype: None on error and a value on success.

    """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.chassis_show,
                         "/rest/running/brocade-chassis/chassis",
                         version.VER_RANGE_821_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "chassis-user-friendly-name", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "chassis-wwn", pyfos_type.type_wwn,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "license-id", pyfos_type.type_wwn,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "serial-number", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "manufacturer", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "part-number", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "max-blades-supported", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "vendor-serial-number", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "vendor-part-number", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "vendor-revision-number", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "product-name", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "vf-enabled", pyfos_type.type_bool,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "vf-supported", pyfos_type.type_bool,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "fcr-enabled", pyfos_type.type_bool,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "fcr-supported", pyfos_type.type_bool,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.load(dictvalues, 1)


class ha_status(pyfos_rest_util.rest_object):
    """Class of Chassis

    Important class members:

        +------------------+-------------------+------------------------------+
        | Attribute name   | Description       |Frequently used methods       |
        +==================+===================+==============================+
        | active-cp        | Active CP id      |:meth:`peek_active_cp`        |
        +------------------+-------------------+------------------------------+
        | standby-cp       | Standby CP id     |:meth:`peek_standby_cp`       |
        +------------------+-------------------+------------------------------+
        | active-slot      | Active slot number|:meth:`peek_active_slot`      |
        +------------------+-------------------+------------------------------+
        | standby-slot     | Standby slot      |:meth:`peek_standby_slot`     |
        |                  | number            |                              |
        +------------------+-------------------+------------------------------+
        | recovery-type    | Warm/Cold Recovery|:meth:`peek_recovery_type`    |
        +------------------+-------------------+------------------------------+
        | recovery-complete| Recovery progress |:meth:`peek_recovery_complete`|
        |                  | status            |                              |
        +------------------+-------------------+------------------------------+
        | standby-health   | Health status of  |:meth:`peek_standby_health`   |
        |                  | standby CP        |                              |
        +------------------+-------------------+------------------------------+
        | ha-enabled       | HA enabled status |:meth:`peek_ha_enabled`       |
        +------------------+-------------------+------------------------------+
        | heartbeat-up     | Heartbeat between |:meth:`peek_heartbeat_up`     |
        |                  | CP is up or down  |                              |
        +------------------+-------------------+------------------------------+
        | ha-synchronized  | HA synchronization|:meth:`peek_ha_synchronized`  |
        |                  | status            |                              |
        +------------------+-------------------+------------------------------+

    *Object methods*

    .. method:: get(session)

        Return :class:`ha_status`

        object or a list of objects filled with attributes.

        Each object can be printed using :func:`pyfos_util.response_print`
        and individual attributes accessed through peek methods.

    *Attribute functions*

    .. function:: peek_active_cp()

        Reads details about Active CP from the object.

        :rtype: None on error and value on success

    .. function:: peek_standby_cp()

        Reads details about Standby CP from the object.

        :rtype: None on error and value on success

    .. function:: peek_active_slot()
        Reads details about Active CP from the object.

        :rtype: None on error and value on success

    .. function:: peek_standby_slot()
        Reads details about Active CP slot from the object.

        :rtype: None on error and value on success

    .. function:: peek_recovery_type()

        Reads recovery type cold/warm from the object.

        :rtype: None on error and value on success

    .. function:: peek_recovery_complete()

        Reads recovery completion status from the object.

        :rtype: None on error and value on success

    .. function:: peek_standby_health()

        Reads standby health status from the object.

        :rtype: None on error and value on success

    .. function:: peek_ha_enabled()

        Reads HA enabled status from the object.

        :rtype: None on error and value on success

    .. function:: peek_heartbeat_up()

        Reads heartbeat status from the object.

        :rtype: None on error and value on success

    .. function:: peek_ha_synchronized()

        Reads HA Synchronization status from the object.

        :rtype: None on error and value on success
    """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.chassis_ha,
                         "/rest/running/brocade-chassis/ha-status",
                         version.VER_RANGE_821_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute("active-cp",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("standby-cp",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("active-slot",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("standby-slot",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("recovery-type",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("recovery-complete",
                 pyfos_type.type_bool, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("standby-health",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("ha-enabled",
                 pyfos_type.type_bool, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("heartbeat-up",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("ha-synchronized",
                 pyfos_type.type_bool, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.load(dictvalues, 1)
