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

:mod:`pyfos_brocade_extension_tunnel` - PyFOS module for Extension Tunnel.
*******************************************************************************
The :mod:`pyfos_extension_tunnel` provides a REST support for
Extension Tunnel objects.
"""
import pyfos.pyfos_rest_util as pyfos_rest_util
from pyfos.pyfos_type import pyfos_type


class extension_tunnel(pyfos_rest_util.rest_object):
    """Class of extension_tunnel

    Important class members:

        +-------------------------------+-------------------------------+-------------------------------------------------+
        | Attribute name                | Description                   |Frequently used functions                        |
        +===============================+===============================+=================================================+
        | name                          | The slot/port name of VE port |:func:`peek_name`                                |
        +-------------------------------+-------------------------------+-------------------------------------------------+
        | name                          | The slot/port name of VE port |:func:`set_name`                                 |
        +-------------------------------+-------------------------------+-------------------------------------------------+
        | admin-enabled                 | The admin enabled tnl state   |:func:`peek_admin_enabled`                       |
        +-------------------------------+-------------------------------+-------------------------------------------------+
        | admin-enabled                 | The admin enabled tnl state   |:func:`set_admin_enabled`                        |
        +-------------------------------+-------------------------------+-------------------------------------------------+
        | fast-write-enabled            | fastwrite enabled             |:func:`peek_fast_write_enabled`                  |
        +-------------------------------+-------------------------------+-------------------------------------------------+
        | fast-write-enabled            | fast-write-enabled            |:func:`set_fast_write_enabled`                   |
        +-------------------------------+-------------------------------+-------------------------------------------------+
        | tape-read                     | tape read                     |:func:`peek_tape_read`                           |
        +-------------------------------+-------------------------------+-------------------------------------------------+
        | tape-read                     | tape-read                     |:func:`set_tape_read`                            |
        +-------------------------------+-------------------------------+-------------------------------------------------+
        | tape-write                    | Tape Write pipelining         |:func:`peek_tape_write`                          |
        +-------------------------------+-------------------------------+-------------------------------------------------+
        | tape-write                    | Tape Write pipelining         |:func:`set_tape_write`                           |
        +-------------------------------+-------------------------------+-------------------------------------------------+
        | tunnel-status                 | The tunnel status             |:func:`peek_tunnel_status`                       |
        +-------------------------------+-------------------------------+-------------------------------------------------+
        | ipsec-enabled                 | IPSEC is enabled flag         |:func:`peek_ipsec_enabled`                       |
        +-------------------------------+-------------------------------+-------------------------------------------------+
        | ipsec-policy                  | IPsec Policy for tunnel       |:func:`peek_ipsec_policy`                        |
        +-------------------------------+-------------------------------+-------------------------------------------------+
        | ipsec-policy                  | IPsec Policy for tunnel       |:func:`set_ipsec_policy`                         |
        +-------------------------------+-------------------------------+-------------------------------------------------+
        | ha-operational-status         | HA operational status of tnl  |:func:`peek_ha_operational_status`               |
        +-------------------------------+-------------------------------+-------------------------------------------------+
        | ip-extension                  | IPEXT Enable/Disable flag     |:func:`peek_ip_extension`                        |
        +-------------------------------+-------------------------------+-------------------------------------------------+
        | ip-extension                  | IPEXT Enable/Disable flag     |:func:`set_ip_extension`                         |
        +-------------------------------+-------------------------------+-------------------------------------------------+
        | load-level                    | The configured load level     |:func:`peek_load_level`                          |
        +-------------------------------+-------------------------------+-------------------------------------------------+
        | load-level                    | The configured load level     |:func:`set_load_level`                           |
        +-------------------------------+-------------------------------+-------------------------------------------------+
        | active-load-level             | negotiated load level         |:func:`peek_active_load_level`                   |
        +-------------------------------+-------------------------------+-------------------------------------------------+
        | peer-load-level               | Peer load level               |:func:`peek_peer_load_level`                     |
        +-------------------------------+-------------------------------+-------------------------------------------------+
        | compression-tunnel            | tunnel compressioon value     |:func:`peek_compression_tunnel`                  |
        +-------------------------------+-------------------------------+-------------------------------------------------+
        | compression-tunnel            | tunnel compression value      |:func:`set_compression_tunnel`                   |
        +-------------------------------+-------------------------------+-------------------------------------------------+
        | compression-protocol          | The protocl compression value |:func:`peek_compression_protocol`                |
        +-------------------------------+-------------------------------+-------------------------------------------------+
        | compression-protocol          | The protcol compression value |:func:`set_compression_protocol`                 |
        +-------------------------------+-------------------------------+-------------------------------------------------+
        | fc-compression                | FC protcol compression value  |:func:`peek_compression_protocol_fc_compression` |
        +-------------------------------+-------------------------------+-------------------------------------------------+
        | fc-compression                | FC protcol compression value  |:func:`set_compression_protocol_fc_compression`  |
        +-------------------------------+-------------------------------+-------------------------------------------------+
        | ip-compression                | IP protcol compression value  |:func:`peek_compression_protocol_ip_compression` |
        +-------------------------------+-------------------------------+-------------------------------------------------+
        | ip-compression                | IP protcol compression value  |:func:`set_compression_protocol_ip_compression`  |
        +-------------------------------+-------------------------------+-------------------------------------------------+
        | qos-ratio                     | QOS ratio                     |:func:`peek_qos_ratio`                           |
        +-------------------------------+-------------------------------+-------------------------------------------------+
        | qos-ratio                     | QOS ratio                     |:func:`set_qos_ratio`                            |
        +-------------------------------+-------------------------------+-------------------------------------------------+
        | distribution                  | the QOS distribution          |:func:`peek_qos_ratio_distribution`              |
        +-------------------------------+-------------------------------+-------------------------------------------------+
        | distribution                  | The QOS distribution          |:func:`set_qos_ratio_distribution`               |
        +-------------------------------+-------------------------------+-------------------------------------------------+
        | distribution-value            | The distribution Vlaue        |:func:`peek_qos_ratio_distribution_value`        |
        +-------------------------------+-------------------------------+-------------------------------------------------+
        | distribution-value            | The distribution Vlaue        |:func:`set_qos_ratio_distribution_value`         |
        +-------------------------------+-------------------------------+-------------------------------------------------+
        | fc-high-qos                   | FC QOS High                   |:func:`peek_qos_ratio_fc_high_qos`               |
        +-------------------------------+-------------------------------+-------------------------------------------------+
        | fc-high-qos                   | FC QOS High                   |:func:`set_qos_ratio_fc_high_qos`                |
        +-------------------------------+-------------------------------+-------------------------------------------------+
        | fc-medium-qos                 | FC QOS High                   |:func:`peek_qos_ratio_fc_medium_qos`             |
        +-------------------------------+-------------------------------+-------------------------------------------------+
        | fc-medium-qos                 | FC QOS Medium                 |:func:`set_qos_ratio_fc_medium_qos`              |
        +-------------------------------+-------------------------------+-------------------------------------------------+
        | fc-low-qos                    | FC QOS Low                    |:func:`peek_qos_ratio_fc_low_qos`                |
        +-------------------------------+-------------------------------+-------------------------------------------------+
        | fc-low-qos                    | FC QOS Low                    |:func:`set_qos_ratio_fc_low_qos`                 |
        +-------------------------------+-------------------------------+-------------------------------------------------+
        | ip-high-qos                   | IP QOS High                   |:func:`peek_qos_ratio_ip_high_qos`               |
        +-------------------------------+-------------------------------+-------------------------------------------------+
        | ip-high-qos                   | IP QOS High                   |:func:`set_qos_ratio_ip_high_qos`                |
        +-------------------------------+-------------------------------+-------------------------------------------------+
        | ip-medium-qos                 | IP QOS Medium                 |:func:`peek_qos_ratio_ip_medium_qos`             |
        +-------------------------------+-------------------------------+-------------------------------------------------+
        | ip-medium-qos                 | IP QOS Medium                 |:func:`set_qos_ratio_ip_medium_qos`              |
        +-------------------------------+-------------------------------+-------------------------------------------------+
        | ip-low-qos                    | IP QOS Low                    |:func:`peek_qos_ratio_ip_low_qos`                |
        +-------------------------------+-------------------------------+-------------------------------------------------+
        | ip-low-qos                    | IP QOS LOw                    |:func:`set_qos_ratio_ip_low_qos`                 |
        +-------------------------------+-------------------------------+-------------------------------------------------+

    Important FICON class members:

        +----------------------------------------+-------------------------------+-------------------------------------------------------+
        | Attribute name                         | Description                   | Frequently used functions                             |
        +========================================+===============================+=======================================================+
        | ficon                                  | The FICON options             |:func:`peek_ficon`                                     |
        +----------------------------------------+-------------------------------+-------------------------------------------------------+
        | ficon-xrc-acceleration                 | The FICON options             |:func:`peek_ficon_xrc_acceleration`                    |
        +----------------------------------------+-------------------------------+-------------------------------------------------------+
        | ficon-tape-read-acceleration           | The FICON options             |:func:`peek_ficon_tape_read_acceleration`              |
        +----------------------------------------+-------------------------------+-------------------------------------------------------+
        | ficon-tape-write-acceleration          | The FICON options             |:func:`peek_ficon_tape_write_acceleration`             |
        +----------------------------------------+-------------------------------+-------------------------------------------------------+
        | ficon-tin-tir-emulation                | The FICON options             |:func:`peek_ficon_tin_tir_emulation`                   |
        +----------------------------------------+-------------------------------+-------------------------------------------------------+
        | ficon-device-acknowledgement-emulation | The FICON options             |:func:`peek_ficon_device_acknowledgement_emulation`    |
        +----------------------------------------+-------------------------------+-------------------------------------------------------+
        | ficon-teradata-read-acceleration       | The FICON options             |:func:`peek_ficon_teradata_read_acceleration`          |
        +----------------------------------------+-------------------------------+-------------------------------------------------------+
        | ficon-teradata-write-acceleration      | The FICON options             |:func:`peek_ficon_teradata_write_acceleration`         |
        +----------------------------------------+-------------------------------+-------------------------------------------------------+
        | ficon-tape-write-max-pipe              | The FICON options             |:func:`peek_ficon_tape_write_max_pipe`                 |
        +----------------------------------------+-------------------------------+-------------------------------------------------------+
        | ficon-tape-read-max-pipe               | The FICON options             |:func:`peek_ficon_tape_read_max_pipe`                  |
        +----------------------------------------+-------------------------------+-------------------------------------------------------+
        | ficon-tape-read-max-devices            | The FICON options             |:func:`peek_ficon_tape_read_max_devices`               |
        +----------------------------------------+-------------------------------+-------------------------------------------------------+
        | ficon-tape-write-max-devices           | The FICON options             |:func:`peek_ficon_tape_write_max_devices`              |
        +----------------------------------------+-------------------------------+-------------------------------------------------------+
        | ficon-tape-write-timer                 | The FICON options             |:func:`peek_ficon_tape_write_timer`                    |
        +----------------------------------------+-------------------------------+-------------------------------------------------------+
        | ficon-tape-write-max-chain             | The FICON options             |:func:`peek_ficon_tape_write_max_chain`                |
        +----------------------------------------+-------------------------------+-------------------------------------------------------+
        | ficon-oxid-base                        | The FICON options             |:func:`peek_ficon_oxid_base`                           |
        +----------------------------------------+-------------------------------+-------------------------------------------------------+
        | ficon                                  | The FICON options             |:func:`set_ficon`                                      |
        +----------------------------------------+-------------------------------+-------------------------------------------------------+
        | ficon-xrc-acceleration                 | The FICON options             |:func:`set_ficon_xrc_acceleration`                     |
        +----------------------------------------+-------------------------------+-------------------------------------------------------+
        | ficon-tape-read-acceleration           | The FICON options             |:func:`set_ficon_tape_read_acceleration`               |
        +----------------------------------------+-------------------------------+-------------------------------------------------------+
        | ficon-tape-write-acceleration          | The FICON options             |:func:`set_ficon_tape_write_acceleration`              |
        +----------------------------------------+-------------------------------+-------------------------------------------------------+
        | ficon-tin-tir-emulation                | The FICON options             |:func:`set_ficon_tin_tir_emulation`                    |
        +----------------------------------------+-------------------------------+-------------------------------------------------------+
        | ficon-device-acknowledgement-emulation | The FICON options             |:func:`set_ficon_device_acknowledgement_emulation`     |
        +----------------------------------------+-------------------------------+-------------------------------------------------------+
        | ficon-teradata-read-acceleration       | The FICON options             |:func:`set_ficon_teradata_read_acceleration`           |
        +----------------------------------------+-------------------------------+-------------------------------------------------------+
        | ficon-teradata-write-acceleration      | The FICON options             |:func:`set_ficon_teradata_write_acceleration`          |
        +----------------------------------------+-------------------------------+-------------------------------------------------------+
        | ficon-tape-write-max-pipe              | The FICON options             |:func:`set_ficon_tape_write_max_pipe`                  |
        +----------------------------------------+-------------------------------+-------------------------------------------------------+
        | ficon-tape-read-max-pipe               | The FICON options             |:func:`set_ficon_tape_read_max_pipe`                   |
        +----------------------------------------+-------------------------------+-------------------------------------------------------+
        | ficon-tape-read-max-devices            | The FICON options             |:func:`set_ficon_tape_read_max_devices`                |
        +----------------------------------------+-------------------------------+-------------------------------------------------------+
        | ficon-tape-write-max-devices           | The FICON options             |:func:`set_ficon_tape_write_max_devices`               |
        +----------------------------------------+-------------------------------+-------------------------------------------------------+
        | ficon-tape-write-timer                 | The FICON options             |:func:`set_ficon_tape_write_timer`                     |
        +----------------------------------------+-------------------------------+-------------------------------------------------------+
        | ficon-tape-write-max-chain             | The FICON options             |:func:`set_ficon_tape_write_max_chain`                 |
        +----------------------------------------+-------------------------------+-------------------------------------------------------+
        | ficon-oxid-base                        | The FICON options             |:func:`set_ficon_oxid_base`                            |
        +----------------------------------------+-------------------------------+-------------------------------------------------------+

    *Object functions*

        .. function:: get()

            Fill the object with values for all the attributes. Once filled,
            the object can be printed using :func:`pyfos_utils.response_print`

            :param session: session handler returned
             by :func:`pyfos_auth.login`
            :rtype: dictionary of error or success response

    *Attribute functions*

        .. function:: peek_name()

            Reads name from the tunnel object.

            :rtype: None on error and value on success

        .. function:: peek_admin_enabled()

            Reads admin enabled/Disabled flag from a tunnel object.

            :rtype: None on error and value on success

        .. function:: peek_fast_write_enabled()

            Reads fast write enabled from the tunnel Object

            :rtype: None on error and value on success

        .. function:: peek_tape_read()

            Reads tape read pipelining from  a tunnel object.

            :rtype: None on error and value on success

        .. function:: peek_tape_write()

            Reads tape write pipelining from a tunnel object.

            :rtype: None on error and value on success

        .. function:: peek_tunnel_status()

            Reads tunnel status from the the tunne object.

            :rtype: None on error and value on success

        .. function:: peek_ipsec_enabled()

            Reads IPSec enabled from a tunnel object.

            :rtype: None on error and value on success

        .. function:: peek_ipsec_policy()

            Reads IPSec policy name from the tunnel object.

            :rtype: None on error and value on success

        .. function:: peek_ha_operational_status()

            Reads ha operational status from a tunnel object.

            :rtype: None on error and value on success

        .. function:: peek_ip_extension()

            Reads IPEXT Enabled/Disabled from the tunnel Object

            :rtype: None on error and value on success

        .. function:: peek_load_level()

            Reads configured load level from  a tunnel object.

            :rtype: None on error and value on success

        .. function:: peek_active_load_level()

            Reads active load level from a tunnel object.

            :rtype: None on error and value on success

        .. function:: peek_peer_load_level()

            Reads peer load level from the the tunnel object.

            :rtype: None on error and value on success

        .. function:: peek_compression_tunnel()

            Reads tunnel compression level from a tunnel object.

            :rtype: None on error and value on success

        .. function:: peek_compression_protocol()

            Reads tunnel compression for protcol from the the tunnel object.

            :rtype: None on error and value on success

        .. function:: peek_compression_protocol_fc_compression()

            Reads FC compression protcol from a tunnel object.

            :rtype: None on error and value on success

        .. function:: peek_compression_protocol_ip_compression()

            Reads IP compression protcol from a tunnel object.

            :rtype: None on error and value on success

        .. function:: peek_qos_ratio()

            Reads qos ratio from a tunnel object.

            :rtype: None on error and value on success

        .. function:: peek_qos_ratio_distribution()

            Reads qos ratio distribution from the tunnel Object.

            :rtype: None on error and value on success

        .. function:: peek_qos_ratio_distribution_value()

            Reads atio distribution value from the tunnel Object.

            :rtype: None on error and value on success

        .. function:: peek_qos_ratio_fc_high_qos()

            Reads FC high priority QOS ratio from the tunnel object.

            :rtype: None on error and value on success

        .. function:: peek_qos_ratio_fc_medium_qos()

            Reads FC medium priority QOS ratio from the tunnel object.

            :rtype: None on error and value on success

        .. function:: peek_qos_ratio_fc_low_qos()

            Reads FC low  priority QOS ratio from the tunnel object.

            :rtype: None on error and value on success

        .. function:: peek_qos_ratio_ip_high_qos()

            Reads IP high priority QOS ratio from the tunnel object.

            :rtype: None on error and value on success

        .. function:: peek_qos_ratio_ip_medium_qos()

            Reads IP medium priority QOS ratio from the tunnel object.

            :rtype: None on error and value on success

        .. function:: peek_qos_ratio_ip_low_qos()

            Reads IP low  priority QOS ratio from the tunnel object.

            :rtype: None on error and value on success

        .. function:: peek_ficon()

            Reads ficon enabled/Disabled flag from a tunnel object.

            :rtype: None on error and value on success

        .. function:: peek_ficon_xrc_acceleration()

            Reads ficon xrc enabled from the tunnel Object

            :rtype: None on error and value on success

        .. function:: peek_ficon_tape_read_acceleration()

            Reads ficon tape read accelaration from  a tunnel object.

            :rtype: None on error and value on success

        .. function:: peek_ficon_tape_write_acceleration()

            Reads ficon tape write accelaration from a tunnel object.

            :rtype: None on error and value on success

        .. function:: peek_ficon_tin_tir_emulation()

            Reads ficon tin tir emulation from the the tunne object.

            :rtype: None on error and value on success

        .. function:: peek_ficon_device_acknowledgement_emulation()

            Reads ficon device ack from a tunnel object.

            :rtype: None on error and value on success

        .. function:: peek_ficon_teradata_read_acceleration()

            Reads ficon teradata read acceleration from the tunnel Object

            :rtype: None on error and value on success

        .. function:: peek_ficon_teradata_write_acceleration()

            Reads ficon teradata write acceleration from the tunnel Object

            :rtype: None on error and value on success

        .. function:: peek_ficon_tape_write_max_pipe()

            Reads ficon tape write max pipe from a tunnel object.

            :rtype: None on error and value on success

        .. function:: peek_ficon_tape_read_max_pipe()

            Reads ficon tape read max pipe from the the tunne object.

            :rtype: None on error and value on success

        .. function:: peek_ficon_tape_write_max_devices()

            Reads ficon tape write max devices from a tunnel object.

            :rtype: None on error and value on success

        .. function:: peek_ficon_tape_read_max_devices()

            Reads ficon tape read max devices from a tunnel object.

            :rtype: None on error and value on success

        .. function:: peek_ficon_tape_write_timer()

            Reads ficon tape write timer from the tunnel Object

            :rtype: None on error and value on success

        .. function:: peek_ficon_tape_write_max_chain()

            Reads tape write max chain from  a tunnel object.

            :rtype: None on error and value on success

        .. function:: peek_ficon_oxid_base()

            Reads ficon oxid base from a tunnel object.

            :rtype: None on error and value on success

        .. function:: set_name(name)

            Set the name in the tunnel object.

            :rtype: dictionary of error or success response and value
             with "name" as key

        .. function:: set_admin_enabled(adminEnabled)

            Set the admin enabled state in the tunnel object.

            :rtype: dictionary of error or success response and value
             with "admin-enabled" as key

        .. function:: set_fast_write_enabled(fastwrite)

            Set the fast write enabled in the tunnel Object

            :rtype: dictionary of error or success response and value
             with "fastwrite-enabled" as key

        .. function:: set_tape_read(tapeRead)

            Set the tape read pipelining in the tunnel object.

            :rtype: dictionary of error or success response and value
             with "tape-read" as key

        .. function:: set_tape_write(tapeWrite)

            Set the tape write pipelining in the tunnel object.

            :rtype: dictionary of error or success response and value
             with "tape-write" as key

        .. function:: set_ipsec_policy(ipsecPolicyName)

            Set the IPSec policy for the tunnel object.

            :rtype: dictionary of error or success response and value
             with "ipsec-policy" as key

        .. function:: set_ip_extension(name)

            Set IPEXT enabled in the tunnel object.

            :rtype: dictionary of error or success response and value
             with "ipsec-policy" as key

        .. function:: set_load_level(loadLevel)

            Set the load level in the tunnel object.

            :rtype: dictionary of error or success response and value
             with "load-level" as key

        .. function:: set_compression_tunnel(tnlCompression)

            Set the tunnel Compression in the tunnel Object

            :rtype: dictionary of error or success response and value
             with "compression-tunnel" as key

        .. function:: set_compression_protocol(protcolCompressiondict)

            Set the protcol level compression in the tunnel object.

            :rtype: dictionary of error or success response and value with
             "compression-protcol" as key

        .. function:: set_compression_protocol_fc_compression(fccompression)

            Set the FC protcol compression in the tunnel object.

            :rtype: dictionary of error or success response and value
             with "fc-compression" as key

        .. function:: set_compression_protocol_ip_compression(ipcompression)

            Set the IP protocol compression in the tunnel object.

            :rtype: dictionary of error or success response and value
             with "ip-compression" as key

        .. function:: set_qos_ratio(qosRation)

            Set the QOS ratio in the tunnel object.

            :rtype: dictionary of error or success response and value
             with "qos-ratio" as key

        .. function:: set_qos_ratio_distribution(qosDistribution)

            Set the qos distribution in the tunnel object.

            :rtype: dictionary of error or success response and value with
             "distribution" as key

        .. function:: set_qos_ratio_distribution_value(qosDistributionVal)

            Set the qos distribution  value in the tunnel object..

            :rtype: dictionary of error or success response and value with
             "distribution-value" as key

        .. function:: set_qos_ratio_fc_high_qos(fcHighQos)

            Set the FC High QOS ratio in the tunnel object.

            :rtype: dictionary of error or success response and
             value with "fc-high-qos" as key

        .. function:: set_qos_ratio_fc_medium_qos(qosRation)

            Set the FC Medium QOS ratio in the tunnel object.

            :rtype: dictionary of error or success response and value
             with "fc-medium-qos" as key

        .. function:: set_qos_ratio_fc_low_qos(fcHighQos)

            Set the FC low QOS ratio in the tunnel object.

            :rtype: dictionary of error or success response and value
             with "fc-low-qos" as key

        .. function:: set_qos_ratio_ip_medium_qos(qosRation)

            Set the IP Medium QOS ratio in the tunnel object.

            :rtype: dictionary of error or success response and value
             with "ip-medium-qos" as key

        .. function:: set_qos_ratio_ip_high_qos(fcHighQos)

            Set the IP High QOS ratio in the tunnel object.

            :rtype: dictionary of error or success response and value
             with "ip-high-qos" as key

        .. function:: set_qos_ratio_ip_low_qos(qosRation)

            Set the FC low QOS ratio in the tunnel object.

            :rtype: dictionary of error or success response and value
             with "ip-low-qos" as key

        .. function:: set_ficon(ficon)

            Write ficon enabled/Disabled flag from a tunnel object.

            :rtype: dictionary of error or success response and value
             with "ficon" as key

        .. function:: set_ficon_xrc_acceleration(xrcAccelaration)

            Write ficon xrc enabled in the tunnel object

            :rtype: dictionary of error or success response and value
             with "ficon-xrc-acceleration" as key

        .. function:: set_ficon_tape_read_acceleration(tapeReadAcc)

            Write ficon tape read accelaration from  a tunnel object.

            :rtype: dictionary of error or success response and value
             with "ficon-tape-read-acceleration" as key

        .. function:: set_ficon_tape_write_acceleration(tapeWriteAcc)

            Write ficon tape write accelaration from a tunnel object.

            :rtype: dictionary of error or success response and value
             with "ficon-tape-write-acceleration" as key

        .. function:: set_ficon_tin_tir_emulation(tinTirEmul)

            Write ficon tin tir emulation from the the tunne object.

            :rtype: dictionary of error or success response and value
             with "ficon-tin-tir-emulation" as key

        .. function:: set_ficon_device_acknowledgement_emulation(deviceAck)

            Write ficon device ack from a tunnel object.

            :rtype: dictionary of error or success response and value
             with "ficon-device-acknowledgement-emulation" as key

        .. function:: set_ficon_teradata_read_acceleration(terradataReadAcc)

            Write ficon teradata read acceleration in the tunnel object

            :rtype: dictionary of error or success response and value with
             "ficon-teradata-read-acceleration" as key

        .. function:: set_ficon_teradata_write_acceleration(terradataWriteAcc)

            Write ficon teradata write acceleration in the tunnel object

            :rtype: dictionary of error or success response and value with
             "ficon-teradata-write-acceleration" as key

        .. function:: set_ficon_tape_write_max_pipe(tapeWriteMaxPipe)

            Write ficon tape write max pipe from a tunnel object.

            :rtype: dictionary of error or success response and value with
             "ficon-tape-write-max-pipe" as key

        .. function:: set_ficon_tape_read_max_pipe(tapeReadMaxPipe)

            Write ficon tape read max pipe from the the tunne object.

            :rtype: dictionary of error or success response and value with
             "ficon-tape-read-max-pipe" as key

        .. function:: set_ficon_tape_write_max_devices(tapeWriteMaxdev)

            Write ficon tape write max devices from a tunnel object.

            :rtype: dictionary of error or success response and value with
             "ficon-tape-write-max-devices" as key

        .. function:: set_ficon_tape_read_max_devices(tapeWriteMaxdev)

            Write ficon tape read max devices from a tunnel object.

            :rtype: dictionary of error or success response and value
             with "ficon-tape-read-max-devices" as key

        .. function:: set_ficon_tape_write_timer(tapeWritetmr)

            Write ficon tape write timer in the tunnel object

            :rtype: dictionary of error or success response and value
             with "ficon-tape-write-timer" as key

        .. function:: set_ficon_tape_write_max_chain(tapeWriteMaxchain)

            Write tape write max chain from  a tunnel object.

            :rtype: dictionary of error or success response and value with
             "ficon-tape-write-max-chain" as key

        .. function:: set_ficon_oxid_base(oxidBase)

            Write ficon oxid base from a tunnel object.

            :rtype: dictionary of error or success response and value
             with "ficon-oxid-base" as key
    """
    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.tunnel,
                         "/rest/running/brocade-extension-tunnel/"
                         "extension-tunnel")
        self.add(pyfos_rest_util.rest_attribute("name",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute("user-friendly-name",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("local-wwn",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("remote-wwn",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("peer-wwn",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("admin-enabled",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("fast-write-enabled",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("tape-read",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("tape-write",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("tunnel-status",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("ipsec-enabled",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("ipsec-policy",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("ha-operational-status",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("ficon",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("ficon-xrc-acceleration",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "ficon-tape-write-acceleration",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "ficon-tape-read-acceleration",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("ficon-tin-tir-emulation",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "ficon-device-acknowledgement-emulation",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "ficon-read-block-id-emulation",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "ficon-teradata-read-acceleration",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "ficon-teradata-write-acceleration",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "ficon-tape-write-max-pipe",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("ficon-tape-read-max-pipe",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "ficon-tape-write-max-devices",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "ficon-tape-read-max-devices",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "ficon-tape-read-acceleration",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("ficon-tape-write-timer",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "ficon-tape-write-max-chain",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("ficon-oxid-base",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("ip-extension",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("load-level",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("active-load-level",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("peer-load-level",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("compression-tunnel",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.add(pyfos_rest_util.rest_attribute("compression-protocol",
                 pyfos_type.type_na, dict(),
                 pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute("fc-compression",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG),
                 ["compression-protocol"])
        self.add(pyfos_rest_util.rest_attribute("ip-compression",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG),
                 ["compression-protocol"])

        self.add(pyfos_rest_util.rest_attribute("qos-ratio",
                 pyfos_type.type_na, dict(),
                 pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute("distribution",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG), ["qos-ratio"])
        self.add(pyfos_rest_util.rest_attribute("distribution-value",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG), ["qos-ratio"])
        self.add(pyfos_rest_util.rest_attribute("fc-high-qos",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG), ["qos-ratio"])
        self.add(pyfos_rest_util.rest_attribute("fc-medium-qos",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG), ["qos-ratio"])
        self.add(pyfos_rest_util.rest_attribute("fc-low-qos",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG), ["qos-ratio"])
        self.add(pyfos_rest_util.rest_attribute("ip-high-qos",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG), ["qos-ratio"])
        self.add(pyfos_rest_util.rest_attribute("ip-medium-qos",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG), ["qos-ratio"])
        self.add(pyfos_rest_util.rest_attribute("ip-low-qos",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG), ["qos-ratio"])
        self.load(dictvalues, 1)


class extension_tunnel_statistics(pyfos_rest_util.rest_object):
    """Class of extension_tunnel_statistics

    Important class members:

        +-------------------------------+-------------------------------+-------------------------------------------------+
        | Attribute name                | Description                   |Frequently used functions                        |
        +===============================+===============================+=================================================+
        | name                          | The slot/port name of GE port |:func:`peek_name`                                |
        +-------------------------------+-------------------------------+-------------------------------------------------+
        | name                          | The slot/port name of GE port |:func:`set_name`                                 |
        +-------------------------------+-------------------------------+-------------------------------------------------+
        | flow-status                   | The IPv4/IPv6 address         |:func:`peek_flow_status`                         |
        +-------------------------------+-------------------------------+-------------------------------------------------+
        | operational-status            | Data-path Processor ID        |:func:`peek_operational_status`                  |
        +-------------------------------+-------------------------------+-------------------------------------------------+
        | connection-count              | The prefix length of IP       |:func:`peek_connection_count`                    |
        +-------------------------------+-------------------------------+-------------------------------------------------+
        | duration                      | The maximum transmission unit |:func:`peek_duration`                            |
        +-------------------------------+-------------------------------+-------------------------------------------------+
        | uncompressed-bytes            | The VLAN ID of the IP Address |:func:`peek_uncompressed_bytes`                  |
        +-------------------------------+-------------------------------+-------------------------------------------------+
        | compressed-bytes              | IP Interface Flags            |:func:`peek_compressed_bytes`                    |
        +-------------------------------+-------------------------------+-------------------------------------------------+

    *Object functions*

        .. function:: get()

            Fill the object with values for all the attributes.
            Once filled, the object can be printed
            using :func:`pyfos_utils.response_print`

            :param session: session handler returned
             by :func:`pyfos_auth.login`
            :rtype: dictionary of error or success response

    *Attribute functions*

        .. function:: peek_name()

            Reads name from the tunnel stats object.

            :rtype: None on error and value on success

        .. function:: peek_flow_status()

            Reads flow status from the tunnel stats object.

            :rtype: None on error and value on success

        .. function:: peek_operational_status()

            Reads the operation status from the tunnel stats object.

            :rtype: None on error and value on success

        .. function:: peek_connection_count()

            Reads the connection count from the tunnel stats object.

            :rtype: None on error and value on success

        .. function:: peek_duration()

            Reads the duration for from the tunnel stats object

            :rtype: None on error and value on success

        .. function:: peek_uncompressed_bytes()

            Reads uncompressed bytes from the tunnel stats object.

            :rtype: None on error and value on success

        .. function:: peek_compressed_bytes()

            Reads compressed bytes  from the tunnel stats object.

            :rtype: None on error and value on success

        .. function:: set_name(name)

            Set the name in the object.

            :rtype: dictionary of error or success response and
             value with "name" as key

    """
    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.tunnel_stats,
                         "/rest/running/brocade-extension-tunnel/"
                         "extension-tunnel-statistics")
        self.add(pyfos_rest_util.rest_attribute("name",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute("flow-status",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("operational-status",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("connection-count",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("duration",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("uncompressed-bytes",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("compressed-bytes",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.load(dictvalues, 1)


class extension_circuit(pyfos_rest_util.rest_object):
        """Class of extension_circuit

        Important class members:

            +-------------------------------+-------------------------------+-------------------------------------------------+
            | Attribute name                | Description                   |Frequently used functions                        |
            +===============================+===============================+=================================================+
            | name                          | The slot/port name of VE port |:func:`peek_name`                                |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | name                          | The slot/port name of VE port |:func:`set_name`                                 |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | circuit-id                    | Circuit ID                    |:func:`peek_circuit_id`                          |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | circuit-id                    | Circuit ID                    |:func:`set_circuit_id`                           |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | local-ip-address              | Ciruit local IP address       |:func:`peek_local_ip_address`                    |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | local-ip-address              | Ciruit local IP address       |:func:`set_local_ip_address`                     |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | remote-ip-address             | Ciruit remote IP address      |:func:`peek_remote_ip_address`                   |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | remote-ip-address             | Ciruit remote IP address      |:func:`set_remote_ip_address`                    |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | local-ha-ip-address           | Ciruit local HA IP address    |:func:`peek_local_ha_ip_address`                 |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | local-ha-ip-address           | Ciruit local HA IP address    |:func:`set_local_ha_ip_address`                  |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | remote-ha-ip-address          | Ciruit remote HA IP address   |:func:`peek_remote_ha_ip_address`                |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | remote-ha-ip-address          | Ciruit remote HA IP address   |:func:`set_remote_ha_ip_address`                 |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | metric                        | Circuit metric value          |:func:`peek_metric`                              |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | metric                        | Circuit metric value          |:func:`set_metric`                               |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | admin-enabled                 | The admin enabled tnl state   |:func:`peek_admin_enabled`                       |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | admin-enabled                 | The admin enabled tnl state   |:func:`set_admin_enabled`                        |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | circuit-status                | The Circuit status            |:func:`peek_circuit_status`                      |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | path-mtu-discovered           | Path MTU discovered           |:func:`peek_path_mtu_discovered`                 |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | failover-group-id             | Circuit Failover group ID     |:func:`peek_failover_group_id`                   |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | failover-group-id             | Circuit Failover group ID     |:func:`set_failover_group_id`                    |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | minimum-communication-rate    | Min Comm rate of circuit      |:func:`peek_minimum_communication_rate`          |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | minimum-communication-rate    | Min Comm rate of circuit      |:func:`set_minimum_communication_rate`           |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | maximum-communication-rate    | Max Comm rate of circuit      |:func:`peek_maximum_communication_rate`          |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | maximum-communication-rate    | Max Comm rate of circuit      |:func:`set_maximum_communication_rate`           |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | vlan-id                       | The Circuit vlan ID           |:func:`peek_vlan_id`                             |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | l2-cos                        | l2cos                         |:func:`peek_l2_cos`                              |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | l2-cos                        | l2cos                         |:func:`set_l2_cos`                               |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | priority-control              | control priority              |:func:`peek_l2_cos_priority_control`             |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | priority-control              | control priority              |:func:`set_l2_cos_priority_control`              |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | fc-priority-high              | FC QOS High                   |:func:`peek_l2_cos_fc_priority_high`             |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | fc-priority-high              | FC QOS High                   |:func:`set_l2_cos_fc_priority_high`              |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | fc-priority-medium            | FC QOS High                   |:func:`peek_l2_cos_fc_priority_medium`           |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | fc-priority-medium            | FC QOS Medium                 |:func:`set_l2_cos_fc_priority_medium`            |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | fc-priority-low               | FC QOS Low                    |:func:`peek_l2_cos_fc_priority_low`              |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | fc-priority-low               | FC QOS Low                    |:func:`set_l2_cos_fc_priority_low`               |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | ip-priority-high              | IP QOS High                   |:func:`peek_l2_cos_ip_priority_high`             |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | ip-priority-high              | IP QOS High                   |:func:`set_l2_cos_ip_priority_high`              |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | ip-priority-medium            | IP QOS Medium                 |:func:`peek_l2_cos_ip_priority_medium`           |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | ip-priority-medium            | IP QOS Medium                 |:func:`set_l2_cos_ip_priority_medium`            |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | ip-priority-low               | IP QOS Low                    |:func:`peek_l2_cos_ip_priority_low`              |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | ip-priority-low               | IP QOS LOw                    |:func:`set_l2_cos_ip_priority_low`               |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | dscp                          | dscp                          |:func:`peek_dscp`                                |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | dscp                          | dscp                          |:func:`set_dscp`                                 |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | priority-control              | control priority              |:func:`peek_dscp_priority_control`               |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | priority-control              | control priority              |:func:`set_dscp_priority_control`                |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | fc-priority-high              | FC QOS High                   |:func:`peek_dscp_fc_priority_high`               |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | fc-priority-high              | FC QOS High                   |:func:`set_dscp_fc_priority_high`                |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | fc-priority-medium            | FC QOS High                   |:func:`peek_dscp_fc_priority_medium`             |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | fc-priority-medium            | FC QOS Medium                 |:func:`set_dscp_fc_priority_medium`              |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | fc-priority-low               | FC QOS Low                    |:func:`peek_dscp_fc_priority_low`                |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | fc-priority-low               | FC QOS Low                    |:func:`set_dscp_fc_priority_low`                 |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | ip-priority-high              | IP QOS High                   |:func:`peek_dscp_ip_priority_high`               |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | ip-priority-high              | IP QOS High                   |:func:`set_dscp_ip_priority_high`                |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | ip-priority-medium            | IP QOS Medium                 |:func:`peek_dscp_ip_priority_medium`             |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | ip-priority-medium            | IP QOS Medium                 |:func:`set_dscp_ip_priority_medium`              |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | ip-priority-low               | IP QOS Low                    |:func:`peek_dscp_ip_priority_low`                |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | ip-priority-low               | IP QOS LOw                    |:func:`set_dscp_ip_priority_low`                 |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | arl-algorithm-mode            | ARL alogirithm                |:func:`peek_arl_algorithm_mode`                  |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | arl-algorithm-mode            | ARL algorithm                 |:func:`set_arl_algorithm_mode`                   |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | keep-alive-timeout            | Keep alive timeout            |:func:`peek_keep_alive_timeout`                  |
            +-------------------------------+-------------------------------+-------------------------------------------------+

        *Object functions*

            .. function:: get()

                Fill the object with values for all the attributes.
                Once filled, the object can be printed
                using :func:`pyfos_utils.response_print`

                :param session: session handler returned
                 by :func:`pyfos_auth.login`
                :rtype: dictionary of error or success response

        *Attribute functions*

            .. function:: peek_name()

                Reads name from the tunnel object.

                :rtype: None on error and value on success

            .. function:: peek_circuit_id()

                Reads circuit ID from the circuit object.

                :rtype: None on error and value on success

            .. function:: peek_local_ip_address()

                Reads local IP address from the circuit object.

                :rtype: None on error and value on success

            .. function:: peek_remote_ip_address()

                Reads remote IP address from the circuit object.

                :rtype: None on error and value on success

            .. function:: peek_local_ha_ip_address()

                Reads local HA IP address from the circuit object.

                :rtype: None on error and value on success

            .. function:: peek_remote_ha_ip_address()

                Reads remote HA IP address from the circuit object.

                :rtype: None on error and value on success

            .. function:: peek_metric()

                Reads metric from the circuit object.

                :rtype: None on error and value on success

            .. function:: peek_admin_enabled()

                Reads admin enabled from the circuit object.

                :rtype: None on error and value on success

            .. function:: peek_circuit_status()

                Reads ciruit status from the circuit object.

                :rtype: None on error and value on success

            .. function:: peek_path_mtu_discovered()

                Reads path MTU discovered from the circuit object.

                :rtype: None on error and value on success

            .. function:: peek_failover_group_id()

                Reads failover group id from the circuit object.

                :rtype: None on error and value on success

            .. function:: peek_minimum_communication_rate()

                Reads minimum communication rate from the circuit object.

                :rtype: None on error and value on success

            .. function:: peek_maximum_communication_rate()

                Reads maximum communication rate from the circuit object.

                :rtype: None on error and value on success

            .. function:: peek_vlan_id()

                Reads vlan-id from the circuit object.

                :rtype: None on error and value on success

            .. function:: peek_l2_cos()

                Reads l2 cos from the circuit object.

                :rtype: None on error and value on success

            .. function:: peek_l2_cos_priority_control()

                Reads priority control l2 cos from the circuit object.

                :rtype: None on error and value on success

            .. function:: peek_l2_cos_fc_priority_high()

                Reads FC high l2 cos from the circuit object.

                :rtype: None on error and value on success

            .. function:: peek_l2_cos_fc_priority_medium()

                Reads FC medium l2 cos from the circuit object.

                :rtype: None on error and value on success

            .. function:: peek_l2_cos_fc_priority_low()

                Reads FC low l2 cos from the circuit object.

                :rtype: None on error and value on success

            .. function:: peek_l2_cos_ip_priority_high()

                Reads IP high l2 cos from the circuit object.

                :rtype: None on error and value on success

            .. function:: peek_l2_cos_ip_priority_medium()

                Reads IP medium l2 cos from the circuit object.

                :rtype: None on error and value on success

            .. function:: peek_l2_cos_ip_priority_low()

                Reads IP low l2 cos from the circuit object.

                :rtype: None on error and value on success

            .. function:: peek_dscp()

                Reads dscp value from the circuit object.

                :rtype: None on error and value on success

            .. function:: peek_dscp_priority_control()

                Reads priority control dscp value from the circuit object.

                :rtype: None on error and value on success

            .. function:: peek_dscp_fc_priority_high()

                Reads FC high dscp value from the circuit object.

                :rtype: None on error and value on success

            .. function:: peek_dscp_fc_priority_medium()

                Reads FC medium dscp value from the circuit object.

                :rtype: None on error and value on success

            .. function:: peek_dscp_fc_priority_low()

                Reads FC low dscp value from the circuit object.

                :rtype: None on error and value on success

            .. function:: peek_dscp_ip_priority_high()

                Reads IP High dscp value from the circuit object.

                :rtype: None on error and value on success

            .. function:: peek_dscp_ip_priority_medium()

                Reads IP medium dscp value from the circuit object.

                :rtype: None on error and value on success

            .. function:: peek_dscp_ip_priority_low()

                Reads IP low dscp value from the circuit object.

                :rtype: None on error and value on success

            .. function:: peek_arl_algorithm_mode()

                Reads ARL algorithm from the circuit object.

                :rtype: None on error and value on success

            .. function:: peek_keep_alive_timeout()

                Reads keep alive timeout from the circuit object.

                :rtype: None on error and value on success

            .. function:: set_name(name)

                Set the name in the tunnel object.

                :rtype: dictionary of error or success response and value
                 with "name" as key

            .. function:: set_circuit_id(ciruitID)

                Set the circuit ID in the circuit object.

                :rtype: dictionary of error or success response and value
                 with "circuit-id" as key

            .. function:: set_local_ip_address(localIP)

                Set the local circuit IP address in the circuit object.

                :rtype: dictionary of error or success response and value
                 with "local-ip-address" as key

            .. function:: set_remote_ip_address(remoteIP)

                Set the Remote circuit IP address in the circuit object.

                :rtype: dictionary of error or success response and value
                 with "remote-ip-address" as key

            .. function:: set_local_ha_ip_address(localHAIP)

                Set the local HA circuit IP address in the circuit object.

                :rtype: dictionary of error or success response and value
                 with "local-ha-ip-address" as key

            .. function:: set_remote_ha_ip_address(remoteHAIP)

                Set the Remote HA circuit IP address in the circuit object.

                :rtype: dictionary of error or success response and value
                 with "remote-ha-ip-address" as key

            .. function:: set_metric(metric)

                Set the metric in the circuit object.

                :rtype: dictionary of error or success response and value
                 with "metric" as key

            .. function:: set_admin_enabled(adminState)

                Set the admin enabled in the circuit object.

                :rtype: dictionary of error or success response and value with
                 "admin-enabled" as key

            .. function:: set_failover_group_id(failoverGroup)

                Set the failover group id in the circuit object.

                :rtype: dictionary of error or success response and value with
                 "failover-group-id" as key

            .. function:: set_minimum_communication_rate(minCommRate)

                Set the min comm rate in the circuit object.

                :rtype: dictionary of error or success response and value with
                 "minimum-communication-rate" as key

            .. function:: set_maximum_communication_rate(maxCommRate)

                Set the max comm rate in the circuit object.

                :rtype: dictionary of error or success response and value with
                 "maximum-communication-rate" as key

            .. function:: set_l2_cos(l2cos)

                Set the l2 cos in the circuit object.

                :rtype: dictionary of error or success response and value
                 with "l2-cos" as key

            .. function:: set_l2_cos_priority_control(controll2Cos)

                Set the priority control l2 cos in the circuit object.

                :rtype: dictionary of error or success response and value
                 with "priority-control" as key

            .. function:: set_l2_cos_fc_priority_high(fcHighl2Cos)

                Set the FC high l2 cos in the circuit object.

                :rtype: dictionary of error or success response and value
                 with "fc-priority-high" as key

            .. function:: set_l2_cos_fc_priority_medium(fcMedl2Cos)

                Set the FC medium l2 cos in the circuit object.

                :rtype: dictionary of error or success response and value
                 with "fc-priority-medium" as key

            .. function:: set_l2_cos_fc_priority_low(fcLowl2Cos)

                Set the FC low l2 cos in the circuit object.

                :rtype: dictionary of error or success response and value
                 with "fc-priority-low" as key

            .. function:: set_l2_cos_ip_priority_high(ipHighl2Cos)

                Set the IP high l2 cos in the circuit object.

                :rtype: dictionary of error or success response and value
                 with "ip-priority-high" as key

            .. function:: set_l2_cos_ip_priority_medium(ipMediuml2Cos)

                Set the IP medium l2 cos in the circuit object.

                :rtype: dictionary of error or success response and value
                 with "ip-priority-medium" as key

            .. function:: set_l2_cos_ip_priority_low(iplowl2Cos)

                Set the IP low l2 cos in the circuit object.

                :rtype: dictionary of error or success response and value
                 with "ip-priority-low" as key

            .. function:: set_dscp(dscp)

                Set the dscp in the circuit object.

                :rtype: dictionary of error or success response and
                 value with "l2-cos" as key

            .. function:: set_dscp_priority_control(controldscp)

                Set the priority control l2 cos in the circuit object.

                :rtype: dictionary of error or success response and value
                 with "priority-control" as key

            .. function:: set_dscp_fc_priority_high(fcHighdscp)

                Set the FC high l2 cos in the circuit object.

                :rtype: dictionary of error or success response and value
                 with "fc-priority-high" as key

            .. function:: set_dscp_fc_priority_medium(fcMeddscp)

                Set the FC medium l2 cos in the circuit object.

                :rtype: dictionary of error or success response and value
                 with "fc-priority-medium" as key

            .. function:: set_dscp_fc_priority_low(fcLowdscp)

                Set the FC low l2 cos in the circuit object.

                :rtype: dictionary of error or success response and value
                 with "fc-priority-low" as key

            .. function:: set_dscp_ip_priority_high(ipHighdscp)

                Set the IP high l2 cos in the circuit object.

                :rtype: dictionary of error or success response and value
                 with "ip-priority-high" as key

            .. function:: set_dscp_ip_priority_medium(ipMediumdscp)

                Set the IP medium l2 cos in the circuit object.

                :rtype: dictionary of error or success response and value
                 with "ip-priority-medium" as key

            .. function:: set_dscp_ip_priority_low(iplowdscp)

                Set the IP low l2 cos in the circuit object.

                :rtype: dictionary of error or success response and value
                 with "ip-priority-low" as key

            .. function:: set_arl_algorithm_mode(arlAlgorithmMode)

                Set the ARL algorithm in the circuit object.

                :rtype: dictionary of error or success response and value
                 with "arl-algorithm-mode" as key

        """
        def __init__(self, dictvalues={}):
            super().__init__(pyfos_rest_util.rest_obj_type.circuit,
                             "/rest/running/brocade-extension-tunnel/"
                             "extension-circuit")
            self.add(pyfos_rest_util.rest_attribute("name",
                     pyfos_type.type_str, None,
                     pyfos_rest_util.REST_ATTRIBUTE_KEY))
            self.add(pyfos_rest_util.rest_attribute("circuit-id",
                     pyfos_type.type_int, None,
                     pyfos_rest_util.REST_ATTRIBUTE_KEY))
            self.add(pyfos_rest_util.rest_attribute("local-ip-address",
                     pyfos_type.type_ip_addr, None,
                     pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
            self.add(pyfos_rest_util.rest_attribute("remote-ip-address",
                     pyfos_type.type_ip_addr, None,
                     pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
            self.add(pyfos_rest_util.rest_attribute("metric",
                     pyfos_type.type_int, None,
                     pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
            self.add(pyfos_rest_util.rest_attribute("failover-group-id",
                     pyfos_type.type_int, None,
                     pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
            self.add(pyfos_rest_util.rest_attribute("admin-enabled",
                     pyfos_type.type_int, None,
                     pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
            self.add(pyfos_rest_util.rest_attribute("path-mtu-discovered",
                     pyfos_type.type_int, None,
                     pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
            self.add(pyfos_rest_util.rest_attribute(
                     "minimum-communication-rate",
                     pyfos_type.type_int, None,
                     pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
            self.add(pyfos_rest_util.rest_attribute(
                     "maximum-communication-rate",
                     pyfos_type.type_int, None,
                     pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
            self.add(pyfos_rest_util.rest_attribute("keep-alive-timeout",
                     pyfos_type.type_int, None,
                     pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
            self.add(pyfos_rest_util.rest_attribute("vlan-id",
                     pyfos_type.type_int, None,
                     pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
            self.add(pyfos_rest_util.rest_attribute("l2-cos",
                     pyfos_type.type_na, dict(),
                     pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
            self.add(pyfos_rest_util.rest_attribute("priority-control",
                     pyfos_type.type_str, None,
                     pyfos_rest_util.REST_ATTRIBUTE_CONFIG), ["l2-cos"])
            self.add(pyfos_rest_util.rest_attribute("fc-priority-high",
                     pyfos_type.type_str, None,
                     pyfos_rest_util.REST_ATTRIBUTE_CONFIG), ["l2-cos"])
            self.add(pyfos_rest_util.rest_attribute("fc-priority-medium",
                     pyfos_type.type_str, None,
                     pyfos_rest_util.REST_ATTRIBUTE_CONFIG), ["l2-cos"])
            self.add(pyfos_rest_util.rest_attribute("fc-priority-low",
                     pyfos_type.type_str, None,
                     pyfos_rest_util.REST_ATTRIBUTE_CONFIG), ["l2-cos"])
            self.add(pyfos_rest_util.rest_attribute("ip-priority-high",
                     pyfos_type.type_str, None,
                     pyfos_rest_util.REST_ATTRIBUTE_CONFIG), ["l2-cos"])
            self.add(pyfos_rest_util.rest_attribute("ip-priority-medium",
                     pyfos_type.type_str, None,
                     pyfos_rest_util.REST_ATTRIBUTE_CONFIG), ["l2-cos"])
            self.add(pyfos_rest_util.rest_attribute("ip-priority-low",
                     pyfos_type.type_str, None,
                     pyfos_rest_util.REST_ATTRIBUTE_CONFIG), ["l2-cos"])

            self.add(pyfos_rest_util.rest_attribute("dscp",
                     pyfos_type.type_na, dict(),
                     pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
            self.add(pyfos_rest_util.rest_attribute("priority-control",
                     pyfos_type.type_str, None,
                     pyfos_rest_util.REST_ATTRIBUTE_CONFIG), ["dscp"])
            self.add(pyfos_rest_util.rest_attribute("fc-priority-high",
                     pyfos_type.type_str, None,
                     pyfos_rest_util.REST_ATTRIBUTE_CONFIG), ["dscp"])
            self.add(pyfos_rest_util.rest_attribute("fc-priority-medium",
                     pyfos_type.type_str, None,
                     pyfos_rest_util.REST_ATTRIBUTE_CONFIG), ["dscp"])
            self.add(pyfos_rest_util.rest_attribute("fc-priority-low",
                     pyfos_type.type_str, None,
                     pyfos_rest_util.REST_ATTRIBUTE_CONFIG), ["dscp"])
            self.add(pyfos_rest_util.rest_attribute("ip-priority-high",
                     pyfos_type.type_str, None,
                     pyfos_rest_util.REST_ATTRIBUTE_CONFIG), ["dscp"])
            self.add(pyfos_rest_util.rest_attribute("ip-priority-medium",
                     pyfos_type.type_str, None,
                     pyfos_rest_util.REST_ATTRIBUTE_CONFIG), ["dscp"])
            self.add(pyfos_rest_util.rest_attribute("ip-priority-low",
                     pyfos_type.type_str, None,
                     pyfos_rest_util.REST_ATTRIBUTE_CONFIG), ["dscp"])
            self.add(pyfos_rest_util.rest_attribute("circuit-status",
                     pyfos_type.type_int, None,
                     pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
            self.add(pyfos_rest_util.rest_attribute("local-ha-ip-address",
                     pyfos_type.type_ip_addr, None,
                     pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
            self.add(pyfos_rest_util.rest_attribute("remote-ha-ip-address",
                     pyfos_type.type_ip_addr, None,
                     pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
            self.add(pyfos_rest_util.rest_attribute("arl-algorithm-mode",
                     pyfos_type.type_int, None,
                     pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
            self.load(dictvalues, 1)


class extension_circuit_statistics(pyfos_rest_util.rest_object):
        """Class of extension_circuit_statistics

        Important class members:

            +-------------------------------+-------------------------------+-------------------------------------------------+
            | Attribute name                | Description                   |Frequently used functions                        |
            +===============================+===============================+=================================================+
            | name                          | The slot/port name of GE port |:func:`peek_name`                                |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | name                          | The slot/port name of GE port |:func:`set_name`                                 |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | circuit-id                    | Circuit ID                    |:func:`peek_circuit_id`                          |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | circuit-id                    | Circuit ID                    |:func:`set_circuit_id`                           |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | flow-status                   | The IPv4/IPv6 address         |:func:`peek_flow_status`                         |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | operational-status            | Data-path Processor ID        |:func:`peek_operational_status`                  |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | connection-count              | The prefix length of IP       |:func:`peek_connection_count`                    |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | duration                      | The maximum transmission unit |:func:`peek_duration`                            |
            +-------------------------------+-------------------------------+-------------------------------------------------+
            | metric                        | Circuit metric value          |:func:`peek_metric`                              |
            +-------------------------------+-------------------------------+-------------------------------------------------+

        *Object functions*

            .. function:: get()

                Fill the object with values for all the attributes.
                Once filled, the object can be printed
                using :func:`pyfos_utils.response_print`

                :param session: session handler returned
                 by :func:`pyfos_auth.login`
                :rtype: dictionary of error or success response

        *Attribute functions*

            .. function:: peek_name()

                Reads name from the circuit stats object.

                :rtype: None on error and value on success

            .. function:: peek_circuit_id()

                Reads circuit ID from the circuit stats object.

                :rtype: None on error and value on success

            .. function:: peek_flow_status()

                Reads flow status from the circuit stats object.

                :rtype: None on error and value on success

            .. function:: peek_operational_status()

                Reads the operation status from the circuit stats object.

                :rtype: None on error and value on success

            .. function:: peek_connection_count()

                Reads the connection count from the circuit stats object.

                :rtype: None on error and value on success

            .. function:: peek_duration()

                Reads the duration for from the circuit stats object

                :rtype: None on error and value on success

            .. function:: peek_metric()

                Reads metric from the circuit stats object.

                :rtype: None on error and value on success

            .. function:: set_name(name)

                Set the name in the object.

                :rtype: dictionary of error or success response and
                 value with "name" as key

            .. function:: set_circuit_id(circuitID)

                Set the circuit ID name in the circuit stats object.

                :rtype: dictionary of error or success response and
                 value with "circuit-id" as key

        """
        def __init__(self, dictvalues={}):
            super().__init__(pyfos_rest_util.rest_obj_type.circuit_stats,
                             "/rest/running/brocade-extension-tunnel/"
                             "extension-circuit-statistics")
            self.add(pyfos_rest_util.rest_attribute("name",
                     pyfos_type.type_str, None,
                     pyfos_rest_util.REST_ATTRIBUTE_KEY))
            self.add(pyfos_rest_util.rest_attribute("circuit-id",
                     pyfos_type.type_int, None,
                     pyfos_rest_util.REST_ATTRIBUTE_KEY))
            self.add(pyfos_rest_util.rest_attribute("flow-status",
                     pyfos_type.type_int, None,
                     pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
            self.add(pyfos_rest_util.rest_attribute("operational-status",
                     pyfos_type.type_int, None,
                     pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
            self.add(pyfos_rest_util.rest_attribute("metric",
                     pyfos_type.type_int, None,
                     pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
            self.add(pyfos_rest_util.rest_attribute("connection-count",
                     pyfos_type.type_int, None,
                     pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
            self.add(pyfos_rest_util.rest_attribute("duration",
                     pyfos_type.type_int, None,
                     pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
            self.load(dictvalues, 1)
