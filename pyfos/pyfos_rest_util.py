# Copyright © 2018-2021 Broadcom.  All rights reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.
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
#
"""
:mod:`pyfos_rest_util` - PyFOS module to provide REST support for FOS objects.
**********************************************************************************
The :mod:`pyfos_rest_util` provides a framework to add new FOS objects for REST support.

**Steps to Add REST Support for a New FOS Object**:

    1. Add a new enum for your FOS object in the rest_obj_type class.

       Module Example::

        class rest_obj_type():
          unknown         = 0
          ipif            = 11

    2. Add the name of your FOS object type in the getrestobjectname function.

       Module Example::

        elif objtype == rest_obj_type.ipif:
            return "Extension IP ADDRESS"

    3. Inherit from the rest_object class, and initialize the base class.

    4.  Add attributes as per the YANG definitions as per `Steps to Add a Rest Attribute`.

       Module Example::

        class extension_ipaddress(rest_object):
                def __init__(self, dictvalues={}):
                    super().__init__(pyfos_rest_util.rest_obj_type.ipif,
                                     "/rest/running/brocade-interface/"
                                     "extension-ip-interface")
                    self.add(pyfos_rest_util.rest_attribute("name",
                             pyfos_type.type_str, None,
                             pyfos_rest_util.REST_ATTRIBUTE_KEY))
                    self.add(pyfos_rest_util.rest_attribute("ip-address",
                             pyfos_type.type_str, None,
                             pyfos_rest_util.REST_ATTRIBUTE_KEY))
                    self.add(pyfos_rest_util.rest_attribute("dp-id",
                             pyfos_type.type_str, None,
                             pyfos_rest_util.REST_ATTRIBUTE_KEY))
                    self.add(pyfos_rest_util.rest_attribute("ip-prefix-length",
                             pyfos_type.type_str, None,
                             pyfos_rest_util.REST_ATTRIBUTE_CONFIG_MANDATORY))
                    self.add(pyfos_rest_util.rest_attribute("mtu-size",
                             pyfos_type.type_str, None,
                             pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
                    self.add(pyfos_rest_util.rest_attribute("vlan-id",
                             pyfos_type.type_str, None,
                             pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
                    self.add(pyfos_rest_util.rest_attribute("status-flags",
                             pyfos_type.type_str, None,
                             pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
                    self.load(dictvalues, 1)


**Steps to Add REST attributes in a FOS object**:
    5. Leaf attribute with no parent.

       Module Example::

           self.add(pyfos_rest_util.rest_attribute("name",
                      pyfos_type.type_str, None,
                      pyfos_rest_util.REST_ATTRIBUTE_KEY)

    6. Container or list attribute.

       Module Example::

            self.add(pyfos_rest_util.rest_attribute("l2-cos",
                     pyfos_type.type_na, dict(),
                     pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))

    7. Leaf attribute with another container or list as its parent.

        Module Example::

            self.add(pyfos_rest_util.rest_attribute("priority-control",
                     pyfos_type.type_str, None,
                     pyfos_rest_util.REST_ATTRIBUTE_CONFIG), ["l2-cos"])
            self.add(pyfos_rest_util.rest_attribute("fc-priority-high",
                     pyfos_type.type_str, None,
                     pyfos_rest_util.REST_ATTRIBUTE_CONFIG), ["l2-cos"])
            self.add(pyfos_rest_util.rest_attribute("fc-priority-medium",
                     pyfos_type.type_str, None,
                     pyfos_rest_util.REST_ATTRIBUTE_CONFIG), ["l2-cos"])
            self.add(pyfos_rest_util.rest_attribute("fc-priority-low",
                     pyfos_type.type_str, None,
                     pyfos_rest_util.REST_ATTRIBUTE_CONFIG), ["l2-cos"])
            self.add(pyfos_rest_util.rest_attribute("ip-priority-high",
                     pyfos_type.type_str, None,
                     pyfos_rest_util.REST_ATTRIBUTE_CONFIG), ["l2-cos"])
            self.add(pyfos_rest_util.rest_attribute("ip-priority-medium",
                     pyfos_type.type_str, None,
                     pyfos_rest_util.REST_ATTRIBUTE_CONFIG), ["l2-cos"])
            self.add(pyfos_rest_util.rest_attribute("ip-priority-low",
                     pyfos_type.type_str, None,
                     pyfos_rest_util.REST_ATTRIBUTE_CONFIG), ["l2-cos"])

**Generic Setters and Getters for Attributes**:
    Any attribute added in the derived class of REST object has the option to get
    and set the value for each attribute. For each attribute in the derived class a
    default setter and getter function is installed and can be invoked independently
    as and when needed.

    :Note:


     1. The getters and setters are prefixed with *peek_* or *set_*.
     2. Then it contains all the parents string starting from the top-level \
        containerun till the immediate parent concatenated with an underscore \'_\'.
     3. Then it contains the corresponding attribute name.
     4. All '-' are replaced with '_' and are in lowercase for installing the function.

    8. Leaf attribute with no parent.:

        Module Example::

            self.add(pyfos_rest_util.rest_attribute("vlan-id",
                     pyfos_type.type_str, None,
                     pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        * Default setter: **set_vlan_id**
        * Default getter: **peek_vlan_id**

        :Note:

         In test code, following can be invoked by the user.

        Script Example::

         myipobject = pyfos_extension_ipaddress.extension_ipaddress(session)
         myipobject.set_vlan_id(800)
         myipobject.peek_vlan_id()

    9. Container or List attribute.

        Module Example::

            self.add(pyfos_rest_util.rest_attribute("l2-cos",
                     pyfos_type.type_na, dict(),
                     pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))

        * Default setter: **set_l2_cos**
        * Default getter: **peek_l2cos**

        :Note:
         The value for the setter will be a list of dictionary values from its child attributes.

        Script Example::

         mytunnelobject = pyfos_extn_tunnel.extension_tunnel(session)
         mytunnelobject.set_l2_cos([{ 'priority-control": 0, 'fc-priority-high' : 1 ........}])
         mytunnelobject.peek_l2_cos()

    10. Leaf attribute with another container or list as its parent.

        Module Example::

            self.add(pyfos_rest_util.rest_attribute("fc-priority-low",
                     pyfos_type.type_str, None,
                     pyfos_rest_util.REST_ATTRIBUTE_CONFIG), ["l2-cos"])

        * Default setter: **set_l2_cos_fc_priority_low**
        * Default getter: **peek_l2cos_fc_priority_low**

        :Note:

         The value for the setter will be a list of dictionary values from its child attributes.

        Script Example::
         mytunnelobject = pyfos_extn_tunnel.extension_tunnel(session)
         mytunnelobject.set_l2_cos_fc_priority_low(5)
         mytunnelobject.peek_l2_cos_fc_priority_low()

**Versioning Support**:

    Any FOS object module can have custom versioning details defined for itself
    along with their attributes. The Attributes visibility is dependent on the
    FOS version the tests are being run against. If versioning information
    for the FOS object is not given its assumed to be supported from version
    8.2.0 onwards. Similary if the Attribute versions are not specified then
    the assumed start version for the attribute support is taken as per the
    FOS object definition. So if neither the attribute or the object has
    versioning information then its assumed to be starting from 8.2.0 onwards.


    * Versioning details:

     The version details comprise the start and end of the FOS version, and they can
     be expressed as a dictionary.

     Module Example::

       VER_RANGE_820_to_820a = {'START': "8.2.0", 'END': "8.2.0a"}
       VER_RANGE_820_and_ABOVE = {'START': "8.2.0", 'END': "9999.9999.9"}

    * Object versioning:

     The object versioning must be specified to the constructor of the super class.

     Module Example::

       super().__init__(pyfos_rest_util.rest_obj_type.ipif,
              "/rest/running/brocade-interface/vobject", VER_RANGE_820_and_ABOVE)

    * Attribute versioning:

     The attribute versioning must be given while defining the object model as per YANG.

     Module Example::

       super().__init__(pyfos_rest_util.rest_obj_type.ipif,
              "/rest/running/brocade-interface/vobject", VER_RANGE_820_to_820a)

    * Typecast support:

     The object module can be typecasted to a specific FOS version.
     The version typecast support is available for display of the object and
     for payload generation from the object.


**Module Details**:

"""


import urllib
import urllib.parse
import json
import re
import inspect
import time
import getpass
import getopt
import ast
import sys
import os
import select
import threading
# import socket
import base64
import paramiko
from pyfos import pyfos_util
from pyfos.pyfos_type import pyfos_type, rest_yang_type, rest_yang_config
from pyfos.pyfos_version import fosversion, fosversion_range, VER_RANGE_820_ABOVE


class rest_obj_type():
    """
    This class identifies the different rest objects supported by FOS
    All derived class from rest_object should define their enum here accordingly
    """
    unknown = 0
    reservedcount = 1
    pseudo_rest_object = 2
    # do no use enums from 1-9
    extension_start = 10
    ipif = 11
    iproute = 12
    tunnel = 13
    tunnel_stats = 14
    circuit = 15
    circuit_stats = 16
    ipsec = 17
    gige = 18
    gige_stats = 19
    dp_hcl_status = 20
    traffic_control_list = 21
    global_lan_statistics = 22
    lan_flow_statistics = 23
    circuit_qos_statistics = 24
    wan_statistics = 25
    extension_operation_parameters = 26
    extension_operation_status = 27
    extension_end = 100
    fos_start = 101
    zone = 102
    zone_defined = 103
    zone_effective = 104
    fabric = 105
    switch = 106
    port_config = 107
    port_stats = 108
    port_diag = 109
    fdmi_hba = 110
    fdmi_port = 111
    logical_switch = 112
    name_server = 113
    zone_fabric_lock = 114
    fabric_topology_domain = 115
    fabric_topology_route = 116
    logical_e_port = 117
    ag_show = 118
    fibrechannel_configuration_port = 121
    fibrechannel_configuration_zone = 122
    fabric_traffic_controller = 123
    lsan_zone = 123
    lsan_device = 124
    # configuration
    switch_configuration = 130
    f_port_login_settings = 131
    chassis_ha = 150
    port_trunk_area = 151
    port_trunk_show = 152
    port_trunk_perf_show = 153
    media_rdp = 154
    fan_unit = 155
    ps_unit = 156
    blade_slot = 157
    chassis_show = 158
    sensor_id = 159
    wwn_unit = 160
    history_show = 161
    routing_configuration = 162
    edge_fabric_alias = 163
    # logging
    audit = 170
    syslog = 171
    log_setting = 172
    raslog = 173
    raslog_module = 174
    log_quiet_control = 175
    error_log = 176
    audit_log = 177
    supportftp = 178
    # AG objects
    ag_start = 200
    ag_portgroup = 201
    ag_nportmap = 202
    ag_fportlist = 203
    ag_policy = 204
    ag_nportsettings = 205
    ag_device_list = 206
    ag_end = 299
    # Layer2
    portchannel = 300
    lldp_global = 301
    lldp_profile = 302
    lldp_neighbor = 303
    lldp_statistics = 304
    lldp_operations = 305
    # system security objects 400 - 500
    time_zone = 400
    clock_server = 401
    ipfilter_policy = 402
    ipfilter_rule = 403
    radius_server = 404
    tacacs_server = 405
    ldap_server = 406
    sec_crypto_cfg = 407
    sec_crypto_cfg_template = 408
    ldap_role_map = 409
    auth_spec = 410
    password_cfg = 411
    user_config = 412
    sshutil = 413
    password = 414
    security_certificate = 415
    fan_unit = 416
    ps_unit = 417
    user_specific_password_cfg = 418
    sec_crypto_cfg_template_action = 419
    security_certificate_generate = 420
    security_certificate_action = 421
    sshutil_key = 422
    sshutil_public_key = 423
    sshutil_public_key_action = 424
    security_certificate_extension = 425
    sensor_id = 426
    wwn_unit = 427
    history_show = 428
    # fos_end = 425
    # use enums from 100 onwards
    license_start = 500
    license = 501
    ports_on_demand_license_info = 502
    license_parameters = 503
    license_end = 599
    #SNMP
    snmp_start = 600
    system = 601
    mib_capability = 602
    trap_capability = 603
    v1_account = 604
    v1_trap = 605
    v3_account = 606
    v3_trap = 607
    access_control = 608
    snmp_end = 699
    # MAPS
    maps_policy = 700
    group = 701
    rule = 702
    switch_status_policy_report = 703
    monitoring_system_matrix = 704
    maps_config = 705
    paused_cfg = 706
    system_resources = 707
    dashboard_misc = 708
    dashboard_rule = 709
    credit_stall_dashboard = 710
    oversubscription_dashboard = 711
    dashboard_history = 712
    fpi_profile = 713
    #Module version
    module_version = 800
    # Supportlink
    supportlink_profile = 1000
    supportlink_history = 1001
    #RPC
    rpc_start = 5000
    rpc_show_status = 5001
    rpc_supportsave = 5002
    rpc_device_management = 5003
    fabric_operation_parameters = 5004
    slot_test = 5005
    rpc_firmwaredownload = 5006
    rpc_license = 5007
    rpc_firmwarecleaninstall = 5008
    rpc_config = 5009
    rpc_supportlink = 5010
    rpc_lldp = 5011
    zone_operation_parameters = 5012

    rpc_end = 6000
    end_user_license_agreement = 6001


