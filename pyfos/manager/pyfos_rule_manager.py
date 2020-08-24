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

:mod:`pyfos_rule_manager` - PyFOS module to provide rule based handling\
        Support.
***************************************************************************************
The :mod:`pyfos_rule_manager`  Provides the rule management for REST
supported classes.

.. _intro:

Introduction
---------------------
The module :mod:`pyfos_rule_manager` supports rules a method for config
management support. User can write rules based on various classes/object
and attribute with conditionals for config operations.

.. _Predefined-Rules-table`:

Table for all predefined rules
--------------------------------

        +------+-------------------------------+--------------------------------------------------------------+
        | Rule |         Pyfos Class           |Details                                                       |
        +======+===============================+==============================================================+
        | R1   |   defined_configuration       | Save the Zoning configuration after POST :ref:`R1`           |
        +------+-------------------------------+--------------------------------------------------------------+
        | R2   |   defined_configuration       | Save the Zoning configuration after DELETE :ref:`R2`         |
        +------+-------------------------------+--------------------------------------------------------------+
        | R3   |   defined_configuration       | Save the Zoning configuration after PATCH  :ref:`R3`         |
        +------+-------------------------------+--------------------------------------------------------------+
        | R4   |   extension_ip_route          | Ignore non static route entries for DELETE :ref:`R4`         |
        +------+-------------------------------+--------------------------------------------------------------+
        | R5   |   extension_ip_route          | Ignore non static route entries for POST  :ref:`R5`          |
        +------+-------------------------------+--------------------------------------------------------------+
        | R6   |   fibrechannel                | Disable/Enable ports while applying configs :ref:`R6`        |
        +------+-------------------------------+--------------------------------------------------------------+
        | R7   |   effective_configuration     | Handle the effective configuration for PATCH :ref:`R7`       |
        +------+-------------------------------+--------------------------------------------------------------+
        | R8   |   fibrechannel_switch         | Disable the switch after applying the configs :ref:`R8`      |
        +------+-------------------------------+--------------------------------------------------------------+
        | R9   |   n_port_map                  | Delete all n-port-map instance configured fports :ref:`R9`   |
        +------+-------------------------------+--------------------------------------------------------------+
        | R10  |   n_port_map                  | Patch all n-port-map instance configured fports  :ref:`R10`  |
        +------+-------------------------------+--------------------------------------------------------------+
        | R11  |   port_group                  | Delete all port-groups except for pg0  :ref:`R11`            |
        +------+-------------------------------+--------------------------------------------------------------+
        | R12  |   port_group                  | Create all port-groups other than pg0  :ref:`R12`            |
        +------+-------------------------------+--------------------------------------------------------------+
        | R13  |   port_group                  | Patch only port-group instance for pg0 :ref:`R13`            |
        +------+-------------------------------+--------------------------------------------------------------+


.. _R1:

Rule-R1
---------------------
This rule is a predefined rule for *defined-configuration* `POST` operation.
As part of rule its meant to fetch the *effective-configuration* before `POST`
operation of *defined-configuration* and then execute cfgsave after the `POST`
operation is complete using *effective-configuration* `PATCH` operation.
This is used by the :mod:`switch_config_apply` for config apply sequence.


    Create defined-configuration config diff::

        > +{
        > +         "defined-configuration": {
        > +             "alias": [
        > +                 {
        > +                     "alias-name": "ali1_test",
        > +                     "member-entry": {
        > +                         "alias-entry-name": [
        > +                             "70:00:8c:7c:ff:5f:54:00",
        > +                             "70:00:8c:7c:ff:5f:55:00"
        > +                         ]
        > +                     }
        > +                 },
        > +             ],
        > +             "cfg": [
        > +                 {
        > +                     "cfg-name": "testcfg",
        > +                     "member-zone": {
        > +                         "zone-name": [
        > +                             "zone1",
        > +                             "zone2"
        > +                         ]
        > +                     }
        > +                 }
        > +             ],
        > +             "zone": [
        > +                 {
        > +                     "member-entry": {
        > +                         "entry-name": [
        > +                             "11:22:33:44:55:66:77:88",
        > +                             "21:22:33:44:55:66:77:88"
        > +                         ]
        > +                     },
        > +                     "zone-name": "zone1",
        > +                     "zone-type": "0"
        > +                 },
        > +                 {
        > +                     "member-entry": {
        > +                         "entry-name": [
        > +                             "11:22:33:44:55:66:77:88",
        > +                             "21:22:33:44:55:66:77:88"
        > +                         ]
        > +                     },
        > +                     "zone-name": "zone2",
        > +                     "zone-type": "0"
        > +             }
        > +             ]
        > +       }
        > +}

    Example::

        Execute  R1 <class 'pyfos.pyfos_brocade_zone.defined_configuration'>
        POST http://10.200.151.183/rest/running/zoning/
        defined-configuration?vf-id=128 - CONTENT ->
        <defined-configuration>
                <cfg>
                        <member-zone>
                                <zone-name>zone1</zone-name>
                                <zone-name>zone2</zone-name>
                        </member-zone>
                        <cfg-name>testcfg</cfg-name>
                </cfg>
                <alias>
                        <alias-name>ali1_test</alias-name>
                        <member-entry>
                                <alias-entry-name>70:00:8c:7c:ff:5f:54:00
                                </alias-entry-name>
                                <alias-entry-name>70:00:8c:7c:ff:5f:55:00
                                </alias-entry-name>
                        </member-entry>
                </alias>
                <zone>
                        <zone-type>0</zone-type>
                        <member-entry>
                                <entry-name>11:22:33:44:55:66:77:88
                                </entry-name>
                                <entry-name>21:22:33:44:55:66:77:88
                                </entry-name>
                        </member-entry>
                        <zone-name>zone1</zone-name>
                </zone>
                <zone>
                        <zone-type>0</zone-type>
                        <member-entry>
                                <entry-name>11:22:33:44:55:66:77:88
                                </entry-name>
                                <entry-name>21:22:33:44:55:66:77:88
                                </entry-name>
                        </member-entry>
                        <zone-name>zone2</zone-name>
                </zone>
        </defined-configuration>
        {'success-code': 201, 'success-message': 'Created',
        'success-type': 'Success'}
        PATCH http://10.200.151.183/rest/running/zoning/
        effective-configuration?vf-id=128 - CONTENT ->
        <effective-configuration>
                <cfg-action>1</cfg-action>
                <checksum>f4edaf2cfa6c629ecaef3ee3460bb1ea</checksum>
        </effective-configuration>
        {'success-code': 204, 'success-message': 'No Content',
        'success-type': 'Success'}

.. _R2:

Rule-R2
---------------------
This rule is a predefined rule for *defined-configuration* `DELETE`
operation. As part of rule its meant to fetch the *effective-configuration*
before `DELETE`operation of *defined-configuration* and then execute cfgsave
after the `DELETE` operation is complete using *effective-configuration*
`PATCH` operation. This is used by the :mod:`switch_config_apply` for
config apply sequence.

    Delete defined-configuration config diff::

        < -{
        < -	"defined-configuration": {
        < -		"alias": [
        < -			{
        < -				"alias-name": "ali2_test",
        < -				"member-entry": {
        < -					"alias-entry-name": [
        < -						"90:00:8c:7c:ff:5f:54:00",
        < -						"90:00:8c:7c:ff:5f:55:00"
        < -					]
        < -				}
        < -			},
        < -			{
        < -				"alias-name": "ali3_test",
        < -				"member-entry": {
        < -					"alias-entry-name": [
        < -						"80:00:8c:7c:ff:5f:54:00",
        < -						"80:00:8c:7c:ff:5f:55:00"
        < -					]
        < -				}
        < -			}
        < -		]
        < -	}
        < -}

    Example::

        Execute  R2 <class 'pyfos.pyfos_brocade_zone.defined_configuration'>
        DELETE http://10.200.151.183/rest/running/zoning/
        defined-configuration?vf-id=128 - CONTENT ->
        <defined-configuration>
                <alias>
                        <member-entry>
                                <alias-entry-name>90:00:8c:7c:ff:5f:54:00
                                </alias-entry-name>
                                <alias-entry-name>90:00:8c:7c:ff:5f:55:00
                                </alias-entry-name>
                        </member-entry>
                        <alias-name>ali2_test</alias-name>
                </alias>
                <alias>
                        <member-entry>
                                <alias-entry-name>80:00:8c:7c:ff:5f:54:00
                                </alias-entry-name>
                                <alias-entry-name>80:00:8c:7c:ff:5f:55:00
                                </alias-entry-name>
                        </member-entry>
                        <alias-name>ali3_test</alias-name>
                </alias>
        </defined-configuration>
        {'success-code': 204, 'success-message': 'No Content',
        'success-type': 'Success'}
        PATCH http://10.200.151.183/rest/running/zoning/
        effective-configuration?vf-id=128 - CONTENT ->
        <effective-configuration>
                <cfg-action>1</cfg-action>
                <checksum>dee3f061746beddbf4ad1c417bc0a61b</checksum>
        </effective-configuration>
        {'success-code': 204, 'success-message': 'No Content',
        'success-type': 'Success'}


.. _R3:

Rule-R3
---------------------
This rule is a predefined rule for *defined-configuration* `PATCH`
operation. As part of rule its meant to fetch the *effective-configuration*
before `PATCH`operation of *defined-configuration* and then execute cfgsave
after the `PATCH` operation is complete using *effective-configuration*
`PATCH` operation. This is used by the :mod:`switch_config_apply` for
config apply sequence.

    PATCH defined-configuration config diff::

            {
                "defined-configuration": {
                    "alias": [
                        {
                            "alias-name": "ali1_test",
                            "member-entry": {
        < -                     "alias-entry-name":
                                                "['70:00:8c:7c:ff:5f:54:00',
                                                  '70:00:8c:7c:ff:5f:55:00']"
        ---
        > +                     "alias-entry-name":
                                                "['70:00:8c:7c:ff:5f:54:00',
                                                  '70:00:8c:7c:ff:5f:55:00',
                                                  '80:00:8c:7c:ff:5f:55:00']"
                            }
                        }
                    ],
                    "zone": [
                        {
                            "member-entry": {
        < -                     "entry-name": "['11:22:33:44:55:66:77:88',
                                                '21:22:33:44:55:66:77:88']"
        ---
        > +                     "entry-name": "['11:22:33:44:55:66:77:88']"
                            },
                            "zone-name": "zone1"
                        }
                    ]
                }
            }


    Example::

        Execute  R3 <class 'pyfos.pyfos_brocade_zone.defined_configuration'>
        PATCH http://10.200.151.183/rest/running/zoning/
        defined-configuration?vf-id=128 - CONTENT ->
        <defined-configuration>
                <zone>
                        <zone-name>zone1</zone-name>
                        <member-entry>
                                <entry-name>11:22:33:44:55:66:77:88
                                </entry-name>
                        </member-entry>
                </zone>
                <alias>
                        <member-entry>
                                <alias-entry-name>70:00:8c:7c:ff:5f:54:00
                                </alias-entry-name>
                                <alias-entry-name>70:00:8c:7c:ff:5f:55:00
                                </alias-entry-name>
                                <alias-entry-name>80:00:8c:7c:ff:5f:55:00
                                </alias-entry-name>
                        </member-entry>
                        <alias-name>ali1_test</alias-name>
                </alias>
        </defined-configuration>
        {'success-code': 204, 'success-message': 'No Content',
        'success-type': 'Success'}
        PATCH http://10.200.151.183/rest/running/zoning/
        effective-configuration?vf-id=128 - CONTENT ->
        <effective-configuration>
                <cfg-action>1</cfg-action>
                <checksum>e4356bad642e80b7509002c03161e048</checksum>
        </effective-configuration>
        {'success-code': 204, 'success-message': 'No Content',
        'success-type': 'Success'}

.. _R4:

Rule-R4
---------------------
This rule is a predefined rule for *extension_ip_route* `DELETE`
operation to ignore default routes. If only default routes are
identified for config operation then there wont be any creation
of iproute seen.


    Delete extension-ip-route config diff::

        < -[
        < -    {
        < -        "extension-ip-route": {
        < -            "dp-id": "0",
        < -            "ip-address": "11.20.50.0",
        < -            "ip-gateway": "*",
        < -            "ip-prefix-length": "24",
        < -           "name": "0/7"
        < -         }
        < -    }
        < -]

    Example::

        Execute  R5 <class
        'pyfos.pyfos_brocade_extension_ip_route.extension_ip_route'>

.. _R5:

Rule-R5
---------------------
This rule is a predefined rule for *extension_ip_route* `POST`
operation to ignore default routes. If only default routes are
identified for config operation then there wont be any creation
of iproute seen.


    Create extension-ip-route config diff::

        > +[
        > +    {
        > +        "extension-ip-route": {
        > +            "dp-id": "0",
        > +            "ip-address": "51.50.50.0",
        > +            "ip-gateway": "*",
        > +            "ip-prefix-length": "24",
        > +           "name": "0/7"
        > +         }
        > +    }
        > +]

    Example::

        Execute  R4 <class
        'pyfos.pyfos_brocade_extension_ip_route.extension_ip_route'>

.. _R6:

Rule-R6
---------------------
This rule is a predefined rule for *fibrechannel* `PATCH`
operation. As part of rule its meant to disable the ports and enable them
after `PATCH` operation.

    Example::

        Execute  R5 <class 'pyfos.pyfos_brocade_fibrechannel.fibrechannel'>
        PATCH http://10.200.151.183/rest/running/brocade-interface/
        fibrechannel?vf-id=128 - CONTENT ->
        <fibrechannel>
                <name>0/0</name>
                <enabled-state>6</enabled-state>
        </fibrechannel>
        {'success-type': 'Success', 'success-message': 'No Content',
        'success-code': 204}
        PATCH http://10.200.151.183/rest/running/brocade-interface/
        fibrechannel?vf-id=128 - CONTENT ->
        <fibrechannel>
                <name>0/0</name>
                <npiv-enabled>0</npiv-enabled>
                <speed>16000000000</speed>
        </fibrechannel>
        {'success-type': 'Success', 'success-message': 'No Content',
        'success-code': 204}
        PATCH http://10.200.151.183/rest/running/brocade-interface/
        fibrechannel?vf-id=128 - CONTENT ->
        <fibrechannel>
                <name>0/0</name>
                <enabled-state>2</enabled-state>
        </fibrechannel>
        {'success-type': 'Success', 'success-message': 'No Content',
        'success-code': 204}

.. _R7:

Rule-R7
---------------------
This rule is a predefined rule for *effective-configuration* `PATCH`
operation. As part of rule its meant to fetch the *effective-configuration*
before `PATCH` operation and use it to populate the checksum
for the `PATCH` operation

    Example::

        Execute  R7 <class 'pyfos.pyfos_brocade_zone.effective_configuration'>
        PATCH http://10.200.151.183/rest/running/zoning/
        effective-configuration?vf-id=128 - CONTENT ->
        <effective-configuration>
                <cfg-name>testcfg</cfg-name>
                <checksum>dee3f061746beddbf4ad1c417bc0a61b</checksum>
        </effective-configuration>
        {'success-code': 204, 'success-message': 'No Content',
        'success-type': 'Success'}

.. _R8:

Rule-R8
---------------------
This rule is a predefined rule for *fibrechannel-switch* `PATCH`
operation. As part of rule its meant to disable the *fibrechannel-switch*
before `PATCH` operation and then perform the expected patch operation
for the `PATCH` operation

    Example::

        Execute  R8 <class
        'pyfos.pyfos_brocade_fibrechannel_switch.fibrechannel_switch'>
        PATCH http://10.155.107.42/rest/running/brocade-fibrechannel-switch/
        fibrechannel-switch - CONTENT ->
        <fibrechannel-switch>
                <name>10:00:00:27:f8:fd:1f:80</name>
                <enabled-state>3</enabled-state>
        </fibrechannel-switch>
        {'http-resp-code': 204, 'success-type': 'Success', 'success-code': 204,
        'success-message': 'No Content'}
        PATCH http://10.155.107.42/rest/running/brocade-fibrechannel-switch/
        fibrechannel-switch - CONTENT ->
        <fibrechannel-switch>
                <name>10:00:00:27:f8:fd:1f:80</name>
                <ag-mode>3</ag-mode>
        </fibrechannel-switch>
        {'http-resp-code': 204, 'success-type': 'Success', 'success-code': 204,
        'success-message': 'No Content'}
        .......More ports below.......

.. _R9:

Rule-R9
---------------------
This rule is a predefined rule for *n-port-map* `DELETE`
operation where all n-port-map with configured fports are deleted.


    DELETE  n-port-map config diff::

        < -{
        < -    "n-port-map": {
        < -         "configured-f-port-list": {
        < -           "f-port": [
        < -                "0/0",
        < -                "0/1"
        < -            ]
        < -         },
        < -         "failback-enabled": "1",
        < -         "failover-enabled": "1",
        < -         "n-port": "0/16",
        < -         "online-status": "0",
        < -         "reliable-status": "1"
        < -    }
        < -},


    Example::

        Execute  R9 <class 'pyfos.pyfos_brocade_access_gateway.n_port_map'>
        DELETE http://10.155.107.42/rest/running/brocade-access-gateway/
        n-port-map - CONTENT ->
        <n-port-map>
                <n-port>0/16</n-port>
        </n-port-map>
        .......More ports below.......

.. _R10:

Rule-R10
---------------------
This rule is a predefined rule for *n-port-map* `PATCH`
operation. As part of rule its meant to configure all *n-port-maps*
with configured fports.


    PATCH  n-port-map config diff::

    > +{
    > +    [
    > +        {
    > +            "n-port-map": {
    > +                "failback-enabled": "1",
    > +                "failover-enabled": "1",
    > +                "n-port": "0/23",
    > +                "online-status": "0",
    > +                "reliable-status": "1"
    > +            }
    > +        }
    > +    ]


    Example::

        Execute  R10 <class 'pyfos.pyfos_brocade_access_gateway.n_port_map'>
        PATCH http://10.155.107.42/rest/running/brocade-access-gateway/
        n-port-map - CONTENT ->
        <n-port-map>
                <n-port>0/16</n-port>
                <failover-enabled>1</failover-enabled>
                <failback-enabled>1</failback-enabled>
                <configured-f-port-list>
                        <f-port>0/0</f-port>
                        <f-port>0/1</f-port>
                </configured-f-port-list>
        </n-port-map>
        {'success-message': 'No Content', 'success-type': 'Success',
        'success-code': 204, 'http-resp-code': 204}

.. _R11:

Rule-R11
---------------------
This rule is a predefined rule for *port-group* `DELETE`
operation to skip default *port-group* **pg0**. if there
are no port-group deltions then it wont do anything.

    Example::

        Execute  R11 <class 'pyfos.pyfos_brocade_access_gateway.port_group'>


.. _R12:

Rule-R12
---------------------
This rule is a predefined rule for *port-group* `POST`
operation to skip default *port-group* **pg0** from creation.


    POST port-group config diff::

        > +{
        > +    "port-group": {
        > +        "port-group-id": "1",
        > +        "port-group-mode": {
        > +            "load-balancing-mode-enabled": "0",
        > +            "multiple-fabric-name-monitoring-mode-enabled": "0"
        > +        },
        > +        "port-group-n-ports": {
        > +            "n-port": [
        > +                "0/4"
        > +            ]
        > +        },
        > +        "port-group-name": "pg1"
        > +    }
        > +}


    Example::

        Execute  R12 <class 'pyfos.pyfos_brocade_access_gateway.port_group'>
        POST http://10.155.107.42/rest/running/brocade-access-gateway/
        port-group - CONTENT ->
        <port-group>
                <port-group-id>1</port-group-id>
                <port-group-mode>
                        <load-balancing-mode-enabled>0
                        </load-balancing-mode-enabled>
                        <multiple-fabric-name-monitoring-mode-enabled>0
                        </multiple-fabric-name-monitoring-mode-enabled>
                </port-group-mode>
                <port-group-n-ports>
                        <n-port>0/4</n-port>
                </port-group-n-ports>
                <port-group-name>pg1</port-group-name>
        </port-group>
        {'success-message': 'Created', 'success-type': 'Success',
        'success-code': 201, 'http-resp-code': 201}


.. _R13:

Rule-R13
---------------------
This rule is a predefined rule for *port-group* `PATCH`
operation to only use default *port-group* **pg0** for modification.


    PATCH port-group config diff::

            {
                "port-group": {
                      "port-group-id": "0",
                      "port-group-n-ports": {
        < -           "n-port": "['0/16', '0/17', '0/18', '0/19', '0/20',
                                  '0/21', '0/22', '0/23']"
        ---
        > +           "n-port": "['0/6', '0/7', '0/8', '0/9', '0/12', '0/13',
                                  '0/14', '0/15', '0/16', '0/17', '0/18',
                                  '0/19', '0/20', '0/21', '0/22', '0/23']"
                     }
                }
            }


    Example::

        Execute  R13 <class 'pyfos.pyfos_brocade_access_gateway.port_group'>
        PATCH http://10.155.107.42/rest/running/brocade-access-gateway/
        port-group - CONTENT ->
        <port-group>
                <port-group-id>0</port-group-id>
                <port-group-n-ports>
                        <n-port>0/6</n-port>
                        <n-port>0/7</n-port>
                        <n-port>0/8</n-port>
                        <n-port>0/9</n-port>
                        <n-port>0/12</n-port>
                        <n-port>0/13</n-port>
                        <n-port>0/14</n-port>
                        <n-port>0/15</n-port>
                        <n-port>0/16</n-port>
                        <n-port>0/17</n-port>
                        <n-port>0/18</n-port>
                        <n-port>0/19</n-port>
                        <n-port>0/20</n-port>
                        <n-port>0/21</n-port>
                        <n-port>0/22</n-port>
                        <n-port>0/23</n-port>
                </port-group-n-ports>
        </port-group>
        {'success-message': 'No Content', 'success-type': 'Success',
        'success-code': 204, 'http-resp-code': 204}


"""

import inspect
import json
from pyfos.manager.pyfos_class_manager import clsmanager
from pyfos.pyfos_brocade_interface import fibrechannel
from pyfos.pyfos_brocade_extension_ip_route import extension_ip_route
from pyfos.pyfos_brocade_zone import defined_configuration
from pyfos.pyfos_brocade_zone import effective_configuration
from pyfos.pyfos_brocade_fibrechannel_switch import fibrechannel_switch
from pyfos.pyfos_brocade_access_gateway import port_group
from pyfos.pyfos_brocade_access_gateway import n_port_map
from pyfos import pyfos_auth
from pyfos import pyfos_util


def code(tabs, codestring):
    wcode = ""
    # pylint: disable=W0612
    for i in range(tabs):
        wcode += "    "
    wcode += codestring + "\n"
    return wcode


class rule_element_encoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, 'reprJSON'):
            return obj.reprJSON()
        else:
            return json.JSONEncoder.default(self, obj)


def clskey(key):
    wclskey = "clskey_" + key
    return wclskey


def ckey(key):
    wclskey = "con_" + key
    return wclskey


def inskey(key):
    winskey = "inskey_" + key
    return winskey


def lhskey(key):
    wlhskey = "lhskey_" + key
    return wlhskey


def rhskey(key):
    wrhskey = "rhskey_" + key
    return wrhskey


class rmelem():
    """
    The Base class for all Rule elements of Rule Manager.
    """
    TYPE_INVALID = 0
    TYPE_RULE = 1
    TYPE_CLASS = 2
    TYPE_ATR = 3
    TYPE_VAR = 4
    TYPE_CONST = 5
    TYPE_COND = 6
    TYPE_UNKNOWN = 7

    def __init__(self, elemtype=TYPE_INVALID, key=None):
        self.key = key
        self.type = elemtype
        self.codeme = ""
        self.logger = None

    def log(self, level, *msg):
        if self.logger is None:
            self.logger = clsmanager.initlogger(str(self.__class__))
        if self.logger is not None:
            clsmanager.logbase(self.logger, level, "".join(map(str, msg)))

    def __repr__(self):
        return (json.dumps(self, cls=rule_element_encoder,
                           sort_keys=True, indent=4))


class rmclass(rmelem):
    """
    The class represents a pyfos class as a rule element to work with
    Rule Manager.
    """
    runtime = 1
    diff = 2
    static = 4

    def __init__(self, key, cls, request, flags=runtime, obj=None):
        super().__init__(rmelem.TYPE_CLASS, key)
        self.isclass = True
        self.cls = cls
        self.obj = obj
        if obj is not None:
            self.isclass = False
        self.istgt = False
        self.request = request
        self.evalrun = None
        self.flags = flags
        self.cfgmgr = None
        self.tgtop = None
        self.tgtslot = None
        # print (self)

    def testeval(self, session, tag, args):
        if self.request == "GET":
            if self.flags == rmclass.runtime:
                self.evalrun = self.cls.get(session)
                if pyfos_util.is_failed_resp(self.evalrun):
                    print(self.evalrun)
                    self.log(3, self.evalrun)
                    self.evalrun = None
            elif self.flags == rmclass.static:
                if self.obj in args.keys():
                    self.evalrun = args[self.obj]
                else:
                    print(tag, "error")
                    self.log(3, tag, "error")
                    self.evalrun = None
            elif self.flags == rmclass.diff:
                # print("enable Me")
                self.cfgmgr = args["tgtcfgmgr"]
                self.tgtop = args["tgtop"]
                self.tgtslot = args["tgtslot"]
                if self.cfgmgr is not None:
                    self.evalrun = self.cfgmgr.get(session['vfid'],
                                                   self.cls,
                                                   self.tgtop,
                                                   self.tgtslot,
                                                   session)
                else:
                    print(tag, "No Config MGR")
                    self.log(3, "No Config MGR")
                    self.evalrun = None
            else:
                return None

            if self.evalrun is not None and not isinstance(self.evalrun, list):
                self.evalrun = [self.evalrun]
        else:
            if self.key in args.keys():
                obj = args[self.key]
                pyfos_auth.debug_set(session, 1)
                if self.request == 'DELETE':
                    self.evalrun = obj.delete(session)
                elif self.request == 'PATCH':
                    self.evalrun = obj.patch(session)
                elif self.request == 'PUT':
                    self.evalrun = obj.put(session)
                elif self.request == 'POST':
                    self.evalrun = obj.post(session)
                print(self.evalrun)
                self.log(1, self.evalrun)
                if self.flags == rmclass.diff:
                    self.cfgmgr = args["tgtcfgmgr"]
                    self.tgtop = args["tgtop"]
                    self.tgtslot = args["tgtslot"]
                    self.cfgmgr.handleCB(self.cls, self.tgtop,
                                         self.tgtslot, session)
                pyfos_auth.debug_set(session, 0)
            else:
                print("No Obj for operation", self.key, args.keys())
                self.log(3, "No Obj for operation", self.key, args.keys())
                self.evalrun = None

        if pyfos_util.is_failed_resp(self.evalrun):
            print(self.evalrun)
            self.log(1, self.evalrun)
            self.evalrun = None
        # print (self.evalrun)
        return self.evalrun

    # pylint: disable=W0613
    def code(self, session, tag, args, tabs):
        if self.request == "GET":
            obj = clskey(self.key)
            if self.flags == rmclass.runtime:
                self.codeme = code(tabs, obj + " = " +
                                   str(self.cls.__name__) + ".get(session)")
                self.codeme += code(tabs, "print(" + obj + ")")
                self.codeme += code(tabs, "if " + obj +
                                    " is not None and isinstance(" +
                                    obj + ", " + str(self.cls.__name__) + "):")
                self.codeme += code(tabs + 1, obj + " = [" + obj + "]")
            elif self.flags == rmclass.static:
                self.codeme = code(tabs, obj + " = " + self.obj)
                self.codeme += code(tabs, "if not isinstance(" + obj +
                                    " , list):")
                self.codeme += code(tabs + 1, obj + " = [ " + obj + " ]")
            elif self.flags == rmclass.diff:
                self.codeme += code(tabs, "self.cfgmgr = args[\"tgtcfgmgr\"]")
                self.codeme += code(tabs, obj + " =  self.cfgmgr.get(" +
                                    session['vfid'] + "," + self.cls.__name__ +
                                    "," + args["tgtslot"] +
                                    "," + self.request + ", session)")
            # print (self.codeme)
        else:
            insobj = inskey(self.key)
            self.codeme = code(tabs, "ret = None")
            if self.request == 'DELETE':
                self.codeme += code(tabs, "ret = " + insobj +
                                    ".delete(session)")
            elif self.request == 'PATCH':
                self.codeme += code(tabs, "ret = " + insobj +
                                    ".patch(session)")
            elif self.request == 'PUT':
                self.codeme += code(tabs, "ret = " + insobj + ".put(session)")
            elif self.request == 'POST':
                self.codeme += code(tabs, "ret = " + insobj + ".post(session)")
            self.codeme += code(tabs, "if pyfos_util.is_failed_resp(ret):")
            self.codeme += code(tabs + 1, "print(ret)")
            self.codeme += code(tabs, "else:")
            self.codeme += code(tabs + 1, "print(ret)")
        # print (self.codeme)
        return self.codeme

    def reprJSON(self):
        retdict = {'CLASS':
                   {'key': self.key,
                    'class': str(self.cls),
                    'request': self.request
                    }
                   }
        return retdict


class rmanyclass(rmclass):
    """
    The class represents a pyfos class dynamically in runtime as a rule element
    to work with Rule Manager.
    """

    def __init__(self, key, cls=None, op=None,
                 flags=rmclass.runtime, obj=None):
        self.target = None
        super().__init__(key, cls, op, flags, obj)

    def setclass(self, cls):
        self.cls = cls

    def setrequest(self, request):
        self.request = request

    def settargetcls(self, cls):
        self.target = cls

    def testeval(self, session, tag, args):
        context = args
        self.cls = context['tgtcls']
        self.tgtop = context['tgtop']
        # return super(rmclass, self).testeval(session, tag, args)
        return super().testeval(session, tag, args)

    def code(self, session, tag, args, tabs):
        context = args
        self.cls = context['tgtcls']
        self.tgtop = context['tgtop']

        return super().code(session, tag, args, tabs)


class rmattribute(rmelem):
    """
    The class represents a pyfos class object attribute as a rule element
    to work with Rule Manager.
    """
    def __init__(self, key, attrib):
        super().__init__(rmelem.TYPE_ATR, key)
        self.attrib = attrib
        self.evalrun = None

    # pylint: disable=W0613
    def testeval(self, session, tag, args):
        self.evalrun = getattr(args[self.key], self.attrib)
        return self.evalrun

    # pylint: disable=W0613
    def code(self, session, tag, args, tabs):
        insobj = inskey(self.key)
        self.codeme = "getattr(" + insobj + ", \"" + self.attrib + "\")"
        # print(self.codeme)
        self.log(1, self.codeme)
        return self.codeme

    def reprJSON(self):
        retdict = {'ATR': {'key': self.key,
                           'atribute': self.attrib,
                           }
                   }
        return retdict


class rmconst(rmelem):
    """
    The class represents a value constant as a rule element
    to work with Rule Manager.
    """
    def __init__(self, val):
        super().__init__(rmelem.TYPE_CONST, None)
        self.val = val
        self.evalrun = None
        # print (self)

    # pylint: disable=W0613
    def testeval(self, session, tag, args):
        self.evalrun = self.val
        return self.evalrun

    # pylint: disable=W0613
    def code(self, session, tag, args, tabs):
        self.codeme = str("\"" + self.val + "\"")
        # print(self.codeme)
        return self.codeme

    def reprJSON(self):
        retdict = {'CONST': {'key': self.key,
                             'val': self.val,
                             }
                   }
        return retdict


class rmcond(rmelem):
    """
    The class represents a conditional variable as a rule element
    to work with Rule Manager.
    """
    def __init__(self, key, op, lhs, rhs):
        super().__init__(rmelem.TYPE_COND, key)
        self.lhs = lhs
        self.rhs = rhs
        self.op = op
        self.elret = None
        self.eleval = None
        self.erret = None
        self.ereval = None
        self.eval = False
        self.ret = False
        self.evalrun = None
        if isinstance(self.lhs, rmconst):
            self.elval = True
        if isinstance(self.rhs, rmconst):
            self.erval = True

    def testeval(self, session, tag, args):
        lhs = None
        rhs = None
        ret = False
        if self.eval is True:
            # print("returning from rmcond", self.key, "Ret", self.ret)
            return self.ret
        if self.op == "not" and self.lhs is not None:
            if self.eleval is None:
                lhs = self.lhs.testeval(session, tag, args)
                ret = bool(not lhs)
                self.ret = ret
            else:
                ret = self.ret
        else:
            if self.lhs is None or (self.rhs is None and
               self.op not in ("not any", "any")):
                # print ("LHS/RHS is none", "LHS=", self.lhs, "RHS", self.rhs)
                return False
            if self.eleval is None:
                plhs = self.lhs.testeval(session, tag, args)
                if inspect.ismethod(plhs) and self.op != "set":
                    lhs = plhs()
                else:
                    lhs = plhs
                self.elret = lhs
                # self.eleval = True
            else:
                lhs = self.elret

            if self.ereval is None and self.rhs is not None:
                prhs = self.rhs.testeval(session, tag, args)
                if inspect.ismethod(prhs):
                    rhs = prhs()
                else:
                    rhs = prhs
                self.erret = rhs
            else:
                rhs = self.erret

            if self.op == "=":
                lhs(rhs)
            if self.op == "eq":
                ret = bool(lhs == rhs)
            if self.op == "not eq":
                ret = bool(not lhs == rhs)
            if self.op == "set":
                lhs(rhs)
                ret = True
            if self.op == "and":
                ret = bool(lhs and rhs)
            if self.op == "or":
                ret = bool(lhs or rhs)
            if self.op == "not any":
                ret = bool(not any(lhs))
            if self.op == "any":
                ret = bool(any(lhs))
        self.ret = ret
        self.eval = True
        self.evalrun = ret
        # print (dict({self.key: self.evalrun, 'lhs': lhs, 'rhs': rhs}))
        return self.evalrun

    def code(self, session, tag, args, tabs):
        lhs = lhskey(self.key)
        rhs = rhskey(self.key)
        mykey = ckey(self.key)
        if self.op == "not" and self.lhs is not None:
            self.codeme += code(tabs, lhs + " = " +
                                self.lhs.code(session, tag,
                                              args, tabs))
            self.codeme += code(0, mykey + " = eval(\"not " +
                                ckey(self.lhs.key) + "\"")
        else:
            if self.lhs is None or (self.rhs is None and
               self.op not in ("any", "not any")):
                # print ("LHS/RHS is none", "LHS=", self.lhs, "RHS", self.rhs)
                return ""
            else:
                if isinstance(self.lhs, rmcond):
                    self.codeme += self.lhs.code(session, tag, args, tabs)
                    self.codeme += code(tabs, lhs + " = " + ckey(self.lhs.key))

                if isinstance(self.rhs, rmcond):
                    self.codeme += self.rhs.code(session, tag, args, tabs)
                    self.codeme += code(tabs, rhs + " = " + ckey(self.rhs.key))

                if isinstance(self.lhs, (rmattribute, rmconst)):
                    self.codeme += code(tabs, lhs + " = " +
                                        self.lhs.code(session, tag,
                                                      args, tabs))
                if isinstance(self.lhs, rmattribute):
                    self.codeme += code(tabs, "if inspect.ismethod(" +
                                        lhs + ") and \"" + self.op +
                                        "\" != \"set\":")
                    self.codeme += code(tabs + 1, lhs + " = eval(\"" +
                                        lhs + "()\")")

                if isinstance(self.rhs, (rmattribute, rmconst)):
                    self.codeme += code(tabs, rhs + " = " +
                                        self.rhs.code(session, tag,
                                                      args, tabs))
                if isinstance(self.rhs, rmattribute):
                    self.codeme += code(tabs, "if inspect.ismethod(" +
                                        rhs + "):")
                    self.codeme += code(tabs + 1, rhs + " = eval(\"" +
                                        rhs + "()\")")

            if self.op == "=":
                self.codeme += code(tabs, lhs + "(" + rhs + ")")
            if self.op == "eq":
                self.codeme += code(tabs, mykey + " = eval(\"" + lhs + " == " +
                                    rhs + "\")")
            if self.op == "not eq":
                self.codeme += code(tabs, mykey + " = eval(\"" + lhs + " != " +
                                    rhs + "\")")
            if self.op == "set":
                self.codeme += code(tabs, mykey + " = eval(\"" + lhs + "(" +
                                    rhs + ")\")")
            if self.op == "and" or self.op == "or":
                self.codeme += code(tabs, mykey + " = eval(\"" + lhs + " " +
                                    self.op + " " + rhs + "\")")
            if self.op in ("any", "not any"):
                self.codeme += code(tabs, mykey + " = eval(\"" +
                                    self.op + "(" + lhs + ")\")")
        # print(self.codeme)
        return self.codeme

    def cleanearly(self, session, tag, args, key):
        # print("Self:", self.key, "key ", key, self.lhs.key, self.rhs.key,
        #      "ret:", self.ret, "Eval" , self.eval)
        if isinstance(self.lhs, rmcond):
            self.lhs.cleanearly(session, tag, args, key)
            if self.lhs.eval is None:
                self.eval = None
                self.ret = None

        if isinstance(self.rhs, rmcond):
            self.rhs.cleanearly(session, tag, args, key)
            if self.rhs.eval is None:
                self.eval = None
                self.ret = None
        # clean leafs only
        if isinstance(self.lhs, rmattribute) and self.lhs.key == key:
            # print("clean")
            self.eleval = None
            self.elret = None
            self.ret = None
            self.eval = None
        if isinstance(self.rhs, rmattribute) and self.rhs.key == key:
            self.ereval = None
            self.erret = None
            self.ret = None
            self.eval = None
        # print("Self:", self.key, "key ", key, self.lhs.key, self.rhs.key,
        #      "ret:", self.ret, "Eval" , self.eval)

    def earlytesteval(self, session, tag, args, key):
        if isinstance(self.lhs, rmcond):
            self.lhs.earlytesteval(session, tag,
                                   args, key)
        if isinstance(self.rhs, rmcond):
            self.lhs.earlytesteval(session,
                                   tag, args, key)
        if not isinstance(self.lhs, rmcond) and\
           self.lhs.key == key:
            self.lhs.testeval(session, tag, args)
        if not isinstance(self.rhs, rmcond) and\
           self.rhs is not None and\
           self.rhs.key == key:
            self.rhs.testeval(session, tag, args)
        if self.eleval is True and self.reval is True and\
           self.eval is None:
            self.testeval(session, tag, args)

    def reprJSON(self):
        retdict = {'COND': {'key': self.key,
                            'op': self.op,
                            'lhs': self.lhs,
                            'rhs': self.rhs
                            }
                   }
        return retdict


class rmrule(rmelem):
    """
    The class represents a rule to work with Rule Manager.
    """
    def __init__(self, rule, tag, inarg=[], fargs=[], operator=[],
                 targ=[], post=[], deps=[]):
        super().__init__(rmelem.TYPE_RULE, rule)
        self.rule = rule
        self.tag = tag
        self.inarg = inarg
        self.fargs = fargs
        self.operator = operator
        self.target = targ
        self.dep = deps
        self.instance = None
        self.priority = 0
        self.i_target = {}
        self.i_deps = {}
        self.post = post
        self.mydict = dict({self.key: self})
        self.tgtcls = None
        self.srccls = None
        self.depth = 0

    def reprJSON(self):
        retdict = {self.key:
                   {'rule': self.rule,
                    'tag': self.tag,
                    'priority': self.priority,
                    'SELECT FROM': self.inarg,
                    'where': self.fargs,
                    'modify': self.operator,
                    'target': self.target,
                    'POST': self.post,
                    'deps': self.dep,
                    'i_deps': self.i_deps,
                    'depth': self.depth
                    }}
        return retdict

    def __repr__(self):
        return (json.dumps(self, cls=rule_element_encoder,
                           sort_keys=True, indent=4))

    def inputarg(self, session, tag, args):
        inargs = dict(args)
        # val = self.inarg
        # print(val, len(val))
        keysmap = dict()
        valid_eval = False
        for i in range(len(self.inarg)):
            keysmap.update(dict({str(i): self.inarg[i].key}))
            inargs.update(dict({self.inarg[i].key:
                          self.inarg[i].testeval(session, tag, args)}))
            val = inargs[self.inarg[i].key]
            if isinstance(val, list) and any(val):
                for j in range(len(self.target)):
                    if self.inarg[i].key == self.target[j].key:
                        valid_eval = True
            # self.early(session, tag, None, self.inarg[i].key, 1)
        if valid_eval is True:
            outargs = dict(args)
            self.forloop(session, tag, keysmap, 0, inargs, outargs)
            return self.postexec(session, tag, outargs)
        return None

    def forloop(self, session, tag, keysmap, count, inargs, outargs):
        ret = None
        if count >= len(keysmap):
            return self.where(session, tag, outargs)
        else:
            key = keysmap[str(count)]
            if key in inargs.keys():
                val = inargs[key]
                if val is None:
                    return dict({key: None})
                elif len(val) > 0:
                    for i in range(len(val)):
                        outargs.update(dict({key: val[i]}))
                        # print("Loop ", key, " count:", i)
                        # rmcond
                        self.early(session, tag, outargs, key, 2)
                        ret = self.forloop(session, tag, keysmap,
                                           count + 1, inargs, outargs)
                        # clean
                        self.early(session, tag, outargs, key, 1)
        return dict({key: ret})

    def early(self, session, tag, args, key, flags):
        ret = True
        if self.fargs is not None:
            for i in range(len(self.fargs)):
                if flags == 1:
                    self.fargs[i].cleanearly(session, tag, args, key)
                if flags == 2:
                    self.fargs[i].earlytesteval(session, tag, args, key)
        if self.operator is not None:
            for i in range(len(self.operator)):
                if flags == 1:
                    self.operator[i].cleanearly(session, tag, args, key)

                if flags == 2:
                    self.operator[i].earlytesteval(session, tag, args, key)
        return ret

    def where(self, session, tag, args):
        val = None
        # print (args)
        if self.fargs is not None:
            for i in range(len(self.fargs)):
                ret = self.fargs[i].testeval(session, tag, args)
                if ret is False:
                    return ret
            val = self.operate(session, tag, args)
        else:
            val = self.operate(session, tag, args)
        return val

    def operate(self, session, tag, args):
        ret = None
        # print("Operate :", args)
        if self.operator is not None:
            for i in range(len(self.operator)):
                # key = self.operator[i].key
                ret = self.operator[i].testeval(session, tag, args)
                # print("operate", self.key)
            ret = self.tgtexec(session, tag, args)
        else:
            ret = self.tgtexec(session, tag, args)
        return ret

    # pylint: disable=W0612,W0613
    def dependency(self, session, tag, args):
        if len(self.i_deps) == 0:
            return
        for k, v in self.i_deps.items():
            v.testeval(session)
        return

    def tgtexec(self, session, tag, args):
        # print (args)
        self.dependency(session, tag, args)
        ret = dict()
        if self.target is not None:
            for i in range(len(self.target)):
                key = self.target[i]
                val = self.target[i].testeval(session, tag, args)
                ret.update(dict({key: val}))
        return ret

    def postexec(self, session, tag, args):
        ret = dict()
        if self.post is not None:
            for i in range(len(self.post)):
                key = self.post[i]
                val = self.post[i].testeval(session, tag, args)
                ret.update(dict({key: val}))
        return ret

    def testeval(self, session, args):
        self.inputarg(session, "test", args)

    def code(self, session, args):
        tabs = 0
        self.codeme = code(tabs, "def rule_" + self.key + " (session):")
        tag = "test"

        tabs = 1
        for i in range(len(self.inarg)):
            self.codeme += self.inarg[i].code(session, tag, args, tabs)
        for i in range(len(self.inarg)):
            clslist = clskey(self.inarg[i].key)
            clsinst = inskey(self.inarg[i].key)
            key = self.inarg[i].key
            keylen = clslist + "len"

            self.codeme += code(tabs + i, "if " + clslist +
                                " is None or isinstance(" + clslist +
                                ", list) and len(" + clslist + ") == 0:")
            self.codeme += code(tabs + i + 1, clslist + "_len = 1")
            self.codeme += code(tabs + i, "else:")
            self.codeme += code(tabs + i + 1, keylen + " = len(" +
                                clslist + ")")
            self.codeme += code(tabs + i, "for " + key +
                                " in range(" + keylen + "):")
            self.codeme += code(tabs + i + 1, "if " + clslist +
                                " is None or isinstance(" + clslist +
                                ", list) and len(" + clslist + ") == 0:")
            self.codeme += code(tabs + i + 2, clsinst + " = None")
            self.codeme += code(tabs + i + 1, "else:")
            self.codeme += code(tabs + i + 2, clsinst + " = " + clslist +
                                "[" + key + "]")
            self.codeme += code(tabs + i + 1, "print(" + clsinst +
                                ", " + clslist + "[" + key + "])")
            self.codeme += code(0, "")

        newtab = tabs + len(self.inarg)

        if self.fargs is not None:
            for i in range(len(self.fargs)):
                self.codeme += self.fargs[i].code(session, tag, args, newtab)
                self.codeme += code(tabs + 1, "if  " +
                                    ckey(self.fargs[i].key) +
                                    " is False:")
                self.codeme += code(tabs + 2, "continue")

        if self.operator is not None:
            for i in range(len(self.operator)):
                self.codeme += self.operator[i].code(session, tag, args,
                                                     newtab)

        if self.target is not None:
            for i in range(len(self.target)):
                self.codeme += self.target[i].code(session, tag, args, newtab)

        if self.post is not None:
            for i in range(len(self.post)):
                self.codeme += self.post[i].code(session, tag, args, tabs)

        self.codeme += code(0, "rule_" + self.key + "(session)")
        print(self.codeme)
        self.log(1, self.codeme)
        return self.codeme


class rmmanager():
    """
    The class represents the Rule Manager to manage a set of rules.
    """
    def __init__(self, rulelist=[], cfgmgr=None):
        self.rulelist = rulelist
        self.ruledict = {}
        self.ruleorm = dict({})
        self.ruleclassorm = dict({})
        self.clslist = clsmanager.getAllCls()
        self.cfgmgr = cfgmgr
        self.ruleclsorm = dict({})
        for i in range(len(rulelist)):
            self.addRule(rulelist[i])
        self.logger = clsmanager.initlogger('RuleManager')

    def log(self, level, *msg):
        if self.logger is None:
            self.logger = clsmanager.initlogger(str(self.__class__))
        if self.logger is not None:
            clsmanager.logbase(self.logger, level, "".join(map(str, msg)))

    def addRule(self, rule):
        """
        Add rule to Rule Manager.
        """
        self.rulelist.append(rule)
        self.ruledict.update(rule.mydict)
        self.process()

    def initorm(self):
        """
        Init the ORM for a Rule Manager.
        """
        self.ruleorm = dict()
        self.ruleclsorm = dict()
        for i in range(len(self.clslist)):
            # Use Get from options moving forward
            operation = clsmanager.getAllOperation()
            opmap = {}
            for j in range(len(operation)):
                req = dict({operation[j]: {'rules': {}}})
                opmap.update(req)
            self.ruleclassorm.update(dict({self.clslist[i]: opmap}))

    def process(self):
        """
        Process all the rules/ORM/Priority of the Rule Manager.
        """
        self.initorm()
        self.processrules()
        self.process_priority()
        self.processorm()

    def processrules(self):
        """
        Process the rules of the Rule Manager for dependency
        evaluations and mapping.
        """
        skip_any_class = False
        for l in range(len(self.rulelist)):
            source = self.rulelist[l]
            skip_any_class = False
            dictrule = self.ruledict
            for j in range(len(source.inarg)):
                if isinstance(source.inarg[j], rmanyclass):
                    skip_any_class = True
            if skip_any_class is True:
                continue
            if source.dep is not None:
                for j in range(len(source.dep)):
                    key = source.dep[j]
                    if key in dictrule.keys():
                        value = dictrule[key]
                        source.i_deps.update({key: value})
                        # self.adddepth(source.target[i])
            if source.target is not None:
                for i in range(len(source.target)):
                    clsobj = source.target[i]
                    if isinstance(clsobj, rmanyclass):
                        continue
                    if not isinstance(clsobj, type(source.inarg[j])):
                        continue
                    if clsobj.cls not in self.ruleclassorm.keys():
                        newdict = dict({clsobj.cls: {clsobj.request:
                                                     {'rules':
                                                      {source.key: source}}}})
                        self.ruleclassorm.update(newdict)
                    else:
                        classdict = self.ruleclassorm[clsobj.cls]
                        if clsobj.request not in classdict.keys():
                            classdict.update(dict({clsobj.request:
                                                   {source.key: source}}))
                        else:
                            requestdict = classdict[clsobj.request]
                            # print(source.key)
                            rulesdict = requestdict['rules']
                            if source.key not in rulesdict.keys():
                                rulesdict.update(dict({source.key: source}))
                                requestdict.update(dict({'rules': rulesdict}))

                            classdict.update(dict({clsobj.request:
                                                   requestdict}))
                        self.ruleclassorm.update(dict({clsobj.cls: classdict}))

    def getclsrules(self, cls, op):
        """
        Get All the rules for a given class based on REST request method.
        """
        clsrule = self.ruleclassorm[cls]
        ormop = clsmanager.getConfigOperation(op)
        oprule = clsrule[ormop]

        ruledict = oprule['rules']
        if len(ruledict) != 0:
            return ruledict
        return dict({'DEF' + op: self.ruledict['DEF' + op]})

    def process_priority(self):
        """
        Process priority for all the rules.
        """
        for i in range(len(self.rulelist)):
            source = self.rulelist[i]
            if len(source.i_deps):
                # pylint: disable=W0612
                for k, v in source.i_deps.items():
                    v.priority = source.priority + 10

    def processorm(self):
        """
        Process ORM for all the rules.
        """
        for i in range(len(self.rulelist)):
            rule = self.rulelist[i]
            if rule.priority == 10:
                self.ruleorm.update(dict({rule.key: rule}))

    def displayorm(self):
        """
        Display ORM for all the rules.
        """
        retdict = dict()
        # pylint: disable=W0612
        for k, v in self.ruleorm.items():
            retdict.update(v.reprJSON())
        return retdict

    def displayclsorm(self):
        """
        Display ORM per class.
        """
        print(self.ruleclassorm)

    def run(self, key, session, inputarg=dict()):
        """
        Execute a Rule from a set of rules of Rule Manager.
        """
        # print(key)
        if key in self.ruledict.keys():
            # print(key, inputarg)
            rule = self.ruledict[key]
            return rule.testeval(session, inputarg)
        return None

    def code(self, key, session, inputarg=dict()):
        """
        Generate the code equivalent of rule from Rule Manager.
        """
        # print (key)
        if key in self.ruledict.keys():
            # print(key, inputarg)
            rule = self.ruledict[key]
            return rule.code(session, inputarg)
        return ""

    def configoprules(self, op, session, listfids, slot):
        """
        Execute Config Rules added in the Rule Manager.
        """
        inputarg = dict()
        tmplist = clsmanager.getsortedlist(op, slot)
        for i in range(len(tmplist)):
            # print(tmplist[i], op, slot)
            inputarg.update({'tgtcls': tmplist[i]})
            for j in range(len(listfids)):
                if not clsmanager.isValidrequest(self.cfgmgr,
                                                 listfids[j],
                                                 op,
                                                 tmplist[i],
                                                 slot,
                                                 session):
                    continue
                if listfids[j] is not None:
                    if listfids[j] != "None":
                        session['vfid'] = listfids[j]
                inputarg.update(dict({'tgtfid': listfids[j]}))
                inputarg.update(dict({'tgtcfgmgr': self.cfgmgr}))
                inputarg.update(dict({'tgtop': op}))
                inputarg.update(dict({'tgtslot': slot}))
                classrule = self.getclsrules(tmplist[i], op)
                # print(tmplist[i], op, slot, listfids[j])
                # pylint: disable=W0612
                for k, v in classrule.items():
                    print("Execute ", k, tmplist[i])
                    self.run(k, session, inputarg)
                    self.log(1, "Execute ", k, tmplist[i])

    def configrunrules(self, rule, cls, op, session, fid, cfgmgr):
        """
        Execute a specific config rule from Rule Manager.
        """
        inputarg = dict()
        inputarg.update(dict({'tgtcls': cls}))
        inputarg.update(dict({'tgtop': op}))
        inputarg.update(dict({'tgtfid': fid}))
        inputarg.update(dict({'tgtcfgmgr': cfgmgr}))
        if fid != "None":
            session['vfid'] = fid
        # print(rule)
        self.run(rule, session, inputarg)

    def allconfigrules(self, session, listoffids, listofslots):
        """
        Add default config Rules for all operation in Rule Manager.
        """
        allop = clsmanager.getConfigStages()
        # print(allop, listofslots)
        for i in range(len(allop)):
            self.addRule(rmrule('DEF' + allop[i], 'DEFRULE',
                         list([rmanyclass('i1', None, "GET", rmclass.diff)]),
                         None,
                         None,
                         list([
                              rmanyclass('i1',
                                         None,
                                         clsmanager.getConfigOperation(
                                             allop[i]), rmclass.diff)
                              ]),
                         None,
                         None))
        for i in range(len(allop)):
            for j in range(len(listofslots)):
                self.configoprules(allop[i], session,
                                   listoffids, listofslots[j])

    @classmethod
    def defaultconfigrules(cls):
        """
        Default config rules list for Rule Manager.
        """
        return list([DefConfigrule1,
                     DefConfigrule2,
                     DefConfigrule3,
                     DefConfigrule4,
                     DefConfigrule5,
                     DefConfigrule6,
                     DefConfigrule7,
                     DefConfigrule8,
                     DefConfigrule9,
                     DefConfigrule10,
                     DefConfigrule11,
                     DefConfigrule12,
                     DefConfigrule13])


# pylint: disable=W0105
"""
List of all predefined Rules for config management
"""

DefConfigrule1 = rmrule('R1', 'zonecreate',
                        list([rmclass('i1', effective_configuration, "GET"),
                              rmclass('i2', defined_configuration, "GET",
                                      rmclass.diff)]),
                        None,
                        list([rmcond('c1', 'and',
                                     rmcond('c2', 'set',
                                            rmattribute('i1',
                                                        'set_cfg_action'),
                                            rmconst("1")),
                                     rmcond('c3', 'set',
                                            rmattribute('i1', 'set_checksum'),
                                            rmattribute('i1',
                                                        'peek_checksum')))]),
                        list([rmclass('i2', defined_configuration,
                                      "POST")]),
                        list([rmclass('i1', effective_configuration,
                                      "PATCH")]),
                        None)

DefConfigrule2 = rmrule('R2', 'zonedelete',
                        list([rmclass('i1', effective_configuration, "GET"),
                              rmclass('i2', defined_configuration, "GET",
                                      rmclass.diff)]),
                        None,
                        list([rmcond('c1', 'and',
                                     rmcond('c2', 'set',
                                            rmattribute('i1',
                                                        'set_cfg_action'),
                                            rmconst("1")),
                                     rmcond('c3', 'set',
                                            rmattribute('i1', 'set_checksum'),
                                            rmattribute('i1',
                                                        'peek_checksum')))]),
                        list([rmclass('i2', defined_configuration,
                                      "DELETE")]),
                        list([rmclass('i1', effective_configuration,
                                      "PATCH")]),
                        None)

DefConfigrule3 = rmrule('R3', 'zonepatch',
                        list([rmclass('i1', effective_configuration, "GET"),
                              rmclass('i2', defined_configuration, "GET",
                                      rmclass.diff)]),
                        None,
                        list([rmcond('c1', 'and',
                                     rmcond('c2', 'set',
                                            rmattribute('i1',
                                                        'set_cfg_action'),
                                            rmconst("1")),
                                     rmcond('c3', 'set',
                                            rmattribute('i1', 'set_checksum'),
                                            rmattribute('i1',
                                                        'peek_checksum')))]),
                        list([rmclass('i2', defined_configuration,
                                      "PATCH")]),
                        list([rmclass('i1', effective_configuration,
                                      "PATCH")]),
                        None)

DefConfigrule4 = rmrule('R4', 'ignoredefaultroutedelete',
                        list([rmclass('i1', extension_ip_route,
                                      "GET", rmclass.diff)]),
                        list([rmcond('c1', 'not eq',
                                     rmattribute('i1', 'peek_ip_gateway'),
                                     rmconst("*"))]),
                        None,
                        list([rmclass('i1', extension_ip_route, "DELETE")]),
                        None,
                        None)
DefConfigrule5 = rmrule('R5', 'ignoredefaultroutepost',
                        list([rmclass('i1', extension_ip_route,
                                      "GET", rmclass.diff)]),
                        list([rmcond('c1', 'not eq',
                                     rmattribute('i1', 'peek_ip_gateway'),
                                     rmconst("*"))]),
                        None,
                        list([rmclass('i1', extension_ip_route, "POST")]),
                        None,
                        None)

DefConfigrule6 = rmrule('R6', 'fibrechanneldisableenable',
                        list([rmclass('i1', fibrechannel, "GET"),
                              rmclass('i2', fibrechannel, "GET", rmclass.diff),
                              rmclass('i3', fibrechannel, "GET")]),
                        list([rmcond('w3', 'and',
                                     rmcond('w4', 'eq',
                                            rmattribute('i1', 'peek_name'),
                                            rmattribute('i2', 'peek_name')),
                                     rmcond('w5', 'eq',
                                            rmattribute('i3', 'peek_name'),
                                            rmattribute('i2', 'peek_name')))]),
                        list([rmcond('c1', 'and',
                                     rmcond('c2', 'set',
                                            rmattribute('i1',
                                                        'set_enabled_state'),
                                            rmconst("6")),
                                     rmcond('c3', 'set',
                                            rmattribute('i3',
                                                        'set_enabled_state'),
                                            rmattribute('i2',
                                                        'peek_enabled_state'
                                                        )))]),
                        list([rmclass('i1', fibrechannel, "PATCH"),
                              rmclass('i2', fibrechannel, "PATCH"),
                              rmclass('i3', fibrechannel, "PATCH")]),
                        None,
                        None)

DefConfigrule7 = rmrule('R7', 'effectivepatch',
                        list([rmclass('i1', effective_configuration, "GET"),
                              rmclass('i2', effective_configuration, "GET",
                                      rmclass.diff)]),
                        None,
                        list([rmcond('c3', 'set',
                                     rmattribute('i2', 'set_checksum'),
                                     rmattribute('i1',
                                                 'peek_checksum'))]),
                        list([rmclass('i2', effective_configuration,
                                      "PATCH")]),
                        None,
                        None)

DefConfigrule8 = rmrule('R8', 'switchdisableenable',
                        list([rmclass('i1', fibrechannel_switch, "GET"),
                              rmclass('i2', fibrechannel_switch, "GET",
                                      rmclass.diff)]),
                        None,
                        list([rmcond('c1', 'set',
                                     rmattribute('i1',
                                                 'set_enabled_state'),
                                     rmconst("3"))]),
                        list([rmclass('i1', fibrechannel_switch, "PATCH"),
                              rmclass('i2', fibrechannel_switch, "PATCH",
                                      rmclass.diff)]),
                        None,
                        None)

DefConfigrule9 = rmrule('R9', 'deletealln_port_map',
                        list([rmclass('i1', n_port_map, "GET", rmclass.diff)]),
                        list([rmcond('c1', 'any',
                                     rmattribute('i1',
                                                 "peek_configured_f_port" +
                                                 "_list_f_port"), None)]),
                        None,
                        list([rmclass('i1', n_port_map, "DELETE",
                                      rmclass.diff)]),
                        None,
                        None)
DefConfigrule10 = rmrule('R10', 'patchalln_port_map',
                         list([rmclass('i1', n_port_map, "GET",
                                       rmclass.diff)]),
                         list([rmcond('c1', 'any',
                                      rmattribute('i1',
                                                  "peek_configured_f_port" +
                                                  "_list_f_port"), None)]),
                         None,
                         list([rmclass('i1', n_port_map, "PATCH",
                                       rmclass.diff)]),
                         None,
                         None)
DefConfigrule11 = rmrule('R11', 'deleteallportgroup',
                         list([rmclass('i1', port_group, "GET",
                                       rmclass.diff)]),
                         list([rmcond('c1', 'not eq',
                                      rmattribute('i1',
                                                  'peek_port_group_name'),
                                      rmconst("pg0"))]),
                         None,
                         list([rmclass('i1', port_group, "DELETE",
                                       rmclass.diff)]),
                         None,
                         None)
DefConfigrule12 = rmrule('R12', 'createallportgroup',
                         list([rmclass('i1', port_group, "GET",
                                       rmclass.diff)]),
                         list([rmcond('c1', 'not eq',
                                      rmattribute('i1',
                                                  'peek_port_group_name'),
                                      rmconst("pg0"))]),
                         None,
                         list([rmclass('i1', port_group, "POST",
                                       rmclass.diff)]),
                         None,
                         None)
DefConfigrule13 = rmrule('R13', 'patchportgroup',
                         list([rmclass('i1', port_group, "GET",
                                       rmclass.diff)]),
                         list([rmcond('c1', 'eq',
                                      rmattribute('i1',
                                                  'peek_port_group_name'),
                                      rmconst("pg0"))]),
                         None,
                         list([rmclass('i1', port_group, "PATCH",
                                       rmclass.diff)]),
                         None,
                         None)
