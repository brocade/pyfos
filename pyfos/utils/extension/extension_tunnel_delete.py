#!/usr/bin/env python3

# Copyright © 2018 Broadcom. All Rights Reserved. The term “Broadcom” refers to
# Broadcom Inc. and/or its subsidiaries.
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

:mod:`extension_tunnel_delete` - PyFOS util for deleting a tunnel.
*******************************************************************************
The :mod:`extension_tunnel_delete` provides tunnel deletion functionality.

This module is a stand-alone script that can be used to delete an extension
tunnel.

extension_tunnel_delete.py: Usage

* Infrastructure options:
    * -i,--ipaddr=IPADDR: IP address of FOS switch.
    * -L,--login=LOGIN: Login name.
    * -P,--password=PASSWORD: Password.
    * -f,--vfid=VFID: VFID to which the request is directed.
    * -s,--secured=MODE: HTTPS mode "self" or "CA"[Optional].
    * -v,--verbose: Verbose mode[Optional].

* Util scripts options:
    * -n,--name=NAME: Set name.

* Outputs:
    * Python dictionary content with RESTCONF response data.

.. function:: extension_tunnel_delete.delete_extension_tunnel(session, name)

    *Delete extension tunnel*

        Example usage of the method::

            ret = extension_tunnel_delete.delete_extension_tunnel(session,
            name)
            print (ret)

        Details::

            tunnel = {
                            "name": name,
                       }
            result = extension_tunnel_delete._delete_extension_tunnel(session,
            tunnel)

        * Inputs:
            :param session: Session returned by login.
            :param name: VE port name expressed as slot/port.

        * Outputs:
            :rtype: Dictionary of return status matching rest response.

        *Use cases*

         Delete an extension tunnel.
"""


import pyfos.pyfos_auth as pyfos_auth
import pyfos.pyfos_util as pyfos_util
from pyfos.pyfos_brocade_extension_tunnel import extension_tunnel
import sys
import pyfos.utils.brcd_util as brcd_util

isHttps = "0"


def _delete_extension_tunnel(session, tnlobject):
    result = tnlobject.delete(session)
    return result


def delete_extension_tunnel(session, name):
    value_dict = {'name': name}
    tnlobject = extension_tunnel(value_dict)
    result = _delete_extension_tunnel(session, tnlobject)
    return result


def validate(tnlobject):
    if tnlobject.peek_name() is None:
            return 1
    return 0


def main(argv):
    # myinput = str("-i 10.17.3.70  -n 4/19 ")
    # argv = myinput.split()
    filters = ['name']
    inputs = brcd_util.parse(argv, extension_tunnel, filters, validate)
    tnlobject = inputs['utilobject']
    session = brcd_util.getsession(inputs)
    result = _delete_extension_tunnel(session, tnlobject)
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
