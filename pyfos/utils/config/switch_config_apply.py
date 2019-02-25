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

:mod:`switch_config_apply` - PyFOS util for applying configurations from dump.
***********************************************************************************
The :mod:`switch_config_apply` PyFOS util for applying configurations from\
dump.

This module is a stand-alone script that can be used to apply a previously
saved dump configuration file from the :mod:`switch_config_dump` to the switch.
The utility can identify the drifted configuration and revert to the same
configuration as the dump file by applying diff only configurations.
Users can opt to first review the drifted configuration by first passing
similar arguments to the :mod:`switch_config_diff` to verify the configuration
changes which are identified and the same would be used for reverting the
configuration.

* Input:
    * -L=<login>: The login ID. If not provided, an interactive
        prompt will request one.
    * -P=<password>:The password. If not provided, an interactive
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
    * A list of changed attributes, and switch_config_apply changes.

**Assumptions**:

    1. A switch_config_dump contains only the read-write supported objects
       (objects that supports **POST, PATCH, DELETE, PUT** operations).
       Therefore, the switch_config_appy operation is only supported for
       read-write objects. Since we cannot make changes to read-only object
       instances, we are not tracking those objects.
    2. A switch_config_dump of objects contains only **config true** attributes
       as per yang in the *XLSX* format, but for *JSON* all attributes
       are dumped. However, in both format types only **config true**
       attributes diff and apply sequence are executed. This is because config
       false attributes are runtime stats/state values and are dependent on
       environment and hence are not supported for configuration operations.
    3. The filtering support for the switch_config_apply is limited only to the
       object level (filtering is supported at the top level container/list).
       The filtering support is not extended to the individual attribute
       leaves.
    4. The complete list of objects available for configuration operations
       should be part of :mod:`pyfos_class_manager`. Please ensure the object
       is part of :py:obj:`pyfos.manager.pyfos_class_manager.clslist` before
       using ir for configuration operation.
    5. Not all the objects are supported for configuration operations. The
       applying of configuration is a complex functionality and requires
       multiple inputs such as sequencing and ordering across different
       objects. Also, there is special case handling with specific values
       and may be disruptive in nature.
    6. The :mod:`pyfos_class_manager` provides mechanism to segregate
       configurations operations across different stages along with priority
       for each module to determine ordering requirements. It supports
       customizations support for ordering in special cases for specific
       attribute values, including disruptive switch_config_apply handling.
       Note: For switch_config_apply handling, not all objects may be
       supported or tested.
    7. The :mod:`pyfos_rule_manager` has predefined rules for some of the
       common objects for configuration operations. An examples is
       saving the defined-configuration occurs after configuration
       operations. Based on new objects, there may be additions to
       the existing configurations for them.
    8. Please understand that not all switch_config_apply operations may be
       successful based on ordering, other requirements, interdependencies
       for untested scenario or objects. For error cases we may need to check
       the sequencing and ordering for them to work correctly.


**Object Filtering Support**:

    The switch_config_apply util supports the object filtering (selectively
    using one or more objects for a config dump, diff, apply sequence).
    Follow the below procedure for selectively applying the configurations.

    1. Create a file with the name *configfilters.json*.
    2. Add the container name for all objects to be used for configuration
       operations.
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

**Using the switch_config_apply util**:

    1. Collect the switch_config_dump from switch.
        To use the configuration apply functionality the user should already
        have a known dump file with the configuration from the switch. Please
        check the :mod:`switch_config_dump` util for steps to collect the
        configuration dump from the switch.

    2. File name format for apply.
        The dump configuration file name follows the format of
        *FOS_<switch IP address>_<date>_<time stamp>_<vfid>.<format>*.
        For logical switch supported switches the configuration dump
        will be across multiple files each with a different **vfid** in the
        filename. For logical switch or VF is not supported then  the
        keyword **None** replaces the **vfid**. However, to pass multiple
        file name for apply functionality, the **vfid** should be skipped
        when providing the filename if you want to run it across multiple
        vfids.

        Example::

            Dump filename :FOS_10.155.107.42_2019_02_14_09_15_14_None.json
            apply filename :FOS_10.155.107.42_2019_02_14_09_15_14.json

    3. File Type Formats.
        The configuraion utility provides two file type formats supported for
        the config apply functionality (*XLSX* and *JSON*). The default mode is
        *XLSX* and is implicit in the command line arguments. However, for
        of *JSON* format, you should explicitly pass **--json**.

        Similar to :mod:`switch_config_apply` there is another
        utility :mod:`switch_config_diff` which can do a diff and of
        the drifted configuration on a switch.

        Example XLSX::

            switch_config_apply.py  -i 10.155.107.42 -L admin -P password
            --compare=FOS_10.155.107.42_2019_02_18_01_30_55.xlsx

        Example json::

            switch_config_apply.py  -i 10.155.107.42 -L admin -P password
            --json --compare=FOS_10.155.107.42_2019_02_18_11_30_15.json


