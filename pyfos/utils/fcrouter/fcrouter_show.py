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


# fcrouter_show.py(pyGen v1.0.0)


"""

:mod:`fcrouter_show` - PyFOS util to show FCR attributes
*******************************************************************************
The :mod:`fcrouter_show` PyFOS util to show FCR attributes


Generic FCR configuration parameters.

fcrouter_show : usage

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


.. function:: fcrouter_show.show_routing_configuration(session,\
lsan_enforce_tags_tag, shortest_ifl, lsan_speed_tag, backbone_fabric_id,\
maximum_lsan_count)

    *Show routing_configuration*

        Example Usage of the Method::

            ret = fcrouter_show.show_routing_configuration(session,\
            lsan_enforce_tags_tag, shortest_ifl, lsan_speed_tag,\
            backbone_fabric_id, maximum_lsan_count)
            print (ret)

        Details::

            routing_configurationObj = routing_configuration()
            routing_configurationObj.set_lsan_enforce_tags_tag(\
            lsan_enforce_tags_tag)
            routing_configurationObj.set_shortest_ifl(shortest_ifl)
            routing_configurationObj.set_lsan_speed_tag(lsan_speed_tag)
            routing_configurationObj.set_backbone_fabric_id(\
            backbone_fabric_id)
            routing_configurationObj.set_maximum_lsan_count(\
            maximum_lsan_count)
            print (ret)

        * Input::

            :param session: The session returned by the login.
            :param lsan_enforce_tags_tag: Accepts only the LSANs from the edge\
              fabric that matches the specified tag string into the local\
              FCR database. A valid tag is a string of a maximum of eight\
              characters. The maximum configurable enforce tags is eight. In\
              case speed tag is configured, only seven enforce tags can be\
              configured. Empty tags are not allowed.
            :param shortest_ifl: Enables or disables the shortest IFL mode in\
              FC Router. When the shortest IFL mode is enabled, FC Router\
              can choose a lowest-cost IFL path in the backbone fabric.  \
              TRUE  : Enables the shortest IFL mode  FALSE : Disables the\
              shortest IFL mode
            :param lsan_speed_tag: Allows the FCR to always import these\
              target devices to the hosts specified in the LSANs that match\
              the speed tag. Only one speed tag is allowed per FC router.\
              Empty tags are not allowed.
            :param backbone_fabric_id: Specifies the Backbone Fabric ID. It\
              uniquely identifies a fabric in FC Router configurations. The\
              backbone fabric is the fabric attached to the U_Ports of the\
              switch, for example, E_Ports or F_Ports. The backbone fabric\
              ID must be unique across all fabrics connected to the FC\
              Router.
            :param maximum_lsan_count: The default maximum LSAN count is set\
              to 3000. User can modify this LSAN count value. The valid\
              values are 3000, 5000 and 7500.

        * Output:

            :rtype: None or more instance of class routing_configuration on\
            Success  or a dictionary with error.

"""


# Start utils imports
import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_fibrechannel_routing import routing_configuration

from pyfos.utils import brcd_util
# End module imports


def _show_routing_configuration(session, routing_configurationObj):
    objlist = routing_configuration.get(session)
    routing_configurationlist = list()
    if isinstance(objlist, routing_configuration):
        objlist = [objlist]
    if isinstance(objlist, list):
        for i in range(len(objlist)):
            if routing_configurationObj.peek_lsan_enforce_tags_tag() != [] and\
               routing_configurationObj.peek_lsan_enforce_tags_tag() !=\
               objlist[i].peek_lsan_enforce_tags_tag():
                continue
            if routing_configurationObj.peek_shortest_ifl() is not None and\
               routing_configurationObj.peek_shortest_ifl() !=\
               objlist[i].peek_shortest_ifl():
                continue
            if routing_configurationObj.peek_lsan_speed_tag() is not None and\
               routing_configurationObj.peek_lsan_speed_tag() !=\
               objlist[i].peek_lsan_speed_tag():
                continue
            if routing_configurationObj.peek_backbone_fabric_id() is not None\
               and routing_configurationObj.peek_backbone_fabric_id() !=\
               objlist[i].peek_backbone_fabric_id():
                continue
            if routing_configurationObj.peek_maximum_lsan_count() is not None\
               and routing_configurationObj.peek_maximum_lsan_count() !=\
               objlist[i].peek_maximum_lsan_count():
                continue
            routing_configurationlist.append(objlist[i])
    else:
        print(objlist)
    return routing_configurationlist


def show_routing_configuration(session, lsan_enforce_tags_tag=None,
                               shortest_ifl=None, lsan_speed_tag=None,
                               backbone_fabric_id=None,
                               maximum_lsan_count=None):
    routing_configurationObj = routing_configuration()
    routing_configurationObj.set_lsan_enforce_tags_tag(lsan_enforce_tags_tag)
    routing_configurationObj.set_shortest_ifl(shortest_ifl)
    routing_configurationObj.set_lsan_speed_tag(lsan_speed_tag)
    routing_configurationObj.set_backbone_fabric_id(backbone_fabric_id)
    routing_configurationObj.set_maximum_lsan_count(maximum_lsan_count)
    return _show_routing_configuration(session, routing_configurationObj)


def validate(routing_configurationObj):
    if routing_configurationObj.peek_lsan_enforce_tags_tag() == [] or\
       routing_configurationObj.peek_shortest_ifl() is None or\
       routing_configurationObj.peek_lsan_speed_tag() is None or\
       routing_configurationObj.peek_backbone_fabric_id() is None or\
       routing_configurationObj.peek_maximum_lsan_count() is None:
        return 0
    return 0


def main(argv):
    filters = []
    inputs = brcd_util.parse(argv, routing_configuration, filters, validate)
    session = brcd_util.getsession(inputs)
    result = _show_routing_configuration(session, inputs['utilobject'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
