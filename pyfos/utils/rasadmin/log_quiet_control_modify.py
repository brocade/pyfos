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

:mod:`log_quiet_control_modify` - PyFOS util for configuring log_quiet_control
******************************************************************************
The :mod:`log_quiet_control_modify` provides for configuring log_quiet_control

This module is a standalone script that can be used to display raslog
attributes

* inputs:
    * -L=<login>: Login ID. If not provided, interactive
        prompt will request one.
    * -P=<password>: Password. If not provided, interactive
        prompt will request one.
    * -i=<IP address>: IP address
    * -f=<VFID>: VFID or -1 if VF is disabled. If unspecified,
        VFID of 128 is assumed.

* Util scripts options:

    * --log-type=LOG-TYPE       Set log type. LOG-TYPE = <audit|raslog>
    * --quiet=QUIET-FLAG        Set quiet status flag QUIET-FLAG = <true|false>
    * --etime=END-TIME          Set quiet end time. END-TIME = Time in <hh:mm>
    * --stime=START-TIME        Set quiet start time. START-TIME = Time <hh:mm>
    * --dow=WEEK-DAYS           Set days for quiet. DAYS = "mon;tue"

* outputs:
    * raslog attributes in JSON format

.. function:: set_quiet (session, log_type, flag, stime, etime, dow)

        Example usage of the method::

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

        * inputs:
            :param session: session returned by login.
            :param log_type: desired log type
            :param flag: desired quiet flag for log type
            :param stime: desired start-time
            :param etime: desired end-time
            :param dow: desired days of the week

        * outputs:
            :rtype: dictionary of return status matching rest response

        *use cases*

        1. Enables/Disables the quiet for logtypes.


"""

import pyfos.pyfos_auth as pyfos_auth
from pyfos.pyfos_brocade_logging import log_quiet_control
import pyfos.pyfos_util as pyfos_util
import sys
import pyfos.utils.brcd_util as brcd_util


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
