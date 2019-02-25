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

:mod:`pyfos_brocade_fibrechannel_diagnostics` - PyFOS module to \
        provide REST support for FC port diagnostics.
*******************************************************************\
*******************************************************
The :mod:`pyfos_brocade_fibrechannel_diagnostics` module provides REST \
        support for FC port diagnostics.

"""

from pyfos import pyfos_rest_util
from pyfos.pyfos_type import pyfos_type
import pyfos.pyfos_version as version


DIAG_STOP = 0
DIAG_START = 1
DIAG_RESTART = 2

DIAG_YES = "yes"
DIAG_NO = "no"


class fibrechannel_diagnostics(pyfos_rest_util.rest_object):
    """Class of FC Port Diagnostics

    Important Class Members:

        +---------------------------------------+----------------------------------------------+---------------------------------------------------+
        | Attribute Name                        | Description                                  |Frequently Used Methods                            |
        +=======================================+==============================================+===================================================+
        | name                                  | Name of the port.                            |:func:`set_name`                                   |
        |                                       |                                              |:func:`peek_name`                                  |
        +---------------------------------------+----------------------------------------------+---------------------------------------------------+
        | diagnostic-control                    | Sets the mode to stop, start, or restart.    |:func:`set_diagnostic_control`                     |
        |                                       |                                              |:func:`peek_diagnostic_control`                    |
        +---------------------------------------+----------------------------------------------+---------------------------------------------------+
        | mode                                  | Displays manual or auto mode.                |:func:`peek_mode`                                  |
        +---------------------------------------+----------------------------------------------+---------------------------------------------------+
        | state                                 | Displays the test status.                    |:func:`peek_state`                                 |
        +---------------------------------------+----------------------------------------------+---------------------------------------------------+
        | distance                              | Displays the estimated ISL         distance. |:func:`peek_distance`                              |
        +---------------------------------------+----------------------------------------------+---------------------------------------------------+
        | electrical-loopback-test/result       | Displays the test status             result. |:func:`peek_electrical_loopback_test_result`       |
        +---------------------------------------+----------------------------------------------+---------------------------------------------------+
        | electrical-loopback-test/comments     | Displays the test status detailed comments.  |:func:`peek_electrical_loopback_test_comments`     |
        +---------------------------------------+----------------------------------------------+---------------------------------------------------+
        | optical-loopback-test/result          | Displays the test status p                   |:func:`peek_optical_loopback_test_result`          |
        +---------------------------------------+----------------------------------------------+---------------------------------------------------+
        | optical-loopback-test/comments        | Displays the test status detailed   comments.|:func:`peek_optical_loopback_test_comments`        |
        +---------------------------------------+----------------------------------------------+---------------------------------------------------+
        | link-traffic-test/result              | Displays the test status result.             |:func:`peek_link_traffic_test_result`              |
        +---------------------------------------+----------------------------------------------+---------------------------------------------------+
        | link-traffic-test/comments            | Displays the test status detailed   comments.|:func:`peek_link_traffic_test_comments`            |
        +---------------------------------------+----------------------------------------------+---------------------------------------------------+
        | start-time                            | Displays the start time of the          test.|:func:`peek_start_time`                            |
        +---------------------------------------+----------------------------------------------+---------------------------------------------------+
        | frame-count                           | Sets the number of frames for the link test. |:func:`set_frame_count`                            |
        |                                       |                                              |:func:`peek_frame_count`                           |
        +---------------------------------------+----------------------------------------------+---------------------------------------------------+
        | frame-size                            | Sets the size of frames for the link   test. |:func:`set_frame_size`                             |
        |                                       |                                              |:func:`peek_frame_size`                            |
        +---------------------------------------+----------------------------------------------+---------------------------------------------------+
        | time                                  | Sets the duration of the test.               |:func:`set_time`                                   |
        |                                       |                                              |:func:`peek_time`                                  |
        +---------------------------------------+----------------------------------------------+---------------------------------------------------+
        | payload-pattern/pattern               | Sets the industry-defined pattern. names     |:func:`set_payload_pattern_pattern`                |
        |                                       |                                              |:func:`peek_payload_pattern_pattern`               |
        +---------------------------------------+----------------------------------------------+---------------------------------------------------+
        | payload-pattern/payload               | Sets the user-defined pattern.               |:func:`set_payload_pattern_payload`                |
        |                                       |                                              |:func:`peek_payload_pattern_payload`               |
        +---------------------------------------+----------------------------------------------+---------------------------------------------------+
        | fec/enable                            | Sets the FEC mode.                           |:func:`set_fec_enable`                             |
        |                                       |                                              |:func:`peek_fec_enable`                            |
        +---------------------------------------+----------------------------------------------+---------------------------------------------------+
        | fec/active                            | Displays the FEC mode.                       |:func:`peek_fec_active`                            |
        +---------------------------------------+----------------------------------------------+---------------------------------------------------+
        | fec/option                            | Displays the FEC option.                     |:func:`peek_fec_option`                            |
        +---------------------------------------+----------------------------------------------+---------------------------------------------------+
        | cr/enable                             | Sets the CR mode.                            |:func:`set_cr_enable`                              |
        |                                       |                                              |:func:`peek_cr_enable`                             |
        +---------------------------------------+----------------------------------------------+---------------------------------------------------+
        | cr/active                             | Displays the  CR mode.                       |:func:`peek_cr_active`                             |
        +---------------------------------------+----------------------------------------------+---------------------------------------------------+
        | cr/option                             | Displays the  CR option.                     |:func:`peek_cr_option`                             |
        +---------------------------------------+----------------------------------------------+---------------------------------------------------+
        | rt-latency                            | Displays the round-trip latency.             |:func:`peek_rt_latency`                            |
        +---------------------------------------+----------------------------------------------+---------------------------------------------------+
        | buffers-required                      | Displays the buffers required for the link.  |:func:`peek_buffers_required`                      |
        +---------------------------------------+----------------------------------------------+---------------------------------------------------+
        | failure-report/errors-detected-local  | Displays the failures detected locally.      |:func:`peek_failure_report_errors_detected_local`  |
        +---------------------------------------+----------------------------------------------+---------------------------------------------------+
        | failure-report/errors-detected-remote | Displays the failures detected remotely.     |:func:`peek_failure_report_errors_detected_remote` |
        +---------------------------------------+----------------------------------------------+---------------------------------------------------+
        | end-time                              | Displays the diag end timestamp.             |:func:`peek_end_time`                              |
        +---------------------------------------+----------------------------------------------+---------------------------------------------------+
        | egress-power-loss/tx                  | Displays the local power transmitted.        |:func:`peek_egress_power_loss_tx`                  |
        +---------------------------------------+----------------------------------------------+---------------------------------------------------+
        | egress-power-loss/rx                  | Displays the local power received.           |:func:`peek_egress_power_loss_rx`                  |
        +---------------------------------------+----------------------------------------------+---------------------------------------------------+
        | egress-power-loss/loss                | Displays the local power loss.               |:func:`peek_egress_power_loss_loss`                |
        +---------------------------------------+----------------------------------------------+---------------------------------------------------+
        | egress-power-loss/comments            | Displays the local power loss details.       |:func:`peek_egress_power_loss_comments`            |
        +---------------------------------------+----------------------------------------------+---------------------------------------------------+
        | ingress-power-loss/tx                 | Displays the remote power transmitted.       |:func:`peek_ingress_power_loss_tx`                 |
        +---------------------------------------+----------------------------------------------+---------------------------------------------------+
        | ingress-power-loss/rx                 | Displays the remote power received.          |:func:`peek_ingress_power_loss_rx`                 |
        +---------------------------------------+----------------------------------------------+---------------------------------------------------+
        | ingress-power-loss/loss               | Displays the remote power loss.              |:func:`peek_ingress_power_loss_loss`               |
        +---------------------------------------+----------------------------------------------+---------------------------------------------------+
        | ingress-power-loss/comments           | Displays the remote power loss details.      |:func:`peek_ingress_power_loss_comments`           |
        +---------------------------------------+----------------------------------------------+---------------------------------------------------+

    *Object Methods*

        .. method:: get(session, name=None)

            Returns a :class:`fibrechannel_diagnostics` object or a
            list of objects filled with attributes gathered
            from the switch. If an optional name is given, either an
            object matching the name of the port is returned
            or an empty object is returned if no match is found.

            Each object can be printed using :func:`pyfos_util.response_print`,
            and individual attributes can be accessed through peek methods.

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: a :class:`fibrechannel` object if a name is given
                or a list of objects if there are more than one

        .. method:: patch(session)

            Applies configurable attribute(s) within the object
            to a port of the switch.

            *Below is an example using individual sets:*

            .. code-block:: python

                # once d_port is enabled on the port
                # set the payload
                diag_info = pyfos_switchfcport.fibrechannel_diagnostics()
                diag_info.set_name(name)
                diag_info.set_payload_pattern_payload("305402420")
                result = diag_info.patch(session)
                pyfos_util.response_print(result)

                # on enabled port, restart the test
                diag_info = pyfos_switchfcport.fibrechannel_diagnostics()
                diag_info.set_name(name)
                diag_info.set_diagnostic_control(pyfos_switchfcport.DIAG_RESTART)
                result = diag_info.patch(session)
                pyfos_util.response_print(result)

            *Below is an example of combining object initialization \
                    and attribute sets:*

            .. code-block:: python

                # once d_port is enabled on the port
                # set the payload
                diag_info = pyfos_switchfcport.fibrechannel_diagnostics(
                    {"name" : name,
                    "payload-pattern" : {"payload" : "305402420"}})
                result = diag_info.patch(session)
                pyfos_util.response_print(result)

                # on enabled port, restart the test
                diag_info = pyfos_switchfcport.fibrechannel_diagnostics(
                    {"name" : name,
                    "diagnostic-control" : pyfos_switchfcport.DIAG_RESTART})
                result = diag_info.patch(session)
                pyfos_util.response_print(result)

            .. code-block:: python

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: a dictionary of error or success information

    *Attribute Methods*

        .. method:: set_name(name)

            Sets the port name in the object.

            :param name: port name to be set within the object
            :rtype: None or a dictionary of error information

        .. method:: peek_name()

            Reads the port name in the object.

            :rtype: None or the port name

        .. method:: set_diagnostic_control(newmode)

            Sets the diag control mode in the object.

            :param newmode: new mode :data:`DIAG_STOP`, :data:`DIAG_START`,
                or :data:`DIAG_RESTART` to be set within the object
            :rtype: None or a dictionary of error information

        .. method:: peek_diagnostic_control()

            Reads the diag control mode in the object.

            :rtype: None or the diag control mode

        .. method:: peek_mode()

            Reads the manual or automatic mode in the object.

            :rtype: None or the current mode

        .. method:: peek_state()

            Reads the current diag state in the object.

            :rtype: None or the current diag state

        .. method:: peek_distance()

            Reads the estimated ISL distsance in the object.

            :rtype: None or the estimated ISL distsance

        .. method:: peek_electrical_loopback_test_result()

            Reads the test result in the object.

            :rtype: None or the test result

        .. method:: peek_electrical_loopback_test_comments()

            Reads the test details in the object.

            :rtype: None or the test details

        .. method:: peek_optical_loopback_test_result()

            Reads the test result in the object.

            :rtype: None or the test result

        .. method:: peek_optical_loopback_test_comments()

            Reads the test details in the object.

            :rtype: None or the port name

        .. method:: peek_link_traffic_test_result()

            Reads the test result in the object.

            :rtype: None or the test result

        .. method:: peek_link_traffic_test_comments()

            Reads the test details in the object.

            :rtype: None or the test details

        .. method:: peek_start_time()

            Reads the diag start timestamp in the object.

            :rtype: None or the diag start timestamp

        .. method:: set_frame_count(newcount)

            Sets the frame count to be used in the diag in the object.

            :param newcount: new count to be set within the object
            :rtype: None or a dictionary of error information

        .. method:: peek_frame_count()

            Reads the frame count in the object.

            :rtype: None or the frame count

        .. method:: set_frame_size(newsize)

            Sets the frame size to be used in the diag in the object.

            :param newsize: new size to be set within the object
            :rtype: None or a dictionary of error information

        .. method:: peek_frame_size()

            Reads the frame size in the object.

            :rtype: None or the frame size

        .. method:: set_time(newtime)

            Sets the test duration to be used in the diag in the object.

            :param newtime: new test duration to be set within the object
            :rtype: None or a dictionary of error information

        .. method:: peek_time()

            Reads the duration of the test in the object.

            :rtype: None or the duration of the test

        .. method:: set_payload_pattern_pattern(newpattern)

            Sets the test pattern name to be used in the diag in the object.

            :param newpattern: new test pattern name to
                be set within the object
            :rtype: None or a dictionary of error information

        .. method:: peek_payload_pattern_pattern()

            Reads the test pattern name in the object.

            :rtype: None or the test pattern name

        .. method:: set_payload_pattern_payload(newpayload)

            Sets the test payload in hex to be used in the diag in the object.

            :param newpayload: new test pattern to be set within the object
            :rtype: None or a dictionary of error information

        .. method:: peek_payload_pattern_payload()

            Reads the test pattern in the object.

            :rtype: None or the known test pattern

        .. method:: set_fec_enable(newmode)

            Sets the FEC mode to be used in the diag in the object.

            :param newmode: new mode of "yes" to
                be set within the object
            :rtype: None or a dictionary of error information

        .. method:: peek_fec_enable()

            Reads the FEC mode in the object.

            :rtype: None or the FEC mode

        .. method:: peek_fec_active()

            Reads the active FEC state in the object.

            :rtype: None or the active FEC state

        .. method:: set_cr_enable(newmode)

            Sets the CR mode to be used in the diag in the object.

            :param newmode: new mode of "yes" to
                be set within the object
            :rtype: None or a dictionary of error information

        .. method:: peek_cr_enable()

            Reads the CR mode in the object.

            :rtype: None or the CR mode

        .. method:: peek_cr_active()

            Reads the active CR state in the object.

            :rtype: None or the active CR state

        .. method:: peek_rt_latency()

            Reads the round-trip latency in the object.

            :rtype: None or the round-trip latency

        .. method:: peek_buffers_required()

            Reads the number of buffers required in the object.

            :rtype: None or the number of buffers required

        .. method:: peek_failure_report_errors_detected_local()

            Reads the local failure report in the object.

            :rtype: None or the local failure report

        .. method:: peek_failure_report_errors_detected_remote()

            Reads the remove failure report in the object.

            :rtype: None or the remote failure report

        .. method:: peek_end_time()

            Reads the test end timestamp in the object.

            :rtype: None or the test end timestamp

        .. method:: peek_egress_power_loss_tx()

            Reads the local transmit power loss in the object.

            :rtype: None or the local transmit power loss

        .. method:: peek_egress_power_loss_rx()

            Reads the local receive power loss in the object.

            :rtype: None or the local receive power loss

        .. method:: peek_egress_power_loss_loss()

            Reads the local power loss in the object.

            :rtype: None or the local power loss

        .. method:: peek_egress_power_loss_comments()

            Reads the local power loss details in the object.

            :rtype: None or the port name

        .. method:: peek_ingress_power_loss_tx()

            Reads the remote transmit power loss in the object.

            :rtype: None or the remote transmit power loss

        .. method:: peek_ingress_power_loss_rx()

            Reads the remote receive power loss in the object.

            :rtype: None or the remote receive power loss

        .. method:: peek_ingress_power_loss_loss()

            Reads the remote power loss in the object.

            :rtype: None or the remote power loss

        .. method:: peek_ingress_power_loss_comments()

            Reads the remote power loss details in the object.

            :rtype: None or the remote power loss details

        """

    def __init__(self, dictvalues={}):
        urilist = list([dict({'URIVER': version.VER_RANGE_820_TO_821A,
                              'URI': "/rest/running/diagnostics/" +
                              "fibrechannel-diagnostics"}),
                        dict({'URIVER': version.VER_RANGE_821b_and_ABOVE,
                              'URI': "/rest/running/" +
                              "brocade-fibrechannel-diagnostics/" +
                              "fibrechannel-diagnostics"})])
        super().__init__(pyfos_rest_util.rest_obj_type.port_diag, urilist)

        self.add(pyfos_rest_util.rest_attribute(
            "name", pyfos_type.type_wwn,
            None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute(
            "diagnostic-control", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "mode", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "state", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "distance", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "electrical-loopback-test", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute(
            "result", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
            ["electrical-loopback-test"])
        self.add(pyfos_rest_util.rest_attribute(
            "comments", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
            ["electrical-loopback-test"])
        self.add(pyfos_rest_util.rest_attribute(
            "optical-loopback-test", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute(
            "result", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
            ["optical-loopback-test"])
        self.add(pyfos_rest_util.rest_attribute(
            "comments", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
            ["optical-loopback-test"])
        self.add(pyfos_rest_util.rest_attribute(
            "link-traffic-test", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute(
            "result", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
            ["link-traffic-test"])
        self.add(pyfos_rest_util.rest_attribute(
            "comments", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
            ["link-traffic-test"])
        self.add(pyfos_rest_util.rest_attribute(
            "start-time", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "frame-count", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "frame-size", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "time", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "payload-pattern", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute(
            "pattern", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG),
            ["payload-pattern"])
        self.add(pyfos_rest_util.rest_attribute(
            "payload", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG),
            ["payload-pattern"])
        self.add(pyfos_rest_util.rest_attribute(
            "fec", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute(
            "enable", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG),
            ["fec"])
        self.add(pyfos_rest_util.rest_attribute(
            "active", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
            ["fec"])
        self.add(pyfos_rest_util.rest_attribute(
            "option", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
            ["fec"])
        self.add(pyfos_rest_util.rest_attribute(
            "cr", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute(
            "enable", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG),
            ["cr"])
        self.add(pyfos_rest_util.rest_attribute(
            "active", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
            ["cr"])
        self.add(pyfos_rest_util.rest_attribute(
            "option", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
            ["cr"])
        self.add(pyfos_rest_util.rest_attribute(
            "rt-latency", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "buffers-required", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "failure-report", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute(
            "errors-detected-local", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
            ["failure-report"])
        self.add(pyfos_rest_util.rest_attribute(
            "errors-detected-remote", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
            ["failure-report"])
        self.add(pyfos_rest_util.rest_attribute(
            "end-time", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "egress-power-loss", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute(
            "tx", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
            ["egress-power-loss"])
        self.add(pyfos_rest_util.rest_attribute(
            "rx", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
            ["egress-power-loss"])
        self.add(pyfos_rest_util.rest_attribute(
            "loss", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
            ["egress-power-loss"])
        self.add(pyfos_rest_util.rest_attribute(
            "comments", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
            ["egress-power-loss"])
        self.add(pyfos_rest_util.rest_attribute(
            "ingress-power-loss", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute(
            "tx", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
            ["ingress-power-loss"])
        self.add(pyfos_rest_util.rest_attribute(
            "rx", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
            ["ingress-power-loss"])
        self.add(pyfos_rest_util.rest_attribute(
            "loss", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
            ["ingress-power-loss"])
        self.add(pyfos_rest_util.rest_attribute(
            "comments", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG),
            ["ingress-power-loss"])

        self.load(dictvalues, 1)
