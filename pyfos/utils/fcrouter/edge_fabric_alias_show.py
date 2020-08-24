#!/usr/bin/env python3


# Copyright © 2019-2020 Broadcom. All rights reserved.
# The term “Broadcom” refers to Broadcom Inc. and/or its subsidiaries.
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


# edge_fabric_alias_show.py(pyGen v1.0.0)


"""

:mod:`edge_fabric_alias_show` - PyFOS util to show edge fabric alias
*******************************************************************************
The :mod:`edge_fabric_alias_show` PyFOS util to show edge fabric alias


Displays edge fabric id's corresponding alias name

edge_fabric_alias_show : usage

* Infrastructure Options:
    * -i,--ipaddr=IPADDR: The IP address of the FOS switch.
    * -L,--login=LOGIN: The login name.
    * -P,--password=PASSWORD: The password.
    * -f,--vfid=VFID: The VFID to which the request is directed.
    * -s,--secured=MODE: The HTTPS mode "self" or "CA" [Optional].
    * -v,--verbose: Verbose mode [Optional].

* Util Script Options:

* Output:
    * Python dictionary content with RESTCONF response data.


.. function:: edge_fabric_alias_show.show_edge_fabric_alias(session,\
alias_name, edge_fabric_id)

    *Show edge_fabric_alias*

        Example Usage of the Method::

            ret = edge_fabric_alias_show.show_edge_fabric_alias(session,\
            alias_name, edge_fabric_id)
            print (ret)

        Details::

            edge_fabric_aliasObj = edge_fabric_alias()
            edge_fabric_aliasObj.set_alias_name(alias_name)
            edge_fabric_aliasObj.set_edge_fabric_id(edge_fabric_id)
            print (ret)

        * Input::

            :param session: The session returned by the login.
            :param alias_name: Alias name of the specific edge fabric id.
            :param edge_fabric_id: The ID of the fabric in which the LSAN zone\
              was created

        * Output:

            :rtype: None or more instance of class edge_fabric_alias on\
            Success  or a dictionary with error.

"""


# Start utils imports
import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_fibrechannel_routing import edge_fabric_alias

from pyfos.utils import brcd_util
# End module imports


def _show_edge_fabric_alias(session, edge_fabric_aliasObj):
    objlist = edge_fabric_alias.get(session)
    edge_fabric_aliaslist = list()
    if isinstance(objlist, edge_fabric_alias):
        objlist = [objlist]
    if isinstance(objlist, list):
        for i in range(len(objlist)):
            if edge_fabric_aliasObj.peek_alias_name() is not None and\
               edge_fabric_aliasObj.peek_alias_name() !=\
               objlist[i].peek_alias_name():
                continue
            if edge_fabric_aliasObj.peek_edge_fabric_id() is not None and\
               edge_fabric_aliasObj.peek_edge_fabric_id() !=\
               objlist[i].peek_edge_fabric_id():
                continue
            edge_fabric_aliaslist.append(objlist[i])
    else:
        print(objlist)
    return edge_fabric_aliaslist


def show_edge_fabric_alias(session, alias_name=None, edge_fabric_id=None):
    edge_fabric_aliasObj = edge_fabric_alias()
    edge_fabric_aliasObj.set_alias_name(alias_name)
    edge_fabric_aliasObj.set_edge_fabric_id(edge_fabric_id)
    return _show_edge_fabric_alias(session, edge_fabric_aliasObj)


def validate(edge_fabric_aliasObj):
    if edge_fabric_aliasObj.peek_alias_name() is None or\
       edge_fabric_aliasObj.peek_edge_fabric_id() is None:
        return 0
    return 0


def main(argv):
    filters = []
    inputs = brcd_util.parse(argv, edge_fabric_alias, filters, validate)
    session = brcd_util.getsession(inputs)
    result = _show_edge_fabric_alias(session, inputs['utilobject'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
