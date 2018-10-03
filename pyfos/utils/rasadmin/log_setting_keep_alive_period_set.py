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

:mod:`log_setting_keep_alive_period_set` - PyFOS util for log_setting use case.
*******************************************************************************
The :mod:`log_setting_keep_alive_period_set` provides for log_setting use case.

This module is a standalone script that can be used to display log_setting
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
    * --alive=ALIVE-PERIOD     Set alive period for log in hours.

* outputs:
    * log_setting attributes in JSON format


.. function:: set_alive_period(session, period)

        Example usage of the method::

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

        * inputs:
            :param session: session returned by login.
            :param period: desired keep alive period in hr.

        * outputs:
            :rtype: dictionary of return status matching rest response

        *use cases*

        1. configures the keep alive period of the raslog

"""

import pyfos.pyfos_auth as pyfos_auth
from pyfos.pyfos_brocade_logging import log_setting
import pyfos.pyfos_util as pyfos_util
import sys
import pyfos.utils.brcd_util as brcd_util


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