def getrestobjectname(objtype, fmt=0):
    """
    This function provides the name for all instances of rest_object that are supported by FOS.
    All derived classes from rest_object should define their object name.
    """
    if fmt == 0:
        if objtype == rest_obj_type.unknown:
            return "Unknown"
        elif objtype == rest_obj_type.ipif:
            return "Extension IP ADDRESS"
        elif objtype == rest_obj_type.iproute:
            return "Extension IP ROUTE"
        elif objtype == rest_obj_type.tunnel:
            return "Extension Tunnel"
        elif objtype == rest_obj_type.tunnel_stats:
            return "Extension Tunnel stats"
        elif objtype == rest_obj_type.circuit:
            return "Extension Circuit"
        elif objtype == rest_obj_type.circuit_stats:
            return "Extension Circuit stats"
        elif objtype == rest_obj_type.ipsec:
            return "Extension IPSec"
        elif objtype == rest_obj_type.gige:
            return "Extension GigE"
        elif objtype == rest_obj_type.gige_stats:
            return "Extension GigE Stats"
        elif objtype == rest_obj_type.dp_hcl_status:
            return "Extension DP HCL Status"
        elif objtype == rest_obj_type.lan_flow_statistics:
            return "Extension LAN Flow Stats"
        elif objtype == rest_obj_type.global_lan_statistics:
            return "Extension Global LAN Stats"
        elif objtype == rest_obj_type.traffic_control_list:
            return "Extension Traffic Control List"
        elif objtype == rest_obj_type.wan_statistics:
            return "Extension WAN Statistics"
        elif objtype == rest_obj_type.extension_operation_parameters:
            return "ExtensionRPC"
        elif objtype == rest_obj_type.extension_operation_status:
            return "ExtensionRPCstatus"
        elif objtype == rest_obj_type.circuit_qos_statistics:
            return "Extension Circuit QOS Stats"
        elif objtype == rest_obj_type.zone:
            return "FOS ZONE"
        elif objtype == rest_obj_type.zone_defined:
            return "FOS Defined Zone"
        elif objtype == rest_obj_type.zone_effective:
            return "FOS Effective Zone"
        elif objtype == rest_obj_type.zone_fabric_lock:
            return "FOS Zone Fabric Lock"
        elif objtype == rest_obj_type.fabric:
            return "FOS Fabric"
        elif objtype == rest_obj_type.switch:
            return "FOS Switch"
        elif objtype == rest_obj_type.port_config:
            return "FOS Port Config"
        elif objtype == rest_obj_type.port_stats:
            return "FOS Port Stats"
        elif objtype == rest_obj_type.port_diag:
            return "FOS Port Diag"
        elif objtype == rest_obj_type.ag_portgroup:
            return "AG Port group"
        elif objtype == rest_obj_type.ag_nportmap:
            return "AG N-port map"
        elif objtype == rest_obj_type.ag_fportlist:
            return "AG F-port list"
        elif objtype == rest_obj_type.ag_policy:
            return "AG Policy"
        elif objtype == rest_obj_type.ag_nportsettings:
            return "AG N-port settings"
        elif objtype == rest_obj_type.ag_device_list:
            return "AG Device list"
        elif objtype == rest_obj_type.fdmi_hba:
            return "FOS FDMI HBA"
        elif objtype == rest_obj_type.fdmi_port:
            return "FOS FDMI Port"
        elif objtype == rest_obj_type.logical_switch:
            return "FOS Logical Switch"
        elif objtype == rest_obj_type.logical_e_port:
            return "FOS Logical Fabric"
        elif objtype == rest_obj_type.lsan_zone:
            return "FCR LSAN Zone"
        elif objtype == rest_obj_type.lsan_device:
            return "FCR LSAN Device"
        elif objtype == rest_obj_type.routing_configuration:
            return "FCR Switch Routing Configuration"
        elif objtype == rest_obj_type.edge_fabric_alias:
            return "FCR Edge Fabric Alias"
        elif objtype == rest_obj_type.name_server:
            return "FOS Name Server"
        elif objtype == rest_obj_type.ag_show:
            return "AG Show"
        elif objtype == rest_obj_type.fibrechannel_configuration_port:
            return "FOS Fibrechannel Configuration Port"
        elif objtype == rest_obj_type.fibrechannel_configuration_zone:
            return "FOS Fibrechannel Configuration Zone"
        elif objtype == rest_obj_type.time_zone:
            return "Time Zone"
        elif objtype == rest_obj_type.clock_server:
            return "Clock Sever"
        elif objtype == rest_obj_type.ipfilter_policy:
            return "IPFilter Policy"
        elif objtype == rest_obj_type.ipfilter_rule:
            return "IPFilter Rule"
        elif objtype == rest_obj_type.radius_server:
            return "Radius Server"
        elif objtype == rest_obj_type.tacacs_server:
            return "Tacacs+ Server"
        elif objtype == rest_obj_type.ldap_server:
            return "Ldap Server"
        elif objtype == rest_obj_type.sec_crypto_cfg:
            return "Seccrypto Configuration"
        elif objtype == rest_obj_type.sec_crypto_cfg_template:
            return "Seccrypto Template configuration"
        elif objtype == rest_obj_type.sec_crypto_cfg_template_action:
            return "Seccrypto Template action"
        elif objtype == rest_obj_type.ldap_role_map:
            return "LDAP role mapping"
        elif objtype == rest_obj_type.auth_spec:
            return "Authentication mode"
        elif objtype == rest_obj_type.password_cfg:
            return "Password configuration"
        elif objtype == rest_obj_type.user_specific_password_cfg:
            return "User specific password configuration"
        elif objtype == rest_obj_type.user_config:
            return "User account configuration"
        elif objtype == rest_obj_type.sshutil:
            return "sshutil for allow user name and rekey interval"
        elif objtype == rest_obj_type.sshutil_key:
            return "sshutil for keys"
        elif objtype == rest_obj_type.sshutil_public_key:
            return "sshutil for public key"
        elif objtype == rest_obj_type.sshutil_public_key_action:
            return "sshutil action for public key"
        elif objtype == rest_obj_type.password:
            return "Password Configuration"
        elif objtype == rest_obj_type.security_certificate:
            return "Show security certificate"
        elif objtype == rest_obj_type.security_certificate_generate:
            return "Generate security certificate"
        elif objtype == rest_obj_type.security_certificate_action:
            return "Security certificate action"
        elif objtype == rest_obj_type.chassis_ha:
            return "Chassis HA Status"
        elif objtype == rest_obj_type.port_trunk_area:
            return "Port Trunk Area"
        elif objtype == rest_obj_type.fan_unit:
            return "fan unit"
        elif objtype == rest_obj_type.ps_unit:
            return "powersupply unit"
        elif objtype == rest_obj_type.port_trunk_show:
            return "Trunk Show"
        elif objtype == rest_obj_type.port_trunk_perf_show:
            return "Trunk Performance Show"
        elif objtype == rest_obj_type.blade_slot:
            return "Blade details"
        elif objtype == rest_obj_type.chassis_show:
            return "Chassis details"
        elif objtype == rest_obj_type.media_rdp:
            return "media rdp details"
        elif objtype == rest_obj_type.audit:
            return "audit cfg details"
        elif objtype == rest_obj_type.syslog:
            return "syslog server details"
        elif objtype == rest_obj_type.log_setting:
            return "log setting details"
        elif objtype == rest_obj_type.supportftp:
            return "supportftp cfg details"
        elif objtype == rest_obj_type.supportlink_profile:
            return "supportlink_profile cfg details"
        elif objtype == rest_obj_type.supportlink_history:
            return "supportlink_history details"
        elif objtype == rest_obj_type.rpc_show_status:
            return "rpc show status"
        elif objtype == rest_obj_type.rpc_supportsave:
            return "rpc supportsave"
        elif objtype == rest_obj_type.rpc_device_management:
            return "rpc device management"
        elif objtype == rest_obj_type.raslog:
            return "raslog details"
        elif objtype == rest_obj_type.raslog_module:
            return "raslog module details"
        elif objtype == rest_obj_type.log_quiet_control:
            return "log quiet details"
        elif objtype == rest_obj_type.error_log:
            return "errdump logs"
        elif objtype == rest_obj_type.audit_log:
            return "auditdump logs"
        elif objtype == rest_obj_type.switch_configuration:
            return "configure switch details"
        elif objtype == rest_obj_type.f_port_login_settings:
            return "configure f-port login details"
        elif objtype == rest_obj_type.license:
            return "license"
        elif objtype == rest_obj_type.ports_on_demand_license_info:
            return "port on demand license info"
        elif objtype == rest_obj_type.license_parameters:
            return "license parameters"
        elif objtype == rest_obj_type.end_user_license_agreement:
            return "end user license agreement"
        elif objtype == rest_obj_type.system:
            return "SNMP system configuration details"
        elif objtype == rest_obj_type.mib_capability:
            return "SNMP MIB capability"
        elif objtype == rest_obj_type.trap_capability:
            return "SNMP MIB-trap capability"
        elif objtype == rest_obj_type.v1_account:
            return "SNMPv1 account details"
        elif objtype == rest_obj_type.v1_trap:
            return "SNMPv1 trap recipient details"
        elif objtype == rest_obj_type.v3_account:
            return "SNMPv3 account details"
        elif objtype == rest_obj_type.v3_trap:
            return "SNMPv3 trap / inform recipient details"
        elif objtype == rest_obj_type.access_control:
            return "SNMP access control configuration details"
        elif objtype == rest_obj_type.module_version:
            return "Module version details"
        elif objtype == rest_obj_type.security_certificate_extension:
            return "Security certificate for Extension"
        elif objtype == rest_obj_type.fabric_topology_domain:
            return "FOS Topology Domain"
        elif objtype == rest_obj_type.fabric_topology_route:
            return "FOS Topology Route"
        elif objtype == rest_obj_type.fabric_traffic_controller:
            return "FOS Fabric Traffic Controller"
        elif objtype == rest_obj_type.sensor_id:
            return "sensor details"
        elif objtype == rest_obj_type.wwn_unit:
            return "WWNcard details"
        elif objtype == rest_obj_type.history_show:
            return "history log details"
        elif objtype == rest_obj_type.fabric_operation_parameters:
            return "fabric operation parameters"
        elif objtype == rest_obj_type.slot_test:
            return "slot_test"
        elif objtype == rest_obj_type.rpc_firmwaredownload:
            return "rpc firmwaredownload"
        elif objtype == rest_obj_type.rpc_license:
            return "rpc license"
        elif objtype == rest_obj_type.rpc_firmwarecleaninstall:
            return "rpc firmwarecleaninstall"
        elif objtype == rest_obj_type.rpc_config:
            return "rpc config"
        elif objtype == rest_obj_type.zone_operation_parameters:
            return "zone operation parameters"
        else:
            return "NOT_EXT_OBJECT"
    else:
        if objtype == rest_obj_type.unknown:
            return "Unknown"
        elif objtype == rest_obj_type.ipif:
            return "ipif"
        elif objtype == rest_obj_type.iproute:
            return "iproute"
        elif objtype == rest_obj_type.tunnel:
            return "tunnel"
        elif objtype == rest_obj_type.tunnel_stats:
            return "tunnelstats"
        elif objtype == rest_obj_type.circuit:
            return "circuit"
        elif objtype == rest_obj_type.circuit_stats:
            return "circuitstats"
        elif objtype == rest_obj_type.ipsec:
            return "IPSec"
        elif objtype == rest_obj_type.gige:
            return "GigE"
        elif objtype == rest_obj_type.gige_stats:
            return "GigEStats"
        elif objtype == rest_obj_type.dp_hcl_status:
            return "DPHCLStatus"
        elif objtype == rest_obj_type.lan_flow_statistics:
            return "LANFlowStats"
        elif objtype == rest_obj_type.global_lan_statistics:
            return "GlobalLANStats"
        elif objtype == rest_obj_type.traffic_control_list:
            return "TCL"
        elif objtype == rest_obj_type.wan_statistics:
            return "WANStats"
        elif objtype == rest_obj_type.extension_operation_parameters:
            return "ExtensionRPC"
        elif objtype == rest_obj_type.extension_operation_status:
            return "ExtensionRPCstatus"
        elif objtype == rest_obj_type.circuit_qos_statistics:
            return "CircuitQOSStats"
        elif objtype == rest_obj_type.zone:
            return "zone"
        elif objtype == rest_obj_type.zone_defined:
            return "definedzone"
        elif objtype == rest_obj_type.zone_effective:
            return "effectivezone"
        elif objtype == rest_obj_type.zone_fabric_lock:
            return "zonefabriclock"
        elif objtype == rest_obj_type.fabric:
            return "Fabric"
        elif objtype == rest_obj_type.switch:
            return "Switch"
        elif objtype == rest_obj_type.port_config:
            return "portcfg"
        elif objtype == rest_obj_type.port_stats:
            return "portstats"
        elif objtype == rest_obj_type.port_diag:
            return "portdiag"
        elif objtype == rest_obj_type.name_server:
            return "nameserver"
        elif objtype == rest_obj_type.ag_show:
            return "agshow"
        elif objtype == rest_obj_type.fibrechannel_configuration_port:
            return "portconfig"
        elif objtype == rest_obj_type.fibrechannel_configuration_zone:
            return "zoneconfig"
        elif objtype == rest_obj_type.ag_portgroup:
            return "agportgroup"
        elif objtype == rest_obj_type.ag_nportmap:
            return "agnportmap"
        elif objtype == rest_obj_type.ag_fportlist:
            return "agfportlist"
        elif objtype == rest_obj_type.ag_policy:
            return "agpolicy"
        elif objtype == rest_obj_type.ag_nportsettings:
            return "agpnportsettings"
        elif objtype == rest_obj_type.ag_device_list:
            return "agdevice_list"
        elif objtype == rest_obj_type.logical_switch:
            return "Logicalswitch"
        elif objtype == rest_obj_type.logical_e_port:
            return "Logicalfabric"
        elif objtype == rest_obj_type.lsan_zone:
            return "fcrlsanzone"
        elif objtype == rest_obj_type.lsan_device:
            return "fcrlsandevice"
        elif objtype == rest_obj_type.routing_configuration:
            return "fcrroutingconfiguration"
        elif objtype == rest_obj_type.edge_fabric_alias:
            return "fcredgefabricalias"
        elif objtype == rest_obj_type.time_zone:
            return "time_zone"
        elif objtype == rest_obj_type.clock_server:
            return "clock_server"
        elif objtype == rest_obj_type.ipfilter_policy:
            return "ipfilter_policy"
        elif objtype == rest_obj_type.ipfilter_rule:
            return "ipfilter_rule"
        elif objtype == rest_obj_type.radius_server:
            return "radius_server"
        elif objtype == rest_obj_type.tacacs_server:
            return "tacacs_server"
        elif objtype == rest_obj_type.ldap_server:
            return "ldap_server"
        elif objtype == rest_obj_type.sec_crypto_cfg:
            return "sec_crypto_cfg"
        elif objtype == rest_obj_type.sec_crypto_template:
            return "sec_crypto_template"
        elif objtype == rest_obj_type.sec_crypto_template_action:
            return "sec_crypto_template_action"
        elif objtype == rest_obj_type.ldap_role_map:
            return "ldap_role_map"
        elif objtype == rest_obj_type.auth_spec:
            return "auth_spec"
        elif objtype == rest_obj_type.password_cfg:
            return "password_cfg"
        elif objtype == rest_obj_type.user_specific_password_cfg:
            return "user_specific_password_cfg"
        elif objtype == rest_obj_type.user_config:
            return "user_config"
        elif objtype == rest_obj_type.sshutil:
            return "sshutil"
        elif objtype == rest_obj_type.sshutil_key:
            return "sshutil-key"
        elif objtype == rest_obj_type.sshutil_public_key:
            return "sshutil-public-key"
        elif objtype == rest_obj_type.sshutil_public_key_action:
            return "sshutil-public-key-action"
        elif objtype == rest_obj_type.password:
            return "password"
        elif objtype == rest_obj_type.security_certificate:
            return "security_certificate"
        elif objtype == rest_obj_type.security_certificate_generate:
            return "security_certificate_generate"
        elif objtype == rest_obj_type.security_certificate_action:
            return "security_certificate_action"
        elif objtype == rest_obj_type.chassis_ha:
            return "chassishastatus"
        elif objtype == rest_obj_type.fdmi_hba:
            return "fdmihba"
        elif objtype == rest_obj_type.fdmi_port:
            return "fdmiport"
        elif objtype == rest_obj_type.logical_switch:
            return "Logicalswitch"
        elif objtype == rest_obj_type.name_server:
            return "nameserver"
        elif objtype == rest_obj_type.port_trunk_area:
            return "porttrunkarea"
        elif objtype == rest_obj_type.fan_unit:
            return "fanunitdetails"
        elif objtype == rest_obj_type.ps_unit:
            return "powersupplyunitdetails"
        elif objtype == rest_obj_type.port_trunk_show:
            return "trunkshow"
        elif objtype == rest_obj_type.port_trunk_perf_show:
            return "TrunkPerfShow"
        elif objtype == rest_obj_type.media_rdp:
            return "sfp_rdp_media"
        elif objtype == rest_obj_type.blade_slot:
            return "bladedetails"
        elif objtype == rest_obj_type.chassis_show:
            return "chassisdetails"
        elif objtype == rest_obj_type.audit:
            return "auditcfg"
        elif objtype == rest_obj_type.syslog:
            return "syslogserver"
        elif objtype == rest_obj_type.log_setting:
            return "logsetting"
        elif objtype == rest_obj_type.supportftp:
            return "trace"
        elif objtype == rest_obj_type.supportlink_profile:
            return "supportlink_profile"
        elif objtype == rest_obj_type.rpc_show_status:
            return "rpcshowstatus"
        elif objtype == rest_obj_type.rpc_supportsave:
            return "rpcsupportsave"
        elif objtype == rest_obj_type.rpc_device_management:
            return "rpc device management"
        elif objtype == rest_obj_type.raslog:
            return "raslog"
        elif objtype == rest_obj_type.raslog_module:
            return "raslog_module"
        elif objtype == rest_obj_type.log_quiet_control:
            return "log_quiet_control"
        elif objtype == rest_obj_type.error_log:
            return "error_log"
        elif objtype == rest_obj_type.audit_log:
            return "audit_log"
        elif objtype == rest_obj_type.switch_configuration:
            return "switch_configuration"
        elif objtype == rest_obj_type.f_port_login_settings:
            return "f_port_login_settings"
        elif objtype == rest_obj_type.license:
            return "license"
        elif objtype == rest_obj_type.ports_on_demand_license_info:
            return "ports_on_demand_license_info"
        elif objtype == rest_obj_type.license_parameters:
            return "license_parameters"
        elif objtype == rest_obj_type.end_user_license_agreement:
            return "end_user_license_agreement"
        elif objtype == rest_obj_type.system:
            return "system"
        elif objtype == rest_obj_type.mib_capability:
            return "mib_capability"
        elif objtype == rest_obj_type.trap_capability:
            return "trap_capability"
        elif objtype == rest_obj_type.v1_account:
            return "v1_account"
        elif objtype == rest_obj_type.v1_trap:
            return "v1_trap"
        elif objtype == rest_obj_type.v3_account:
            return "v3_account"
        elif objtype == rest_obj_type.v3_trap:
            return "v3_trap"
        elif objtype == rest_obj_type.access_control:
            return "access_ control"
        elif objtype == rest_obj_type.module_version:
            return "module_version"
        elif objtype == rest_obj_type.security_certificate_extension:
            return "security_cert_extension"
        elif rest_obj_type.fabric_topology_domain:
            return "topology_domain"
        elif rest_obj_type.fabric_topology_route:
            return "topology_route"
        elif objtype == rest_obj_type.fabric_traffic_controller:
            return "fabric_traffic_controller"
        elif objtype == rest_obj_type.wwn_unit:
            return "wwncarddetails"
        elif objtype == rest_obj_type.history_show:
            return "historydetails"
        elif objtype == rest_obj_type.sensor_id:
            return "sensordetails"
        elif objtype == rest_obj_type.fabric_operation_parameters:
            return "fabricoperationparameters"
        elif objtype == rest_obj_type.slot_test:
            return "slot_test"
        elif objtype == rest_obj_type.rpc_firmwaredownload:
            return "rpcfirmwaredownload"
        elif objtype == rest_obj_type.rpc_license:
            return "rpclicense"
        elif objtype == rest_obj_type.rpc_firmwarecleaninstall:
            return "rpcfirmwarecleaninstall"
        elif objtype == rest_obj_type.rpc_config:
            return "rpcconfig"
        elif objtype == rest_obj_type.zone_operation_parameters:
            return "zoneoperationparameters"
        else:
            return "Unknown"


class rest_get_method():
    """
    This class provides enum definition for different request methods for rest_handler class.
    Based on these enum definitions the rest handler class creates appropriate URI and or POST data for request.
    """
    GET_ALL_KEY_CONFIG = 0
    GET_ALL_KEY = 1
    GET_ALL_CONFIG = 2
    GET_MODIFIED_CONFIG = 3
    GET_KEY_AND_MODIFIED_CONFIG = 4
    GET_KEY_AND_MODIFIED_CONFIG_DELETE = 5
    GET_ALL_FILTERS = 6
    GET_ALL_FILTERS_KEY = 7


# pylint: disable=W0604
global REST_ATTRIBUTE_KEY
global REST_ATTRIBUTE_CONFIG
global REST_ATTRIBUTE_CONFIG_MANDATORY
global REST_ATTRIBUTE_NOT_CONFIG
global REST_ATTRIBUTE_CONTAINER
global REST_ATTRIBUTE_LEAF_LIST
global REST_ATTRIBUTE_CONTAINER_LIST


REST_ATTRIBUTE_KEY = (rest_yang_type.yang_leaf | rest_yang_config.yang_key)
REST_ATTRIBUTE_CONFIG = (rest_yang_type.yang_leaf | rest_yang_config.yang_config)
REST_ATTRIBUTE_CONFIG_MANDATORY = (rest_yang_type.yang_leaf | rest_yang_config.yang_config | rest_yang_config.yang_mandatory)
REST_ATTRIBUTE_NOT_CONFIG = (rest_yang_type.yang_leaf)
REST_ATTRIBUTE_CONTAINER = (rest_yang_type.yang_container | rest_yang_config.yang_config)
REST_ATTRIBUTE_CONTAINER_NOT_CONFIG = (rest_yang_type.yang_container)
REST_ATTRIBUTE_LEAF_LIST = (rest_yang_type.yang_leaf_list | rest_yang_config.yang_config)
REST_ATTRIBUTE_LEAF_LIST_NOT_CONFIG = (rest_yang_type.yang_leaf_list)
REST_ATTRIBUTE_CONTAINER_LIST = (rest_yang_type.yang_container | rest_yang_type.yang_list | rest_yang_config.yang_config)
REST_ATTRIBUTE_CONTAINER_LIST_NOT_CONFIG = (rest_yang_type.yang_container | rest_yang_type.yang_list)


IGN = 0
DBG = 1
INF = 2
WRN = 3
ERR = 4


class rest_debug():
    def __init__(self, enable=False, level=ERR, session=None):
        """Instantiate a rest_debugger"""
        self.dbg_level = level
        self.dbg_session = session
        self.dbg_mode = enable

    def isdebugverbose(self, level):
        session_dbg = 0
        if self.dbg_session is not None and 'debug' in self.dbg_session.keys():
            session_dbg = self.dbg_session['debug']
        if self.dbg_mode or session_dbg == 1:
            if self.dbg_level <= level:
                return True
        return False

    def setdbg_log(self, level, *args):
        if self.isdebugverbose(level):
            mystring = str(self.getdbg_level_string(level)) +\
                       str(" :<") + "".join(map(str, args)) + ">\nSTACK :\n" +\
                       str(inspect.stack()[2][3]) + ", " +\
                       str(inspect.stack()[3][3]) + ", " +\
                       str(inspect.stack()[3][3]) + "\n" +\
                       "Class:" + str(self.__class__) + "\n" +\
                       "Object Details:\n" + str(self) + "\n"
            if level == DBG:
                pyfos_util.print_test_green(mystring)
            if level == INF:
                pyfos_util.print_test_yellow(mystring)
            if level == ERR:
                pyfos_util.print_test_red(mystring)

    def setdbg_session(self, session):
        self.dbg_session = session

    def setdbg_level(self, level):
        self.dbg_level = level

    def setdbg_mode(self, enabled=0):
        self.dbg_mode = enabled

    def getdbg_level_string(self, level):
        if level == IGN:
            return "IGNORE"
        if level == DBG:
            return "DEBUG"
        if level == WRN:
            return "WARNING"
        if level == ERR:
            return "ERROR"
        if level == INF:
            return "INFO"

        return "UNKNOWN"


class rest_attribute_encoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, 'reprJSON'):
            return obj.reprJSON()
        else:
            return json.JSONEncoder.default(self, obj)


class rest_useropt():
    FILTER_LGETOPT = 0
    FILTER_SGETOPT = 1
    FILTER_LONGOPT = 2
    FILTER_SHRTOPT = 3
    FILTER_ALLOPT = 4
    FILTER_CMDLINE_MANDATORY = 5
    FILTER_CMDLINE_OPTIONAL = 6


