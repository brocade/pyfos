# Copyright 2017 Brocade Communications Systems LLC.  All rights reserved.
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

:mod:`pyfos_brocade_media` - PyFOS module to provide \
        REST support for port sfp-rdp media.
****************************************************************************************************
The :mod:`pyfos_brocade_media` module provides REST support \
for port sfp-rdp media.
"""


from pyfos import pyfos_rest_util
from pyfos.pyfos_type import pyfos_type
import pyfos.pyfos_version as version


class media_rdp(pyfos_rest_util.rest_object):
    """ Class of Media rdp

    Important Class Members:

        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | Attribute Name                 | Description                      |Frequently Used Methods                                 |
        +================================+==================================+========================================================+
        | name                           | The name of the port.            |:func:`peek_name`                                       |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | identifier                     | The media identifier.            |:func:`peek_identifier`                                 |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | connector                      | The connector type of the media. |:func:`peek_connector`                                  |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | media-speed-capability/speed   | The speed capability list        |:func:`peek_media_speed_capability_speed`               |
        |                                | supported by the media.          |                                                        |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | media-distance/distance        | The distance list supported by   |:func:`peek_media_distance_distance`                    |
        |                                | the media.                       |                                                        |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | encoding                       | The encoding type of the media.  |:func:`peek_encoding`                                   |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | vendor-oui                     | The vendor OUI for the media.    |:func:`peek_vendor_oui`                                 |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | part-number                    | The part number of the media.    |:func:`peek_part_number`                                |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | serial-number                  | The serial number of the media.  |:func:`peek_serial_number`                              |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | vendor-name                    | The vendor name of the media.    |:func:`peek_vendor_name`                                |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | vendor-revision                | The vendor revision of the media.|:func:`peek_vendor_revision`                            |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | date-code                      | Manufacturing date of            |:func:`peek_date_code`                                  |
        |                                | the media.                       |                                                        |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | temperature                    |The temperature of the media.     |:func:`peek_temperature`                                |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | rx-power                       | The rx power of the media.       |:func:`peek_rx_power`                                   |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | tx-power                       | The tx power of the media.       |:func:`peek_tx_power`                                   |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | current                        | The media current.               |:func:`peek_current`                                    |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | voltage                        | The media voltage.               |:func:`peek_voltage`                                    |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | wavelength                     | The media wavelength.            |:func:`peek_wavelength`                                 |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | power-on-time                  | The media power-on time.         |:func:`peek_power_on_time`                              |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-identifier              | The remote media identifier.     |:func:`peek_remote_identifier`                          |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-laser-type              | The remote media laser type.     |:func:`peek_remote_laser_type`                          |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-media-speed-capability/ | The speed capability list        |:func:`peek_remote_media_speed_capability_speed`        |
        | speed                          | supported by the remote media.   |                                                        |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-media-temperature       | The remote media temperature.    |:func:`peek_remote_media_temperature`                   |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-media-rx-power          | The remote media rx power.       |:func:`peek_remote_media_rx_power`                      |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-media-tx-power          | The remote media tx power.       |:func:`peek_remote_media_tx_power`                      |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-media-current           | The remote media current.        |:func:`peek_remote_media_current`                       |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-media-voltage           | The remote media voltage.        |:func:`peek_remote_media_voltage`                       |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-optical-product-data/   | Media part number in the remote  |:func:`peek_remote_optical_product_data_part_number`    |
        | part-number                    | optical product data group.      |                                                        |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-optical-product-data/   |Media serial number in the remote |:func:`peek_remote_optical_product_data_serial_number`  |
        | serial-number                  | optical product data group.      |                                                        |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-optical-product-data/   | Media vendor name in the remote  |:func:`peek_remote_optical_product_data_vendor_name`    |
        |   vendor-name                  | optical product data group.      |                                                        |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-optical-product-data/   | Media vendor revision in the     |:func:`peek_remote_optical_product_data_vendor_revision`|
        | vendor-revision              | remote optical product data group. |                                                        |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-optical-product-data/   | Manufacturing date in the remote |:func:`peek_remote_optical_product_data_date_code`      |
        |   date-code                    | optical product data group.      |                                                        |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-media-voltage-alert/    | High alarm in the remote media   |:func:`peek_remote_media_voltage_alert_high_alarm`      |
        |   high-alarm                   | voltage alert group.             |                                                        |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-media-voltage-alert/    | Low alarm in the remote media    |:func:`peek_remote_media_voltage_alert_low_alarm`       |
        |   low-alarm                    | voltage alert group.             |                                                        |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-media-voltage-alert/    | High warning in the remote media |:func:`peek_remote_media_voltage_alert_high_warning`    |
        |  high-warning                  | voltage alert group.             |                                                        |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-media-voltage-alert/    | Low warning in the remote media  |:func:`peek_remote_media_voltage_alert_low_warning`     |
        |   low-warning                  | voltage alert group.             |                                                        |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-media-temperature-alert/| High alarm in the remote media   |:func:`peek_remote_media_temperature_alert_high_alarm`  |
        |   high-alarm                   | temperature alert group.         |                                                        |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-media-temperature-alert/| Low alarm in the remote media    |:func:`peek_remote_media_temperature_alert_low_alarm`   |
        |   low-alarm                    | temperature alert group.         |                                                        |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-media-temperature-alert/| High warning in the remote media |:func:`peek_remote_media_temperature_alert_high_warning`|
        |  high-warning                  | temperature alert group.         |                                                        |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-media-temperature-alert/| Low warning in the remote media  |:func:`peek_remote_media_temperature_alert_low_warning` |
        |   low-warning                  | temperature alert group.         |                                                        |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-media-tx-bias-alert/    | High alarm in the remote media   |:func:`peek_remote_media_tx_bias_alert_high_alarm`      |
        |   high-alarm                   | tx bias alert group.             |                                                        |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-media-tx-bias-alert/    | Low alarm in the remote media    |:func:`peek_remote_media_tx_bias_alert_low_alarm`       |
        |   low-alarm                    | tx bias alert group.             |                                                        |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-media-tx-bias-alert/    | High warning in the remote media |:func:`peek_remote_media_tx_bias_alert_high_warning`    |
        |  high-warning                  | tx bias alert group.             |                                                        |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-media-tx-bias-alert/    | Low warning in the remote media  |:func:`peek_remote_media_tx_bias_alert_low_warning`     |
        |   low-warning                  | tx bias alert group.             |                                                        |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-media-tx-power-alert/   | High alarm in the remote media   |:func:`peek_remote_media_tx_power_alert_high_alarm`     |
        |   high-alarm                   | tx power alert group.            |                                                        |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-media-tx-power-alert/   | Low alarm in the remote media    |:func:`peek_remote_media_tx_power_alert_low_alarm`      |
        |   low-alarm                    | tx power alert group.            |                                                        |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-media-tx-power-alert/   | High warning in the remote media |:func:`peek_remote_media_tx_power_alert_high_warning`   |
        |  high-warning                  | tx power alert group.            |                                                        |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-media-tx-power-alert/   | Low warning in the remote media  |:func:`peek_remote_media_tx_power_alert_low_warning`    |
        |   low-warning                  | tx power alert group.            |                                                        |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-media-rx-power-alert/   | High alarm in the remote media   |:func:`peek_remote_media_rx_power_alert_high_alarm`     |
        |   high-alarm                   | rx power alert group.            |                                                        |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-media-rx-power-alert/   | Low alarm in the remote media    |:func:`peek_remote_media_rx_power_alert_low_alarm`      |
        |   low-alarm                    | rx power alert group.            |                                                        |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-media-rx-power-alert/   | High warning in the remote media |:func:`peek_remote_media_rx_power_alert_high_warning`   |
        |  high-warning                  | rx power alert group.            |                                                        |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-media-rx-power-alert/   | Low warning in the remote media  |:func:`peek_remote_media_rx_power_alert_low_warning`    |
        |   low-warning                  | rx power alert group.            |                                                        |
        +--------------------------------+----------------------------------+--------------------------------------------------------+

    *Object Methods*

        .. method:: get(session, name=None)

            Returns a :class:`media_rdp` object or a list of
            objects with the attributes gathered
            from port media. If an optional name is given, returns either an
            object matching the name of the port
            or an empty object with the corresponding
            error if no match is found.

            Each object can be printed using :func:`pyfos_util.response_print`,
            and individual attributes can be accessed
            through peek methods.

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :param name: The interface slot port details in the format of
                         interface/slot/port.
            :rtype: A :class:`media_rdp` object if the name is
                provided or a list of objects if there is more than one.

    *Attribute Methods*

        .. method:: peek_name()

            Reads the port name in the object.

            :rtype: None or the port name.

        .. method:: peek_identifier()

            Reads the media identifier.

            :rtype: None or the identifier.

        .. method:: peek_connector()

            Reads the connector type of the media.

            :rtype: None or the connector type.

        .. method:: peek_media_speed_capability_speed()

            Reads a list of supported speed capabilities of the media.

            :rtype: None or a list of speeds.

        .. method:: peek_media_distance_distance()

            Reads a list of distance media support.

            :rtype: None or a list of distance media.

        .. method:: peek_encoding()

            Reads the supported encoding type of the media.

            :rtype: None or the encoding type.

        .. method:: peek_vendor_oui()

            Reads the vendor OUI of the media.

            :rtype: None or the vendor OUI.

        .. method:: peek_part_number()

            Reads the part number of the media.

            :rtype: None or the part number.

        .. method:: peek_serial_number()

            Reads the serial number of the media.

            :rtype: None or the serial number.

        .. method:: peek_vendor_name()

            Reads the vendor name of the media.

            :rtype: None or the vendor name.

        .. method:: peek_vendor_revision()

            Reads the vendor revision of the media.

            :rtype: None or the vendor revision.

        .. method:: peek_date_code()

            Reads the manufacturing date of the media.

            :rtype: None or the manufacturing date code.

        .. method:: peek_temperature()

            Reads the temperature of the media.

            :rtype: None or the temperature.

        .. method:: peek_tx_power()

            Reads the tx power of the media.

            :rtype: None or the tx power.

        .. method:: peek_rx_power()

            Reads the rx power of the media.

            :rtype: None or the rx power.

        .. method:: peek_current()

            Reads the media current.

            :rtype: None or the current.

        .. method:: peek_voltage()

            Reads the media voltage.

            :rtype: None or the voltage.

        .. method:: peek_wavelength()

            Reads the media wavelength.

            :rtype: None or the wavelength.

        .. method:: peek_power_on_time()

            Reads the media power on time.

            :rtype: None or the power on time.

        .. method:: peek_remote_identifier()

            Reads the remote media identifier.

            :rtype: None or the remote identifier.

        .. method:: peek_remote_laser_type()

            Reads the remote media laser type.

            :rtype: None or the laser type.

        .. method:: peek_remote_media_speed_capability_speed()

            Reads a list of remote media capable speeds.

            :rtype: None or the laser type.

        .. method:: peek_remote_media_temperature()

            Reads the remote media temperature.

            :rtype: None or the temperature.

        .. method:: peek_remote_media_tx_power()

            Reads the tx power of the remote media.

            :rtype: None or the tx power.

        .. method:: peek_remote_media_rx_power()

            Reads the rx power of the remote media.

            :rtype: None or the rx power.

        .. method:: peek_remote_media_current()

            Reads the remote media current.

            :rtype: None or the current.

        .. method:: peek_remote_media_voltage()

            Reads the remote media voltage.

            :rtype: None or the voltage.

        .. method:: peek_remote_optical_product_data_part_number()

            Reads the remote media part number.

            :rtype: None or the part number.

        .. method:: peek_remote_optical_product_data_serial_number()

            Reads the remote media serial number.

            :rtype: None or the serial number.

        .. method:: peek_remote_optical_product_data_vendor_name()

            Reads the remote media vendor name.

            :rtype: None or the vendor name.

        .. method:: peek_remote_optical_product_data_vendor_revision()

            Reads the remote media vendor revision.

            :rtype: None or the vendor revision.

        .. method:: peek_remote_optical_product_data_date_code()

            Reads the remote media manufacturing date.

            :rtype: None or the date code.

        .. method:: peek_remote_media_voltage_alert_high_alarm()

            Reads the high alarm in the voltage alert object.

            :rtype: None or the high alarm.

        .. method:: peek_remote_media_voltage_alert_low_alarm()

            Reads the low alarm in the voltage alert object.

            :rtype: None or the low alarm.

        .. method:: peek_remote_media_voltage_alert_high_warning()

            Reads the high warning in the voltage alert object.

            :rtype: None or the high warning.

        .. method:: peek_remote_media_voltage_alert_low_warning()

            Reads the low warning in the voltage alert object.

            :rtype: None or the low warning.

        .. method:: peek_remote_media_temperature_alert_high_alarm()

            Reads the high alarm in the temperature alert object.

            :rtype: None or the high alarm.

        .. method:: peek_remote_media_temperature_alert_low_alarm()

            Reads the low alarm in the temperature alert object.

            :rtype: None or the low alarm.

        .. method:: peek_remote_media_temperature_alert_high_warning()

            Reads the high warning in the temperature alert object.

            :rtype: None or the high warning.

        .. method:: peek_remote_media_temperature_alert_low_warning()

            Reads the low warning in the temperature alert object.

            :rtype: None or the low warning.

        .. method:: peek_remote_media_tx_bias_alert_high_alarm()

            Reads the high alarm in the tx bias alert object.

            :rtype: None or the high alarm

        .. method:: peek_remote_media_tx_bias_alert_low_alarm()

            Reads the low alarm in the tx bias alert object.

            :rtype: None or the low alarm.

        .. method:: peek_remote_media_tx_bias_alert_high_warning()

            Reads the high warning in the tx bias alert object.

            :rtype: None or the high warning.

        .. method:: peek_remote_media_tx_bias_alert_low_warning()

            Reads the low warning in the tx bias alert object.

            :rtype: None or the low warning.

        .. method:: peek_remote_media_tx_power_alert_high_alarm()

            Reads the high alarm in the tx power alert object.

            :rtype: None or the high alarm.

        .. method:: peek_remote_media_tx_power_alert_low_alarm()

            Reads the low alarm in the tx power alert object.

            :rtype: None or the low alarm.

        .. method:: peek_remote_media_tx_power_alert_high_warning()

            Reads the high warning in the tx power alert object.

            :rtype: None or the high warning.

        .. method:: peek_remote_media_tx_power_alert_low_warning()

            Reads the low warning in the tx power alert object.

            :rtype: None or the low warning.

        .. method:: peek_remote_media_rx_power_alert_high_alarm()

            Reads the high alarm in the rx power alert object.

            :rtype: None or the high alarm.

        .. method:: peek_remote_media_rx_power_alert_low_alarm()

            Reads the low alarm in the rx power alert object.

            :rtype: None or the low alarm.

        .. method:: peek_remote_media_rx_power_alert_high_warning()

            Reads the high warning in the rx power alert object.

            :rtype: None or the high warning.

        .. method:: peek_remote_media_rx_power_alert_low_warning()

            Reads the low warning in the rx power alert object.

            :rtype: None or the low warning.
    """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.media_rdp,
                         "/rest/running/brocade-media/media-rdp",
                         version.VER_RANGE_821_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
                 "name", pyfos_type.type_str,
                 None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute(
                 "identifier", pyfos_type.type_str,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "connector", pyfos_type.type_str,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "media-speed-capability", pyfos_type.type_na,
                 dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute(
                 "speed", pyfos_type.type_na,
                 None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST),
                 ["media-speed-capability"])
        self.add(pyfos_rest_util.rest_attribute(
                 "media-distance", pyfos_type.type_na,
                 dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute(
                 "distance", pyfos_type.type_na,
                 None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST),
                 ["media-distance"])
        self.add(pyfos_rest_util.rest_attribute(
                 "encoding", pyfos_type.type_str,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "vendor-oui", pyfos_type.type_str,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "part-number", pyfos_type.type_str,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "serial-number", pyfos_type.type_str,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "vendor-name", pyfos_type.type_str,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "vendor-revision", pyfos_type.type_str,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "date-code", pyfos_type.type_str,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "temperature", pyfos_type.type_int,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "rx-power", pyfos_type.type_float,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "tx-power", pyfos_type.type_float,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "current", pyfos_type.type_float,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "voltage", pyfos_type.type_float,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "wavelength", pyfos_type.type_int,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "power-on-time", pyfos_type.type_int,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "remote-identifier", pyfos_type.type_str,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "remote-laser-type", pyfos_type.type_str,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "remote-media-speed-capability", pyfos_type.type_na,
                 dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute(
                 "speed", pyfos_type.type_na,
                 None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST),
                 ["remote-media-speed-capability"])
        self.add(pyfos_rest_util.rest_attribute(
                 "remote-media-temperature", pyfos_type.type_int,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "remote-media-rx-power", pyfos_type.type_float,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "remote-media-tx-power", pyfos_type.type_float,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "remote-media-current", pyfos_type.type_float,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "remote-media-voltage", pyfos_type.type_float,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "remote-optical-product-data", pyfos_type.type_na,
                 dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute(
                 "part-number", pyfos_type.type_str,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
                 ["remote-optical-product-data"])
        self.add(pyfos_rest_util.rest_attribute(
                 "serial-number", pyfos_type.type_str,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
                 ["remote-optical-product-data"])
        self.add(pyfos_rest_util.rest_attribute(
                 "vendor-name", pyfos_type.type_str,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
                 ["remote-optical-product-data"])
        self.add(pyfos_rest_util.rest_attribute(
                 "vendor-revision", pyfos_type.type_str,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
                 ["remote-optical-product-data"])
        self.add(pyfos_rest_util.rest_attribute(
                 "date-code", pyfos_type.type_str,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
                 ["remote-optical-product-data"])
        self.add(pyfos_rest_util.rest_attribute(
                 "remote-media-voltage-alert", pyfos_type.type_na,
                 dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute(
                 "high-alarm", pyfos_type.type_int,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
                 ["remote-media-voltage-alert"])
        self.add(pyfos_rest_util.rest_attribute(
                 "low-alarm", pyfos_type.type_int,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
                 ["remote-media-voltage-alert"])
        self.add(pyfos_rest_util.rest_attribute(
                 "high-warning", pyfos_type.type_int,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
                 ["remote-media-voltage-alert"])
        self.add(pyfos_rest_util.rest_attribute(
                 "low-warning", pyfos_type.type_int,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
                 ["remote-media-voltage-alert"])
        self.add(pyfos_rest_util.rest_attribute(
                 "remote-media-temperature-alert", pyfos_type.type_na,
                 dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute(
                 "high-alarm", pyfos_type.type_int,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
                 ["remote-media-temperature-alert"])
        self.add(pyfos_rest_util.rest_attribute(
                 "low-alarm", pyfos_type.type_int,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
                 ["remote-media-temperature-alert"])
        self.add(pyfos_rest_util.rest_attribute(
                 "high-warning", pyfos_type.type_int,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
                 ["remote-media-temperature-alert"])
        self.add(pyfos_rest_util.rest_attribute(
                 "low-warning", pyfos_type.type_int,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
                 ["remote-media-temperature-alert"])
        self.add(pyfos_rest_util.rest_attribute(
                 "remote-media-tx-bias-alert", pyfos_type.type_na,
                 dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute(
                 "high-alarm", pyfos_type.type_int,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
                 ["remote-media-tx-bias-alert"])
        self.add(pyfos_rest_util.rest_attribute(
                 "low-alarm", pyfos_type.type_int,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
                 ["remote-media-tx-bias-alert"])
        self.add(pyfos_rest_util.rest_attribute(
                 "high-warning", pyfos_type.type_int,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
                 ["remote-media-tx-bias-alert"])
        self.add(pyfos_rest_util.rest_attribute(
                 "low-warning", pyfos_type.type_int,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
                 ["remote-media-tx-bias-alert"])
        self.add(pyfos_rest_util.rest_attribute(
                 "remote-media-tx-power-alert", pyfos_type.type_na,
                 dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute(
                 "high-alarm", pyfos_type.type_int,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
                 ["remote-media-tx-power-alert"])
        self.add(pyfos_rest_util.rest_attribute(
                 "low-alarm", pyfos_type.type_int,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
                 ["remote-media-tx-power-alert"])
        self.add(pyfos_rest_util.rest_attribute(
                 "high-warning", pyfos_type.type_int,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
                 ["remote-media-tx-power-alert"])
        self.add(pyfos_rest_util.rest_attribute(
                 "low-warning", pyfos_type.type_int,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
                 ["remote-media-tx-power-alert"])
        self.add(pyfos_rest_util.rest_attribute(
                 "remote-media-rx-power-alert", pyfos_type.type_na,
                 dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute(
                 "high-alarm", pyfos_type.type_int,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
                 ["remote-media-rx-power-alert"])
        self.add(pyfos_rest_util.rest_attribute(
                 "low-alarm", pyfos_type.type_int,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
                 ["remote-media-rx-power-alert"])
        self.add(pyfos_rest_util.rest_attribute(
                 "high-warning", pyfos_type.type_int,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
                 ["remote-media-rx-power-alert"])
        self.add(pyfos_rest_util.rest_attribute(
                 "low-warning", pyfos_type.type_int,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
                 ["remote-media-rx-power-alert"])

        self.load(dictvalues, 1)
