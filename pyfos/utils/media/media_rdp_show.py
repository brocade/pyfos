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

:mod:`media_show` - PyFOS util to display port media information
********************************************************************************
The :mod:`media_show` displays local port and peer port media information.
peer port media information is supported for F-Port alone.

This module is a standalone script that can be used to display port media
information with specified interface/slot/port id ass input. If no
is given, all ports media information will be displayed.

* inputs:

| Infrastructure options:

  | -i,--ipaddr=IPADDR     IP address of FOS switch.
  | -L,--login=LOGIN       login name.
  | -P,--password=PASSWORD password.
  | -f,--vfid=VFID         VFID to which the request is directed to [OPTIONAL].
  | -s,--secured=MODE      HTTPS mode "self" or "CA" [OPTIONAL].
  | -v,--verbose           verbose mode[OPTIONAL].

|  Util scripts options:

  |    --name=Interface/slot/port                           port name


* outputs:
    * Media information of specified port. When port is not provided,
      all existing ports media information will be displayed.

.. function:: media_rdp_show.show_media_rdp(session, name)

    * Display the port media information.

        Example usage of the method::

            # Example 1: Display all the ports media information
            ret = media_rdp_show.show_media_rdp(session, None)
            print (ret)

            # Example 2: Display a specific port media information
            ret = media_rdp_show.show_media_rdp(session, \'FC/0/2\')
            print (ret)

        Details::

            media_object = media_rdp()
            if slot_port is None: #All ports media
                result = media_object.get(session, None)
            else:
                result = media_object.get(session, name)

        * inputs:
            :param session: session returned by login.
            :param name: Specific port in the format of interface/slot/port
                         or None for all ports. Interface should be either
                         FC or GE or TE

        * outputs:
            :rtype: dictionary of return status matching rest response

        *use cases*

        1. Retrieve the port media information.

"""

import sys
import pyfos.pyfos_auth as pyfos_auth
import pyfos.pyfos_util as pyfos_util
import pyfos.utils.brcd_util as brcd_util
from pyfos.pyfos_brocade_media import media_rdp


def show_media_rdp(session, name):
    media_object = media_rdp()
    if name is None:
        result = media_object.get(session, None)
    else:
        result = media_object.get(session, name)
    return result


def main(argv):
    filters = ['name']
    inputs = brcd_util.parse(argv, media_rdp, filters)
    media_obj = inputs['utilobject']
    session = brcd_util.getsession(inputs)
    result = show_media_rdp(inputs['session'], media_obj.peek_name())
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