class rest_attribute():
    """
    This class encompasses a REST attribute and may be a leaf or be a container attribute as per YANG.

    Attributes:
        name: The `name` of the attribute as per the YANG definition.
        is_config:  The `is_config` indicates if it is a config attribute as per YANG.
        isattributemap:  The `isattributemap` indicates if it is a container attribute as per YANG.
        is_key: The `is_key` confirms if it is key attribute.
        parent: The `parent` is the parent container of the object.

        value: The `value` of the attribute.
        note:
        1. The Leaf Attribute **value** is the value of the object.
        2. The Container Attribute **value** is the value of its children dictionary.
        3. The Leaf List Attribute **Value** is a list of values.
        4. The Container List Attribute **value** is a list of dictionary values of a child.
    """

    def __init__(self, name, a_type, value=dict(), rest_type=0, ver=None, parent=None, list_count=0):
        """Instantiate a rest_attribute """
        # TODO Compact the attribute class based on new defines
        self.name = name
        self.a_type = pyfos_type(a_type)
        self.is_key = (rest_type & rest_yang_config.yang_key)
        self.is_config = (rest_type & rest_yang_config.yang_config)
        self.is_mandatory = (rest_type & rest_yang_config.yang_mandatory)
        self.is_attribute_map = (rest_type & rest_yang_type.yang_container)
        self.is_list = (rest_type & (rest_yang_type.yang_list | rest_yang_type.yang_leaf_list))
        self.is_leaf = (rest_type & (rest_yang_type.yang_leaf | rest_yang_type.yang_leaf_list))
        self.properties = rest_type
        self.parent = parent
        self.list_count = list_count
        if self.is_attribute_map and not self.is_list:
            self.value = dict()
            for k1, v1 in value.items():
                myattrib = rest_attribute(k1, v1, self.is_key, self.is_config)
                self.value.update(myattrib.todict)
        elif self.is_list:
            if self.is_leaf:
                self.value = []
            else:
                self.value = [dict()]
        else:
            self.value = value
        self.parent_is_list = 0
        self.value_changed = 0
        self.configchanged = 0
        self.driftvalue = None
        self.configlist = dict()
        self.attrib = dict()
        if ver is not None:
            self.version_supported = fosversion_range(ver)
            self.version_active = fosversion(self.version_supported.start.to_string())
        else:
            self.version_supported = None
            self.version_active = None
        self.uname = None
        self.clone_dict = dict({'name': name, 'value': value, 'version': ver, 'type': a_type, 'prop': rest_type})
        self.hierarchy = []
        self.restobject = None
        self.filter = 0
        self.usage = None
        self.loption = None
        self.soption = None
        self.help = None
        self.optional = 0
        self.noarg = False
        self.cmdline = None
        self.row = 0

    def checkusagefilter(self, filters):
        if filters is not None and self.uname in filters or filters is None:
            return 1
        return 0

    def Iclonename(self):
        name = str(self.uname)
        if self.list_count > 0:
            name = str(self.uname) + "_" + str(self.list_count)
        return name

    def setusage(self):
        """ Sets the usage of the attribute parsing. """
        if self.checkusagefilter(None) == 0:
            return
        retdict = self.restobject.overwriteparser(self.uname)
        if retdict is None:
            retdict = self.restobject.overwriteparser(self.name)
        self.soption = None
        self.loption = str(self.getallparentstring() + self.getname())
        self.help = "set \"" + self.name + "\""
        self.optional = 0
        optional = ""
        cmdline = ""
        if retdict is not None:
            if 'help' in retdict.keys():
                self.help = retdict['help']
            if 'loption' in retdict.keys():
                self.loption = retdict['loption']
            if 'soption' in retdict.keys():
                self.soption = retdict['soption']
            if 'optional' in retdict.keys():
                if retdict['optional'] == 1:
                    optional = "[OPTIONAL]"
            loption = self.loption + "=" + self.loption.upper()
        else:
            loption = self.loption + "=VALUE"

        if self.soption is not None:
            cmdline = "-" + self.soption + " "
        else:
            cmdline = "--" + self.loption + "="

        cmdline += self.loption.upper()
        if self.optional:
            self.cmdline = " [" + cmdline + "]"
        else:
            self.cmdline = " <" + cmdline + ">"

        if self.soption is not None:
            usage_str = '{0:5}-{1:1},--{2:40}{3:35}\n'.format("", self.soption, loption, self.help + optional)
        else:
            usage_str = '{0:8}--{1:40}{2:35}\n'.format("", loption, self.help)
        self.usage = usage_str
        self.dbg_print(DBG, self.usage)

    def displaycustomcli(self):
        if self.checkusagefilter(None) == 0:
            return {self.uname: None}
        retdict = dict()
        retdict.update({"soption": self.soption})
        retdict.update({"loption": self.loption})
        retdict.update({"help": self.help})
        retdict.update({"optional": self.optional})
        retdict.update({"value": self.optional})
        return {self.uname: retdict}

    def getusage(self, filters=None):
        if self.checkusagefilter(filters):
            return self.usage
        return ""

    def getmyopts(self, useropt=rest_useropt.FILTER_LGETOPT, filters=None):
        if self.checkusagefilter(filters):
            if useropt == rest_useropt.FILTER_LGETOPT:
                opts = self.loption + "="
                return [opts]
            elif useropt == rest_useropt.FILTER_LONGOPT:
                opts = "--" + self.loption
                return opts
            elif useropt == rest_useropt.FILTER_SGETOPT:
                if self.soption is not None:
                    opts = "" + self.soption + ":"
                    return opts
                return ""
            elif useropt == rest_useropt.FILTER_SHRTOPT:
                if self.soption is not None:
                    opts = "-" + self.soption
                    return opts
                return ""
            elif useropt == rest_useropt.FILTER_ALLOPT:
                sopt = self.getmyopts(rest_useropt.FILTER_SHRTOPT, filters)
                lopt = self.getmyopts(rest_useropt.FILTER_LONGOPT, filters)
                if len(sopt) > 0:
                    return sopt, lopt
                else:
                    return lopt
            elif useropt == rest_useropt.FILTER_CMDLINE_MANDATORY:
                if self.optional == 0:
                    return self.cmdline
            elif useropt == rest_useropt.FILTER_CMDLINE_OPTIONAL:
                if self.optional == 1:
                    return self.cmdline
            else:
                self.dbg_print(ERR, "Unknown user option to getmyopts :",
                               useropt, " for ", self.name)
        return ""

    def setclonename(self):
        """ This is the cloning name and should be called after linking it with the parent is complete. """
        clonename = re.sub('-', '_', str(self.getallparentstring() + self.getname()))
        self.uname = clonename.lower()
        self.dbg_print(DBG, clonename)

    def setversion(self, ver):
        """ Sets the version of the attribute."""
        self.version_supported = fosversion_range(ver)
        self.version_active = fosversion(self.version_supported.start.to_string())
        self.clone_dict['version'] = ver

    def addfilter(self, filterme):
        self.dbg_print(DBG, "Add filter ", self.name, " Value:", self.filter)
        self.filter = filterme

    def setfilter(self):
        self.addfilter(1)

    def resetfilter(self):
        self.addfilter(0)

    def getfilter(self, setfilters):
        if self.filter == 1:
            self.dbg_print(DBG, self.name, "filter value : ", self.filter)
            setfilters.append(self.getclonename())

    def is_empty(self):
        if self.is_attribute_map and not self.is_list:
            if self.value is None:
                return True
            else:
                retdict = dict()
                empty = bool(self.restobject.configchanged != 0)
                if self.value is not None:
                    for k1, v1 in self.value.items():
                        if v1.is_empty() is False:
                            if empty is True and not v1.is_key:
                                empty = False
                            retdict[k1] = v1
                return bool(not any(retdict) or empty is True)
        if self.is_list:
            if self.is_leaf:
                if self.restobject.configchanged != 0 \
                   and self.configchanged == 0:
                    return True
                elif self.configchanged == 2:
                    return False
                return bool(len(self.value) == 0 or self.value is None)

            retarray = []
            for v1 in self.value:
                retdict = dict()
                empty = bool(self.restobject.configchanged != 0)
                for k2, v2 in v1.items():
                    if v2.is_empty() is False:
                        if empty is True and not v2.is_key:
                            empty = False
                        retdict[k2] = v2
                if len(retdict) != 0 and not empty:
                    retarray.append(retdict)
            return bool(len(retarray) == 0)
        else:
            if self.restobject.configchanged != 0:
                if (self.configchanged != 0 or self.is_key) and self.value is not None:
                    return False
                else:
                    return True
            return bool(self.value is None)

    def getmyselfrow(self, listcount):
        if self.is_attribute_map and not self.is_list:
            rows = 1
            for k1, v1 in self.value.items():
                self.dbg_print(DBG, k1, v1)
                tmprow = v1.getmyselfrow(-1)
                if tmprow > rows:
                    rows = tmprow
            return rows
        elif self.is_list:
            if self.is_leaf and not self.is_attribute_map:
                if self.value is None:
                    return 1
                elif len(self.value) == 0:
                    return 1
                else:
                    return len(self.value)
            else:
                rows = 0
                for i in range(len(self.value)):
                    if listcount == -1 or i <= listcount:
                        v1 = self.value[i]
                        tmprow = 1
                        tmprowd = 1
                        for k, v in v1.items():
                            self.dbg_print(DBG, i, k, v)
                            tmprowd = v.getmyselfrow(-1)
                            if tmprow < tmprowd:
                                tmprow = tmprowd
                        rows += tmprow
                        self.dbg_print(DBG, "LS", i, listcount,
                                       rows, tmprow)
                    else:
                        self.dbg_print(DBG, "LS", listcount, i)
                return rows
        else:
            if self.is_leaf:
                return 1
        self.dbg_print(ERR, "Default return ", self.name)
        return 1

    def getmyrow(self, listcount):
        if not self.getisconfig():
            return 0
        self.dbg_print(DBG, self.name)
        rows = self.getmyselfrow(listcount)
        self.dbg_print(DBG, self.name, rows)
        return rows

    def writemycolumn(self, ws, sr, er, filters):
        if self.getiskey() or self.getisconfig():
            self.dbg_print(DBG, sr, er)
            if self.is_attribute_map and not self.is_list:
                for k, v in self.value.items():
                    self.dbg_print(DBG, k, v)
                    v.writemycolumn(ws, sr, er, filters)
            elif self.is_list:
                if self.is_leaf and isinstance(self.value, list):
                    if filters is None or \
                       (filters is not None and self.uname in filters):
                        col = self.restobject.getmywritecolumn(self.uname)
                        llen = len(self.value)
                        wr = sr
                        for i in range(llen):
                            wr = sr + i
                            cell = ws.cell(row=(wr),
                                           column=col)
                            cell.value = self.value[i]
                            self.dbg_print(DBG, self.name, col, ":", wr,
                                           sr, er, self.value)
                else:
                    wsr = sr
                    wer = er
                    for i in range(len(self.value)):
                        tmprow = self.getmyrow(i)
                        val = self.value[i]
                        if i+1 == len(self.value):
                            wer = er
                        else:
                            wer = sr + tmprow
                        for k, v in val.items():
                            v.writemycolumn(ws, wsr, wer, filters)
                        wsr = wer
            else:
                if self.value is not None:
                    if filters is None or \
                       (filters is not None and self.uname in filters):
                        col = self.restobject.getmywritecolumn(self.uname)
                        cell = ws.cell(row=sr, column=col)
                        cell.value = self.value
                        self.dbg_print(DBG, self.name, col, ":",
                                       sr, er, self.value)

    def wsload(self, ws, sr, er, filters):
        """Loads the attribute value from ws."""
        self.dbg_print(DBG, "starting load", self.name, sr, er)
        if self.getisattributemap() and not self.getisattributelist():
            self.dbg_print(DBG, "Container", self.name)
            for k1, v1 in self.value.items():
                self.dbg_print(DBG, "Load", k1, v1)
                v1.wsload(ws, sr, er, filters)
        elif self.getisattributelist():
            if self.is_leaf:
                if filters is None or \
                   (filters is not None and self.uname in filters):
                    if not (self.getisconfig() or self.getiskey()):
                        return
                    col = self.restobject.getmyreadcolumn(self.uname)
                    listvalue = self.restobject.getlistcount(ws, sr, er, col)
                    value = list(map(lambda x: x[0], listvalue))
                    tmplist = []
                    for i in range(len(value)):
                        if value[i] is not None:
                            tmplist.append(value[i])
                    self.setInfravalue(tmplist)
            else:
                maxlistcount = 1
                listvalue = [(None, sr, er)]
                for i in range(len(self.value)):
                    for k1, v1 in self.value[i].items():
                        if (v1.getisconfig() and v1.is_leaf or v1.is_key) and\
                           not v1.is_list:
                            if filters is None or \
                               (filters is not None and v1.uname in filters):
                                col = self.restobject.getmyreadcolumn(v1.uname)
                                lvalue = self.restobject.getlistcount(ws, sr, er, col)
                                llen = len(lvalue)
                                if maxlistcount <= llen:
                                    maxlistcount = llen
                                    listvalue = lvalue
                self.dbg_print(DBG, maxlistcount, listvalue)
                for i in range(1, len(listvalue)):
                    self.clone(i)

                for i in range(maxlistcount):
                    for k1, v1 in self.value[i].items():
                        v1.wsload(ws, listvalue[i][1], listvalue[i][2], filters)
        else:
            if self.is_key or self.getisconfig():
                if filters is None or \
                   (filters is not None and self.uname in filters):
                    col = self.restobject.getmyreadcolumn(self.uname)
                    lvalue = self.restobject.getlistcount(ws, sr, er, col)
                    llen = len(lvalue)
                    if llen == 0:
                        return
                    elif llen == 1:
                        self.setInfravalue(lvalue[0][0])
                        self.dbg_print(DBG, lvalue[0][0], self.uname, self.value)
                    elif self.is_list:
                        listvalue = list(map(lambda x: x[0], lvalue))
                        tmplist = []
                        for i in range(len(listvalue)):
                            if listvalue[i] is not None:
                                tmplist.append(listvalue[i])
                        self.setInfravalue(tmplist)
                    else:
                        self.dbg_print(ERR, self.name, "->Incorrect len:",
                                       sr, er, col, llen, lvalue)
        return

    def reprJSON(self, ver=None):
        """Gets the JSON representation of the rest_attribute."""
        if self.is_attribute_map and not self.is_list:
            if self.value is None:
                return None
            elif len(self.value) == 0:
                return None
            else:
                retdict = dict()
                if self.value is not None:
                    skip = bool(self.restobject.configchanged != 0)
                    for k1, v1 in self.value.items():
                        if v1.is_empty() is False:
                            if skip is True and not v1.is_key:
                                skip = False
                            if ver is None or self.version_supported.visible(ver):
                                retdict[k1] = v1
                if len(retdict) == 0 or skip:
                    return None
                else:
                    return retdict
        if self.is_list:

            if self.is_leaf:
                if len(self.value) == 0 and self.driftvalue is None:
                    return None
                elif ver is None or self.version_supported.visible(ver):
                    if self.driftvalue is not None:
                        return dict({"Original" : str(self.value), "Drifted": str(self.driftvalue)})
                    else:
                        return self.value
                else:
                    return None

            retarray = []
            if self.value is not None:
                for v1 in self.value:
                    if ver is None or self.version_supported.visible(ver):
                        retdict = dict()
                        skip = bool(self.restobject.configchanged != 0)
                        for k2, v2 in v1.items():
                            if v2.is_empty() is False:
                                if skip is True and not v2.is_key:
                                    skip = False
                                if ver is None or v2.version_supported.visible(ver):
                                    retdict[k2] = v2
                        if len(retdict) != 0 and skip is False:
                            retarray.append(retdict)
            if len(retarray) == 0:
                return None
            else:
                return retarray
        else:
            if self.value is None and self.driftvalue is None:
                return None
            elif ver is None or self.version_supported.visible(ver):
                if self.configchanged == 2:
                    change = ""
                elif self.configchanged == 4:
                    change = "[+]"
                elif self.configchanged == 8:
                    change = "[-]"
                else:
                    change = ""
                if self.driftvalue is not None:
                    return dict({"Original" : str(self.value), "Drifted": str(self.driftvalue)})
                else:
                    if self.restobject.configchanged == 0:
                        return str(self.value)
                    else:
                        if self.configchanged != 0 or self.is_key:
                            return change + str(self.value)
                        else:
                            return None
            else:
                return None

    def getclonename(self):
        """Gets the clone name of the rest_attribute."""
        return self.uname

    def getname(self):
        """Gets the name of the rest_attribute. """
        return self.name

    def setmyconfigop(self, config):
        if not (self.getisconfig() or self.getiskey()):
            return
        self.configchanged = config
        if (self.restobject.configchanged & config) != config or self.restobject.configchanged != 0:
            self.restobject.configchanged |= config
        if self.parent is not None and config != 0:
            self.dbg_print(DBG, "Parent Config OP set :", self.parent.name)
            self.parent.setconfigoplist(self.list_count, config)
        self.dbg_print(DBG, "Set the config op", self.name,
                       config, self.restobject.configchanged)
        return

    def setconfigforallchildren(self, config):
        self.dbg_print(DBG, "Config OP set for child:", self.name,
                       "Config change", config)
        if self.is_leaf:
            self.configchanged = config
        elif self.getisattributelist():
            for i in range(len(self.value)):
                dictvalue = self.value[i]
                for k1, v1 in dictvalue.items():
                    self.dbg_print(DBG, "setconfigchildren", k1, v1)
                    v1.setconfigforallchildren(config)
        elif self.getisattributemap():
            for k1, v1 in self.value.items():
                v1.setconfigforallchildren(config)

    def setconfigoplist(self, list_count, config):
        if self.getisattributelist():
            self.dbg_print(DBG, self.name, list_count, config)
            if list_count not in self.configlist:
                self.configlist.update(dict({list_count: 0}))
            if config != 0:
                storedconfig = self.configlist[list_count]
                if config not in (storedconfig, 2):
                    self.configlist[list_count] = config
                    # special case for POST and delete handling
                    childrendict = self.value[list_count]
                    for k1, v1 in childrendict.items():
                        self.dbg_print(DBG, "setconfigoplist", k1, v1)
                        v1.setconfigforallchildren(config)

                elif storedconfig == 2 and config == 4:
                    self.configlist[list_count] = config
                    # special case for POST handling
                    childrendict = self.value[list_count]
                    for k1, v1 in childrendict.items():
                        v1.setconfigforallchildren(config)
        else:
            if self.parent is not None:
                self.parent.setconfigoplist(self.list_count, config)

    # pylint: disable=W0613
    def setparent(self, parent, list_count=0):
        """Sets the parent of the rest_attribute. """
        if parent.getisattributelist() or parent.parent_is_list:
            self.parent = parent
            self.parent_is_list = 1
        else:
            self.parent = parent

    def noparentislist(self):
        if self.parent is None:
            return True
        elif self.parent.getisattributelist():
            return False
        return self.parent.noparentislist()

    def compare(self, retdict, reset_modified=0):
        """Compares the object to the passed dictionary values. """
        if self.getisattributemap() and not self.getisattributelist():
            for k1, v1 in self.value.items():
                if isinstance(retdict, list):
                    myvalue = retdict[0]
                elif isinstance(retdict, dict):
                    myvalue = retdict
                else:
                    # TODO remove the newline check after xmltodict merge
                    if len(retdict) and retdict != '\n':
                        print("Illegal param passed for Key", self.uname, "Dict:", retdict, "\n")
                        return 1
                    else:
                        return 0
                if k1 in myvalue.keys():
                    if v1.compare(myvalue[k1]) != 0:
                        return 1
            return 0
        elif self.getisattributelist():
            if isinstance(retdict, list):
                if len(retdict) >= len(self.value):
                    # Leaf list handling
                    if self.is_leaf:
                        for i in range(len(self.value)):
                            found = 0
                            for j in range(len(retdict)):
                                if self.value[i] == retdict[j]:
                                    found = 1
                                    break
                            if found == 0:
                                return 1
                        return 0
                    else:
                        # Not a Leaf list
                        for i in range(len(self.value)):
                            value = self.value[i]
                            compare = len(value)

                            for k1, v1 in value.items():
                                for j in range(len(retdict)):
                                    compare = len(value)
                                    myvalue = retdict[j]
                                    if k1 in myvalue.keys():
                                        if v1.compare(myvalue[k1]) == 1:
                                            continue
                                        compare -= 1
                                        if compare == 0:
                                            break

                                if compare == 0:
                                    break
                            if compare != 0:
                                return compare
                    return 0
                else:
                    return 1

            else:
                if self.is_leaf:
                    for i in range(len(self.value)):
                        if self.value[i] != value:
                            return 1
                else:
                    for i in range(len(self.value)):
                        value = self.value[i]
                        compare = len(value)

                        for k1, v1 in value.items():
                            compare = len(value)
                            myvalue = retdict
                            if k1 in myvalue.keys():
                                if v1.compare(myvalue[k1]) == 1:
                                    return 1
            return 0
        else:
            if self.getiskey() and self.getisconfig():
                if value is None or value == retdict:
                    if reset_modified:
                        self.setvaluechanged(0)
                    return 1
                else:
                    self.dbg_print(ERR, "Mismatch values for Attribute ",
                                   self.getname(), "Value (",
                                   retdict, "/", self.getvalue())
                    return 0

        if reset_modified:
            self.setvaluechanged(0)
        return 1

    def modified(self):
        """Checks if any of the values in the object are modified. """
        if self.getisattributemap() and not self.getisattributelist():
            # pylint: disable=W0612
            for k1, v1 in self.value.items():
                if v1.modified() == 1:
                    return 1
        elif self.getisattributelist():
            # Leaf list handling
            if self.is_leaf:
                if self.getisvaluechanged():
                    return 1
                else:
                    return 0

            # Not leaf list
            for i in range(len(self.value.items())):
                value = self.value[i]
                for k1, v1 in value.items():
                    if v1.modified() == 1:
                        return 1
        else:
            if self.getiskey() and self.getisconfig():
                if self.getisvaluechanged():
                    return 1
        return 0

    def __eq__(self, rhs):
        return self.issameas(rhs)

    def issameas(self, other):
        if isinstance(other, self.__class__):
            if self.is_key:
                if self.getuservalue() != other.getuservalue():
                    return False
            elif self.getisattributemap() and not self.getisattributelist():
                for k1, v1 in self.value.items():
                    if k1 in other.value.keys():
                        v2 = other.value[k1]
                        if not v1.issameas(v2):
                            return False
            elif self.getisattributelist() or self.is_leaf:
                return True
        return True

    def diff(self, other, filters=None, changed=0):
        if self.is_leaf:
            if filters is not None and self.uname in filters:
                return
        else:
            if not (self.getisconfig() or self.getiskey()):
                return
        if self.getisattributemap() and not self.getisattributelist():
            for k1, v1 in self.value.items():
                if other is None:
                    v1.setmyconfigop(changed)
                elif k1 in other.value.keys():
                    v2 = other.value[k1]
                    v1.diff(v2, filters)
        elif self.getisattributelist():
            # Leaf list handling
            if self.is_leaf:
                if other is None:
                    self.setmyconfigop(changed)
                elif self.value != other.value:
                    self.driftvalue = other.value
                    if len(self.value) > 0:
                        self.setmyconfigop(2)
                    else:
                        other.setmyconfigop(8)
                return
            # Not leaf list
            for i in range(len(self.value)):
                found = 1
                haskey = 0
                dictvalue1 = self.value[i]
                skip_not_found = 0
                if other is None:
                    for k1, v1 in dictvalue1.items():
                        v1.setmyconfigop(changed)
                        v1.diff(other, filters, changed)

                else:
                    for j in range(len(other.value)):
                        found = 1
                        haskey = 0
                        dictvalue2 = other.value[j]
                        self.dbg_print(DBG, "Old DICT:", dictvalue1,
                                       "New DICT:", dictvalue2)
                        for k1, v1 in dictvalue1.items():
                            if k1 in dictvalue2.keys():
                                v2 = dictvalue2[k1]
                                self.dbg_print(DBG, "Compare old2new", v1.value, v2.value)
                                if v1.is_key:
                                    haskey = 1
                                    if v1.value is None:
                                        skip_not_found = 1

                                if not v1 == v2:
                                    found = 0
                                    self.dbg_print(DBG, "Not FOUND:", v1.value, v2.value)
                                    break

                        if found == 1:
                            for k1, v1 in dictvalue1.items():
                                if k1 in dictvalue2.keys():
                                    v2 = dictvalue2[k1]
                                    v1.diff(v2, filters)
                            break
                    if found == 0 and skip_not_found == 0:
                        for k1, v1 in dictvalue1.items():
                            self.dbg_print(DBG, "Setting Creation/modification key:", haskey)
                            if haskey == 1:
                                v1.setmyconfigop(4)
                            else:
                                v1.setmyconfigop(2)

            if other is not None:
                for i in range(len(other.value)):
                    found = 0
                    skip_not_found = 0
                    dictvalue1 = other.value[i]
                    for j in range(len(self.value)):
                        found = 1
                        dictvalue2 = self.value[j]
                        for k1, v1 in dictvalue1.items():
                            if k1 in dictvalue2.keys():
                                v2 = dictvalue2[k1]
                                self.dbg_print(DBG, "Compare new2old:", v1.value, v2.value)
                                if v1.is_key:
                                    if v1.value is None:
                                        skip_not_found = 1
                                if not v1 == v2:
                                    found = 0
                                    self.dbg_print(DBG, "Not FOUND", v1.value, v2.value)
                                    break
                        if found == 1:
                            self.dbg_print(DBG, "new2old Compare FOUND")
                            break
                    if found == 0 and skip_not_found == 0:
                        for k1, v1 in dictvalue1.items():
                            v1.setmyconfigop(8)
                            self.dbg_print(DBG, "Adding new obj for Delete", k1, v1.value)
                            break

        elif self.getiskey() or self.getisconfig():
            if other is not None:
                if self.getuservalue() != other.getuservalue():
                    self.driftvalue = other.value
                    # print("DIFF", self.name," : ", self.value, self.driftvalue)
                    if self.getiskey():
                        self.setmyconfigop(4)
                    else:
                        self.setmyconfigop(2)
            else:
                self.driftvalue = None
        return

    def clean(self, filters):
        """Checks if anything must be cleaned. """
        if filters is not None and (self.uname in filters or self.getiskey()):
            return 0

        if self.getisattributemap() and not self.getisattributelist():
            # pylint: disable=W0612
            for k1, v1 in self.value.items():
                v1.clean(filters)
        elif self.getisattributelist():
            # Leaf list handling
            if self.is_leaf:
                self.value.clear()
                self.value = []
                return 0
            # Not leaf list
            list_count = len(self.value) - 1
            if list_count > 0:
                if list_count == 1:
                    del self.value[1]
                else:
                    del self.value[1: list_count]
            for i in range(1):
                value = self.value[i]
                for k1, v1 in value.items():
                    v1.clean(filters)
        elif self.is_leaf:
            self.value = None
        return 0

    def getchildattrib(self, name, list_count=0):
        """Gets the child attribute for this attribute. """
        if self.getisattributemap() and not self.getisattributelist() and name in self.value.keys():
            return self.value[name]
        elif self.getisattributelist():
            if list_count < len(self.value):
                value = self.value[list_count]
                if name in value.keys():
                    return value[name]
        return 0

    def addchild(self, attribute, list_count=0):
        """Adds a child attribute to another attribute, which is a map. """

        # print("ADD Child", self.name, attribute.name)
        if self.getisattributemap() and not self.getisattributelist():
            self.value.update(attribute.todict())
            attribute.setparent(self)
        elif self.getisattributelist():
            if self.is_leaf:
                self.dbg_print(ERR, "Cannot add child to leaf list")
                self.dbg_print(ERR, "Cannot add attribute ",
                               attribute.name, "for parent", self.name)
            else:
                if len(self.value) <= list_count:
                    value = dict()
                    value.update(attribute.todict())
                    attribute.setparent(self)
                    self.value.append(value)
                else:
                    value = self.value[list_count]
                    value.update(attribute.todict())
                    attribute.setparent(self)
                    self.value[list_count] = value

        else:
            self.dbg_print(ERR, "Parent not an attribute map or list ",
                           self.name)
            self.dbg_print(ERR, "Cannot add attribute ",
                           attribute.name, "for parent", self.name)
            return 0

        if self.restobject.initialized == 0:
            self.addhierarchy(attribute)

        return 1

    def addhierarchy(self, attribute):
        """Adds a child attribute to another attribute, which is a map. """
        if self.getisattributelist() or self.getisattributemap():
            if self.is_leaf == 0:
                self.hierarchy.append(attribute.clone_dict)
        self.dbg_print(DBG, self.hierarchy)

    def gethierarchy(self, attribute):
        """Returns the clone hierarchy of the attribute."""
        if self.getisattributelist() or self.getisattributemap():
            return self.hierarchy

        return None

    def getuservalue(self):
        """Gets the value of the attribute. This is the external function. """
        correct_type, value = self.a_type.validate_peek(self.getvalue())
        if correct_type:
            return value
        else:
            self.dbg_print(ERR, "type of" + str(self.a_type.get_type()),
                           "missmatched to " + str(self.getvalue()))
            return "type of" + str(self.a_type.get_type()) + "missmatched to " + str(self.getvalue())

    def getvalue(self):
        """Gets the value of the attribute. This is the internal function for the object. """
        if self.getisattributemap() and not self.getisattributelist():
            mydict = dict()
            for k1, v1 in self.value.items():
                mydict.update({k1: v1.getvalue()})
            return mydict
        if self.getisattributelist():
            if self.is_leaf:
                return self.value

            mylist = []
            for i in range(len(self.value)):
                value = self.value[i]
                mydict = dict()
                for k1, v1 in value.items():
                    mydict.update({k1: v1.getvalue()})
                mylist.append(mydict)
            return mylist
        else:
            return self.value

    def is_top_level(self):
        """Checks if the attribute is top level, that is, a direct child attribute of the REST object."""
        return bool(self.getallparentstring() == "")

    def getallparentstring(self):
        """Gets all parent strings for generic setters and getters implementation. """
        if self.parent:
            getparentstring = self.parent.getallparentstring()
            return getparentstring + self.parent.getname() + "-"
        return ""

    def getiskey(self):
        """Gets the is_key value of this attribute."""
        return self.is_key

    def getisconfig(self):
        """Gets the is_config value of this attribute."""
        return self.is_config

    def getisattributemap(self):
        """Gets the isattributemap value of this attribute."""
        return self.is_attribute_map

    def getisattributelist(self):
        """Gets the isattributemap value of this attribute."""
        return self.is_list

    def todict(self):
        """Converts the attribute into a dictionary."""
        self.attrib = {self.name: self}
        return self.attrib

    def fromdict(self, attribdict):
        """Assigns the attrbiute value from a dictionary."""
        self.setvalue((attribdict[self.name]).getvalue())

    def getisvaluechanged(self):
        """Gets if the value is changed for the object."""
        return self.value_changed

    def setvaluechanged(self, changed):
        """Sets if the value is changed for the object."""
        self.value_changed = changed

    def copy(self):
        """Copies the constructor for an attribute."""
        return rest_attribute(self.name, self.value, self.is_key, self.is_config)

    def clone(self, list_count=0):
        """Clones an attribute."""
        if self.getisattributelist() or self.getisattributemap():
            hierarchy = self.restobject.gethierarchy(self.uname)
            self.dbg_print(DBG, "Hierarchy ", hierarchy, self.uname, "\n")
            self.clone_hierarchy(hierarchy, self, list_count)

    def clone_hierarchy(self, hierarchy, parent, list_count):
        """Clones the attribute hierarchy of the attribute."""
        if isinstance(hierarchy, list):
            for i in range(len(hierarchy)):
                clone_dict = hierarchy[i]
                attribute = rest_attribute(clone_dict['name'], clone_dict['type'], clone_dict['value'], clone_dict['prop'], clone_dict['version'], parent, list_count)
                if attribute.version_active < self.version_active:
                    attribute.version_active.from_string(attribute.version_active.to_string())
                attribute.restobject = self.restobject
                self.addchild(attribute, list_count)
                attribute.setclonename()
                attribute.setusage()
                self.restobject.setIndexedClonename(attribute)
                # The list_count always starts from 0 becuase we are inside a container or list
                attribute.clone(0)

    def setuservalue(self, value, changed=1, to_add=False):
        """Sets the value of the attribute external function."""
        if self.supportedop(rest_get_method.GET_ALL_KEY_CONFIG, self.version_active):
            return self.setInfravalue(value, changed, to_add)
        else:
            myfunc = self.getclonename()
            self.dbg_print(ERR, "Unsupported: ", "set_" + myfunc,
                           " function is not allowed for the attribute \"",
                           self.getname(), "\".\n")
            return {"info-code": -1, "info-message": "Incorrect call",
                    "info-type": "Unsupported set operation on attribute"}
        return dict({self.name: self.getvalue()})

    def setInfravalue(self, value, changed=1, to_add=False):
        # Validate type
        # pylint: disable=W0612
        correct_type, rvalue = self.a_type.validate_peek(value)
        if not correct_type:
            self.dbg_print(ERR, "type of" + str(self.a_type.get_type()),
                           "missmatched to ", type(value))
            return {"info-code": -1, "info-message": "Setting of the value failed",
                    "info-type": "Incorrect type/format of value passed expected \'" +
                    self.a_type.get_type_str() + "\'"}

        # validate Format
        result = self.setvalue(value, changed, to_add)

        if result:
            return {"info-code": -1, "info-message": "Setting of the value failed",
                    "info-type": "Incorrect type/format of value passed"}

        # bubble up the version default till object
        myver = self.version_active
        myparent = self.parent
        while (myparent is not None) and (myver > myparent.version_active):
            myparent.version_active.from_string(myver.to_string())
            myparent = myparent.parent
        if myver > self.restobject.version_active:
            self.restobject.version_active.from_string(myver.to_string())
            self.dbg_print(DBG, "Active Version changed:", myver.to_string())
        return dict({self.name: self.getvalue()})

    def parseInfraset(self, value, changed=1, to_add=False):
        valuedict = self.setInfravalue(value, changed, to_add)
        if isinstance(valuedict, dict):
            if "info-code" in valuedict.keys():
                print("Error :", valuedict['info-message'], "info",
                      valuedict['info-type'])
                return 1
        return 0

    def setvalue(self, value, changed=1, to_add=False):
        """Sets the value of the attribute internal function."""
        ver = self.version_active
        if self.getisattributemap() and not self.getisattributelist():
            self.dbg_print(DBG, "Container", self.name, value)
            if value is None:
                self.value.clear()
            else:
                for k1, v1 in self.value.items():
                    self.dbg_print(DBG, value)
                    myvalue = value
                    if isinstance(value, list):
                        myvalue = value[0]
                    self.dbg_print(DBG, k1, myvalue, v1)
                    if not isinstance(myvalue, dict):
                        self.dbg_print(ERR, "Incorrect non dictionary value "
                                       "passed for set \"",
                                       self.name, "\" Value:", myvalue)
                        return 1
                    if k1 in myvalue.keys():
                        if v1.version_active > ver:
                            ver.from_string(v1.version_active.to_string())
                            self.dbg_print(DBG, self.name,
                                           v1.version_active.to_string(), ver.to_string())

                        v1.setvalue(myvalue[k1], changed)
                        self.dbg_print(DBG, "calling setvalue", v1.name)

        elif self.getisattributelist():
            if isinstance(value, list):
                if self.is_leaf:
                    self.dbg_print(DBG, "Leaf List ", self.name, value)
                    if not to_add:
                        self.value.clear()
                    for v1 in value:
                        self.value.append(v1)
                    self.dbg_print(DBG, "Leaf List ", self.name,
                                   self.value, value)
                else:
                    for i in range(len(value)):
                        if len(self.value) <= i:
                            self.clone(i)

                    for i in range(len(value)):
                        self.dbg_print(DBG, "container List ", self.name,
                                       "::", value, "::", i, self.value[i])
                        myvalue = value[i]
                        if not isinstance(myvalue, dict):
                            self.dbg_print(ERR, "Incorrect non dictionary"
                                           " value passed for set \"",
                                           self.name, "\" Value:", myvalue)
                            return 1
                        objvalue = self.value[i]
                        for k1, v1 in objvalue.items():
                            if k1 in myvalue.keys():
                                v1.setvalue(myvalue[k1], changed)
            else:
                if self.is_leaf:
                    if not to_add:
                        self.value.clear()

                    self.dbg_print(DBG, "Leaf List with one entry only ",
                                   self.name, value)
                    self.value.append(value)
                else:
                    if not isinstance(value, dict):
                        self.dbg_print(ERR, "Incorrect non dictionary value "
                                       "passed for set \"", self.name,
                                       "\" Value:", value)
                        return 1

                    for i in range(len(self.value)):
                        objvalue = self.value[i]
                        for k1, v1 in objvalue.items():
                            if k1 in value.keys():
                                v1.setvalue(value[k1], changed)
        else:
            if self.a_type.get_type() == pyfos_type.type_bool:
                correct_type, rvalue = self.a_type.validate_peek(value)
                if correct_type is True:
                    if rvalue is True:
                        self.value = 'true'
                    else:
                        self.value = 'false'
                else:
                    self.dbg_print(ERR, self.name,
                                   ":Incorrect bool value found:", value)
            else:
                self.value = value

        if ver > self.version_active:
            self.version_active.from_string(ver.to_string())
        self.value_changed = changed
        return 0

    def objdisplay(self, ver=None):
        """Displays an attribute."""
        mydisplay = []
        if self.getisattributemap() or (self.getisattributelist() and self.is_leaf == 0):
            self.dbg_print(DBG, self.name, "::", self.value)
            if self.getisattributelist():
                for i in range(len(self.value)):
                    tmpdict = self.value[i]
                    list1 = []
                    for k1, v1 in tmpdict.items():
                        list1.append(tmpdict[k1].objdisplay(ver))
                    mydisplay.append(list1)
            else:
                for k1, v1 in self.value.items():
                    if ver is None or v1.version_supported.visible(ver):
                        mydisplay.append(self.value[k1].objdisplay(ver))

            mydict = {"name": self.name, "pointer": self, "value": mydisplay, "iskey": self.is_key, "isconfig": self.is_config}
        else:
            mydict = {"name": self.name, "pointer": self, "value": self.value, "iskey": self.is_key, "isconfig": self.is_config}

        self.dbg_print(DBG, mydict)
        return mydict

    def display(self, ver):
        """Displays an attribute."""
        mydisplay = []
        mydict = dict()
        if self.getisattributemap() or (self.getisattributelist() and self.is_leaf == 0):
            self.dbg_print(DBG, self.name, "::", self.value)
            if self.getisattributelist():
                for i in range(len(self.value)):
                    tmpdict = self.value[i]
                    list1 = []
                    # pylint: disable=W0612
                    for k1, v1 in tmpdict.items():
                        if v1.version_supported.visible(ver):
                            # list1.append(tmpdict[k1].display(ver))
                            list1.append(v1.display(ver))
                    if len(list1) > 0:
                        mydisplay.append(list1)
            else:
                for k1, v1 in self.value.items():
                    if v1.version_supported.visible(ver):
                        # mydisplay.append(self.value[k1].display(ver))
                        mydisplay.append(v1.display(ver))

            # mydict={"name": self.name,"value" :mydisplay}
            if self.version_supported.visible(ver):
                mydict = {self.name: mydisplay}
                self.dbg_print(DBG, self.name, "::", mydict)

        else:
            # mydict={"name": self.name, "value" : self.value}
            if self.version_supported.visible(ver):
                correct_type, value = self.a_type.validate_peek(self.getvalue())
                if correct_type:
                    mydict = {self.name: value}
                else:
                    print("processing error", self.name, self.value)

        self.dbg_print(DBG, mydict)
        return mydict

    def __repr__(self):
        return json.dumps(self, cls=rest_object_encoder, sort_keys=True, indent=4)

    def supportedop(self, op, ver):
        """Checks if the attribute is supported for the GET methods requested."""
        if self.version_supported.visible(ver) == 0:
            self.dbg_print(DBG, "Ignored class[",
                           self.display(self.version_active), "] Active Version:",
                           self.version_active.to_string(), " Requested version ",
                           ver.to_string())
            return 0
        if self.filter == 1 and op in (rest_get_method.GET_ALL_FILTERS, rest_get_method.GET_ALL_FILTERS_KEY):
            return 1
        self.dbg_print(DBG, " Name :", self.name, "config: ",
                       self.configchanged, " OP:", op, "VAL", self.value)
        if self.is_leaf:
            if op == rest_get_method.GET_ALL_KEY_CONFIG:
                # if self.getisconfig() or self.getiskey() or self.is_mandatory:
                #    return 1

                if self.restobject.configchanged == 0:
                    if self.getisconfig() or self.getiskey() or self.is_mandatory:
                        return 1
                elif (self.restobject.configchanged & 4) == 4 and self.configchanged == 4:
                    if self.getisconfig() or self.getiskey() or self.is_mandatory:
                        return 1
            if op in (rest_get_method.GET_ALL_KEY, rest_get_method.GET_ALL_FILTERS_KEY):
                # if self.getiskey():
                #    return 1
                if self.restobject.configchanged == 0:
                    if self.getiskey():
                        return 1
            if op in (rest_get_method.GET_KEY_AND_MODIFIED_CONFIG, rest_get_method.GET_KEY_AND_MODIFIED_CONFIG_DELETE):
                # if self.getisconfig() and self.getisvaluechanged() or self.getiskey():
                #    self.dbg_print(DBG, self.name, " :", self.value, "Changes:", self.getisvaluechanged())
                if self.restobject.configchanged == 0:
                    if self.getisconfig() and self.getisvaluechanged() or self.getiskey():
                        self.dbg_print(DBG, self.name, " :", self.value, "Changes:", self.getisvaluechanged())
                        return 1
                elif self.configchanged != 0 and (self.restobject.configchanged & self.configchanged) == self.configchanged:
                    if (self.configchanged == 8 or self.configchanged == 2):
                        return 1
                elif (self.restobject.configchanged & 2) == 2:
                    if self.getiskey():
                        return 1
                elif (self.restobject.configchanged & 8) == 8:
                    if self.getiskey() and self.noparentislist():
                        return 1
            if op == rest_get_method.GET_ALL_CONFIG:
                # if self.getisconfig() and not self.getiskey():
                #    return 1
                if self.restobject.configchanged == 0:
                    if self.getisconfig() and not self.getiskey():
                        return 1
                elif (self.restobject.configchanged & self.configchanged) == self.configchanged:
                    if self.getisconfig() and not self.getiskey():
                        if self.configchanged == 2:
                            return 1
            if op == rest_get_method.GET_MODIFIED_CONFIG:
                # if self.getisconfig() and self.getisvaluechanged():
                #    return 1
                if self.restobject.configchanged == 0:
                    if self.getisconfig() and self.getisvaluechanged():
                        return 1
                elif (self.restobject.configchanged & self.configchanged) == self.configchanged:
                    if self.getisconfig() and self.getisvaluechanged():
                        if self.configchanged == 2:
                            return 1
        elif self.getisattributelist():
            for i in range(len(self.value)):
                # pylint: disable=W0612
                for k1, v1 in self.value[i].items():
                    if op == rest_get_method.GET_KEY_AND_MODIFIED_CONFIG:
                        if v1.supportedop(op, ver) == 1 and not v1.is_key:
                            return 1
                    else:
                        if v1.supportedop(op, ver) == 1:
                            return 1
        elif self.getisattributemap():
            for k1, v1 in self.value.items():
                if v1.supportedop(op, ver) == 1:
                    return 1

        return 0

    def create_html_content(self, optype, version):
        """Creates the post string data equivalent for an attribute."""
        poststring = ""
        usefilter = 0
        if optype in (rest_get_method.GET_ALL_FILTERS, rest_get_method.GET_ALL_FILTERS_KEY):
            usefilter = 1
        self.dbg_print(DBG, self.name, " : ", self.value, "OP :", self.supportedop(optype, version))
        if self.getisattributemap() and not self.getisattributelist() and self.supportedop(optype, version):
            poststringchild = ""
            # pylint: disable=W0612
            if self.filter == 1 and usefilter == 1:
                return "\n<" + self.name + "></" + self.name + ">"
            else:
                for k1, v1 in self.value.items():
                    poststringchild += v1.create_html_content(optype, version)
                if len(poststringchild):
                    poststringchild = re.sub("\n", "\n\t", poststringchild)
                    poststring = "\n<" + self.name + ">" + poststringchild + "\n</" + self.name + ">"
                else:
                    return poststringchild
            return poststring
        elif self.getisattributelist() and self.supportedop(optype, version):
            if self.filter == 1 and usefilter == 1:
                return "\n<" + self.name + "></" + self.name + ">"
            elif self.value is not None:
                poststringchild = ""
                listvalue = self.value
                if isinstance(listvalue, list):
                    for i in range(len(listvalue)):
                        poststringchild = ""
                        value = listvalue[i]
                        # Leaf List Handling
                        if self.is_leaf:
                            if value is not None:
                                poststring += "\n<" + self.name + ">" + value + "</" + self.name + ">"
                        else:
                            # Not a Leaf List Handling
                            skip_only_keys = False
                            if optype == rest_get_method.GET_KEY_AND_MODIFIED_CONFIG:
                                skip_only_keys = True

                            for k1, v1 in value.items():
                                if skip_only_keys is True and v1.supportedop(optype, version) == 1 and not v1.is_key:
                                    skip_only_keys = False
                                poststringchild += v1.create_html_content(optype, version)

                            if len(poststringchild) and not skip_only_keys:
                                poststringchild = re.sub("\n", "\n\t", poststringchild)
                                poststring += "\n<" + self.name + ">" + poststringchild + "\n</" + self.name + ">"

                    return poststring
        else:
            if self.filter == 1 and usefilter == 1:
                return "\n<" + self.name + "></" + self.name + ">"
            elif self.value is not None and self.supportedop(optype, version):
                return "\n<" + self.name + ">" + str(self.value) + "</" + self.name + ">"
        return ""

    def uri_string(self, optype, ver):
        """Creates the URI string data equivalent for an attribute."""
        if (self.getisattributemap() or self.getisattributelist()) and self.is_leaf == 0:
            uristring = "/" + self.name
            if optype == rest_get_method.GET_ALL_FILTERS:
                return "\n</" + self.name + ">"
            # pylint: disable=W0612
            for k1, v1 in self.value.items():
                if v1.supportedop(optype, ver):
                    uristring += v1.uri_string()
            return uristring
        else:
            if optype == rest_get_method.GET_ALL_FILTERS:
                return "\n</" + self.name + ">"
            elif self.getvalue() is not None:
                return "/" + self.name + "/" + urllib.parse.quote(str(self.getvalue()), safe='')
        return ""

    def dbg_print(self, level, *args):
        self.restobject.dbg_print(level, args)


