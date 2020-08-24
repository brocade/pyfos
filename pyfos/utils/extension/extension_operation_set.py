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


# extension_operation_set.py(pyGen v1.0.0)


"""

:mod:`extension_operation_set` - PyFOS util  support for RPC operations\
of extension_operation_parameters
******************************************************************************\
*******************************************************************************
The :mod:`extension_operation_set` PyFOS util  support for RPC operations of\
extension_operation_parameters


The extension operation input container.

extension_operation_set : usage

* Infrastructure Options:
    * -i,--ipaddr=IPADDR: The IP address of the FOS switch.
    * -L,--login=LOGIN: The login name.
    * -P,--password=PASSWORD: The password.
    * -f,--vfid=VFID: The VFID to which the request is directed.
    * -s,--secured=MODE: The HTTPS mode "self" or "CA" [Optional].
    * -v,--verbose: Verbose mode [Optional].

* Util Script Options:
    * --config-clear=CONFIG-CLEAR Clear the extension configuration for the\
      switch or blade.  The config clear operation may be disruptive in\
      nature.  switch : A switch needs to be rebooted after a config clear\
      operation, without which future config operations  will be blocked. \
      blade  : A blade needs to be powered off before clearing the   slot\
      corresponding configuration.  Supported values:  false: No operation\
      true : Clear the extension configuration.
    * --config-default=CONFIG-DEFAULT Default the extension configuration for\
      the switch or blade. The config default operation is a disruptive\
      operation and details are as below.  switch : After successful\
      operation the switch    automatically reboots.  blade  : A blade\
      should be in online state for the operation    to be allowed and the\
      blade may be slot powered off and on    to allow different extension\
      modes to be applied correctly. Supported values:  false: No operation \
      true : Default the extension configuration.
    * --slot=SLOT The slot number of for the datapath processor.
    * --dp-id=DP-ID Extension Data Path Processor ID. Based on platform either\
      it will have a single DP or dual DP. In case of single DP only DP0 is\
      supported, and in case of dual DP both DP0 and DP1 are supported  0 :\
      DP0 1 : DP1.
    * --global-lan-statistics-reset=GLOBAL-LAN-STATISTICS-RESET Reset the\
      global LAN statistics on a DP.  Supported values:  false: No operation\
       true : Reset the global LAN statistics.
* Output:
    * Python dictionary content with RESTCONF response data.


.. function::\
extension_operation_set.rpc_extension_operation_parameters(session,\
config_clear, config_default, slot, dp_id, global_lan_statistics_reset)

    *RPC extension_operation_parameters*

        Example Usage of the Method::

            ret =\
            extension_operation_set.rpc_extension_operation_parameters(\
            session, config_clear, config_default, slot, dp_id,\
            global_lan_statistics_reset)
            print (ret)

        Details::

            extension_operation_parametersObj =\
            extension_operation_parameters()
            extension_operation_parametersObj.set_config_clear(config_clear)
            extension_operation_parametersObj.set_config_default(\
            config_default)
            extension_operation_parametersObj.set_slot(slot)
            extension_operation_parametersObj.set_dp_id(dp_id)
            extension_operation_parametersObj.set_global_lan_statistics_reset(\
            global_lan_statistics_reset)
            print (ret)

        * Input::

            :param session: The session returned by the login.
            :param config_clear: Clear the extension configuration for the\
              switch or blade.  The config clear operation may be disruptive\
              in nature.  switch : A switch needs to be rebooted after a\
              config clear operation, without which future config operations\
               will be blocked.  blade  : A blade needs to be powered off\
              before clearing the   slot corresponding configuration. \
              Supported values:  false: No operation true : Clear the\
              extension configuration.
            :param config_default: Default the extension configuration for the\
              switch or blade. The config default operation is a disruptive\
              operation and details are as below.  switch : After successful\
              operation the switch    automatically reboots.  blade  : A\
              blade should be in online state for the operation    to be\
              allowed and the blade may be slot powered off and on    to\
              allow different extension modes to be applied correctly.\
              Supported values:  false: No operation  true : Default the\
              extension configuration.
            :param slot: The slot number of for the datapath processor.
            :param dp_id: Extension Data Path Processor ID. Based on platform\
              either it will have a single DP or dual DP. In case of single\
              DP only DP0 is supported, and in case of dual DP both DP0 and\
              DP1 are supported  0 : DP0 1 : DP1.
            :param global_lan_statistics_reset: Reset the global LAN\
              statistics on a DP.  Supported values:  false: No operation \
              true : Reset the global LAN statistics.

        * Output:

            :rtype: Dictionary of response

"""


# Start utils imports
import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_operation_extension import\
     extension_operation_parameters

from pyfos.utils import brcd_util
# End module imports


def _rpc_extension_operation_parameters(session,
                                        extension_operation_parametersObj):
    return extension_operation_parametersObj.post(session)


def rpc_extension_operation_parameters(session, config_clear=None,
                                       config_default=None, slot=None,
                                       dp_id=None,
                                       global_lan_statistics_reset=None):
    extension_op_parametersObj = extension_operation_parameters()
    extension_op_parametersObj.set_config_clear(config_clear)
    extension_op_parametersObj.set_config_default(config_default)
    extension_op_parametersObj.set_slot(slot)
    extension_op_parametersObj.set_dp_id(dp_id)
    extension_op_parametersObj.set_global_lan_statistics_reset(
                                      global_lan_statistics_reset)
    return _rpc_extension_operation_parameters(session,
                                               extension_op_parametersObj)


def validate(extension_operation_parametersObj):
    if extension_operation_parametersObj.peek_slot() is None or\
       extension_operation_parametersObj.peek_config_clear() is None and\
       extension_operation_parametersObj.peek_config_default() is None and\
       extension_operation_parametersObj.peek_global_lan_statistics_reset()\
       is None:
        return 1
    return 0


def main(argv):
    filters = ["config_clear", "config_default", "slot", "dp_id",
               "global_lan_statistics_reset"]
    inputs = brcd_util.parse(argv, extension_operation_parameters, filters,
                             validate)
    session = brcd_util.getsession(inputs)
    result = _rpc_extension_operation_parameters(session,
                                                 inputs['utilobject'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
