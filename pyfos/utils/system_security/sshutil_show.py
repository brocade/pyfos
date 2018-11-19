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

:mod:`sshutil_show` - PyFOS util for displaying rekey interval and
allowed user name on a switch
***********************************************************************************
The :mod:`sshutil_show` provides option to display rekey interval and
allowed user name information

This module can be used to display key information. If user name is not
provided, then all SSH related information will be displayed.

* inputs:

|  Infrastructure options:

  |   -i,--ipaddr=IPADDR     IP address of FOS switch
  |   -L,--login=LOGIN       login name.
  |   -P,--password=PASSWORD password.
  |   -s,--secured=MODE      HTTPS mode "self" or "CA" [OPTIONAL].
  |   -v,--verbose           verbose mode[OPTIONAL].

|  Util scripts options:



* outputs:
    * SSH key related information

.. function:: sshutil_show.show_system_security_sshutil(session)

    * Display the SSH key information in the switch.

        Example usage of the method:

            ret = sshutil_show.show_system_security_sshutil(session)
            print (ret)

        Details::

            result = sshutil_show.show_system_security_sshutil(
              session)

        * inputs:
            :param session: session returned by login.
            :param user_name: user name for which public keys are associated

        * outputs:
            :rtype: dictionary of return status matching rest response

        *use cases*

        1. Retrieve the rekey interval information.
        2. Retrieve the allowed user name.


"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_security import sshutil
from pyfos.utils import brcd_util


def show_system_security_sshutil(session):
    sshutil_obj = sshutil()
    result = sshutil_obj.get(session)
    return result


def main(argv):
    # Print arguments
    # print(sys.argv[1:])

    filters = ['']
    inputs = brcd_util.parse(argv, sshutil, filters)

    session = brcd_util.getsession(inputs)

    result = show_system_security_sshutil(inputs['session'])

    pyfos_util.response_print(result)

    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
