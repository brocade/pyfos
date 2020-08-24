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


# lsan_zone_show.py(pyGen v1.0.0)


"""

:mod:`lsan_zone_show` - PyFOS util to show for lsan_zone
*******************************************************************************
The :mod:`lsan_zone_show` PyFOS util to show for lsan_zone


Displays the list of LSAN zone members in a particular zone.

lsan_zone_show : usage

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


.. function:: lsan_zone_show.show_lsan_zone(session, zone_name,\
members_member, edge_fabric_id)

    *Show lsan_zone*

        Example Usage of the Method::

            ret = lsan_zone_show.show_lsan_zone(session, zone_name,\
            members_member, edge_fabric_id)
            print (ret)

        Details::

            lsan_zoneObj = lsan_zone()
            lsan_zoneObj.set_zone_name(zone_name)
            lsan_zoneObj.set_members_member(members_member)
            lsan_zoneObj.set_edge_fabric_id(edge_fabric_id)
            print (ret)

        * Input::

            :param session: The session returned by the login.
            :param zone_name: The name of the zone
            :param members_member: The member of the zone
            :param edge_fabric_id: The ID of the fabric in which the LSAN zone\
              was created

        * Output:

            :rtype: None or more instance of class lsan_zone on Success  or a\
            dictionary with error.

"""


# Start utils imports
import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_fibrechannel_routing import lsan_zone

from pyfos.utils import brcd_util
# End module imports


def _show_lsan_zone(session, lsan_zoneObj):
    objlist = lsan_zone.get(session)
    lsan_zonelist = list()
    if isinstance(objlist, lsan_zone):
        objlist = [objlist]
    if isinstance(objlist, list):
        for i in range(len(objlist)):
            if lsan_zoneObj.peek_zone_name() is not None and\
               lsan_zoneObj.peek_zone_name() != objlist[i].peek_zone_name():
                continue
            if lsan_zoneObj.peek_members_member() != [] and\
               lsan_zoneObj.peek_members_member() !=\
               objlist[i].peek_members_member():
                continue
            if lsan_zoneObj.peek_edge_fabric_id() is not None and\
               lsan_zoneObj.peek_edge_fabric_id() !=\
               objlist[i].peek_edge_fabric_id():
                continue
            lsan_zonelist.append(objlist[i])
    else:
        print(objlist)
    return lsan_zonelist


def show_lsan_zone(session, zone_name=None, members_member=None,
                   edge_fabric_id=None):
    lsan_zoneObj = lsan_zone()
    lsan_zoneObj.set_zone_name(zone_name)
    lsan_zoneObj.set_members_member(members_member)
    lsan_zoneObj.set_edge_fabric_id(edge_fabric_id)
    return _show_lsan_zone(session, lsan_zoneObj)


def validate(lsan_zoneObj):
    if lsan_zoneObj.peek_zone_name() is None or\
       lsan_zoneObj.peek_members_member() == [] or\
       lsan_zoneObj.peek_edge_fabric_id() is None:
        return 0
    return 0


def main(argv):
    filters = []
    inputs = brcd_util.parse(argv, lsan_zone, filters, validate)
    session = brcd_util.getsession(inputs)
    result = _show_lsan_zone(session, inputs['utilobject'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
