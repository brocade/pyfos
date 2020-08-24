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


# portchannel_create.py(pyGen v1.0.0)


"""

:mod:`portchannel_create` - PyFOS util to create for portchannel
*******************************************************************************
The :mod:`portchannel_create` PyFOS util to create for portchannel


The list of portchannel interfaces on the switch, their related configuration\
and operational state.

portchannel_create : usage

* Infrastructure Options:
    * -i,--ipaddr=IPADDR: The IP address of the FOS switch.
    * -L,--login=LOGIN: The login name.
    * -P,--password=PASSWORD: The password.
    * -f,--vfid=VFID: The VFID to which the request is directed.
    * -s,--secured=MODE: The HTTPS mode "self" or "CA" [Optional].
    * -v,--verbose: Verbose mode [Optional].

* Util Script Options:
    * --name=NAME The portchannel name.
    * --portchannel-type=PORTCHANNEL-TYPE The type of a portchannel interface.\
      Portchannel Type is a mandatory parameter while the portchannel is\
      created.  Possible values: static   : Static portchannel type. dynamic\
       : Dynamic portchannel type.
* Output:
    * Python dictionary content with RESTCONF response data.


.. function:: portchannel_create.create_portchannel(session, name,\
portchannel_type)

    *Create portchannel*

        Example Usage of the Method::

            ret = portchannel_create.create_portchannel(session, name,\
            portchannel_type)
            print (ret)

        Details::

            portchannelObj = portchannel()
            portchannelObj.set_name(name)
            portchannelObj.set_portchannel_type(portchannel_type)
            print (ret)

        * Input::

            :param session: The session returned by the login.
            :param name: The portchannel name.
            :param portchannel_type: The type of a portchannel interface.\
              Portchannel Type is a mandatory parameter while the\
              portchannel is created.  Possible values: static   : Static\
              portchannel type. dynamic  : Dynamic portchannel type.

        * Output:

            :rtype: Dictionary of response

"""


# Start utils imports
import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_interface import portchannel
from pyfos.utils import brcd_util
# End module imports


def _create_portchannel(session, portchannelObj):
    return portchannelObj.post(session)


def create_portchannel(session, name=None, portchannel_type=None):
    portchannelObj = portchannel()
    portchannelObj.set_name(name)
    portchannelObj.set_portchannel_type(portchannel_type)
    return _create_portchannel(session, portchannelObj)


def validate(portchannelObj):
    if portchannelObj.peek_name() is None or\
       portchannelObj.peek_portchannel_type() is None:
        return 1
    return 0


def main(argv):
    filters = ["name", "portchannel_type"]
    inputs = brcd_util.parse(argv, portchannel, filters, validate)
    session = brcd_util.getsession(inputs)
    result = _create_portchannel(session, inputs['utilobject'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
