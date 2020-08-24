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


# pod_state_interface_set.py(pyGen v1.0.0)


"""

:mod:`pod_state_interface_set` - PyFOS util to modify for fibrechannel
*******************************************************************************
The :mod:`pod_state_interface_set` PyFOS util to modify for fibrechannel


A list of interfaces on the device.  System-controlled interfaces created by\
the system are always present in this list, whether they are configured or\
not.

pod_state_interface_set : usage

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
    * --pod-license-state=POD-LICENSE-STATE POD license status of the logical\
      port.
* Output:
    * Python dictionary content with RESTCONF response data.


.. function:: pod_state_interface_set.modify_fibrechannel(session, name,\
pod_license_state)

    *Modify fibrechannel*

        Example Usage of the Method::

            ret = pod_state_interface_set.modify_fibrechannel(session, name,\
            pod_license_state)
            print (ret)

        Details::

            fibrechannelObj = fibrechannel()
            fibrechannelObj.set_name(name)
            fibrechannelObj.set_pod_license_state(pod_license_state)
            print (ret)

        * Input::

            :param session: The session returned by the login.
            :param name: The name of the interface. The slot and port number\
              of the specified port in the format slot/port.
            :param pod_license_state: POD license status of the logical port.

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


def modify_fibrechannel(session, name=None, pod_license_state=None):
    fibrechannelObj = fibrechannel()
    fibrechannelObj.set_name(name)
    fibrechannelObj.set_pod_license_state(pod_license_state)
    return _modify_fibrechannel(session, fibrechannelObj)


def validate(fibrechannelObj):
    if fibrechannelObj.peek_name() is None or\
       fibrechannelObj.peek_pod_license_state() is None:
        return 1
    return 0


def main(argv):
    filters = ["name", "pod_license_state"]
    inputs = brcd_util.parse(argv, fibrechannel, filters, validate)
    session = brcd_util.getsession(inputs)
    result = _modify_fibrechannel(session, inputs['utilobject'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
