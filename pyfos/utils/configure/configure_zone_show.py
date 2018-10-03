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

:mod:`configure_zone_show` - PyFos util to get and display zone configuration.
***********************************************************************************
The :mod:`configure_zone_show` displays zone configuration.

This module is a standalone script that can be used to display zone
attributes

* Infrastructure options:
    * -i,--ipaddr=IPADDR: IP address of FOS switch.
    * -L,--login=LOGIN: login name.
    * -P,--password=PASSWORD: password.
    * -f,--vfid=VFID: VFID to which the request is directed to.
    * -s,--secured=MODE: HTTPS mode "self" or "CA"[OPTIONAL].
    * -v,--verbose: verbose mode[OPTIONAL].

* outputs:
    * Python dictionary content with RESTCONF response data

..function:: get_zone_configuration(session)

    Example usage of the method::

        ret = configure_zone_show.get_zone_configuration(session)
        print (ret)

    Details::

        result = configure_zone_show.get_zone_configuration(session)

    * inputs:
        :param session: session returned by login

    * outputs:
        :rtype: dictionary of return status matching rest response

    *use cases*

    1. Retrieve the zone configuration parameters of the switch

"""

import pyfos.pyfos_auth as pyfos_auth
import pyfos.pyfos_util as pyfos_util
import sys
import pyfos.utils.brcd_util as brcd_util
from pyfos.pyfos_brocade_fibrechannel_configuration import zone_configuration


def get_zone_configuration(session):
    zone_configuration_obj = zone_configuration()
    result = zone_configuration_obj.get(session)
    return result


def main(argv):

    filters = []
    inputs = brcd_util.parse(argv, zone_configuration, filters)

    session = brcd_util.getsession(inputs)

    result = get_zone_configuration(inputs['session'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
