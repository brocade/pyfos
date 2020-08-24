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


# fabric_operations.py(pyGen v1.0.0)


"""

:mod:`fabric_operations` - PyFOS util  support for RPC operations of\
fabric_operation_parameters
******************************************************************************\
*******************************************************************************
The :mod:`fabric_operations` PyFOS util  support for RPC operations of\
fabric_operation_parameters


Input container to perform fabric related operation.

fabric_operations : usage

* Infrastructure Options:
    * -i,--ipaddr=IPADDR: The IP address of the FOS switch.
    * -L,--login=LOGIN: The login name.
    * -P,--password=PASSWORD: The password.
    * -f,--vfid=VFID: The VFID to which the request is directed.
    * -s,--secured=MODE: The HTTPS mode "self" or "CA" [Optional].
    * -v,--verbose: Verbose mode [Optional].

* Util Script Options:
    * --build-fabric=BUILD-FABRIC The input which is required to initiate the\
      build fabric operation. This operation requires switch to be enabled\
      state. And only 'true' should be used as input. To verify the build\
      fabric status please infer brocade-fibrechannel-fabric?
* Output:
    * Python dictionary content with RESTCONF response data.


.. function:: fabric_operations.rpc_fabric_operation_parameters(session,\
build_fabric)

    *RPC fabric_operation_parameters*

        Example Usage of the Method::

            ret = fabric_operations.rpc_fabric_operation_parameters(session,\
            build_fabric)
            print (ret)

        Details::

            fabric_operation_parametersObj = fabric_operation_parameters()
            fabric_operation_parametersObj.set_build_fabric(build_fabric)
            print (ret)

        * Input::

            :param session: The session returned by the login.
            :param build_fabric: The input which is required to initiate the\
              build fabric operation. This operation requires switch to be\
              enabled state. And only 'true' should be used as input. To\
              verify the build fabric status please infer\
              brocade-fibrechannel-fabric?

        * Output:

            :rtype: Dictionary of response

"""


# Start utils imports
import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_operation_fabric import\
     fabric_operation_parameters

from pyfos.utils import brcd_util
# End module imports


def _rpc_fabric_operation_parameters(session, fabric_operation_parametersObj):
    return fabric_operation_parametersObj.post(session)


def rpc_fabric_operation_parameters(session, build_fabric=None):
    fabric_operation_parametersObj = fabric_operation_parameters()
    fabric_operation_parametersObj.set_build_fabric(build_fabric)
    return _rpc_fabric_operation_parameters(session,
                                            fabric_operation_parametersObj)


def validate(fabric_operation_parametersObj):
    if fabric_operation_parametersObj.peek_build_fabric() is None:
        return 1
    return 0


def main(argv):
    filters = ["build_fabric"]
    inputs = brcd_util.parse(argv, fabric_operation_parameters, filters,
                             validate)
    session = brcd_util.getsession(inputs)
    result = _rpc_fabric_operation_parameters(session, inputs['utilobject'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
