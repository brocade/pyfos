#!/usr/bin/env python3

# Copyright 2018 Brocade Communications Systems LLC.  All rights reserved.
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

:mod:`configure_port_name_set` - PyFos util to set the port name mode of the \
switch.
*****************************************************************************\
********
The :mod:`configure_port_name_set` sets the port name mode of the switch.

This module is a stand-alone script that can be used to set the port name mode
of the switch. If the mode is "dynamic", the dynamic port name format can be
set as well.

* Infrastructure Options:
    * -i,--ipaddr=IPADDR: The IP address of the FOS switch.
    * -L,--login=LOGIN: The login name.
    * -P,--password=PASSWORD: The password.
    * -f,--vfid=VFID: The VFID to which the request is directed.
    * -s,--secured=MODE: The HTTPS mode "self" or "CA" [OPTIONAL].
    * -v,--verbose: Verbose mode [OPTIONAL].

* Util Script Options:
    * --portname-mode=PORTNAME-MODE: Sets the given port name mode.
    * --dynamic-portname-format=DYNAMIC-PORTNAME-FORMAT: Sets the dynamic \
port name format [OPTIONAL].

* Output:
    * Python dictionary content with RESTCONF response data.

..function:: set_port_name_mode(session, portname_mode,
                                dynamic_portname_format=None)

    Example Usage of the Method::

        ret = configure_port_name_set.set_port_name_mode(session,
                portname_mode, dynamic_portname_format)
        print (ret)

    Details::

        result = configure_port_name_set.set_port_name_mode(session, mode,
                dynamic_format)

    * Input:
        :param session: The session returned by login.
        :param portname_mode: Sets the port name mode.
        :param dynamic_portname_format: Sets the dynamic port name format,
                 if dynamic mode is specified.

    * Output:
        :rtype: A dictionary of return status matching the REST response.

    *Use Cases*

    1. Patch the port name configuration of the switch.

"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.utils import brcd_util
from pyfos.pyfos_brocade_fibrechannel_configuration import port_configuration


def _set_port_name_mode(session, port_configuration_object):
    # Set parameters
    result = port_configuration_object.patch(session)
    return result


def _validate_port_name_mode(port_configuration_object):
    # Get parameters
    portname_mode = port_configuration_object.peek_portname_mode()
    dynamic_portname_format = port_configuration_object.\
        peek_dynamic_portname_format()

    # Verify parameters
    if portname_mode is None:
        print("Missing required option 'portname-mode'")
        return 1
    if portname_mode not in 'dynamic' and dynamic_portname_format is not None:
        print("'dynamic-portname-format' is invalid when port name mode is "
              "not 'dynamic'")
        return 1

    # Success
    return 0


def set_port_name_mode(session, portname_mode, dynamic_portname_format=None):
    # Set parameters
    value_dict = {'portname-mode': portname_mode, 'dynamic-portname-format':
                  dynamic_portname_format}
    port_configuration_object = port_configuration(value_dict)

    # Validate paramters
    rc = _validate_port_name_mode(port_configuration_object)
    if rc == 1:
        # Failed validation
        return None

    # Set portname mode
    result = _set_port_name_mode(session, port_configuration_object)
    return result


def main(argv):
    # Parse inputs
    filters = ["portname_mode", "dynamic_portname_format"]
    inputs = brcd_util.parse(argv, port_configuration, filters,
                             _validate_port_name_mode)

    # Get object
    port_configuration_object = inputs['utilobject']

    # Get session
    session = brcd_util.getsession(inputs)

    # Call function
    result = _set_port_name_mode(session, port_configuration_object)
    if result is None:
        print(inputs['utilusage'])
        sys.exit(1)

    # Print response
    pyfos_util.response_print(result)

    # Log out
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
