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


# lldp_global_modify.py(pyGen v1.0.0)


"""

:mod:`lldp_global_modify` - PyFOS util to modify for lldp_global
*******************************************************************************
The :mod:`lldp_global_modify` PyFOS util to modify for lldp_global


The LLDP switch level configuration and operational parameters.

lldp_global_modify : usage

* Infrastructure Options:
    * -i,--ipaddr=IPADDR: The IP address of the FOS switch.
    * -L,--login=LOGIN: The login name.
    * -P,--password=PASSWORD: The password.
    * -f,--vfid=VFID: The VFID to which the request is directed.
    * -s,--secured=MODE: The HTTPS mode "self" or "CA" [Optional].
    * -v,--verbose: Verbose mode [Optional].

* Util Script Options:
    * --multiplier=MULTIPLIER The LLDP timeout multiplier value. Default value\
      is 4
    * --enabled-state=ENABLED-STATE The LLDP protocol state of the switch. The\
      possible values are:  true : LLDP is enabled on the switch  false :\
      LLDP is disabled on the switch Default value is true.
    * --system-name=SYSTEM-NAME The LLDP system name of the switch.
    * --system-description=SYSTEM-DESCRIPTION The LLDP system description of\
      the switch.
    * --tx-interval=TX-INTERVAL The LLDP Tx interval of the switch. Default\
      value is 30 seconds
* Output:
    * Python dictionary content with RESTCONF response data.


.. function:: lldp_global_modify.modify_lldp_global(session, multiplier,\
enabled_state, system_name, system_description, tx_interval)

    *Modify lldp_global*

        Example Usage of the Method::

            ret = lldp_global_modify.modify_lldp_global(session, multiplier,\
            enabled_state, system_name, system_description, tx_interval)
            print (ret)

        Details::

            lldp_globalObj = lldp_global()
            lldp_globalObj.set_multiplier(multiplier)
            lldp_globalObj.set_enabled_state(enabled_state)
            lldp_globalObj.set_system_name(system_name)
            lldp_globalObj.set_system_description(system_description)
            lldp_globalObj.set_tx_interval(tx_interval)
            print (ret)

        * Input::

            :param session: The session returned by the login.
            :param multiplier: The LLDP timeout multiplier value. Default\
              value is 4
            :param enabled_state: The LLDP protocol state of the switch. The\
              possible values are:  true : LLDP is enabled on the switch \
              false : LLDP is disabled on the switch Default value is true.
            :param system_name: The LLDP system name of the switch.
            :param system_description: The LLDP system description of the\
              switch.
            :param tx_interval: The LLDP Tx interval of the switch. Default\
              value is 30 seconds

        * Output:

            :rtype: Dictionary of response

"""


# Start utils imports
import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_lldp import lldp_global
from pyfos.utils import brcd_util
# End module imports


def _modify_lldp_global(session, lldp_globalObj):
    return lldp_globalObj.patch(session)


def modify_lldp_global(session, multiplier=None, enabled_state=None,
                       system_name=None, system_description=None,
                       tx_interval=None):
    lldp_globalObj = lldp_global()
    lldp_globalObj.set_multiplier(multiplier)
    lldp_globalObj.set_enabled_state(enabled_state)
    lldp_globalObj.set_system_name(system_name)
    lldp_globalObj.set_system_description(system_description)
    lldp_globalObj.set_tx_interval(tx_interval)
    return _modify_lldp_global(session, lldp_globalObj)


def validate(lldp_globalObj):
    if lldp_globalObj.peek_multiplier() is None and\
       lldp_globalObj.peek_enabled_state() is None and\
       not lldp_globalObj.peek_system_name() and\
       not lldp_globalObj.peek_system_description() and\
       lldp_globalObj.peek_tx_interval() is None:
        return 1
    return 0


def main(argv):
    filters = ["multiplier", "enabled_state", "system_name",
               "system_description", "tx_interval"]
    inputs = brcd_util.parse(argv, lldp_global, filters, validate)
    session = brcd_util.getsession(inputs)
    result = _modify_lldp_global(session, inputs['utilobject'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
