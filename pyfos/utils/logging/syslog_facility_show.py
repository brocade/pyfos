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
:mod:`syslog_facility_show` - PyFOS util to display syslog facility\
configuration on switch.
***********************************************************************************\
*************************
:mod:`syslog_facility_show` provides option to display the config parameter\
of syslog facility level on switch.

This module is a standalone script that can be used to display the syslog
facility configuration on switch.

* inputs:

| Infrastructure options:

  | -i,--ipaddr=IPADDR     IP address of FOS switch.
  | -L,--login=LOGIN       login name.
  | -P,--password=PASSWORD password.
  | -f,--vfid=VFID         VFID to which the request is directed to [OPTIONAL].
  | -s,--secured=MODE      HTTPS mode "self" or "CA" [OPTIONAL].
  | -v,--verbose           verbose mode[OPTIONAL].


* outputs:
    * Status of show operation

.. function:: show_syslog_facility(session)

        Example usage of the method::

            ret = syslog_facility_show.show_syslog_facility(session)
            print (ret)

        Details::

            result = syslog_facility_show.show_syslog_facility(session)

        * inputs:
            :param session: session returned by login.

        * outputs:
            :rtype: dictionary of return status matching rest response

        *use cases*

           Retrieve syslog facility-level information.

"""

import sys
import pyfos.pyfos_auth as pyfos_auth
import pyfos.pyfos_util as pyfos_util
from pyfos.pyfos_brocade_logging import log_setting
import pyfos.utils.brcd_util as brcd_util


def show_syslog_facility(session):
    facility_obj = log_setting()
    return facility_obj.get(session).peek_syslog_facility_level()


def main(argv):

    # Print arguments
    # print(sys.argv[1:])

    filters = ['']
    inputs = brcd_util.parse(argv, log_setting, filters)

    session = brcd_util.getsession(inputs)

    result = show_syslog_facility(inputs['session'])

    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
