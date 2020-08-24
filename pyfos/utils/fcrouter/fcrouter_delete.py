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


# fcrouter_delete.py(pyGen v1.0.0)


"""

:mod:`fcrouter_delete` - PyFOS util to delete FCR attributes
*******************************************************************************
The :mod:`fcrouter_delete` PyFOS util to delete FCR attributes


Generic FCR configuration parameters.

fcrouter_delete : usage

* Infrastructure Options:
    * -i,--ipaddr=IPADDR: The IP address of the FOS switch.
    * -L,--login=LOGIN: The login name.
    * -P,--password=PASSWORD: The password.
    * -f,--vfid=VFID: The VFID to which the request is directed.
    * -s,--secured=MODE: The HTTPS mode "self" or "CA" [Optional].
    * -v,--verbose: Verbose mode [Optional].

* Util Script Options:
    * --lsan-enforce-tag=LSAN-ENFORCE-TAG Accepts only the LSANs from the\
      edge fabric that matches the specified tag string into the local FCR\
      database. A valid tag is a string of a maximum of eight characters.\
      The maximum configurable enforce tags is eight. In case speed tag is\
      configured, only seven enforce tags can be configured. Empty tags are\
      not allowed.
    * --lsan-speed-tag=LSAN-SPEED-TAG Allows the FCR to always import these\
      target devices to the hosts specified in the LSANs that match the\
      speed tag. Only one speed tag is allowed per FC router. Empty tags are\
      not allowed.
* Output:
    * Python dictionary content with RESTCONF response data.


.. function:: fcrouter_delete.delete_routing_configuration(session,\
lsan_enforce_tags_tag, shortest_ifl, lsan_speed_tag, backbone_fabric_id,\
maximum_lsan_count)

    *Delete routing_configuration*

        Example Usage of the Method::

            ret = fcrouter_delete.delete_routing_configuration(session,\
            lsan_enforce_tags_tag, shortest_ifl, lsan_speed_tag,\
            backbone_fabric_id, maximum_lsan_count)
            print (ret)

        Details::

            routing_configurationObj = routing_configuration()
            routing_configurationObj.set_lsan_enforce_tags_tag(\
            lsan_enforce_tags_tag)
            routing_configurationObj.set_lsan_speed_tag(lsan_speed_tag)
            print (ret)

        * Input::

            :param session: The session returned by the login.
            :param lsan_enforce_tags_tag: Accepts only the LSANs from the edge\
              fabric that matches the specified tag string into the local\
              FCR database. A valid tag is a string of a maximum of eight\
              characters. The maximum configurable enforce tags is eight. In\
              case speed tag is configured, only seven enforce tags can be\
              configured. Empty tags are not allowed.
            :param lsan_speed_tag: Allows the FCR to always import these\
              target devices to the hosts specified in the LSANs that match\
              the speed tag. Only one speed tag is allowed per FC router.\
              Empty tags are not allowed.

        * Output:

            :rtype: Dictionary of response

"""


# Start utils imports
import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_fibrechannel_routing import routing_configuration

from pyfos.utils import brcd_util
# End module imports


def _delete_routing_configuration(session, routing_configurationObj):
    return routing_configurationObj.delete(session)


def delete_routing_configuration(session, lsan_enforce_tags_tag=None,
                                 lsan_speed_tag=None):
    routing_configurationObj = routing_configuration()
    routing_configurationObj.set_lsan_enforce_tags_tag(lsan_enforce_tags_tag)
    routing_configurationObj.set_lsan_speed_tag(lsan_speed_tag)
    return _delete_routing_configuration(session, routing_configurationObj)


def validate(routing_configurationObj):
    if routing_configurationObj.peek_lsan_speed_tag() is not None or\
       routing_configurationObj.peek_lsan_enforce_tags_tag() != []:
        return 0
    return 1


def main(argv):
    filters = ["lsan_enforce_tags_tag", "lsan_speed_tag"]
    inputs = brcd_util.parse(argv, routing_configuration, filters, validate)
    session = brcd_util.getsession(inputs)
    result = _delete_routing_configuration(session, inputs['utilobject'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
