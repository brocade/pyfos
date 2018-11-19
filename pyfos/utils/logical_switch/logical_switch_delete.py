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

:mod:`logical_switch_delete` - PyFOS util for deletion of Logical Switch.
******************************************************************************
The :mod:`logical_switch_delete` provides for deletion of Logical Switch.

This module is a standalone script and API that can be used to delete
an existing Logical switch. When ports/GE ports are provided, deletion of
specified ports is done in the logical switch with specified Fabric ID.

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

  |    --fabric-id=FABRIC-ID    Fabric ID of logical switch this \
                                action is targeting
  |    --ports=PORT-LIST        Port members of logical switch <\"3/4;3/5\">
  |    --geports=GE-PORT-LIST   GE port members of logical switch <\"3/4;3/5\">


* outputs:
    * Status of the logical switch delete operation

.. function:: logical_switch_delete.delete_logical_switch(session, \
                    fid, ports, geports)

    * Delete a logical switch or ports from a logical switch

        Example usage of the method::

            # Example 1: remove ports from logical-switch 1
            ret = logical_switch_delete.delete_logical_switch(session,
                    1, "0/4 0/5", None)
            print (ret)

            # Example 2: remove GE ports from logical-switch 3
            ret = logical_switch_delete.delete_logical_switch(session,
                    3, None, "0/1 0/2")
            print (ret)

            # Example 3: remove logical-switch 3
            ret = logical_switch_delete.delete_logical_switch(session,
                    3, None, None)
            print (ret)

        Details::


            ls_delete_obj = fibrechannel_logical_switch()
            ls_delete_obj.set_fabric_id(fid)
            if ports is not None:
                ls_delete_obj.set_port_member_list_port_member(ports)
            if geports is not None:
                ls_delete_obj.set_ge_port_member_list_port_member(geports)
            result = ls_delete_obj.delete(session)

        * inputs:
            :param session: session returned by login.
            :param fid: Fabric ID of logical switch.
            :param ports: Port members of the logical switch.
            :param geports: GE port members of the logical switch.

        * outputs:
            :rtype: dictionary of return status matching rest response

        *use cases*

        1. Delete port members from the logical-switch
        2. Delete GE port members from the logical-switch
        3. Delete the logical-switch

"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.utils import brcd_util
from pyfos.pyfos_brocade_fibrechannel_logical_switch \
    import fibrechannel_logical_switch


def _delete_logical_switch(session, restobject):
    return restobject.delete(session)


def delete_logical_switch(session, fid, ports, geports):
    ls_delete_obj = fibrechannel_logical_switch()
    ls_delete_obj.set_fabric_id(fid)
    if ports is not None:
        ls_delete_obj.set_port_member_list_port_member(ports)
    if geports is not None:
        ls_delete_obj.set_ge_port_member_list_port_member(geports)
    result = _delete_logical_switch(session, ls_delete_obj)
    return result


def validate(ls_obj):
    vfid = ls_obj.peek_fabric_id()
    if vfid is None:
        print("Missing fabric-id option in commandline:")
        return 1
    return 0


def main(argv):
    filters = ['fabric_id', 'port_member_list_port_member',
               'ge_port_member_list_port_member']
    inputs = brcd_util.parse(argv, fibrechannel_logical_switch, filters,
                             validate)

    ls_obj = inputs['utilobject']

    session = brcd_util.getsession(inputs)
    result = _delete_logical_switch(session, ls_obj)

    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
