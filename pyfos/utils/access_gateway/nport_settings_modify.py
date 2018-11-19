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

:mod:`nport_settings_modify` - PyFOS util to configure the n-port settings.
***********************************************************************************
The :mod:`nport_settings_modify` provides option to configure the
n-port settings.

This module can be used to display the n-port settings information.

* inputs:

| Infrastructure options:

|   -i,--ipaddr=IPADDR     IP address of FOS switch.
|   -L,--login=LOGIN       login name.
|   -P,--password=PASSWORD password.
|   -f,--vfid=VFID         VFID to which the request is directed to [OPTIONAL].
|   -s,--secured=MODE      HTTPS mode "self" or "CA" [OPTIONAL].
|   -v,--verbose           verbose mode[OPTIONAL].

| Util scripts options:

|      --reliability-counter=VALUE          set "reliability-counter"

* outputs:
    * Status of the AG n-port setting change operation.

.. function:: nport_settings_modify.set_reliability_counter(session, relcount)

    * Set the N-port reliability counter value.

        Example usage of the method::

            ret = nport_settings_modify.set_reliability_counter(session,
                      relcount)
            print (ret)

        Details:

            settings_obj = n_port_settings()
            settings_obj.set_reliability_counter(relcount)
            return settings_obj.patch(session)

        * inputs:
            :param session: session returned by login.

        * outputs:
            :rtype: dictionary of return status matching rest response

        *use cases*

        1. Set the N-port reliability counter value.
"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.utils import brcd_util
from pyfos.pyfos_brocade_access_gateway import n_port_settings


def set_reliability_counter(session, relcount):
    settings_obj = n_port_settings()
    settings_obj.set_reliability_counter(relcount)
    # print(settings_obj)
    return settings_obj.patch(session)


def validate(settings_obj):
    if settings_obj.peek_reliability_counter() is None:
        return 1
    return 0


def main(argv):

    # Print arguments
    # print(sys.argv[1:])

    filters = ['reliability_counter']
    inputs = brcd_util.parse(argv, n_port_settings, filters, validate)

    settings_obj = inputs['utilobject']

    session = brcd_util.getsession(inputs)

    # pyfos_util.response_print(inputs['utilobject'].displaycustomcli())
    result = set_reliability_counter(inputs['session'],
                                     settings_obj.peek_reliability_counter())
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
