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

:mod:`raslog_message_enabled_set` - PyFOS util for configuring raslog
*********************************************************************
The :mod:`raslog_message_enabled_set` provides for configuring raslog

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
    * --msg=MSG-IDENTIFIER      Set Message Id.
    * --enable=ENABLE-FLAG      Set Message Status flag <True|False>.

* outputs:
    * raslog attributes in JSON format


.. function:: set_message(session, msg_id, msg_flag)

        Example usage of the method::

            ret=raslog_message_enabled_set.set_message(session,msg_id,msg_flag)
            print (ret)

        Details::

            obj = {
                "message-enabled": msg_flag,
                "message-id": msg_id
            }
            raslog_obj = raslog(obj)
            result = _set_message(session, raslog_obj)

        * inputs:
            :param session: session returned by login.
            :param msg_id: desired raslog message-id
            :param msg_flag: desired message flag for raslog message-id

        * outputs:
            :rtype: dictionary of return status matching rest response

        *use cases*

        1. Enables/Disables the raslog message.

"""
import pyfos.pyfos_auth as pyfos_auth
from pyfos.pyfos_brocade_logging import raslog
import pyfos.pyfos_util as pyfos_util
import sys
import pyfos.utils.brcd_util as brcd_util


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
