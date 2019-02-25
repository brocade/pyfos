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

:mod:`raslog_module_set` - PyFOS util for configuring the RASLog module.
*******************************************************************************
The :mod:`raslog_module_set` util provides for configuring the RASLog module.

This module is a stand-alone script that can be used to display RASLog module
attributes.

* Input:
    * -L=<login>: The login ID. If not provided, an interactive
        prompt will request one.
    * -P=<password>: The password. If not provided, an interactive
        prompt will request one.
    * -i=<IP address>: The IP address.
    * -f=<VFID>: The VFID or -1 if VF is disabled. If unspecified,
        a VFID of 128 is assumed.

* Util Script Options:
    * --module-id=MODULE-ID     Sets the FOS module ID.
    * --enable=ENABLE-FLAG      Sets the status flag of the\
                                 FOS module <true|false>.

* Output:
    * RASLog attributes in JSON format.

.. function:: set_raslog_module(session, mod_id, mod_flag)

        Example Usage of the Method::

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

        * Input:
            :param session: The session returned by the login.
            :param mod_id: The FOS module ID.
            :param mod_flag: The message flag for all messages in the\
                              FOS module.

        * Output:
            :rtype: A dictionary of return status matching the REST response.

        *Use Cases*

        1. Enable or disable the RASLog messages belonging to a FOS module.

"""

import sys
from pyfos import pyfos_auth
from pyfos.pyfos_brocade_logging import raslog_module
from pyfos import pyfos_util
from pyfos.utils import brcd_util


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
