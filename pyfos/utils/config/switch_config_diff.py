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

:mod:`switch_config_diff` - PyFOS util to detect configuration drift from dump.
***********************************************************************************
The :mod:`switch_config_diff` PyFOS util to detect configuration drift from\
dump.

This module is a stand-alone script that is used to display the drifted
configurations in terms of different *config true* attributes of an object
instance compared to the corresponding instance from an existing dump file.
The drift is between the current switch configuration and a previously saved
dump configuration file.

The configuration files are saved by :mod:`switch_config_dump` script.

* Inputs:
    * -L=<login>: The login ID. If not provided, an interactive
        prompt will request one.
    * -P=<password>: The password. If not provided, an interactive
        prompt will request one.
    * -i=<IP address>: The IP address.
    * --compare=<compare dump file>: The name of the directory that
        contains the XLSX/JSON encoded switch configuration files with
        name of the file with or without a vfid in the dump filename in the
        format _<vfid>.<file extension>. If the vfid is specified, only that
        vfid is used; otherwise it detects all vfids for loading and
        drift detection for configuration operation.
    * --json: Use JSON format, The default is XLSX format. [Optional]

* Output:
    * Displays the list of attributes that have drifted.

**Assumptions**:

    1. The switch_config_dump contains only read-write supported objects
       (objects that supports **POST, PATCH, DELETE, PUT** operations).
       Therefore, the diff operation is supported for read-write objects.
    2. The switch_config_dump of objects contains only **config true**
       attributes as per yang in the *XLSX* format, but for *JSON* all
       attributes are dumped. However, in both the format types only
       **config true** attributes diff is displayed. This is because config
       false attributes are runtime stats/state values and are dependent on
       environment and are not supported for configuration operations.
    3. The filtering support for switch_config_diff is limited to the object
       level (filtering is supported at the top level container/list). The
       filtering support is not extended to the individual attribute leaves.
    4. The complete list of objects available for configuration operations
       should be part of :mod:`pyfos_class_manager`. Please ensure the object
       is part of :py:obj:`pyfos.manager.pyfos_class_manager.clslist` before
       it can be used for configuration operation.

**Object Filtering Support**:

    The diff util supports the object filtering (selectively using one or
    more objects for a config dump, diff, apply sequence). Follow the
    procedure below to selectively apply the configuration operations.

    1. Create a file with the name *configfilters.json*.
    2. Add the container name for all objects to be used for configuration
       operation.
    3. Put the *configfilters.json* file in the execution directory. Otherwise,
       no user available CLI options are supported to pass this filename.
    4. If the **configfilter.json** file is empty then all objects in the
       :mod: `pyfos_class_manager` list are used for configuration operation.
    5. If the **configfilter.json** file is not empty, only the objects in
       the filters file are used for configuration operation.

    Example Content of the *configfilters.json* File::

        [
            "fibrechannel-switch",
            "extesnion-tunnel"
        ]

**Using the switch_config_diff utility**:

    1. Collect the dump from the switch.
        To use the switch_config_diff functionality, you should already
        have a known dump file with the configuration from the switch.
        Please check the util :mod:`switch_config_dump` for steps to
        collect the configuration dump from the switch.

    2. File name format for diff.
        The dump configuration file name follows the format:
        *FOS_<switch IP address>_<date>_<time stamp>_<vfid>.<format>*.
        For logical switch supported switches, the configuration dump
        will be across multiple files each with a different **vfid** in the
        filename. For logical switch or VF not supported the keyword
        **None** replaces the **vfid**. However, to pass multiple filename
        for diff functionality the **vfid** should be skipped when providing
        the filename if you want to run it across multiple vfids.

        Example::

            Dump filename :FOS_10.155.107.42_2019_02_14_09_15_14_None.json
            Diff filename :FOS_10.155.107.42_2019_02_14_09_15_14.json

    3. File Type Formats.
        The configuration utility provides two file type formats supported
        for the config diff functionality (*XLSX* and *JSON*). The default
        mode is *XLSX* and is implicit in the command line arguments. However
        for *JSON* format you should explicitly pass **--json**.

        Similar to :mod:`switch_config_diff` there is another
        utility :mod:`switch_config_apply` which can do a diff and even revert
        from drifted configuration on a switch.

        Example XLSX::

            switch_config_diff.py  -i 10.200.151.183 -L admin -P password
            --compare=FOS_10.155.107.42_2019_02_18_01_30_55.xlsx

        Example JSON::

            switch_config_diff.py  -i 10.200.151.183 -L admin -P password
            --json --compare=FOS_10.155.107.42_2019_02_18_01_30_55.json

        Example Execution::

            ./switch_config_diff.py  -i 10.155.107.42 -L admin -P password
            --json --compare=FOS_10.155.107.42_2019_02_14_09_15_14_None.json
            Handle Diff Start.
            Loading Dump configuration Start.
            Loading from file : FOS_10.155.107.42_2019_02_14_09_15_14_None.json
            Loading Dump configuration Complete.
            Loading Switch configuration Start[ None ].
            Loading Switch configuration Complete.
            Init Class Ordering.
            Calculating Diff Start
            Calculating Diff Complete.
            "------Colored------------"
               [
                   {
                       [
                           {
                               "fibrechannel-switch": {
                                   "name": "10:00:00:27:f8:fd:1f:80",
            < -                    "user-friendly-name": "EDGE"
            ---
            > +                    "user-friendly-name": "AG"
                               }
                           }
                       ]
                   }
               ]
            "------No Color------------"
               [
                   {
                       [
                           {
                               "fibrechannel-switch": {
                                   "name": "10:00:00:27:f8:fd:1f:80",
            < -                    "user-friendly-name": "EDGE"
            ---
            > +                    "user-friendly-name": "AG"
                               }
                           }
                       ]
                   }
               ]


