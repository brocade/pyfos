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


# pyfos_brocade_extension_tunnel.py(pyGen v1.0.0)


"""

:mod:`pyfos_brocade_extension_tunnel` - PyFOS module Represents tunnel\
 and circuit configuration and operational status for extension blade or\
 system.
******************************************************************************\
*******************************************************************************
The:mod:`pyfos_brocade_extension_tunnel` The PyFOS module support Represents\
 tunnel and circuit configuration and operational status for extension blade\
 or system.
"""


# Start module imports
from pyfos import pyfos_rest_util
from pyfos.pyfos_type import pyfos_type
from pyfos import pyfos_version as version
# End module imports


class extension_tunnel(pyfos_rest_util.rest_object):

    """Class of extension_tunnel

    *Description extension_tunnel*

        Represents tunnel interface for extension blade or system.

    Important class members of extension_tunnel:

        +--------------------------------------------+--------------------------------+--------------------------------------------------------------+
        | Attribute Name                             | Description                    |  Frequently Used Methods                                     |
        +============================================+================================+==============================================================+
        | name                                       | The name of the interface.     | :func:`peek_name`                                            |
        |                                            |                                | :func:`set_name`                                             |
        +--------------------------------------------+--------------------------------+--------------------------------------------------------------+
        | ficon-tape-write-timer                     | Defines a time limit for       | :func:`peek_ficon_tape_write_timer`                          |
        |                                            | pipelined write chains. This   | :func:`set_ficon_tape_write_timer`                           |
        |                                            | value is specified in          |                                                              |
        |                                            | milliseconds (ms). If a        |                                                              |
        |                                            | pipelined write chain takes    |                                                              |
        |                                            | longer than this value to      |                                                              |
        |                                            | complete, the ending status    |                                                              |
        |                                            | for the next write chain       |                                                              |
        |                                            | will be withheld from the      |                                                              |
        |                                            | channel. This limits           |                                                              |
        |                                            | processing to what the         |                                                              |
        |                                            | network and device can         |                                                              |
        |                                            | support. Too small a value     |                                                              |
        |                                            | limits pipelining              |                                                              |
        |                                            | performance. Too large a       |                                                              |
        |                                            | value results in too much      |                                                              |
        |                                            | data being accepted for one    |                                                              |
        |                                            | device on a path. This field   |                                                              |
        |                                            | is valid only if FICON         |                                                              |
        |                                            | emulation is enabled on the    |                                                              |
        |                                            | specified tunnel.              |                                                              |
        +--------------------------------------------+--------------------------------+--------------------------------------------------------------+
        | ficon-tape-write-max-chain                 | Defines the maximum amount     | :func:`peek_ficon_tape_write_max_chain`                      |
        |                                            | of data that can be            | :func:`set_ficon_tape_write_max_chain`                       |
        |                                            | contained in a single CCW      |                                                              |
        |                                            | chain in bytes. If this        |                                                              |
        |                                            | value is exceeded, emulation   |                                                              |
        |                                            | is suspended. This field is    |                                                              |
        |                                            | valid only if FICON            |                                                              |
        |                                            | emulation is enabled on the    |                                                              |
        |                                            | specified tunnel.              |                                                              |
        +--------------------------------------------+--------------------------------+--------------------------------------------------------------+
        | ficon-tin-tir-emulation                    | Enables or disables FICON      | :func:`peek_ficon_tin_tir_emulation`                         |
        |                                            | TIN/TIR emulation. This        | :func:`set_ficon_tin_tir_emulation`                          |
        |                                            | feature enhances recovery      |                                                              |
        |                                            | when a TIN/TIR exchange        |                                                              |
        |                                            | occurs as part of a channel    |                                                              |
        |                                            | recovery operation during      |                                                              |
        |                                            | tape emulation. This feature   |                                                              |
        |                                            | is enabled by default          |                                                              |
        |                                            | (recommended setting). This    |                                                              |
        |                                            | field is valid only if FICON   |                                                              |
        |                                            | emulation is enabled on the    |                                                              |
        |                                            | specified tunnel. 0 :          |                                                              |
        |                                            | Disable 1 : Enable             |                                                              |
        +--------------------------------------------+--------------------------------+--------------------------------------------------------------+
        | remote-wwn                                 | WWN that can be optionally     | :func:`peek_remote_wwn`                                      |
        |                                            | configured to be verified      | :func:`set_remote_wwn`                                       |
        |                                            | against the WWN of the         |                                                              |
        |                                            | remote FC entity.              |                                                              |
        +--------------------------------------------+--------------------------------+--------------------------------------------------------------+
        | admin-enabled                              | Enables or disables the        | :func:`peek_admin_enabled`                                   |
        |                                            | tunnel VE port. Admin status   | :func:`set_admin_enabled`                                    |
        |                                            | is enabled by default. 0 :     |                                                              |
        |                                            | Disabled 1 : Enabled           |                                                              |
        +--------------------------------------------+--------------------------------+--------------------------------------------------------------+
        | ficon-tape-read-max-pipe                   | Defines the maximum number     | :func:`peek_ficon_tape_read_max_pipe`                        |
        |                                            | of tape read channel           | :func:`set_ficon_tape_read_max_pipe`                         |
        |                                            | commands (CCWs) that can       |                                                              |
        |                                            | enter the read pipeline for    |                                                              |
        |                                            | a single device whether all    |                                                              |
        |                                            | the CCWs are bundled in a      |                                                              |
        |                                            | single channel program or in   |                                                              |
        |                                            | multiple channel programs.     |                                                              |
        |                                            | The setting has significance   |                                                              |
        |                                            | only for host (channel)        |                                                              |
        |                                            | initiated operations at this   |                                                              |
        |                                            | side and will not affect       |                                                              |
        |                                            | tape write operations          |                                                              |
        |                                            | initiated by hosts             |                                                              |
        |                                            | (channels) attached at the     |                                                              |
        |                                            | opposite side. Too small of    |                                                              |
        |                                            | a value will result in poor    |                                                              |
        |                                            | performance. The value         |                                                              |
        |                                            | should be chosen based upon    |                                                              |
        |                                            | the typical tape channel       |                                                              |
        |                                            | program that requires          |                                                              |
        |                                            | optimum performance. This      |                                                              |
        |                                            | field is valid only if FICON   |                                                              |
        |                                            | emulation is enabled on the    |                                                              |
        |                                            | specified tunnel.              |                                                              |
        +--------------------------------------------+--------------------------------+--------------------------------------------------------------+
        | ficon-read-block-id-emulation              | Enables or disables FICON      | :func:`peek_ficon_read_block_id_emulation`                   |
        |                                            | read Tape Read Block ID        | :func:`set_ficon_read_block_id_emulation`                    |
        |                                            | emulation. This feature        |                                                              |
        |                                            | permits FICON write channel    |                                                              |
        |                                            | programs containing embedded   |                                                              |
        |                                            | read block ID commands         |                                                              |
        |                                            | (CCWs) with a byte count of    |                                                              |
        |                                            | exactly four bytes to be       |                                                              |
        |                                            | processed as emulated          |                                                              |
        |                                            | commands during write          |                                                              |
        |                                            | emulation processes. This      |                                                              |
        |                                            | field is valid only if FICON   |                                                              |
        |                                            | emulation is enabled on the    |                                                              |
        |                                            | specified tunnel. 0 :          |                                                              |
        |                                            | Disable 1 : Enable             |                                                              |
        +--------------------------------------------+--------------------------------+--------------------------------------------------------------+
        | ip-extension                               | Enables or disables IP         | :func:`peek_ip_extension`                                    |
        |                                            | Extension capability of a      | :func:`set_ip_extension`                                     |
        |                                            | tunnel. Possible values: 0 :   |                                                              |
        |                                            | Disable 1 : Enable             |                                                              |
        +--------------------------------------------+--------------------------------+--------------------------------------------------------------+
        | ficon-tape-write-max-pipe                  | Defines the maximum number     | :func:`peek_ficon_tape_write_max_pipe`                       |
        |                                            | of tape write channel          | :func:`set_ficon_tape_write_max_pipe`                        |
        |                                            | commands (CCWs) that can       |                                                              |
        |                                            | enter the write pipeline for   |                                                              |
        |                                            | a single device whether all    |                                                              |
        |                                            | the CCWs are bundled in a      |                                                              |
        |                                            | single channel program or in   |                                                              |
        |                                            | multiple channel programs.     |                                                              |
        |                                            | The setting has significance   |                                                              |
        |                                            | only for host (channel)        |                                                              |
        |                                            | initiated operations at this   |                                                              |
        |                                            | side and will not affect       |                                                              |
        |                                            | tape write operations          |                                                              |
        |                                            | initiated by hosts             |                                                              |
        |                                            | (channels) attached at the     |                                                              |
        |                                            | opposite side. Too small of    |                                                              |
        |                                            | a value will result in poor    |                                                              |
        |                                            | performance. The value         |                                                              |
        |                                            | should be chosen based upon    |                                                              |
        |                                            | the typical tape channel       |                                                              |
        |                                            | program that requires          |                                                              |
        |                                            | optimum performance. This      |                                                              |
        |                                            | field is valid only if FICON   |                                                              |
        |                                            | emulation is enabled on the    |                                                              |
        |                                            | specified tunnel.              |                                                              |
        +--------------------------------------------+--------------------------------+--------------------------------------------------------------+
        | ficon-device-acknowledgement-emulation     | Enables or disables FICON      | :func:`peek_ficon_device_acknowledgement_emulation`          |
        |                                            | Device Level Acknowledgement   | :func:`set_ficon_device_acknowledgement_emulation`           |
        |                                            | emulation. This feature is     |                                                              |
        |                                            | applicable to both FICON       |                                                              |
        |                                            | Disk and Tape                  |                                                              |
        |                                            | configurations. The feature    |                                                              |
        |                                            | removes one network round      |                                                              |
        |                                            | trip for exchanges that end    |                                                              |
        |                                            | with a Device Level            |                                                              |
        |                                            | Acknowledgement frame from     |                                                              |
        |                                            | the device. This feature is    |                                                              |
        |                                            | enabled by default             |                                                              |
        |                                            | (recommended setting). This    |                                                              |
        |                                            | field is valid only if FICON   |                                                              |
        |                                            | emulation is enabled on the    |                                                              |
        |                                            | specified tunnel. 0 :          |                                                              |
        |                                            | Disable 1 : Enable             |                                                              |
        +--------------------------------------------+--------------------------------+--------------------------------------------------------------+
        | load-level                                 | Specifies spillover or         | :func:`peek_load_level`                                      |
        |                                            | failover load-balancing        | :func:`set_load_level`                                       |
        |                                            | method. The default            |                                                              |
        |                                            | load-balancing method is       |                                                              |
        |                                            | 'failover'. Possible values    |                                                              |
        |                                            | are:  'default', 'failover'    |                                                              |
        |                                            | and 'spillover'                |                                                              |
        +--------------------------------------------+--------------------------------+--------------------------------------------------------------+
        | ficon-teradata-write-acceleration          | Enables or disables FICON      | :func:`peek_ficon_teradata_write_acceleration`               |
        |                                            | Write Emulation for a          | :func:`set_ficon_teradata_write_acceleration`                |
        |                                            | Teradata server on the         |                                                              |
        |                                            | specified extension tunnel.    |                                                              |
        |                                            | This field is valid only if    |                                                              |
        |                                            | FICON emulation is enabled     |                                                              |
        |                                            | on the specified tunnel. 0 :   |                                                              |
        |                                            | Disable 1 : Enable             |                                                              |
        +--------------------------------------------+--------------------------------+--------------------------------------------------------------+
        | ficon-oxid-base                            | Defines the base value of an   | :func:`peek_ficon_oxid_base`                                 |
        |                                            | entry pool of 256 OXIDs        | :func:`set_ficon_oxid_base`                                  |
        |                                            | supplied to                    |                                                              |
        |                                            | emulation-generated            |                                                              |
        |                                            | exchanges. It should fall      |                                                              |
        |                                            | outside the range used by      |                                                              |
        |                                            | FICON channels and devices     |                                                              |
        |                                            | to avoid conflicts. The        |                                                              |
        |                                            | default value is 0x9000        |                                                              |
        |                                            | (recommended setting). This    |                                                              |
        |                                            | field is valid only if FICON   |                                                              |
        |                                            | emulation is enabled on the    |                                                              |
        |                                            | specified tunnel.              |                                                              |
        +--------------------------------------------+--------------------------------+--------------------------------------------------------------+
        | ficon-tape-write-max-devices               | Defines the maximum number     | :func:`peek_ficon_tape_write_max_devices`                    |
        |                                            | of concurrent emulated tape    | :func:`set_ficon_tape_write_max_devices`                     |
        |                                            | write operations. As           |                                                              |
        |                                            | concurrency increases, the     |                                                              |
        |                                            | value of emulation             |                                                              |
        |                                            | decreases. Excessive           |                                                              |
        |                                            | concurrency has the            |                                                              |
        |                                            | potential to oversubscribe     |                                                              |
        |                                            | packet data memory. The        |                                                              |
        |                                            | setting has significance       |                                                              |
        |                                            | only for host (channel)        |                                                              |
        |                                            | initiated operations at this   |                                                              |
        |                                            | side and will not affect       |                                                              |
        |                                            | tape write operations          |                                                              |
        |                                            | initiated by hosts             |                                                              |
        |                                            | (channels) attached. This      |                                                              |
        |                                            | field is valid only if FICON   |                                                              |
        |                                            | emulation is enabled on the    |                                                              |
        |                                            | specified tunnel.              |                                                              |
        +--------------------------------------------+--------------------------------+--------------------------------------------------------------+
        | ficon-xrc-acceleration                     | Enables or disables FICON      | :func:`peek_ficon_xrc_acceleration`                          |
        |                                            | XRC emulation. FICON XRC       | :func:`set_ficon_xrc_acceleration`                           |
        |                                            | Emulation allows XRC (IBM      |                                                              |
        |                                            | eXtendedRemote Copy, also      |                                                              |
        |                                            | known as IBM z/OS              |                                                              |
        |                                            | GlobalMirroring) to operate    |                                                              |
        |                                            | effectively at extended        |                                                              |
        |                                            | distances. This field is       |                                                              |
        |                                            | valid only if FICON            |                                                              |
        |                                            | emulation is enabled on the    |                                                              |
        |                                            | specified tunnel. 0 :          |                                                              |
        |                                            | Disable 1 : Enable             |                                                              |
        +--------------------------------------------+--------------------------------+--------------------------------------------------------------+
        | ficon-tape-read-acceleration               | Enables or disables FICON      | :func:`peek_ficon_tape_read_acceleration`                    |
        |                                            | Tape Read Pipelining. This     | :func:`set_ficon_tape_read_acceleration`                     |
        |                                            | feature improves performance   |                                                              |
        |                                            | for certain applications       |                                                              |
        |                                            | when reading from FICON tape   |                                                              |
        |                                            | over extended distances.       |                                                              |
        |                                            | This field is valid only if    |                                                              |
        |                                            | FICON emulation is enabled     |                                                              |
        |                                            | on the specified tunnel. 0 :   |                                                              |
        |                                            | Disable 1 : Enable             |                                                              |
        +--------------------------------------------+--------------------------------+--------------------------------------------------------------+
        | ficon-teradata-read-acceleration           | Enables or disables FICON      | :func:`peek_ficon_teradata_read_acceleration`                |
        |                                            | Read Emulation for a           | :func:`set_ficon_teradata_read_acceleration`                 |
        |                                            | Teradata server on the         |                                                              |
        |                                            | specified extension tunnel.    |                                                              |
        |                                            | This field is valid only if    |                                                              |
        |                                            | FICON emulation is enabled     |                                                              |
        |                                            | on the specified tunnel. 0 :   |                                                              |
        |                                            | Disable 1 : Enable             |                                                              |
        +--------------------------------------------+--------------------------------+--------------------------------------------------------------+
        | ipsec-policy                               | Sets the Internet Protocol     | :func:`peek_ipsec_policy`                                    |
        |                                            | Security (IPsec) on the        | :func:`set_ipsec_policy`                                     |
        |                                            | specified tunnel to use the    |                                                              |
        |                                            | specified IPsec Policy, or     |                                                              |
        |                                            | to disable IPsec for the       |                                                              |
        |                                            | tunnel if the 'none' operand   |                                                              |
        |                                            | is used. Policy name can be    |                                                              |
        |                                            | 1 to 31 characters in          |                                                              |
        |                                            | length.                        |                                                              |
        +--------------------------------------------+--------------------------------+--------------------------------------------------------------+
        | tape-read                                  | Enables read Tape Pipelining   | :func:`peek_tape_read`                                       |
        |                                            | (FCIP FastWrite must also be   | :func:`set_tape_read`                                        |
        |                                            | enabled). Read Tape            |                                                              |
        |                                            | Pipelining can not be          |                                                              |
        |                                            | enabled if write Tape          |                                                              |
        |                                            | Pipelining is disabled. 0 :    |                                                              |
        |                                            | Disable 1 : Enable             |                                                              |
        +--------------------------------------------+--------------------------------+--------------------------------------------------------------+
        | fast-write-enabled                         | Disables or enables the FCIP   | :func:`peek_fast_write_enabled`                              |
        |                                            | FastWrite on the specified     | :func:`set_fast_write_enabled`                               |
        |                                            | extension tunnel. 0 :          |                                                              |
        |                                            | Disable 1 : Enable             |                                                              |
        +--------------------------------------------+--------------------------------+--------------------------------------------------------------+
        | ficon-tape-write-acceleration              | Enables or disables FICON      | :func:`peek_ficon_tape_write_acceleration`                   |
        |                                            | Tape Write Pipelining. This    | :func:`set_ficon_tape_write_acceleration`                    |
        |                                            | feature improves the           |                                                              |
        |                                            | performance of certain         |                                                              |
        |                                            | applications when writing to   |                                                              |
        |                                            | tape over extended             |                                                              |
        |                                            | distances. This field is       |                                                              |
        |                                            | valid only if FICON            |                                                              |
        |                                            | emulation is enabled on the    |                                                              |
        |                                            | specified tunnel. 0 :          |                                                              |
        |                                            | Disable 1 : Enable             |                                                              |
        +--------------------------------------------+--------------------------------+--------------------------------------------------------------+
        | user-friendly-name                         | Specifies a description for    | :func:`peek_user_friendly_name`                              |
        |                                            | the specified tunnel.          | :func:`set_user_friendly_name`                               |
        +--------------------------------------------+--------------------------------+--------------------------------------------------------------+
        | ficon                                      | Enables or disables FICON      | :func:`peek_ficon`                                           |
        |                                            | emulation on the specified     | :func:`set_ficon`                                            |
        |                                            | extension tunnel. 0 :          |                                                              |
        |                                            | Disable 1 : Enable             |                                                              |
        +--------------------------------------------+--------------------------------+--------------------------------------------------------------+
        | tape-write                                 | Enables write Tape             | :func:`peek_tape_write`                                      |
        |                                            | Pipelining (FCIP FastWrite     | :func:`set_tape_write`                                       |
        |                                            | must also be enabled). 0 :     |                                                              |
        |                                            | Disable 1 : Enable             |                                                              |
        +--------------------------------------------+--------------------------------+--------------------------------------------------------------+
        | compression-tunnel                         | Configures compression on      | :func:`peek_compression_tunnel`                              |
        |                                            | the specified tunnel. The      | :func:`set_compression_tunnel`                               |
        |                                            | value (5 : Fast Deflate) is    |                                                              |
        |                                            | only supported on SX6 and      |                                                              |
        |                                            | 7840. 0 : Off (Compression     |                                                              |
        |                                            | disabled) 3 : Deflate 4 :      |                                                              |
        |                                            | Aggressive Deflate 5 : Fast    |                                                              |
        |                                            | Deflate                        |                                                              |
        +--------------------------------------------+--------------------------------+--------------------------------------------------------------+
        | ficon-tape-read-max-devices                | Defines the maximum number     | :func:`peek_ficon_tape_read_max_devices`                     |
        |                                            | of concurrent emulated tape    | :func:`set_ficon_tape_read_max_devices`                      |
        |                                            | read operations. As            |                                                              |
        |                                            | concurrency increases, the     |                                                              |
        |                                            | value of emulation             |                                                              |
        |                                            | decreases. Excessive           |                                                              |
        |                                            | concurrency has the            |                                                              |
        |                                            | potential to oversubscribe     |                                                              |
        |                                            | packet data memory. The        |                                                              |
        |                                            | setting has significance       |                                                              |
        |                                            | only for host (channel)        |                                                              |
        |                                            | initiated operations at this   |                                                              |
        |                                            | side and will not affect       |                                                              |
        |                                            | tape read operations           |                                                              |
        |                                            | initiated by hosts             |                                                              |
        |                                            | (channels) attached at the     |                                                              |
        |                                            | opposite side. This field is   |                                                              |
        |                                            | valid only if FICON            |                                                              |
        |                                            | emulation is enabled on the    |                                                              |
        |                                            | specified tunnel.              |                                                              |
        +--------------------------------------------+--------------------------------+--------------------------------------------------------------+
        | qos-ratio                                  | Specifies tunnel bandwidth     | :func:`peek_qos_ratio`                                       |
        |                                            | distribution values.           | :func:`set_qos_ratio`                                        |
        +--------------------------------------------+--------------------------------+--------------------------------------------------------------+
        | compression-protocol                       | This property denotes the      | :func:`peek_compression_protocol`                            |
        |                                            | FC/IP compression mode for     | :func:`set_compression_protocol`                             |
        |                                            | the tunnel.                    |                                                              |
        +--------------------------------------------+--------------------------------+--------------------------------------------------------------+
        | distribution                               | Specifies tunnel bandwidth     | :func:`peek_qos_ratio_distribution`                          |
        |                                            | distribution mode: 1 :         | :func:`set_qos_ratio_distribution`                           |
        |                                            | Default, for FCIP mode 2 :     |                                                              |
        |                                            | Protocol, for Hybrid mode      |                                                              |
        +--------------------------------------------+--------------------------------+--------------------------------------------------------------+
        | ip-medium-qos                              | Specifies QoS percentage for   | :func:`peek_qos_ratio_ip_medium_qos`                         |
        |                                            | IP medium priority. Each       | :func:`set_qos_ratio_ip_medium_qos`                          |
        |                                            | priority can have a minimum    |                                                              |
        |                                            | of 10%. The sum of             |                                                              |
        |                                            | percentages must equal 100%.   |                                                              |
        |                                            | This field is valid only if    |                                                              |
        |                                            | IP extension is enabled on     |                                                              |
        |                                            | the tunnel.                    |                                                              |
        +--------------------------------------------+--------------------------------+--------------------------------------------------------------+
        | fc-high-qos                                | Specifies QoS percentage for   | :func:`peek_qos_ratio_fc_high_qos`                           |
        |                                            | FC high priority. Each         | :func:`set_qos_ratio_fc_high_qos`                            |
        |                                            | priority can have a minimum    |                                                              |
        |                                            | of 10%. The sum of             |                                                              |
        |                                            | percentages must equal 100%.   |                                                              |
        +--------------------------------------------+--------------------------------+--------------------------------------------------------------+
        | fc-compression                             | Specifies FC compression on    | :func:`peek_compression_protocol_fc_compression`             |
        |                                            | the specified tunnel. It       | :func:`set_compression_protocol_fc_compression`              |
        |                                            | will return -1 when default    |                                                              |
        |                                            | or otherwise the configured    |                                                              |
        |                                            | compression set for FC         |                                                              |
        |                                            | protocol. The value (5 :       |                                                              |
        |                                            | Fast Deflate) is only          |                                                              |
        |                                            | supported on SX6 and 7840.     |                                                              |
        |                                            | Specifies one of the           |                                                              |
        |                                            | following values for           |                                                              |
        |                                            | compression_level: -1 :        |                                                              |
        |                                            | Default (Enable default        |                                                              |
        |                                            | compression level specified    |                                                              |
        |                                            | in   compression-tunnel        |                                                              |
        |                                            | attribute) 0 : Off             |                                                              |
        |                                            | (Compression disabled) 3 :     |                                                              |
        |                                            | Deflate 4 : Aggressive         |                                                              |
        |                                            | Deflate 5 : Fast Deflate       |                                                              |
        +--------------------------------------------+--------------------------------+--------------------------------------------------------------+
        | ip-low-qos                                 | Specifies QoS percentage for   | :func:`peek_qos_ratio_ip_low_qos`                            |
        |                                            | IP low priority. Each          | :func:`set_qos_ratio_ip_low_qos`                             |
        |                                            | priority can have a minimum    |                                                              |
        |                                            | of 10%. The sum of             |                                                              |
        |                                            | percentages must equal 100%.   |                                                              |
        |                                            | This field is valid only if    |                                                              |
        |                                            | IP extension is enabled on     |                                                              |
        |                                            | the tunnel.                    |                                                              |
        +--------------------------------------------+--------------------------------+--------------------------------------------------------------+
        | distribution-value                         | Specifies values for           | :func:`peek_qos_ratio_distribution_value`                    |
        |                                            | bandwidth distribution: '' -   | :func:`set_qos_ratio_distribution_value`                     |
        |                                            | for FCIP mode (zero-length     |                                                              |
        |                                            | string is used for FCIP        |                                                              |
        |                                            | mode),                         |                                                              |
        |                                            | '<Percentage-for-FC-           |                                                              |
        |                                            | bandwidth>,                    |                                                              |
        |                                            | <Percentage-for-IP-            |                                                              |
        |                                            | bandwidth>' - for Hybrid       |                                                              |
        |                                            | mode. For example, the value   |                                                              |
        |                                            | in case of Hybrid mode will    |                                                              |
        |                                            | be '50,50'.                    |                                                              |
        +--------------------------------------------+--------------------------------+--------------------------------------------------------------+
        | fc-low-qos                                 | Specifies QoS percentage for   | :func:`peek_qos_ratio_fc_low_qos`                            |
        |                                            | FC low priority. Each          | :func:`set_qos_ratio_fc_low_qos`                             |
        |                                            | priority can have a minimum    |                                                              |
        |                                            | of 10%. The sum of             |                                                              |
        |                                            | percentages must equal 100%.   |                                                              |
        +--------------------------------------------+--------------------------------+--------------------------------------------------------------+
        | ip-compression                             | Specifies IP compression on    | :func:`peek_compression_protocol_ip_compression`             |
        |                                            | the specified tunnel. It       | :func:`set_compression_protocol_ip_compression`              |
        |                                            | will return -1 when default    |                                                              |
        |                                            | or otherwise the configured    |                                                              |
        |                                            | compression set for IP         |                                                              |
        |                                            | protocol. Specifies one of     |                                                              |
        |                                            | the following values for       |                                                              |
        |                                            | compression_level: -1 :        |                                                              |
        |                                            | Default (Enable default        |                                                              |
        |                                            | compression level specified    |                                                              |
        |                                            | in   compression-tunnel        |                                                              |
        |                                            | attribute) 0 : Off             |                                                              |
        |                                            | (Compression disabled) 3 :     |                                                              |
        |                                            | Deflate 4 : Aggressive         |                                                              |
        |                                            | Deflate                        |                                                              |
        +--------------------------------------------+--------------------------------+--------------------------------------------------------------+
        | ip-high-qos                                | Specifies QoS percentage for   | :func:`peek_qos_ratio_ip_high_qos`                           |
        |                                            | IP high priority. Each         | :func:`set_qos_ratio_ip_high_qos`                            |
        |                                            | priority can have a minimum    |                                                              |
        |                                            | of 10%. The sum of             |                                                              |
        |                                            | percentages must equal 100%.   |                                                              |
        |                                            | This field is valid only if    |                                                              |
        |                                            | IP extension is enabled on     |                                                              |
        |                                            | the tunnel.                    |                                                              |
        +--------------------------------------------+--------------------------------+--------------------------------------------------------------+
        | fc-medium-qos                              | Specifies QoS percentage for   | :func:`peek_qos_ratio_fc_medium_qos`                         |
        |                                            | FC medium priority. Each       | :func:`set_qos_ratio_fc_medium_qos`                          |
        |                                            | priority can have a minimum    |                                                              |
        |                                            | of 10%. The sum of             |                                                              |
        |                                            | percentages must equal 100%.   |                                                              |
        +--------------------------------------------+--------------------------------+--------------------------------------------------------------+
        | local-wwn                                  | Specifies the WWN of the       | :func:`peek_local_wwn`                                       |
        |                                            | local FC entity.               |                                                              |
        +--------------------------------------------+--------------------------------+--------------------------------------------------------------+
        | tunnel-status                              | Tunnel operational status.     | :func:`peek_tunnel_status`                                   |
        |                                            |                                |                                                              |
        +--------------------------------------------+--------------------------------+--------------------------------------------------------------+
        | ha-operational-status                      | HA Oper Status of a tunnel:    | :func:`peek_ha_operational_status`                           |
        |                                            | 8 : HA Online 9 : HA Offline   |                                                              |
        |                                            | 10 : HA Ready                  |                                                              |
        +--------------------------------------------+--------------------------------+--------------------------------------------------------------+
        | active-load-level                          | Load level value currently     | :func:`peek_active_load_level`                               |
        |                                            | active on the tunnel.          |                                                              |
        +--------------------------------------------+--------------------------------+--------------------------------------------------------------+
        | ipsec-enabled                              | Specifies the disabled or      | :func:`peek_ipsec_enabled`                                   |
        |                                            | enabled state of Internet      |                                                              |
        |                                            | Protocol Security (IPsec) on   |                                                              |
        |                                            | the specified tunnel: 0 :      |                                                              |
        |                                            | IPsec is disabled on the       |                                                              |
        |                                            | tunnel 1 : IPsec is enabled    |                                                              |
        |                                            | on the tunnel                  |                                                              |
        +--------------------------------------------+--------------------------------+--------------------------------------------------------------+
        | peer-wwn                                   | Specifies the WWN of the       | :func:`peek_peer_wwn`                                        |
        |                                            | remote FC entity.              |                                                              |
        +--------------------------------------------+--------------------------------+--------------------------------------------------------------+
        | peer-load-level                            | Specifies the load level       | :func:`peek_peer_load_level`                                 |
        |                                            | configured on the peer-end     |                                                              |
        |                                            | of the tunnel.                 |                                                              |
        +--------------------------------------------+--------------------------------+--------------------------------------------------------------+
        | qos-ratio                                  | Specifies tunnel bandwidth     | :func:`peek_qos_ratio`                                       |
        |                                            | distribution values.           | :func:`set_qos_ratio`                                        |
        +--------------------------------------------+--------------------------------+--------------------------------------------------------------+
        | compression-protocol                       | This property denotes the      | :func:`peek_compression_protocol`                            |
        |                                            | FC/IP compression mode for     | :func:`set_compression_protocol`                             |
        |                                            | the tunnel.                    |                                                              |
        +--------------------------------------------+--------------------------------+--------------------------------------------------------------+

    *Object functions for extension_tunnel*

    .. function:: get()

        Get the instances of class "extension_tunnel from switch. The object
         can be printed using :func:`pyfos_utils.response_print`.

        :param session: The session handler returned by
         :func:`pyfos_auth.login`.

        :rtype: A dictionary of errors or a success response.


    *Class functions for extension_tunnel*

        .. function:: peek_name()

            Reads the value assigned to name in the object.

            :rtype: None on error and a value on success.


        .. function:: set_name(value)

            Set the value of name in the object.

            :rtype: A dictionary of error or a success response and a value
             with "name" as the key


        .. function:: peek_ficon_tape_write_timer()

            Reads the value assigned to ficon-tape-write-timer in the
             object.

            :rtype: None on error and a value on success.


        .. function:: set_ficon_tape_write_timer(value)

            Set the value of ficon-tape-write-timer in the object.

            :rtype: A dictionary of error or a success response and a value
             with "ficon-tape-write-timer" as the key


        .. function:: peek_ficon_tape_write_max_chain()

            Reads the value assigned to ficon-tape-write-max-chain in the
             object.

            :rtype: None on error and a value on success.


        .. function:: set_ficon_tape_write_max_chain(value)

            Set the value of ficon-tape-write-max-chain in the object.

            :rtype: A dictionary of error or a success response and a value
             with "ficon-tape-write-max-chain" as the key


        .. function:: peek_ficon_tin_tir_emulation()

            Reads the value assigned to ficon-tin-tir-emulation in the
             object.

            :rtype: None on error and a value on success.


        .. function:: set_ficon_tin_tir_emulation(value)

            Set the value of ficon-tin-tir-emulation in the object.

            :rtype: A dictionary of error or a success response and a value
             with "ficon-tin-tir-emulation" as the key


        .. function:: peek_remote_wwn()

            Reads the value assigned to remote-wwn in the object.

            :rtype: None on error and a value on success.


        .. function:: set_remote_wwn(value)

            Set the value of remote-wwn in the object.

            :rtype: A dictionary of error or a success response and a value
             with "remote-wwn" as the key


        .. function:: peek_admin_enabled()

            Reads the value assigned to admin-enabled in the object.

            :rtype: None on error and a value on success.


        .. function:: set_admin_enabled(value)

            Set the value of admin-enabled in the object.

            :rtype: A dictionary of error or a success response and a value
             with "admin-enabled" as the key


        .. function:: peek_ficon_tape_read_max_pipe()

            Reads the value assigned to ficon-tape-read-max-pipe in the
             object.

            :rtype: None on error and a value on success.


        .. function:: set_ficon_tape_read_max_pipe(value)

            Set the value of ficon-tape-read-max-pipe in the object.

            :rtype: A dictionary of error or a success response and a value
             with "ficon-tape-read-max-pipe" as the key


        .. function:: peek_ficon_read_block_id_emulation()

            Reads the value assigned to ficon-read-block-id-emulation in the
             object.

            :rtype: None on error and a value on success.


        .. function:: set_ficon_read_block_id_emulation(value)

            Set the value of ficon-read-block-id-emulation in the object.

            :rtype: A dictionary of error or a success response and a value
             with "ficon-read-block-id-emulation" as the key


        .. function:: peek_ip_extension()

            Reads the value assigned to ip-extension in the object.

            :rtype: None on error and a value on success.


        .. function:: set_ip_extension(value)

            Set the value of ip-extension in the object.

            :rtype: A dictionary of error or a success response and a value
             with "ip-extension" as the key


        .. function:: peek_ficon_tape_write_max_pipe()

            Reads the value assigned to ficon-tape-write-max-pipe in the
             object.

            :rtype: None on error and a value on success.


        .. function:: set_ficon_tape_write_max_pipe(value)

            Set the value of ficon-tape-write-max-pipe in the object.

            :rtype: A dictionary of error or a success response and a value
             with "ficon-tape-write-max-pipe" as the key


        .. function:: peek_ficon_device_acknowledgement_emulation()

            Reads the value assigned to
             ficon-device-acknowledgement-emulation in the object.

            :rtype: None on error and a value on success.


        .. function:: set_ficon_device_acknowledgement_emulation(value)

            Set the value of ficon-device-acknowledgement-emulation in the
             object.

            :rtype: A dictionary of error or a success response and a value
             with "ficon-device-acknowledgement-emulation" as the key


        .. function:: peek_load_level()

            Reads the value assigned to load-level in the object.

            :rtype: None on error and a value on success.


        .. function:: set_load_level(value)

            Set the value of load-level in the object.

            :rtype: A dictionary of error or a success response and a value
             with "load-level" as the key


        .. function:: peek_ficon_teradata_write_acceleration()

            Reads the value assigned to ficon-teradata-write-acceleration in
             the object.

            :rtype: None on error and a value on success.


        .. function:: set_ficon_teradata_write_acceleration(value)

            Set the value of ficon-teradata-write-acceleration in the
             object.

            :rtype: A dictionary of error or a success response and a value
             with "ficon-teradata-write-acceleration" as the key


        .. function:: peek_ficon_oxid_base()

            Reads the value assigned to ficon-oxid-base in the object.

            :rtype: None on error and a value on success.


        .. function:: set_ficon_oxid_base(value)

            Set the value of ficon-oxid-base in the object.

            :rtype: A dictionary of error or a success response and a value
             with "ficon-oxid-base" as the key


        .. function:: peek_ficon_tape_write_max_devices()

            Reads the value assigned to ficon-tape-write-max-devices in the
             object.

            :rtype: None on error and a value on success.


        .. function:: set_ficon_tape_write_max_devices(value)

            Set the value of ficon-tape-write-max-devices in the object.

            :rtype: A dictionary of error or a success response and a value
             with "ficon-tape-write-max-devices" as the key


        .. function:: peek_ficon_xrc_acceleration()

            Reads the value assigned to ficon-xrc-acceleration in the
             object.

            :rtype: None on error and a value on success.


        .. function:: set_ficon_xrc_acceleration(value)

            Set the value of ficon-xrc-acceleration in the object.

            :rtype: A dictionary of error or a success response and a value
             with "ficon-xrc-acceleration" as the key


        .. function:: peek_ficon_tape_read_acceleration()

            Reads the value assigned to ficon-tape-read-acceleration in the
             object.

            :rtype: None on error and a value on success.


        .. function:: set_ficon_tape_read_acceleration(value)

            Set the value of ficon-tape-read-acceleration in the object.

            :rtype: A dictionary of error or a success response and a value
             with "ficon-tape-read-acceleration" as the key


        .. function:: peek_ficon_teradata_read_acceleration()

            Reads the value assigned to ficon-teradata-read-acceleration in
             the object.

            :rtype: None on error and a value on success.


        .. function:: set_ficon_teradata_read_acceleration(value)

            Set the value of ficon-teradata-read-acceleration in the object.

            :rtype: A dictionary of error or a success response and a value
             with "ficon-teradata-read-acceleration" as the key


        .. function:: peek_ipsec_policy()

            Reads the value assigned to ipsec-policy in the object.

            :rtype: None on error and a value on success.


        .. function:: set_ipsec_policy(value)

            Set the value of ipsec-policy in the object.

            :rtype: A dictionary of error or a success response and a value
             with "ipsec-policy" as the key


        .. function:: peek_tape_read()

            Reads the value assigned to tape-read in the object.

            :rtype: None on error and a value on success.


        .. function:: set_tape_read(value)

            Set the value of tape-read in the object.

            :rtype: A dictionary of error or a success response and a value
             with "tape-read" as the key


        .. function:: peek_fast_write_enabled()

            Reads the value assigned to fast-write-enabled in the object.

            :rtype: None on error and a value on success.


        .. function:: set_fast_write_enabled(value)

            Set the value of fast-write-enabled in the object.

            :rtype: A dictionary of error or a success response and a value
             with "fast-write-enabled" as the key


        .. function:: peek_ficon_tape_write_acceleration()

            Reads the value assigned to ficon-tape-write-acceleration in the
             object.

            :rtype: None on error and a value on success.


        .. function:: set_ficon_tape_write_acceleration(value)

            Set the value of ficon-tape-write-acceleration in the object.

            :rtype: A dictionary of error or a success response and a value
             with "ficon-tape-write-acceleration" as the key


        .. function:: peek_user_friendly_name()

            Reads the value assigned to user-friendly-name in the object.

            :rtype: None on error and a value on success.


        .. function:: set_user_friendly_name(value)

            Set the value of user-friendly-name in the object.

            :rtype: A dictionary of error or a success response and a value
             with "user-friendly-name" as the key


        .. function:: peek_ficon()

            Reads the value assigned to ficon in the object.

            :rtype: None on error and a value on success.


        .. function:: set_ficon(value)

            Set the value of ficon in the object.

            :rtype: A dictionary of error or a success response and a value
             with "ficon" as the key


        .. function:: peek_tape_write()

            Reads the value assigned to tape-write in the object.

            :rtype: None on error and a value on success.


        .. function:: set_tape_write(value)

            Set the value of tape-write in the object.

            :rtype: A dictionary of error or a success response and a value
             with "tape-write" as the key


        .. function:: peek_compression_tunnel()

            Reads the value assigned to compression-tunnel in the object.

            :rtype: None on error and a value on success.


        .. function:: set_compression_tunnel(value)

            Set the value of compression-tunnel in the object.

            :rtype: A dictionary of error or a success response and a value
             with "compression-tunnel" as the key


        .. function:: peek_ficon_tape_read_max_devices()

            Reads the value assigned to ficon-tape-read-max-devices in the
             object.

            :rtype: None on error and a value on success.


        .. function:: set_ficon_tape_read_max_devices(value)

            Set the value of ficon-tape-read-max-devices in the object.

            :rtype: A dictionary of error or a success response and a value
             with "ficon-tape-read-max-devices" as the key


        .. function:: peek_qos_ratio()

            Reads the value assigned to qos-ratio in the object.

            :rtype: None on error and a value on success.


        .. function:: set_qos_ratio(value)

            Set the value of qos-ratio in the object.

            :rtype: A dictionary of error or a success response and a value
             with "qos-ratio" as the key


        .. function:: peek_compression_protocol()

            Reads the value assigned to compression-protocol in the object.

            :rtype: None on error and a value on success.


        .. function:: set_compression_protocol(value)

            Set the value of compression-protocol in the object.

            :rtype: A dictionary of error or a success response and a value
             with "compression-protocol" as the key


        .. function:: peek_qos_ratio_distribution()

            Reads the value assigned to distribution in the object.

            :rtype: None on error and a value on success.


        .. function:: set_qos_ratio_distribution(value)

            Set the value of distribution in the object.

            :rtype: A dictionary of error or a success response and a value
             with "distribution" as the key


        .. function:: peek_qos_ratio_ip_medium_qos()

            Reads the value assigned to ip-medium-qos in the object.

            :rtype: None on error and a value on success.


        .. function:: set_qos_ratio_ip_medium_qos(value)

            Set the value of ip-medium-qos in the object.

            :rtype: A dictionary of error or a success response and a value
             with "ip-medium-qos" as the key


        .. function:: peek_qos_ratio_fc_high_qos()

            Reads the value assigned to fc-high-qos in the object.

            :rtype: None on error and a value on success.


        .. function:: set_qos_ratio_fc_high_qos(value)

            Set the value of fc-high-qos in the object.

            :rtype: A dictionary of error or a success response and a value
             with "fc-high-qos" as the key


        .. function:: peek_compression_protocol_fc_compression()

            Reads the value assigned to fc-compression in the object.

            :rtype: None on error and a value on success.


        .. function:: set_compression_protocol_fc_compression(value)

            Set the value of fc-compression in the object.

            :rtype: A dictionary of error or a success response and a value
             with "fc-compression" as the key


        .. function:: peek_qos_ratio_ip_low_qos()

            Reads the value assigned to ip-low-qos in the object.

            :rtype: None on error and a value on success.


        .. function:: set_qos_ratio_ip_low_qos(value)

            Set the value of ip-low-qos in the object.

            :rtype: A dictionary of error or a success response and a value
             with "ip-low-qos" as the key


        .. function:: peek_qos_ratio_distribution_value()

            Reads the value assigned to distribution-value in the object.

            :rtype: None on error and a value on success.


        .. function:: set_qos_ratio_distribution_value(value)

            Set the value of distribution-value in the object.

            :rtype: A dictionary of error or a success response and a value
             with "distribution-value" as the key


        .. function:: peek_qos_ratio_fc_low_qos()

            Reads the value assigned to fc-low-qos in the object.

            :rtype: None on error and a value on success.


        .. function:: set_qos_ratio_fc_low_qos(value)

            Set the value of fc-low-qos in the object.

            :rtype: A dictionary of error or a success response and a value
             with "fc-low-qos" as the key


        .. function:: peek_compression_protocol_ip_compression()

            Reads the value assigned to ip-compression in the object.

            :rtype: None on error and a value on success.


        .. function:: set_compression_protocol_ip_compression(value)

            Set the value of ip-compression in the object.

            :rtype: A dictionary of error or a success response and a value
             with "ip-compression" as the key


        .. function:: peek_qos_ratio_ip_high_qos()

            Reads the value assigned to ip-high-qos in the object.

            :rtype: None on error and a value on success.


        .. function:: set_qos_ratio_ip_high_qos(value)

            Set the value of ip-high-qos in the object.

            :rtype: A dictionary of error or a success response and a value
             with "ip-high-qos" as the key


        .. function:: peek_qos_ratio_fc_medium_qos()

            Reads the value assigned to fc-medium-qos in the object.

            :rtype: None on error and a value on success.


        .. function:: set_qos_ratio_fc_medium_qos(value)

            Set the value of fc-medium-qos in the object.

            :rtype: A dictionary of error or a success response and a value
             with "fc-medium-qos" as the key


        .. function:: peek_local_wwn()

            Reads the value assigned to local-wwn in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_tunnel_status()

            Reads the value assigned to tunnel-status in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_ha_operational_status()

            Reads the value assigned to ha-operational-status in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_active_load_level()

            Reads the value assigned to active-load-level in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_ipsec_enabled()

            Reads the value assigned to ipsec-enabled in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_peer_wwn()

            Reads the value assigned to peer-wwn in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_peer_load_level()

            Reads the value assigned to peer-load-level in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_qos_ratio()

            Reads the value assigned to qos-ratio in the object.

            :rtype: None on error and a value on success.


        .. function:: set_qos_ratio(value)

            Set the value of qos-ratio in the object.

            :rtype: A dictionary of error or a success response and a value
             with "qos-ratio" as the key


        .. function:: peek_compression_protocol()

            Reads the value assigned to compression-protocol in the object.

            :rtype: None on error and a value on success.


        .. function:: set_compression_protocol(value)

            Set the value of compression-protocol in the object.

            :rtype: A dictionary of error or a success response and a value
             with "compression-protocol" as the key


    """

    def __init__(self, dictvalues=None):

        clsuri = "/rest" + "/running" + "/brocade-extension-tunnel" +\
                 "/extension-tunnel"
        clstype = pyfos_rest_util.rest_obj_type.tunnel
        super().__init__(clstype, clsuri)

        self.add(pyfos_rest_util.rest_attribute("name", pyfos_type.type_str,
                 None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute("ficon-tape-write-timer",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("ficon-tape-write-max-chain",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("ficon-tin-tir-emulation",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("remote-wwn",
                 pyfos_type.type_wwn, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("admin-enabled",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("ficon-tape-read-max-pipe",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "ficon-read-block-id-emulation", pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("ip-extension",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("ficon-tape-write-max-pipe",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "ficon-device-acknowledgement-emulation",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("load-level",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "ficon-teradata-write-acceleration", pyfos_type.type_int,
                 None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("ficon-oxid-base",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "ficon-tape-write-max-devices", pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("ficon-xrc-acceleration",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "ficon-tape-read-acceleration", pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "ficon-teradata-read-acceleration", pyfos_type.type_int,
                 None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("ipsec-policy",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("tape-read",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("fast-write-enabled",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "ficon-tape-write-acceleration", pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("user-friendly-name",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("ficon", pyfos_type.type_int,
                 None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("tape-write",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("compression-tunnel",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("ficon-tape-read-max-devices",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("qos-ratio",
                 pyfos_type.type_na, dict(),
                 pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute("compression-protocol",
                 pyfos_type.type_na, dict(),
                 pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute("distribution",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG), ['qos-ratio'])
        self.add(pyfos_rest_util.rest_attribute("ip-medium-qos",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG), ['qos-ratio'])
        self.add(pyfos_rest_util.rest_attribute("fc-high-qos",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG), ['qos-ratio'])
        self.add(pyfos_rest_util.rest_attribute("fc-compression",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG),
                 ['compression-protocol'])
        self.add(pyfos_rest_util.rest_attribute("ip-low-qos",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG), ['qos-ratio'])
        self.add(pyfos_rest_util.rest_attribute("distribution-value",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG), ['qos-ratio'])
        self.add(pyfos_rest_util.rest_attribute("fc-low-qos",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG), ['qos-ratio'])
        self.add(pyfos_rest_util.rest_attribute("ip-compression",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG),
                 ['compression-protocol'])
        self.add(pyfos_rest_util.rest_attribute("ip-high-qos",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG), ['qos-ratio'])
        self.add(pyfos_rest_util.rest_attribute("fc-medium-qos",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG), ['qos-ratio'])
        self.add(pyfos_rest_util.rest_attribute("local-wwn",
                 pyfos_type.type_wwn, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("tunnel-status",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("ha-operational-status",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("active-load-level",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("ipsec-enabled",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("peer-wwn",
                 pyfos_type.type_wwn, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("peer-load-level",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.load(dictvalues, 1)


class extension_circuit(pyfos_rest_util.rest_object):

    """Class of extension_circuit

    *Description extension_circuit*

        Represents circuit interface for extension blade or system.

    Important class members of extension_circuit:

        +--------------------------------+--------------------------------------------------------+--------------------------------------------------+
        | Attribute Name                 | Description                                            |  Frequently Used Methods                         |
        +================================+========================================================+==================================================+
        | circuit-id                     | Circuit identifier. In case of 7810 the range is       | :func:`peek_circuit_id`                          |
        |                                | restricted to 0..5.                                    | :func:`set_circuit_id`                           |
        +--------------------------------+--------------------------------------------------------+--------------------------------------------------+
        | name                           | The name of the interface.                             | :func:`peek_name`                                |
        |                                |                                                        | :func:`set_name`                                 |
        +--------------------------------+--------------------------------------------------------+--------------------------------------------------+
        | local-ha-ip-address            | Specifies the local HA IP address to use for the       | :func:`peek_local_ha_ip_address`                 |
        |                                | circuit. This HA configuration is only supported on    | :func:`set_local_ha_ip_address`                  |
        |                                | 7840 and SX6.                                          |                                                  |
        +--------------------------------+--------------------------------------------------------+--------------------------------------------------+
        | local-ip-address               | Specifies the local IP address to use for the          | :func:`peek_local_ip_address`                    |
        |                                | circuit.                                               | :func:`set_local_ip_address`                     |
        +--------------------------------+--------------------------------------------------------+--------------------------------------------------+
        | keep-alive-timeout             | Specifies the keep alive timeout in milliseconds. If   | :func:`peek_keep_alive_timeout`                  |
        |                                | the tunnel does not already have FICON Emulation       | :func:`set_keep_alive_timeout`                   |
        |                                | enabled, circuits created on the tunnel default to     |                                                  |
        |                                | the the keep alive timeout of 6000 ms (6 seconds).     |                                                  |
        |                                | If FICON emulation is enabled on the extension         |                                                  |
        |                                | tunnel when a circuit is created, the keep alive       |                                                  |
        |                                | timeout defaults to 1000 ms (1 seconds).               |                                                  |
        +--------------------------------+--------------------------------------------------------+--------------------------------------------------+
        | maximum-communication-rate     | Maximum Communication Rate of the tunnel in kbps.      | :func:`peek_maximum_communication_rate`          |
        |                                | You can set a minimum and a maximum for the            | :func:`set_maximum_communication_rate`           |
        |                                | committed rate to configure the tunnel for Adaptive    |                                                  |
        |                                | Rate Limiting (ARL), which allows for a more           |                                                  |
        |                                | effective sharing of bandwidth between applications.   |                                                  |
        |                                | The maximum committed rate can be no larger than       |                                                  |
        |                                | five times the minimum committed rate, and both        |                                                  |
        |                                | sides of the circuit must have matching                |                                                  |
        |                                | configurations. The range on 7810 is restricted to     |                                                  |
        |                                | 0|20000..2500000.                                      |                                                  |
        +--------------------------------+--------------------------------------------------------+--------------------------------------------------+
        | remote-ha-ip-address           | Specifies the remote HA IP address to use for the      | :func:`peek_remote_ha_ip_address`                |
        |                                | circuit.                                               | :func:`set_remote_ha_ip_address`                 |
        +--------------------------------+--------------------------------------------------------+--------------------------------------------------+
        | is-admin-enabled               | Is Circuit admin status enabled. Default: true,        | :func:`peek_is_admin_enabled`                    |
        |                                | Values supported are true/false. false - Disabled      | :func:`set_is_admin_enabled`                     |
        |                                | true - Enabled                                         |                                                  |
        +--------------------------------+--------------------------------------------------------+--------------------------------------------------+
        | failover-group-id              | Specifies the failover group ID for the configured     | :func:`peek_failover_group_id`                   |
        |                                | circuit. The circuit failover groups must be defined   | :func:`set_failover_group_id`                    |
        |                                | at both ends of the extension tunnel and each          |                                                  |
        |                                | failover group should include at least one metric 0    |                                                  |
        |                                | and one metric 1 circuit. If all metric 0 circuits     |                                                  |
        |                                | in the failover group go down, the transmission        |                                                  |
        |                                | fails over to the metric 1 circuits in the group. If   |                                                  |
        |                                | all metric 0 circuits in a tunnel go down, by          |                                                  |
        |                                | default the traffic will run over the metric 1         |                                                  |
        |                                | circuits. This field has no meaning when load level    |                                                  |
        |                                | for the tunnel is 'spillover'.                         |                                                  |
        +--------------------------------+--------------------------------------------------------+--------------------------------------------------+
        | arl-algorithm-mode             | Specifies Adaptive Rate Limiting (ARL) algorithm.      | :func:`peek_arl_algorithm_mode`                  |
        |                                | Allowable modes are: 0 : auto 1 : reset 2 :            | :func:`set_arl_algorithm_mode`                   |
        |                                | step-down 3 : timed-step-down                          |                                                  |
        +--------------------------------+--------------------------------------------------------+--------------------------------------------------+
        | metric                         | Specifies the metric for the configured circuit. A     | :func:`peek_metric`                              |
        |                                | lower metric assigns a higher priority to the          | :func:`set_metric`                               |
        |                                | circuit. As data is flowing through the extension      |                                                  |
        |                                | tunnel, it automatically traverses the lowest metric   |                                                  |
        |                                | cost circuits. For example, if a tunnel has four       |                                                  |
        |                                | circuits, three of which are set to a metric of 0      |                                                  |
        |                                | and one is set to a metric of 1, all data will flow    |                                                  |
        |                                | over the metric 0 circuits. This parameter is          |                                                  |
        |                                | meaningful only, if you configure more than one        |                                                  |
        |                                | circuit. 0 : Primary 1 : Failover                      |                                                  |
        +--------------------------------+--------------------------------------------------------+--------------------------------------------------+
        | minimum-communication-rate     | Minimum Communication Rate of the tunnel in kbps.      | :func:`peek_minimum_communication_rate`          |
        |                                | You can set a minimum and a maximum for the            | :func:`set_minimum_communication_rate`           |
        |                                | committed rate to configure the tunnel for Adaptive    |                                                  |
        |                                | Rate Limiting (ARL), which allows for a more           |                                                  |
        |                                | effective sharing of bandwidth between applications.   |                                                  |
        |                                | The maximum committed rate can be no larger than       |                                                  |
        |                                | five times the minimum committed rate, and both        |                                                  |
        |                                | sides of the circuit must have matching                |                                                  |
        |                                | configurations. The range on 7810 is restricted to     |                                                  |
        |                                | 0|20000..2500000.                                      |                                                  |
        +--------------------------------+--------------------------------------------------------+--------------------------------------------------+
        | remote-ip-address              | Specifies the remote IP address to use for the         | :func:`peek_remote_ip_address`                   |
        |                                | circuit.                                               | :func:`set_remote_ip_address`                    |
        +--------------------------------+--------------------------------------------------------+--------------------------------------------------+
        | admin-enabled                  | Is Circuit admin status enabled. Default: 1, Values    | :func:`peek_admin_enabled`                       |
        |                                | supported are 0..5 However user is not allowed to      | :func:`set_admin_enabled`                        |
        |                                | set all of them as some of them are Internal RO        |                                                  |
        |                                | states. Supported configure values are Disabled and    |                                                  |
        |                                | Enabled only. Internal values are Config,              |                                                  |
        |                                | HA-disabled, Fenced and Test. 0 - Disabled 1 -         |                                                  |
        |                                | Enabled 2 - Config 3 - HA-disabled 4 - Fenced 5 -      |                                                  |
        |                                | Test. Deprecated: Please use 'is-admin-enabled' leaf   |                                                  |
        |                                | instead.                                               |                                                  |
        +--------------------------------+--------------------------------------------------------+--------------------------------------------------+
        | dscp                           | The Internet Protocol (IP) Differentiated Services     | :func:`peek_dscp`                                |
        |                                | Code Point markings for frames.                        | :func:`set_dscp`                                 |
        +--------------------------------+--------------------------------------------------------+--------------------------------------------------+
        | l2-cos                         | L2 class of service/priority as defined by IEEE        | :func:`peek_l2_cos`                              |
        |                                | 802.1p for the tunnel.                                 | :func:`set_l2_cos`                               |
        +--------------------------------+--------------------------------------------------------+--------------------------------------------------+
        | ip-priority-high               | Specifies the DSCP value for IP High Priority. The     | :func:`peek_dscp_ip_priority_high`               |
        |                                | range is 0 to 63.                                      | :func:`set_dscp_ip_priority_high`                |
        +--------------------------------+--------------------------------------------------------+--------------------------------------------------+
        | fc-priority-high               | Specifies the DSCP value for FC High Priority. The     | :func:`peek_dscp_fc_priority_high`               |
        |                                | range is 0 to 63.                                      | :func:`set_dscp_fc_priority_high`                |
        +--------------------------------+--------------------------------------------------------+--------------------------------------------------+
        | ip-priority-high               | Specifies the L2CoS value for IP High Priority         | :func:`peek_l2_cos_ip_priority_high`             |
        |                                | Traffic.                                               | :func:`set_l2_cos_ip_priority_high`              |
        +--------------------------------+--------------------------------------------------------+--------------------------------------------------+
        | fc-priority-medium             | Specifies the L2CoS value for FC Medium Priority       | :func:`peek_l2_cos_fc_priority_medium`           |
        |                                | Traffic.                                               | :func:`set_l2_cos_fc_priority_medium`            |
        +--------------------------------+--------------------------------------------------------+--------------------------------------------------+
        | fc-priority-low                | Specifies the DSCP value for FC Low Priority. The      | :func:`peek_dscp_fc_priority_low`                |
        |                                | range is 0 to 63.                                      | :func:`set_dscp_fc_priority_low`                 |
        +--------------------------------+--------------------------------------------------------+--------------------------------------------------+
        | ip-priority-low                | Specifies the L2CoS value for IP Low Priority          | :func:`peek_l2_cos_ip_priority_low`              |
        |                                | Traffic.                                               | :func:`set_l2_cos_ip_priority_low`               |
        +--------------------------------+--------------------------------------------------------+--------------------------------------------------+
        | fc-priority-high               | Specifies the L2CoS value for FC High Priority         | :func:`peek_l2_cos_fc_priority_high`             |
        |                                | Traffic.                                               | :func:`set_l2_cos_fc_priority_high`              |
        +--------------------------------+--------------------------------------------------------+--------------------------------------------------+
        | fc-priority-low                | Specifies the L2CoS value for FC Low Priority          | :func:`peek_l2_cos_fc_priority_low`              |
        |                                | Traffic.                                               | :func:`set_l2_cos_fc_priority_low`               |
        +--------------------------------+--------------------------------------------------------+--------------------------------------------------+
        | priority-control               | Specifies the Layer 2 Class of Service (L2CoS) value   | :func:`peek_l2_cos_priority_control`             |
        |                                | for F-Class Traffic. This priority setting controls    | :func:`set_l2_cos_priority_control`              |
        |                                | connections between switches.                          |                                                  |
        +--------------------------------+--------------------------------------------------------+--------------------------------------------------+
        | ip-priority-medium             | Specifies the DSCP value for IP Medium Priority. The   | :func:`peek_dscp_ip_priority_medium`             |
        |                                | range is 0 to 63.                                      | :func:`set_dscp_ip_priority_medium`              |
        +--------------------------------+--------------------------------------------------------+--------------------------------------------------+
        | priority-control               | Specifies the DSCP value for F-Class Traffic. The      | :func:`peek_dscp_priority_control`               |
        |                                | range is 0 to 63.                                      | :func:`set_dscp_priority_control`                |
        +--------------------------------+--------------------------------------------------------+--------------------------------------------------+
        | ip-priority-medium             | Specifies the L2CoS value for IP Medium Priority       | :func:`peek_l2_cos_ip_priority_medium`           |
        |                                | Traffic.                                               | :func:`set_l2_cos_ip_priority_medium`            |
        +--------------------------------+--------------------------------------------------------+--------------------------------------------------+
        | fc-priority-medium             | Specifies the DSCP value for FC Medium Priority. The   | :func:`peek_dscp_fc_priority_medium`             |
        |                                | range is 0 to 63.                                      | :func:`set_dscp_fc_priority_medium`              |
        +--------------------------------+--------------------------------------------------------+--------------------------------------------------+
        | ip-priority-low                | Specifies the DSCP value for IP Low Priority. The      | :func:`peek_dscp_ip_priority_low`                |
        |                                | range is 0 to 63.                                      | :func:`set_dscp_ip_priority_low`                 |
        +--------------------------------+--------------------------------------------------------+--------------------------------------------------+
        | path-mtu-discovered            | Discovered Path MTU value. This field is valid only    | :func:`peek_path_mtu_discovered`                 |
        |                                | when Path MTU discovery is enabled.                    |                                                  |
        +--------------------------------+--------------------------------------------------------+--------------------------------------------------+
        | vlan-id                        | Specifies the VLAN ID. When not set, this value will   | :func:`peek_vlan_id`                             |
        |                                | show up as 0.                                          |                                                  |
        +--------------------------------+--------------------------------------------------------+--------------------------------------------------+
        | admin-status                   | Is Circuit admin status enabled. Default: 1, Values    | :func:`peek_admin_status`                        |
        |                                | supported are 0..5 However user is not allowed to      |                                                  |
        |                                | set all of them as some of them are Internal RO        |                                                  |
        |                                | states. Supported configure values are Disabled and    |                                                  |
        |                                | Enabled only. Internal values are Config,              |                                                  |
        |                                | HA-disabled, Fenced and Test. 0 - Disabled 1 -         |                                                  |
        |                                | Enabled 2 - Config 3 - HA-disabled 4 - Fenced 5 -      |                                                  |
        |                                | Test.                                                  |                                                  |
        +--------------------------------+--------------------------------------------------------+--------------------------------------------------+
        | circuit-status                 | Circuit operational status                             | :func:`peek_circuit_status`                      |
        |                                |                                                        |                                                  |
        +--------------------------------+--------------------------------------------------------+--------------------------------------------------+

    *Object functions for extension_circuit*

    .. function:: get()

        Get the instances of class "extension_circuit from switch. The object
         can be printed using :func:`pyfos_utils.response_print`.

        :param session: The session handler returned by
         :func:`pyfos_auth.login`.

        :rtype: A dictionary of errors or a success response.


    *Class functions for extension_circuit*

        .. function:: peek_circuit_id()

            Reads the value assigned to circuit-id in the object.

            :rtype: None on error and a value on success.


        .. function:: set_circuit_id(value)

            Set the value of circuit-id in the object.

            :rtype: A dictionary of error or a success response and a value
             with "circuit-id" as the key


        .. function:: peek_name()

            Reads the value assigned to name in the object.

            :rtype: None on error and a value on success.


        .. function:: set_name(value)

            Set the value of name in the object.

            :rtype: A dictionary of error or a success response and a value
             with "name" as the key


        .. function:: peek_local_ha_ip_address()

            Reads the value assigned to local-ha-ip-address in the object.

            :rtype: None on error and a value on success.


        .. function:: set_local_ha_ip_address(value)

            Set the value of local-ha-ip-address in the object.

            :rtype: A dictionary of error or a success response and a value
             with "local-ha-ip-address" as the key


        .. function:: peek_local_ip_address()

            Reads the value assigned to local-ip-address in the object.

            :rtype: None on error and a value on success.


        .. function:: set_local_ip_address(value)

            Set the value of local-ip-address in the object.

            :rtype: A dictionary of error or a success response and a value
             with "local-ip-address" as the key


        .. function:: peek_keep_alive_timeout()

            Reads the value assigned to keep-alive-timeout in the object.

            :rtype: None on error and a value on success.


        .. function:: set_keep_alive_timeout(value)

            Set the value of keep-alive-timeout in the object.

            :rtype: A dictionary of error or a success response and a value
             with "keep-alive-timeout" as the key


        .. function:: peek_maximum_communication_rate()

            Reads the value assigned to maximum-communication-rate in the
             object.

            :rtype: None on error and a value on success.


        .. function:: set_maximum_communication_rate(value)

            Set the value of maximum-communication-rate in the object.

            :rtype: A dictionary of error or a success response and a value
             with "maximum-communication-rate" as the key


        .. function:: peek_remote_ha_ip_address()

            Reads the value assigned to remote-ha-ip-address in the object.

            :rtype: None on error and a value on success.


        .. function:: set_remote_ha_ip_address(value)

            Set the value of remote-ha-ip-address in the object.

            :rtype: A dictionary of error or a success response and a value
             with "remote-ha-ip-address" as the key


        .. function:: peek_is_admin_enabled()

            Reads the value assigned to is-admin-enabled in the object.

            :rtype: None on error and a value on success.


        .. function:: set_is_admin_enabled(value)

            Set the value of is-admin-enabled in the object.

            :rtype: A dictionary of error or a success response and a value
             with "is-admin-enabled" as the key


        .. function:: peek_failover_group_id()

            Reads the value assigned to failover-group-id in the object.

            :rtype: None on error and a value on success.


        .. function:: set_failover_group_id(value)

            Set the value of failover-group-id in the object.

            :rtype: A dictionary of error or a success response and a value
             with "failover-group-id" as the key


        .. function:: peek_arl_algorithm_mode()

            Reads the value assigned to arl-algorithm-mode in the object.

            :rtype: None on error and a value on success.


        .. function:: set_arl_algorithm_mode(value)

            Set the value of arl-algorithm-mode in the object.

            :rtype: A dictionary of error or a success response and a value
             with "arl-algorithm-mode" as the key


        .. function:: peek_metric()

            Reads the value assigned to metric in the object.

            :rtype: None on error and a value on success.


        .. function:: set_metric(value)

            Set the value of metric in the object.

            :rtype: A dictionary of error or a success response and a value
             with "metric" as the key


        .. function:: peek_minimum_communication_rate()

            Reads the value assigned to minimum-communication-rate in the
             object.

            :rtype: None on error and a value on success.


        .. function:: set_minimum_communication_rate(value)

            Set the value of minimum-communication-rate in the object.

            :rtype: A dictionary of error or a success response and a value
             with "minimum-communication-rate" as the key


        .. function:: peek_remote_ip_address()

            Reads the value assigned to remote-ip-address in the object.

            :rtype: None on error and a value on success.


        .. function:: set_remote_ip_address(value)

            Set the value of remote-ip-address in the object.

            :rtype: A dictionary of error or a success response and a value
             with "remote-ip-address" as the key


        .. function:: peek_admin_enabled()

            Reads the value assigned to admin-enabled in the object.

            :rtype: None on error and a value on success.


        .. function:: set_admin_enabled(value)

            Set the value of admin-enabled in the object.

            :rtype: A dictionary of error or a success response and a value
             with "admin-enabled" as the key


        .. function:: peek_dscp()

            Reads the value assigned to dscp in the object.

            :rtype: None on error and a value on success.


        .. function:: set_dscp(value)

            Set the value of dscp in the object.

            :rtype: A dictionary of error or a success response and a value
             with "dscp" as the key


        .. function:: peek_l2_cos()

            Reads the value assigned to l2-cos in the object.

            :rtype: None on error and a value on success.


        .. function:: set_l2_cos(value)

            Set the value of l2-cos in the object.

            :rtype: A dictionary of error or a success response and a value
             with "l2-cos" as the key


        .. function:: peek_dscp_ip_priority_high()

            Reads the value assigned to ip-priority-high in the object.

            :rtype: None on error and a value on success.


        .. function:: set_dscp_ip_priority_high(value)

            Set the value of ip-priority-high in the object.

            :rtype: A dictionary of error or a success response and a value
             with "ip-priority-high" as the key


        .. function:: peek_dscp_fc_priority_high()

            Reads the value assigned to fc-priority-high in the object.

            :rtype: None on error and a value on success.


        .. function:: set_dscp_fc_priority_high(value)

            Set the value of fc-priority-high in the object.

            :rtype: A dictionary of error or a success response and a value
             with "fc-priority-high" as the key


        .. function:: peek_l2_cos_ip_priority_high()

            Reads the value assigned to ip-priority-high in the object.

            :rtype: None on error and a value on success.


        .. function:: set_l2_cos_ip_priority_high(value)

            Set the value of ip-priority-high in the object.

            :rtype: A dictionary of error or a success response and a value
             with "ip-priority-high" as the key


        .. function:: peek_l2_cos_fc_priority_medium()

            Reads the value assigned to fc-priority-medium in the object.

            :rtype: None on error and a value on success.


        .. function:: set_l2_cos_fc_priority_medium(value)

            Set the value of fc-priority-medium in the object.

            :rtype: A dictionary of error or a success response and a value
             with "fc-priority-medium" as the key


        .. function:: peek_dscp_fc_priority_low()

            Reads the value assigned to fc-priority-low in the object.

            :rtype: None on error and a value on success.


        .. function:: set_dscp_fc_priority_low(value)

            Set the value of fc-priority-low in the object.

            :rtype: A dictionary of error or a success response and a value
             with "fc-priority-low" as the key


        .. function:: peek_l2_cos_ip_priority_low()

            Reads the value assigned to ip-priority-low in the object.

            :rtype: None on error and a value on success.


        .. function:: set_l2_cos_ip_priority_low(value)

            Set the value of ip-priority-low in the object.

            :rtype: A dictionary of error or a success response and a value
             with "ip-priority-low" as the key


        .. function:: peek_l2_cos_fc_priority_high()

            Reads the value assigned to fc-priority-high in the object.

            :rtype: None on error and a value on success.


        .. function:: set_l2_cos_fc_priority_high(value)

            Set the value of fc-priority-high in the object.

            :rtype: A dictionary of error or a success response and a value
             with "fc-priority-high" as the key


        .. function:: peek_l2_cos_fc_priority_low()

            Reads the value assigned to fc-priority-low in the object.

            :rtype: None on error and a value on success.


        .. function:: set_l2_cos_fc_priority_low(value)

            Set the value of fc-priority-low in the object.

            :rtype: A dictionary of error or a success response and a value
             with "fc-priority-low" as the key


        .. function:: peek_l2_cos_priority_control()

            Reads the value assigned to priority-control in the object.

            :rtype: None on error and a value on success.


        .. function:: set_l2_cos_priority_control(value)

            Set the value of priority-control in the object.

            :rtype: A dictionary of error or a success response and a value
             with "priority-control" as the key


        .. function:: peek_dscp_ip_priority_medium()

            Reads the value assigned to ip-priority-medium in the object.

            :rtype: None on error and a value on success.


        .. function:: set_dscp_ip_priority_medium(value)

            Set the value of ip-priority-medium in the object.

            :rtype: A dictionary of error or a success response and a value
             with "ip-priority-medium" as the key


        .. function:: peek_dscp_priority_control()

            Reads the value assigned to priority-control in the object.

            :rtype: None on error and a value on success.


        .. function:: set_dscp_priority_control(value)

            Set the value of priority-control in the object.

            :rtype: A dictionary of error or a success response and a value
             with "priority-control" as the key


        .. function:: peek_l2_cos_ip_priority_medium()

            Reads the value assigned to ip-priority-medium in the object.

            :rtype: None on error and a value on success.


        .. function:: set_l2_cos_ip_priority_medium(value)

            Set the value of ip-priority-medium in the object.

            :rtype: A dictionary of error or a success response and a value
             with "ip-priority-medium" as the key


        .. function:: peek_dscp_fc_priority_medium()

            Reads the value assigned to fc-priority-medium in the object.

            :rtype: None on error and a value on success.


        .. function:: set_dscp_fc_priority_medium(value)

            Set the value of fc-priority-medium in the object.

            :rtype: A dictionary of error or a success response and a value
             with "fc-priority-medium" as the key


        .. function:: peek_dscp_ip_priority_low()

            Reads the value assigned to ip-priority-low in the object.

            :rtype: None on error and a value on success.


        .. function:: set_dscp_ip_priority_low(value)

            Set the value of ip-priority-low in the object.

            :rtype: A dictionary of error or a success response and a value
             with "ip-priority-low" as the key


        .. function:: peek_path_mtu_discovered()

            Reads the value assigned to path-mtu-discovered in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_vlan_id()

            Reads the value assigned to vlan-id in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_admin_status()

            Reads the value assigned to admin-status in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_circuit_status()

            Reads the value assigned to circuit-status in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_dscp()

            Reads the value assigned to dscp in the object.

            :rtype: None on error and a value on success.


        .. function:: set_dscp(value)

            Set the value of dscp in the object.

            :rtype: A dictionary of error or a success response and a value
             with "dscp" as the key


        .. function:: peek_l2_cos()

            Reads the value assigned to l2-cos in the object.

            :rtype: None on error and a value on success.


        .. function:: set_l2_cos(value)

            Set the value of l2-cos in the object.

            :rtype: A dictionary of error or a success response and a value
             with "l2-cos" as the key


    """

    def __init__(self, dictvalues=None):

        clsuri = "/rest" + "/running" + "/brocade-extension-tunnel" +\
                 "/extension-circuit"
        clstype = pyfos_rest_util.rest_obj_type.circuit
        super().__init__(clstype, clsuri)

        self.add(pyfos_rest_util.rest_attribute("circuit-id",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute("name", pyfos_type.type_str,
                 None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute("local-ha-ip-address",
                 pyfos_type.type_ip_addr, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("local-ip-address",
                 pyfos_type.type_ip_addr, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("keep-alive-timeout",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("maximum-communication-rate",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("remote-ha-ip-address",
                 pyfos_type.type_ip_addr, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("is-admin-enabled",
                 pyfos_type.type_bool, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG,
                 version.VER_RANGE_821b_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute("failover-group-id",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("arl-algorithm-mode",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("metric", pyfos_type.type_int,
                 None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("minimum-communication-rate",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("remote-ip-address",
                 pyfos_type.type_ip_addr, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("admin-enabled",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("dscp", pyfos_type.type_na,
                 dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute("l2-cos", pyfos_type.type_na,
                 dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute("ip-priority-high",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG), ['dscp'])
        self.add(pyfos_rest_util.rest_attribute("fc-priority-high",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG), ['dscp'])
        self.add(pyfos_rest_util.rest_attribute("ip-priority-high",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG), ['l2-cos'])
        self.add(pyfos_rest_util.rest_attribute("fc-priority-medium",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG), ['l2-cos'])
        self.add(pyfos_rest_util.rest_attribute("fc-priority-low",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG), ['dscp'])
        self.add(pyfos_rest_util.rest_attribute("ip-priority-low",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG), ['l2-cos'])
        self.add(pyfos_rest_util.rest_attribute("fc-priority-high",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG), ['l2-cos'])
        self.add(pyfos_rest_util.rest_attribute("fc-priority-low",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG), ['l2-cos'])
        self.add(pyfos_rest_util.rest_attribute("priority-control",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG), ['l2-cos'])
        self.add(pyfos_rest_util.rest_attribute("ip-priority-medium",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG), ['dscp'])
        self.add(pyfos_rest_util.rest_attribute("priority-control",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG), ['dscp'])
        self.add(pyfos_rest_util.rest_attribute("ip-priority-medium",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG), ['l2-cos'])
        self.add(pyfos_rest_util.rest_attribute("fc-priority-medium",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG), ['dscp'])
        self.add(pyfos_rest_util.rest_attribute("ip-priority-low",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG), ['dscp'])
        self.add(pyfos_rest_util.rest_attribute("path-mtu-discovered",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("vlan-id",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("admin-status",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG,
                 version.VER_RANGE_821b_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute("circuit-status",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.load(dictvalues, 1)


class extension_tunnel_statistics(pyfos_rest_util.rest_object):

    """Class of extension_tunnel_statistics

    *Description extension_tunnel_statistics*

        Represents tunnel statistics for extension blade or system.

    Important class members of extension_tunnel_statistics:

        +----------------------------+-------------------------------+-------------------------------------------------+
        | Attribute Name             | Description                   |  Frequently Used Methods                        |
        +============================+===============================+=================================================+
        | name                       | The name of the interface.    | :func:`peek_name`                               |
        |                            |                               | :func:`set_name`                                |
        +----------------------------+-------------------------------+-------------------------------------------------+
        | fc-ha-status               | The FC HA status of the       | :func:`peek_fc_ha_status`                       |
        |                            | extension-tunnel.             |                                                 |
        +----------------------------+-------------------------------+-------------------------------------------------+
        | last-error                 | The last tunnel error seen.   | :func:`peek_last_error`                         |
        |                            |                               |                                                 |
        +----------------------------+-------------------------------+-------------------------------------------------+
        | compressed-bytes           | Compressed Bytes.             | :func:`peek_compressed_bytes`                   |
        |                            |                               |                                                 |
        +----------------------------+-------------------------------+-------------------------------------------------+
        | flow-status                | Flow control status: 0 :      | :func:`peek_flow_status`                        |
        |                            | flow control is off 1 :       |                                                 |
        |                            | flow control is on            |                                                 |
        +----------------------------+-------------------------------+-------------------------------------------------+
        | connection-count           | Active connection count.      | :func:`peek_connection_count`                   |
        |                            |                               |                                                 |
        +----------------------------+-------------------------------+-------------------------------------------------+
        | ip-ha-status               | The IP HA status of the       | :func:`peek_ip_ha_status`                       |
        |                            | extension-tunnel.             |                                                 |
        +----------------------------+-------------------------------+-------------------------------------------------+
        | remote-hcl-in-progress     | Indicates whether remote      | :func:`peek_remote_hcl_in_progress`             |
        |                            | HCL is in progress true:      |                                                 |
        |                            | Remote HCL in progress.       |                                                 |
        |                            | false: No remote HCL in       |                                                 |
        |                            | progress.                     |                                                 |
        +----------------------------+-------------------------------+-------------------------------------------------+
        | uncompressed-bytes         | Uncompressed Bytes.           | :func:`peek_uncompressed_bytes`                 |
        |                            |                               |                                                 |
        +----------------------------+-------------------------------+-------------------------------------------------+
        | duration                   | Connection duration (in       | :func:`peek_duration`                           |
        |                            | seconds).                     |                                                 |
        +----------------------------+-------------------------------+-------------------------------------------------+
        | local-hcl-in-progress      | Indicates whether local HCL   | :func:`peek_local_hcl_in_progress`              |
        |                            | is in progress. true: local   |                                                 |
        |                            | HCL is in progress false:     |                                                 |
        |                            | local HCL is not in           |                                                 |
        |                            | progress.                     |                                                 |
        +----------------------------+-------------------------------+-------------------------------------------------+
        | operational-status         | Tunnel operational status.    | :func:`peek_operational_status`                 |
        |                            |                               |                                                 |
        +----------------------------+-------------------------------+-------------------------------------------------+

    *Object functions for extension_tunnel_statistics*

    .. function:: get()

        Get the instances of class "extension_tunnel_statistics from switch.
         The object can be printed using :func:`pyfos_utils.response_print`.

        :param session: The session handler returned by
         :func:`pyfos_auth.login`.

        :rtype: A dictionary of errors or a success response.


    *Class functions for extension_tunnel_statistics*

        .. function:: peek_name()

            Reads the value assigned to name in the object.

            :rtype: None on error and a value on success.


        .. function:: set_name(value)

            Set the value of name in the object.

            :rtype: A dictionary of error or a success response and a value
             with "name" as the key


        .. function:: peek_fc_ha_status()

            Reads the value assigned to fc-ha-status in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_last_error()

            Reads the value assigned to last-error in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_compressed_bytes()

            Reads the value assigned to compressed-bytes in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_flow_status()

            Reads the value assigned to flow-status in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_connection_count()

            Reads the value assigned to connection-count in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_ip_ha_status()

            Reads the value assigned to ip-ha-status in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_remote_hcl_in_progress()

            Reads the value assigned to remote-hcl-in-progress in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_uncompressed_bytes()

            Reads the value assigned to uncompressed-bytes in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_duration()

            Reads the value assigned to duration in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_local_hcl_in_progress()

            Reads the value assigned to local-hcl-in-progress in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_operational_status()

            Reads the value assigned to operational-status in the object.

            :rtype: None on error and a value on success.


    """

    def __init__(self, dictvalues=None):

        clsuri = "/rest" + "/running" + "/brocade-extension-tunnel" +\
                 "/extension-tunnel-statistics"
        clstype = pyfos_rest_util.rest_obj_type.tunnel_stats
        super().__init__(clstype, clsuri)

        self.add(pyfos_rest_util.rest_attribute("name", pyfos_type.type_str,
                 None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute("compressed-bytes",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("flow-status",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("connection-count",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("uncompressed-bytes",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("operational-status",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("duration",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("ip-ha-status",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG,
                 version.VER_RANGE_900_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute("remote-hcl-in-progress",
                 pyfos_type.type_bool, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG,
                 version.VER_RANGE_900_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute("local-hcl-in-progress",
                 pyfos_type.type_bool, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG,
                 version.VER_RANGE_900_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute("fc-ha-status",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG,
                 version.VER_RANGE_900_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute("last-error",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG,
                 version.VER_RANGE_900_and_ABOVE))
        self.load(dictvalues, 1)


class extension_circuit_statistics(pyfos_rest_util.rest_object):

    """Class of extension_circuit_statistics

    *Description extension_circuit_statistics*

        Represents circuit statistics for extension blade or system.

    Important class members of extension_circuit_statistics:

        +--------------------------+---------------------------------+-------------------------------------------------+
        | Attribute Name           | Description                     |  Frequently Used Methods                        |
        +==========================+=================================+=================================================+
        | name                     | The name of the interface.      | :func:`peek_name`                               |
        |                          |                                 | :func:`set_name`                                |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | circuit-id               | Circuit identifier.             | :func:`peek_circuit_id`                         |
        |                          |                                 | :func:`set_circuit_id`                          |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | operational-status       | Circuit operational status.     | :func:`peek_operational_status`                 |
        |                          |                                 |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | flow-status              | Flow control status: 0 : flow   | :func:`peek_flow_status`                        |
        |                          | control is off 1 : flow         |                                                 |
        |                          | control is on                   |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | out-packet-total         | Number of total TCP packets     | :func:`peek_out_packet_total`                   |
        |                          | sent out in the Network.        |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | duration                 | Connection duration (in         | :func:`peek_duration`                           |
        |                          | seconds).                       |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | out-packet-lost          | Number of TCP packets lost      | :func:`peek_out_packet_lost`                    |
        |                          | because of delay/drop in the    |                                                 |
        |                          | Network.                        |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | connection-count         | Active connection count.        | :func:`peek_connection_count`                   |
        |                          |                                 |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+

    *Object functions for extension_circuit_statistics*

    .. function:: get()

        Get the instances of class "extension_circuit_statistics from switch.
         The object can be printed using :func:`pyfos_utils.response_print`.

        :param session: The session handler returned by
         :func:`pyfos_auth.login`.

        :rtype: A dictionary of errors or a success response.


    *Class functions for extension_circuit_statistics*

        .. function:: peek_name()

            Reads the value assigned to name in the object.

            :rtype: None on error and a value on success.


        .. function:: set_name(value)

            Set the value of name in the object.

            :rtype: A dictionary of error or a success response and a value
             with "name" as the key


        .. function:: peek_circuit_id()

            Reads the value assigned to circuit-id in the object.

            :rtype: None on error and a value on success.


        .. function:: set_circuit_id(value)

            Set the value of circuit-id in the object.

            :rtype: A dictionary of error or a success response and a value
             with "circuit-id" as the key


        .. function:: peek_operational_status()

            Reads the value assigned to operational-status in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_flow_status()

            Reads the value assigned to flow-status in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_out_packet_total()

            Reads the value assigned to out-packet-total in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_duration()

            Reads the value assigned to duration in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_out_packet_lost()

            Reads the value assigned to out-packet-lost in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_connection_count()

            Reads the value assigned to connection-count in the object.

            :rtype: None on error and a value on success.


    """

    def __init__(self, dictvalues=None):

        clsuri = "/rest" + "/running" + "/brocade-extension-tunnel" +\
                 "/extension-circuit-statistics"
        clstype = pyfos_rest_util.rest_obj_type.circuit_stats
        super().__init__(clstype, clsuri)

        self.add(pyfos_rest_util.rest_attribute("name", pyfos_type.type_str,
                 None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute("circuit-id",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute("operational-status",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("flow-status",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("connection-count",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("duration",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("out-packet-lost",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG,
                 version.VER_RANGE_821_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute("out-packet-total",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG,
                 version.VER_RANGE_821_and_ABOVE))
        self.load(dictvalues, 1)


class wan_statistics(pyfos_rest_util.rest_object):

    """Class of wan_statistics

    *Description wan_statistics*

        Represents TCP WAN statistics for extension blade or system.

    Important class members of wan_statistics:

        +-----------------------------------------+--------------------------------------+-----------------------------------------------------------+
        | Attribute Name                          | Description                          |  Frequently Used Methods                                  |
        +=========================================+======================================+===========================================================+
        | ve-port                                 | The name of the interface.           | :func:`peek_ve_port`                                      |
        |                                         |                                      | :func:`set_ve_port`                                       |
        +-----------------------------------------+--------------------------------------+-----------------------------------------------------------+
        | circuit-id                              | Circuit identifier.                  | :func:`peek_circuit_id`                                   |
        |                                         |                                      | :func:`set_circuit_id`                                    |
        +-----------------------------------------+--------------------------------------+-----------------------------------------------------------+
        | connection-id                           | TCP connection identifier            | :func:`peek_connection_id`                                |
        |                                         | associated with the WAN TCP          | :func:`set_connection_id`                                 |
        |                                         | connection. The TCP connection       |                                                           |
        |                                         | identifier may change in case of     |                                                           |
        |                                         | connection going down or             |                                                           |
        |                                         | establishment. These are not         |                                                           |
        |                                         | persistent identifiers associated    |                                                           |
        |                                         | with the connection.                 |                                                           |
        +-----------------------------------------+--------------------------------------+-----------------------------------------------------------+
        | in-queued-packets-maximum-sequence      | TCP queued packets maximum           | :func:`peek_in_queued_packets_maximum_sequence`           |
        |                                         | sequence number received.            |                                                           |
        +-----------------------------------------+--------------------------------------+-----------------------------------------------------------+
        | arl-current                             | ARL current value                    | :func:`peek_arl_current`                                  |
        |                                         |                                      |                                                           |
        +-----------------------------------------+--------------------------------------+-----------------------------------------------------------+
        | in-packets                              | Total TCP packets received.          | :func:`peek_in_packets`                                   |
        |                                         |                                      |                                                           |
        +-----------------------------------------+--------------------------------------+-----------------------------------------------------------+
        | retransmit-timeout                      | TCP retransmits timeout              | :func:`peek_retransmit_timeout`                           |
        |                                         |                                      |                                                           |
        +-----------------------------------------+--------------------------------------+-----------------------------------------------------------+
        | out-packets                             | Total TCP packets sent.              | :func:`peek_out_packets`                                  |
        |                                         |                                      |                                                           |
        +-----------------------------------------+--------------------------------------+-----------------------------------------------------------+
        | arl-minimum                             | ARL minimum value                    | :func:`peek_arl_minimum`                                  |
        |                                         |                                      |                                                           |
        +-----------------------------------------+--------------------------------------+-----------------------------------------------------------+
        | in-queued-out-of-order                  | TCP queued out of order packets      | :func:`peek_in_queued_out_of_order`                       |
        |                                         | received.                            |                                                           |
        +-----------------------------------------+--------------------------------------+-----------------------------------------------------------+
        | duplicate-acknowledgement               | TCP duplicate acknowledgement        | :func:`peek_duplicate_acknowledgement`                    |
        |                                         | received.                            |                                                           |
        +-----------------------------------------+--------------------------------------+-----------------------------------------------------------+
        | in-window-scale                         | Receiver negotiated window scale.    | :func:`peek_in_window_scale`                              |
        |                                         |                                      |                                                           |
        +-----------------------------------------+--------------------------------------+-----------------------------------------------------------+
        | out-queued-packets-maximum-sequence     | Source TCP queued packets maximum    | :func:`peek_out_queued_packets_maximum_sequence`          |
        |                                         | sequence number.                     |                                                           |
        +-----------------------------------------+--------------------------------------+-----------------------------------------------------------+
        | out-queued-packets-minimum-sequence     | Source TCP queued packets minimum    | :func:`peek_out_queued_packets_minimum_sequence`          |
        |                                         | sequence number.                     |                                                           |
        +-----------------------------------------+--------------------------------------+-----------------------------------------------------------+
        | out-window-scale                        | Source window scaling shift count.   | :func:`peek_out_window_scale`                             |
        |                                         |                                      |                                                           |
        +-----------------------------------------+--------------------------------------+-----------------------------------------------------------+
        | rtt-variance-maximum                    | Maximum variance in round trip       | :func:`peek_rtt_variance_maximum`                         |
        |                                         | time.                                |                                                           |
        +-----------------------------------------+--------------------------------------+-----------------------------------------------------------+
        | arl-next-reset-algorithm                | ARL next reset algorithm.            | :func:`peek_arl_next_reset_algorithm`                     |
        |                                         |                                      |                                                           |
        +-----------------------------------------+--------------------------------------+-----------------------------------------------------------+
        | source-port                             | TCP source port number               | :func:`peek_source_port`                                  |
        |                                         |                                      |                                                           |
        +-----------------------------------------+--------------------------------------+-----------------------------------------------------------+
        | fast-retransmits                        | TCP fast retransmits                 | :func:`peek_fast_retransmits`                             |
        |                                         |                                      |                                                           |
        +-----------------------------------------+--------------------------------------+-----------------------------------------------------------+
        | rtt-maximum                             | maximum round trip time.             | :func:`peek_rtt_maximum`                                  |
        |                                         |                                      |                                                           |
        +-----------------------------------------+--------------------------------------+-----------------------------------------------------------+
        | congestion-window                       | The congestion window is the         | :func:`peek_congestion_window`                            |
        |                                         | maximum data that can be sent        |                                                           |
        |                                         | before an ACK is received.           |                                                           |
        +-----------------------------------------+--------------------------------------+-----------------------------------------------------------+
        | in-window-size-maximum                  | Receiver maximum window size.        | :func:`peek_in_window_size_maximum`                       |
        |                                         |                                      |                                                           |
        +-----------------------------------------+--------------------------------------+-----------------------------------------------------------+
        | out-bytes                               | Total bytes sent.                    | :func:`peek_out_bytes`                                    |
        |                                         |                                      |                                                           |
        +-----------------------------------------+--------------------------------------+-----------------------------------------------------------+
        | operation-mode                          | TCP operation mode algorithm used    | :func:`peek_operation_mode`                               |
        |                                         | for connection.                      |                                                           |
        +-----------------------------------------+--------------------------------------+-----------------------------------------------------------+
        | out-queued-packets-next-sequence        | Source TCP queued packets next       | :func:`peek_out_queued_packets_next_sequence`             |
        |                                         | sequence number.                     |                                                           |
        +-----------------------------------------+--------------------------------------+-----------------------------------------------------------+
        | arl-maximum                             | ARL maximum value                    | :func:`peek_arl_maximum`                                  |
        |                                         |                                      |                                                           |
        +-----------------------------------------+--------------------------------------+-----------------------------------------------------------+
        | slow-start-threshold                    | Source slow start threshold.         | :func:`peek_slow_start_threshold`                         |
        |                                         |                                      |                                                           |
        +-----------------------------------------+--------------------------------------+-----------------------------------------------------------+
        | slow-retransmits                        | TCP slow retransmits                 | :func:`peek_slow_retransmits`                             |
        |                                         |                                      |                                                           |
        +-----------------------------------------+--------------------------------------+-----------------------------------------------------------+
        | retransmits                             | TCP retransmits                      | :func:`peek_retransmits`                                  |
        |                                         |                                      |                                                           |
        +-----------------------------------------+--------------------------------------+-----------------------------------------------------------+
        | connection-mss                          | TCP connection MSS.                  | :func:`peek_connection_mss`                               |
        |                                         |                                      |                                                           |
        +-----------------------------------------+--------------------------------------+-----------------------------------------------------------+
        | in-queued-packets                       | TCP queued packets received.         | :func:`peek_in_queued_packets`                            |
        |                                         |                                      |                                                           |
        +-----------------------------------------+--------------------------------------+-----------------------------------------------------------+
        | maximum-retransmits                     | TCP maximum retransmits              | :func:`peek_maximum_retransmits`                          |
        |                                         |                                      |                                                           |
        +-----------------------------------------+--------------------------------------+-----------------------------------------------------------+
        | out-window-size                         | Source window size.                  | :func:`peek_out_window_size`                              |
        |                                         |                                      |                                                           |
        +-----------------------------------------+--------------------------------------+-----------------------------------------------------------+
        | rtt-variance                            | variance in round trip time.         | :func:`peek_rtt_variance`                                 |
        |                                         |                                      |                                                           |
        +-----------------------------------------+--------------------------------------+-----------------------------------------------------------+
        | in-queued-out-of-order-maximum          | TCP total out of order packets       | :func:`peek_in_queued_out_of_order_maximum`               |
        |                                         | received.                            |                                                           |
        +-----------------------------------------+--------------------------------------+-----------------------------------------------------------+
        | ha-type                                 | Tunnel HA type configuration.        | :func:`peek_ha_type`                                      |
        |                                         |                                      |                                                           |
        +-----------------------------------------+--------------------------------------+-----------------------------------------------------------+
        | maximum-fast-retransmits                | TCP maximum fast retransmits         | :func:`peek_maximum_fast_retransmits`                     |
        |                                         |                                      |                                                           |
        +-----------------------------------------+--------------------------------------+-----------------------------------------------------------+
        | rtt                                     | round trip time.                     | :func:`peek_rtt`                                          |
        |                                         |                                      |                                                           |
        +-----------------------------------------+--------------------------------------+-----------------------------------------------------------+
        | in-queued-out-of-order-total            | TCP total out of order packets       | :func:`peek_in_queued_out_of_order_total`                 |
        |                                         | received.                            |                                                           |
        +-----------------------------------------+--------------------------------------+-----------------------------------------------------------+
        | out-in-flight-packets                   | Source in flight packets.            | :func:`peek_out_in_flight_packets`                        |
        |                                         |                                      |                                                           |
        +-----------------------------------------+--------------------------------------+-----------------------------------------------------------+
        | destination-port                        | TCP remote destination port number   | :func:`peek_destination_port`                             |
        |                                         |                                      |                                                           |
        +-----------------------------------------+--------------------------------------+-----------------------------------------------------------+
        | in-window-size                          | Receiver window size.                | :func:`peek_in_window_size`                               |
        |                                         |                                      |                                                           |
        +-----------------------------------------+--------------------------------------+-----------------------------------------------------------+
        | in-bytes                                | Total bytes received.                | :func:`peek_in_bytes`                                     |
        |                                         |                                      |                                                           |
        +-----------------------------------------+--------------------------------------+-----------------------------------------------------------+
        | priority                                | QOS Priority value for the tunnel    | :func:`peek_priority`                                     |
        |                                         |                                      |                                                           |
        +-----------------------------------------+--------------------------------------+-----------------------------------------------------------+
        | out-unacknowledged-packets-sequence     | Source unacknowledged packets        | :func:`peek_out_unacknowledged_packets_sequence`          |
        |                                         | sequence.                            |                                                           |
        +-----------------------------------------+--------------------------------------+-----------------------------------------------------------+
        | in-queued-packets-next-sequence         | TCP queued packets next sequence     | :func:`peek_in_queued_packets_next_sequence`              |
        |                                         | number received.                     |                                                           |
        +-----------------------------------------+--------------------------------------+-----------------------------------------------------------+
        | in-queued-packets-minimum-sequence      | TCP queued packets minimum           | :func:`peek_in_queued_packets_minimum_sequence`           |
        |                                         | sequence number received.            |                                                           |
        +-----------------------------------------+--------------------------------------+-----------------------------------------------------------+
        | slow-starts                             | TCP slow starts.                     | :func:`peek_slow_starts`                                  |
        |                                         |                                      |                                                           |
        +-----------------------------------------+--------------------------------------+-----------------------------------------------------------+

    *Object functions for wan_statistics*

    .. function:: get()

        Get the instances of class "wan_statistics from switch. The object can
         be printed using :func:`pyfos_utils.response_print`.

        :param session: The session handler returned by
         :func:`pyfos_auth.login`.

        :rtype: A dictionary of errors or a success response.


    *Class functions for wan_statistics*

        .. function:: peek_ve_port()

            Reads the value assigned to ve-port in the object.

            :rtype: None on error and a value on success.


        .. function:: set_ve_port(value)

            Set the value of ve-port in the object.

            :rtype: A dictionary of error or a success response and a value
             with "ve-port" as the key


        .. function:: peek_circuit_id()

            Reads the value assigned to circuit-id in the object.

            :rtype: None on error and a value on success.


        .. function:: set_circuit_id(value)

            Set the value of circuit-id in the object.

            :rtype: A dictionary of error or a success response and a value
             with "circuit-id" as the key


        .. function:: peek_connection_id()

            Reads the value assigned to connection-id in the object.

            :rtype: None on error and a value on success.


        .. function:: set_connection_id(value)

            Set the value of connection-id in the object.

            :rtype: A dictionary of error or a success response and a value
             with "connection-id" as the key


        .. function:: peek_in_queued_packets_maximum_sequence()

            Reads the value assigned to in-queued-packets-maximum-sequence in
             the object.

            :rtype: None on error and a value on success.


        .. function:: peek_arl_current()

            Reads the value assigned to arl-current in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_in_packets()

            Reads the value assigned to in-packets in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_retransmit_timeout()

            Reads the value assigned to retransmit-timeout in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_out_packets()

            Reads the value assigned to out-packets in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_arl_minimum()

            Reads the value assigned to arl-minimum in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_in_queued_out_of_order()

            Reads the value assigned to in-queued-out-of-order in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_duplicate_acknowledgement()

            Reads the value assigned to duplicate-acknowledgement in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_in_window_scale()

            Reads the value assigned to in-window-scale in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_out_queued_packets_maximum_sequence()

            Reads the value assigned to out-queued-packets-maximum-sequence
             in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_out_queued_packets_minimum_sequence()

            Reads the value assigned to out-queued-packets-minimum-sequence
             in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_out_window_scale()

            Reads the value assigned to out-window-scale in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_rtt_variance_maximum()

            Reads the value assigned to rtt-variance-maximum in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_arl_next_reset_algorithm()

            Reads the value assigned to arl-next-reset-algorithm in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_source_port()

            Reads the value assigned to source-port in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_fast_retransmits()

            Reads the value assigned to fast-retransmits in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_rtt_maximum()

            Reads the value assigned to rtt-maximum in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_congestion_window()

            Reads the value assigned to congestion-window in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_in_window_size_maximum()

            Reads the value assigned to in-window-size-maximum in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_out_bytes()

            Reads the value assigned to out-bytes in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_operation_mode()

            Reads the value assigned to operation-mode in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_out_queued_packets_next_sequence()

            Reads the value assigned to out-queued-packets-next-sequence in
             the object.

            :rtype: None on error and a value on success.


        .. function:: peek_arl_maximum()

            Reads the value assigned to arl-maximum in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_slow_start_threshold()

            Reads the value assigned to slow-start-threshold in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_slow_retransmits()

            Reads the value assigned to slow-retransmits in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_retransmits()

            Reads the value assigned to retransmits in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_connection_mss()

            Reads the value assigned to connection-mss in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_in_queued_packets()

            Reads the value assigned to in-queued-packets in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_maximum_retransmits()

            Reads the value assigned to maximum-retransmits in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_out_window_size()

            Reads the value assigned to out-window-size in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_rtt_variance()

            Reads the value assigned to rtt-variance in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_in_queued_out_of_order_maximum()

            Reads the value assigned to in-queued-out-of-order-maximum in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_ha_type()

            Reads the value assigned to ha-type in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_maximum_fast_retransmits()

            Reads the value assigned to maximum-fast-retransmits in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_rtt()

            Reads the value assigned to rtt in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_in_queued_out_of_order_total()

            Reads the value assigned to in-queued-out-of-order-total in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_out_in_flight_packets()

            Reads the value assigned to out-in-flight-packets in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_destination_port()

            Reads the value assigned to destination-port in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_in_window_size()

            Reads the value assigned to in-window-size in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_in_bytes()

            Reads the value assigned to in-bytes in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_priority()

            Reads the value assigned to priority in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_out_unacknowledged_packets_sequence()

            Reads the value assigned to out-unacknowledged-packets-sequence
             in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_in_queued_packets_next_sequence()

            Reads the value assigned to in-queued-packets-next-sequence in
             the object.

            :rtype: None on error and a value on success.


        .. function:: peek_in_queued_packets_minimum_sequence()

            Reads the value assigned to in-queued-packets-minimum-sequence in
             the object.

            :rtype: None on error and a value on success.


        .. function:: peek_slow_starts()

            Reads the value assigned to slow-starts in the object.

            :rtype: None on error and a value on success.


    """

    def __init__(self, dictvalues=None):

        clsuri = "/rest" + "/running" + "/brocade-extension-tunnel" +\
                 "/wan-statistics"
        clstype = pyfos_rest_util.rest_obj_type.wan_statistics
        clsver = version.VER_RANGE_900_and_ABOVE
        super().__init__(clstype, clsuri, clsver)

        self.add(pyfos_rest_util.rest_attribute("ve-port",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute("circuit-id",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute("connection-id",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute(
                 "in-queued-packets-maximum-sequence", pyfos_type.type_int,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("arl-current",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("in-packets",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("retransmit-timeout",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("out-packets",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("arl-minimum",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("in-queued-out-of-order",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("duplicate-acknowledgement",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("in-window-scale",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "out-queued-packets-maximum-sequence", pyfos_type.type_int,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "out-queued-packets-minimum-sequence", pyfos_type.type_int,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("out-window-scale",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("rtt-variance-maximum",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("arl-next-reset-algorithm",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("source-port",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("fast-retransmits",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("rtt-maximum",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("congestion-window",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("in-window-size-maximum",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("out-bytes",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("operation-mode",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "out-queued-packets-next-sequence", pyfos_type.type_int,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("arl-maximum",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("slow-start-threshold",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("slow-retransmits",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("retransmits",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("connection-mss",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("in-queued-packets",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("maximum-retransmits",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("out-window-size",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("rtt-variance",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "in-queued-out-of-order-maximum", pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("ha-type",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("maximum-fast-retransmits",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("rtt", pyfos_type.type_int,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "in-queued-out-of-order-total", pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("out-in-flight-packets",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("destination-port",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("in-window-size",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("in-bytes",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("priority",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "out-unacknowledged-packets-sequence", pyfos_type.type_int,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "in-queued-packets-next-sequence", pyfos_type.type_int,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
                 "in-queued-packets-minimum-sequence", pyfos_type.type_int,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("slow-starts",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.load(dictvalues, 1)


class circuit_qos_statistics(pyfos_rest_util.rest_object):

    """Class of circuit_qos_statistics

    *Description circuit_qos_statistics*

        Represents circuit statistics for extension blade or system.

    Important class members of circuit_qos_statistics:

        +------------------------------+-----------------------------+-------------------------------------------------+
        | Attribute Name               | Description                 |  Frequently Used Methods                        |
        +==============================+=============================+=================================================+
        | ha-type                      | Tunnel group HA type        | :func:`peek_ha_type`                            |
        |                              | configuration.              | :func:`set_ha_type`                             |
        +------------------------------+-----------------------------+-------------------------------------------------+
        | ve-port                      | The name of the             | :func:`peek_ve_port`                            |
        |                              | extension-tunnel            | :func:`set_ve_port`                             |
        |                              | interface.                  |                                                 |
        +------------------------------+-----------------------------+-------------------------------------------------+
        | priority                     | QOS Priority value for      | :func:`peek_priority`                           |
        |                              | the tunnel                  | :func:`set_priority`                            |
        +------------------------------+-----------------------------+-------------------------------------------------+
        | circuit-id                   | Circuit identifier the      | :func:`peek_circuit_id`                         |
        |                              | allowed values are for 0    | :func:`set_circuit_id`                          |
        |                              | to 9.                       |                                                 |
        +------------------------------+-----------------------------+-------------------------------------------------+
        | operational-status           | Circuit operational         | :func:`peek_operational_status`                 |
        |                              | status.                     |                                                 |
        +------------------------------+-----------------------------+-------------------------------------------------+
        | tcp-out-of-order-packets     | TCP total out of order      | :func:`peek_tcp_out_of_order_packets`           |
        |                              | packets.                    |                                                 |
        +------------------------------+-----------------------------+-------------------------------------------------+
        | tcp-slow-starts              | TCP slow starts.            | :func:`peek_tcp_slow_starts`                    |
        |                              |                             |                                                 |
        +------------------------------+-----------------------------+-------------------------------------------------+
        | flow-status                  | Flow control status:        | :func:`peek_flow_status`                        |
        |                              | false : flow control is     |                                                 |
        |                              | off true : flow control     |                                                 |
        |                              | is on                       |                                                 |
        +------------------------------+-----------------------------+-------------------------------------------------+
        | connection-count             | Active connection count.    | :func:`peek_connection_count`                   |
        |                              |                             |                                                 |
        +------------------------------+-----------------------------+-------------------------------------------------+
        | out-bytes                    | total octets sent.          | :func:`peek_out_bytes`                          |
        |                              |                             |                                                 |
        +------------------------------+-----------------------------+-------------------------------------------------+
        | out-bytes-average            | Total octets send per 30s   | :func:`peek_out_bytes_average`                  |
        |                              | average.                    |                                                 |
        +------------------------------+-----------------------------+-------------------------------------------------+
        | out-packets                  | Total TCP packets sent.     | :func:`peek_out_packets`                        |
        |                              |                             |                                                 |
        +------------------------------+-----------------------------+-------------------------------------------------+
        | in-bytes                     | total octets received.      | :func:`peek_in_bytes`                           |
        |                              |                             |                                                 |
        +------------------------------+-----------------------------+-------------------------------------------------+
        | out-tcp-packets              | TCP packets sent.           | :func:`peek_out_tcp_packets`                    |
        |                              |                             |                                                 |
        +------------------------------+-----------------------------+-------------------------------------------------+
        | tcp-retransmits              | TCP retransmits /lost       | :func:`peek_tcp_retransmits`                    |
        |                              | packets.                    |                                                 |
        +------------------------------+-----------------------------+-------------------------------------------------+
        | rtt                          | The round trip time.        | :func:`peek_rtt`                                |
        |                              |                             |                                                 |
        +------------------------------+-----------------------------+-------------------------------------------------+
        | in-tcp-bytes                 | Total TCP bytes received.   | :func:`peek_in_tcp_bytes`                       |
        |                              |                             |                                                 |
        +------------------------------+-----------------------------+-------------------------------------------------+
        | in-tcp-packets               | TCP packets received.       | :func:`peek_in_tcp_packets`                     |
        |                              |                             |                                                 |
        +------------------------------+-----------------------------+-------------------------------------------------+
        | out-tcp-bytes                | Total TCP bytes sent.       | :func:`peek_out_tcp_bytes`                      |
        |                              |                             |                                                 |
        +------------------------------+-----------------------------+-------------------------------------------------+
        | in-packets                   | total packets received.     | :func:`peek_in_packets`                         |
        |                              |                             |                                                 |
        +------------------------------+-----------------------------+-------------------------------------------------+
        | duration                     | Connection duration (in     | :func:`peek_duration`                           |
        |                              | seconds).                   |                                                 |
        +------------------------------+-----------------------------+-------------------------------------------------+
        | in-bytes-average             | Total octets received per   | :func:`peek_in_bytes_average`                   |
        |                              | 30s average.                |                                                 |
        +------------------------------+-----------------------------+-------------------------------------------------+

    *Object functions for circuit_qos_statistics*

    .. function:: get()

        Get the instances of class "circuit_qos_statistics from switch. The
         object can be printed using :func:`pyfos_utils.response_print`.

        :param session: The session handler returned by
         :func:`pyfos_auth.login`.

        :rtype: A dictionary of errors or a success response.


    *Class functions for circuit_qos_statistics*

        .. function:: peek_ha_type()

            Reads the value assigned to ha-type in the object.

            :rtype: None on error and a value on success.


        .. function:: set_ha_type(value)

            Set the value of ha-type in the object.

            :rtype: A dictionary of error or a success response and a value
             with "ha-type" as the key


        .. function:: peek_ve_port()

            Reads the value assigned to ve-port in the object.

            :rtype: None on error and a value on success.


        .. function:: set_ve_port(value)

            Set the value of ve-port in the object.

            :rtype: A dictionary of error or a success response and a value
             with "ve-port" as the key


        .. function:: peek_priority()

            Reads the value assigned to priority in the object.

            :rtype: None on error and a value on success.


        .. function:: set_priority(value)

            Set the value of priority in the object.

            :rtype: A dictionary of error or a success response and a value
             with "priority" as the key


        .. function:: peek_circuit_id()

            Reads the value assigned to circuit-id in the object.

            :rtype: None on error and a value on success.


        .. function:: set_circuit_id(value)

            Set the value of circuit-id in the object.

            :rtype: A dictionary of error or a success response and a value
             with "circuit-id" as the key


        .. function:: peek_operational_status()

            Reads the value assigned to operational-status in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_tcp_out_of_order_packets()

            Reads the value assigned to tcp-out-of-order-packets in the
             object.

            :rtype: None on error and a value on success.


        .. function:: peek_tcp_slow_starts()

            Reads the value assigned to tcp-slow-starts in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_flow_status()

            Reads the value assigned to flow-status in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_connection_count()

            Reads the value assigned to connection-count in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_out_bytes()

            Reads the value assigned to out-bytes in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_out_bytes_average()

            Reads the value assigned to out-bytes-average in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_out_packets()

            Reads the value assigned to out-packets in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_in_bytes()

            Reads the value assigned to in-bytes in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_out_tcp_packets()

            Reads the value assigned to out-tcp-packets in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_tcp_retransmits()

            Reads the value assigned to tcp-retransmits in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_rtt()

            Reads the value assigned to rtt in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_in_tcp_bytes()

            Reads the value assigned to in-tcp-bytes in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_in_tcp_packets()

            Reads the value assigned to in-tcp-packets in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_out_tcp_bytes()

            Reads the value assigned to out-tcp-bytes in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_in_packets()

            Reads the value assigned to in-packets in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_duration()

            Reads the value assigned to duration in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_in_bytes_average()

            Reads the value assigned to in-bytes-average in the object.

            :rtype: None on error and a value on success.


    """

    def __init__(self, dictvalues=None):

        clsuri = "/rest" + "/running" + "/brocade-extension-tunnel" +\
                 "/circuit-qos-statistics"
        clstype = pyfos_rest_util.rest_obj_type.circuit_qos_statistics
        clsver = version.VER_RANGE_900_and_ABOVE
        super().__init__(clstype, clsuri, clsver)

        self.add(pyfos_rest_util.rest_attribute("ha-type",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute("ve-port",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute("priority",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute("circuit-id",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute("operational-status",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("tcp-out-of-order-packets",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("tcp-slow-starts",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("flow-status",
                 pyfos_type.type_bool, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("connection-count",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("out-bytes",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("out-bytes-average",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("out-packets",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("in-bytes",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("out-tcp-packets",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("tcp-retransmits",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("rtt", pyfos_type.type_int,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("in-tcp-bytes",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("in-tcp-packets",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("out-tcp-bytes",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("in-packets",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("duration",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("in-bytes-average",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.load(dictvalues, 1)
