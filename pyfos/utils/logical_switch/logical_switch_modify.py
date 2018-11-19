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

:mod:`logical_switch_modify` - PyFOS util to modify Logical switch attributes
********************************************************************************
The :mod:`logical_switch_modify` allows to modify Logical switch attributes.

This module is a standalone script and API that can be used to modify logical
switch attributes like enable or disable of base switch, FICON mode and
Logical ISL state. The port assignment of the logical switch can also be
modified using this script. Modifications will be done only on the logical
switch having the specified Fabric ID.

logical_switch_modify.py : Usage

* inputs:

| Infrastructure options:

  | -i,--ipaddr=IPADDR     IP address of FOS switch.
  | -L,--login=LOGIN       login name.
  | -P,--password=PASSWORD password.
  | -f,--vfid=VFID         VFID of LS context to which the request \
                           is directed to [OPTIONAL].
  | -s,--secured=MODE      HTTPS mode "self" or "CA" [OPTIONAL].
  | -v,--verbose           verbose mode[OPTIONAL].

| Util scripts options:

  | --fabric-id=FABRIC-ID     Fabric ID of logical switch this \
                              action is targeting
  | --base=BS-MODE            Base switch mode <0|1>
  | --ficon=FICON-MODE        FICON mode <0|1>
  | --lislenable=LISL-ENABLE  LISL enable <0|1>
  | --ports=PORT-LIST         Port members of logical switch <\"3/4;3/5\">
  | --geports=GE-PORT-LIST    GE port members of logical switch <\"3/4;3/5\">

* outputs:

    * Status of the logical-switch set operation

.. function:: logical_switch_modify.modify_logical_switch(session, fid, \
base, ficon, lislenable, ports, geports)

    *Modify logical-switch attributes*

        Example usage of the method::

            ret = logical_switch_modify.modify_logical_switch(session,
                fid, base, ficon, lislenable, ports, geports)
            print (ret)

        Details::


            ls_dict = {
                "fabric-id": fid,
                "base-switch-enabled": base,
                "ficon-mode-enabled": ficon,
                "logical-isl-enabled": lislenable,
                "port-member-list-port-member" : ports,
                "ge-port-member-list-port-member" : geports,
            }
            ls_obj = fibrechannel_logical_switch()
            ls_obj.load(ls_dict, 1)
            result = ls_obj.patch(session)

        * inputs:
            :param session: session returned by login
            :param fid: Fabric ID of logical switch.
            :param base: Base switch mode.
            :param ficon: FICON mode.
            :param lislenable: Logical ISL enabled.
            :param ports: Port members assigned to the logical switch.
            :param geports: GE port members assigned to the logical switch.

        * outputs:
            :rtype: dictionary of return status matching rest response

        *use cases*

        1. Set a logical switch in FICON mode
        2. Enable/disable base switch
        3. Enable logical ISLs
        4. Modify existing port member list
        5. Modify existing GE port member list

"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.utils import brcd_util
from pyfos.pyfos_brocade_fibrechannel_logical_switch \
    import fibrechannel_logical_switch


def _modify_logical_switch(session, ls_object):
    return ls_object.patch(session)


def modify_logical_switch(session, fid, base, ficon, lislenable,
                          ports, geports):
    value_dict = {'fabric_id': fid,
                  'base_switch_enabled': base,
                  'ficon_mode_enabled': ficon,
                  'logical_isl_enabled': lislenable,
                  'port_member_list_port_member': ports,
                  'ge_port_member_list_port_member': geports}
    ls_modify_obj = fibrechannel_logical_switch()
    ls_modify_obj.load(value_dict, 1)
    result = _modify_logical_switch(session, ls_modify_obj)
    return result


def validate(ls_obj):
    vfid = ls_obj.peek_fabric_id()
    if vfid is None:
        print("Missing fabric-id option in commandline:")
        return 1
    lisl = ls_obj.peek_logical_isl_enabled()
    if (lisl is not None and lisl != 0 and lisl != 1):
        print("Invalid input for logical_isl_enabled option in commandline:")
        return 1
    return 0


def main(argv):
    filters = ['fabric_id', 'base_switch_enabled', 'ficon_mode_enabled',
               'logical_isl_enabled', 'port_member_list_port_member',
               'ge_port_member_list_port_member']
    inputs = brcd_util.parse(argv, fibrechannel_logical_switch, filters,
                             validate)

    ls_obj = inputs['utilobject']

    session = brcd_util.getsession(inputs)
    result = _modify_logical_switch(session, ls_obj)

    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
