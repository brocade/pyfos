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

:mod:`device_list_show` - PyFOS util to show the logged in device information.
*******************************************************************************
The :mod:`device_list_show` provides option to display the
logged in device information.

This module can be used to display the logged in device information
including the FCID, current n-port and F-port through which the device
is logged in.

* inputs:

| Infrastructure options:

|   -i,--ipaddr=IPADDR     IP address of FOS switch.
|   -L,--login=LOGIN       login name.
|   -P,--password=PASSWORD password.
|   -f,--vfid=VFID         VFID to which the request is directed to [OPTIONAL].
|   -s,--secured=MODE      HTTPS mode "self" or "CA" [OPTIONAL].
|   -v,--verbose           verbose mode[OPTIONAL].

  Util scripts options:

|      --wwn=VALUE      set "wwn"

* outputs:
    * Device wwn, FCID, F-port and current n-port mapping details.

.. function:: device_list_show.show_device_list(session, wwn)

    * Display the logged in device information on AG and their details.

        Example usage of the method:

            ret = device_list_show.show_device_list(session, wwn)
            print (ret)

        Details::

           device_list_obj = device_list()
           if wwn is None:
               result = device_list_obj.get(session, None)
           else:
               result = device_list_obj.get(session, wwn)

        * inputs:
            :param session: session returned by login.
            :param wwn: Specific wwn name or None for all wwn's

        * outputs:
            :rtype: dictionary of return status matching rest response

        *use cases*

        1. Retrieve the login details of the devices on Access gateway.
"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_access_gateway import device_list
from pyfos.utils import brcd_util


def show_device_list(session, wwn):
    device_list_obj = device_list()
    if wwn is None:
        result = device_list_obj.get(session, None)
    else:
        result = device_list_obj.get(session, wwn)
    return result


def main(argv):

    # Print arguments
    # print(sys.argv[1:])

    filters = ['wwn']
    inputs = brcd_util.parse(argv, device_list, filters)

    device_obj = inputs['utilobject']

    session = brcd_util.getsession(inputs)

    # pyfos_util.response_print(inputs['utilobject'].displaycustomcli())
    result = show_device_list(inputs['session'], device_obj.peek_wwn())
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
