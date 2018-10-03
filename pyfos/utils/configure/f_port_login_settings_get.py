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

:mod:`f_port_login_settings_get` - PyFOS util for getting configured login
**************************************************************************
The :mod:`f_port_login_settings_get` provides for getting configured login

This module is a standalone script that can be used to display login
attributes

* inputs:
    * -L=<login>: Login ID. If not provided, interactive
        prompt will request one.
    * -P=<password>: Password. If not provided, interactive
        prompt will request one.
    * -i=<IP address>: IP address
    * -f=<VFID>: VFID or -1 if VF is disabled. If unspecified,
        VFID of 128 is assumed.

* outputs:
    * login attributes in JSON format

.. function:: show_login_conf(session)

        Example usage of the method::

            ret = f_port_login_settings_get.show_login_conf(session)
            print (ret)

        Details::

            switch_conf_obj = f_port_login_settings()
            result = switch_conf_obj.get(session)
            return result

        * inputs:
            :param session: session returned by login.

        * outputs:
            :rtype: dictionary of return status matching rest response

        *use cases*

        1. Retrieve the f-port login parameters of switch.


"""

import pyfos.pyfos_auth as pyfos_auth
import pyfos.pyfos_brocade_fibrechannel_configuration as py_fc
import pyfos.pyfos_util as pyfos_util
import sys
import pyfos.utils.brcd_util as brcd_util

login = py_fc.f_port_login_settings


def show_login_conf(session):
    login_conf_obj = login()
    result = login_conf_obj.get(session)
    return result


def main(argv):

    filters = []
    inputs = brcd_util.parse(argv, login, filters)

    session = brcd_util.getsession(inputs)

    result = show_login_conf(inputs['session'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
