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


# fabric_topology_domais.py(pyGen v1.0.0)


"""

:mod:`fabric_topology_domain` - PyFOS util for topology_domain
*******************************************************************************
The :mod:`fabric_topology_domain` PyFOS util for topology_domain


Topology data for one of the fabric domains, including the Shortest Path First\
(SPF) path cost (metric), the total number of potential paths that qualify\
based on the SPF calculations, and a list of the egress (out-ports) that are\
in use for routing traffic to the domain.

fabric_topology_domain: usage

* Infrastructure Options:
    * -i,--ipaddr=IPADDR: The IP address of the FOS switch.
    * -L,--login=LOGIN: The login name.
    * -P,--password=PASSWORD: The password.
    * -f,--vfid=VFID: The VFID to which the request is directed.
    * -s,--secured=MODE: The HTTPS mode "self" or "CA" [Optional].
    * -v,--verbose: Verbose mode [Optional].

* Util Script Options:
    * --domain-id=DOMAIN-ID: The domain ID for which to get the topology data \
      for.
* Output:
    * Python dictionary content with RESTCONF response data.


.. function:: fabric_topology_domain.show_topology_domain(session, domain_id)

    *Show topology_domain*

    Example Usage of the Method::

        ret = fabric_topology_domain.show_topology_domain(session, domain_id)
        print (ret)

    Details::

        topology_domainObj = topology_domain()
        topology_domainObj.set_domain_id(domain_id)
        print (ret)

    :param session: The session returned by the login.
    :param domain_id: The domain ID for which to get the topology data for.

    :rtype: None or more instance of class topology_domain on Success or a \
    dictionary with error.

"""


# Start utils imports
import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_fibrechannel_switch import topology_domain

from pyfos.utils import brcd_util
# End module imports


def _show_topology_domain(session, topology_domainObj):
    objlist = topology_domain.get(session)
    topology_domainlist = list()
    if isinstance(objlist, topology_domain):
        objlist = [objlist]
    if isinstance(objlist, list):
        for i in range(len(objlist)):
            if topology_domainObj.peek_domain_id() is not None and\
               topology_domainObj.peek_domain_id() !=\
               objlist[i].peek_domain_id():
                continue
            topology_domainlist.append(objlist[i])
    else:
        print(objlist)
    return topology_domainlist


def show_topology_domain(session, domain_id=None):
    topology_domainObj = topology_domain()
    topology_domainObj.set_domain_id(domain_id)
    return _show_topology_domain(session, topology_domainObj)


def validate(topology_domainObj):
    if topology_domainObj.peek_domain_id() is None:
        return 0
    return 0


def main(argv):
    filters = ["domain_id"]
    inputs = brcd_util.parse(argv, topology_domain, filters, validate)
    session = brcd_util.getsession(inputs)
    result = _show_topology_domain(session, inputs['utilobject'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
