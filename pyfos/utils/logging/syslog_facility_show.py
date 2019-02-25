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
:mod:`syslog_facility_show` - PyFOS util to display the syslog facility \
configuration on a switch.
***********************************************************************************\
*************************
The :mod:`syslog_facility_show` util provides the option to display the \
configuration parameter of the syslog facility level on a switch.

This module is a stand-alone script that can be used to display the syslog
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


* Output:
    * Status of the show operation.

.. function:: show_syslog_facility(session)

        Example Usage of the Method::

            ret = syslog_facility_show.show_syslog_facility(session)
            print (ret)

        Details::

            result = syslog_facility_show.show_syslog_facility(session)

        * Input:
            :param session: The session returned by the login.

        * Output:
            :rtype: A dictionary of return status matching the REST response.

        *Use Cases*

           Retrieve the syslog facility level information.

"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_logging import log_setting
from pyfos.utils import brcd_util


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
