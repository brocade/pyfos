#!/usr/bin/env python3

# Copyright © 2018 Broadcom. All rights reserved. The term "Broadcom"
# refers to Broadcom Inc. and/or its subsidiaries.
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

:mod:`switch_config_dump` - PyFOS util to dump existing switch configuration.
***********************************************************************************
The :mod:`switch_config_dump` PyFOS util to dump existing switch configuration.

This module is a stand-alone script that can be used to dump spreadsheet
or JSON encoded switch configuration details into a timestamped file. The
resulting configuration files can be used for monitoring drift in configs
and/or revert the drifts in config by applying of older configs to a switch.

* Inputs:
    * -L=<login>: The login ID. If not provided, an interactive
        prompt will request one.
    * -P=<password>: The password. If not provided, an interactive
        prompt will request one.
    * -i=<IP address>:The IP address.
    * --json: Use JSON Format,The default is XLSX format. [Optional]

* Outputs:
    * Displays the dump file name

**Using switch_config_dump**:

    1.  File Name Format.
        The dump configuration file name follows the format:
        *FOS_<switch IP address>_<date>_<time stamp>_<vfid>.<format>*.
        For logical switch supported switches the configuration dump
        will be across multiple files each with a different **vfid** in the
        filename. For logical switch or VF not supported then
        the keyword **None** replaces the **vfid** .

        Example::

            FOS_10.155.107.42_2019_02_14_09_15_14_None.json

    2. File Type Formats.
        The configuration utility provides two file type formats supported
        for the config dump functionality *(XLSX and JSON)*. The default mode
        is *XLSX* and is implicit in the command line arguments. However for
        of *JSON* format you should explicitly pass **--json**. The dumped
        configuration file can be passed to the :mod:`switch_config_diff` and
        :mod:`switch_config_apply` utils for identifying the drifts and or
        reverting the drifted configurations.

        Example XLSX::

            switch_config_dump.py  -i 10.200.151.183 -L admin -P password

        Example JSON::

            switch_config_dump.py  -i 10.200.151.183 -L admin -P password
            --json

        Example Execution::

            python3.5 switch_config_dump.py -i 10.155.107.42 -L admin
            -P password --json
            Dump configuration Start
            Saving Dump file FOS_10.155.107.42_2019_02_18_01_30_55_None.json
            Dump configuration Completed
            done

**Assumptions**:

    1. The switch_config_dump contains only the read-write supported objects
       (that supports POST/PATCH/DELETE/PUT operations).
    2. The switch_config_dump of objects contains only config true attributes
       as per yang in the *XLSX* format. However in case of *JSON* all
       attributes are dumped.
    3. The filtering support for switch_config_dump is limited to the object
       level (filtering is supported at the top level container/list name). The
       filtering support is not extended to the individual attribute leaves.
    4. The complete list of objects available for configuration operations
       should be part of :mod:`pyfos_class_manager`. Please ensure the object
       is part of :py:obj:`pyfos.manager.pyfos_class_manager.clslist` before it
       can be used for configuration operation.


**Object Filtering Support**:

    The utils supports filtering (selectively using one or more objects for
    config dump, diff, apply sequence). Follow the procedure below to
    selectively apply the configuration operations.

    1. Create a file with the name *configfilters.json*.
    2. Add the container name for all objects to be used for configuration
       operation.
    3. Put the *configfilters.json* file in the execution directory. Otherwise,
       no user available CLI options are supported to pass this filename.
    4. If the **configfilter.json** file is empty then all objects in the
       :mod:`pyfos_class_manager` list are used for configuration operation.
    5. If the **configfilter.json** file is not empty, only the objects in
       the filters file are used for configuration operation.

    Example Content of the *configfilters.json* File::

        [
            "fibrechannel-switch",
            "extesnion-tunnel"
        ]

**Switch Configuration Object Dump XLSX**:

    1. Each object type is dumped in its own work sheet based on its container
       name. However it's also possible from the object dump infra to extend
       the dump of attributes of a container or list across multiple work
       sheets. Note that the same is not available as a user configurable
       option. The separation of attributes into multiple sheet makes it
       difficult to review them and is not used in general unless we have
       complex object model which makes them suitable to be separated across
       multiple sheets (for example, sheet dump is only done for
       **defined-configuration**).
    2. Each object is dumped in the XLSX file in column based format i.e all
       the leaves of the object form a column entry in the XLSX, irrespective
       of the depth(i.e when inside container or nested container/list).
    3. The dump only contains the *config true* attributes.
    4. All instances of the same type are dumped in their separate rows,
       without any empty rows between (all used columns of an object cannot
       be missing values fo all columns between subsequent instances).
    5. For list attributes the entries are captured in the subsequent
       below rows of the same column.
    6. Each attribute column name uses its unique attribute name. The unique
       attribute name is formed by concatenating the parent name with an
       underscore for any leaf attribute. Also all hyphens ’-’ are converted
       to underscore.
    7. An attribute dump of config true attributes follows rules below.

       * Yang Leaf Attributes:

          a. Each leaf attribute is represented as one column.
          b. A column-map is created for each attribute leaf internally.
          c. The leaf value corresponding to each leaf is dumped in it's
             respective column.

       * Yang List Attributes:

          a. Each leaf attribute is represented as one column.
          b. A column-map is created for each attribute leaf internally.
          c. The leaf value corresponding to each leaf is dumped in it's
             respective column.
          d. If there are more than one list element the values are dumped in
             the subsequent rows below.

       * Yang Container Attributes:

         a. There is no explicit dump for container attribute as the object
            is flattened as a leaf, list or leaflist and follows the above
            rules for dump.