**Working Of switch_config_diff**:

    1. The switch_config_diff is based on the principle that only if config
       true attributes are different then there is a diff. The steps involved
       in the diff calculation process are as follows.

        * Find all instances that are missing in the dumped configurations and
          mark them for deletion.
        * Find all instances that are missing in the switch configurations and
          mark them for creations.
        * Find the matching old and new instances whose keys are the same
          for diff calculation.
        * Once the two instances are identified for diff calculation then
          they are used to calculate the diff between their attributes
          from top to bottom for config true attributes only.
        * Once the attributes are compared, their diff is marked at the
          attribute level and also at an object level using bitmasked
          flags along with a cached drifted value.
        * The type of diff identified can be easily mapped into
          different REST CRUD operations.
        * Once the diff has been completed the diff object can be
          used for generating diff corresponding payload itself based
          on different CRUD operations.
        * A single object can participate in multiple CRUD operations
          with different payload generation as per diff identifcation
          (for example`defined-configuration`).

    2. The display format for different diff identified are shown below.
       For leaf level only modification identified, the display of
       the restobject will only have its corresponding key values along with
       the diff modification identified for different attributes (leaf,list).
       However, in case of creation or deletion the corresponding object
       instance is missing in either the old list or the new list.
       Therefore in case of POST or DELETE operations identified by diff
       utility the complete object dump will be seen.

        Example Yang Leaf's Modification::

                {
                     "gigabitethernet": {
                         "name": "0/17",
            < -          "speed": "10000000000"
            ---
            > +          "speed": "1000000000"
                     }
                }

        Example Yang List Modification::

                {
                        "defined-configuration": {
                                "alias": [
                                        {
                                                "alias-name": "ali1_test",
                                                "member-entry": {
            < -                                     "alias-entry-name":
            < - "['70:00:8c:7c:ff:5f:54:00', '70:00:8c:7c:ff:5f:55:00']"
            ---
            > +                                     "alias-entry-name":
            > + "['70:00:8c:7c:ff:5f:54:00']"
                                                }
                                        }
                                ]
                        }
                }

        Example Yang List Creation::

                {
                        "defined-configuration": {
                                "alias": [
            > +                     {
            > +                             "alias-name": "ali1_test",
            > +                             "member-entry": {
            > +                                     "alias-entry-name": [
            > +                                      "70:00:8c:7c:ff:5f:54:00",
            > +                                      "70:00:8c:7c:ff:5f:55:00"
            > +                                     ]
            > +                             }
            > +                     },
                                ]
                        }
                }

        Example Diff Object Creation::

            > +        [
            > +            {
            > +                "extension-ip-route": {
            > +                    "dp-id": "0",
            > +                    "ip-address": "51.50.50.0",
            > +                    "ip-gateway": "10.200.14.18",
            > +                    "ip-prefix-length": "24",
            > +                    "name": "0/7"
            > +                }
            > +            }
            > +        ]

        Example Diff Object Deletion::

            < -            {
            < -                "n-port-map": {
            < -                    "configured-f-port-list": {
            < -                        "f-port": [
            < -                            "0/6",
            < -                            "0/7"
            < -                        ]
            < -                    },
            < -                    "failback-enabled": "1",
            < -                    "failover-enabled": "1",
            < -                    "n-port": "0/19",
            < -                    "online-status": "0",
            < -                    "reliable-status": "1"
            < -                }
            < -            },

"""

import sys
from pyfos import pyfos_auth
from pyfos.utils import brcd_util
from pyfos.manager.pyfos_config_manager import config_manager


def usage():
    print("  Script specific options:")
    print("")
    print("    --compare=PATH               Config dump file name")
    print("    --json                      ",
          "Use JSON format, Default is XLSX format. [Optional]")
    print("")


def main(argv):
    valid_options = ["json", "compare", "template", "reffcport"]
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

    if 'compare' not in inputs or inputs['compare'] is None:
        usage()
        sys.exit()

    envelope_name = inputs['compare']

    in_json = False
    if 'json' in inputs:
        in_json = inputs['json']

    # template = None
    # if 'template' in inputs:
    #    template = switch_config_util.get_template(inputs['template'])

    if in_json:
        fmtfile = 'JSON'
        fmtobj = 'json'
        # ext = '.json'
    else:
        fmtfile = 'XLSX'
        fmtobj = 'attributes'
        # ext = '.xlsx'
    mgr = config_manager(fmtfile, fmtobj)
    mgr.handlediff(envelope_name, session)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
