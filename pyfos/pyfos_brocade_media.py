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
        rest support for port sfp-rdp media.
****************************************************************************************************
The :mod:`pyfos_brocade_media` provides a REST support \
        for port sfp-rdp media.

"""

import pyfos.pyfos_rest_util as pyfos_rest_util
from pyfos.pyfos_type import pyfos_type
import pyfos.pyfos_version as version


class media_rdp(pyfos_rest_util.rest_object):
    """ Class of media rdp

    Important class members:

        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | Attribute name                 | Description                      |Frequstly used methods                                  |
        +================================+==================================+========================================================+
        | name                           | name of port                     |:func:`peek_name`                                       |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | identifier                     | Media identifier                 |:func:`peek_identifier`                                 |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | connector                      | Connector type of media          |:func:`peek_connector`                                  |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | media-speed-capability/speed   | Speed capability list supported  |:func:`peek_media_speed_capability_speed`               |
        |                                | by media                         |                                                        |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | media-distance/distance        | Distance list supported by       |:func:`peek_media_distance_distance`                    |
        |                                | media                            |                                                        |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | encoding                       | Encoding type of media           |:func:`peek_encoding`                                   |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | vendor-oui                     | Vendor-OUI for the media         |:func:`peek_vendor_oui`                                 |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | part-number                    | Part number of the media         |:func:`peek_part_number`                                |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | serial-number                  | Serial number of the media       |:func:`peek_serial_number`                              |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | vendor-name                    | Vendor name of the media         |:func:`peek_vendor_name`                                |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | vendor-revision                | Vendor revision of the media     |:func:`peek_vendor_revision`                            |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | date-code                      | Manufacturing date of the media  |:func:`peek_date_code`                                  |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | temperature                    | Temperature of the media         |:func:`peek_temperature`                                |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | rx-power                       | Rx-power of the media            |:func:`peek_rx_power`                                   |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | tx-power                       | Tx-power of the media            |:func:`peek_tx_power`                                   |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | current                        | Media current                    |:func:`peek_current`                                    |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | voltage                        | Media voltage                    |:func:`peek_voltage`                                    |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | wavelength                     | Media wavelength                 |:func:`peek_wavelength`                                 |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | power-on-time                  | Media power-on-time              |:func:`peek_power_on_time`                              |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-identifier              | Remote media identifier          |:func:`peek_remote_identifier`                          |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-laser-type              | Remote media laser type          |:func:`peek_remote_laser_type`                          |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-media-speed-capability/ | Speed capability list supported  |:func:`peek_remote_media_speed_capability_speed`        |
        | speed                          | by remote media                  |                                                        |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-media-temperature       | Remote media temperature         |:func:`peek_remote_media_temperature`                   |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-media-rx-power          | Remote media rx power            |:func:`peek_remote_media_rx_power`                      |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-media-tx-power          | Remote media tx power            |:func:`peek_remote_media_tx_power`                      |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-media-current           | Remote media current             |:func:`peek_remote_media_current`                       |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-media-voltage           | Remote media voltage             |:func:`peek_remote_media_voltage`                       |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-optical-product-data/   | Media part number in remote      |:func:`peek_remote_optical_product_data_part_number`    |
        | part-number                    | optical product data group       |                                                        |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-optical-product-data/   | Media serial number in remote    |:func:`peek_remote_optical_product_data_serial_number`  |
        |   serial-number                | optical product data group       |                                                        |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-optical-product-data/   | Media vendor name in remote      |:func:`peek_remote_optical_product_data_vendor_name`    |
        |   vendor-name                  | optical product data group       |                                                        |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-optical-product-data/   | Media vendor revision in remote  |:func:`peek_remote_optical_product_data_vendor_revision`|
        |   vendor-revision              | optical product data group       |                                                        |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-optical-product-data/   | Manufacturing date in remote     |:func:`peek_remote_optical_product_data_date_code`      |
        |   date-code                    | optical product data group       |                                                        |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-media-voltage-alert/    | High alarm in remote media       |:func:`peek_remote_media_voltage_alert_high_alarm`      |
        |   high-alarm                   | voltage alert group              |                                                        |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-media-voltage-alert/    | Low alarm in remote media        |:func:`peek_remote_media_voltage_alert_low_alarm`       |
        |   low-alarm                    | voltage alert group              |                                                        |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-media-voltage-alert/    | High warning in remote media     |:func:`peek_remote_media_voltage_alert_high_warning`    |
        |  high-warning                  | voltage alert group              |                                                        |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-media-voltage-alert/    | Low warning in remote media      |:func:`peek_remote_media_voltage_alert_low_warning`     |
        |   low-warning                  | voltage alert group              |                                                        |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-media-temperature-alert/| High alarm in remote media       |:func:`peek_remote_media_temperature_alert_high_alarm`  |
        |   high-alarm                   | temperature alert group          |                                                        |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-media-temperature-alert/| Low alarm in remote media        |:func:`peek_remote_media_temperature_alert_low_alarm`   |
        |   low-alarm                    | temperature alert group          |                                                        |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-media-temperature-alert/| High warning in remote media     |:func:`peek_remote_media_temperature_alert_high_warning`|
        |  high-warning                  | temperature alert group          |                                                        |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-media-temperature-alert/| Low warning in remote media      |:func:`peek_remote_media_temperature_alert_low_warning` |
        |   low-warning                  | temperature alert group          |                                                        |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-media-tx-bias-alert/    | High alarm in remote media       |:func:`peek_remote_media_tx_bias_alert_high_alarm`      |
        |   high-alarm                   | tx-bias alert group              |                                                        |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-media-tx-bias-alert/    | Low alarm in remote media        |:func:`peek_remote_media_tx_bias_alert_low_alarm`       |
        |   low-alarm                    | tx-bias alert group              |                                                        |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-media-tx-bias-alert/    | High warning in remote media     |:func:`peek_remote_media_tx_bias_alert_high_warning`    |
        |  high-warning                  | tx-bias alert group              |                                                        |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-media-tx-bias-alert/    | Low warning in remote media      |:func:`peek_remote_media_tx_bias_alert_low_warning`     |
        |   low-warning                  | tx-bias alert group              |                                                        |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-media-tx-power-alert/   | High alarm in remote media       |:func:`peek_remote_media_tx_power_alert_high_alarm`     |
        |   high-alarm                   | tx-power alert group             |                                                        |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-media-tx-power-alert/   | Low alarm in remote media        |:func:`peek_remote_media_tx_power_alert_low_alarm`      |
        |   low-alarm                    | tx-power alert group             |                                                        |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-media-tx-power-alert/   | High warning in remote media     |:func:`peek_remote_media_tx_power_alert_high_warning`   |
        |  high-warning                  | tx-power alert group             |                                                        |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-media-tx-power-alert/   | Low warning in remote media      |:func:`peek_remote_media_tx_power_alert_low_warning`    |
        |   low-warning                  | tx-power alert group             |                                                        |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-media-rx-power-alert/   | High alarm in remote media       |:func:`peek_remote_media_rx_power_alert_high_alarm`     |
        |   high-alarm                   | rx-power alert group             |                                                        |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-media-rx-power-alert/   | Low alarm in remote media        |:func:`peek_remote_media_rx_power_alert_low_alarm`      |
        |   low-alarm                    | rx-power alert group             |                                                        |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-media-rx-power-alert/   | High warning in remote media     |:func:`peek_remote_media_rx_power_alert_high_warning`   |
        |  high-warning                  | rx-power alert group             |                                                        |
        +--------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-media-rx-power-alert/   | Low warning in remote media      |:func:`peek_remote_media_rx_power_alert_low_warning`    |
        |   low-warning                  | rx-power alert group             |                                                        |
        +--------------------------------+----------------------------------+--------------------------------------------------------+

    *Object methods*

        .. method:: get(session, name=None)

            Returns a :class:`media_rdp` object or a list of
            objects filled with attributes gathered
            from port media. If optional name is given, either an
            object matching the name of the port is returned
            or an empty object is returned with the corresponding
            error if no match is found.

            Each object can be printed using :func:`pyfos_util.response_print`
            and individual attributes accessed
            through peek methods.

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :param name: Interface slot port details in the form of
                         interface/slot/port
            :rtype: a :class:`media_rdp` object if name is
                given or a list of objects if there are more than one

    *Attribute methods*

        .. method:: peek_name()

            Reads port name in the object.

            :rtype: None or port name

        .. method:: peek_identifier()

            Reads media identifier.

            :rtype: None or identifier

        .. method:: peek_connector()

            Reads connector type of the media.

            :rtype: None or connector type
        .. method:: peek_media_speed_capability_speed()

            Reads list of speeds media capable

            :rtype: None or list of speeds
        .. method:: peek_media_distance_distance()

            Reads list of distance media supports

            :rtype: None or list of distance
        .. method:: peek_encoding()

            Reads encoding supports type of media.

            :rtype: None or encoding type

        .. method:: peek_vendor_oui()

            Reads vendor oui of the media.

            :rtype: None or vendor oui

        .. method:: peek_part_number()

            Reads part number of the media.

            :rtype: None or part number

        .. method:: peek_serial_number()

            Reads serial number of the media.

            :rtype: None or serial number

        .. method:: peek_vendor_name()

            Reads vendor name of the media.

            :rtype: None or vendor name

        .. method:: peek_vendor_revision()

            Reads vendor revision of the media.

            :rtype: None or vendor revision

        .. method:: peek_date_code()

            Reads Manufacturing date of the media.

            :rtype: None or manufacturing date code

        .. method:: peek_temperature()

            Reads temperature of the media.

            :rtype: None or temperature

        .. method:: peek_tx_power()

            Reads tx power of the media.

            :rtype: None or tx power

        .. method:: peek_rx_power()

            Reads rx power of the media.

            :rtype: None or rx power

        .. method:: peek_current()

            Reads media current.

            :rtype: None or current

        .. method:: peek_voltage()

            Reads media voltage.

            :rtype: None or voltage

        .. method:: peek_wavelength()

            Reads media wavelength.

            :rtype: None or wavelength

        .. method:: peek_power_on_time()

            Reads media power on time.

            :rtype: None or power on time

        .. method:: peek_remote_identifier()

            Reads remote media identifier.

            :rtype: None or remote identifier
        .. method:: peek_remote_laser_type()

            Reads remote media laser type.

            :rtype: None or laser type
        .. method:: peek_remote_media_speed_capability_speed()

            Reads list of speeds remote media capable

            :rtype: None or laser type
        .. method:: peek_remote_media_temperature()

            Reads remote media temperature.

            :rtype: None or temperature
        .. method:: peek_remote_media_tx_power()

            Reads tx power of the remote media.

            :rtype: None or tx power

        .. method:: peek_remote_media_rx_power()

            Reads rx power of the remote media.

            :rtype: None or rx power

        .. method:: peek_remote_media_current()

            Reads remote media current.

            :rtype: None or current

        .. method:: peek_remote_media_voltage()

            Reads remote media voltage.

            :rtype: None or voltage

        .. method:: peek_remote_optical_product_data_part_number()

            Reads remote media part number.

            :rtype: None or part number

        .. method:: peek_remote_optical_product_data_serial_number()

            Reads remote media serial number.

            :rtype: None or serial number

        .. method:: peek_remote_optical_product_data_vendor_name()

            Reads remote media vendor name.

            :rtype: None or vendor name

        .. method:: peek_remote_optical_product_data_vendor_revision()

            Reads remote media vendor revision.

            :rtype: None or vendor revision

        .. method:: peek_remote_optical_product_data_date_code()

            Reads remote media manufacturing date.

            :rtype: None or date code

        .. method:: peek_remote_media_voltage_alert_high_alarm()

            Reads high alarm in the voltage alert object

            :rtype: None or high alarm

        .. method:: peek_remote_media_voltage_alert_low_alarm()

            Reads low alarm in the voltage alert object

            :rtype: None or low alarm

        .. method:: peek_remote_media_voltage_alert_high_warning()

            Reads high warning in the voltage alert object

            :rtype: None or high warning

        .. method:: peek_remote_media_voltage_alert_low_warning()

            Reads low warning in the voltage alert object

            :rtype: None or low warning

        .. method:: peek_remote_media_temperature_alert_high_alarm()

            Reads high alarm in the temperature alert object

            :rtype: None or high alarm

        .. method:: peek_remote_media_temperature_alert_low_alarm()

            Reads low alarm in the temperature alert object

            :rtype: None or low alarm

        .. method:: peek_remote_media_temperature_alert_high_warning()

            Reads high warning in the temperature alert object

            :rtype: None or high warning

        .. method:: peek_remote_media_temperature_alert_low_warning()

            Reads low warning in the temperature alert object

            :rtype: None or low warning

        .. method:: peek_remote_media_tx_bias_alert_high_alarm()

            Reads high alarm in the tx bias alert object

            :rtype: None or high alarm

        .. method:: peek_remote_media_tx_bias_alert_low_alarm()

            Reads low alarm in the tx bias alert object

            :rtype: None or low alarm

        .. method:: peek_remote_media_tx_bias_alert_high_warning()

            Reads high warning in the tx bias alert object

            :rtype: None or high warning

        .. method:: peek_remote_media_tx_bias_alert_low_warning()

            Reads low warning in the tx bias alert object

            :rtype: None or low warning

        .. method:: peek_remote_media_tx_power_alert_high_alarm()

            Reads high alarm in the tx power alert object

            :rtype: None or high alarm

        .. method:: peek_remote_media_tx_power_alert_low_alarm()

            Reads low alarm in the tx power alert object

            :rtype: None or low alarm

        .. method:: peek_remote_media_tx_power_alert_high_warning()

            Reads high warning in the tx power alert object

            :rtype: None or high warning

        .. method:: peek_remote_media_tx_power_alert_low_warning()

            Reads low warning in the tx power alert object

            :rtype: None or low warning

        .. method:: peek_remote_media_rx_power_alert_high_alarm()

            Reads high alarm in the rx power alert object

            :rtype: None or high alarm

        .. method:: peek_remote_media_rx_power_alert_low_alarm()

            Reads low alarm in the rx power alert object

            :rtype: None or low alarm

        .. method:: peek_remote_media_rx_power_alert_high_warning()

            Reads high warning in the rx power alert object

            :rtype: None or high warning

        .. method:: peek_remote_media_rx_power_alert_low_warning()

            Reads low warning in the rx power alert object

            :rtype: None or low warning

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
