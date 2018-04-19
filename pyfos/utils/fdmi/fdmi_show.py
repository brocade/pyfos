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

This module is a stand-alone script and API that can be used to display
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
    * --hba-id=<HBAID>: HBA ID.

* Outputs:
    * Python dictionary of FDMI HBA entries and Python dictionary of
        FDMI HBA port entries.

"""

import pyfos.pyfos_auth as pyfos_auth
import pyfos.pyfos_brocade_fdmi as pyfos_fdmi
import pyfos.pyfos_util as pyfos_util
import sys
import pyfos.utils.brcd_util as brcd_util


def fdmishow(session, hba_id):
    
    # Get HBA attributes
    hba_attributes = pyfos_fdmi.hba.get(session, hba_id)
    pyfos_util.response_print(hba_attributes)

    # Sort port attributes if HBA ID specified
    if hba_id is not None:
        hba_ports = []

        # Get port attributes
        port_attributes = pyfos_fdmi.port.get(session, None)

        # Iterate through port entries
        for port_entry in port_attributes:
            # Check if same HBA ID
            if hba_id == port_entry.peek_hba_id():
                # Add port entry to list
                hba_ports.append(port_entry)

        # Print HBA port attributes
        pyfos_util.response_print(hba_ports)
    else:
        # Print all HBA port attributes
        port_attributes = pyfos_fdmi.port.get(session, None)
        pyfos_util.response_print(port_attributes)


def main(argv):
    # Parse input arguments
    filters = ['hba_id']
    inputs = brcd_util.parse(argv, pyfos_fdmi.hba, filters)

    # Get session
    session = brcd_util.getsession(inputs)

    # Get hba-id, if provided
    hba_id = inputs['utilobject'].peek_hba_id()

    # Print FDMI properties
    fdmishow(session, hba_id)

    # Logout
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
