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

:mod:`raslog_syslog_enabled_set` - PyFOS util for configuring RASLog.
*******************************************************************************
The :mod:`raslog_syslog_enabled_set` util provides for configuring RASLog.

This module is a stand-alone script that can be used to display the RASLog
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
    * --msg=MSG-IDENTIFIER                         Sets the message ID.
    * --syslog-enable=SYSLOG-ENABLE                Sets the syslog status flag.

* Output:
    * RASLog attributes in JSON format.

.. function:: set_syslog(session, msg_id, flag)

        Example Usage of the Method::

            ret = raslog_syslog_enabled_set.set_syslog(session, msg_id, flag)
            print (ret)

        Details::

            val = {
                    "message-id": msg_id,
                    "syslog-enabled": syslog_flag
                }
            sobj = raslog(val)
            result = _set_syslog (session, sobj)
            return result


        * Input:
            :param session: The session returned by the login.
            :param msg_id: The RASLog message ID.
            :param flag: The syslog flag.

        * Output:
            :rtype: A dictionary of return status matching the REST response.

        *Use Cases*

        1. Enable or disable the syslog message.


"""

import sys
from pyfos import pyfos_auth
from pyfos.pyfos_brocade_logging import raslog
from pyfos import pyfos_util
from pyfos.utils import brcd_util


def set_syslog(session, msg_id, syslog_flag):
    val = {
            "message-id": msg_id,
            "syslog-enabled": syslog_flag
        }
    sobj = raslog(val)
    result = _set_syslog(session, sobj)
    return result


def _set_syslog(session, restobject):
    return restobject.patch(session)


def main(argv):

    filters = ['message_id', 'syslog_enabled']
    inputs = brcd_util.parse(argv, raslog, filters)

    session = brcd_util.getsession(inputs)

    result = _set_syslog(inputs['session'], inputs['utilobject'])

    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
