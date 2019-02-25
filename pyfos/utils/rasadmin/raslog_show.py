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

:mod:`raslog_show` - PyFOS util for retrieving the RASLog message.
***********************************************************************************
The :mod:`raslog_show` util provides for retrieving the RASLog message.

This module is a stand-alone script that can be used to display RASLog message
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
    * --message-id <message_id>: Sets the message ID for the RASLog\
                                  to retrieve.

* Output:
    * RASLog attributes in JSON format.


.. function:: show_raslog(session, msg_id)

        Example Usage of the Method::

            ret = raslog_show.show_raslog(session, msg_id)
            print (ret)

        Details::

            result = raslog_show.show_raslog(
              session, 'AUTH-1001')

        * Input:
            :param session: The session returned by the login.
            :param msg_id: The specific RASLog message ID.

        * Output:
            :rtype: A dictionary of return status matching the REST response.

        *Use Cases*

        1. Retrieve the RASLog message.

"""

import sys
from pyfos import pyfos_auth
from pyfos.pyfos_brocade_logging import raslog
from pyfos import pyfos_util
from pyfos.utils import brcd_util


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
