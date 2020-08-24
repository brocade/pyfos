#!/usr/bin/env python3

# Copyright © 2018 Broadcom. All Rights Reserved. The term “Broadcom” refers to
# Broadcom Inc. and/or its subsidiaries.
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

:mod:`fdmi_show` - PyFOS util to show FMDI entries.
***********************************************************************************
The :mod:`fdmi_show` supports 'fdmishow' CLI use case.

This module is a standalone script and API that can be used to display
all FDMI HBA and port entries. If an HBA ID is specified, only the entries
corresponding to that HBA will be displayed.

* Inputs:
    * -L=<login>: Login ID. If not provided, an interactive
        prompt will request one.
    * -P=<password>: Password. If not provided, an interactive
        prompt will request one.
    * -i=<IP address>: IP address.
    * -f=<VFID>: VFID or -1 if VF is disabled. If unspecified,
        a VFID of 128 is assumed.
    * --hbaid=<HBAID>: HBA ID.

* Outputs:
    * Python dictionary of FDMI HBA entries and Python dictionary of
        FDMI HBA port entries.

"""

import sys
from pyfos import pyfos_auth
import pyfos.pyfos_brocade_fdmi as pyfos_fdmi
from pyfos import pyfos_util
from pyfos.utils import brcd_util


def usage():
    print("  Script specific options:")
    print("")
    print("    --hbaid=HBAID                HBA ID. [OPTIONAL]")
    print("")


def fdmishow(session, inputs):
    # Get HBA ID, if provided
    if "hbaid" not in inputs:
        hba = None
    else:
        hba = inputs["hbaid"]

    # Get HBA attributes
    hba_attributes = pyfos_fdmi.hba.get(session, hba)
    pyfos_util.response_print(hba_attributes)

    # Sort port attributes if HBA ID specified
    if hba is not None:
        # Only print ports if HBA is valid
        if not pyfos_util.is_failed_resp(hba_attributes):
            # Create list of ports associated with specified HBA
            hba_ports = []

            # Get port attributes
            port_attributes = pyfos_fdmi.port.get(session, None)

            # Check if multiple port entries
            if isinstance(port_attributes, list):
                # Iterate through port entries
                for port_entry in port_attributes:
                    # Check if same HBA ID
                    if hba == port_entry.peek_hba_id():
                        # Add port entry to list
                        hba_ports.append(port_entry)
            else:
                if hba == port_attributes.peek_hba_id():
                    # Add port entry to list
                    hba_ports.append(port_attributes)

            # Print HBA port attributes
            pyfos_util.response_print(hba_ports)
    else:
        # Print all HBA port attributes
        port_attributes = pyfos_fdmi.port.get(session, None)
        pyfos_util.response_print(port_attributes)


def main(argv):
    valid_options = ["hbaid"]
    inputs = brcd_util.generic_input(argv, usage, valid_options)

    session = brcd_util.getsession(inputs)

    # Set VF ID, if necessary
    vfid = None
    if 'vfid' in inputs:
        vfid = inputs['vfid']
    if vfid is not None:
        pyfos_auth.vfid_set(session, vfid)

    # Call fdmishow
    fdmishow(session, inputs)

    # Log out
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
