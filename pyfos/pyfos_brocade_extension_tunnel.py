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

:mod:`pyfos_brocade_extension_tunnel` - PyFOS module for an extension tunnel.
*******************************************************************************
The :mod:`pyfos_extension_tunnel` module provides REST support for
extension tunnel objects.
"""
from pyfos import pyfos_rest_util
from pyfos.pyfos_type import pyfos_type
from pyfos import pyfos_version


class extension_tunnel(pyfos_rest_util.rest_object):
    """Class of extension_tunnel

    Important Class Members:

        +-----------------------+--------------+------------------------------------------------+
        | Attribute Name        | Description  |Frequently Used Functions                       |
        +=======================+==============+================================================+
        |name                   |The slot/port |:func:`peek_name`                               |
        |                       |name of the   |:func:`set_name`                                |
        |                       |VE_Port.      |                                                |
        +-----------------------+--------------+------------------------------------------------+
        |admin-enabled          |The admin     |:func:`peek_admin_enabled`                      |
        |                       |enabled tunnel|:func:`set_admin_enabled`                       |
        |                       |state.        |                                                |
        +-----------------------+--------------+------------------------------------------------+
        |fast-write-enabled     |The fastwrite |:func:`peek_fast_write_enabled`                 |
        |                       |enabled state.|:func:`set_fast_write_enabled`                  |
        +-----------------------+--------------+------------------------------------------------+
        |tape-read              |The tape read |:func:`peek_tape_read`                          |
        |                       |enabled state.|:func:`set_tape_read`                           |
        +-----------------------+--------------+------------------------------------------------+
        |tape-write             |The tape write|:func:`peek_tape_write`                         |
        |                       |enabled       |:func:`set_tape_write`                          |
        |                       |pipelining    |                                                |
        |                       |state.        |                                                |
        +-----------------------+--------------+------------------------------------------------+
        |tunnel-status          |The tunnel    |:func:`peek_tunnel_status`                      |
        |                       |state.        |                                                |
        +-----------------------+--------------+------------------------------------------------+
        |ipsec-enabled          |The IPsec     |:func:`peek_ipsec_enabled`                      |
        |                       |enabled state.|                                                |
        +-----------------------+--------------+------------------------------------------------+
        |ipsec-policy           |The IPsec     |:func:`peek_ipsec_policy`                       |
        |                       |policy for the|:func:`set_ipsec_policy`                        |
        |                       |tunnel.       |                                                |
        +-----------------------+--------------+------------------------------------------------+
        |ha-operational-status  |The HA        |:func:`peek_ha_operational_status`              |
        |                       |operational   |                                                |
        |                       |status of the |                                                |
        |                       |tunnel.       |                                                |
        +-----------------------+--------------+------------------------------------------------+
        |ip-extension           |The IP        |:func:`peek_ip_extension`                       |
        |                       |extension     |:func:`set_ip_extension`                        |
        |                       |enable or     |                                                |
        |                       |disable state.|                                                |
        +-----------------------+--------------+------------------------------------------------+
        |load-level             |The configured|:func:`peek_load_level`                         |
        |                       | load level.  |:func:`set_load_level`                          |
        +-----------------------+--------------+------------------------------------------------+
        |active-load-level      |The negotiated|:func:`peek_active_load_level`                  |
        |                       | load level.  |                                                |
        +-----------------------+--------------+------------------------------------------------+
        |peer-load-level        |The peer load |:func:`peek_peer_load_level`                    |
        |                       |level.        |                                                |
        +-----------------------+--------------+------------------------------------------------+
        |compression-tunnel     |The tunnel    |:func:`peek_compression_tunnel`                 |
        |                       |compressioon  |:func:`set_compression_tunnel`                  |
        |                       |value.        |                                                |
        +-----------------------+--------------+------------------------------------------------+
        |compression-protocol   |The protocol  |:func:`peek_compression_protocol`               |
        |                       |compressioon  |:func:`set_compression_protocol`                |
        |                       |value.        |                                                |
        +-----------------------+--------------+------------------------------------------------+
        |fc-compression         |The FC        |:func:`peek_compression_protocol_fc_compression`|
        |                       |protocol      |:func:`set_compression_protocol_fc_compression` |
        |                       |compressioon  |                                                |
        |                       |value.        |                                                |
        +-----------------------+--------------+------------------------------------------------+
        |ip-compression         |The IP        |:func:`peek_compression_protocol_ip_compression`|
        |                       |protocol      |:func:`set_compression_protocol_ip_compression` |
        |                       |compressioon  |                                                |
        |                       |value.        |                                                |
        +-----------------------+--------------+------------------------------------------------+
        |qos-ratio              |The QOS ratio.|:func:`peek_qos_ratio`                          |
        |                       |              |:func:`set_qos_ratio`                           |
        +-----------------------+--------------+------------------------------------------------+
        |distribution           |The QOS       |:func:`peek_qos_ratio_distribution`             |
        |                       |distribution. |:func:`set_qos_ratio_distribution`              |
        +-----------------------+--------------+------------------------------------------------+
        |distribution-value     |The QOS       |:func:`peek_qos_ratio_distribution_value`       |
        |                       |distribution  |:func:`set_qos_ratio_distribution_value`        |
        |                       |value.        |                                                |
        +-----------------------+--------------+------------------------------------------------+
        |fc-high-qos            |The FC        |:func:`peek_qos_ratio_fc_high_qos`              |
        |                       |QOS high      |:func:`set_qos_ratio_fc_high_qos`               |
        |                       |percentage.   |                                                |
        +-----------------------+--------------+------------------------------------------------+
        |fc-medium-qos          |The FC        |:func:`peek_qos_ratio_fc_medium_qos`            |
        |                       |QOS medium    |:func:`set_qos_ratio_fc_medium_qos`             |
        |                       |percentage.   |                                                |
        +-----------------------+--------------+------------------------------------------------+
        |fc-low-qos             |The FC        |:func:`peek_qos_ratio_fc_low_qos`               |
        |                       |QOS low       |:func:`set_qos_ratio_fc_low_qos`                |
        |                       |percentage.   |                                                |
        +-----------------------+--------------+------------------------------------------------+
        |ip-high-qos            |The IP        |:func:`peek_qos_ratio_ip_high_qos`              |
        |                       |QOS high      |:func:`set_qos_ratio_ip_high_qos`               |
        |                       |percentage.   |                                                |
        +-----------------------+--------------+------------------------------------------------+
        |ip-medium-qos          |The IP        |:func:`peek_qos_ratio_ip_medium_qos`            |
        |                       |QOS medium    |:func:`set_qos_ratio_ip_medium_qos`             |
        |                       |percentage.   |                                                |
        +-----------------------+--------------+------------------------------------------------+
        |ip-low-qos             |The IP        |:func:`peek_qos_ratio_ip_low_qos`               |
        |                       |QOS low       |:func:`set_qos_ratio_ip_low_qos`                |
        |                       |percentage.   |                                                |
        +-----------------------+--------------+------------------------------------------------+


    Important FICON Class Members:

        +-----------------------------+---------------+---------------------------------------------------+
        | Attribute Name              | Description   |Frequently Used Functions                          |
        +=============================+===============+===================================================+
        |ficon                        |Enables or     |:func:`peek_ficon`                                 |
        |                             |disables       |:func:`set_ficon`                                  |
        |                             |FICON.         |                                                   |
        +-----------------------------+---------------+---------------------------------------------------+
        |ficon-xrc-acceleration       |Enables or     |:func:`peek_ficon_xrc_acceleration`                |
        |                             |disables       |:func:`set_ficon_xrc_acceleration`                 |
        |                             |FICON XRC      |                                                   |
        |                             |emulation.     |                                                   |
        +-----------------------------+---------------+---------------------------------------------------+
        |ficon-tape-read-acceleration |Enables or     |:func:`peek_ficon_tape_read_acceleration`          |
        |                             |disables       |:func:`set_ficon_tape_read_acceleration`           |
        |                             |FICON Tape     |                                                   |
        |                             |Read Pipeling. |                                                   |
        +-----------------------------+---------------+---------------------------------------------------+
        |ficon-tape-write-acceleration|Enables or     |:func:`peek_ficon_tape_read_acceleration`          |
        |                             |disables       |:func:`set_ficon_tape_write_acceleration`          |
        |                             |FICON Tape     |                                                   |
        |                             |Write          |                                                   |
        |                             |Pipeling.      |                                                   |
        +-----------------------------+---------------+---------------------------------------------------+
        |ficon-tin-tir-emulation      |Enables or     |:func:`peek_ficon_tin_tir_emulation`               |
        |                             |disables       |:func:`set_ficon_tin_tir_emulation`                |
        |                             |FICON TIN/TIR  |                                                   |
        |                             |emulation.     |                                                   |
        +-----------------------------+---------------+---------------------------------------------------+
        |ficon-device-acknowledgement |Enables or     |:func:`peek_ficon_device_acknowledgement_emulation`|
        |-emulation                   |disables       |:func:`set_ficon_device_acknowledgement_emulation` |
        |                             |FICON Device   |                                                   |
        |                             |Level          |                                                   |
        |                             |Acknowledgement|                                                   |
        |                             |emulation.     |                                                   |
        +-----------------------------+---------------+---------------------------------------------------+
        |ficon-teradata-read-         |Enables or     |:func:`peek_ficon_teradata_read_acceleration`      |
        |acceleration                 |disables       |:func:`set_ficon_teradata_read_acceleration`       |
        |                             |FICON Read     |                                                   |
        |                             |Emulation for  |                                                   |
        |                             |a Teradata     |                                                   |
        |                             |server.        |                                                   |
        +-----------------------------+---------------+---------------------------------------------------+
        |ficon-teradata-write-        |Enables or     |:func:`peek_ficon_teradata_write_acceleration`     |
        |acceleration                 |disables       |:func:`set_ficon_teradata_write_acceleration`      |
        |                             |FICON Write    |                                                   |
        |                             |Emulation for  |                                                   |
        |                             |a Teradata     |                                                   |
        |                             |server.        |                                                   |
        +-----------------------------+---------------+---------------------------------------------------+
        |ficon-tape-write-max-pipe    |The maximum    |:func:`peek_ficon_tape_write_max_pipe`             |
        |                             |number of tape |:func:`set_ficon_tape_write_max_pipe`              |
        |                             |write channel  |                                                   |
        |                             |commands       |                                                   |
        +-----------------------------+---------------+---------------------------------------------------+
        |ficon-tape-read-max-pipe     |The maximum    |:func:`peek_ficon_tape_read_max_pipe`              |
        |                             |number of tape |:func:`set_ficon_tape_read_max_pipe`               |
        |                             |read channel   |                                                   |
        |                             |commands       |                                                   |
        +-----------------------------+---------------+---------------------------------------------------+
        |ficon-tape-read-max-devices  |The maximum    |:func:`peek_ficon_tape_read_max_devices`           |
        |                             |number of      |:func:`set_ficon_tape_read_max_devices`            |
        |                             |concurrent     |                                                   |
        |                             |emulated tape  |                                                   |
        |                             |read           |                                                   |
        |                             |operations.    |                                                   |
        +-----------------------------+---------------+---------------------------------------------------+
        |ficon-tape-write-max-devices |The maximum    |:func:`peek_ficon_tape_write_max_devices`          |
        |                             |number of      |:func:`set_ficon_tape_write_max_devices`           |
        |                             |concurrent     |                                                   |
        |                             |emulated tape  |                                                   |
        |                             |write          |                                                   |
        |                             |operations.    |                                                   |
        +-----------------------------+---------------+---------------------------------------------------+
        |ficon-tape-write-timer       |The time limit |:func:`peek_ficon_tape_write_timer`                |
        |                             |for pipelined  |:func:`set_ficon_tape_write_timer`                 |
        |                             |write chains.  |                                                   |
        |                             |               |                                                   |
        +-----------------------------+---------------+---------------------------------------------------+
        |ficon-tape-write-max-chain   |The maximum    |:func:`peek_ficon_tape_write_max_chain`            |
        |                             |amount of data |:func:`set_ficon_tape_write_max_chain`             |
        |                             |that can be    |                                                   |
        |                             |contained in a |                                                   |
        |                             |single CCW     |                                                   |
        |                             |chain.         |                                                   |
        +-----------------------------+---------------+---------------------------------------------------+
        |ficon-oxid-base              |The base value |:func:`peek_ficon_oxid_base`                       |
        |                             |of an entry    |:func:`set_ficon_oxid_base`                        |
        |                             |pool of 256    |                                                   |
        |                             |OXIDs.         |                                                   |
        +-----------------------------+---------------+---------------------------------------------------+


    *Object Functions*

        .. function:: get()

            Fills the object with values for all the attributes. Once filled,
            the object can be printed using :func:`pyfos_utils.response_print`.

            :param session: The session handler returned
             by :func:`pyfos_auth.login`.
            :rtype: A dictionary of errors or a success response.

    *Attribute Functions*

        .. function:: peek_name()

            Reads the name from the tunnel object.

            :rtype: None on error and a value on success.

        .. function:: peek_admin_enabled()

            Reads the admin enabled/disabled flag from the tunnel object.

            :rtype: None on error and a value on success.

        .. function:: peek_fast_write_enabled()

            Reads the fast write enabled/disabled flag from the tunnel object.

            :rtype: None on error and a value on success.

        .. function:: peek_tape_read()

            Reads the tape read pipelining from the tunnel object.

            :rtype: None on error and a value on success.

        .. function:: peek_tape_write()

            Reads the tape write pipelining from the tunnel object.

            :rtype: None on error and a value on success.

        .. function:: peek_tunnel_status()

            Reads the tunnel status from the tunnel object.

            :rtype: None on error and a value on success.

        .. function:: peek_ipsec_enabled()

            Reads the IPSec enabled/disabled flag from the tunnel object.

            :rtype: None on error and a value on success.

        .. function:: peek_ipsec_policy()

            Reads the IPSec policy name from the tunnel object.

            :rtype: None on error and a value on success.

        .. function:: peek_ha_operational_status()

            Reads the HA operational status from the tunnel object.

            :rtype: None on error and a value on success.

        .. function:: peek_ip_extension()

            Reads the IP extension enabled/disabled flag from \
             the tunnel object.

            :rtype: None on error and a value on success.

        .. function:: peek_load_level()

            Reads the configured load level from the tunnel object.

            :rtype: None on error and a value on success.

        .. function:: peek_active_load_level()

            Reads the active load level from the tunnel object.

            :rtype: None on error and a value on success.

        .. function:: peek_peer_load_level()

            Reads the peer load level from the tunnel object.

            :rtype: None on error and a value on success.

        .. function:: peek_compression_tunnel()

            Reads the tunnel compression level from the tunnel object.

            :rtype: None on error and a value on success.

        .. function:: peek_compression_protocol()

            Reads the tunnel compression for protcol from the tunnel object.

            :rtype: None on error and a value on success.

        .. function:: peek_compression_protocol_fc_compression()

            Reads the FC compression protcol from the tunnel object.

            :rtype: None on error and a value on success.

        .. function:: peek_compression_protocol_ip_compression()

            Reads the IP compression protcol from the tunnel object.

            :rtype: None on error and a value on success.

        .. function:: peek_qos_ratio()

            Reads the QOS ratio from the tunnel object.

            :rtype: None on error and a value on success.

        .. function:: peek_qos_ratio_distribution()

            Reads the QOS ratio distribution from the tunnel object.

            :rtype: None on error and a value on success.

        .. function:: peek_qos_ratio_distribution_value()

            Reads the QOS ratio distribution value from the tunnel object.

            :rtype: None on error and a value on success.

        .. function:: peek_qos_ratio_fc_high_qos()

            Reads the FC high priority QOS ratio from the tunnel object.

            :rtype: None on error and a value on success.

        .. function:: peek_qos_ratio_fc_medium_qos()

            Reads the FC medium priority QOS ratio from the tunnel object.

            :rtype: None on error and a value on success.

        .. function:: peek_qos_ratio_fc_low_qos()

            Reads the FC low priority QOS ratio from the tunnel object.

            :rtype: None on error and a value on success.

        .. function:: peek_qos_ratio_ip_high_qos()

            Reads the IP high priority QOS ratio from the tunnel object.

            :rtype: None on error and a value on success.

        .. function:: peek_qos_ratio_ip_medium_qos()

            Reads the IP medium priority QOS ratio from the tunnel object.

            :rtype: None on error and a value on success.

        .. function:: peek_qos_ratio_ip_low_qos()

            Reads the IP low priority QOS ratio from the tunnel object.

            :rtype: None on error and a value on success.

        .. function:: peek_ficon()

            Reads the FICON enabled/disabled flag from the tunnel object.

            :rtype: None on error and a value on success.

        .. function:: peek_ficon_xrc_acceleration()

            Reads the FICON XRC enabled/disabled flag from the tunnel object.

            :rtype: None on error and a value on success.

        .. function:: peek_ficon_tape_read_acceleration()

            Reads the FICON tape read accelaration from the tunnel object.

            :rtype: None on error and a value on success.

        .. function:: peek_ficon_tape_write_acceleration()

            Reads the FICON tape write accelaration from the tunnel object.

            :rtype: None on error and a value on success.

        .. function:: peek_ficon_tin_tir_emulation()

            Reads the FICON TIN/TIR emulation from the tunnel object.

            :rtype: None on error and a value on success.

        .. function:: peek_ficon_device_acknowledgement_emulation()

            Reads the FICON device acknowledge from the tunnel object.

            :rtype: None on error and a value on success.

        .. function:: peek_ficon_teradata_read_acceleration()

            Reads the FICON teradata read acceleration from the tunnel object.

            :rtype: None on error and a value on success.

        .. function:: peek_ficon_teradata_write_acceleration()

            Reads the FICON teradata write acceleration from the tunnel object.

            :rtype: None on error and a value on success.

        .. function:: peek_ficon_tape_write_max_pipe()

            Reads the FICON tape write max pipe from the tunnel object.

            :rtype: None on error and a value on success.

        .. function:: peek_ficon_tape_read_max_pipe()

            Reads the FICON tape read max pipe from the tunnel object.

            :rtype: None on error and a value on success.

        .. function:: peek_ficon_tape_write_max_devices()

            Reads the FICON tape write maximum number of devices from \
             the tunnel object.

            :rtype: None on error and a value on success.

        .. function:: peek_ficon_tape_read_max_devices()

            Reads the FICON tape read maximum number of devices from \
             the tunnel object.

            :rtype: None on error and a value on success.

        .. function:: peek_ficon_tape_write_timer()

            Reads the FICON tape write timer from the tunnel object.

            :rtype: None on error and a value on success.

        .. function:: peek_ficon_tape_write_max_chain()

            Reads the tape write maximum amount of data contained in a single \
             CCW chain from the tunnel object.

            :rtype: None on error and a value on success.

        .. function:: peek_ficon_oxid_base()

            Reads the FICON OXID base from the tunnel object.

            :rtype: None on error and a value on success.

        .. function:: set_name(name)

            Sets the name in the tunnel object.

            :rtype: A dictionary of errors or a success response and value
             with "name" as the key.

        .. function:: set_admin_enabled(adminEnabled)

            Sets the admin enabled/disabled flag in the tunnel object.

            :rtype: A dictionary of errors or a success response and value
             with "admin-enabled" as the key.

        .. function:: set_fast_write_enabled(fastwrite)

            Sets the fast write enabled/disabled flag in the tunnel object.

            :rtype: A dictionary of errors or a success response and value
             with "fastwrite-enabled" as the key.

        .. function:: set_tape_read(tapeRead)

            Sets the tape read pipelining in the tunnel object.

            :rtype: A dictionary of errors or a success response and value
             with "tape-read" as the key.

        .. function:: set_tape_write(tapeWrite)

            Sets the tape write pipelining in the tunnel object.

            :rtype: A dictionary of errors or a success response and value
             with "tape-write" as the key.

        .. function:: set_ipsec_policy(ipsecPolicyName)

            Sets the IPSec policy for the tunnel object.

            :rtype: A dictionary of errors or a success response and value
             with "ipsec-policy" as the key.

        .. function:: set_ip_extension(name)

            Sets the IP extension enabled flag in the tunnel object.

            :rtype: A dictionary of errors or a success response and value
             with "ipsec-policy" as the key.

        .. function:: set_load_level(loadLevel)

            Sets the load level in the tunnel object.

            :rtype: A dictionary of errors or a success response and value
             with "load-level" as the key.

        .. function:: set_compression_tunnel(tnlCompression)

            Sets the tunnel compression in the tunnel object.

            :rtype: A dictionary of errors or a success response and value
             with "compression-tunnel" as the key.

        .. function:: set_compression_protocol(protcolCompressiondict)

            Sets the protcol level compression in the tunnel object.

            :rtype: A dictionary of errors or a success response and value with
             "compression-protcol" as the key.

        .. function:: set_compression_protocol_fc_compression(fccompression)

            Sets the FC protcol compression in the tunnel object.

            :rtype: A dictionary of errors or a success response and value
             with "fc-compression" as the key.

        .. function:: set_compression_protocol_ip_compression(ipcompression)

            Sets the IP protocol compression in the tunnel object.

            :rtype: A dictionary of errors or a success response and value
             with "ip-compression" as the key.

        .. function:: set_qos_ratio(qosRation)

            Sets the QOS ratio in the tunnel object.

            :rtype: A dictionary of errors or a success response and value
             with "qos-ratio" as the key.

        .. function:: set_qos_ratio_distribution(qosDistribution)

            Sets the QOS distribution in the tunnel object.

            :rtype: A dictionary of errors or a success response and value with
             "distribution" as the key.

        .. function:: set_qos_ratio_distribution_value(qosDistributionVal)

            Sets the QOS distribution value in the tunnel object..

            :rtype: A dictionary of errors or a success response and value with
             "distribution-value" as the key.

        .. function:: set_qos_ratio_fc_high_qos(fcHighQos)

            Sets the FC high QOS ratio in the tunnel object.

            :rtype: A dictionary of errors or a success response and
             value with "fc-high-qos" as the key.

        .. function:: set_qos_ratio_fc_medium_qos(qosRation)

            Sets the FC medium QOS ratio in the tunnel object.

            :rtype: A dictionary of errors or a success response and value
             with "fc-medium-qos" as the key.

        .. function:: set_qos_ratio_fc_low_qos(fcHighQos)

            Sets the FC low QOS ratio in the tunnel object.

            :rtype: A dictionary of errors or a success response and value
             with "fc-low-qos" as the key.

        .. function:: set_qos_ratio_ip_medium_qos(qosRation)

            Set the IP medium QOS ratio in the tunnel object.

            :rtype: A dictionary of errors or a success response and value
             with "ip-medium-qos" as the key.

        .. function:: set_qos_ratio_ip_high_qos(fcHighQos)

            Sets the IP high QOS ratio in the tunnel object.

            :rtype: A dictionary of errors or a success response and value
             with "ip-high-qos" as the key.

        .. function:: set_qos_ratio_ip_low_qos(qosRation)

            Sets the FC low QOS ratio in the tunnel object.

            :rtype: A dictionary of errors or a success response and value
             with "ip-low-qos" as the key.

        .. function:: set_ficon(ficon)

            Writes the FICON enabled/disabled flag from the tunnel object.

            :rtype: A dictionary of errors or a success response and value
             with "ficon" as the key.

        .. function:: set_ficon_xrc_acceleration(xrcAccelaration)

            Writes the FICON XRC enabled flag in the tunnel object

            :rtype: A dictionary of errors or a success response and value
             with "ficon-xrc-acceleration" as the key.

        .. function:: set_ficon_tape_read_acceleration(tapeReadAcc)

            Writes the FICON tape read accelaration from the tunnel object.

            :rtype: A dictionary of errors or a success response and value
             with "ficon-tape-read-acceleration" as the key.

        .. function:: set_ficon_tape_write_acceleration(tapeWriteAcc)

            Writes the FICON tape write accelaration from the tunnel object.

            :rtype: A dictionary of errors or a success response and value
             with "ficon-tape-write-acceleration" as the key.

        .. function:: set_ficon_tin_tir_emulation(tinTirEmul)

            Writes the FICON TIN/TIR emulation from the the tunnel object.

            :rtype: A dictionary of errors or a success response and value
             with "ficon-tin-tir-emulation" as the key.

        .. function:: set_ficon_device_acknowledgement_emulation(deviceAck)

            Writes the FICON device acknowledge from the tunnel object.

            :rtype: A dictionary of errors or a success response and value
             with "ficon-device-acknowledgement-emulation" as the key.

        .. function:: set_ficon_teradata_read_acceleration(terradataReadAcc)

            Writes the FICON teradata read acceleration in the tunnel object

            :rtype: A dictionary of errors or a success response and value with
             "ficon-teradata-read-acceleration" as the key.

        .. function:: set_ficon_teradata_write_acceleration(terradataWriteAcc)

            Writes the FICON teradata write acceleration in the tunnel object

            :rtype: A dictionary of errors or a success response and value with
             "ficon-teradata-write-acceleration" as the key.

        .. function:: set_ficon_tape_write_max_pipe(tapeWriteMaxPipe)

            Writes the FICON tape write max pipe from the tunnel object.

            :rtype: A dictionary of errors or a success response and value with
             "ficon-tape-write-max-pipe" as the key.

        .. function:: set_ficon_tape_read_max_pipe(tapeReadMaxPipe)

            Writes the FICON tape read max pipe from the tunnel object.

            :rtype: A dictionary of errors or a success response and value with
             "ficon-tape-read-max-pipe" as the key.

        .. function:: set_ficon_tape_write_max_devices(tapeWriteMaxdev)

            Writes the FICON tape write maximum number of devices from \
             the tunnel object.

            :rtype: A dictionary of errors or a success response and value with
             "ficon-tape-write-max-devices" as the key.

        .. function:: set_ficon_tape_read_max_devices(tapeWriteMaxdev)

            Writes the FICON tape read maximum number of devices from \
            the tunnel object.

            :rtype: A dictionary of errors or a success response and value
             with "ficon-tape-read-max-devices" as the key.

        .. function:: set_ficon_tape_write_timer(tapeWritetmr)

            Writes the FICON tape write timer in the tunnel object.

            :rtype: A dictionary of errors or a success response and value
             with "ficon-tape-write-timer" as the key.

        .. function:: set_ficon_tape_write_max_chain(tapeWriteMaxchain)

            Writes the FICON tape write maximum abount of data contained in \
             a CCW chain from the tunnel object.

            :rtype: A dictionary of errors or a success response and value with
             "ficon-tape-write-max-chain" as the key.

        .. function:: set_ficon_oxid_base(oxidBase)

            Writes the FICON OXID base from the tunnel object.

            :rtype: A dictionary of errors or a success response and value
             with "ficon-oxid-base" as the key.
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
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
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
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
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

        +------------------+--------------+-------------------------------+
        | Attribute Name   | Description  |Frequently Used Functions      |
        +==================+==============+===============================+
        |name              |The slot/port |:func:`peek_name`              |
        |                  |name of       |:func:`set_name`               |
        |                  |GE_Port.      |                               |
        +------------------+--------------+-------------------------------+
        |flow-status       |The flow      |:func:`peek_flow_status`       |
        |                  |status.       |                               |
        +------------------+--------------+-------------------------------+
        |operational-status|The           |:func:`peek_operational_status`|
        |                  |operational   |                               |
        |                  |status.       |                               |
        +------------------+--------------+-------------------------------+
        |connection-count  |The           |:func:`peek_connection_count`  |
        |                  |connection    |                               |
        |                  |count.        |                               |
        +------------------+--------------+-------------------------------+
        |duration          |The duration. |:func:`peek_duration`          |
        +------------------+--------------+-------------------------------+
        |uncompressed-bytes|The           |:func:`peek_uncompressed_bytes`|
        |                  |uncompressed  |                               |
        |                  |bytes.        |                               |
        +------------------+--------------+-------------------------------+
        |compressed-bytes  |The compressed|:func:`peek_compressed_bytes`  |
        |                  |bytes.        |                               |
        +------------------+--------------+-------------------------------+


    *Object Functions*

        .. function:: get()

            Fills the object with values for all the attributes.
            Once filled, the object can be printed
            using :func:`pyfos_utils.response_print`.

            :param session: The session handler returned
             by :func:`pyfos_auth.login`.
            :rtype: A dictionary of errors or a success response.

    *Attribute Functions*

        .. function:: peek_name()

            Reads the name from the tunnel statistics object.

            :rtype: None on error and a value on success.

        .. function:: peek_flow_status()

            Reads the flow status from the tunnel statistics object.

            :rtype: None on error and a value on success.

        .. function:: peek_operational_status()

            Reads the operational status from the tunnel statistics object.

            :rtype: None on error and a value on success.

        .. function:: peek_connection_count()

            Reads the connection count from the tunnel statistics object.

            :rtype: None on error and a value on success.

        .. function:: peek_duration()

            Reads the duration from the tunnel statistics object

            :rtype: None on error and a value on success.

        .. function:: peek_uncompressed_bytes()

            Reads the uncompressed bytes from the tunnel statistics object.

            :rtype: None on error and a value on success.

        .. function:: peek_compressed_bytes()

            Reads the compressed bytes from the tunnel statistics object.

            :rtype: None on error and a value on success.

        .. function:: set_name(name)

            Sets the name in the object.

            :rtype: A dictionary of errors or a success response and
             value with "name" as the key.

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

    Important Class Members:

        +--------------------------+--------------+---------------------------------------+
        | Attribute Name           | Description  |Frequently Used Functions              |
        +==========================+==============+=======================================+
        |name                      |The slot/port |:func:`peek_name`                      |
        |                          |name of       |:func:`set_name`                       |
        |                          |VE_Port       |                                       |
        +--------------------------+--------------+---------------------------------------+
        |circuit-id                |The circuit   |:func:`peek_circuit_id`                |
        |                          |ID.           |:func:`set_circuit_id`                 |
        +--------------------------+--------------+---------------------------------------+
        |local-ip-address          |The local IP  |:func:`peek_local_ip_address`          |
        |                          |address of the|:func:`set_local_ip_address`           |
        |                          |circuit.      |                                       |
        +--------------------------+--------------+---------------------------------------+
        |remote-ip-address         |The remote IP |:func:`peek_remote_ip_address`         |
        |                          |address of    |:func:`set_remote_ip_address`          |
        |                          |the circuit.  |                                       |
        +--------------------------+--------------+---------------------------------------+
        |local-ha-ip-address       |The local HA  |:func:`peek_local_ha_ip_address`       |
        |                          |IP address of |:func:`set_local_ha_ip_address`        |
        |                          |the circuit.  |                                       |
        +--------------------------+--------------+---------------------------------------+
        |remote-ha-ip-address      |The remote HA |:func:`peek_remote_ha_ip_address`      |
        |                          |IP address of |:func:`set_remote_ha_ip_address`       |
        |                          |the circuit.  |                                       |
        +--------------------------+--------------+---------------------------------------+
        |metric                    |The metric    |:func:`peek_metric`                    |
        |                          |value of the  |:func:`set_metric`                     |
        |                          |circuit.      |                                       |
        +--------------------------+--------------+---------------------------------------+
        |admin-enabled             |The admin     |:func:`peek_admin_enabled`             |
        |                          |enabled tunnel|:func:`set_admin_enabled`              |
        |                          |state.        |                                       |
        +--------------------------+--------------+---------------------------------------+
        |circuit-status            |The circuit   |:func:`peek_circuit_status`            |
        |                          |status.       |                                       |
        +--------------------------+--------------+---------------------------------------+
        |path-mtu-discovered       |The discovered|:func:`peek_path_mtu_discovered`       |
        |                          | path MTU.    |                                       |
        +--------------------------+--------------+---------------------------------------+
        |failover-group-id         |The failover  |:func:`peek_failover_group_id`         |
        |                          |group ID of   |:func:`set_failover_group_id`          |
        |                          |circuit.      |                                       |
        +--------------------------+--------------+---------------------------------------+
        |minimum-communication-rate|The minimum   |:func:`peek_minimum_communication_rate`|
        |                          |communications|:func:`set_minimum_communication_rate` |
        |                          |rate of the   |                                       |
        |                          |circuit.      |                                       |
        +--------------------------+--------------+---------------------------------------+
        |maximum-communication-rate|The maximum   |:func:`peek_maximum_communication_rate`|
        |                          |communications|:func:`set_maximum_communication_rate` |
        |                          |rate of the   |                                       |
        |                          |circuit.      |                                       |
        +--------------------------+--------------+---------------------------------------+
        |vlan-id                   |The VLAN ID   |:func:`peek_vlan_id`                   |
        |                          |of the        |                                       |
        |                          |circuit.      |                                       |
        +--------------------------+--------------+---------------------------------------+
        |l2-cos                    |The Layer 2   |:func:`peek_l2_cos`                    |
        |                          |Class of      |:func:`set_l2_cos`                     |
        |                          |Service.      |                                       |
        +--------------------------+--------------+---------------------------------------+
        |priority-control          |The control   |:func:`peek_l2_cos_priority_control`   |
        |                          |priority.     |:func:`set_l2_cos_priority_control`    |
        +--------------------------+--------------+---------------------------------------+
        |fc-priority-high          |The high      |:func:`peek_l2_cos_fc_priority_high`   |
        |                          |priority FC   |:func:`set_l2_cos_fc_priority_high`    |
        |                          |Layer2 COS.   |                                       |
        +--------------------------+--------------+---------------------------------------+
        |fc-priority-medium        |The medium    |:func:`peek_l2_cos_fc_priority_medium` |
        |                          |priority FC   |:func:`set_l2_cos_fc_priority_medium`  |
        |                          |Layer2 COS.   |                                       |
        +--------------------------+--------------+---------------------------------------+
        |fc-priority-low           |The low       |:func:`peek_l2_cos_fc_priority_low`    |
        |                          |priority FC   |:func:`set_l2_cos_fc_priority_low`     |
        |                          |Layer2 COS.   |                                       |
        +--------------------------+--------------+---------------------------------------+
        |ip-priority-high          |The high      |:func:`peek_l2_cos_ip_priority_high`   |
        |                          |priority IP   |:func:`set_l2_cos_ip_priority_high`    |
        |                          |Layer2 COS.   |                                       |
        +--------------------------+--------------+---------------------------------------+
        |ip-priority-medium        |The medium    |:func:`peek_l2_cos_ip_priority_medium` |
        |                          |priority IP   |:func:`set_l2_cos_ip_priority_medium`  |
        |                          |Layer2 COS.   |                                       |
        +--------------------------+--------------+---------------------------------------+
        |ip-priority-low           |The low       |:func:`peek_l2_cos_ip_priority_low`    |
        |                          |priority IP   |:func:`set_l2_cos_ip_priority_low`     |
        |                          |Layer2 COS.   |                                       |
        +--------------------------+--------------+---------------------------------------+
        |dscp                      |The DSCP.     |:func:`peek_dscp`                      |
        |                          |              |:func:`set_dscp`                       |
        +--------------------------+--------------+---------------------------------------+
        |priority-control          |The DSCP      |:func:`peek_dscp_priority_control`     |
        |                          |control       |:func:`set_dscp_priority_control`      |
        |                          |priority.     |                                       |
        +--------------------------+--------------+---------------------------------------+
        |fc-priority-high          |The high      |:func:`peek_dscp_fc_priority_high`     |
        |                          |priority FC   |:func:`set_dscp_fc_priority_high`      |
        |                          |DSCP.         |                                       |
        +--------------------------+--------------+---------------------------------------+
        |fc-priority-medium        |The medium    |:func:`peek_dscp_fc_priority_medium`   |
        |                          |priority FC   |:func:`set_dscp_fc_priority_medium`    |
        |                          |DSCP.         |                                       |
        +--------------------------+--------------+---------------------------------------+
        |fc-priority-low           |The low       |:func:`peek_dscp_fc_priority_low`      |
        |                          |priority FC   |:func:`set_dscp_fc_priority_low`       |
        |                          |DSCP.         |                                       |
        +--------------------------+--------------+---------------------------------------+
        |ip-priority-high          |The high      |:func:`peek_dscp_ip_priority_high`     |
        |                          |priority IP   |:func:`set_dscp_ip_priority_high`      |
        |                          |DSCP.         |                                       |
        +--------------------------+--------------+---------------------------------------+
        |ip-priority-medium        |The medium    |:func:`peek_dscp_ip_priority_medium`   |
        |                          |priority IP   |:func:`set_dscp_ip_priority_medium`    |
        |                          |DSCP.         |                                       |
        +--------------------------+--------------+---------------------------------------+
        |ip-priority-low           |The low       |:func:`peek_dscp_ip_priority_low`      |
        |                          |priority IP   |:func:`set_dscp_ip_priority_low`       |
        |                          |DSCP.         |                                       |
        +--------------------------+--------------+---------------------------------------+
        |arl-algorithm-mode        |The ARL       |:func:`peek_arl_algorithm_mode`        |
        |                          |alogirithm.   |:func:`set_arl_algorithm_mode`         |
        +--------------------------+--------------+---------------------------------------+
        |keep-alive-timeout        |The keep      |:func:`peek_keep_alive_timeout`        |
        |                          |alive timeout.|                                       |
        +--------------------------+--------------+---------------------------------------+

    *Object Functions*

        .. function:: get()

            Fills the object with values for all the attributes.
            Once filled, the object can be printed
            using :func:`pyfos_utils.response_print`.

            :param session: The session handler returned
             by the :func:`pyfos_auth.login`.
            :rtype: A dictionary of errors or a success response.

    *Attribute Functions*

        .. function:: peek_name()

            Reads the name from the tunnel object.

            :rtype: None on error and a value on success.

        .. function:: peek_circuit_id()

            Reads the circuit ID from the circuit object.

            :rtype: None on error and a value on success.

        .. function:: peek_local_ip_address()

            Reads the local IP address from the circuit object.

            :rtype: None on error and a value on success.

        .. function:: peek_remote_ip_address()

            Reads the remote IP address from the circuit object.

            :rtype: None on error and a value on success.

        .. function:: peek_local_ha_ip_address()

            Reads the local HA IP address from the circuit object.

            :rtype: None on error and a value on success.

        .. function:: peek_remote_ha_ip_address()

            Reads the remote HA IP address from the circuit object.

            :rtype: None on error and a value on success.

        .. function:: peek_metric()

            Reads the metric from the circuit object.

            :rtype: None on error and a value on success.

        .. function:: peek_admin_enabled()

            Reads the admin enabled from the circuit object.

            :rtype: None on error and a value on success.

        .. function:: peek_circuit_status()

            Reads the ciruit status from the circuit object.

            :rtype: None on error and a value on success.

        .. function:: peek_path_mtu_discovered()

            Reads the path MTU discovered from the circuit object.

            :rtype: None on error and a value on success.

        .. function:: peek_failover_group_id()

            Reads the failover group ID from the circuit object.

            :rtype: None on error and a value on success.

        .. function:: peek_minimum_communication_rate()

            Reads the minimum communication rate from the circuit object.

            :rtype: None on error and a value on success.

        .. function:: peek_maximum_communication_rate()

            Reads the maximum communication rate from the circuit object.

            :rtype: None on error and a value on success.

        .. function:: peek_vlan_id()

            Reads the VLAN ID from the circuit object.

            :rtype: None on error and a value on success.

        .. function:: peek_l2_cos()

            Reads the Layer2 COS from the circuit object.

            :rtype: None on error and a value on success.

        .. function:: peek_l2_cos_priority_control()

            Reads the priority control Layer2 COS from the circuit object.

            :rtype: None on error and a value on success.

        .. function:: peek_l2_cos_fc_priority_high()

            Reads the high FC Layer2 COS from the circuit object.

            :rtype: None on error and a value on success.

        .. function:: peek_l2_cos_fc_priority_medium()

            Reads the medium FC Layer2 COS from the circuit object.

            :rtype: None on error and a value on success.

        .. function:: peek_l2_cos_fc_priority_low()

            Reads the low FC Layer2 COS from the circuit object.

            :rtype: None on error and a value on success.

        .. function:: peek_l2_cos_ip_priority_high()

            Reads the high IP Layer2 COS from the circuit object.

            :rtype: None on error and a value on success.

        .. function:: peek_l2_cos_ip_priority_medium()

            Reads the medium IP Layer2 COS from the circuit object.

            :rtype: None on error and a value on success.

        .. function:: peek_l2_cos_ip_priority_low()

            Reads the low IP Layer2 COS from the circuit object.

            :rtype: None on error and a value on success.

        .. function:: peek_dscp()

            Reads the DSCP value from the circuit object.

            :rtype: None on error and a value on success.

        .. function:: peek_dscp_priority_control()

            Reads the priority control DSCP value from the circuit object.

            :rtype: None on error and a value on success.

        .. function:: peek_dscp_fc_priority_high()

            Reads the high FC DSCP value from the circuit object.

            :rtype: None on error and a value on success.

        .. function:: peek_dscp_fc_priority_medium()

            Reads the medium FC DSCP value from the circuit object.

            :rtype: None on error and a value on success.

        .. function:: peek_dscp_fc_priority_low()

            Reads the low FC DSCP value from the circuit object.

            :rtype: None on error and a value on success.

        .. function:: peek_dscp_ip_priority_high()

            Reads the high IP DSCP value from the circuit object.

            :rtype: None on error and a value on success.

        .. function:: peek_dscp_ip_priority_medium()

            Reads the medium IP DSCP value from the circuit object.

            :rtype: None on error and a value on success.

        .. function:: peek_dscp_ip_priority_low()

            Reads the low IP DSCP value from the circuit object.

            :rtype: None on error and a value on success.

        .. function:: peek_arl_algorithm_mode()

            Reads the ARL algorithm from the circuit object.

            :rtype: None on error and a value on success.

        .. function:: peek_keep_alive_timeout()

            Reads the keep alive timeout from the circuit object.

            :rtype: None on error and a value on success.

        .. function:: set_name(name)

            Sets the name in the tunnel object.

            :rtype: A dictionary of errors or a success response and value\
             with "name" as the key.

        .. function:: set_circuit_id(ciruitID)

            Sets the circuit ID in the circuit object.

            :rtype: A dictionary of errors or a success response and value\
             with "circuit-id" as the key.

        .. function:: set_local_ip_address(localIP)

            Sets the local circuit IP address in the circuit object.

            :rtype: A dictionary of errors or a success response and value\
             with "local-ip-address" as the key.

        .. function:: set_remote_ip_address(remoteIP)

            Sets the remote circuit IP address in the circuit object.

            :rtype: A dictionary of errors or a success response and value\
             with "remote-ip-address" as the key.

        .. function:: set_local_ha_ip_address(localHAIP)

            Sets the local HA circuit IP address in the circuit object.

            :rtype: A dictionary of errors or a success response and value\
             with "local-ha-ip-address" as the key.

        .. function:: set_remote_ha_ip_address(remoteHAIP)

            Sets the remote HA circuit IP address in the circuit object.

            :rtype: A dictionary of errors or a success response and value\
             with "remote-ha-ip-address" as the key.

        .. function:: set_metric(metric)

            Sets the metric in the circuit object.

            :rtype: A dictionary of errors or a success response and value\
             with "metric" as the key.

        .. function:: set_admin_enabled(adminState)

            Sets the admin enabled state in the circuit object.

            :rtype: A dictionary of errors or a success response and value with\
             "admin-enabled" as the key.

        .. function:: set_failover_group_id(failoverGroup)

            Sets the failover group ID in the circuit object.

            :rtype: A dictionary of errors or a success response and value with\
             "failover-group-id" as the key.

        .. function:: set_minimum_communication_rate(minCommRate)

            Sets the minimum communication rate in the circuit object.

            :rtype: A dictionary of errors or a success response and value with\
             "minimum-communication-rate" as the key.

        .. function:: set_maximum_communication_rate(maxCommRate)

            Sets the maximum communication rate in the circuit object.

            :rtype: A dictionary of errors or a success response and value with\
             "maximum-communication-rate" as the key.

        .. function:: set_l2_cos(l2cos)

            Sets the Layer2 COS in the circuit object.

            :rtype: A dictionary of errors or a success response and value\
             with "l2-cos" as the key.

        .. function:: set_l2_cos_priority_control(controll2Cos)

            Sets the priority control Layer2 COS in the circuit object.

            :rtype: A dictionary of errors or a success response and value\
             with "priority-control" as the key.

        .. function:: set_l2_cos_fc_priority_high(fcHighl2Cos)

            Sets the high FC Layer2 COS in the circuit object.

            :rtype: A dictionary of errors or a success response and value\
             with "fc-priority-high" as the key.

        .. function:: set_l2_cos_fc_priority_medium(fcMedl2Cos)

            Sets the medium FC Layer2 COS in the circuit object.

            :rtype: A dictionary of errors or a success response and value\
             with "fc-priority-medium" as the key.

        .. function:: set_l2_cos_fc_priority_low(fcLowl2Cos)

            Sets the low FC Layer2 COS in the circuit object.

            :rtype: A dictionary of errors or a success response and value\
             with "fc-priority-low" as the key.

        .. function:: set_l2_cos_ip_priority_high(ipHighl2Cos)

            Sets the high IP Layer2 COS in the circuit object.

            :rtype: A dictionary of errors or a success response and value\
             with "ip-priority-high" as the key.

        .. function:: set_l2_cos_ip_priority_medium(ipMediuml2Cos)

            Sets the medium IP Layer2 COS in the circuit object.

            :rtype: A dictionary of errors or a success response and value\
             with "ip-priority-medium" as the key.

        .. function:: set_l2_cos_ip_priority_low(iplowl2Cos)

            Sets the low IP Layer2 COS in the circuit object.

            :rtype: A dictionary of errors or a success response and value\
             with "ip-priority-low" as the key.

        .. function:: set_dscp(dscp)

            Sets the DSCP in the circuit object.

            :rtype: A dictionary of errors or a success response and
             value with "l2-cos" as the key.

        .. function:: set_dscp_priority_control(controldscp)

            Sets the priority control Layer2 COS in the circuit object.

            :rtype: A dictionary of errors or a success response and value\
             with "priority-control" as the key.

        .. function:: set_dscp_fc_priority_high(fcHighdscp)

            Sets the high FC Layer2 COS in the circuit object.

            :rtype: A dictionary of errors or a success response and value\
             with "fc-priority-high" as the key.

        .. function:: set_dscp_fc_priority_medium(fcMeddscp)

            Sets the medium FC Layer2 COS in the circuit object.

            :rtype: A dictionary of errors or a success response and value\
             with "fc-priority-medium" as the key.

        .. function:: set_dscp_fc_priority_low(fcLowdscp)

            Sets the low FC Layer2 COS in the circuit object.

            :rtype: A dictionary of errors or a success response and value\
             with "fc-priority-low" as the key.

        .. function:: set_dscp_ip_priority_high(ipHighdscp)

            Sets the high IP Layer2 COS in the circuit object.

            :rtype: A dictionary of errors or a success response and value\
             with "ip-priority-high" as the key.

        .. function:: set_dscp_ip_priority_medium(ipMediumdscp)

            Set the medium IP Layer2 COS in the circuit object.

            :rtype: A dictionary of errors or a success response and value\
             with "ip-priority-medium" as the key.

        .. function:: set_dscp_ip_priority_low(iplowdscp)

            Set the low IP Layer2 COS in the circuit object.

            :rtype: A dictionary of errors or a success response and value\
             with "ip-priority-low" as the key.

        .. function:: set_arl_algorithm_mode(arlAlgorithmMode)

            Sets the ARL algorithm in the circuit object.

            :rtype: A dictionary of errors or a success response and value\
             with "arl-algorithm-mode" as the key.

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

    Important Class Members:

        +------------------+--------------+-------------------------------+
        | Attribute Name   | Description  |Frequently Used Functions      |
        +==================+==============+===============================+
        |name              |The slot/port |:func:`peek_name`              |
        |                  |name of       |:func:`set_name`               |
        |                  |GE_Port.      |                               |
        +------------------+--------------+-------------------------------+
        |circuit-id        |The circuit   |:func:`peek_circuit_id`        |
        |                  |ID.           |:func:`set_circuit_id`         |
        +------------------+--------------+-------------------------------+
        |flow-status       |The IPv4/IPv6 |:func:`peek_flow_status`       |
        |                  |address.      |                               |
        +------------------+--------------+-------------------------------+
        |operational-status|The data-path |:func:`peek_operational_status`|
        |                  |processor ID. |                               |
        +------------------+--------------+-------------------------------+
        |connection-count  |The IP prefix |:func:`peek_connection_count`  |
        |                  |length.       |                               |
        +------------------+--------------+-------------------------------+
        |duration          |The maximum   |:func:`peek_duration`          |
        |                  |transmission  |                               |
        |                  |unit.         |                               |
        +------------------+--------------+-------------------------------+
        |metric            |The circuit   |:func:`peek_metric`            |
        |                  |metric value. |                               |
        |                  |              |                               |
        +------------------+--------------+-------------------------------+


    *Object Functions*

        .. function:: get()

            Fills the object with values for all the attributes.
            Once filled, the object can be printed
            using :func:`pyfos_utils.response_print`.

            :param session: The session handler returned
             by :func:`pyfos_auth.login`.
            :rtype: A dictionary of errors or a success response.

    *Attribute Functions*

        .. function:: peek_name()

            Reads the name from the circuit stats object.

            :rtype: None on error and a value on success.

        .. function:: peek_circuit_id()

            Reads the circuit ID from the circuit statistics object.

            :rtype: None on error and a value on success.

        .. function:: peek_flow_status()

            Reads the flow status from the circuit statistics object.

            :rtype: None on error and a value on success.

        .. function:: peek_operational_status()

            Reads the operation status from the circuit statistics object.

            :rtype: None on error and a value on success.

        .. function:: peek_connection_count()

            Reads the connection count from the circuit statistics object.

            :rtype: None on error and a value on success.

        .. function:: peek_duration()

            Reads the duration for from the circuit statistics object

            :rtype: None on error and a value on success.

        .. function:: peek_metric()

            Reads the metric from the circuit statistics object.

            :rtype: None on error and a value on success.

        .. function:: set_name(name)

            Sets the name in the object.

            :rtype: A dictionary of error or a success response and
             value with "name" as the key.

        .. function:: set_circuit_id(circuitID)

            Sets the circuit ID name in the circuit statistics object.

            :rtype: A dictionary of error or a success response and
             value with "circuit-id" as the key.

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
        self.add(pyfos_rest_util.rest_attribute("out-packet-lost",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG,
                 pyfos_version.VER_RANGE_821_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute("out-packet-total",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG,
                 pyfos_version.VER_RANGE_821_and_ABOVE))
        self.load(dictvalues, 1)
