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

:mod:`nport_settings_show` - PyFOS util to display the n-port settings.
***********************************************************************************
The :mod:`nport_settings_show` provides option to display n-port settings.

This module can be used to display the AG n-port settings.

* inputs:

| Infrastructure options:

|   -i,--ipaddr=IPADDR     IP address of FOS switch.
|   -L,--login=LOGIN       login name.
|   -P,--password=PASSWORD password.
|   -f,--vfid=VFID         VFID to which the request is directed to [OPTIONAL].
|   -s,--secured=MODE      HTTPS mode "self" or "CA" [OPTIONAL].
|   -v,--verbose           verbose mode[OPTIONAL].

* outputs:
    * N-port properties and their current state.

.. function:: nport_settings_show.show_settings(session)

    * Display the N-port settings like the reliability counter.

        Example usage of the method::

            ret = nport_settings_show.show_settings(session)
            print (ret)

        Details::

            nportsettings_obj = n_port_settings()
            result = nportsettings_obj.get(session)

        * inputs:
            :param session: session returned by login.

        * outputs:
            :rtype: dictionary of return status matching rest response

        *use cases*

        1. Retrieve the AG N-port reliability counter value.
"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.utils import brcd_util
from pyfos.pyfos_brocade_access_gateway import n_port_settings


def show_settings(session):
    nportsettings_obj = n_port_settings()
    return nportsettings_obj.get(session)


def main(argv):

    # Print arguments
    # print(sys.argv[1:])

    filters = []
    inputs = brcd_util.parse(argv, n_port_settings, filters)

    session = brcd_util.getsession(inputs)

    # pyfos_util.response_print(inputs['utilobject'].displaycustomcli())
    result = show_settings(inputs['session'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
