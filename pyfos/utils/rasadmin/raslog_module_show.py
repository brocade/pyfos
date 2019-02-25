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

:mod:`raslog_module_show` - PyFOS util for configuring raslog_module op use case
********************************************************************************
The :mod:`raslog_module_show` provides for configuring raslog_module op use case

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
    * --module-id <module_id>, Optional module id for the raslog to retrieve

* outputs:
    * raslog_module attributes in JSON format


.. function:: show_raslog_module(session)

        Example usage of the method::

            ret = raslog_module_show.show_raslog_module(session, module_id)
            print (ret)

        Details::

            result = raslog_module_show.show_raslog_module(
              session, 'AUTH')

        * inputs:
            :param session: session returned by login.
            :param module_id: Optional Specific FOS Module Id

        * outputs:
            :rtype: dictionary of return status matching rest response

        *use cases*

        1. Retrieve the FOS Module information.

"""

import sys
from pyfos import pyfos_auth
from pyfos.pyfos_brocade_logging import raslog_module
from pyfos import pyfos_util
from pyfos.utils import brcd_util


def show_raslog_module(session, mod_id):
    raslog_module_obj = raslog_module()
    if mod_id is None:
        return raslog_module_obj.get(session)
    else:
        return raslog_module_obj.get(session, mod_id)


def main(argv):

    filters = ['module_id']
    inputs = brcd_util.parse(argv, raslog_module, filters)

    session = brcd_util.getsession(inputs)

    module = inputs['utilobject'].peek_module_id()
    result = show_raslog_module(inputs['session'], module)

    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
