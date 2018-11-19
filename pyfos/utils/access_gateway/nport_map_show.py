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

:mod:`nport_map_show` - PyFOS util for displaying nport information.
***********************************************************************************
The :mod:`nport_map_show` provides option to display nport information.

This module can be used to display nport information.

* inputs:

|  Infrastructure options:

 |  -i,--ipaddr=IPADDR     IP address of FOS switch
 |  -L,--login=LOGIN       login name.
 |  -P,--password=PASSWORD password.
 |  -f,--vfid=VFID         VFID to which the request is directed to [OPTIONAL.
 |  -s,--secured=MODE      HTTPS mode "self" or "CA" [OPTIONAL].
 |  -v,--verbose           verbose mode[OPTIONAL].

|  Util scripts options

 |  --n-port=N-PORT                             N-port Name

* outputs:    * Status of the nport show operation
    * N-port map information. When N-port is not provided,
      all the existing N-port map information will be displayed.

.. function:: nport_map_show.show_access_gateway_nportmap(session)

        Example usage of the method:

            ret = nport_map_show.show_access_gateway_nportmap(session, n_port)
            print (ret)

        Details::

            result = nport_map_show.show_access_gateway_nportmap(
              session, \'0/45\'')

        * inputs:
            :param session: session returned by login.
            :param n_port: Specific N-port or None for all N-ports

        * outputs:
            :rtype: dictionary of return status matching rest response

        *use cases*

        1. Retrieve the AG N-port mappings information.
"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.utils import brcd_util
from pyfos.pyfos_brocade_access_gateway import n_port_map


def show_access_gateway_nportmap(session, n_port):
    nport_obj = n_port_map()
    if n_port is None:
        result = nport_obj.get(session, None)
    else:
        result = nport_obj.get(session, n_port)
    return result


def main(argv):
    # Print arguments
    # print(sys.argv[1:])

    filters = ['n_port']
    inputs = brcd_util.parse(argv, n_port_map, filters)

    nportmap_obj = inputs['utilobject']

    session = brcd_util.getsession(inputs)

    result = show_access_gateway_nportmap(
        inputs['session'], nportmap_obj.peek_n_port())

    pyfos_util.response_print(result)

    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
