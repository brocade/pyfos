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

:mod:`log_quiet_control_show` - PyFOS util for configuring the log\
 quiet control.
*********************************************************************************
The :mod:`log_quiet_control_show` util provides for configuring the log\
 quiet control.

This module is a stand-alone script that can be used to display the log\
 quiet control attributes.

* Input:
    * -L=<login>: The login ID. If not provided, an interactive
        prompt will request one.
    * -P=<password>: The password. If not provided, an interactive
        prompt will request one.
    * -i=<IP address>: The IP address.
    * -f=<VFID>: The VFID or -1 if VF is disabled. If unspecified,
        a VFID of 128 is assumed.

* Util Script Options:
    * --log-type <log_type>: Sets the log type (optional) to retrieve.

* Output:
    * Log quiet control attributes in JSON format.

.. function:: show_log_quiet_control(session)

        Example Usage of the Method::

            ret = log_quiet_control_show.show_log_quiet_control(session,
                    log_type)
            print (ret)

        Details::

            result = log_quiet_control_show.show_log_quiet_control(
              session, 'raslog')

        * Input:
            :param session: The session returned by the login.
            :param log_type: The specific log type (optional).

        * Output:
            :rtype: A dictionary of return status matching the REST response.

        *Use Cases*

        1. Retrieve the list or row of quiet information.


"""

import sys
from pyfos import pyfos_auth
from pyfos.pyfos_brocade_logging import log_quiet_control
from pyfos import pyfos_util
from pyfos.utils import brcd_util


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
