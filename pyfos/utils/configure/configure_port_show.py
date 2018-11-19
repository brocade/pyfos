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

:mod:`configure_port_show` - PyFOS util to get and display the port\
 configuration.
***********************************************************************************
The :mod:`configure_port_show` util displays the port configuration.

This module is a stand-alone script that can be used to display port
attributes.

* Infrastructure Options:
    * -i,--ipaddr=IPADDR: The IP address of the FOS switch.
    * -L,--login=LOGIN: The login name.
    * -P,--password=PASSWORD: The password.
    * -f,--vfid=VFID: The VFID to which the request is directed.
    * -s,--secured=MODE: The HTTPS mode "self" or "CA" [OPTIONAL].
    * -v,--verbose: Verbose mode [OPTIONAL].

* Output:
    * Python dictionary content with RESTCONF response data.

..function:: get_port_configuration(session)

    Example Usage of the Method::

        ret = configure_port_show.get_port_configuration(session)
        print (ret)

    Details::

        result = configure_port_show.get_port_configuration(session)

    * Input:
        :param session: The session returned by login.

    * Output:
        :rtype: A dictionary of return status matching the REST response.

    *Use Cases*

    1. Retrieve the port configuration parameters of the switch.

"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.utils import brcd_util
from pyfos.pyfos_brocade_fibrechannel_configuration import port_configuration


def get_port_configuration(session):
    port_configuration_obj = port_configuration()
    result = port_configuration_obj.get(session)
    return result


def main(argv):

    filters = []
    inputs = brcd_util.parse(argv, port_configuration, filters)

    session = brcd_util.getsession(inputs)

    result = get_port_configuration(inputs['session'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
