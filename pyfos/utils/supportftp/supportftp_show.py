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

:mod:`supportftp_show` - PyFOS util for showing supportftp config.
*******************************************************************************
The :mod:`supportftp_show` util is used to show the supportftp config used to
access FTP server for sending trace data.

This module is a standalone script that can be used to display the config
parameters for supportftp

* inputs:
    * -L=<login>: Login ID. If not provided, interactive
        prompt will request one.
    * -P=<password>: Password. If not provided, interactive
        prompt will request one.
    * -i=<IP address>: IP address
    * -f=<VFID>: VFID or -1 if VF is disabled. If unspecified,
        VFID of 128 is assumed.


* outputs:
    * Python dictionary content with RESTCONF response data.

.. function:: show_supportftp_params(session)

        Example usage of the method::

            ret = supportftp_show.show_supportftp_params(session)
            print (ret)

        Details::

            filters = ["host", "user_name", "remote_directory", \
                  "auto_enabled", "protocol", "port", \
                  "connectivity_check_interval"]
            result = supportftp.get(session, None, filters)
            return result

        * inputs:
            :param session: session returned by login.

        * outputs:
            :rtype: dictionary of return status matching rest response

        *use cases*

        1. Retrieve the IP address/DNS name of host FTP server
        2. Retrieve user name of account in server
        3. Retrieve directory path of trace data in server
        4. Retrieve auto-supportftp enable state in boolean
        5. Retrieve protocol to transfer data
        6. Retrieve port number used by protocol to transfer data
        7. Retreive interval to check server connectivity


"""

import sys
import pyfos.pyfos_auth as pyfos_auth
import pyfos.pyfos_util as pyfos_util
import pyfos.utils.brcd_util as brcd_util
from pyfos.pyfos_brocade_logging import supportftp
import pyfos.pyfos_version as version


def show_supportftp_params(session):
    filters = ["host", "user_name", "remote_directory",
               "auto_enabled", "protocol", "port",
               "connectivity_check_interval"]
    result = supportftp.get(session, None, filters)
    return result


def main(argv):

    filters = []
    inputs = brcd_util.parse(argv, supportftp, filters)

    session = brcd_util.getsession(inputs)
    if session['version'] < version.fosversion("9.0.0"):
        print("GET operation on supportftp parameters\
 are supported from FOS v9.0.0")
        pyfos_auth.logout(session)
        return
    result = show_supportftp_params(inputs['session'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
