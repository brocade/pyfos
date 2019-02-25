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
:mod:`syslog_facility_modify` - PyFOS util to modify the syslog facility\
 configuration on a switch.
***********************************************************************************\
*************************
The :mod:`syslog_facility_modify` util provides the option to modify the \
configuration parameter of the syslog facility level on a switch.

This module is a stand-alone script that can be used to modify the syslog \
facility configuration on a switch.

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

  | --syslog_facility_level=facility-level

* Output:
    * Status of the modify operation.

.. function:: modify_syslog_facility(session, facility):

        Example Usage of the Method::

           ret = syslog_facility_modify.modify_syslog_server(session, facility)
           print (ret)

        Details::

              val = {
                     "facility": facility-level
                    }

            facility_obj = log_setting()
            facility_obj.set_syslog_facility_level(facility)
            result = _modify_syslog_facility(session, facility_obj)
            return result


        * Input:
                :param session: The session returned by the login.
                :param syslog_facility_level: The facility level.

        * Output:
                :rtype: A dictionary of return status matching the\
                 REST response.

        *Use Cases*

         Modify the syslog facility level configuration.
"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_logging import log_setting
from pyfos.utils import brcd_util


def _modify_syslog_facility(session, restobject):
    return restobject.patch(session)


def modify_syslog_facility(session, facility):
    facility_obj = log_setting()
    if facility is None:
        return None
    facility_obj.set_syslog_facility_level(facility)
    result = _modify_syslog_facility(session, facility_obj)
    return result


def validate(syslog_obj):
    if not syslog_obj.peek_syslog_facility_level():
        return 1
    return 0


def main(argv):

    # Print arguments
    # print(sys.argv[1:])

    filters = ['syslog_facility_level']

    inputs = brcd_util.parse(argv, log_setting, filters, validate)

    session = brcd_util.getsession(inputs)

    result = _modify_syslog_facility(inputs['session'], inputs['utilobject'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
