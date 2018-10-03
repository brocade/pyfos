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

:mod:`configure_fabric_modify` - PyFos util for configuring fabric parameters.
***********************************************************************************
The :mod:`configure_fabric_modify` It provides update for fabric configuration.

This module is a standalone script that can be used to update the fabric \
attributes of the switch.

* Infrastructure options:
    * -i,--ipaddr=IPADDR: IP address of FOS switch.
    * -L,--login=LOGIN: login name.
    * -P,--password=PASSWORD: password.
    * -f,--vfid=VFID: VFID to which the request is directed to.
    * -s,--secured=MODE: HTTPS mode "self" or "CA"[OPTIONAL].
    * -v,--verbose: verbose mode[OPTIONAL].

* Util scripts options:
    * --insistent-domain-id-enabled=INSISTENT-DOMAIN-ID-ENABLED: set the\
           fabric to insistent domain mode.

* outputs:
    * Python dictionary content with RESTCONF response data

..function:: set_fabric_configure(session, idid_mode)

    Example usage of the method::

        ret = configure_fabric_modify.set_fabric_configuration(session,
                idid_mode)
        print (ret)

    Details::

        result = configure_fabric_modify.set_fabric_configuration(session,
                 idid_mode)

    * inputs:
        :param session: session returned by login
        :param idid_mode: Configure insistent domain mode.

    * outputs:
        :rtype: dictionary of return status matching rest response

    *use cases*

        1. Patch the fabric configuration parameters of switch.

"""

import pyfos.pyfos_auth as pyfos_auth
import pyfos.pyfos_util as pyfos_util
import sys
import pyfos.utils.brcd_util as brcd_util
from pyfos.pyfos_brocade_fibrechannel_configuration import fabric


def _set_fabric_configuration(session, fabric_configuration_object):
    # Set parameters
    result = fabric_configuration_object.patch(session)
    return result


def _validate_fabric_configuration(fabric_configuration_object):
    # Get parameters
    idid_mode = fabric_configuration_object.peek_insistent_domain_id_enabled()

    # Verify parameters
    if idid_mode is None:
        print("Missing required option 'insistent-domain-id-enabled'")
        return 1

    # Success
    return 0


def set_fabric_configuration(session, idid_mode):
    # Set parameters
    value_dict = {'insistent-domain-id-enabled': idid_mode}
    fabric_configuration_object = fabric(value_dict)

    # Validate paramaters
    rc = _validate_fabric_configuration(fabric_configuration_object)
    if rc == 1:
        # Failed validation
        return None

    # Set idid mode
    result = _set_fabric_configuration(session, fabric_configuration_object)
    return result


def main(argv):
    # Parse inputs
    filters = ["insistent_domain_id_enabled"]
    inputs = brcd_util.parse(argv, fabric, filters,
                             _validate_fabric_configuration)

    # Get object
    fabric_configuration_object = inputs['utilobject']

    # Get session
    session = brcd_util.getsession(inputs)

    # Call function
    result = _set_fabric_configuration(session, fabric_configuration_object)
    if result is None:
        print(inputs['utilusage'])
        sys.exit(1)

    # Print response
    pyfos_util.response_print(result)

    # Log out
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
