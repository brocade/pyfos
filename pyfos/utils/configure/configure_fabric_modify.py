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

:mod:`configure_fabric_modify` - PyFOS util for configuring fabric parameters.
*******************************************************************************
The :mod:`configure_fabric_modify` util provides updates for the\
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
    * --insistent-domain-id-enabled=INSISTENT-DOMAIN-ID-ENABLED: Sets the\
           fabric to insistent domain mode.
    * --principal-selection-enabled=PRINCIPAL-SELECTION-ENABLED Enables or\
      disables principal  switch  selection.  true     : Enables principal\
      switch selection mode.  false    : Disables principal switch selection\
      mode.
    * --principal-priority=PRINCIPAL-PRIORITY Sets  the  principal  selection \
      priority  of  the switch. Not  all of these values can be assigned.\
      This mechanism provide a preference for a switch requesting to be the\
      principal switch in a fabric, but they do not provide an absolute\
      guarantee that a switch requesting to be the principal switch is\
      granted this status.  0x01     Highest and default priority (if\
      priority nt given).  0x02     Should be avoided as this is internal\
      priority          given during fabric rebuild.  0x03-    Priority \
      value range. Higher  numbers 0xFE     mean lower priority.  0xFF    \
      Switch  is not capable of acting as a principal          switch.


* Output:
    * Python dictionary content with RESTCONF response data.

..function:: set_fabric_configure(session, idid_mode,
             princ_sel_mode, princ_pri)

    Example Usage of the Method::

        ret = configure_fabric_modify.set_fabric_configuration(session,
                idid_mode, princ_sel_mode, princ_pri)
        print (ret)

    Details::

        result = configure_fabric_modify.set_fabric_configuration(session,
                 idid_mode, princ_sel_mode, princ_pri)

    * Input:
        :param session: The session returned by login.
        :param idid_mode: Configures the insistent domain mode.
        :param princ_sel_mode: Enables or disables principal \
                                            switch  selection.
        :param princ_pri: Sets  the  principal  selection \
                                   priority  of  the switch.

    * Output:
        :rtype: A dictionary of return status matching the REST response.

    *Use Cases*

        1. Patch the fabric configuration parameters of a switch.

"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.utils import brcd_util
from pyfos.pyfos_brocade_fibrechannel_configuration import fabric


def _set_fabric_configuration(session, fabric_configuration_object):
    # Set parameters
    result = fabric_configuration_object.patch(session)
    return result


def _validate_fabric_configuration(fabric_configuration_object):
    flag = 0
    # Get parameters
    if fabric_configuration_object.peek_insistent_domain_id_enabled() \
       is not None:
        flag = flag + 1
    if fabric_configuration_object.peek_principal_selection_enabled() \
       is not None:
        flag = flag + 1
    if fabric_configuration_object.peek_principal_priority() is not None:
        flag = flag + 1

    # Success
    return 0 if flag >= 1 else 1


def set_fabric_configuration(session, idid_mode, princ_sel_mode, princ_pri):
    # Set parameters
    value_dict = {'insistent-domain-id-enabled': idid_mode,
                  'principal-selection-enabled': princ_sel_mode,
                  'principal-priority': princ_pri}
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
    filters = ["insistent_domain_id_enabled",
               "principal_selection_enabled",
               "principal_priority"]
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
