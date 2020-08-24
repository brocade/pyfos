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

# lsan_device_show.py(pyGen v1.0.0)

"""

:mod:`lsan_device_show` - PyFOS util to show lsan devices
*******************************************************************************
The :mod:`lsan_device_show` PyFOS util to show lsan devices


Displays the information of each device.

lsan_device_show : usage

* Infrastructure Options:
    * -i,--ipaddr=IPADDR: The IP address of the FOS switch.
    * -L,--login=LOGIN: The login name.
    * -P,--password=PASSWORD: The password.
    * -f,--vfid=VFID: The VFID to which the request is directed.
    * -s,--secured=MODE: The HTTPS mode "self" or "CA" [Optional].
    * -v,--verbose: Verbose mode [Optional].

* Util Script Options:

* Output:
    * Python dictionary content with RESTCONF response data.


.. function:: lsan_device_show.show_lsan_device(session, physical_pid,\
source_fabric_id, device_status, proxy_pid, device_wwn, imported_fabric_id)

    *Show lsan_device*

        Example Usage of the Method::

            ret = lsan_device_show.show_lsan_device(session, physical_pid,\
            source_fabric_id, device_status, proxy_pid, device_wwn,\
            imported_fabric_id)
            print (ret)

        Details::

            lsan_deviceObj = lsan_device()
            lsan_deviceObj.set_physical_pid(physical_pid)
            lsan_deviceObj.set_source_fabric_id(source_fabric_id)
            lsan_deviceObj.set_device_status(device_status)
            lsan_deviceObj.set_proxy_pid(proxy_pid)
            lsan_deviceObj.set_device_wwn(device_wwn)
            lsan_deviceObj.set_imported_fabric_id(imported_fabric_id)
            print (ret)

        * Input::

            :param session: The session returned by the login.
            :param physical_pid: The port ID of the device in source fabric.
            :param source_fabric_id: The fabric in which the device are\
              physically present.
            :param device_status: States include:   configured   - Device is\
              configured to be in an LSAN, but the device                 is\
              neither imported nor exists in this fabric  initializing -\
              Device is in an intermediate state. It is not yet             \
                 imported into the fabric.  exist        - Device exists in\
              this fabric (the fabric of the zone                 entry). \
              imported     - Device has been imported (proxy created) into\
              this                 fabric.
            :param proxy_pid: The proxy pid of the device.
            :param device_wwn: The WWN of the device.
            :param imported_fabric_id: The fabric in which the devices are\
              imported.

        * Output:

            :rtype: None or more instance of class lsan_device on Success  or\
            a dictionary with error.

"""


# Start utils imports
import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_fibrechannel_routing import lsan_device

from pyfos.utils import brcd_util
# End module imports


def _show_lsan_device(session, lsan_deviceObj):
    objlist = lsan_device.get(session)
    lsan_devicelist = list()
    if isinstance(objlist, lsan_device):
        objlist = [objlist]
    if isinstance(objlist, list):
        for i in range(len(objlist)):
            if lsan_deviceObj.peek_physical_pid() is not None and\
               lsan_deviceObj.peek_physical_pid() !=\
               objlist[i].peek_physical_pid():
                continue
            if lsan_deviceObj.peek_source_fabric_id() is not None and\
               lsan_deviceObj.peek_source_fabric_id() !=\
               objlist[i].peek_source_fabric_id():
                continue
            if lsan_deviceObj.peek_device_status() is not None and\
               lsan_deviceObj.peek_device_status() !=\
               objlist[i].peek_device_status():
                continue
            if lsan_deviceObj.peek_proxy_pid() is not None and\
               lsan_deviceObj.peek_proxy_pid() !=\
               objlist[i].peek_proxy_pid():
                continue
            if lsan_deviceObj.peek_device_wwn() is not None and\
               lsan_deviceObj.peek_device_wwn() !=\
               objlist[i].peek_device_wwn():
                continue
            if lsan_deviceObj.peek_imported_fabric_id() is not None and\
               lsan_deviceObj.peek_imported_fabric_id() !=\
               objlist[i].peek_imported_fabric_id():
                continue
            lsan_devicelist.append(objlist[i])
    else:
        print(objlist)
    return lsan_devicelist


def show_lsan_device(session, physical_pid=None, source_fabric_id=None,
                     device_status=None, proxy_pid=None, device_wwn=None,
                     imported_fabric_id=None):
    lsan_deviceObj = lsan_device()
    lsan_deviceObj.set_physical_pid(physical_pid)
    lsan_deviceObj.set_source_fabric_id(source_fabric_id)
    lsan_deviceObj.set_device_status(device_status)
    lsan_deviceObj.set_proxy_pid(proxy_pid)
    lsan_deviceObj.set_device_wwn(device_wwn)
    lsan_deviceObj.set_imported_fabric_id(imported_fabric_id)
    return _show_lsan_device(session, lsan_deviceObj)


def validate(lsan_deviceObj):
    if lsan_deviceObj.peek_physical_pid() is None or\
       lsan_deviceObj.peek_source_fabric_id() is None or\
       lsan_deviceObj.peek_device_status() is None or\
       lsan_deviceObj.peek_proxy_pid() is None or\
       lsan_deviceObj.peek_device_wwn() is None or\
       lsan_deviceObj.peek_imported_fabric_id() is None:
        return 0
    return 0


def main(argv):
    filters = []
    inputs = brcd_util.parse(argv, lsan_device, filters, validate)
    session = brcd_util.getsession(inputs)
    result = _show_lsan_device(session, inputs['utilobject'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
