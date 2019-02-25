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

:mod:`media_show` - PyFOS util to display port media information.
********************************************************************************
The :mod:`media_show` util displays local port and peer port media information.
Peer port media information is supported only for F_Ports.

This module is a stand-alone script that can be used to display port media
information with a specified interface/slot/port ID. If no specified port
is given, media information will be displayed for all ports.

* Input:

| Infrastructure Options:

  | -i,--ipaddr=IPADDR     The IP address of the FOS switch.
  | -L,--login=LOGIN       The login name.
  | -P,--password=PASSWORD The password.
  | -f,--vfid=VFID         The VFID to which the request\
                            is directed [OPTIONAL].
  | -s,--secured=MODE      The HTTPS mode "self" or "CA" [OPTIONAL].
  | -v,--verbose           Verbose mode [OPTIONAL].

|  Util Script Options:

  |    --name=Interface/slot/port                  Sets the port name.


* Output:
    * Media information about specified port. When the port is not provided,
      media information will be displayed for all existing ports.

.. function:: media_rdp_show.show_media_rdp(session, name)

    * Display the port media information.

        Example Usage of the Method::

            # Example 1: Display media information for all ports.
            ret = media_rdp_show.show_media_rdp(session, None)
            print (ret)

            # Example 2: Display media information for a specific port.
            ret = media_rdp_show.show_media_rdp(session, \'FC/0/2\')
            print (ret)

        Details::

            media_object = media_rdp()
            if slot_port is None: #All ports media
                result = media_object.get(session, None)
            else:
                result = media_object.get(session, name)

        * Input:
            :param session: The session returned by the login.
            :param name: The specific port in the format of interface/slot/port
                         or none for all ports. Interface should be
                         FC, GE, or TE.

        * Output:
            :rtype: A dictionary of return status matching the REST response.

        *Use Cases*

        1. Retrieve the port media information.

"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.utils import brcd_util
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
