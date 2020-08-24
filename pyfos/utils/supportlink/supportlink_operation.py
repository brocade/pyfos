#!/usr/bin/env python3

# Copyright © 2018 Broadcom. All Rights Reserved. The term “Broadcom” refers to
# Broadcom Inc. and/or its subsidiaries.
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

:mod:`supportlink_operation` - PyFOS util to trigger the supportlink operation.
*******************************************************************************
The :mod:`supportlink_operation` util is used for the supportlink operation.

This module is a stand-alone script and API that can be used to execute the \
supportlink operation. Supportlink collects all log files from the switch
and copies them to the remote server.

* Input:

* Infrastructure Options:

    * -i,--ipaddr=IPADDR: The IP address of the FOS switch.
    * -L,--login=LOGIN: The login name.
    * -P,--password=PASSWORD: The password.
    * -f,--vfid=VFID         The VFID to which the request is \
                             directed [OPTIONAL].
    * -s,--secured=MODE      The HTTPS mode "self" or "CA" [OPTIONAL].
    * -v,--verbose           Verbose mode [OPTIONAL].
    * -a,--authtoken: AuthToken value or AuthTokenManager config\
                      file[OPTIONAL].
    * -z,--nosession: Sessionless authentication based login[OPTIONAL].
    * --nocredential: No credential to be sent in the request[OPTIONAL].

* Util Script Options:
    * --action=ACTION-TYPE: Sets the action type as default, collect or send.

* Output:

    * Status of the supportlink operation.

.. function:: _post_supportlink(session, ssObj)

    *Supportlink Operation*

        Example Usage of the Method::

            status = supportlink(session, ssObj)

        Details::

            ss_dict = {
                "action": action_type,
            }
            ss_obj = supportlink()
            ss_obj.load(ss_dict, 1)
            result = ss_obj.post(session)

        * Input:
            :param session: The session returned by the login.
            :param action: The action type of default/collect/send.

        * Output:
            :rtype: A dictionary of return status matching the REST response.

        *Use Cases*

         Trigger supportlink and retrieve the status.

"""

import sys
from pyfos import pyfos_auth
from pyfos.pyfos_brocade_operation_supportlink import supportlink
from pyfos import pyfos_util
from pyfos.utils import brcd_util


def _post_supportlink(session, ss):
    return ss.post(session)


def ss_validate(ss_obj):
    if (ss_obj.peek_action() is None):
        return 1
    return 0


def main(argv):
    filters = ['action']
    inputs = brcd_util.parse(argv, supportlink, filters, ss_validate)
    ss_obj = inputs['utilobject']
    session = brcd_util.getsession(inputs)
    ss_rsp_obj = _post_supportlink(session, ss_obj)
    pyfos_util.response_print(ss_rsp_obj)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