**Switch Configuration Object Dump JSON**:
    For JSON dump all objects are dumped as a single list.

    Example ::

            {
                "fibrechannel": {
                    "auto-negotiate": "1",
                    "clean-address-enabled": "false",
                    "compression-active": "0",
                    "compression-configured": "0",
                    "credit-recovery-active": "0",
                    "credit-recovery-enabled": "0",
                    "congestion-signal-enabled": "true",
                    "d-port-enable": "0",
                    "default-index": "0",
                    "e-port-credit": "0",
                    "enabled-state": "6",
                    "f-port-buffers": "0",
                    "fault-delay-enabled": "0",
                    "fcid": "0",
                    "fcid-hex": "0x000000",
                    "fec-active": "0",
                    "fec-enabled": "1",
                    "is-enabled-state": "false",
                    "los-tov-mode-enabled": "0",
                    "max-speed": "16000000000",
                    "mirror-port-enabled": "0",
                    "n-port-enabled": "0",
                    "name": "0/0",
                    "npiv-enabled": "1",
                    "npiv-flogi-logout-enabled": "0",
                    "npiv-pp-limit": "128",
                    "operational-status": "3",
                    "persistent-disable": "0",
                    "physical-state": "no_light",
                    "pod-license-status": "true",
                    "port-autodisable-enabled": "0",
                    "port-type": "11",
                    "qos-enabled": "1",
                    "speed": "16000000000",
                    "target-driven-zoning-enable": "0",
                    "trunk-port-enabled": "1",
                    "user-friendly-name": "port0",
                    "via-tts-fec-enabled": "0",
                    "wwn": "20:00:00:27:f8:fd:1f:80"
                }
            "----------Truncated Lines above-------------"
            }, {
                "chassis": {
                    "chassis-user-friendly-name": "Brocade6505",
                    "chassis-wwn": "10:00:00:27:f8:fd:1f:8f",
                    "manufacturer": "Brocade Communications Systems LLC",
                    "max-blades-supported": "1",
                    "part-number": "40-1000737-03",
                    "product-name": "6505",
                    "serial-number": "CCD2506K018",
                    "vendor-part-number": "BROCAD0000650"
                }
            }]


"""

import sys
import time
from pyfos import pyfos_auth
from pyfos.manager.pyfos_config_manager import config_manager
from pyfos.utils import brcd_util


def get_envelope_name(ipaddr):
    return "FOS_" + ipaddr + "_" + time.strftime("%Y_%m_%d_%H_%M_%S")


def usage():
    print("  Script specific options:")
    print("")
    print("    --json                      ",
          "Use JSON format, Default is XLSX format. [Optional]")
    print("")


def main(argv):
    valid_options = ["json", "compare"]
    inputs = brcd_util.generic_input(argv, usage, valid_options)

    session = pyfos_auth.login(inputs["login"], inputs["password"],
                               inputs["ipaddr"], inputs["secured"],
                               verbose=inputs["verbose"])
    if pyfos_auth.is_failed_login(session):
        print("login failed because",
              session.get(pyfos_auth.CREDENTIAL_KEY)
              [pyfos_auth.LOGIN_ERROR_KEY])
        usage()
        sys.exit()

    brcd_util.exit_register(session)

    vfid = None
    if 'vfid' in inputs:
        vfid = inputs['vfid']

    if vfid is not None:
        pyfos_auth.vfid_set(session, vfid)

    in_json = False
    if 'json' in inputs:
        in_json = inputs['json']

    if in_json:
        fmtfile = 'JSON'
        fmtobj = 'json'
        ext = '.json'
    else:
        fmtfile = 'XLSX'
        fmtobj = 'attributes'
        ext = '.xlsx'
    envelope_name = get_envelope_name(inputs['ipaddr'])
    envelope_name += ext
    mgr = config_manager(fmtfile, fmtobj)
    mgr.dumptofile(session, envelope_name)
    print("done")

    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
