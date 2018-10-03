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

:mod:`raslog_get` - PyFOS util for configuring raslog op use case.
***********************************************************************************
The :mod:`raslog_get` provides for configuring raslog op use case.

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
    * --message-id <message_id>, Optional message id for the raslog to retrieve

* outputs:
    * raslog attributes in JSON format


.. function:: show_raslog(session, msg_id)

        Example usage of the method::

            ret = raslog_get.show_raslog(session, msg_id)
            print (ret)

        Details::

            result = raslog_get.show_raslog(
              session, 'AUTH-1001')

        * inputs:
            :param session: session returned by login.
            :param msg_id: Specific Raslog Message Id

        * outputs:
            :rtype: dictionary of return status matching rest response

        *use cases*

        1. Retrieve the raslog message.

"""

import pyfos.pyfos_auth as pyfos_auth
from pyfos.pyfos_brocade_logging import raslog
import pyfos.pyfos_util as pyfos_util
import sys
import pyfos.utils.brcd_util as brcd_util


def show_raslog(session, msg_id):
    raslog_obj = raslog()
    if msg_id is None:
        return raslog_obj.get(session)
    else:
        return raslog_obj.get(session, msg_id)


def main(argv):

    filters = ['message_id']
    inputs = brcd_util.parse(argv, raslog, filters)

    session = brcd_util.getsession(inputs)

    msg_id = inputs['utilobject'].peek_message_id()
    result = show_raslog(inputs['session'], msg_id)

    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
