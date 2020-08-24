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


"""

:mod:`end_device_management` - PyFOS util  support for RPC operations of\
End_Device_parameters
******************************************************************************\
******************************************************************************
The :mod:`end_device_management` PyFOS util  support for RPC operations of\
End Device Management Module.

This module can be used to manage END device.

* inputs:

|  Infrastructure options:

  | -i,--ipaddr=IPADDR     IP address of FOS switch.
  | -L,--login=LOGIN       login name.
  | -P,--password=PASSWORD password.
  | -f,--vfid=VFID         VFID to which the request is directed to [OPTIONAL].
  | -s,--secured=MODE      HTTPS mode "self" or "CA" [OPTIONAL].
  | -v,--verbose           verbose mode[OPTIONAL].

|  Util scripts options:

   | --n-port-wwn=N-PORT-WWN: The world wide Port name (PWWN) of the device
   | --n-port-id=N-PORT-ID: The Fibre Channel ID (FCID) of the device
   | --payload=PAYLOAD: Opaque payload and response buffer in base64 format
   | --version=VERSION: Version Identifier for the remote device

* outputs:
    * Status of the End Device Management operation


.. function:: end_device_management.rpc_end_device_management(session,
                  n_port_wwn, n_port_id, payload)


    *RPC End Device Management*


        Example usage of the method::

            ret = end_device_management.rpc_end_device_management(session,
                  n_port_wwn, n_port_id, payload)
            print (ret)

        Details::

            result = _add_access_gateway_nportmap(session, nport_obj)
            end_device_managementObj = end_device_management()
            end_device_managementObj.set_n_port_wwn(n_port_wwn)
            end_device_managementObj.set_n_port_id(n_port_id)
            end_device_managementObj.payload(payload)
            return _rpc_end_device_management(session,
                                      end_device_managementObj)

        * inputs:
            :param session: session returned by login.
            :param n_port_wwn: The world wide Port name (PWWN) of the device.
            :param n_port_id: The Fibre Channel ID (FCID) of the device.
            :param payload: Opaque payload and response buffer in\
                             base64 format.

        * outputs:
            :rtype: dictionary of return status matching rest response

"""


# Start utils imports
import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_operation_end_device_management import\
    end_device_management

from pyfos.utils import brcd_util
# End module imports


def _rpc_end_device_management(session,
                               end_device_managementObj):
    return end_device_managementObj.post(session)


def rpc_end_device_management(session, n_port_wwn=None,
                              n_port_id=None, payload=None):
    end_device_managementObj = end_device_management()
    end_device_managementObj.set_n_port_wwn(n_port_wwn)
    end_device_managementObj.set_n_port_id(n_port_id)
    end_device_managementObj.payload(payload)
    return _rpc_end_device_management(session,
                                      end_device_managementObj)


def validate(end_device_management_operation_paramObj):
    if end_device_management_operation_paramObj.peek_n_port_wwn() is None or\
       end_device_management_operation_paramObj.peek_n_port_id() is None or\
       end_device_management_operation_paramObj.peek_payload() is None\
       is None:
        return 1
    return 0


def main(argv):
    filters = ["n_port_wwn", "n_port_id", "payload", "version"]
    inputs = brcd_util.parse(argv, end_device_management, filters, validate)
    session = brcd_util.getsession(inputs)
    result = _rpc_end_device_management(session, inputs['utilobject'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