SSH_FAILED_PREFIX = "SSH failed:"

def ssh_cmd(login, password, ipaddr, hostkeymust, cmdstr):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    if not hostkeymust:
        ssh.set_missing_host_key_policy(paramiko.client.WarningPolicy())
    try:
        ssh.connect(ipaddr, username=login, password=password)
    # pylint: disable=W0703
    except Exception as e:
        return SSH_FAILED_PREFIX + str(e)

    e_stdin, e_stdout, e_stderr = ssh.exec_command(cmdstr)
    e_resp = e_stdout.read().decode()
    # mask pylint W0612: Unused variable 'e_stderr' (unused-variable`)
    # mask pylint W0612: Unused variable 'e_stdin' (unused-variable)
    if e_stdin is not None:
        e_stdin = None
    if e_stderr is not None:
        e_stderr = None

    ssh.close()

    return e_resp

EULA_LAST_LINE = "Effective October 1, 2019"

def ssh_eula_text(login, password, ipaddr, hostkeymust):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    if not hostkeymust:
        ssh.set_missing_host_key_policy(paramiko.client.WarningPolicy())
    try:
        ssh.connect(ipaddr, username=login, password=password)
    # pylint: disable=W0703
    except Exception as e:
        return SSH_FAILED_PREFIX + str(e)

    chan = ssh.invoke_shell()
    time.sleep(5)
    cmd = "firmwaredownload --showEULA"
    chan.send(cmd + "\n")

    last_line = ""
    eula_text = ""
    while True:
        if chan.exit_status_ready():
            break
        rl, wl, xl = select.select([chan], [], [], 0.0)
        # mask pylint W0612: Unused variable 'xl' (unused-variable)
        if xl is not None:
            xl = None
        # mask pylint W0612: Unused variable 'wl' (unused-variable)
        if wl is not None:
            wl = None
        if len(rl) > 0:
            last_line += chan.recv(1024).decode("ISO-8859-1")
            if last_line.endswith("\n") or EULA_PAGE in last_line or EULA_LAST_LINE in last_line:
                if EULA_PAGE in last_line:
                    eula_text = eula_text + last_line.replace(EULA_PAGE, "")
                    chan.send(" ")
                else:
                    eula_text = eula_text + last_line

                if EULA_LAST_LINE in last_line:
                    break

                last_line = ""

    ssh.close()

    return eula_text

