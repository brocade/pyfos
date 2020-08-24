#!/usr/bin/env python3.5

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
:mod:`clear_log_modify` - PyFOS util to clear switch RASlogs and auditlogs
*****************************************************************************
The :mod:`clear_log_modify` util provides the option to clear the \
RASlogs and auditlogs in a switch.

This module is a stand-alone script that can be used to clear the debug \
RASlogs and auditlogs in a switch

* Input:

| Infrastructure Options:

  | -i,--ipaddr=IPADDR     The IP address of the FOS switch.
  | -L,--login=LOGIN       The login name.
  | -P,--password=PASSWORD The password.
  | -f,--vfid=VFID         The VFID to which the request is \
                            directed [OPTIONAL].
  | -s,--secured=MODE      The HTTPS mode "self" or "CA" [OPTIONAL].
  | -v,--verbose           Verbose mode [OPTIONAL].

| Util Script Options:

  | -c,--clear_log=logtype: logtype=error-log to clear errdump,
                            logtype=audit-log to clear auditdump,
                            logtype=all to clear both errdump and \
                                 auditdump

* Output:
    * Status of the clear operation.

.. function:: modify_clear_log(session, logtype):

        Example Usage of the Method::

           ret = clear_log_modify.modify_clear_log(session, logtype)
           print (ret)

        Details::

            logsetting_obj = log_setting()
            if logtype is None:
                return None
            logsetting_obj.set_clear_log(logtype)
            result = _modify_clear_log(session, logsetting_obj)
            return result

        * Input:
                :param session: Session returned by login
                :param logtype: Log type to be cleared

        * Output:
                :rtype: A dictionary of return status matching the\
                 REST response.

        *Use Cases*

         Clear the switch RASlogs and auditlogs.
"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_logging import log_setting
from pyfos.utils import brcd_util
import pyfos.pyfos_version as version


def _modify_clear_log(session, restobject):
    return restobject.patch(session)


def modify_clear_log(session, logtype):
    logsetting_obj = log_setting()
    if logtype is None:
        return None
    logsetting_obj.set_clear_log(logtype)
    result = _modify_clear_log(session, logsetting_obj)
    return result


def validate(logsetting_obj):
    if logsetting_obj.peek_clear_log() is None:
        return 1
    return 0


def main(argv):

    filters = ['clear_log']

    inputs = brcd_util.parse(argv, log_setting, filters, validate)

    session = brcd_util.getsession(inputs)
    if session['version'] < version.fosversion("9.0.0"):
        print("PATCH operation on clear-log attribute\
 is supported from FOS v9.0.0")
        pyfos_auth.logout(session)
        return

    result = _modify_clear_log(inputs['session'], inputs['utilobject'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
