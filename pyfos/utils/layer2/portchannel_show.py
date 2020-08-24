#!/usr/bin/env python3


# Copyright © 2019 Broadcom. All rights reserved.
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


# portchannel_show.py(pyGen v1.0.0)


"""

:mod:`portchannel_show` - PyFOS util to show for portchannel
*******************************************************************************
The :mod:`portchannel_show` PyFOS util to show for portchannel


The list of portchannel interfaces on the switch, their related configuration\
and operational state.

portchannel_show : usage

* Infrastructure Options:
    * -i,--ipaddr=IPADDR: The IP address of the FOS switch.
    * -L,--login=LOGIN: The login name.
    * -P,--password=PASSWORD: The password.
    * -f,--vfid=VFID: The VFID to which the request is directed.
    * -s,--secured=MODE: The HTTPS mode "self" or "CA" [Optional].
    * -v,--verbose: Verbose mode [Optional].

* Util Script Options:
    * --name=NAME The portchannel name.
* Output:
    * Python dictionary content with RESTCONF response data.


.. function:: portchannel_show.show_portchannel(session, name)

    *Show portchannel*

        Example Usage of the Method::

            ret = portchannel_show.show_portchannel(session, name)
            print (ret)

        Details::

            portchannelObj = portchannel()
            portchannelObj.set_name(name)
            print (ret)

        * Input::

            :param session: The session returned by the login.
            :param name: The portchannel name.

        * Output:

            :rtype: None or more instance of class portchannel on Success  or\
            a dictionary with error.

"""


# Start utils imports
import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_interface import portchannel
from pyfos.utils import brcd_util
# End module imports


def _show_portchannel(session, portchannelObj):
    objlist = portchannel.get(session)
    portchannellist = list()
    if isinstance(objlist, portchannel):
        objlist = [objlist]
    if isinstance(objlist, list):
        for i in range(len(objlist)):
            if portchannelObj.peek_name() is not None and\
               portchannelObj.peek_name() != objlist[i].peek_name():
                continue
            portchannellist.append(objlist[i])
    else:
        print(objlist)
    return portchannellist


def show_portchannel(session, name=None):
    portchannelObj = portchannel()
    portchannelObj.set_name(name)
    return _show_portchannel(session, portchannelObj)


def validate(portchannelObj):
    if portchannelObj.peek_name() is None:
        return 0
    return 0


def main(argv):
    filters = ["name"]
    inputs = brcd_util.parse(argv, portchannel, filters, validate)
    session = brcd_util.getsession(inputs)
    result = _show_portchannel(session, inputs['utilobject'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
