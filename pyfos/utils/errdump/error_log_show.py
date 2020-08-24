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

:mod:`error_log_show` - PyFOS util for showing switch RASLogs.
***********************************************************************************
The :mod:`error_log_show` util provides for displaying the RASLogs accumulated
in a switch.

This module is a stand-alone script that can be used to display the attributes
of RASLog messages.

* Input:
    * -L=<login>: The login ID. If not provided, an interactive
        prompt will request one.
    * -P=<password>: The password. If not provided, an interactive
        prompt will request one.
    * -i=<IP address>: The IP address.
    * -f=<VFID>: The VFID or -1 if VF is disabled. If unspecified,
        a VFID of 128 is assumed.

* Util Script Options:
    * -m,--message-id=MSG_ID: Display RASlogs having given message-id.
    * -l,--severity-level=VALUE: Display RASlogs with given severity.
    *    --slot-id=VALUE: Display RASlogs from given slot-id.

* Output:
    * RASLog attributes in JSON format


.. function:: show_messages(session, msg_id)

        Example Usage of the Method::

            ret = error_log_show.show_messages(session, filters)
            print (ret)

        Details::

            raslog_obj = error_log()
            objlist = raslog_obj.get(session)
            if filter_applied is None:
              return objlist
            filtered_list = []

            if isinstance(objlist, error_log):
                objlist = [objlist]
            if isinstance(objlist, list):
                for i in range(len(objlist)):
                    if not isinstance(objlist[i], error_log):
                        continue
                    if filter_applied.peek_message_id() is not None and \
                       filter_applied.peek_message_id() != \
                       objlist[i].peek_message_id():
                        continue
                    if filter_applied.peek_severity_level() is not None and \
                       filter_applied.peek_severity_level() != \
                       objlist[i].peek_severity_level():
                        continue
                    if filter_applied.peek_slot_id() is not None and \
                       filter_applied.peek_slot_id() != \
                       objlist[i].peek_slot_id():
                        continue
                    filtered_list.append(objlist[i])
            else:
                return objlist
            return filtered_list

        * Input:
            :param session: The session returned by the login.
            :param msg_id: The specific RASLog message ID.

        * Output:
            :rtype: A dictionary of return status matching the REST response.

        *Use Cases*

        1. Retrieves the RASLog message.

"""

import sys
from pyfos import pyfos_auth
from pyfos.pyfos_brocade_logging import error_log
from pyfos import pyfos_util
from pyfos.utils import brcd_util


def show_messages(session, filter_applied):
    raslog_obj = error_log()
    objlist = raslog_obj.get(session)
    if filter_applied is None:
        return objlist
    filtered_list = []

    if isinstance(objlist, error_log):
        objlist = [objlist]
    if isinstance(objlist, list):
        for i in range(len(objlist)):
            if not isinstance(objlist[i], error_log):
                continue
            if filter_applied.peek_message_id() is not None and \
               filter_applied.peek_message_id() != \
               objlist[i].peek_message_id():
                continue
            if filter_applied.peek_severity_level() is not None and \
               filter_applied.peek_severity_level() != \
               objlist[i].peek_severity_level():
                continue
            if filter_applied.peek_slot_id() is not None and \
               filter_applied.peek_slot_id() != \
               objlist[i].peek_slot_id():
                continue
            filtered_list.append(objlist[i])
    else:
        return objlist
    return filtered_list


def main(argv):

    filters = ['message_id', 'severity_level', 'slot_id']
    inputs = brcd_util.parse(argv, error_log, filters, None)

    session = brcd_util.getsession(inputs)
    given_filters = inputs['utilobject']
    result = show_messages(inputs['session'], given_filters)

    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
