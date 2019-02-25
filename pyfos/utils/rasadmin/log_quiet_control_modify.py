#!/usr/bin/env python3

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

:mod:`log_quiet_control_modify` - PyFOS util for configuring log quiet control.
********************************************************************************
The :mod:`log_quiet_control_modify` util provides for configuring log\
 quiet control.

This module is a stand-alone script that can be used to display the RASLog
attributes.

* Input:
    * -L=<login>: The login ID. If not provided, an interactive
        prompt will request one.
    * -P=<password>: The password. If not provided, an interactive
        prompt will request one.
    * -i=<IP address>: The IP address.
    * -f=<VFID>: The VFID or -1 if VF is disabled. If unspecified,
        a VFID of 128 is assumed.

* Util Script Options:

    * --log-type=LOG-TYPE       Sets the log type <audit|raslog>.
    * --quiet=QUIET-FLAG        Sets the quiet status flag <true|false>.
    * --etime=END-TIME          Sets the quiet end time <hh:mm>.
    * --stime=START-TIME        Sets the quiet start time <hh:mm>.
    * --dow=WEEK-DAYS           Sets the days for quiet\
                                 (for example, "mon;tue").

* Output:
    * RASLog attributes in JSON format.

.. function:: set_quiet (session, log_type, flag, stime, etime, dow)

        Example Usage of the Method::

            ret = log_quiet_control_modify.set_quiet(session, log_type, flag,
                    stime, etime, dow)
            print (ret)

        Details::

            val = {
                    "log-type": log_type,
                    "quiet-enabled": flag,
                    "start-time": stime,
                    "end-time": etime,
                    "days-of-week": dow
                }
            lobj = log_quiet_control(val)
            result = _set_quiet(session, lobj)
            return result

        * Input:
            :param session: The session returned by the login.
            :param log_type: The log type.
            :param flag: The quiet flag for the log type.
            :param stime: The start time.
            :param etime: The end time.
            :param dow: The days of the week.

        * Output:
            :rtype: A dictionary of return status matching the REST response.

        *Use Cases*

        1. Enable or disable the quiet flag for log types.


"""

import sys
from pyfos import pyfos_auth
from pyfos.pyfos_brocade_logging import log_quiet_control
from pyfos import pyfos_util
from pyfos.utils import brcd_util


def set_quiet(session, log_type, flag, stime, etime, dow):
    val = {
            "log-type": log_type,
            "quiet-enabled": flag,
            "start-time": stime,
            "end-time": etime,
            "days-of-week": dow
        }
    lobj = log_quiet_control(val)
    result = _set_quiet(session, lobj)
    return result


def validate(raslog_obj):
    return 1 if raslog_obj.peek_quiet_enabled() is None else 0


def _set_quiet(session, restobject):
    return restobject.patch(session)


def main(argv):

    filters = ['log_type', 'quiet_enabled', 'start_time', 'end_time',
               'days_of_week_day']

    inputs = brcd_util.parse(argv, log_quiet_control, filters, validate)

    session = brcd_util.getsession(inputs)

    result = _set_quiet(inputs['session'], inputs['utilobject'])

    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
