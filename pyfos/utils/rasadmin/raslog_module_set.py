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

:mod:`raslog_module_set` - PyFOS util for configuring raslog_module op use case
*******************************************************************************
The :mod:`raslog_module_set` provides for configuring raslog_module op use case

This module is a standalone script that can be used to display raslog_module
attributes

* inputs:
    * -L=<login>: Login ID. If not provided, interactive
        prompt will request one.
    * -P=<password>: Password. If not provided, interactive
        prompt will request one.
    * -i=<IP address>: IP address
    * -f=<VFID>: VFID or -1 if VF is disabled. If unspecified,
        VFID of 128 is assumed.

* Util scripts options:
    * --module-id=MODULE-ID     Set FOS Module Id.
    * --enable=ENABLE-FLAG      Set Status flag of the FOS Module. <true|false>

* outputs:
    * raslog_module attributes in JSON format

.. function:: set_raslog_module(session, mod_id, mod_flag)

        Example usage of the method::

            ret = raslog_module_set.set_raslog_module(session,mod_id,mod_flag)
            print (ret)

        Details::

            value = {
                        "module-id": mod_id,
                        "log-enabled": mod_flag
                    }
            rmobj = raslog_module(value)
            result = _set_raslog_module (session, rmobj)
            return result

        * inputs:
            :param session: session returned by login.
            :param mod_id: FOS Module ID.
            :param mod_flag: Message Flag for all messages in the FOS Module.

        * outputs:
            :rtype: dictionary of return status matching rest response

        *use cases*
        1. Enables/Disables the raslog messages belonging to a FOS Module.

"""

import pyfos.pyfos_auth as pyfos_auth
from pyfos.pyfos_brocade_logging import raslog_module
import pyfos.pyfos_util as pyfos_util
import sys
import pyfos.utils.brcd_util as brcd_util


def set_raslog_module(session, mod_id, mod_flag):
    value = {
                "module-id": mod_id,
                "log-enabled": mod_flag
            }
    rmobj = raslog_module(value)

    result = _set_raslog_module(session, rmobj)
    return result


def _set_raslog_module(session, restobject):
    return restobject.patch(session)


def main(argv):

    filters = ['module_id', 'log_enabled']
    inputs = brcd_util.parse(argv, raslog_module, filters)

    session = brcd_util.getsession(inputs)

    result = _set_raslog_module(inputs['session'], inputs['utilobject'])

    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
