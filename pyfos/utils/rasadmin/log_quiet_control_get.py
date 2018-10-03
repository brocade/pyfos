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

:mod:`log_quiet_control_get` - PyFOS util for configuring log_quiet_control
***************************************************************************
The :mod:`log_quiet_control_get` provides for configuring log_quiet_control

This module is a standalone script that can be used to display
log_quiet_control attributes

* inputs:
    * -L=<login>: Login ID. If not provided, interactive
        prompt will request one.
    * -P=<password>: Password. If not provided, interactive
        prompt will request one.
    * -i=<IP address>: IP address
    * -f=<VFID>: VFID or -1 if VF is disabled. If unspecified,
        VFID of 128 is assumed.

* Util scripts options:
    * --log-type <log_type>, Optional logtype to retrieve

* outputs:
    * log_quiet_control attributes in JSON format

.. function:: show_log_quiet_control(session)

        Example usage of the method::

            ret = log_quiet_control_get.show_log_quiet_control(session,
                    log_type)
            print (ret)

        Details::

            result = log_quiet_control_get.show_log_quiet_control(
              session, 'raslog')

        * inputs:
            :param session: session returned by login.
            :param log_type: Optional Specific Log type

        * outputs:
            :rtype: dictionary of return status matching rest response

        *use cases*

        1. Retrieve the list/row of Quiet information.


"""

import pyfos.pyfos_auth as pyfos_auth
from pyfos.pyfos_brocade_logging import log_quiet_control
import pyfos.pyfos_util as pyfos_util
import sys
import pyfos.utils.brcd_util as brcd_util


def show_log_quiet_control(session, log_id):
    log_quiet_control_obj = log_quiet_control()
    if log_id is None:
        return log_quiet_control_obj.get(session)
    else:
        return log_quiet_control_obj.get(session, log_id)


def main(argv):

    filters = ['log_type']
    inputs = brcd_util.parse(argv, log_quiet_control, filters)

    session = brcd_util.getsession(inputs)

    log_type = inputs['utilobject'].peek_log_type()
    result = show_log_quiet_control(inputs['session'], log_type)

    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