MAX_PROGRESS = 330
PASSWORD_INPUT_POMPT = "Password: "
CONTINUE_PROMPT = "Do you want to continue (Y/N) [Y]:"
EULA_PROMPT1 = "Please respond with (Y/y) to accept, (N/n) to Not accept, or (D/d) to Display the EULA):"
EULA_PROMPT2 = "Please respond with (Y/y) to Accept, (N/n) to Not accept, or (D/d) to Display the EULA:"
EULA_PAGE = "Type <CR> or <SPACE BAR> to continue, <q> to stop"
NOT_SUPPORTED = "Cannot download the requested firmware because the firmware doesn't support this platform. Please enter another firmware path."

def ssh_firmwaredownload(session, login, password, ipaddr, hostkeymust, cmdstr, eula_action):
    session["fd_thread_status"] = "in-progress"
    session["fd_thread_message"] = "in-progress"
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    if not hostkeymust:
        ssh.set_missing_host_key_policy(paramiko.client.WarningPolicy())
    try:
        ssh.connect(ipaddr, username=login, password=password)
    # pylint: disable=W0703
    except Exception as e:
        session["fd_thread_status"] = "error"
        session["fd_thread_message"] = SSH_FAILED_PREFIX + str(e)
        return SSH_FAILED_PREFIX + str(e)

    chan = ssh.invoke_shell()
    time.sleep(5)
    chan.send(cmdstr + "\n")

    keep_progress = False
    progress = 0
    last_line = ""
    eula_display = False
    eula_text = ""
    while True:
        if chan.exit_status_ready():
            break
        rl, wl, xl = select.select([chan], [], [], 0.0)
        # mask pylint W0612: Unused variable 'xl' (unused-variable)
        if xl is not None:
            xl = None
        # mask pylint W0612: Unused variable 'wl' (unused-variable)
        if wl is not None:
            wl = None
        if len(rl) > 0:
            last_line += chan.recv(1024).decode()
            if last_line.endswith("\n") or CONTINUE_PROMPT in last_line or PASSWORD_INPUT_POMPT in last_line or EULA_PROMPT1 in last_line or EULA_PROMPT2 in last_line or EULA_PAGE in last_line or NOT_SUPPORTED in last_line:
                if session["debug"]:
                    if "firmwaredownload  -p" in last_line:
                        print("firmwaredownload output: command being suppressed to avoid printing password")
                    else:
                        print("firmwaredownload output:", last_line, progress, session["fd_completion"])

                if "failed" in last_line:
                    if session["debug"]:
                        print("firmwaredownload detected failed")
                    session["fd_thread_status"] = "error"
                    session["fd_thread_message"] = last_line
                    break

                if "Usage:" in last_line:
                    if session["debug"]:
                        print("firmwaredownload invalid inputs")
                    session["fd_thread_status"] = "error"
                    session["fd_thread_message"] = last_line
                    break

                if "The server is inaccessible or firmware path is invalid" in last_line:
                    if session["debug"]:
                        print("firmwaredownload unable to get the file")
                    session["fd_thread_status"] = "error"
                    session["fd_thread_message"] = last_line
                    break

                if "Cannot access the server. Please check whether the server name or IP address is valid." in last_line:
                    if session["debug"]:
                        print("firmwaredownload cannot access server")
                    session["fd_thread_status"] = "error"
                    session["fd_thread_message"] = last_line
                    break

                if "Please change passwords for switch default accounts now" in last_line:
                    if session["debug"]:
                        print("firmwaredownload asking default password change")
                    session["fd_thread_status"] = "error"
                    session["fd_thread_message"] = last_line
                    break

                if NOT_SUPPORTED in last_line:
                    if session["debug"]:
                        print("The firmware does not support the platform")
                    session["fd_thread_status"] = "error"
                    session["fd_thread_message"] = last_line
                    break

                if CONTINUE_PROMPT in last_line:
                    if session["debug"]:
                        print("firmwaredownload got prompt")
                    chan.send("\n")
                    keep_progress = True

                if PASSWORD_INPUT_POMPT in last_line:
                    if session["debug"]:
                        print("firmwaredownload got password prompt")
                    chan.send("\n")

                if eula_display:
                    if EULA_PAGE in last_line:
                        eula_text = eula_text + last_line.replace(EULA_PAGE, "")
                        chan.send(" ")
                    elif EULA_PROMPT1 in last_line or EULA_PROMPT2 in last_line:
                        chan.send("N\n")
                        session["fd_thread_status"] = "error"
                        session["fd_thread_message"] = eula_text
                        break
                    else:
                        eula_text = eula_text + last_line
                else:
                    if EULA_PROMPT1 in last_line or EULA_PROMPT2 in last_line:
                        if session["debug"]:
                            print("firmwaredownload got eula prompt", eula_action)
                        if eula_action == "accept-eula":
                            chan.send("Y\n")
                        elif eula_action == "display-eula":
                            eula_display = True
                            chan.send("D\n")
                        else:
                            chan.send("N\n")
                            break

                if "HA Rebooting ..." in last_line:
                    if session["debug"]:
                        print("firmwaredownload ha rebooting")
                    session["fd_thread_status"] = "done"
                    session["fd_thread_message"] = "done"
                    break

                if " -r " in cmdstr and "Firmware has been downloaded to the secondary partition of the switch." in last_line:
                    if session["debug"]:
                        print("firmwaredownload has downloaded to the secondary partition")
                    session["fd_thread_status"] = "done"
                    session["fd_thread_message"] = "done"
                    break

                if "firmwareactivate" in cmdstr and "No need to activate the firmware" in last_line:
                    if session["debug"]:
                        print("firmwaredownload no need to activate")
                    session["fd_thread_status"] = "error"
                    session["fd_thread_message"] = last_line
                    break

                if "Standby CP booted successfully with new firmware." in last_line:
                    if session["debug"]:
                        print("firmwaredownload Standby CP is going to reboot with new firmware.")
                    session["fd_thread_status"] = "done"
                    session["fd_thread_message"] = "done"
                    break

                session["fd_thread_message"] = last_line

                if keep_progress:
                    progress += 1
                    session["fd_completion"] = int((progress * 100) / MAX_PROGRESS)

                last_line = ""

    ssh.close()

    if session["fd_thread_status"] != "done":
        if session["debug"]:
            print("firmwaredownload return not done", last_line)
        session["fd_thread_status"] = "error"


# pylint: disable=W0613
def find_if_chassis(session, login, password, ipaddr, hostkeymust):
    ssh_resp = ssh_cmd(session["username"], session["password"], session["ip_addr"], False, "hashow")
    if session["debug"]:
        print("hashow", ssh_resp)

    if SSH_FAILED_PREFIX in ssh_resp:
        return -1, "Cannot retrieve HA information", False, ""

    if "Not supported on this platform" in ssh_resp:
        return 0, "Non-Chassis", False, ""

    standby_cp = "unknown"
    lines = ssh_resp.splitlines()
    for line in lines:
        if ": Standby," in line or ": Non-Redundant" in line:
            # pylint: disable=R1723
            if "CP0" in line:
                standby_cp = "CP0"
                break
            elif "CP1" in line:
                standby_cp = "CP1"
                break
    if session["debug"]:
        print("chassis standby is ", standby_cp)

    if standby_cp == "unknown":
        return -1, "Cannot retrieve standby information", True, ""

    ssh_resp = ssh_cmd(session["username"], session["password"], session["ip_addr"], False, "ipaddrshow")
    if session["debug"]:
        print("ipaddrshow", ssh_resp)

    if SSH_FAILED_PREFIX in ssh_resp:
        return -1, "Cannot retrieve IP address information", True, ""

    standby_ip = "unknown"
    found_standby = False
    lines = ssh_resp.splitlines()
    for line in lines:
        if found_standby and "Ethernet IP Address: " in line:
            standby_ip = line[len("Ethernet IP Address: "):]
            break

        if standby_cp in line:
            found_standby = True

    if session["debug"]:
        print("standby ip address", standby_ip)

    if standby_ip == "unknown":
        return -1, "Cannot retrieve standby ip information", True, ""

    ssh_resp = ssh_cmd(session["username"], session["password"], standby_ip, False, "version")
    if session["debug"]:
        print("version on standby", ssh_resp)

    if SSH_FAILED_PREFIX in ssh_resp:
        return -1, "Cannot retrieve access standby CP", True, ""

    return 0, "Success", True, standby_ip

FIRMWARECLEANINSTALL_REBOOT = "The system is going down for reboot NOW for firmware clean install"

def ssh_firmwarecleaninstall(session, login, password, ipaddr, hostkeymust, cmdstr, eula_action):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    if not hostkeymust:
        ssh.set_missing_host_key_policy(paramiko.client.WarningPolicy())
    try:
        ssh.connect(ipaddr, username=login, password=password)
    # pylint: disable=W0703
    except Exception as e:
        return SSH_FAILED_PREFIX + str(e)

    chan = ssh.invoke_shell()
    time.sleep(5)
    chan.send(cmdstr + "\n")

    last_line = ""
    eula_display = False
    eula_text = ""
    while True:
        if chan.exit_status_ready():
            break
        rl, wl, xl = select.select([chan], [], [], 0.0)
        # mask pylint W0612: Unused variable 'xl' (unused-variable)
        if xl is not None:
            xl = None
        # mask pylint W0612: Unused variable 'wl' (unused-variable)
        if wl is not None:
            wl = None
        if len(rl) > 0:
            last_line += chan.recv(1024).decode("ISO-8859-1")
            if last_line.endswith("\n") or CONTINUE_PROMPT in last_line or PASSWORD_INPUT_POMPT in last_line or EULA_PROMPT1 in last_line or EULA_PROMPT2 in last_line or EULA_PAGE in last_line or NOT_SUPPORTED in last_line:
                if session["debug"]:
                    if "firmwarecleaninstall  -p" in last_line:
                        print("firmwarecleaninstall output: command being suppressed to avoid printing password")
                    else:
                        print("firmwarecleaninstall output:", last_line)

                if "The system is going down for reboot NOW" in last_line:
                    if session["debug"]:
                        print("firmwwarecleaninstall is rebooting now")
                    last_line = FIRMWARECLEANINSTALL_REBOOT
                    time.sleep(20)
                    break

                if CONTINUE_PROMPT in last_line:
                    if session["debug"]:
                        print("firmwarecleaninstall got prompt")
                    chan.send("\n")

                if eula_display:
                    if EULA_PAGE in last_line:
                        eula_text = eula_text + last_line.replace(EULA_PAGE, "")
                        chan.send(" ")
                    elif EULA_PROMPT1 in last_line or EULA_PROMPT2 in last_line:
                        chan.send("N\n")
                        last_line = eula_text
                        break
                    else:
                        eula_text = eula_text + last_line
                else:
                    if EULA_PROMPT1 in last_line or EULA_PROMPT2 in last_line:
                        if session["debug"]:
                            print("firmwaredownload got eula prompt", eula_action)
                        if eula_action == "accept-eula":
                            chan.send("Y\n")
                        elif eula_action == "display-eula":
                            eula_display = True
                            chan.send("D\n")
                        else:
                            chan.send("N\n")
                            break

                if PASSWORD_INPUT_POMPT in last_line:
                    if session["debug"]:
                        print("firmwarecleaninstall got password prompt")
                    chan.send("\n")

                if "The server is inaccessible or firmware path is invalid" in last_line:
                    if session["debug"]:
                        print("firmwarecleaninstall unable to get the file")
                    break

                if NOT_SUPPORTED in last_line:
                    if session["debug"]:
                        print("The firmware is not supported on this platform")
                    break

                last_line = ""

    ssh.close()

    return last_line

CONFIG_PASSWORD_PROMPT = " password: "
CONFIG_CONTINUE_PROMPT = "Do you want to continue [y/n]:"
CONFIG_TERMINIATED_LINE = "Terminated"
CONFIG_UP_COMPLETED_LINE = "configUpload complete:"
CONFIG_REBOOT_LINE = "Rebooting!"
CONFIG_DOWN_COMPLETED_LINE = "configDownload complete:"
CONFIG_DOWN_COMPLETED_LINE2 = "port2area files downloaded successfully"
CONFIG_USAGE = "configupload Usage"
CONFIG_SEG_FAULT = "Segmentation fault"
CONFIG_UNKNOWN_ID = "unknown fabric ID"
CONFIG_NOT_PERMITTED = "configUpload not permitted"
CONFIG_DOWN_STOPPED = "configdownload stopped"
CONFIG_FID_NOT = "Configdownload failure : cannot find the specific FID"
CONFIG_DOWN_NOT_PERMITTED = "configDownload not permitted"

def ssh_config(session, login, password, ipaddr, hostkeymust, cmdstr, secure_password):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    if not hostkeymust:
        ssh.set_missing_host_key_policy(paramiko.client.WarningPolicy())
    try:
        ssh.connect(ipaddr, username=login, password=password)
    # pylint: disable=W0703
    except Exception as e:
        return SSH_FAILED_PREFIX + str(e)

    chan = ssh.invoke_shell()
    time.sleep(5)
    chan.send(cmdstr + "\n")

    last_line = ""
    while True:
        if chan.exit_status_ready():
            break
        rl, wl, xl = select.select([chan], [], [], 0.0)
        # mask pylint W0612: Unused variable 'xl' (unused-variable)
        if xl is not None:
            xl = None
        # mask pylint W0612: Unused variable 'wl' (unused-variable)
        if wl is not None:
            wl = None
        if len(rl) > 0:
            last_line += chan.recv(1024).decode("ISO-8859-1")
            if last_line.endswith("\n") or CONFIG_PASSWORD_PROMPT in last_line or CONFIG_CONTINUE_PROMPT in last_line:
                if session["debug"]:
                    if "configupload  -all" in last_line:
                        print("config output: configupload -all")
                    elif "configupload  -vf" in last_line:
                        print("config output: configupload -vf")
                    elif "configupload  -map" in last_line:
                        print("config output: configupload -map")
                    elif "configdownload  -all" in last_line:
                        print("config output: configdownload -all")
                    elif "configdownload  -vf" in last_line:
                        print("config output: configdownload -vf")
                    elif "configdownload  -map" in last_line:
                        print("config output: configdownload -map")
                    else:
                        print("config output:", last_line)

                if CONFIG_PASSWORD_PROMPT in last_line:
                    if session["debug"]:
                        print("config got password prompt")
                    chan.send(base64.b64decode(secure_password).decode("utf-8") + "\n")

                if CONFIG_CONTINUE_PROMPT in last_line:
                    if session["debug"]:
                        print("config got continue prompt")
                    chan.send("y\n")

                if CONFIG_TERMINIATED_LINE in last_line or CONFIG_UP_COMPLETED_LINE in last_line or CONFIG_REBOOT_LINE in last_line or CONFIG_DOWN_COMPLETED_LINE in last_line or CONFIG_USAGE in last_line or CONFIG_SEG_FAULT in last_line or CONFIG_UNKNOWN_ID in last_line or CONFIG_NOT_PERMITTED in last_line or CONFIG_DOWN_COMPLETED_LINE2 in last_line or CONFIG_DOWN_STOPPED in last_line or CONFIG_FID_NOT in last_line or CONFIG_DOWN_NOT_PERMITTED in last_line:
                    if session["debug"]:
                        print("breaking.")
                    break

                last_line = ""

    ssh.close()

    return last_line

REBOOT_PROMPT = "Are you sure you want to reboot the switch [y/n]?"
REBOOT_PROMPT2 = "Are you sure you want to reboot the active CP [y/n]"

def ssh_reboot(session, login, password, ipaddr, hostkeymust, cmdstr):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    if not hostkeymust:
        ssh.set_missing_host_key_policy(paramiko.client.WarningPolicy())
    try:
        ssh.connect(ipaddr, username=login, password=password)
    # pylint: disable=W0703
    except Exception as e:
        return SSH_FAILED_PREFIX + str(e)

    chan = ssh.invoke_shell()
    time.sleep(5)
    chan.send(cmdstr + "\n")

    last_line = ""
    while True:
        if chan.exit_status_ready():
            break
        rl, wl, xl = select.select([chan], [], [], 0.0)
        # mask pylint W0612: Unused variable 'xl' (unused-variable)
        if xl is not None:
            xl = None
        # mask pylint W0612: Unused variable 'wl' (unused-variable)
        if wl is not None:
            wl = None
        if len(rl) > 0:
            last_line += chan.recv(1024).decode("ISO-8859-1")
            if last_line.endswith("\n") or REBOOT_PROMPT in last_line or REBOOT_PROMPT2 in last_line:
                if session["debug"]:
                    print("reboot output:", last_line)

                if REBOOT_PROMPT in last_line or REBOOT_PROMPT2 in last_line:
                    if session["debug"]:
                        print("reboot got prompt")
                    chan.send("y\n")
                    time.sleep(10)
                    last_line = "Rebooting!"
                    break

                last_line = ""

    ssh.close()

    return last_line


LICENSE_URI = "/rest/operations/license"
FIRMWAREDOWNLOAD_URI = "/rest/operations/firmwaredownload"
FIRMWARECLEANINSTALL_URI = "/rest/operations/firmwarecleaninstall"
SHOW_STATUS_URI = "/rest/operations/show-status"
CHASSIS_URI = "/rest/running/brocade-chassis/chassis"
LICENSE_EULA_URI = "/rest/running/brocade-license/end-user-license-agreement"
CONFIG_URI = "/rest/operations/config"
SSH_URIS = [
    {
        "uri": LICENSE_URI,
        "rest_fos_version": fosversion("9.0.0")
    },
    {
        "uri": FIRMWAREDOWNLOAD_URI,
        "rest_fos_version": fosversion("9.0.0")
    },
    {
        "uri": FIRMWARECLEANINSTALL_URI,
        "rest_fos_version": fosversion("9.0.0")
    },
    {
        "uri": CHASSIS_URI,
        "rest_fos_version": fosversion("9.0.0")
    },
    {
        "uri": LICENSE_EULA_URI,
        "rest_fos_version": fosversion("9.0.0")
    },
    {
        # there are no plans for configupload/download support in rest
        "uri": CONFIG_URI,
        "rest_fos_version": fosversion("9999.9999.9")
    }
    ]

