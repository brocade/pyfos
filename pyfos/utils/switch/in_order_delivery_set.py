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


# in_order_delivery_set.py(pyGen v1.0.0)


"""

:mod:`in_order_delivery_set` - PyFOS util to modify fibrechannel_switch
******************************************************************************\
*******************************************************************************
The :mod:`in_order_delivery_set` PyFOS util to modify fibrechannel_switch


Switch state parameters. Requests can also be made using a query that \
specifies the vf-id of the fabric. This request also provides the switch \
state parameters.

in_order_delivery_set : usage

* Infrastructure Options:
    * -i,--ipaddr=IPADDR: The IP address of the FOS switch.
    * -L,--login=LOGIN: The login name.
    * -P,--password=PASSWORD: The password.
    * -f,--vfid=VFID: The VFID to which the request is directed.
    * -s,--secured=MODE: The HTTPS mode "self" or "CA" [Optional].
    * -v,--verbose: Verbose mode [Optional].

* Util Script Options:
    * --name=NAME: The switch world wide name (WWN).
    * --in-order-delivery-enabled=IN-ORDER-DELIVERY-ENABLED: Desired state \
      for the In Order Delivery (IOD) feature. true: Enabled false: Disabled
* Output:
    * Python dictionary content with RESTCONF response data.


.. function:: in_order_delivery_set.modify_fibrechannel_switch(session, name, \
in_order_delivery_enabled)

    *Modify fibrechannel_switch*

    Example Usage of the Method::

        ret = in_order_delivery_set.modify_fibrechannel_switch(session, name, \
in_order_delivery_enabled)
        print (ret)

    Details::

        fibrechannel_switchObj = fibrechannel_switch()
        fibrechannel_switchObj.set_name(name)
        fibrechannel_switchObj.set_in_order_delivery_enabled(\
in_order_delivery_enabled)
        print (ret)

    :param session: The session returned by the login.
    :param name: The switch world wide name (WWN).
    :param in_order_delivery_enabled: Desired state for the In Order \
      Delivery (IOD) feature. true: Enabled false: Disabled

    :rtype: Dictionary of response

"""


# Start utils imports
import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_fibrechannel_switch import fibrechannel_switch
from pyfos.utils import brcd_util
# End module imports


def _modify_fibrechannel_switch(session, fibrechannel_switchObj):
    return fibrechannel_switchObj.patch(session)


def modify_fibrechannel_switch(session, name=None,
                               in_order_delivery_enabled=None):
    fibrechannel_switchObj = fibrechannel_switch()
    fibrechannel_switchObj.set_name(name)
    fibrechannel_switchObj.set_in_order_delivery_enabled(
                           in_order_delivery_enabled)
    return _modify_fibrechannel_switch(session, fibrechannel_switchObj)


def validate(fibrechannel_switchObj):
    if fibrechannel_switchObj.peek_name() is None or\
       fibrechannel_switchObj.peek_in_order_delivery_enabled() is None:
        return 1
    return 0


def main(argv):
    filters = ["name", "in_order_delivery_enabled"]
    inputs = brcd_util.parse(argv, fibrechannel_switch, filters, validate)
    session = brcd_util.getsession(inputs)
    result = _modify_fibrechannel_switch(session, inputs['utilobject'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
