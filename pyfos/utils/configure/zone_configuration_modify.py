#!/usr/bin/env python3

# Copyright 2019 Brocade Communications Systems LLC.  All rights reserved.
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

:mod:`zone_configuration_modify` - PyFOS util for modifying zone settings.
************************************************************************************************
The :mod:`zone_configuration_modify` utility is a standalone script that
provides a way for the user to modify certain zone settings.

* Input:
    * -L=<login>: The login ID. If not provided, an interactive
        prompt will request one.
    * -P=<password>: The password. If not provided, an interactive
        prompt will request one.
    * -i=<IP address>: The IP address.
    * -f=<VFID>: The VFID or -1 if VF is disabled. If unspecified,
        a VFID of 128 is assumed.

* Utility Script Options:

    * --node-name-zoning-enabled=NODE-NAME-ZONING-MODE   Enables or disables
                                                         zoning node-name
                                                         checking.
    * --timeout=ZONE-FABRIC-LOCK-TIMEOUT                 Sets the zoning fabric
                                                         lock timeout value
                                                         (valid range: 5-30 \
                                                         minutes)

* Output:
    * The HTTP status in JSON format.

.. function:: patch_zone_conf(session, node_name_checking, fab_lock_timeout)

        Example Usage of the Method::

            ret = zone_configuration_modify.patch_zone_conf (session,
                    node_name_checking, fab_lock_timeout)
            print (ret)

        Details::

            val = {
                "node_name_zoning_enabled": node_name_checking,
                "fabric-lock-timeout": fab_lock_timeout
                }
            obj = zone_configuration(val)
            result = _patch_zone_conf(session, obj)
            return result

        * Input:
            :param session: The session returned by login.
            :param node_name_checking: Enables or disables zoning node name
                                       checking.
            :param fab_lock_timeout: Sets the zoning fabric lock timeout value
                                     in minutes (valid range: 5-30)

        * Output:
            :rtype: A dictionary of return status matching the REST response.

        *Use Cases*

        1. Patch certain zoning attributes on the switch.

"""

import sys
from pyfos import pyfos_auth
import pyfos.pyfos_brocade_fibrechannel_configuration as py_fc
from pyfos import pyfos_util
from pyfos.utils import brcd_util

zonecfg = py_fc.zone_configuration


def validate(obj):
    flag = 0
    if obj.peek_node_name_zoning_enabled() is not None:
        flag = flag + 1
    if obj.peek_fabric_lock_timeout() is not None:
        flag = flag + 1

    return 0 if flag >= 1 else 1


def patch_zone_conf(session, node_name_checking, fab_lock_timeout):
    val = {
        "node-name-zoning-enabled": node_name_checking,
        "fabric-lock-timeout": fab_lock_timeout
        }
    obj = zonecfg(val)
    result = _patch_zone_conf(session, obj)
    return result


def _patch_zone_conf(session, restobject):
    return restobject.patch(session)


def main(argv):

    filters = ['node_name_zoning_enabled', 'fabric_lock_timeout']
    inputs = brcd_util.parse(argv, zonecfg, filters, validate)
    session = brcd_util.getsession(inputs)

    result = _patch_zone_conf(inputs['session'], inputs['utilobject'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
