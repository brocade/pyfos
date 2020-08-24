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


# logical_fabric_show.py(pyGen v1.0.0)


"""

:mod:`logical_fabric_show` - PyFOS util to show logical_e_port
*******************************************************************************
The :mod:`logical_fabric_show` PyFOS util to show logical_e_port


The list of logical E_Port interfaces on the device which form the logical \
inter switch link (lisl).

logical_fabric_show : usage

* Infrastructure Options:
    * -i,--ipaddr=IPADDR: The IP address of the FOS switch.
    * -L,--login=LOGIN: The login name.
    * -P,--password=PASSWORD: The password.
    * -f,--vfid=VFID: The VFID to which the request is directed.
    * -s,--secured=MODE: The HTTPS mode "self" or "CA" [Optional].
    * -v,--verbose: Verbose mode [Optional].

* Util Script Options:
    * --port-index=PORT-INDEX The unique port number on the switch for\
      identifying a logical E_Port.
* Output:
    * Python dictionary content with RESTCONF response data.


.. function:: logical_fabric_show.show_logical_e_port(session, port_index)

    *Show logical_e_port*

        Example Usage of the Method::

            ret = logical_fabric_show.show_logical_e_port(session, port_index)
            print (ret)

        Details::

            logical_e_portObj = logical_e_port()
            logical_e_portObj.set_port_index(port_index)
            print (ret)

        * Input::

            :param session: The session returned by the login.
            :param port_index: The unique port number on the switch for\
              identifying a logical E_Port.

        * Output:

            :rtype: None or more instance of class logical_e_port on Success \
            or a dictionary with error.

"""


# Start utils imports
import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_interface import logical_e_port

from pyfos.utils import brcd_util
# End module imports


def _show_logical_e_port(session, logical_e_portObj):
    objlist = logical_e_port.get(session)
    logical_e_portlist = list()
    if isinstance(objlist, logical_e_port):
        objlist = [objlist]
    if isinstance(objlist, list):
        for i in range(len(objlist)):
            if logical_e_portObj.peek_port_index() is not None and\
               logical_e_portObj.peek_port_index() !=\
               objlist[i].peek_port_index():
                continue
            logical_e_portlist.append(objlist[i])
    else:
        print(objlist)
    return logical_e_portlist


def show_logical_e_port(session, port_index=None):
    logical_e_portObj = logical_e_port()
    logical_e_portObj.set_port_index(port_index)
    return _show_logical_e_port(session, logical_e_portObj)


def validate(logical_e_portObj):
    if logical_e_portObj.peek_port_index() is None:
        return 0
    return 0


def main(argv):
    filters = ["port_index"]
    inputs = brcd_util.parse(argv, logical_e_port, filters, validate)
    session = brcd_util.getsession(inputs)
    result = _show_logical_e_port(session, inputs['utilobject'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
