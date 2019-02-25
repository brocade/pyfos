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

:mod:`switch_configuration_show` - PyFOS util for configuring switch operation
********************************************************************************
The :mod:`switch_configuration_show` util provides for configuring switch \
operation.

This module is a stand-alone script that can be used to display switch
attributes.

* Input:
    * -L=<login>: The login ID. If not provided, an interactive
        prompt will request one.
    * -P=<password>: The password. If not provided, an interactive
        prompt will request one.
    * -i=<IP address>: The IP address.
    * -f=<VFID>: The VFID or -1 if VF is disabled. If unspecified,
        a VFID of 128 is assumed.

* Output:
    * The switch attributes in JSON format.

.. function:: show_switch_conf(session)

        Example Usage of the Method::

            ret = switch_configuration_show.show_switch_conf(session)
            print (ret)

        Details::

            switch_conf_obj = switch_configuration()
            result = switch_conf_obj.get(session)
            return result

        * Input:
            :param session: The session returned by login.

        * Output:
            :rtype: A dictionary of return status matching the REST response.

        *Use Cases*

        1. Retrieve the configuration parameters of the switch.

"""

import sys
from pyfos import pyfos_auth
import pyfos.pyfos_brocade_fibrechannel_configuration as py_fc
from pyfos import pyfos_util
from pyfos.utils import brcd_util

switch = py_fc.switch_configuration


def show_switch_conf(session):
    switch_conf_obj = switch()
    result = switch_conf_obj.get(session)
    return result


def main(argv):

    filters = []
    inputs = brcd_util.parse(argv, switch, filters)

    session = brcd_util.getsession(inputs)

    result = show_switch_conf(inputs['session'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
