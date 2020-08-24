#!/usr/bin/env python3

# Copyright 2019 Broadcom. All rights reserved.
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

# sensor_show.py(pyGen v1.0.0)

"""

:mod:`sensor_show` - PyFOS util to show the details about sensors.
*********************************************************************
The :mod:`sensor_show` util displays the sensor details.

This module can be used to display the sensor information.

* Input:

| Infrastructure options:

|   -i,--ipaddr=IPADDR     The IP address of the FOS switch.
|   -L,--login=LOGIN       The login name.
|   -P,--password=PASSWORD The password.
|   -f,--vfid=VFID         The VFID to which the request is \
                            directed [OPTIONAL].
|   -s,--secured=MODE      The HTTPS mode "self" or "CA" [OPTIONAL].
|   -v,--verbose           Verbose mode [OPTIONAL].


|  Util Script Options:

   |   --id=id    Sets the sensor index.

* Output:
    * Sensor information. When the sensor index is not provided,
      all sensors will be displayed.

.. function:: sensor_id_show.show_sensor_id(session, id)

    * Displays the sensor details.

        Example Usage of the Method::

            # Example 1: Display all the sensors
            ret = sensor_id_show.show_sensor_id(session, None)
            print (ret)

            # Example 2: Display a specific sensor-id 1
            ret = sensor_id_show.show_sensor_id(session, 1)
            print (ret)

        Details::

            sensor_obj = sensor()
            if sensor-id is None: # All sensors
                result = sensor_obj.get(session, None)
            else:
                result = sensor_obj.get(session, id)

        * Input:
            :param session: The session returned by the login.
            :param id: The specific sensor or none for all sensors.

        * Output:
            :rtype: A dictionary of return status matching the REST response.

        *Use Cases*

        1. Retrieve the sensor information.
"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_fru import sensor
from pyfos.utils import brcd_util


def show_sensor_id(session, id):
    sensor_obj = sensor()
    if id is None:
        result = sensor_obj.get(session, None)
    else:
        result = sensor_obj.get(session, id)
    return result


def main(argv):

    # Print arguments
    # print(sys.argv[1:])

    filters = ['id']
    inputs = brcd_util.parse(argv, sensor, filters)

    sensor_obj = inputs['utilobject']

    session = brcd_util.getsession(inputs)

    # pyfos_util.response_print(inputs['utilobject'].displaycustomcli())
    result = show_sensor_id(inputs['session'], sensor_obj.peek_id())
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
