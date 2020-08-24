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

:mod:`configure_chassis_modify` - PyFOS util for configuring fabric parameters.
*******************************************************************************
The :mod:`configure_chassis_modify` util provides updates for the\
 fabric configuration.

This module is a stand-alone script that can be used to update the fabric \
attributes of the switch.

* Infrastructure Options:
    * -i,--ipaddr=IPADDR: The IP address of the FOS switch.
    * -L,--login=LOGIN: The login name.
    * -P,--password=PASSWORD: The password.
    * -f,--vfid=VFID: The VFID to which the request is directed.
    * -s,--secured=MODE: The HTTPS mode "self" or "CA" [OPTIONAL].
    * -v,--verbose: Verbose mode [OPTIONAL].

* Util Script Options:

    *--firmware-synchronization-enabled=FIRM-SYNC-ENABLE	Sets the Firmware \
                                                                Syncing
    *--http-session-ttl=HTTP-SES-TTL				Sets Timeout value.
    *--ezserver-enabled=EZSERV-ENABLE				Sets EZSERVER enabling.

* Output:
    *Python dictionary content with RESTCONF response data.

..function:: set_chassis_configuration(session, sync_enable,
                         http_ses_ttl, ezserver_en)

    Example Usage of the Method::

        ret = configure_fabric_modify.set_fabric_configuration(session,
             sync_enable, http_ses_ttl, ezserver_en)
        print (ret)

    Details::

        result = configure_fabric_modify.set_fabric_configuration(session,
                sync_enable, http_ses_ttl, ezserver_en)

    * Input:
        :param sync_enable: Enables or disables Firmware \
                                synchronization.
        :param http_ses_ttl: Denotes timeout value for BNA, \
                                SANNav, REST and PYfos in Seconds.
        :param ezserver_en: Enables or disables EZserver configuration. \

    * Output:
        :rtype: A dictionary of return status matching the REST response.

    *Use Cases*

        1. Patch the fabric configuration parameters of a switch.

"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.utils import brcd_util
from pyfos.pyfos_brocade_fibrechannel_configuration \
    import chassis_config_settings


def _set_chassis_configuration(session, chassis_configuration_object):
    # Set parameters
    result = chassis_configuration_object.patch(session)
    return result


def _validate_chassis_configuration(chassis_configuration_object):
    flag = 0
    # Get parameters
    if chassis_configuration_object.peek_firmware_synchronization_enabled() \
       is not None:
        flag = flag + 1
    if chassis_configuration_object.peek_http_session_ttl() \
       is not None:
        flag = flag + 1
    if chassis_configuration_object.peek_ezserver_enabled() is not None:
        flag = flag + 1

    # Success
    return 0 if flag >= 1 else 1


def set_chassis_configuration(session, sync_enable, http_ses_ttl, ezserver_en):
    # Set parameters
    value_dict = {'firmware-synchronization-enabled': sync_enable,
                  'http-session-ttl': http_ses_ttl,
                  'ezserver-enabled': ezserver_en}
    chassis_configuration_object = chassis_config_settings(value_dict)

    # Validate paramaters
    rc = _validate_chassis_configuration(chassis_configuration_object)
    if rc == 1:
        # Failed validation
        return None

    # Set idid mode
    result = _set_chassis_configuration(session, chassis_configuration_object)
    return result


def main(argv):
    # Parse inputs
    filters = ["firmware_synchronization_enabled",
               "http_session_ttl",
               "ezserver_enabled"]
    inputs = brcd_util.parse(argv, chassis_config_settings, filters,
                             _validate_chassis_configuration)

    # Get object
    chassis_configuration_object = inputs['utilobject']

    # Get session
    session = brcd_util.getsession(inputs)

    # Call function
    result = _set_chassis_configuration(session, chassis_configuration_object)
    if result is None:
        print(inputs['utilusage'])
        sys.exit(1)

    # Print response
    pyfos_util.response_print(result)

    # Log out
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