class rest_handler(rest_debug):
    """ This class encompasses all the REST operations supported from the FOS objects as per YANG.

    Attributes:
        session: The login `session` to a FOS switch.
        uri_base:  The `uri_base` is the base URI string to access the corresponding object.
        obj:  The `obj` is the corresponding REST object instance for rest_handler to work on.
        test: The `test` dictionary captures all the different test executions.

    """
    # pylint: disable=W0602
    global test
    test = dict()
    test.update({1: {"total_tc": 0, "show_all": 0, "get": 0, "get_uri": 0, "post": 0, "patch": 0, "create_uri": 0, "delete": 0, "delete_uri": 0, "modify_put": 0, "modify_put_uri": 0, "modify_patch": 0, "modify_patch_uri": 0}})

    def __init__(self, uri):
        rest_debug.__init__(self)
        self.urilist = uri
        self.obj = self
        self.uri_base = None
        if self.obj.obj_type not in test.keys():
            test.update({self.obj.obj_type: {"show_all": 0, "get": 0, "get_uri": 0, "post": 0, "patch": 0, "create_uri": 0, "delete": 0, "delete_uri": 0, "modify_put": 0, "modify_put_uri": 0, "modify_patch": 0, "modify_patch_uri": 0}})

    def createtest(self, request, negative=0):
        dictglobal = test[1]
        dictobj = test[self.obj.obj_type]
        counttotal = dictglobal['total_tc']
        counttotal += 1
        countg = dictglobal[request]
        countg += 1
        counto = dictobj[request]
        counto += 1

        dictglobal[request] = countg
        dictobj[request] = counto
        dictglobal['total_tc'] = counttotal
        mytestcase = "Testing " + request + " for " + getrestobjectname(self.obj.obj_type) + str(self.__class__)
        testcaseID = "Rest" + str(counttotal) + "." + request + "." + str(countg) + getrestobjectname(self.obj.obj_type, 1) + "." + str(counto) + ""
        pyfos_util.test_title_set(testcaseID.upper(), mytestcase.upper())
        pyfos_util.test_negative_test_set(negative)
        time.sleep(3)

    def isvalidsession(self, session):
        nocred = session.get("nocredential", False)
        # print self.session
        if not nocred and isinstance(session, dict) and \
           "credential" in session.keys():
            if "Authorization" in session['credential'].keys():
                return 1
        return 0

    def checkstatus(self, retdict):
        if len(retdict) and isinstance(retdict, dict):
            if 'success-code' in retdict.keys():
                return True
            elif 'errors' in retdict.keys():
                return False
            else:
                return True

        return False

    def validate(self, negative, retdict):
        if self.checkstatus(retdict):
            if not negative:
                getdict = self.show(0, 0)
                if self.checkstatus(getdict):
                    # showstr = json.dumps(getdict, sort_keys=True)
                    # objstr self.obj.display()
                    # objstr = json.dumps(self.obj.display(), sort_keys=True)
                    # if re.search(objstr, showstr):
                        # print "found"
                    # print "Show:\n", showstr
                    # print "\nOBJ:\n", objstr
                    if self.obj.container in getdict.keys() and self.obj.compare(getdict) == 1:
                        # pyfos_util.test_explicit_result_failed("Objects do not match")
                        print("Return Dict:\n", getdict, "\nObj Display:\n")
                        self.obj.display()
                        # print "\n"

        return retdict

    def process_ssh_license_id(self, session):
        if session["debug"]:
            print("cmd requested licenseidshow")

        ssh_resp = ssh_cmd(session["username"], session["password"], session["ip_addr"], False, "licenseidshow")

        return ssh_resp.rstrip()

    def process_ssh_eula(self, session):
        if session["debug"]:
            print("cmd requested eula_text")

        ssh_resp = ssh_eula_text(session["username"], session["password"], session["ip_addr"], False)

        retval = {}
        retval["text"] = ssh_resp
        return retval

    def show_all(self, session, negative=0, is_tc=0):
        ret = self.obj.is_valid(session)
        if ret["info-code"] != 0:
            return ret
        if is_tc:
            self.createtest("show_all", negative)
        retdict = {}
        if self.uri_base == LICENSE_EULA_URI:
            if self.is_ssh(session, self.uri_base, session["version"]):
                retdict["end-user-license-agreement"] = self.process_ssh_eula(session)
            else:
                retdict = pyfos_util.get_request(session, self.uri_base, "")
        else:
            retdict = pyfos_util.get_request(session, self.uri_base, "")

        if pyfos_util.is_failed_resp(retdict):
            return retdict

        if self.uri_base == CHASSIS_URI:
            if self.is_ssh(session, self.uri_base, session["version"]):
                retdict["chassis"]["license-id"] = self.process_ssh_license_id(session)

        return retdict

    def get(self, session, negative=0, is_tc=0):
        ret = self.obj.is_valid(session)
        if ret["info-code"] != 0:
            return ret
        if is_tc:
            self.createtest("get", negative)
        if self.isfilterset() > 0:
            ret = pyfos_util.get_request(session, self.uri_base, self.obj.create_html_content(rest_get_method.GET_ALL_FILTERS_KEY, session))
        else:
            ret = pyfos_util.get_request(session, self.uri_base, self.obj.create_html_content(rest_get_method.GET_ALL_KEY, session))
        return ret

    def get_uri(self, session, negative=0, is_tc=0):
        ret = self.obj.is_valid(session)
        if ret["info-code"] != 0:
            return ret
        if is_tc:
            self.createtest("get_uri", negative)
        ret = pyfos_util.get_request(session, self.uri_base + self.obj.uri_string(rest_get_method.GET_ALL_KEY, session), "")
        self.dbg_print(DBG, "GET URI:\n", self.uri_base + self.obj.uri_string(rest_get_method.GET_ALL_KEY, session), ret)
        return ret

    def options(self, session, negative=0, is_tc=0):
        ret = self.obj.is_valid(session)
        if ret["info-code"] != 0:
            return ret
        if is_tc:
            self.createtest("options", negative)
        ret = pyfos_util.options_request(session, self.uri_base, self.obj.create_html_content(0, session))
        self.dbg_print(DBG, "Options:\n", self.uri_base, self.obj.create_html_content(0, session), ret)
        return ret

    def is_ssh(self, session, uri, c_version):
        # if uri is show status and message id is created by pyfos
        # this is async task created through ssh
        if uri == SHOW_STATUS_URI:
            if self.peek_message_id() == 0:
                if session["debug"]:
                    print("show-status URI requires SSH", uri, c_version.to_string(), self.peek_message_id())
                return True

        for sshentry in SSH_URIS:
            if sshentry["uri"] == uri and c_version.__lt__(sshentry["rest_fos_version"]):
                if session["debug"]:
                    print("URI requires SSH", uri, c_version.to_string())
                return True
        return False

    def process_ssh_license(self, session):
        ret_dict = {"Response" : {"license-operation-status" : {"status-message": "NA"}}}
        cmd = ""
        if self.peek_action() == "install":
            cmd = "licenseadd " + self.peek_name()
        elif self.peek_action() == "remove":
            cmd = "licenseremove " + self.peek_name()
        else:
            ret_dict["Response"]["license-operation-status"]["status-message"] = "Unknown action"

        if session["debug"]:
            print("cmd requested", cmd)

        ssh_resp = ssh_cmd(session["username"], session["password"], session["ip_addr"], False, cmd)

        if ssh_resp.startswith("\nLicense Added"):
            ret_dict["Response"]["license-operation-status"]["status-message"] = "License Install success"
        elif ssh_resp.startswith("\nLicense Removed"):
            ret_dict["Response"]["license-operation-status"]["status-message"] = "License Remove success"
        else:
            ret_dict["Response"]["license-operation-status"]["status-message"] = ssh_resp.replace("\n", " ")

        return ret_dict

    def process_ssh_firmwarecleaninstall(self, session):
        ret_dict = {"Response" : {"firmwarecleaninstall-operation-status" : {"status-message": "NA"}}}
        cmd = "firmwarecleaninstall "

        if self.peek_protocol() is  None:
            ret_dict["Response"]["firmwarecleaninstall-operation-status"]["status-message"] = "Protocol (ftp/scp/sftp) required"
            return ret_dict
        else:
            cmd = cmd + " -p " + self.peek_protocol()

        if self.peek_host() is  None:
            ret_dict["Response"]["firmwarecleaninstall-operation-status"]["status-message"] = "Host name required"
            return ret_dict
        else:
            cmd = cmd + " " + self.peek_host() + ","

        if self.peek_user_name() is  None:
            ret_dict["Response"]["firmwarecleaninstall-operation-status"]["status-message"] = "User name required"
            return ret_dict
        else:
            cmd = cmd + self.peek_user_name() + ","

        if self.peek_remote_directory() is  None:
            ret_dict["Response"]["firmwarecleaninstall-operation-status"]["status-message"] = "Remote directory required"
            return ret_dict
        else:
            cmd = cmd + self.peek_remote_directory() + ","

        if session["debug"]:
            print("cmd requested without password", cmd)

        if self.peek_password() is  None:
            ret_dict["Response"]["firmwarecleaninstall-operation-status"]["status-message"] = "Password required"
            return ret_dict
        else:
            try:
                cmd = cmd + base64.b64decode(self.peek_password()).decode("utf-8")
            # pylint: disable=W0702
            except:
                ret_dict["Response"]["firmwarecleaninstall-operation-status"]["status-message"] = "Password cannot be decoded"
                return ret_dict

        retval, msg, is_chassis, standby_ip = find_if_chassis(session, session["username"], session["password"], session["ip_addr"], False)

        if retval < 0:
            ret_dict = {"Response" : {"firmwareclean-operation-status" : {"status-message": msg}}}
        else:
            ssh_resp = ""
            if is_chassis is False:
                ssh_resp = ssh_firmwarecleaninstall(session, session["username"], session["password"], session["ip_addr"], False, cmd, self.peek_eula_action())
                ret_dict = {"Response" : {"firmwareclean-operation-status" : {"status-message": ssh_resp}}}
            else:
                ssh_resp = ssh_firmwarecleaninstall(session, session["username"], session["password"], standby_ip, False, cmd, self.peek_eula_action())

                if FIRMWARECLEANINSTALL_REBOOT in ssh_resp:
                    ssh_resp = ssh_firmwarecleaninstall(session, session["username"], session["password"], session["ip_addr"], False, cmd, self.peek_eula_action())
                    if FIRMWARECLEANINSTALL_REBOOT in ssh_resp:
                        ret_dict = {"Response" : {"firmwareclean-operation-status" : {"status-message": ssh_resp}}}
                    else:
                        ret_dict = {"Response" : {"firmwareclean-operation-status" : {"status-message": "Standby firmearecleaninstall success. Active firmwarecleaninstall failed: " + ssh_resp}}}
                else:
                    ret_dict = {"Response" : {"firmwareclean-operation-status" : {"status-message": "Standby firmwarecleaninstall failed: " + ssh_resp}}}

        return ret_dict

    def process_ssh_config(self, session):
        ret_dict = {"Response" : {"config-operation-status" : {"status-message": "NA"}}}
        cmd = ""

        if self.peek_upload() is  None:
            ret_dict["Response"]["config-operation-status"]["status-message"] = "Indicate upload or download"
            return ret_dict
        else:
            if self.peek_upload() is  True:
                cmd = cmd + "configupload "
            else:
                cmd = cmd + "configdownload "

        if self.peek_type() is  None:
            ret_dict["Response"]["config-operation-status"]["status-message"] = "Indicate all, vf, or map"
            return ret_dict
        else:
            if self.peek_type() == "all":
                cmd = cmd + " -all"
            elif "vf" in self.peek_type():
                cmd = cmd + " -vf"
            elif "fid" in self.peek_type():
                fid = self.peek_type()[4:]
                try:
                    int_fid = int(fid)
                except Exception as ex:
                    ret_dict["Response"]["config-operation-status"]["status-message"] = "Unknown type. fid option should include fid in the form of fid=xx"
                    return ret_dict
                cmd = cmd + " -fid " + str(int_fid)
            elif "map" in self.peek_type():
                valid_fid = True
                fid = self.peek_type()[4:]
                try:
                    int_fid = int(fid)
                except Exception as ex:
                    valid_fid = False

                if valid_fid:
                    cmd = cmd + " -fid " + str(int_fid) + " -map"
                else:
                    cmd = cmd + " -all -map"
            else:
                ret_dict["Response"]["config-operation-status"]["status-message"] = "Unknown type. Indicate all, vf, or map"
                return ret_dict

        if self.peek_protocol() is None:
            ret_dict["Response"]["config-operation-status"]["status-message"] = "Protocol (ftp/scp/sftp) required"
            return ret_dict
        else:
            cmd = cmd + " -p " + self.peek_protocol()
            if self.peek_protocol() == "scp" or self.peek_protocol() == "sftp":
                cmd = cmd + " -P 22 "

        if self.peek_host() is None:
            ret_dict["Response"]["config-operation-status"]["status-message"] = "Host name required"
            return ret_dict
        else:
            cmd = cmd + " " + self.peek_host() + ","

        if self.peek_user_name() is None:
            ret_dict["Response"]["config-operation-status"]["status-message"] = "User name required"
            return ret_dict
        else:
            cmd = cmd + self.peek_user_name() + ","

        if self.peek_path() is None:
            ret_dict["Response"]["config-operation-status"]["status-message"] = "Path and filename required"
            return ret_dict
        else:
            cmd = cmd + self.peek_path() + ","

        if session["debug"]:
            print("cmd requested without password", cmd)

        # password is always passed interatively to avoid weird bash shell
        # issues with special characters
        if self.peek_password() is None:
            ret_dict["Response"]["config-operation-status"]["status-message"] = "Password required"
            return ret_dict
        else:
            if self.peek_protocol() == "ftp":
                cmd = cmd + base64.b64decode(self.peek_password()).decode("utf-8")

        if self.peek_upload() is False:
            ssh_resp = ssh_cmd(session["username"], session["password"], session["ip_addr"], False, "chassisdisable -force")
            if ssh_resp != "":
                ret_dict = {"Response" : {"config-operation-status" : {"status-message": "failed to chassisdisable for configdownload"}}}
                return ret_dict

        ssh_resp = ssh_config(session, session["username"], session["password"], session["ip_addr"], False, cmd, self.peek_password())
        if self.peek_upload() is True:
            ret_dict = {"Response" : {"config-operation-status" : {"status-message": ssh_resp.replace("\n", " ").replace("\r", " ")}}}
        else:
            if CONFIG_DOWN_COMPLETED_LINE in ssh_resp:
                ssh_resp = ssh_reboot(session, session["username"], session["password"], session["ip_addr"], False, "reboot")
            if CONFIG_DOWN_COMPLETED_LINE2 in ssh_resp:
                ssh_resp = ssh_reboot(session, session["username"], session["password"], session["ip_addr"], False, "reboot")

            ret_dict = {"Response" : {"config-operation-status" : {"status-message": ssh_resp.replace("\n", " ").replace("\r", " ")}}}

        return ret_dict


    def process_ssh_firmwaredownload(self, session):
        ret_dict = {'show-status': {'message-id': '0', 'status': 'queued', 'application-name': 'RESTAPI', 'percentage-complete': '0', 'operation': 'firmwaredownload', 'firmwaredownload': {'message': 'XXX'}}}
        cmd = ""

        if self.peek_activate() is True:
            cmd = "firmwareactivate"

            if session["debug"]:
                print("cmd requested", cmd)
        else:

            cmd = "firmwaredownload "

            if self.peek_stage() is True:
                cmd = cmd + " -r "

            if self.peek_protocol() is None:
                ret_dict["show-status"]["firmwaredownload"]["message"] = "Protocol (ftp/scp/sftp) required"
                return ret_dict
            else:
                if "scp" in self.peek_protocol() or "ftp" in self.peek_protocol() or "sftp" in self.peek_protocol():
                    cmd = cmd + " -p " + self.peek_protocol()
                else:
                    ret_dict["show-status"]["firmwaredownload"]["message"] = "Protocol (ftp/scp/sftp) required"
                    return ret_dict

            if self.peek_host() is None:
                ret_dict["show-status"]["firmwaredownload"]["message"] = "Host name required"
                return ret_dict
            else:
                cmd = cmd + " " + self.peek_host() + ","

            if self.peek_user_name() is None:
                ret_dict["show-status"]["firmwaredownload"]["message"] = "User name required"
                return ret_dict
            else:
                cmd = cmd + self.peek_user_name() + ","

            if self.peek_remote_directory() is None:
                ret_dict["show-status"]["firmwaredownload"]["message"] = "Remote directory required"
                return ret_dict
            else:
                cmd = cmd + self.peek_remote_directory() + ","

            if session["debug"]:
                print("cmd requested without password", cmd)

            if self.peek_password() is None:
                ret_dict["show-status"]["firmwaredownload"]["message"] = "Password required"
                return ret_dict
            else:
                try:
                    cmd = cmd + base64.b64decode(self.peek_password()).decode("utf-8")
                # pylint: disable=W0702
                except:
                    return  {"client-error-code": 400, "client-error-message": "Bad Request", "client-errors" : {"errors": {"@xmlns": "urn:ietf:params:xml:ns:yang:ietf-restconf", "error": [{"error-type": "application", "error-tag": "operation-failed", "error-app-tag": "Error", "error-message": "Password cannot be decoded", "error-info": {"error-code": 589824, "error-module": "cal"}}]}}}

        # ssh_resp = "\n"

        session["fd_thread"] = threading.Thread(target=ssh_firmwaredownload, args=(session, session["username"], session["password"], session["ip_addr"], False, cmd, self.peek_eula_action()))

        session["fd_thread"].start()
        session["fd_thread_status"] = "queued"
        session["fd_thread_message"] = "queued"
        session["fd_completion"] = 0

        ret_dict["show-status"]["firmwaredownload"]["message"] = "Firmwaredownload initiated successfully"
#        if ssh_resp == "\n":
#            ret_dict["show-status"]["firmwaredownload"]["message"] = "Firmwaredownload initiated successfully"
#        else:
#            ret_dict["show-status"]["firmwaredownload"]["message"] = ssh_resp

        return ret_dict

    def process_ssh_show_status(self, session):
        if self.peek_message_id() == 0:
            if "fd_thread" not in session:
                ret_dict = {'show-status': {'message-id': self.peek_message_id(), 'status': 'error', 'application-name': 'RESTAPI', 'percentage-complete': '0', 'operation': 'firmwaredownload', 'firmwaredownload': {'message': 'unknown message-id'}}}
                return ret_dict

            if session["fd_thread"].is_alive():
                ret_dict = {'show-status': {'message-id': self.peek_message_id(), 'status': 'in-progress', 'application-name': 'RESTAPI', 'percentage-complete': session["fd_completion"], 'operation': 'firmwaredownload', 'firmwaredownload': {'message': 'in-progress'}}}
            else:
                if session["fd_thread_status"] == "done":
                    session["fd_thread_status"] = "delivered"
                    ret_dict = {'show-status': {'message-id': self.peek_message_id(), 'status': 'delivered', 'application-name': 'RESTAPI', 'percentage-complete': '100', 'operation': 'firmwaredownload', 'firmwaredownload': {'message': 'delivered'}}}
                elif session["fd_thread_status"] == "delivered":
                    ret_dict = {'show-status': {'message-id': self.peek_message_id(), 'status': 'delivered', 'application-name': 'RESTAPI', 'percentage-complete': '100', 'operation': 'firmwaredownload', 'firmwaredownload': {'message': 'delivered'}}}
                else:
                    ret_dict = {'show-status': {'message-id': self.peek_message_id(), 'status': session["fd_thread_status"], 'application-name': 'RESTAPI', 'percentage-complete': '0', 'operation': 'firmwaredownload', 'firmwaredownload': {'message': session["fd_thread_message"]}}}
        else:
            ret_dict = {'show-status': {'message-id': self.peek_message_id(), 'status': 'error', 'application-name': 'RESTAPI', 'percentage-complete': '0', 'operation': 'firmwaredownload', 'firmwaredownload': {'message': 'unknown message-id'}}}
        return ret_dict

    def process_ssh(self, session, uri):
        if uri == LICENSE_URI:
            return self.process_ssh_license(session)
        elif uri == FIRMWARECLEANINSTALL_URI:
            return self.process_ssh_firmwarecleaninstall(session)
        elif uri == FIRMWAREDOWNLOAD_URI:
            return self.process_ssh_firmwaredownload(session)
        elif uri == CONFIG_URI:
            return self.process_ssh_config(session)
        elif uri == SHOW_STATUS_URI:
            return self.process_ssh_show_status(session)
        else:
            ret_dict = {'show-status': {'message-id': '20000', 'status': 'queued', 'application-name': 'RESTAPI', 'percentage-complete': '0', 'operation': 'firmwaredownload', 'firmwaredownload': {'message': 'Firmwaredownload sanity check in-progress.'}}}
            return ret_dict

