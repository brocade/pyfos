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

:mod:`log_setting_keep_alive_period_set` - PyFOS util for setting the\
 keepalive period.
******************************************************************************************
The :mod:`log_setting_keep_alive_period_set` util provides for setting the\
 keepalive period.

This module is a stand-alone script that can be used to set the\
 keepalive period.

* Input:
    * -L=<login>: The login ID. If not provided, an interactive
        prompt will request one.
    * -P=<password>: The password. If not provided, an interactive
        prompt will request one.
    * -i=<IP address>: The IP address.
    * -f=<VFID>: The VFID or -1 if VF is disabled. If unspecified,
        a VFID of 128 is assumed.

* Util Script Options:
    * --alive=ALIVE-PERIOD     Sets the alive period for the login hours.

* Output:
    * Log setting attributes in JSON format.


.. function:: set_alive_period(session, period)

        Example Usage of the Method::

            ret = log_setting_keep_alive_period_set.set_alive_period(session,
                    period)
            print (ret)

        Details::

            obj = {
                    "keep-alive-period": period
                }
            log_setting_obj = log_setting(obj)
            result =_set_alive_period(session, log_setting_obj)
            return result

        * Input:
            :param session: The session returned by the login.
            :param period: The keepalive period in hours.

        * Output:
            :rtype: A dictionary of return status matching the REST response.

        *Use Cases*

        1. Configure the keepalive period of the RASLog.

"""

import sys
from pyfos import pyfos_auth
from pyfos.pyfos_brocade_logging import log_setting
from pyfos import pyfos_util
from pyfos.utils import brcd_util


def validate(log_setting_obj):
    return 1 if log_setting_obj.peek_keep_alive_period() is None else 0


def set_alive_period(session, period):
    obj = {
            "keep-alive-period": period
        }
    log_setting_obj = log_setting(obj)
    result = _set_alive_period(session, log_setting_obj)
    return result


def _set_alive_period(session, restobj):
    return restobj.patch(session)


def main(argv):

    filters = ['keep_alive_period']
    inputs = brcd_util.parse(argv, log_setting, filters, validate)

    session = brcd_util.getsession(inputs)

    result = _set_alive_period(inputs['session'], inputs['utilobject'])

    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