**Working of switch_config_apply**:
    1. Similar to :mod:`switch_config_diff` even :mod:`switch_config_apply`
       util identifies the drifted configuration before applying them for
       reverting the same.
    2. The utility interacts with the :mod:`pyfos_class_manager` to segregate
       the configuration drift changes into different configuration stages
       along with priority for the sequencing or ordering requirement for
       interdependencies. The segregated configuration across fid and
       different stages are managed by :mod:`pyfos_config_manager`.
    3. The utility interacts with the :mod:`pyfos_rule_manager` to apply the
       drifted configuration. It supports a set of predefined rules for
       switch_config_apply and handles scenarios where something needs to be
       done before or after the changes or otherwise skipped or their
       combinations.


**Example switch_config_apply**::

    switch_config_apply.py  -i 10.155.107.42 -L admin -P password
    --json --compare=FOS_10.200.151.183_2018_12_14_18_30_15_128.json

    Handle Diff Start.
    Loading Dump configuration Start.
    Loading from file : FOS_10.200.151.183_2018_12_14_18_30_15_128.json
    Loading objects fmt type: attributes
    Loading Dump configuration Complete.
    Loading Switch configuration Start[ 128 ].
    Loading Switch configuration Complete.
    Init Class Ordering.
    Calculating Diff Start
    Calculating Diff Complete.
       [
           {
               [
                   {
                       "fibrechannel": {
                           "name": "0/23",
    < -                    "npiv-enabled": "0"
    ---
    > +                    "npiv-enabled": "1"
                       }
                   }
               ]
           },
           {
               [
                   {
                       "defined-configuration": {
                           "alias": [
                               {
                                   "alias-name": "ali1_test",
                                   "member-entry": {
    < -                                "alias-entry-name": "
    ['70:00:8c:7c:ff:5f:54:00', '70:00:8c:7c:ff:5f:55:00',
    '80:00:8c:7c:ff:5f:55:00']"
    ---
    > +                                "alias-entry-name":
    "['70:00:8c:7c:ff:5f:54:00', '70:00:8c:7c:ff:5f:55:00']"
                                   }
                               }
                           ],
                           "zone": [
                               {
                                   "member-entry": {
    < -                                "entry-name":
    "['11:22:33:44:55:66:77:88']"
    ---
    > +                                "entry-name":
    "['11:22:33:44:55:66:77:88', '21:22:33:44:55:66:77:88']"
                                   },
                                   "zone-name": "zone1"
                               }
                           ]
                       }
                   }
               ]
           },
           {
    > +        [
    > +            {
    > +                "extension-circuit": {
    > +                    "admin-enabled": "1",
    > +                    "arl-algorithm-mode": "0",
    > +                    "circuit-id": "0",
    > +                    "failover-group-id": "0",
    > +                    "local-ip-address": "103.11.7.2",
    > +                    "maximum-communication-rate": "100000",
    > +                    "metric": "0",
    > +                    "minimum-communication-rate": "100000",
    > +                    "name": "0/24",
    > +                    "remote-ip-address": "102.10.2.2"
    > +                }
    > +            }
    > +        ]
           },
           {
    > +        [
    > +            {
    > +                "extension-tunnel": {
    > +                    "admin-enabled": "1",
    > +                    "compression-tunnel": "0",
    > +                    "fast-write-enabled": "0",
    > +                    "ficon": "0",
    > +                    "ip-extension": "0",
    > +                    "load-level": "Failover",
    > +                    "name": "0/24",
    > +                    "qos-ratio": {
    > +                        "distribution": "1",
    > +                        "fc-high-qos": "50",
    > +                        "fc-low-qos": "20",
    > +                        "fc-medium-qos": "30"
    > +                    },
    > +                    "tape-read": "0",
    > +                    "tape-write": "0"
    > +                }
    > +            },
    > +            {
    > +                "extension-tunnel": {
    > +                    "admin-enabled": "1",
    > +                    "compression-tunnel": "0",
    > +                    "fast-write-enabled": "0",
    > +                    "ficon": "0",
    > +                    "ip-extension": "0",
    > +                    "load-level": "Failover",
    > +                    "name": "0/34",
    > +                    "qos-ratio": {
    > +                        "distribution": "1",
    > +                        "fc-high-qos": "50",
    > +                        "fc-low-qos": "20",
    > +                        "fc-medium-qos": "30"
    > +                    },
    > +                    "tape-read": "0",
    > +                    "tape-write": "0"
    > +                }
    > +            }
    > +        ]
           },
           {
    > +        [
    > +            {
    > +                "extension-ip-route": {
    > +                    "dp-id": "0",
    > +                    "ip-address": "51.50.50.0",
    > +                    "ip-gateway": "*",
    > +                    "ip-prefix-length": "24",
    > +                    "name": "0/7"
    > +                }
    > +            }
    > +        ]
           },
           {
               [
                   {
                       "extension-ip-interface": {
                           "dp-id": "0",
                           "ip-address": "103.11.7.2",
                           "name": "0/7",
    < -                    "vlan-id": "200"
    ---
    > +                    "vlan-id": "0"
                       }
                   }
               ]
           },
           {
    > +        [
    > +            {
    > +                "extension-ip-interface": {
    > +                    "dp-id": "0",
    > +                    "ip-address": "51.50.50.10",
    > +                    "ip-prefix-length": "24",
    > +                    "mtu-size": "1500",
    > +                    "name": "0/7",
    > +                    "vlan-id": "0"
    > +                }
    > +            }
    > +        ]
           },
           {
               [
                   {
                       "gigabitethernet": {
                           "name": "0/17",
    < -                    "speed": "10000000000"
    ---
    > +                    "speed": "1000000000"
                       }
                   }
               ]
           },
           {
               [
                   {
                       "blade": {
    < -                    "extension-app-mode": "FCIP"
    ---
    > +                    "extension-app-mode": "hybrid"
                           "slot-number": "0"
                       }
                   }
               ]
           }
       ]

    Init Rule Manager.
    Apply Rule Manager.
    Execute  R3 <class 'pyfos.pyfos_brocade_zone.defined_configuration'>
    PATCH http://10.200.151.183/rest/running/zoning/defined-configuration?
    vf-id=128 - CONTENT ->
    <defined-configuration>
            <zone>
                    <zone-name>zone1</zone-name>
                    <member-entry>
                            <entry-name>11:22:33:44:55:66:77:88</entry-name>
                            <entry-name>21:22:33:44:55:66:77:88</entry-name>
                    </member-entry>
            </zone>
            <alias>
                    <alias-name>ali1_test</alias-name>
                    <member-entry>
                            <alias-entry-name>70:00:8c:7c:ff:5f:54:00
                            </alias-entry-name>
                            <alias-entry-name>70:00:8c:7c:ff:5f:55:00
                            </alias-entry-name>
                    </member-entry>
            </alias>
    </defined-configuration>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/zoning/effective-configuration?
    vf-id=128 - CONTENT ->
    <effective-configuration>
            <checksum>8da3d60cb0cfcc1500b514cedf6131f7</checksum>
            <cfg-action>1</cfg-action>
    </effective-configuration>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    Execute  R6 <class 'pyfos.pyfos_brocade_fibrechannel.fibrechannel'>
    PATCH http://10.200.151.183/rest/running/brocade-interface/fibrechannel?
    vf-id=128 - CONTENT ->
    <fibrechannel>
            <name>0/0</name>
            <enabled-state>6</enabled-state>
    </fibrechannel>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/fibrechannel?
    vf-id=128 - CONTENT ->
    <fibrechannel>
            <name>0/0</name>
            <speed>8000000000</speed>
            <npiv-enabled>1</npiv-enabled>
    </fibrechannel>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/fibrechannel?
    vf-id=128 - CONTENT ->
    <fibrechannel>
            <name>0/0</name>
            <enabled-state>2</enabled-state>
    </fibrechannel>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/fibrechannel?
    vf-id=128 - CONTENT ->
    <fibrechannel>
            <name>0/1</name>
            <enabled-state>6</enabled-state>
    </fibrechannel>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/fibrechannel?
    vf-id=128 - CONTENT ->
    <fibrechannel>
            <name>0/1</name>
            <speed>8000000000</speed>
            <npiv-enabled>1</npiv-enabled>
    </fibrechannel>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/fibrechannel?
    vf-id=128 - CONTENT ->
    <fibrechannel>
            <name>0/1</name>
            <enabled-state>2</enabled-state>
    </fibrechannel>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/fibrechannel?
    vf-id=128 - CONTENT ->
    <fibrechannel>
            <name>0/2</name>
            <enabled-state>6</enabled-state>
    </fibrechannel>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/fibrechannel?
    vf-id=128 - CONTENT ->
    <fibrechannel>
            <name>0/2</name>
            <npiv-enabled>1</npiv-enabled>
    </fibrechannel>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/fibrechannel?
    vf-id=128 - CONTENT ->
    <fibrechannel>
            <name>0/2</name>
            <enabled-state>2</enabled-state>
    </fibrechannel>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/fibrechannel?
    vf-id=128 - CONTENT ->
    <fibrechannel>
            <name>0/3</name>
            <enabled-state>6</enabled-state>
    </fibrechannel>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/fibrechannel?
    vf-id=128 - CONTENT ->
    <fibrechannel>
            <name>0/3</name>
            <npiv-enabled>1</npiv-enabled>
    </fibrechannel>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/fibrechannel?
    vf-id=128 - CONTENT ->
    <fibrechannel>
            <name>0/3</name>
            <enabled-state>2</enabled-state>
    </fibrechannel>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/fibrechannel?
    vf-id=128 - CONTENT ->
    <fibrechannel>
            <name>0/4</name>
            <enabled-state>6</enabled-state>
    </fibrechannel>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/fibrechannel?
    vf-id=128 - CONTENT ->
    <fibrechannel>
            <name>0/4</name>
            <npiv-enabled>1</npiv-enabled>
    </fibrechannel>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/fibrechannel?
    vf-id=128 - CONTENT ->
    <fibrechannel>
            <name>0/4</name>
            <enabled-state>2</enabled-state>
    </fibrechannel>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/fibrechannel?
    vf-id=128 - CONTENT ->
    <fibrechannel>
            <name>0/5</name>
            <enabled-state>6</enabled-state>
    </fibrechannel>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/fibrechannel?
    vf-id=128 - CONTENT ->
    <fibrechannel>
            <name>0/5</name>
            <npiv-enabled>1</npiv-enabled>
    </fibrechannel>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/fibrechannel?
    vf-id=128 - CONTENT ->
    <fibrechannel>
            <name>0/5</name>
            <enabled-state>2</enabled-state>
    </fibrechannel>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/fibrechannel?
    vf-id=128 - CONTENT ->
    <fibrechannel>
            <name>0/6</name>
            <enabled-state>6</enabled-state>
    </fibrechannel>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/fibrechannel?
    vf-id=128 - CONTENT ->
    <fibrechannel>
            <name>0/6</name>
            <npiv-enabled>1</npiv-enabled>
    </fibrechannel>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/fibrechannel?
    vf-id=128 - CONTENT ->
    <fibrechannel>
            <name>0/6</name>
            <enabled-state>2</enabled-state>
    </fibrechannel>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/fibrechannel?
    vf-id=128 - CONTENT ->
    <fibrechannel>
            <name>0/7</name>
            <enabled-state>6</enabled-state>
    </fibrechannel>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/fibrechannel?
    vf-id=128 - CONTENT ->
    <fibrechannel>
            <name>0/7</name>
            <npiv-enabled>1</npiv-enabled>
    </fibrechannel>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/fibrechannel?
    vf-id=128 - CONTENT ->
    <fibrechannel>
            <name>0/7</name>
            <enabled-state>2</enabled-state>
    </fibrechannel>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/fibrechannel?
    vf-id=128 - CONTENT ->
    <fibrechannel>
            <name>0/8</name>
            <enabled-state>6</enabled-state>
    </fibrechannel>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/fibrechannel?
    vf-id=128 - CONTENT ->
    <fibrechannel>
            <name>0/8</name>
            <npiv-enabled>1</npiv-enabled>
    </fibrechannel>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/fibrechannel?
    vf-id=128 - CONTENT ->
    <fibrechannel>
            <name>0/8</name>
            <enabled-state>2</enabled-state>
    </fibrechannel>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/fibrechannel?
    vf-id=128 - CONTENT ->
    <fibrechannel>
            <name>0/9</name>
            <enabled-state>6</enabled-state>
    </fibrechannel>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/fibrechannel?
    vf-id=128 - CONTENT ->
    <fibrechannel>
            <name>0/9</name>
            <npiv-enabled>1</npiv-enabled>
    </fibrechannel>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/fibrechannel?
    vf-id=128 - CONTENT ->
    <fibrechannel>
            <name>0/9</name>
            <enabled-state>2</enabled-state>
    </fibrechannel>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/fibrechannel?
    vf-id=128 - CONTENT ->
    <fibrechannel>
            <name>0/10</name>
            <enabled-state>6</enabled-state>
    </fibrechannel>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/fibrechannel?
    vf-id=128 - CONTENT ->
    <fibrechannel>
            <name>0/10</name>
            <npiv-enabled>1</npiv-enabled>
    </fibrechannel>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/fibrechannel?
    vf-id=128 - CONTENT ->
    <fibrechannel>
            <name>0/10</name>
            <enabled-state>2</enabled-state>
    </fibrechannel>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/fibrechannel?
    vf-id=128 - CONTENT ->
    <fibrechannel>
            <name>0/11</name>
            <enabled-state>6</enabled-state>
    </fibrechannel>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/fibrechannel?
    vf-id=128 - CONTENT ->
    <fibrechannel>
            <name>0/11</name>
            <npiv-enabled>1</npiv-enabled>
    </fibrechannel>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/fibrechannel?
    vf-id=128 - CONTENT ->
    <fibrechannel>
            <name>0/11</name>
            <enabled-state>2</enabled-state>
    </fibrechannel>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/fibrechannel?
    vf-id=128 - CONTENT ->
    <fibrechannel>
            <name>0/12</name>
            <enabled-state>6</enabled-state>
    </fibrechannel>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/fibrechannel?
    vf-id=128 - CONTENT ->
    <fibrechannel>
            <name>0/12</name>
            <npiv-enabled>1</npiv-enabled>
    </fibrechannel>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/fibrechannel?
    vf-id=128 - CONTENT ->
    <fibrechannel>
            <name>0/12</name>
            <enabled-state>2</enabled-state>
    </fibrechannel>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/fibrechannel?
    vf-id=128 - CONTENT ->
    <fibrechannel>
            <name>0/13</name>
            <enabled-state>6</enabled-state>
    </fibrechannel>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/fibrechannel?
    vf-id=128 - CONTENT ->
    <fibrechannel>
            <name>0/13</name>
            <npiv-enabled>1</npiv-enabled>
    </fibrechannel>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/fibrechannel?
    vf-id=128 - CONTENT ->
    <fibrechannel>
            <name>0/13</name>
            <enabled-state>2</enabled-state>
    </fibrechannel>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/fibrechannel?
    vf-id=128 - CONTENT ->
    <fibrechannel>
            <name>0/14</name>
            <enabled-state>6</enabled-state>
    </fibrechannel>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/fibrechannel?
    vf-id=128 - CONTENT ->
    <fibrechannel>
            <name>0/14</name>
            <npiv-enabled>1</npiv-enabled>
    </fibrechannel>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/fibrechannel?
    vf-id=128 - CONTENT ->
    <fibrechannel>
            <name>0/14</name>
            <enabled-state>2</enabled-state>
    </fibrechannel>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/fibrechannel?
    vf-id=128 - CONTENT ->
    <fibrechannel>
            <name>0/15</name>
            <enabled-state>6</enabled-state>
    </fibrechannel>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/fibrechannel?
    vf-id=128 - CONTENT ->
    <fibrechannel>
            <name>0/15</name>
            <npiv-enabled>1</npiv-enabled>
    </fibrechannel>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/fibrechannel?
    vf-id=128 - CONTENT ->
    <fibrechannel>
            <name>0/15</name>
            <enabled-state>2</enabled-state>
    </fibrechannel>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/fibrechannel?
    vf-id=128 - CONTENT ->
    <fibrechannel>
            <name>0/16</name>
            <enabled-state>6</enabled-state>
    </fibrechannel>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/fibrechannel?
    vf-id=128 - CONTENT ->
    <fibrechannel>
            <name>0/16</name>
            <npiv-enabled>1</npiv-enabled>
    </fibrechannel>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/fibrechannel?
    vf-id=128 - CONTENT ->
    <fibrechannel>
            <name>0/16</name>
            <enabled-state>2</enabled-state>
    </fibrechannel>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/fibrechannel?
    vf-id=128 - CONTENT ->
    <fibrechannel>
            <name>0/17</name>
            <enabled-state>6</enabled-state>
    </fibrechannel>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/fibrechannel?
    vf-id=128 - CONTENT ->
    <fibrechannel>
            <name>0/17</name>
            <npiv-enabled>1</npiv-enabled>
    </fibrechannel>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/fibrechannel?
    vf-id=128 - CONTENT ->
    <fibrechannel>
            <name>0/17</name>
            <enabled-state>2</enabled-state>
    </fibrechannel>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/fibrechannel?
    vf-id=128 - CONTENT ->
    <fibrechannel>
            <name>0/18</name>
            <enabled-state>6</enabled-state>
    </fibrechannel>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/fibrechannel?
    vf-id=128 - CONTENT ->
    <fibrechannel>
            <name>0/18</name>
            <npiv-enabled>1</npiv-enabled>
    </fibrechannel>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/fibrechannel?
    vf-id=128 - CONTENT ->
    <fibrechannel>
            <name>0/18</name>
            <enabled-state>2</enabled-state>
    </fibrechannel>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/fibrechannel?
    vf-id=128 - CONTENT ->
    <fibrechannel>
            <name>0/19</name>
            <enabled-state>6</enabled-state>
    </fibrechannel>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/fibrechannel?
    vf-id=128 - CONTENT ->
    <fibrechannel>
            <name>0/19</name>
            <npiv-enabled>1</npiv-enabled>
    </fibrechannel>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/fibrechannel?
    vf-id=128 - CONTENT ->
    <fibrechannel>
            <name>0/19</name>
            <enabled-state>2</enabled-state>
    </fibrechannel>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/fibrechannel?
    vf-id=128 - CONTENT ->
    <fibrechannel>
            <name>0/20</name>
            <enabled-state>6</enabled-state>
    </fibrechannel>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/fibrechannel?
    vf-id=128 - CONTENT ->
    <fibrechannel>
            <name>0/20</name>
            <npiv-enabled>1</npiv-enabled>
    </fibrechannel>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/fibrechannel?
    vf-id=128 - CONTENT ->
    <fibrechannel>
            <name>0/20</name>
            <enabled-state>2</enabled-state>
    </fibrechannel>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/fibrechannel?
    vf-id=128 - CONTENT ->
    <fibrechannel>
            <name>0/21</name>
            <enabled-state>6</enabled-state>
    </fibrechannel>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/fibrechannel?
    vf-id=128 - CONTENT ->
    <fibrechannel>
            <name>0/21</name>
            <npiv-enabled>1</npiv-enabled>
    </fibrechannel>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/fibrechannel?
    vf-id=128 - CONTENT ->
    <fibrechannel>
            <name>0/21</name>
            <enabled-state>2</enabled-state>
    </fibrechannel>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/fibrechannel?
    vf-id=128 - CONTENT ->
    <fibrechannel>
            <name>0/22</name>
            <enabled-state>6</enabled-state>
    </fibrechannel>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/fibrechannel?
    vf-id=128 - CONTENT ->
    <fibrechannel>
            <name>0/22</name>
            <compression-configured>1</compression-configured>
            <npiv-enabled>1</npiv-enabled>
    </fibrechannel>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/fibrechannel?
    vf-id=128 - CONTENT ->
    <fibrechannel>
            <name>0/22</name>
            <enabled-state>2</enabled-state>
    </fibrechannel>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/fibrechannel?
    vf-id=128 - CONTENT ->
    <fibrechannel>
            <name>0/23</name>
            <enabled-state>6</enabled-state>
    </fibrechannel>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/fibrechannel?
    vf-id=128 - CONTENT ->
    <fibrechannel>
            <name>0/23</name>
            <npiv-enabled>1</npiv-enabled>
    </fibrechannel>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/fibrechannel?
    vf-id=128 - CONTENT ->
    <fibrechannel>
            <name>0/23</name>
            <enabled-state>2</enabled-state>
    </fibrechannel>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    Execute  DEFPRE_PATCH <class 'pyfos.pyfos_brocade_fru.blade'>
    PATCH http://10.200.151.183/rest/running/brocade-fru/blade?
    vf-id=128 - CONTENT ->
    <blade>
            <slot-number>0</slot-number>
            <extension-app-mode>hybrid</extension-app-mode>
    </blade>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    Start sleep for [ 400 ]s.[ 10.200.151.183 ]
    End sleep of [ 400 ]s.[ 10.200.151.183 ]
    Dup Session start
    Start sleep for [ 20 ]s.[ 10.200.151.183 ]
    End sleep of [ 20 ]s.[ 10.200.151.183 ]
    Start sleep for [ 20 ]s.[ 10.200.151.183 ]
    End sleep of [ 20 ]s.[ 10.200.151.183 ]
    Start sleep for [ 20 ]s.[ 10.200.151.183 ]
    End sleep of [ 20 ]s.[ 10.200.151.183 ]
    Start sleep for [ 20 ]s.[ 10.200.151.183 ]
    End sleep of [ 20 ]s.[ 10.200.151.183 ]
    Start sleep for [ 20 ]s.[ 10.200.151.183 ]
    End sleep of [ 20 ]s.[ 10.200.151.183 ]
    Dup Session Completed after Iterations: 5
    Start sleep for [ 30 ]s.[ 10.200.151.183 ]
    End sleep of [ 30 ]s.[ 10.200.151.183 ]
    Execute  DEFPRE_PATCH <class
    'pyfos.pyfos_brocade_extension_ip_interface.extension_ip_interface'>
    PATCH http://10.200.151.183/rest/running/brocade-interface/
    extension-ip-interface?vf-id=128 - CONTENT ->
    <extension-ip-interface>
            <name>0/6</name>
            <ip-address>103.11.6.16</ip-address>
            <dp-id>0</dp-id>
            <mtu-size>9216</mtu-size>
            <vlan-id>200</vlan-id>
    </extension-ip-interface>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/
    extension-ip-interface?vf-id=128 - CONTENT ->
    <extension-ip-interface>
            <name>0/6</name>
            <ip-address>103.11.6.17</ip-address>
            <dp-id>0</dp-id>
            <mtu-size>9216</mtu-size>
    </extension-ip-interface>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/
    extension-ip-interface?vf-id=128 - CONTENT ->
    <extension-ip-interface>
            <name>0/7</name>
            <ip-address>103.11.7.2</ip-address>
            <dp-id>0</dp-id>
            <vlan-id>0</vlan-id>
    </extension-ip-interface>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    Execute  DEFPRE_PATCH <class
    'pyfos.pyfos_brocade_gigabitethernet.gigabitethernet'>
    PATCH http://10.200.151.183/rest/running/brocade-interface/
    gigabitethernet?vf-id=128 - CONTENT ->
    <gigabitethernet>
            <name>0/16</name>
            <speed>10000000000</speed>
    </gigabitethernet>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    PATCH http://10.200.151.183/rest/running/brocade-interface/
    gigabitethernet?vf-id=128 - CONTENT ->
    <gigabitethernet>
            <name>0/17</name>
            <speed>1000000000</speed>
    </gigabitethernet>
    {'success-code': 204, 'success-message': 'No Content',
    'success-type': 'Success'}
    Execute  DEFPOST <class
    'pyfos.pyfos_brocade_extension_ip_interface.extension_ip_interface'>
    POST http://10.200.151.183/rest/running/brocade-interface/
    extension-ip-interface?vf-id=128 - CONTENT ->
    <extension-ip-interface>
            <name>0/7</name>
            <ip-address>51.50.50.10</ip-address>
            <dp-id>0</dp-id>
            <ip-prefix-length>24</ip-prefix-length>
            <mtu-size>1500</mtu-size>
            <vlan-id>0</vlan-id>
    </extension-ip-interface>
    {'success-code': 201, 'success-message': 'Created',
    'success-type': 'Success'}
    Execute  R5 <class
    'pyfos.pyfos_brocade_extension_ip_route.extension_ip_route'>
    Execute  DEFPOST <class
    'pyfos.pyfos_brocade_extension_tunnel.extension_tunnel'>
    POST http://10.200.151.183/rest/running/brocade-extension-tunnel/
    extension-tunnel?vf-id=128 - CONTENT ->
    <extension-tunnel>
            <name>0/24</name>
            <admin-enabled>1</admin-enabled>
            <fast-write-enabled>0</fast-write-enabled>
            <tape-read>0</tape-read>
            <tape-write>0</tape-write>
            <ficon>0</ficon>
            <ip-extension>0</ip-extension>
            <load-level>Failover</load-level>
            <compression-tunnel>0</compression-tunnel>
            <qos-ratio>
                    <distribution>1</distribution>
                    <fc-high-qos>50</fc-high-qos>
                    <fc-medium-qos>30</fc-medium-qos>
                    <fc-low-qos>20</fc-low-qos>
            </qos-ratio>
    </extension-tunnel>
    {'success-code': 201, 'success-message': 'Created',
    'success-type': 'Success'}
    POST http://10.200.151.183/rest/running/brocade-extension-tunnel/
    extension-tunnel?vf-id=128 - CONTENT ->
    <extension-tunnel>
            <name>0/34</name>
            <admin-enabled>1</admin-enabled>
            <fast-write-enabled>0</fast-write-enabled>
            <tape-read>0</tape-read>
            <tape-write>0</tape-write>
            <ficon>0</ficon>
            <ip-extension>0</ip-extension>
            <load-level>Failover</load-level>
            <compression-tunnel>0</compression-tunnel>
            <qos-ratio>
                    <distribution>1</distribution>
                    <fc-high-qos>50</fc-high-qos>
                    <fc-medium-qos>30</fc-medium-qos>
                    <fc-low-qos>20</fc-low-qos>
            </qos-ratio>
    </extension-tunnel>
    {'success-code': 201, 'success-message': 'Created',
    'success-type': 'Success'}
    Execute  DEFPOST <class
    'pyfos.pyfos_brocade_extension_tunnel.extension_circuit'>
    POST http://10.200.151.183/rest/running/brocade-extension-tunnel/
    extension-circuit?vf-id=128 - CONTENT ->
    <extension-circuit>
            <name>0/24</name>
            <circuit-id>0</circuit-id>
            <local-ip-address>103.11.7.2</local-ip-address>
            <remote-ip-address>102.10.2.2</remote-ip-address>
            <metric>0</metric>
            <failover-group-id>0</failover-group-id>
            <admin-enabled>1</admin-enabled>
            <minimum-communication-rate>100000</minimum-communication-rate>
            <maximum-communication-rate>100000</maximum-communication-rate>
            <arl-algorithm-mode>0</arl-algorithm-mode>
    </extension-circuit>
    {'success-code': 201, 'success-message': 'Created',
    'success-type': 'Success'}


"""

import sys
from pyfos import pyfos_auth
from pyfos.utils import brcd_util
from pyfos.manager.pyfos_config_manager import config_manager
from pyfos.manager.pyfos_class_manager import clsmanager
# import pyfos.pyfos_brocade_fibrechannel_logical_switch as fc_ls


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
        in_json = True

    if in_json:
        fmtfile = 'JSON'
        fmtobj = 'json'
        # ext = '.json'
    else:
        fmtfile = 'XLSX'
        fmtobj = 'attributes'
        # ext = '.xlsx'
    clsmanager.addsession(session, inputs["login"], inputs["password"])
    mgr = config_manager(fmtfile, fmtobj)
    fcmodechange = config_manager()
    fcmodechange.applygoldenobject(session, envelope_name,
                                   "fibrechannel-switch", 6)
    mgr.applydiff(envelope_name, session)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
