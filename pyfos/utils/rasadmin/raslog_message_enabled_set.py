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

:mod:`raslog_message_enabled_set` - PyFOS util for configuring the\
 RASLog message.
***********************************************************************************
The :mod:`raslog_message_enabled_set` util provides for configuring the
 RASLog message.

This module is a stand-alone script that can be used to display the\
 RASLog message attributes.

* Input:
    * -L=<login>: The login ID. If not provided, an interactive
        prompt will request one.
    * -P=<password>: The password. If not provided, an interactive
        prompt will request one.
    * -i=<IP address>: The IP address.
    * -f=<VFID>: The VFID or -1 if VF is disabled. If unspecified,
        a VFID of 128 is assumed.

* Util Script Options:
    * --msg=MSG-IDENTIFIER      Sets the message ID.
    * --enable=ENABLE-FLAG      Sets the message status flag <true|false>.

* Output:
    * RASLog message attributes in JSON format.


.. function:: set_message(session, msg_id, msg_flag)

        Example Usage of the Method::

            ret=raslog_message_enabled_set.set_message(session,msg_id,msg_flag)
            print (ret)

        Details::

            obj = {
                "message-enabled": msg_flag,
                "message-id": msg_id
            }
            raslog_obj = raslog(obj)
            result = _set_message(session, raslog_obj)

        * Input:
            :param session: The session returned by the login.
            :param msg_id: The RASLog message ID.
            :param msg_flag: The message flag for the RASLog message ID.

        * Output:
            :rtype: A dictionary of return status matching the REST response.

        *Use Cases*

        1. Enable or disable the RASLog message.

"""
import sys
from pyfos import pyfos_auth
from pyfos.pyfos_brocade_logging import raslog
from pyfos import pyfos_util
from pyfos.utils import brcd_util


def set_message(session, msg_id, enabled_flag):
    obj = {
        "message-enabled": enabled_flag,
        "message-id": msg_id
    }
    raslog_obj = raslog(obj)
    result = _set_message(session, raslog_obj)
    return result


def _set_message(session, restobject):
    return restobject.patch(session)


def validate(raslog_obj):
    return 1 if raslog_obj.peek_message_enabled() is None else 0


def main(argv):

    filters = ['message_id', 'message_enabled']
    inputs = brcd_util.parse(argv, raslog, filters, validate)

    session = brcd_util.getsession(inputs)

    result = _set_message(inputs['session'], inputs['utilobject'])

    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
