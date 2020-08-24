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
# limitations under the License

"""

:mod:`access_gateway_show` - PyFOS util for displaying connected \
access gateway information.
********************************************************************************\
********************************************************************************
The :mod:`access_gateway_show` provides option to display connected access\
gateway information.

This module can be used to display connected access gateway \
information in the Native mode

* inputs:

|  Infrastructure options:

 |  -i,--ipaddr=IPADDR     IP address of FOS switch
 |  -L,--login=LOGIN       login name.
 |  -P,--password=PASSWORD password.
 |  -f,--vfid=VFID         VFID to which the request is directed to [OPTIONAL].
 |  -s,--secured=MODE      HTTPS mode "self" or "CA" [OPTIONAL].
 |  -v,--verbose           verbose mode[OPTIONAL].

|  Util scripts options

 |  --wwn=WWN				switch wwn

* outputs:

      * Status of the AG show operation

.. function:: access_gateway_show.show_access_gateway(session)

         Example usage of the method:

            ret = access_gateway_show.show_access_gateway(session, wwn)
            print (ret)

        Details::

            result = access_gateway_show.show_access_gateway\
            (session, '10:00:00:05:33:e6:ce:80')

        * inputs:
            :param session: session returned by login.
            :param wwn: Specific AG wwn or None for all AG wwn

        * outputs:
            :rtype: dictionary of return status matching rest response

        *use cases*

        1. Retrieve the Connected AG information in the Native mode.
"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.utils import brcd_util
from pyfos.pyfos_brocade_fabric import access_gateway


def show_access_gateway(session, wwn):
    access_gateway_obj = access_gateway()
    if wwn is None:
        result = access_gateway_obj.get(session, None)
    else:
        result = access_gateway_obj.get(session, wwn)
    return result


def main(argv):
    # Print arguments
    # print(sys.argv[1:])

    filters = ['switch_wwn']
    inputs = brcd_util.parse(argv, access_gateway, filters)

    accessgateway_obj = inputs['utilobject']

    session = brcd_util.getsession(inputs)

    result = show_access_gateway(
        inputs['session'], accessgateway_obj.peek_switch_wwn())
    pyfos_util.response_print(result)

    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
