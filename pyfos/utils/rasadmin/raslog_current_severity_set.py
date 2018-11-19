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

:mod:`raslog_current_severity_set` - PyFOS util for configuring raslog
**********************************************************************
The :mod:`raslog_current_severity_set` provides for configuring raslog

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
    * --msg=MSG-IDENTIFIER                              Set Message Id.
    * --severity=SEVERITY-LEVEL                         Set Message Severity.

* outputs:
    * raslog attributes in JSON format

.. function:: set_message_severity (session, msg_id, severity)

        Example usage of the method::

            ret =
                    raslog_current_severity_set.set_message_severity(
                    session, msg_id, severity)
            print (ret)

        Details::

            val = {
                    "message-id": msg_id,
                    "current-severity": severity
                }
            obj = raslog(val)
            result = _set_message_severity (session, obj)
            return result

        * inputs:
            :param session: session returned by login.
            :param msg_id: desired raslog message-id
            :param severity: desired severity for raslog

        * outputs:
            :rtype: dictionary of return status matching rest response

        *use cases*

        1. Configures the severity of the raslog message.

"""

import sys
from pyfos import pyfos_auth
from pyfos.pyfos_brocade_logging import raslog
from pyfos import pyfos_util
from pyfos.utils import brcd_util


def set_message_severity(session, msg_id, severity):
    val = {
            "message-id": msg_id,
            "current-severity": severity
        }
    obj = raslog(val)
    result = _set_message_severity(session, obj)
    return result


def validate(raslog_obj):
    return 1 if raslog_obj.peek_current_severity() is None else 0


def _set_message_severity(session, restobject):
    return restobject.patch(session)


def main(argv):

    filters = ['message_id', 'current_severity']
    inputs = brcd_util.parse(argv, raslog, filters, validate)

    session = brcd_util.getsession(inputs)

    result = _set_message_severity(inputs['session'], inputs['utilobject'])

    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
