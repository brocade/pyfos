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

:mod:`log_setting_keep_alive_period_get` - PyFOS util for setting alive period
******************************************************************************
The :mod:`log_setting_keep_alive_period_get` provides for configuring period

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

* outputs:
    * log_setting attributes in JSON format


.. function:: show_alive_period(session)

        Example usage of the method::

            ret = log_setting_keep_alive_period_get.show_alive_period(session)
            print (ret)

        Details::

            result = log_setting_keep_alive_period_get.show_alive_period(
                    session)

        * inputs:
            :param session: session returned by login.

        * outputs:
            :rtype: dictionary of return status matching rest response

        *use cases*

        1. Retrieve the keep alive period of the raslog

"""

import pyfos.pyfos_auth as pyfos_auth
from pyfos.pyfos_brocade_logging import log_setting
import pyfos.pyfos_util as pyfos_util
import sys
import pyfos.utils.brcd_util as brcd_util


def show_alive_period(session):
    log_setting_obj = log_setting()
    return log_setting_obj.get(session, None, ["keep_alive_period"])


def main(argv):

    filters = []
    inputs = brcd_util.parse(argv, log_setting, filters)

    session = brcd_util.getsession(inputs)

    result = show_alive_period(inputs['session'])

    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
