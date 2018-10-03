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
:mod:`syslog_facility_modify` - PyFOS util to modify syslog facility\
 configuration on switch.
***********************************************************************************\
*************************
The :mod:`syslog_facility_modify` provides option to modify the config\
 parameter of syslog facility level on switch.

This module is a standalone script that can be used to modify the syslog\
 facility configuration on switch.

* inputs:

| Infrastructure options:

  | -i,--ipaddr=IPADDR     IP address of FOS switch.
  | -L,--login=LOGIN       login name.
  | -P,--password=PASSWORD password.
  | -f,--vfid=VFID         VFID to which the request is directed to [OPTIONAL].
  | -s,--secured=MODE      HTTPS mode "self" or "CA" [OPTIONAL].
  | -v,--verbose           verbose mode[OPTIONAL].

| Util scripts options:

  | --syslog_facility_level=facility-level

* outputs:
    * Status of modify operation

.. function:: modify_syslog_facility(session, facility):

        Example usage of the method::

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


        * inputs:
                :param session: session returned by login.
                :param syslog_facility_level: facility-level

        * outputs:
                :rtype: dictionary of return status matching rest response

        *use cases*

         Modify the syslog facility level configuration.
"""

import sys
import pyfos.pyfos_auth as pyfos_auth
import pyfos.pyfos_util as pyfos_util
from pyfos.pyfos_brocade_logging import log_setting
import pyfos.utils.brcd_util as brcd_util


def _modify_syslog_facility(session, restobject):
    return restobject.patch(session)


def modify_syslog_facility(session, facility):
    facility_obj = log_setting()
    if facility is None:
        return
    facility_obj.set_syslog_facility_level(facility)
    result = _modify_syslog_facility(session, facility_obj)
    return result


def validate(syslog_obj):
    if (not syslog_obj.peek_syslog_facility_level()):
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
