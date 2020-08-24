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


# fabric_topology_route.py(pyGen v1.0.0)


"""

:mod:`fabric_topology_route` - PyFOS util for retieving the topology_route data
*******************************************************************************
The :mod:`fabric_topology_route` PyFOS util for retieving the topology_route \
data

A route currently programmed by the local switch. Each includes one egress \
(out-ports), any ingress (in-ports), and the number of hops to reach the \
domain, by the switch.

fabric_topology_route : usage

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


.. function:: fabric_topology_route.show_topology_route(session)

    *Show topology_route*

    Example Usage of the Method::

        ret = fabric_topology_route.show_topology_route(session)
        print (ret)

    Details::

        topology_routeObj = topology_route()
        print (ret)

    :param session: The session returned by the login.
    :rtype: None or more instance of class topology_route on Success or a \
     dictionary with error.

"""


# Start utils imports
import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_fibrechannel_switch import topology_route

from pyfos.utils import brcd_util
# End module imports


def _show_topology_route(session, topology_routeObj):
    objlist = topology_route.get(session)
    topology_routelist = list()
    if isinstance(objlist, topology_route):
        objlist = [objlist]
    if isinstance(objlist, list):
        for i in range(len(objlist)):
            topology_routelist.append(objlist[i])
    else:
        print(objlist)
    return topology_routelist


def show_topology_route(session):
    topology_routeObj = topology_route()
    return _show_topology_route(session, topology_routeObj)


def validate(topology_routeObj):
    return 0


def main(argv):
    filters = []
    inputs = brcd_util.parse(argv, topology_route, filters, validate)
    session = brcd_util.getsession(inputs)
    result = _show_topology_route(session, inputs['utilobject'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
