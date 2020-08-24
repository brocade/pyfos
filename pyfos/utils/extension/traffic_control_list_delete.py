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


# traffic_control_list_delete.py(pyGen v1.0.0)


"""

:mod:`traffic_control_list_delete` - PyFOS util to delete for\
 traffic_control_list
******************************************************************************\
*******************************************************************************
The:mod:`traffic_control_list_delete` PyFOS util to delete for\
 traffic_control_list


Represents traffic control lists in order to manage IP Extension LAN flows.

traffic_control_list_delete: usage

* Infrastructure Options:
    * -i,--ipaddr=IPADDR: The IP address of the FOS switch.
    * -L,--login=LOGIN: The login name.
    * -P,--password=PASSWORD: The password.
    * -f,--vfid=VFID: The VFID to which the request is directed.
    * -s,--secured=MODE: The HTTPS mode "self" or "CA" [Optional].
    * -v,--verbose: Verbose mode [Optional].
    * -a,--authtoken: AuthToken value or AuthTokenManager config\
    file[OPTIONAL].
    * -z,--nosession: Sessionless authentication based login[OPTIONAL].
    * --nocredential: No credential to be sent in the request[OPTIONAL].

* Util Script Options:
    * --traffic-control-list-name=TRAFFIC-CONTROL-LIST-NAME: Name of the\
      Traffic-Control-List.
* Output:
    * Python dictionary content with RESTCONF response data.


.. function:: traffic_control_list_delete.delete_traffic_control_list(session,\
traffic_control_list_name)

    *Delete traffic_control_list*

    Example Usage of the Method::

            ret =\
 traffic_control_list_delete.delete_traffic_control_list(session,\
 traffic_control_list_name)
            print(ret)

    Details::

        traffic_control_listObj = traffic_control_list()
       \
 traffic_control_listObj.set_traffic_control_list_name(\
 traffic_control_list_name)
        ret = _delete_traffic_control_list(session, traffic_control_listObj)
        print(ret)

    **Inputs**

    :param session: The session returned by the login.
    :param traffic_control_list_name: Name of the Traffic-Control-List.

    **Output**

    :rtype: Dictionary of response

"""


# Start utils imports
import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_extension import traffic_control_list

from pyfos.utils import brcd_util
# End module imports


def _delete_traffic_control_list(session, traffic_control_listObj):
    return traffic_control_listObj.delete(session)


def delete_traffic_control_list(session, traffic_control_list_name=None):
    traffic_control_listObj = traffic_control_list()
    traffic_control_listObj.set_traffic_control_list_name(
                            traffic_control_list_name)
    return _delete_traffic_control_list(session, traffic_control_listObj)


def validate(traffic_control_listObj):
    if traffic_control_listObj.peek_traffic_control_list_name() is None:
        return 1
    return 0


def main(argv):
    filters = ["traffic_control_list_name"]
    inputs = brcd_util.parse(argv, traffic_control_list, filters, validate)
    session = brcd_util.getsession(inputs)
    result = _delete_traffic_control_list(session, inputs['utilobject'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
