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


# port_export_state_set.py(pyGen v1.0.0)


"""

:mod:`port_export_state_set` - PyFOS util to modify for EX-Port attributes
*******************************************************************************
The :mod:`port_export_state_set` PyFOS util to modify for EX-Port attributes


A list of interfaces on the device.  System-controlled interfaces created by\
the system are always present in this list, whether they are configured or\
not.

port_export_state_set : usage

* Infrastructure Options:
    * -i,--ipaddr=IPADDR: The IP address of the FOS switch.
    * -L,--login=LOGIN: The login name.
    * -P,--password=PASSWORD: The password.
    * -f,--vfid=VFID: The VFID to which the request is directed.
    * -s,--secured=MODE: The HTTPS mode "self" or "CA" [Optional].
    * -v,--verbose: Verbose mode [Optional].

* Util Script Options:
    * --name=NAME The name of the interface. The slot and port number of the\
      specified port in the format slot/port.
    * --edge-fabric-id=EDGE-FABRIC-ID Specifies the fabric ID. The valid\
      values for FID are from 1 through 128.
    * --preferred-front-domain-id=PREFERRED-FRONT-DOMAIN-ID Specifies the\
      preferred domain ID. The valid values are 1 to 239.
    * --ex-port-enabled=EX-PORT-ENABLED Configures the port as an EX_Port.  0\
      : The port is not configured as an EX_Port. 1 : The port is configured\
      as an EX_Port.
* Output:
    * Python dictionary content with RESTCONF response data.


.. function:: port_export_state_set.modify_fibrechannel(session, name,\
edge_fabric_id, preferred_front_domain_id, ex_port_enabled)

    *Modify fibrechannel*

        Example Usage of the Method::

            ret = port_export_state_set.modify_fibrechannel(session, name,\
            edge_fabric_id, preferred_front_domain_id, ex_port_enabled)
            print (ret)

        Details::

            fibrechannelObj = fibrechannel()
            fibrechannelObj.set_name(name)
            fibrechannelObj.set_edge_fabric_id(edge_fabric_id)
            fibrechannelObj.set_preferred_front_domain_id(\
            preferred_front_domain_id)
            fibrechannelObj.set_ex_port_enabled(ex_port_enabled)
            print (ret)

        * Input::

            :param session: The session returned by the login.
            :param name: The name of the interface. The slot and port number\
              of the specified port in the format slot/port.
            :param edge_fabric_id: Specifies the fabric ID. The valid values\
              for FID are from 1 through 128.
            :param preferred_front_domain_id: Specifies the preferred domain\
              ID. The valid values are 1 to 239.
            :param ex_port_enabled: Configures the port as an EX_Port.  0 :\
              The port is not configured as an EX_Port. 1 : The port is\
              configured as an EX_Port.

        * Output:

            :rtype: Dictionary of response

"""


# Start utils imports
import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_interface import fibrechannel

from pyfos.utils import brcd_util
# End module imports


def _modify_fibrechannel(session, fibrechannelObj):
    return fibrechannelObj.patch(session)


def modify_fibrechannel(session, name=None, edge_fabric_id=None,
                        preferred_front_domain_id=None, ex_port_enabled=None):
    fibrechannelObj = fibrechannel()
    fibrechannelObj.set_name(name)
    fibrechannelObj.set_edge_fabric_id(edge_fabric_id)
    fibrechannelObj.set_preferred_front_domain_id(preferred_front_domain_id)
    fibrechannelObj.set_ex_port_enabled(ex_port_enabled)
    return _modify_fibrechannel(session, fibrechannelObj)


def validate(fibrechannelObj):
    if fibrechannelObj.peek_name() is not None and\
       (fibrechannelObj.peek_edge_fabric_id() is not None or
        fibrechannelObj.peek_preferred_front_domain_id() is not None or
       fibrechannelObj.peek_ex_port_enabled() is not None):
        return 0
    return 1


def main(argv):
    filters = ["name", "edge_fabric_id", "preferred_front_domain_id",
               "ex_port_enabled"]
    inputs = brcd_util.parse(argv, fibrechannel, filters, validate)
    session = brcd_util.getsession(inputs)
    result = _modify_fibrechannel(session, inputs['utilobject'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
