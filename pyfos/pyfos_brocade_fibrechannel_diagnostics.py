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
        provide rest support for FC port diagnostics.
*************************************************************************************************************************************
The :mod:`pyfos_brocade_fibrechannel_diagnostics` provides a REST \
        support for FC port diagnostics.

"""

import pyfos.pyfos_rest_util as pyfos_rest_util
from pyfos.pyfos_type import pyfos_type


DIAG_STOP = 0
DIAG_START = 1
DIAG_RESTART = 2

DIAG_YES = "yes"
DIAG_NO = "no"


class fibrechannel_diagnostics(pyfos_rest_util.rest_object):
    """Class of FC port diagnostics

    Important class members:

        +---------------------------------------+-------------------------------+---------------------------------------------------+
        | Attribute name                        | Description                   |Frequstly used methods                             |
        +=======================================+===============================+===================================================+
        | name                                  | name of port                  |:func:`set_name`                                   |
        |                                       |                               |:func:`peek_name`                                  |
        +---------------------------------------+-------------------------------+---------------------------------------------------+
        | diagnostic-control                    | set mode to stop, start,      |:func:`set_diagnostic_control`                     |
        |                                       | or restart                    |:func:`peek_diagnostic_control`                    |
        +---------------------------------------+-------------------------------+---------------------------------------------------+
        | mode                                  | display manual or auto mode   |:func:`peek_mode`                                  |
        +---------------------------------------+-------------------------------+---------------------------------------------------+
        | state                                 | test status                   |:func:`peek_state`                                 |
        +---------------------------------------+-------------------------------+---------------------------------------------------+
        | distance                              | estimated ISL distance        |:func:`peek_distance`                              |
        +---------------------------------------+-------------------------------+---------------------------------------------------+
        | electrical-loopback-test/result       | test status result            |:func:`peek_electrical_loopback_test_result`       |
        +---------------------------------------+-------------------------------+---------------------------------------------------+
        | electrical-loopback-test/comments     | test status detail comments   |:func:`peek_electrical_loopback_test_comments`     |
        +---------------------------------------+-------------------------------+---------------------------------------------------+
        | optical-loopback-test/result          | test status result            |:func:`peek_optical_loopback_test_result`          |
        +---------------------------------------+-------------------------------+---------------------------------------------------+
        | optical-loopback-test/comments        | test status detail comments   |:func:`peek_optical_loopback_test_comments`        |
        +---------------------------------------+-------------------------------+---------------------------------------------------+
        | link-traffic-test/result              | test status result            |:func:`peek_link_traffic_test_result`              |
        +---------------------------------------+-------------------------------+---------------------------------------------------+
        | link-traffic-test/comments            | test status detail comments   |:func:`peek_link_traffic_test_comments`            |
        +---------------------------------------+-------------------------------+---------------------------------------------------+
        | start-time                            | start time of the test        |:func:`peek_start_time`                            |
        +---------------------------------------+-------------------------------+---------------------------------------------------+
        | frame-count                           | number of frames for link test|:func:`set_frame_count`                            |
        |                                       |                               |:func:`peek_frame_count`                           |
        +---------------------------------------+-------------------------------+---------------------------------------------------+
        | frame-size                            | size of frames for link test  |:func:`set_frame_size`                             |
        |                                       |                               |:func:`peek_frame_size`                            |
        +---------------------------------------+-------------------------------+---------------------------------------------------+
        | time                                  | duration of test              |:func:`set_time`                                   |
        |                                       |                               |:func:`peek_time`                                  |
        +---------------------------------------+-------------------------------+---------------------------------------------------+
        | payload-pattern/pattern               | industry defined pattern names|:func:`set_payload_pattern_pattern`                |
        |                                       |                               |:func:`peek_payload_pattern_pattern`               |
        +---------------------------------------+-------------------------------+---------------------------------------------------+
        | payload-pattern/payload               | user defined pattern          |:func:`set_payload_pattern_payload`                |
        |                                       |                               |:func:`peek_payload_pattern_payload`               |
        +---------------------------------------+-------------------------------+---------------------------------------------------+
        | fec/enable                            | set FEC mode                  |:func:`set_fec_enable`                             |
        |                                       |                               |:func:`peek_fec_enable`                            |
        +---------------------------------------+-------------------------------+---------------------------------------------------+
        | fec/active                            | show FEC mode                 |:func:`peek_fec_active`                            |
        +---------------------------------------+-------------------------------+---------------------------------------------------+
        | fec/option                            | show FEC option               |:func:`peek_fec_option`                            |
        +---------------------------------------+-------------------------------+---------------------------------------------------+
        | cr/enable                             | set CR mode                   |:func:`set_cr_enable`                              |
        |                                       |                               |:func:`peek_cr_enable`                             |
        +---------------------------------------+-------------------------------+---------------------------------------------------+
        | cr/active                             | show CR mode                  |:func:`peek_cr_active`                             |
        +---------------------------------------+-------------------------------+---------------------------------------------------+
        | cr/option                             | show CR option                |:func:`peek_cr_option`                             |
        +---------------------------------------+-------------------------------+---------------------------------------------------+
        | rt-latency                            | round trip latency            |:func:`peek_rt_latency`                            |
        +---------------------------------------+-------------------------------+---------------------------------------------------+
        | buffers-required                      | buffer required for link      |:func:`peek_buffers_required`                      |
        +---------------------------------------+-------------------------------+---------------------------------------------------+
        | failure-report/errors-detected-local  | failure detected locally      |:func:`peek_failure_report_errors_detected_local`  |
        +---------------------------------------+-------------------------------+---------------------------------------------------+
        | failure-report/errors-detected-remote | failure detected remotely     |:func:`peek_failure_report_errors_detected_remote` |
        +---------------------------------------+-------------------------------+---------------------------------------------------+
        | end-time                              | diag end time stamp           |:func:`peek_end_time`                              |
        +---------------------------------------+-------------------------------+---------------------------------------------------+
        | egress-power-loss/tx                  | local power transmitted       |:func:`peek_egress_power_loss_tx`                  |
        +---------------------------------------+-------------------------------+---------------------------------------------------+
        | egress-power-loss/rx                  | local power received          |:func:`peek_egress_power_loss_rx`                  |
        +---------------------------------------+-------------------------------+---------------------------------------------------+
        | egress-power-loss/loss                | local power loss              |:func:`peek_egress_power_loss_loss`                |
        +---------------------------------------+-------------------------------+---------------------------------------------------+
        | egress-power-loss/comments            | local power loss details      |:func:`peek_egress_power_loss_comments`            |
        +---------------------------------------+-------------------------------+---------------------------------------------------+
        | ingress-power-loss/tx                 | remote power transmitted      |:func:`peek_ingress_power_loss_tx`                 |
        +---------------------------------------+-------------------------------+---------------------------------------------------+
        | ingress-power-loss/rx                 | remote power received         |:func:`peek_ingress_power_loss_rx`                 |
        +---------------------------------------+-------------------------------+---------------------------------------------------+
        | ingress-power-loss/loss               | remote power loss             |:func:`peek_ingress_power_loss_loss`               |
        +---------------------------------------+-------------------------------+---------------------------------------------------+
        | ingress-power-loss/comments           | remote power loss details     |:func:`peek_ingress_power_loss_comments`           |
        +---------------------------------------+-------------------------------+---------------------------------------------------+

    *Object methods*

        .. method:: get(session, name=None)

            Returns a :class:`fibrechannel_diagnostics` object or a
            list of objects filled with attributes gathered
            from switch. If optional name is given, either an
            object matching the name of the port is returned
            or an empty object is returned if no match is found.

            Each object can be printed using :func:`pyfos_util.response_print`
            and individual attributes accessed through peek methods.

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: a :class:`fibrechannel` object if name is given
                or a list of objects if there are more than one

        .. method:: patch(session)

            Apply configurable attribute(s) within the object
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

    *Attribute methods*

        .. method:: set_name(name)

            Sets port name in the object.

            :param name: port name to be set within the object
            :rtype: None or dictionary of error information

        .. method:: peek_name()

            Reads port name in the object.

            :rtype: None or port name

        .. method:: set_diagnostic_control(newmode)

            Sets diag control mode in the object.

            :param newmode: new mode :data:`DIAG_STOP`, :data:`DIAG_START`,
                or :data:`DIAG_RESTART` to be set within the object
            :rtype: None or dictionary of error information

        .. method:: peek_diagnostic_control()

            Reads diag control mode in the object.

            :rtype: None or diag control mode

        .. method:: peek_mode()

            Reads either manual or automatic mode in the object.

            :rtype: None or current mode

        .. method:: peek_state()

            Reads current diag state in the object.

            :rtype: None or current diag state

        .. method:: peek_distance()

            Reads estimated ISL distsance in the object.

            :rtype: None or estimated ISL distsance

        .. method:: peek_electrical_loopback_test_result()

            Reads test result in the object.

            :rtype: None or test result

        .. method:: peek_electrical_loopback_test_comments()

            Reads test details in the object.

            :rtype: None or test details

        .. method:: peek_optical_loopback_test_result()

            Reads test result in the object.

            :rtype: None or test result

        .. method:: peek_optical_loopback_test_comments()

            Reads test details in the object.

            :rtype: None or port name

        .. method:: peek_link_traffic_test_result()

            Reads test result in the object.

            :rtype: None or test result

        .. method:: peek_link_traffic_test_comments()

            Reads test details in the object.

            :rtype: None or test details

        .. method:: peek_start_time()

            Reads diag start timestamp in the object.

            :rtype: None or diag start timestamp

        .. method:: set_frame_count(newcount)

            Sets frame count to be used in diag in the object.

            :param newcount: new count to be set within the object
            :rtype: None or dictionary of error information

        .. method:: peek_frame_count()

            Reads frame count in the object.

            :rtype: None or frame count

        .. method:: set_frame_size(newsize)

            Sets frame size to be used in diag in the object.

            :param newsize: new size to be set within the object
            :rtype: None or dictionary of error information

        .. method:: peek_frame_size()

            Reads frame size in the object.

            :rtype: None or frame size

        .. method:: set_time(newtime)

            Sets test duration to be used in diag in the object.

            :param newtime: new test duration to be set within the object
            :rtype: None or dictionary of error information

        .. method:: peek_time()

            Reads duration of the test in the object.

            :rtype: None or duration of the test

        .. method:: set_payload_pattern_pattern(newpattern)

            Sets test pattern name to be used in diag in the object.

            :param newpattern: new test pattern name to
                be set within the object
            :rtype: None or dictionary of error information

        .. method:: peek_payload_pattern_pattern()

            Reads test pattern name in the object.

            :rtype: None or test pattern name

        .. method:: set_payload_pattern_payload(newpayload)

            Sets test payload in hex to be used in diag in the object.

            :param newpayload: new test pattern to be set within the object
            :rtype: None or dictionary of error information

        .. method:: peek_payload_pattern_payload()

            Reads test pattern in the object.

            :rtype: None or known test pattern

        .. method:: set_fec_enable(newmode)

            Sets fec mode to be used in diag in the object.

            :param newmode: new mode of "yes" to
                be set within the object
            :rtype: None or dictionary of error information

        .. method:: peek_fec_enable()

            Reads fec mode in the object.

            :rtype: None or fec mode

        .. method:: peek_fec_active()

            Reads active state of fec in the object.

            :rtype: None or active state of fec

        .. method:: set_cr_enable(newmode)

            Sets cr mode to be used in diag in the object.

            :param newmode: new mode of "yes" to
                be set within the object
            :rtype: None or dictionary of error information

        .. method:: peek_cr_enable()

            Reads cr mode in the object.

            :rtype: None or cr mode

        .. method:: peek_cr_active()

            Reads active state of cr in the object.

            :rtype: None or active state of cr

        .. method:: peek_rt_latency()

            Reads round trip latency in the object.

            :rtype: None or round trip latency

        .. method:: peek_buffers_required()

            Reads number of buffers required in the object.

            :rtype: None or number of buffers required

        .. method:: peek_failure_report_errors_detected_local()

            Reads local failure report in the object.

            :rtype: None or local failure report

        .. method:: peek_failure_report_errors_detected_remote()

            Reads remove failure report in the object.

            :rtype: None or remote failure report

        .. method:: peek_end_time()

            Reads test end timestamp in the object.

            :rtype: None or test end timestamp

        .. method:: peek_egress_power_loss_tx()

            Reads local transmit power loss in the object.

            :rtype: None or local transmit power loss

        .. method:: peek_egress_power_loss_rx()

            Reads local receive power loss in the object.

            :rtype: None or local receive power loss

        .. method:: peek_egress_power_loss_loss()

            Reads local power loss in the object.

            :rtype: None or local power loss

        .. method:: peek_egress_power_loss_comments()

            Reads local power loss details in the object.

            :rtype: None or port name

        .. method:: peek_ingress_power_loss_tx()

            Reads remote transmit power loss in the object.

            :rtype: None or remote transmit power loss

        .. method:: peek_ingress_power_loss_rx()

            Reads remote receive power loss in the object.

            :rtype: None or remote receive power loss

        .. method:: peek_ingress_power_loss_loss()

            Reads remote power loss in the object.

            :rtype: None or remote power loss

        .. method:: peek_ingress_power_loss_comments()

            Reads remote power loss details in the object.

            :rtype: None or remote power loss details

        """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.port_diag,
                         "/rest/running/diagnostics/fibrechannel-diagnostics")

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
