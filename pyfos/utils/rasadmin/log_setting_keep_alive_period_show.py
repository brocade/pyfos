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

:mod:`log_setting_keep_alive_period_show` - PyFOS util for setting the\
 keepalive period.
***************************************************************************\
******************
The :mod:`log_setting_keep_alive_period_show` util provides for configuring\
 the keepalive period.

This module is a stand-alone script that can be used to display log setting
attributes.

* Input:
    * -L=<login>: The login ID. If not provided, an interactive
        prompt will request one.
    * -P=<password>: The password. If not provided, an interactive
        prompt will request one.
    * -i=<IP address>: The IP address.
    * -f=<VFID>: The VFID or -1 if VF is disabled. If unspecified,
        a VFID of 128 is assumed.

* Output:
    * Log setting attributes in JSON format.


.. function:: show_alive_period(session)

        Example Usage of the Method::

            ret = log_setting_keep_alive_period_show.show_alive_period(session)
            print (ret)

        Details::

            result = log_setting_keep_alive_period_show.show_alive_period(
                    session)

        * Input:
            :param session: The session returned by the login.

        * Output:
            :rtype: A dictionary of return status matching the REST response.

        *Use Cases*

        1. Retrieve the keepalive period of the RASLog.

"""

import sys
from pyfos import pyfos_auth
from pyfos.pyfos_brocade_logging import log_setting
from pyfos import pyfos_util
from pyfos.utils import brcd_util


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