#        ret_dict = {'show-status': {'message-id': '20000', 'status': 'queued', 'application-name': 'RESTAPI', 'percentage-complete': '0', 'operation': 'firmwaredownload', 'firmwaredownload': {'message': 'Firmwaredownload sanity check in-progress.'}}}

    def post(self, session, negative=0, is_tc=0):
        ret = self.obj.is_valid(session)
        if ret["info-code"] != 0:
            return ret
        if is_tc:
            self.createtest("post", negative)
        if self.rpc == 1:
            if self.is_ssh(session, self.uri_base, session["version"]):
                ret = self.process_ssh(session, self.uri_base)
            else:
                ret = pyfos_util.rpc_request(session, self.uri_base, self.obj.create_html_content(0, session))
        else:
            ret = pyfos_util.post_request(session, self.uri_base, self.obj.create_html_content(0, session))
        self.dbg_print(DBG, "Create:\n", self.uri_base, self.obj.create_html_content(0, session), ret)
        return ret

    def delete(self, session, negative=0, is_tc=0):
        ret = self.obj.is_valid(session)
        if ret["info-code"] != 0:
            return ret
        if is_tc:
            self.createtest("delete", negative)
        ret = pyfos_util.delete_request(session, self.uri_base, self.obj.create_html_content(rest_get_method.GET_KEY_AND_MODIFIED_CONFIG_DELETE, session))
        self.dbg_print(DBG, "Delete:\n", self.uri_base, self.obj.create_html_content(rest_get_method.GET_KEY_AND_MODIFIED_CONFIG_DELETE, session), ret)
        return ret

    def delete_uri(self, session, negative=0, is_tc=0):
        ret = self.obj.is_valid(session)
        if ret["info-code"] != 0:
            return ret
        if is_tc:
            self.createtest("delete_uri", negative)
        ret = pyfos_util.delete_request(session, self.uri_base + self.obj.uri_string(rest_get_method.GET_KEY_AND_MODIFIED_CONFIG_DELETE, session), "")
        self.dbg_print(DBG, "Delete:\n", self.uri_base + self.obj.uri_string(rest_get_method.GET_KEY_AND_MODIFIED_CONFIG_DELETE, session), ret)
        return ret

    def patch(self, session, negative=0, is_tc=0, modified_dict={}):
        ret = self.obj.is_valid(session)
        if ret["info-code"] != 0:
            return ret
        self.load(modified_dict, 1)
        if is_tc:
            self.createtest("patch", negative)
        ret = pyfos_util.patch_request(session, self.uri_base, self.obj.create_html_content(rest_get_method.GET_KEY_AND_MODIFIED_CONFIG, session))
        self.dbg_print(DBG, "Delete:\n", self.uri_base, self.obj.create_html_content(rest_get_method.GET_KEY_AND_MODIFIED_CONFIG, session), ret)
        return ret

    # pylint: disable=W0613
    @staticmethod
    def patch_all(session, negative=0, is_tc=0, modified_dict={},
                  objsList=[]):
        "The patch_all handler handles more than one object to perform a patch operation; for example, a list of ports."
        buf = ""
        if "Authorization" in session['credential'].keys() == 0:
            return {"info-code": -1, "info-message": "Invalid session", "info-type": "Incorrect auth details in session"}

        for obj in objsList:
            # '''
            # print("Type\n", type(obj), type(obj.obj))
            # ret = obj.obj.is_valid(session)
            #
            # if ( ret["info-code"] != 0 ):
            #   return ret
            # obj.load(modified_dict, 1)
            # if is_tc:
            #   obj.createtest("patch", negative)
            # '''
            uri_base = obj.uri_base

            buf += obj.obj.create_html_content(rest_get_method.GET_KEY_AND_MODIFIED_CONFIG, session)

        ret = pyfos_util.patch_request(session, uri_base, buf)
        # self.dbg_print(DBG, "Delete:\n", uri_base, buf, ret)
        return ret

    @staticmethod
    def post_all(session, negative=0, is_tc=0, modified_dict={},
                 objsList=[]):
        "The post_all handler handles more than one object to perform post operation; for example, a list of ports."

        buf = ""

        if "Authorization" in session['credential'].keys() == 0:
            return {"info-code": -1, "info-message": "Invalid session", "info-type": "Incorrect auth details in session"}

        for obj in objsList:
            # '''
            # ret = obj.obj.is_valid(session)
            # if ( ret["info-code"] != 0 ):
            #     return ret
            # obj.load(modified_dict, 1)
            #
            # if is_tc:
            #    obj.createtest("patch", negative)
            # '''

            uri_base = obj.uri_base
            buf += obj.obj.create_html_content(0, session)

        ret = pyfos_util.post_request(session, uri_base, buf)
        # self.dbg_print(DBG, "Delete:\n", uri_base, buf, ret)
        return ret

    def patch_uri(self, session, negative=0, is_tc=0, modified_dict={}):
        ret = self.obj.is_valid(session)
        if ret["info-code"] != 0:
            return ret
        self.load(modified_dict, 1)
        if is_tc:
            self.createtest("patch_uri", negative)
        ret = pyfos_util.patch_request(session, self.uri_base + self.obj.uri_string(rest_get_method.GET_ALL_KEY, session), self.obj.create_html_content(rest_get_method.GET_MODIFIED_CONFIG, session))
        return self.validate(negative, ret)


class rest_object_encoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, 'reprJSON'):
            return obj.reprJSON()
        else:
            return json.JSONEncoder.default(self, obj)


