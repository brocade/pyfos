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

:mod:`configure_fabric_show` - PyFOS util for fetching the fabric \
configuration.
*************************************************************************************
The :mod:`configure_fabric_show` util displays the fabric configuration.

This module is a stand-alone script that can be used to display fabric
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
    * Python dictionary content with RESTCONF response data.

.. function:: show_fabric_configuration(session)

        Example Usage of the Method::

            ret = configure_fabric_show.show_fabric_configuration(session)
            print (ret)

        Details::

            fabric_conf_obj = fabric_configuration()
            result = fabric_conf_obj.get(session)
            return result

        * Input:
            :param session: The session returned by login.

        * Output:
            :rtype: A dictionary of return status matching the REST response.

        *Use Cases*

        1. Retrieve the configuration parameters of the fabric.

"""

import sys
from pyfos import pyfos_auth
from pyfos.pyfos_brocade_fibrechannel_configuration import fabric
from pyfos import pyfos_util
from pyfos.utils import brcd_util


def show_fabric_configuration(session):
    fabric_conf_Obj = fabric()
    result = fabric_conf_Obj.get(session)
    return result


def validate(fabric_conf_Obj):
    if fabric_conf_Obj.peek_insistent_domain_id_enabled() is None or\
       fabric_conf_Obj.peek_principal_selection_enabled() is None or\
       fabric_conf_Obj.peek_principal_priority() is None:
        return 0
    return 0


def main(argv):

    filters = []
    inputs = brcd_util.parse(argv, fabric, filters, validate)

    session = brcd_util.getsession(inputs)

    result = show_fabric_configuration(inputs['session'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
