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

:mod:`zoning_object_expunge` - PyFOS util used for expunging a zone object.
*******************************************************************************
The :mod:`zoning_object_expunge` PyFOS util is used to expunge a zone object.

Use this utility to expunge a zone object from the zone database.  In addition
to deleting the specified object, this will also remove the object from the
member lists of all other objects.  After successful execution, the specified
object will no longer exist in the defined configuration.  You can use this
utility for all zone object types including cfgs, zones, aliases, WWN members,
and D,I members.  Members of Target Peer Zones are not allowed to be expunged.

This utility changes the defined configuration.  After successful completion
of the expunge operation, this utility will automatically save the changes to
nonvolatile memory (similar to the 'cfgSave' CLI).  If for some reason the
save operation fails, the expunge operation will be undone by way of a
transaction abort operation.

If the expunge operation results in editing the defined configuration version
of the current effective configuration, upon successful completion of the
expunge and implicit save operation, the defined and effective configurations
will be mismatched which can result in undesired behavior.  In this case, it
is highly recommended to enable the configuration with the
:mod:`zoning_cfg_enable` PyFOS utility.

.. note::
    If the object being expunged is the only member of a zone object, the
    parent object is also deleted.  If the parent object that is implicitly
    deleted happens to also be the enabled zone configuration, the implicit
    save operation which is performed after expunge will fail.  In this case,
    users should first either enable a different configuration with the
    :mod:`zoning_cfg_enable` PyFOS utility, or disable the current enabled
    configuration using the :mod:`zoning_cfg_disable` PyFOS utility and retry
    the expunge utility.

* Input:

* Infrastructure Options:
    * -i,--ipaddr=IPADDR: The IP address of the FOS switch.
    * -L,--login=LOGIN: The login name.
    * -P,--password=PASSWORD: The password.
    * -f,--vfid=VFID: The VFID to which the request is directed.
    * -s,--secured=MODE: The HTTPS mode "self" or "CA" [Optional].
    * -v,--verbose: Verbose mode [Optional].
    * -a,--authtoken: AuthToken value or AuthTokenManager config\
    file[OPTIONAL].
    * -z,--nosession: Sessionless authentication based login[OPTIONAL].
    * --nocredential: No credential to be sent in the request[OPTIONAL].

* Util Script Options:
    * --zone-object: Name of the object to be expunged.

* Output:
    * Status of the expunge operation.

"""


# Start utils imports
import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_operation_zone import zone_operation_parameters

import pyfos.pyfos_brocade_zone as pyfos_zone
from pyfos.utils import brcd_util
import pyfos.utils.zoning.zoning_cfg_save as cfgsave
import pyfos.utils.zoning.zoning_cfg_abort as cfgabort
# End module imports


def _do_zone_object_expunge(session, zone_operation_parametersObj):
    return zone_operation_parametersObj.post(session)


def do_zone_object_expunge(session, zone_operation_parametersObj):
    # Hard code the 'action' leaf to 'expunge'
    action_str = "expunge"
    zone_operation_parametersObj.set_action(action_str)

    # Issue the POST request
    return _do_zone_object_expunge(session, zone_operation_parametersObj)


def validate(zone_operation_parametersObj):
    if zone_operation_parametersObj.peek_zone_object() is None:
        return 1
    return 0


def usage():
    print("  Script specific options:")
    print("")
    print("    --zone-object: Name of the object to be expunged.")
    print("")


def main(argv):
    filters = ["zone_object"]
    inputs = brcd_util.parse(argv, zone_operation_parameters, filters,
                             validate)
    session = brcd_util.getsession(inputs)

    # Store the checksum before editing the zoneDB to use for the
    #  cfgsave at the end
    current_effective = pyfos_zone.effective_configuration.get(session)

    result = do_zone_object_expunge(session, inputs['utilobject'])
    pyfos_util.response_print(result)

    # If the expunge operation succeeds, perform an implicit cfgsave
    # If the expunge operation fails, it should get automatically aborted
    # in the FOS Zone module, so no need to abort the transaction.
    if pyfos_util.is_success_resp(result):
        result = cfgsave.cfgsave(session, current_effective.peek_checksum())

        # If the save operation fails, check to see if there is an open
        #  transaction. If there is, then abort the transaction
        if pyfos_util.is_failed_resp(result):
            print("Expunge succeeded, but the cfgSave failed.")
            current_effective = pyfos_zone.effective_configuration.get(session)
            if current_effective.peek_transaction_token() != 0:
                pyfos_util.response_print(result)
                print("\nAborting the transaction.")
                result = cfgabort.cfgabort(session)
                pyfos_util.response_print(result)

    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