class rest_object(rest_handler):
    """ This class encompasses a REST-supported FOS object as per YANG.

    .. Attributes:
        obj_type: The `obj_type` corresponding to a FOS object.
        uri_base:  The `uri_base` is the base URI string to access the corresponding object.
        obj:  The `obj` is the corresponding REST object instance for rest_handler to work on.
        test: The `test` dictionary captures all the different test executions.


    .. classmethod:: get(session, args=None, filters=None)

      Returns a :class: of type `cls` object or a list of
      objects filled with attributes gathered
      from the switch. If optional arguments are given a unique object
      instance is returned.

      Each object can be printed using :func:`pyfos_util.response_print`
      and individual attributes accessed through peek methods.

      :param session: Session handler returned by
          :func:`pyfos_auth.login`.
      :param args: Argument for uniquely identifying the object.
      :param filters: List of filter attributes.
      :rtype: An object or list of objects of type class *cls*.

    :Example:

     *The following are some examples on how to use the class method.*

      Get using a key in a dictionary::

       # Importing the module

       from pyfos.pyfos_brocade_gigabitethernet import extension_gigabitethernet

       # Using key as a dictionary
       myobj = extension_gigabitethernet.get(session, {'name': '4/16'})

       # Display the object
       # print(myobj.display())
       pyfos_util.response_print(myobj)

      Get using a key as a value::

       # Importing the module

       from pyfos.pyfos_brocade_gigabitethernet import extension_gigabitethernet

       # Using key as a dictionary
       myobj = extension_gigabitethernet.get(session, '4/15')

       # Display the object
       # print(myobj.display())
       pyfos_util.response_print(myobj)

      Get all::

       # Importing the module

       from pyfos.pyfos_brocade_gigabitethernet import extension_gigabitethernet

       # Using key as a dictionary
       objlist = extension_gigabitethernet.get(session)

       # Display the object
       # For i in range(len(objlist)):
       #    print(objlist[i].display())
       pyfos_util.response_print(objlist)

    """
    def __init__(self, obj_type, uri, visible_version=VER_RANGE_820_ABOVE, rpc=0, container=None):
        """ This is the constructor of the class."""
        self.obj_type = obj_type
        self.attributes_dict = dict()
        self.attributes = []
        self.clone_instance = dict()
        self.configchanged = 0
        self.initialized = 0
        rest_handler.__init__(self, uri)
        self.version_supported = fosversion_range(visible_version)
        self.version_active = fosversion(self.version_supported.start.to_string())
        self.keyslist = []
        self.use_custom_cli = 1
        self.use_custom_dict = None
        self.rpc = rpc
        self.columnmap = dict()
        self.loadcolumnmap = dict()
        self.adjustcolumn = None
        self.setcontainer = container
        self.container = container
        self.setmyuri(self.version_active)

    def setmyuri(self, version=None):
        if version is None:
            version = self.version_active
        tmpuri = None
        uri = self.urilist
        if isinstance(uri, list):
            for i in range(len(uri)):
                vver = fosversion_range(uri[i]['URIVER'])
                vuri = uri[i]['URI']
                if version is not None and vver.visible(version):
                    tmpuri = str(vuri)
                elif version is None:
                    tmpuri = str(vuri)
            if tmpuri is None:
                self.dbg_print(ERR, "Unable to Detect the URI from version " +
                               str(uri),
                               version)
        else:
            tmpuri = str(self.urilist)
        if self.setcontainer is None:
            uriarray = tmpuri.split("/")
            self.uri_base = tmpuri
            i = len(uriarray)
            if self.setcontainer is None:
                self.container = uriarray[i-1]
        else:
            self.uri_base = tmpuri
            self.container = self.setcontainer

    def load(self, dictvalues, changed=0, ver=None):
        """The function loads or deserialzes from a dictionary of values into the object itself."""
        if ver is None:
            ver = fosversion(self.version_active.to_string())
        self.initialized = 1
        if dictvalues is not None and len(dictvalues):
            if self.container in dictvalues.keys():
                retdict = dictvalues[self.container]
            else:
                retdict = dictvalues
            for k1, v1 in retdict.items():
                if k1 in self.attributes_dict.keys():
                    attribute = self.attributes_dict[k1]
                    attribute.setvalue(v1, changed)
                    if ver < attribute.version_active:
                        ver.from_string(attribute.version_active.to_string())
                else:
                    self.dbg_print(ERR, "Unknown Attribute \"" + k1 +
                                   "\" found in Object load",
                                   getrestobjectname(self.obj_type))
        if ver != self.version_active:
            self.version_active.from_string(ver.to_string())

    def clean(self, filters=None):
        """The function cleans an object."""
        # pylint: disable=W0612
        for k1, v1 in self.attributes_dict.items():
            v1.clean(filters)

    def getInstances(self, session, filters=None):
        get_by_key = 0
        obj = self.__class__()
        if filters is not None and len(self.keyslist) == 0:
            get_by_key = 1
        for i in range(len(self.keyslist)):
            if self.keyslist[i].value is not None:
                get_by_key = 1
                break
        if get_by_key == 1:
            if filters is not None:
                self.addfilter(filters)

            obj_list = super(rest_object, self).get(session)

            if filters is not None:
                self.removefilter(filters)

        else:
            obj_list = obj.show_all(session)

        self.dbg_print(DBG, obj_list)
        if pyfos_util.is_failed_resp(obj_list):
            self.dbg_print(ERR, obj_list)
            return obj_list
        # Additional check for reponse data
        elif not isinstance(obj_list, dict) or obj.getcontainer() not in obj_list.keys():
            self.dbg_print(ERR, "Incorrect response format/data received",
                           obj_list)
            return obj_list
        elif obj_list[obj.getcontainer()] is None:
            return self
        elif isinstance(obj_list[obj.getcontainer()], dict):
            if obj_list[obj.getcontainer()] is not None:
                # self.dbg_print(DBG, pyfos_util.response_print(obj_list[obj.getcontainer()]))
                self.load(obj_list[obj.getcontainer()])
                if filters is not None and get_by_key == 0:
                    self.clean(filters)
            return self
        else:
            retobj_list = []
            for one_instance in obj_list[obj.getcontainer()]:
                retobj = self.__class__()
                retobj.setdbg_session(session)
                retobj.load(one_instance)
                # TODO : Try to see if bulk get can be used instead.
                # Remove the clean operation as its shrink functionality
                if filters is not None:
                    retobj.clean(filters)
                retobj_list.append(retobj)
            return retobj_list

    @classmethod
    def get(cls, session, args=None, filters=None):
        obj = cls()
        if args is not None:
            if isinstance(args, dict):
                obj.load(args)
            elif isinstance(args, list):
                if len(obj.keyslist) == len(args):
                    for i in range(len(obj.keyslist)):
                        obj.keyslist[i].setvalue(args[i])
                else:
                    obj.dbg_print(ERR, "Incorrect key details passed[",
                                  cls, "] needs ", len(obj.keylist),
                                  "keys, but given ", len(args))
            else:
                if len(obj.keyslist) == 1:
                    obj.keyslist[0].setvalue(args)

        return obj.getInstances(session, filters)

    def display(self, ver=None):
        """The function serializes the object to a dictionary."""
        if ver is None:
            ver = self.version_active

        mydict = dict()
        for i in range(len(self.attributes)):
            mydict.update(self.attributes[i].display(ver))
        retdict = {self.container: mydict}
        return retdict

    def objdisplay(self, ver=None):
        """The function serializes the object to a dictionary with object pointer details."""
        mydict = dict()

        for i in range(len(self.attributes)):
            mydict.update(self.attributes[i].objdisplay(ver))
        return mydict

    def getIndexedClonename(self, attribute):
        if attribute.parent is None:
            return attribute.Iclonename()
        else:
            return attribute.parent.Iclonename() + attribute.Iclonename()

    def setIndexedClonename(self, attribute):
        # Indexedclone
        myfunc = self.getIndexedClonename(attribute)
        setattr(self, "set_" + myfunc.lower(), attribute.setuservalue)
        setattr(self, "peek_" + myfunc.lower(), attribute.getuservalue)

    def add(self, attribute, parents=[]):
        """The function adds the attribute to the REST object."""
        if attribute.version_active is None:
            attribute.setversion(self.version_supported.to_string())
        else:
            if self.version_supported.visible(attribute.version_active) == 0:
                self.dbg_print(ERR, "Version of attribute not supported by parent:",
                               attribute.name)
                self.dbg_print(ERR, "Parent version::", self.version_supported.to_string())
                self.dbg_print(ERR, "Attribute version::", attribute.version_active.to_string())
                return 0

        attribute.restobject = self
        # This is only required that direct level attributes are added to the attributes_dict
        if len(parents) == 0:
            self.attributes_dict.update(attribute.todict())
            self.attributes.append(attribute)
        else:
            parent = self.getparent(parents, attribute.version_active)
            if parent is not None:
                parent.addchild(attribute)
            else:
                self.dbg_print(ERR, "No parent found matching hierarchy??", parents)
                self.dbg_print(INF, "Attribute:", attribute.getname(), "\n",
                               " version::", attribute.version_active.to_string())
                return 0

        # Set the clonename of the attribute
        attribute.setclonename()
        attribute.setusage()
        myfunc = attribute.getclonename()
        if attribute.is_leaf and (attribute.getiskey() or attribute.getisconfig()):
            tmplen = len(self.columnmap) + 1
            if myfunc in self.columnmap.keys():
                self.dbg_print(ERR, "Attribute with same name added twice",
                               attribute.name, self.__class__)
            else:
                self.columnmap.update(dict({myfunc: tmplen}))
        # Install the generic Setters and getters of the function
        setattr(self, "set_" + myfunc.lower(), attribute.setuservalue)
        setattr(self, "peek_" + myfunc.lower(), attribute.getuservalue)
        self.setIndexedClonename(attribute)
        self.addclone(attribute.uname, attribute)
        if attribute.is_key:
            self.keyslist.append(attribute)
        return 0

    def addclone(self, name, attribute):
        """Adds the clone instance Update."""
        self.clone_instance.update({name: attribute})
        self.dbg_print(INF, "clone instance ", name, self.clone_instance)

    # pylint: disable=W1401
    def default_set(self, value, changed=1):
        parentcaller = str(inspect.stack()[1][4])
        myfunc = re.sub('set_', '', re.sub('^.*\w\.', '', re.sub('\\(.*', '', parentcaller)), 1)
        if myfunc in self.name_dict.keys():
            attribute = self.name_dict[myfunc]
            if attribute.supportedop(rest_get_method.GET_ALL_KEY_CONFIG):
                self.name_dict[myfunc].setvalue(value, changed)
            else:
                print("Unsupported: ", "set_" + myfunc, " function is not allowed for the attribute \"", attribute.getname(), "\".\n")
            return None
        else:
            print("CALL: ", parentcaller, "FUNC: ", myfunc, self.name_dict.keys())
            return {"info-code": -1, "info-message": "Incorrect call", "info-type": "Unable to locate the attrib in the calls"}

    def default_get(self):
        parentcaller = str(inspect.stack()[1][4])
        myfunc = re.sub('get_', '', re.sub('^.*\w\.', '', re.sub('\\(.*', '', parentcaller)))
        if myfunc in self.name_dict.keys():
            return self.name_dict[myfunc].getvalue()
        else:
            print("CALL: ", parentcaller, "FUNC: ", myfunc, self.name_dict.keys())
            return {"info-code": -1, "info-message": "Incorrect call", "info-type": "Unable to locate the attrib in the calls"}

    def reprJSON(self, ver=None):
        """Represents the REST object in JSON format."""
        if ver is None:
            ver = self.version_active
        retdict = dict()
        retdict[self.container] = dict()
        for k1, v1 in self.attributes_dict.items():
            if v1.is_empty() is False:
                if v1.version_supported.visible(ver):
                    retdict[self.container][k1] = v1
        return retdict

    def getcontainer(self):
        """Gets the REST container object name."""
        return self.container

    def gethierarchy(self, clonename):
        """Gets the clone hierarchy given a clone name."""
        if clonename in self.clone_instance.keys():
            attribute = self.clone_instance[clonename]
            if attribute.getisattributelist() or attribute.getisattributemap():
                return attribute.hierarchy

        return None

    def addfilter(self, filters):
        """Adds the filter for an attribute. """
        for i in range(len(filters)):
            if filters[i] in self.clone_instance.keys():
                attribute = self.clone_instance[filters[i]]
                attribute.setfilter()
            else:
                self.dbg_print(ERR, "Unknown filter name ", filters[i])

    def removefilter(self, filters):
        """Removes the filter for an attribute."""
        for i in range(len(filters)):
            if filters[i] in self.clone_instance.keys():
                attribute = self.clone_instance[filters[i]]
                attribute.resetfilter()

    def overwriteparser(self, clonename):
        if self.use_custom_cli and self.use_custom_dict is not None:
            if clonename in self.use_custom_dict.keys():
                return self.use_custom_dict[clonename]
        return None

    def ignoreclifilters(self, filters, key):
        usagefilterdict = dict()
        testcondition = list()
        usagefilterdict.update(dict({"ignoreMandatory" : list(["ipaddr", "login", "password"])}))
        usagefilterdict.update(dict({"ignoreMandatoryNonIP": list(["login", "password"])}))
        selectivecheck = [item for item in filters if item in usagefilterdict.keys()]
        if len(selectivecheck):
            testcondition = [item for item in selectivecheck if key in usagefilterdict[item]]
        return bool(len(testcondition))

    def showusage(self, filters=None):
        cmd_mandatory = ""
        if not self.ignoreclifilters(filters, "ipaddr"):
            cmd_mandatory = " <-i IPADDR>"
        if not self.ignoreclifilters(filters, "login"):
            cmd_mandatory += " <-L LOGIN>"
        if not self.ignoreclifilters(filters, "login"):
            cmd_mandatory += " <-P PASSWORD>"
        cmd_optional = " [-f VFID] [-s MODE] [-v] [-a AuthToken] [-z]"
        objusagestr = ""
        objkeystr = ""
        objmandatory = ""
        objoptional = ""
        # pylint: disable=W0612
        for k1, v1 in self.clone_instance.items():
            cmd_mandatory += v1.getmyopts(rest_useropt.FILTER_CMDLINE_MANDATORY, filters)
            cmd_optional += v1.getmyopts(rest_useropt.FILTER_CMDLINE_OPTIONAL, filters)
            if v1.is_key:
                objkeystr += v1.getusage(filters)
            elif v1.is_mandatory:
                objmandatory += v1.getusage(filters)
            else:
                objoptional += v1.getusage(filters)

        objusagestr = objkeystr + objmandatory + objoptional
        usagestr = "\n" + os.path.basename(sys.argv[0]) + cmd_mandatory + cmd_optional + "\n"
        usagestr += 'Usage:\n'
        usagestr += "\n  Infrastructure options:\n\n"
        if not self.ignoreclifilters(filters, "ipaddr"):
            usagestr += '{0:5}{1:3}--{2:40}{3:35}\n'.format("", "-i,",
                        "ipaddr=IPADDR", "IP address of FOS switch.")
        if not self.ignoreclifilters(filters, "login"):
            usagestr += '{0:5}{1:3}--{2:40}{3:35}\n'.format("", "-L,",
                        "login=LOGIN", "login name.")
        if not self.ignoreclifilters(filters, "password"):
            usagestr += '{0:5}{1:3}--{2:40}{3:35}\n'.format("", "-P,",
                        "password=PASSWORD", "password.")
        usagestr += '{0:5}{1:3}--{2:40}{3:35}\n'.format("", "-f,", "vfid=VFID",
                    "VFID of LS context to which the request is directed" +
                    " to [OPTIONAL].")
        usagestr += '{0:5}{1:3}--{2:40}{3:35}\n'.format("", "-s,",
                    "secured=MODE",
                    "HTTPS mode \"self\" or \"CA\" [OPTIONAL].")
        usagestr += '{0:5}{1:3}--{2:40}{3:35}\n'.format("", "-v,", "verbose",
                    "verbose mode[OPTIONAL].")
        usagestr += '{0:5}{1:3}--{2:40}{3:35}\n'.format("", "-a,", "authtoken",
                    "AuthToken value or AuthTokenManager config file[OPTIONAL].")
        usagestr += '{0:5}{1:3}--{2:40}{3:35}\n'.format("", "-z,", "nosession",
                    "Sessionless authentication based login[OPTIONAL].")
        usagestr += '{0:5}{1:3}--{2:40}{3:35}\n'.format("", "", "nocredential",
                    "No credential to be sent in the request.[OPTIONAL].")
        usagestr += "\n  Utils script specific options:\n\n"
        usagestr += objusagestr

        return usagestr

    @classmethod
    def cliusage(cls, filters=None):
        myobj = cls()
        return myobj.showusage(filters)

    def getmyopts(self, useropt, filters=None):
        if useropt == rest_useropt.FILTER_LGETOPT:
            myopts = []
            # pylint: disable=W0612
            for k1, v1 in self.clone_instance.items():
                myopts += v1.getmyopts(useropt, filters)
            return myopts
        else:
            myopts = ""
            for k1, v1 in self.clone_instance.items():
                myopts += v1.getmyopts(useropt, filters)
            return myopts
        return ""

    def parse_attrib(self, opt, arg, filters=None):
        # pylint: disable=W0612
        for k1, v1 in self.clone_instance.items():
            self.dbg_print(DBG, opt, arg,
                           v1.getmyopts(rest_useropt.FILTER_ALLOPT, filters))
            if opt in v1.getmyopts(rest_useropt.FILTER_ALLOPT, filters):
                vshrtopt = v1.getmyopts(rest_useropt.FILTER_SHRTOPT, filters)
                vlongopt = v1.getmyopts(rest_useropt.FILTER_LONGOPT, filters)
                if not opt in vshrtopt:
                    if opt in vlongopt and opt != vlongopt:
                        continue
                if v1.is_leaf and v1.is_list:
                    return v1.parseInfraset(arg.split(';'))
                elif v1.is_leaf:
                    return v1.parseInfraset(arg)
                else:
                    modifiedarg = re.sub(";", " ", arg)
                    mydict = ast.literal_eval(modifiedarg)
                    another = json.loads(mydict)
                    if len(mydict) > 0:
                        return v1.parseInfraset(another)
                    else:
                        return 1
                return 0
        return 1

    def setmycustomcli(self, mydict):
        if mydict is not None:
            self.use_custom_dict = mydict
            self.use_custom_cli = 1
            # pylint: disable=W0612
            for k1, v1 in self.clone_instance.items():
                v1.setusage()
        else:
            self.use_custom_dict = None
            self.use_custom_cli = 0

    def resetmycustomcli(self):
        self.use_custom_dict = None
        self.use_custom_cli = 0
        # pylint: disable=W0612
        for k1, v1 in self.clone_instance.items():
            v1.setusage()

    def displaycustomcli(self):
        retdict = dict()
        # pylint: disable=W0612
        for k1, v1 in self.clone_instance.items():
            attribdict = v1.displaycustomcli()
            if attribdict is not None:
                retdict.update(attribdict)
        return {self.container: retdict}

    @classmethod
    def parse(cls, argv, inputs, filters, custom_cli, validate=None):
        myobj = cls()
        return myobj.parse_commandline(argv, inputs, filters,
                                       custom_cli, validate)

    def parse_commandline(self, argv, inputs, filters, custom_cli, validate=None):
        myobj = self
        if custom_cli is not None:
            myobj.setmycustomcli(custom_cli)
        myopts = ["help", "ipaddr=", "vfid=", "login=", "password=",
                  "secured=", "verbose", "authtoken=", "nosession", "nocredential"] +\
                 myobj.getmyopts(rest_useropt.FILTER_LGETOPT, filters)
        myobj.dbg_print(DBG, "Short:",
                        myobj.getmyopts(rest_useropt.FILTER_SGETOPT, filters))
        myobj.dbg_print(DBG, "LONG:",
                        myobj.getmyopts(rest_useropt.FILTER_LGETOPT, filters))
        # pylint: disable=W0612
        try:
            opts, args = getopt.getopt(argv, "hi:f:L:P:s:avz" +
                                       myobj.getmyopts(
                                           rest_useropt.FILTER_SGETOPT,
                                           filters), myopts)
        except getopt.GetoptError as err:
            print("getopt error", str(err))
            print(myobj.showusage(filters))
            return None

        myobj.dbg_print(DBG, opts)
        for opt, arg in opts:
            myobj.dbg_print(DBG, "OPTIONS->", opt, " : ", arg)
            if opt in ("-h", "--help"):
                print(myobj.showusage(filters))
                return None
            if opt in ("-i", "--ipaddr"):
                inputs.update({'ipaddr': arg})
            elif opt in ("-f", "--vfid"):
                if not pyfos_util.isInt(arg):
                    print("*** Invalid vfid:", arg)
                    print(myobj.showusage(filters))
                    return None
                inputs.update({'vfid': int(arg)})
            elif opt in ("-L", "--login"):
                if arg is not None and arg[0] == "-":
                    print("Incorrect Login specified.")
                    print(myobj.showusage(filters))
                    return None
                inputs.update({'login': arg})
            elif opt in ("-P", "--password"):
                if arg is not None and arg[0] == "-":
                    print("Incorrect password specified.")
                    print(myobj.showusage(filters))
                    return None
                inputs.update({'password': arg})
            elif opt in ("-s", "--secured"):
                if arg not in ('self', 'CA'):
                    print("defaults to CA")
                    arg = "CA"
                inputs.update({'secured': arg})
            elif opt in ("-v", "--verbose"):
                inputs.update({'verbose': 1})
            elif opt in ("-a", "--authtoken"):
                if len(arg) == 0:
                    inputs.update({'authtoken': None})
                else:
                    inputs.update({'authtoken': arg})
            elif opt in ("-z", "--nosession"):
                inputs.update({'sessionless': True})
            elif opt == "--nocredential":
                inputs.update({'nocredential': True})
                filters.append("ignoreMandatoryNonIP")
            elif myobj.parse_attrib(opt, arg, filters):
                print("Invalid options specified ", opt)
                print(myobj.showusage(filters))
                return None

        if "ipaddr" not in inputs.keys() and not\
           self.ignoreclifilters(filters, "ipaddr"):
            print("Missing IP address input")
            print(myobj.showusage(filters))
            return None
            # ipaddr = input("Please provide switch IP address:")
            # inputs.update({'ipaddr': ipaddr})
        elif not self.ignoreclifilters(filters, "ipaddr"):
            ipaddr = inputs['ipaddr']
            if not pyfos_util.isIPAddr(ipaddr) and\
               not self.ignoreclifilters(filters, "ipaddr"):
                print("*** Invalid ipaddr:", ipaddr)
                print(myobj.showusage(filters))
                return None
        if validate is not None and validate(myobj) != 0:
            print("Please provide the missing util script option.")
            print(myobj.showusage(filters))
            return None

        if "login" not in inputs.keys() and\
           not self.ignoreclifilters(filters, "login"):
            login = input("Login:")
            inputs.update({'login': login})

        if "password" not in inputs.keys() and "authtoken" not in inputs.keys()\
           and not self.ignoreclifilters(filters, "password"):
            password = getpass.getpass()
            inputs.update({'password': password})
        elif "password" in inputs.keys() and "authtoken" in inputs.keys()\
             and not self.ignoreclifilters(filters, "password"):
            print("No Password needed in case of authToken based authentication.")
            print(myobj.showusage(filters))
            return None
        if 'nocredential' in inputs.keys():
            if "password" in inputs.keys():
                print("No password required with \"--nocredential\" option.")
                return None
            if "login" in inputs.keys():
                print("No login user required with \"--nocredential\" option.")
                return None
            if "authtoken" in inputs.keys():
                print("No authtoken input required with \"--nocredential\" option.")
                return None
        if 'sessionless' in inputs.keys() and inputs['sessionless'] is True:
            if "authtoken" in inputs.keys():
                print("No authtoken input required with \"--nosession\" option.")
                return None
            if "nocredential" in inputs.keys():
                print("The \"--nocredential\" input and \"--nosession\" " +
                      "options not supported together.")
                return None
        if "secured" not in inputs.keys():
            inputs.update({'secured': None})

        return myobj

    def showfilter(self):
        filters = []
        # pylint: disable=W0612
        for k1, v1 in self.clone_instance.items():
            v1.getfilter(filters)
        return filters

    def isfilterset(self):
        filters = self.showfilter()
        if (len(filters)) > 0:
            return 1
        return 0

    def getattribute(self, name):
        attrib = self.attributes_dict[name]
        return attrib

    # pylint: disable=W0613
    def getparent(self, parents, ver, list_count=0):
        parentobj = None
        for i in range(len(parents)):
            if i == 0:
                if parents[i] in self.attributes_dict.keys():
                    parentobj = self.attributes_dict[parents[i]]
                    if parentobj.version_supported.visible(ver) == 0:
                        self.dbg_print(ERR, parentobj.getname(),
                                       ":Parent version not supported Version::",
                                       parentobj.version_supported.to_string(),
                                       ver.to_string())
                        return None
                else:
                    self.dbg_print(ERR, "Unknown Parent hierarchy", parents)
            elif parentobj is not None:
                child = parentobj.getchildattrib(parents[i])
                if child.version_supported.visible(ver):
                    parentobj = child
                else:
                    self.dbg_print(ERR, parentobj.getname(), ":Parent version not supported version:",
                                   parentobj.version_supported.to_string(), ver.to_string())
                    return None
            else:
                self.dbg_print(ERR, "No parent found in the hierarchy", parents)
        return parentobj

    def remove(self, attribute):
        attrib = self.attributes_dict[attribute.getname()]
        self.attributes.remove(attrib)
        del self.attributes_dict[attribute.getname()]

    def update(self, attribute):
        myattrib = self.attributes_dict[attribute.getname()]
        myattrib.setvalue(attribute.getvalue)

    def is_empty(self):
        count = len(self.attributes_dict)
        if count > 0:
            return 0
        return 1

    def namekeys(self):
        return self.attributes_dict.keys()

    def is_key_attrib(self, name):
        attrib = self.attributes_dict[name]
        return attrib.getiskey()

    def is_config_attrib(self, name):
        return self.attributes_dict[name].getisconfig()

    def is_value_changed(self, name):
        return self.attributes_dict[name].getisvaluechanged()

    def set_value_changed(self, name, changed=0):
        return self.attributes_dict[name].setvaluechanged(changed)

    def getvalue(self, name):
        return self.attributes_dict[name].getvalue()

    def compare(self, retdict, reset_changed=0):
        if len(retdict):
            if self.container in retdict.keys():
                retdict = retdict[self.container]

        for k1, v1 in self.attributes_dict.items():
            if k1 in retdict:
                if v1.compare(retdict[k1], reset_changed) == 0:
                    return 0
            else:
                return 0

        return 1

    def __repr__(self):
        return json.dumps(self, cls=rest_attribute_encoder, sort_keys=True, indent=4)

    def modified(self):
        for k1, v1 in self.attributes_dict.items():
            if v1.modified() == 1:
                self.dbg_print(DBG, "modified(", k1, ":", v1, ")")
                return 1
        return 0

    def is_valid(self, session):
        self.setdbg_session(session)
        nocred = session.get("nocredential", False)
        if not nocred and self.isvalidsession(session) == 0:
            return {"info-code": -1,
                    "info-message": "Invalid session",
                    "info-type": "Incorrect auth details in session"}
        if session['version'] is not None:
            if not self.version_supported.visible(session['version']):
                self.dbg_print(ERR, "Version not supported")
                self.dbg_print(ERR, "Session [",
                               session['version'].to_string(),
                               "] Supported version[",
                               self.version_supported.to_string(), "]")
                ret_error = {"info-code": -1,
                             "info-message": "Switch version is lower than the object",
                             "info-type": "Informational"}
                return ret_error
        self.obj.setmyuri(session['version'])
        ret_error = {"info-code": 0,
                     "info-message": "attributes details are present",
                     "info-type": "Informational"}
        return ret_error

    def create_html_content(self, optype=0, session=None, add_container=1):
        version = None
        if session is not None:
            version = session.get('version', None)
            if version is not None:
                self.setdbg_session(session)
        if version is None:
            version = self.version_active
        string_post = ""
        for name in self.namekeys():
            attrib = self.attributes_dict[name]
            if attrib.is_key:
                if self.attributes_dict[name].supportedop(optype, version):
                    string_post += self.attributes_dict[name].create_html_content(optype, version)
        for name in self.namekeys():
            attrib = self.attributes_dict[name]
            # print(attrib.name, attrib.value)
            if not attrib.is_key:
                if self.attributes_dict[name].supportedop(optype, version):
                    string_post += self.attributes_dict[name].create_html_content(optype, version)
        if add_container:
            string_post = re.sub("\n", "\n\t", string_post)
            string_post = "\n<" + self.container + ">" + string_post + "\n</" + self.container + ">"
        self.dbg_print(INF, "HTML CONTENT DATA:\n", string_post)
        return string_post

    def uri_string(self, optype=0, session=None):
        version = None
        if session is not None:
            version = session['version']
            self.setdbg_session(session)
        if version is None:
            version = self.version_active
        string_uri = ""
        for name in self.namekeys():
            if self.attributes_dict[name].supportedop(optype, version):
                string_uri += self.attributes_dict[name].uri_string(optype, version)
        self.dbg_print(INF, string_uri)
        return string_uri

    def dbg_print(self, level, *args):
        self.setdbg_log(level, args)

    def configops(self, op):
        if op == 'POST' and self.configchanged & 4:
            return True
        if op == 'PATCH' and self.configchanged & 2:
            return True
        if op == 'PUT' and self.configchanged & 2:
            return True
        if op == 'DELETE' and self.configchanged & 8:
            return True
        return True

    def diff(self, other, filters=None):
        if isinstance(other, self.__class__):
            for name in self.namekeys():
                attrib1 = self.attributes_dict[name]
                attrib2 = other.attributes_dict[name]
                attrib1.diff(attrib2, filters, 0)

    def getmyrow(self, listcount=-1):
        sr = 0
        er = 0
        rowcount = 1
        for name in self.namekeys():
            attrib = self.attributes_dict[name]
            count = attrib.getmyrow(listcount)
            if rowcount < count:
                rowcount = count
            self.dbg_print(DBG, attrib.name, rowcount)
            if er < rowcount:
                er = sr + rowcount - 1
        return sr+1, er+1, rowcount

    def getmywritecolumn(self, uname):
        if uname in self.columnmap.keys():
            return self.columnmap[uname] - self.adjustcolumn + 1
        self.dbg_print(DBG, uname)
        return 0

    def getmyreadcolumn(self, uname):
        if uname in self.loadcolumnmap.keys():
            return self.loadcolumnmap[uname]
        self.dbg_print(DBG, uname)
        return 0

    def dumpheaders(self, ws, baserow, filters=None):
        self.getmincolumnwrite(filters)
        r = baserow
        self.dbg_print(DBG, self.columnmap)
        for k, v in self.columnmap.items():
            self.dbg_print(DBG, k, v)
            if filters is None or \
               (filters is not None and k in filters):
                col = self.getmywritecolumn(k)
                cell = ws.cell(row=r, column=col)
                cell.value = k

    def getmincolumnwrite(self, filters):
        minvalue = None
        for k, v in self.columnmap.items():
            if filters is None or \
               (filters is not None and k in filters):
                if minvalue is None:
                    minvalue = v
                elif v < minvalue:
                    minvalue = v
        self.adjustcolumn = minvalue

    def dumpdata(self, ws, baserow, filters=None):
        self.getmincolumnwrite(filters)
        sr, er, rowcount = self.getmyrow(-1)
        sr += baserow
        er += baserow
        for name in self.namekeys():
            attrib = self.attributes_dict[name]
            attrib.writemycolumn(ws, sr, er, filters)
        return rowcount

    def loadheaders(self, ws, baserow, filters):
        self.loadcolumnmap = dict()
        self.getmincolumnwrite(filters)
        r = baserow
        col = 1
        cell = ws.cell(row=r, column=col)
        uname = cell.value
        while uname is not None or col < 100:
            if uname is not None:
                self.loadcolumnmap.update(dict({uname: col}))
            col += 1
            cell = ws.cell(row=r, column=col)
            uname = cell.value
        self.dbg_print(INF, self.loadcolumnmap)
        for k, v in self.columnmap.items():
            if filters is not None and k not in filters:
                continue
            if k not in self.loadcolumnmap.keys():
                print("Key is missing", k, v, self.__class__)
            # flake8: noqa
            # noqa : ignore=E127
            elif v != self.loadcolumnmap[k] and \
                 (v - self.adjustcolumn + 1) != self.loadcolumnmap[k]:
                print("Columns not matching in dump and load", self.__class__,
                      "Key", k, "Dump:", self.loadcolumnmap[k],
                      "Load:", v, "->", v - self.adjustcolumn + 1)
        # print(self.loadcolumnmap)

    def getcolumnwidth(self, ws, col, baserow, count=0):
        psr = baserow + 1
        nsr = baserow + 1
        rcount = count + 1
        tcount = 0
        while not self.emptyrow(ws, nsr) and tcount < rcount:
            cell = ws.cell(row=nsr, column=col)
            val = cell.value
            if val is not None:
                psr = nsr
                tcount += 1
            nsr += 1
        while not self.emptyrow(ws, nsr):
            cell = ws.cell(row=nsr, column=col)
            val = cell.value
            if val is not None:
                break
            nsr += 1
        diff = rcount - tcount
        if diff != 0:
            self.dbg_print(DBG, nsr + diff, nsr + diff, count, rcount)
            return (nsr+diff, nsr+diff, (nsr - psr))
        return (psr, nsr-1, (nsr - psr))

    # pylint: disable=E0633
    def getlistcount(self, ws, sr, er, col):
        tsr = sr
        ter = er
        listvalue = []
        tmpvalue = None
        if col is None:
            return listvalue
        while tsr <= ter:
            width = 1
            cell = ws.cell(row=tsr, column=col)
            value = cell.value
            self.dbg_print(DBG, "val", tsr, col, value)
            if value is not None:
                if tmpvalue is not None:
                    (val, lsr, ler, wd) = tmpvalue
                    self.dbg_print(DBG, val, lsr, ler, wd)
                    tmpvalue = (val, lsr, tsr-1, wd)
                    listvalue.append(tmpvalue)
                tmpvalue = (value, tsr, tsr + width - 1, width)
            tsr += width
        if tmpvalue is not None:
            (val, lsr, ler, wd) = tmpvalue
            tmpvalue = (val, lsr, tsr-1, wd)
            listvalue.append(tmpvalue)
        self.dbg_print(DBG, sr, er, col, listvalue)
        return listvalue

    def getmykeywidth(self, ws, baserow, count=0, filters=None):
        sr = baserow + 1
        er = sr
        ret1 = None
        alllist = 0
        for name in self.namekeys():
            self.dbg_print(DBG, "start for ", name)
            attrib = self.attributes_dict[name]
            if filters is None or \
               (filters is not None and self.uname in filters):
                if attrib.getiskey():
                    col = self.getmyreadcolumn(attrib.uname)
                    self.dbg_print(DBG, attrib.uname, col)
                    if col is None:
                        continue
                    ret1 = self.getcolumnwidth(ws, col, baserow, count)
                    return ret1
        if alllist == 0:
            if count == 0:
                j = 0
                while not self.emptyrow(ws, sr+j):
                    j += 1
                return (sr, sr+j-1, j)
            else:
                (psr, per, pw) = self.getmykeywidth(ws, baserow, count-1)
                return (psr+pw, per+1, 1)
        return (sr, er, 1)

    def emptyrow(self, ws, sr):
        for k, v in self.loadcolumnmap.items():
            self.dbg_print(DBG, k, v)
            if ws.cell(row=sr, column=v).value is not None:
                return False
        return True

    def wsrowisvalid(self, ws, baserow, count):
        (sr, er, width) = self.getmykeywidth(ws, baserow, count)
        self.dbg_print(DBG, sr, er, width)
        for k, v in self.loadcolumnmap.items():
            self.dbg_print(DBG, k, v)
            if ws.cell(row=sr, column=v).value is not None:
                return True
        return False

    def loadmyobj(self, ws, baserow, count=0, filters=None):
        if not any(self.loadcolumnmap):
            self.loadheaders(ws, baserow - 1, filters)
        (sr, er, width) = self.getmykeywidth(ws, baserow, count)
        self.dbg_print(DBG, sr, er, width)
        for name in self.namekeys():
            attrib = self.attributes_dict[name]
            attrib.wsload(ws, sr, er, filters)

    # pylint: disable=W0612
    def loadmyobjfromrow(self, ws, baserow, osr, filters=None):
        self.loadheaders(ws, baserow - 1, filters)
        i = 0
        while self.wsrowisvalid(ws, baserow, i) is True:
            (sr, er, width) = self.getmykeywidth(ws, baserow, i, filters)
            if sr < osr:
                i += 1
            else:
                break
        if sr != osr:
            print("Unable to load the object for ", self.container,
                  "at Start Row:", sr)
            return False
        return self.loadmyobj(ws, baserow, i, filters)

    def getmywslist(self, ws, baserow, filters=None):
        objlist = []
        obj = self
        i = 0
        self.loadheaders(ws, baserow - 1, filters)
        tmpdict = dict(self.loadcolumnmap)
        adcolumn = self.adjustcolumn
        while self.wsrowisvalid(ws, baserow, i) is True:
            obj.loadmyobj(ws, baserow, i, filters)
            objlist.append(obj)
            obj = self.__class__()
            obj.loadcolumnmap = dict(tmpdict)
            obj.adjustcolumn = adcolumn
            i += 1
        return objlist

    def __eq__(self, rhs):
        return self.issameas(rhs)

    def issameas(self, other):
        if isinstance(other, self.__class__):
            for name in self.namekeys():
                attrib1 = self.attributes_dict[name]
                attrib2 = other.attributes_dict[name]
                if not attrib1.issameas(attrib2):
                    self.dbg_print(DBG, "false :", attrib1, attrib2)
                    return False
        return True

    def setconfigchanged(self, change=0):
        self.configchanged |= change

    @staticmethod
    def pseudodictrestobject(clidict):
        """ Static method available to create a pseudo rest object Instance."""
        if isinstance(clidict, dict) and any(clidict):
            for mycontainer, attributes in clidict.items():
                restobject = rest_object(rest_obj_type.pseudo_rest_object, mycontainer)
                for k, v in attributes.items():
                    restobject.dbg_print(DBG, k, v['valtype'], v['resttype'])
                    restobject.add(rest_attribute(k, v['valtype'], None, v['resttype']))
                restobject.setmycustomcli(attributes)
                restobject.dbg_print(DBG, restobject)
                return restobject
        return None
