# Copyright © 2018 Broadcom.  All rights reserved.
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
         mytunnelobject.set_l2_cos([{ 'priority-control": 0, 'fc-priority-high" : 1 ........}])
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




import http.client as httplib
import urllib
import string
import base64
import json
import xml.etree.ElementTree as ET
import pyfos.pyfos_util as pyfos_util
import urllib.parse
import re
import inspect
import time
from pyfos.pyfos_type import *
from pyfos.pyfos_version import *
import getpass
import getopt
import ast
import sys
import os


class rest_obj_type():
    """
    This class identifies the different rest objects supported by FOS
    All derived class from rest_object should define their enum here accordingly
    """
    unknown         = 0
    reservedcount   = 1
    # do no use enums from 1-9
    extension_start = 10
    ipif            = 11
    iproute         = 12
    tunnel          = 13
    tunnel_stats    = 14
    circuit         = 15
    circuit_stats   = 16
    ipsec           = 17
    gige            = 18
    gige_stats      = 19
    extension_end   = 100
    fos_start       = 101
    zone            = 102
    zone_defined    = 103
    zone_effective  = 104
    fabric          = 105
    switch          = 106
    port_config     = 107
    port_stats      = 108
    port_diag       = 109
    fdmi_hba        = 110
    fdmi_port       = 111
    logical_switch  = 112
    name_server     = 113
    #AG objects
    ag_start        = 200
    ag_portgroup    = 201
    ag_nportmap     = 202
    ag_fportlist    = 203
    ag_policy       = 204
    ag_nportsettings = 205
    ag_end          = 299
    fos_end         = 300
    #use enums from 100 onwards
    
def getrestobjectname(objtype, fmt = 0):
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
        elif objtype == rest_obj_type.zone:
            return "FOS ZONE"
        elif objtype == rest_obj_type.zone_defined:
            return "FOS Defined Zone"
        elif objtype == rest_obj_type.zone_effective:
            return "FOS Effective Zone"
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
        elif objtype == rest_obj_type.fdmi_hba:
            return "FOS FDMI HBA"
        elif objtype == rest_obj_type.fdmi_port:
            return "FOS FDMI Port"
        elif objtype == rest_obj_type.logical_switch:
            return "FOS Logical Switch"
        elif objtype == rest_obj_type.name_server:
            return "FOS Name Server"
        else:
            return "NOT_EXT_OBJECT"
    else :
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
        elif objtype == rest_obj_type.zone:
            return "zone"
        elif objtype == rest_obj_type.zone_defined:
            return "definedzone"
        elif objtype == rest_obj_type.zone_effective:
            return "effectivezone"
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
        elif objtype == rest_obj_type.fdmi_hba:
            return "fdmihba"
        elif objtype == rest_obj_type.fdmi_port:
            return "fdmiport"
        elif objtype == rest_obj_type.logical_switch:
            return "Logicalswitch"
        elif objtype == rest_obj_type.name_server:
            return "nameserver"
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
    GET_ALL_FILTERS = 5
    GET_ALL_FILTERS_KEY = 6


global  REST_ATTRIBUTE_KEY
global  REST_ATTRIBUTE_CONFIG
global  REST_ATTRIBUTE_CONFIG_MANDATORY
global  REST_ATTRIBUTE_NOT_CONFIG
global  REST_ATTRIBUTE_CONTAINER
global  REST_ATTRIBUTE_LEAF_LIST
global  REST_ATTRIBUTE_CONTAINER_LIST

    

REST_ATTRIBUTE_KEY = (rest_yang_type.yang_leaf | rest_yang_config.yang_key)
REST_ATTRIBUTE_CONFIG = (rest_yang_type.yang_leaf | rest_yang_config.yang_config)
REST_ATTRIBUTE_CONFIG_MANDATORY = (rest_yang_type.yang_leaf | rest_yang_config.yang_config | rest_yang_config.yang_mandatory)
REST_ATTRIBUTE_NOT_CONFIG = (rest_yang_type.yang_leaf)
REST_ATTRIBUTE_CONTAINER = (rest_yang_type.yang_container | rest_yang_config.yang_config)
REST_ATTRIBUTE_LEAF_LIST = (rest_yang_type.yang_leaf_list | rest_yang_config.yang_config)
REST_ATTRIBUTE_CONTAINER_LIST = (rest_yang_type.yang_container | rest_yang_type.yang_list | rest_yang_config.yang_config)


IGN=0
DBG=1
INF=2
WRN=3
ERR=4

class rest_debug():
    def __init__(self, enable=False, level=ERR, session=None):
        """Instantiate a rest_debugger"""
        self.dbg_level=level
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
                       str(" :<") + "".join(map(str,args)) + ">\nSTACK :\n" +\
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

    def __init__(self, name, a_type, value=dict(), rest_type=0, ver=None, parent=None, list_count = 0):     
        """Instantiate a rest_attribute """
        # TODO Compact the attribute class based on new defines
        self.name = name
        self.a_type = pyfos_type(a_type)
        self.is_key = (rest_type & rest_yang_config.yang_key)
        self.is_config =(rest_type & rest_yang_config.yang_config)
        self.is_mandatory = (rest_type & rest_yang_config.yang_mandatory)
        self.is_attribute_map = (rest_type & rest_yang_type.yang_container)
        self.is_list = (rest_type & (rest_yang_type.yang_list | rest_yang_type.yang_leaf_list))
        self.is_leaf = (rest_type & (rest_yang_type.yang_leaf|rest_yang_type.yang_leaf_list))
        self.properties = rest_type
        self.parent = parent
        self.list_count = list_count
        if self.is_attribute_map and not self.is_list:
            self.value = dict()
            for k1, v1 in value.items():
                myattrib = rest_attribute(k1, v1, is_key, is_config)
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
        self.attrib = dict()
        if ver != None:
            self.version_supported = fosversion_range(ver)
            self.version_active = fosversion(self.version_supported.start.to_string())
        else:
            self.version_supported = None
            self.version_active = None
        self.uname = None
        self.clone_dict = dict({ 'name':name, 'value': value, 'version': ver, 'type': a_type, 'prop': rest_type})
        self.hierarchy = []
        self.restobject = None
        self.filter = 0
        self.usage = None
        self.loption = None
        self.soption = None
        self.help = None
        self.optional = 0
        self.cmdline = None


    def checkusagefilter(self, filters):
        if filters is not None and self.uname in filters or filters is None:
            return 1
        return 0
        

    def setusage(self):
        """ Sets the usage of the attribute parsing. """
        if self.checkusagefilter(None) == 0:
            return
        retdict=self.restobject.overwriteparser(self.uname)
        self.soption = None
        self.loption = str(self.getallparentstring() + self.getname())
        self.help = "set \"" + self.name + "\""
        self.optional = 0
        optional = ""
        cmdline=""
        if retdict is not None:
            if 'help' in retdict.keys():
                self.help = retdict['help']
            if 'loption' in retdict.keys():
                self.loption = retdict['loption']
            if 'soption' in retdict.keys():
                self.soption = retdict['soption']
            if 'optional' in retdict.keys():
                if retdict['optional'] == 1:
                    optional="[OPTIONAL]"
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
            return
        retdict = dict()
        retdict.update({"soption" : self.soption})
        retdict.update({"loption" : self.loption})
        retdict.update({"help" : self.help})
        retdict.update({"optional" : self.optional})
        retdict.update({"value" : self.optional})
        return {self.uname : retdict}


    def getusage(self, filters=None):
        if self.checkusagefilter(filters):
            return (self.usage)
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
                    return (sopt, lopt)
                else:
                    return (lopt)
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
            elif len(self.value) == 0:
                return True
            else:
                retdict = dict()
                if self.value is not None:
                    for k1, v1 in self.value.items():
                        if v1.is_empty() == False:
                            retdict[k1] = v1
                if len(retdict) == 0:
                    return True
                else:
                    return False
        if self.is_list:
            if self.value is None:
                return True
            elif len(self.value) == 0:
                return True
            else:
                if self.is_leaf:
                    if len(self.value) == 0:
                        return True
                    else:
                        return False

                retarray = []
                for v1 in self.value:
                    retdict = dict()
                    for k2, v2 in v1.items():
                        if v2.is_empty() == False:
                            retdict[k2] = v2
                    if len(retdict) is not 0:
                        retarray.append(v1)
                if len(retarray) == 0:
                    return True
                else:
                    return False
        else:
            if self.value == None:
                return True
            else:
                return False

    
    def reprJSON(self, ver = None):
        """Gets the JSON representation of the rest_attribute."""          
        if self.is_attribute_map and not self.is_list:
            if self.value is None:
                return None
            elif len(self.value) == 0:
                return None
            else:
                retdict = dict()
                if self.value is not None:
                    for k1, v1 in self.value.items():
                        if v1.is_empty() == False:
                            if ver == None or self.version_supported.visible(ver):
                                retdict[k1] = v1
                if len(retdict) == 0:
                    return None
                else:
                    return retdict
        if self.is_list:
            if self.value is None:
                return None
            elif len(self.value) == 0:
                return None
            else:
                if self.is_leaf:
                    if len(self.value) == 0:
                        return None
                    elif  ver == None or self.version_supported.visible(ver):
                        return self.value
                    else:
                        return None

                retarray = []
                if self.value is not None:
                    for v1 in self.value:
                        if ver == None or self.version_supported.visible(ver):
                            retdict = dict()
                            for k2, v2 in v1.items():
                                if v2.is_empty() == False:
                                    if ver == None or v2.version_supported.visible(ver):
                                        retdict[k2] = v2
                            if len(retdict) is not 0:
                                retarray.append(v1)
                if len(retarray) == 0:
                    return None
                else:
                    return retarray
        else:
            if self.value == None:
                return None
            elif ver == None or self.version_supported.visible(ver):
                return self.value
            else:
                return None
            

    def getclonename(self):
        """Gets the clone name of the rest_attribute."""
        return (self.uname)
     
    def getname(self):
        """Gets the name of the rest_attribute. """
        return self.name

    def setparent(self, parent, list_count = 0):
        """Sets the parent of the rest_attribute. """
        if  parent.getisattributelist() or parent.parent_is_list:
            self.parent = parent
            self.parent_is_list = 1          
        else:
            self.parent = parent
        return
    
    def compare(self, retdict, reset_modified = 0):
        """Compares the object to the passed dictionary values. """
        if self.getisattributemap() and not self.getisattributelist():
            for k1,v1 in self.value.items():
                if isinstance(retdict, list):
                    myvalue = retdict[0]
                elif isinstance(retdict, dict):
                    myvalue = retdict;
                else:
                    #TODO remove the newline check after xmltodict merge
                    if len (retdict) and retdict != '\n':
                        print ("Illegal param passed for Key", self.uname, "Dict:", retdict, "\n")
                        return 1
                    else:
                        return 0
                if k1 in myvalue.keys():
                    if v1.compare(myvalue[k1]) != 0:
                        return 1
            return 0
        elif self.getisattributelist():
            if isinstance(retdict, list):
                if len(retdict) >= len (self.value):
                    #Leaf list handling
                    if self.is_leaf:
                        for i in range (len(self.value)):
                            found = 0
                            for j in range(len(retdict)):
                                if self.value[i] == retdict[j]:
                                    found = 1
                                    break
                            if found == 0:
                                return 1
                        return 0
                    else:
                        #Not a Leaf list
                        for i in range(len (self.value)):
                            value = self.value[i]
                            compare = len(value)
                            
                            for k1,v1 in value.items():
                                for j in range(len(retdict)):
                                    compare = len(value)
                                    myvalue = retdict[j]
                                    if k1 in myvalue.keys():
                                        if v1.compare(myvalue[k1]) == 1:
                                            continue
                                        else:
                                            compare -= 1
                                            if compare == 0:
                                                break
                                        
                                if compare == 0:
                                    break;
                            if compare != 0:
                                return compare
                    return 0
                else:
                    return 1
                
            else:
                if self.is_leaf:
                    for i in range (len(self.value)):
                        if self.value[i] != value :
                            return 1
                else:
                    for i in range (len(self.value)):
                        value = self.value[i]
                        compare = len(value)

                        for k1,v1 in value.items():
                            compare = len(value)
                            myvalue = retdict
                            if k1 in myvalue.keys():
                                if v1.compare(myvalue[k1]) == 1:
                                    return 1
            return 0            
        else:
            if self.getiskey() and self.getisconfig():
                if value == None or value == retdict:
                    if reset_modified:
                            self.setvaluechanged(0)
                    return 1
                else:
                    self.dbg_print(ERR, "Mismatch values for Attribute ",
                                     self.getname(), "Value (",
                                     retdict, "/",  self.getvalue())
                    return 0

        if reset_modified:
            self.setvaluechanged(0)
        return 1

    def modified(self):
        """Checks if any of the values in the object are modified. """
        if self.getisattributemap() and not self.getisattributelist():
            for k1,v1 in self.value.items():
                if v1.modified() == 1:
                    return 1
        elif self.getisattributelist():
            #Leaf list handling
            if self.is_leaf:
                if self.getisvaluechanged():
                    return 1
                else:
                    return 0
                
            #Not leaf list 
            for i in range(len(self.value.items())):
                value = self.value[i]
                for k1,v1 in  value.items():
                    if v1.modified() == 1:
                        return 1
        else:
            if self.getiskey() and self.getisconfig():
                if self.getisvaluechanged():
                    return 1
        return 0

    def clean(self, filters):
        """Checks if anything must be cleaned. """
        if filters is not None and (self.uname in filters or self.getiskey()):
            return

        if self.getisattributemap() and not self.getisattributelist():
            for k1,v1 in self.value.items():
                v1.clean(filters)
        elif self.getisattributelist():
            #Leaf list handling
            if self.is_leaf:
                self.value.clear()
                self.value = [] 
                return 0
            #Not leaf list
            list_count = len(self.value) - 1
            if list_count > 0:
                if (list_count == 1):
                    del self.value[1]
                else:
                    del self.value[1: list_count]
            for i in range(1):
                value = self.value[i]
                for k1,v1 in  value.items():
                    v1.clean(filters)
        elif self.is_leaf:
            self.value = None
        return 0

    def getchildattrib(self, name, list_count = 0):
        """Gets the child attribute for this attribute. """     
        if self.getisattributemap() and not self.getisattributelist() and name in self.value.keys():
            return (self.value[name])
        elif self.getisattributelist():
            if list_count < len(self.value):
                value = self.value[list_count]
                if name in value.keys():
                    return value[name]
        return 0

    def addchild(self, attribute, list_count = 0):
        """Adds a child attribute to another attribute, which is a map. """
        if self.getisattributemap()  and not self.getisattributelist():
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
            self.hierarchy            

    def getuservalue(self):
        """Gets the value of the attribute. This is the external function. """
        correct_type, value = self.a_type.validate_peek(self.getvalue())
        if correct_type:
            return value
        else:
            self.dbg_print(ERR, "type of" + str(self.a_type.get_type()),\
                             "missmatched to " + str(self.getvalue()))
            return "type of" + str(self.a_type.get_type()) + "missmatched to " + str(self.getvalue())
        
    def getvalue(self):
        """Gets the value of the attribute. This is the internal function for the object. """
        if self.getisattributemap() and not self.getisattributelist() :
            mydict = dict()
            for k1, v1 in self.value.items():
                mydict.update({k1 : v1.getvalue()})
            return (mydict)
        if self.getisattributelist() :
            if self.is_leaf:
                return (self.value)
            
            mylist = []
            for i in range(len(self.value)):
                value = self.value[i]
                mydict = dict()
                for k1, v1 in value.items():
                    mydict.update({k1 : v1.getvalue()})
                mylist.append(mydict)
            return mylist
        else:
            return self.value
       
    def is_top_level(self):
        """Checks if the attribute is top level, that is, a direct child attribute of the REST object."""
        if self.getallparentstring() == "":
            return True
        else:
            return False

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
        self.attrib={self.name: self}
        return self.attrib

    def fromdict(self, attribdict):
        """Assigns the attrbiute value from a dictionary."""
        self.setvalue((attribdict[self.name]).getvalue())

    def getisvaluechanged(self):
        """Gets if the value is changed for the object."""
        return (self.value_changed)

    def setvaluechanged(self, changed):
        """Sets if the value is changed for the object."""
        self.value_changed = changed
        return
        
    def copy(self):
        """Copies the constructor for an attribute."""
        return rest_attribute(self.name, self.value, self.is_key, self.is_config)

    def clone(self, list_count = 0):
        """Clones an attribute."""
        if self.getisattributelist() or self.getisattributemap():
            hierarchy = self.restobject.gethierarchy(self.uname)
            self.dbg_print(DBG,"Hierarchy ", hierarchy, self.uname, "\n")
            self.clone_hierarchy(hierarchy, self, list_count)
            
    def clone_hierarchy(self, hierarchy,  parent, list_count):
        """Clones the attribute hierarchy of the attribute."""
        if isinstance(hierarchy, list):
            for i in range(len(hierarchy)):
                clone_dict = hierarchy[i]
                attribute = rest_attribute(clone_dict['name'], clone_dict['type'], clone_dict['value'], clone_dict['prop'], clone_dict['version'], parent,  list_count)
                if attribute.version_active < self.version_active:
                    attribute.version_active.from_string(attribute.version_active.to_string())
                attribute.restobject = self.restobject
                self.addchild(attribute, list_count)
                attribute.setclonename()
                attribute.setusage()
                # The list_count always starts from 0 becuase we are inside a container or list
                attribute.clone(0)
           
    def setuservalue(self, value, changed = 1, to_add = False):
        """Sets the value of the attribute external function."""
        if self.supportedop(rest_get_method.GET_ALL_KEY_CONFIG, self.version_active):
            return (self.setInfravalue(value, changed, to_add))
        else:
            myfunc = self.getclonename()
            self.dbg_print(ERR, "Unsupported: ", "set_" + myfunc,\
                    " function is not allowed for the attribute \"",\
                                         self.getname(),"\".\n")
            return {"info-code": -1, "info-message": "Incorrect call",\
                    "info-type": "Unsupported set operation on attribute"}
        return dict({self.name: self.getvalue()})


    def setInfravalue(self, value, changed = 1, to_add = False):
        # Validate type
        correct_type, rvalue = self.a_type.validate_peek(value)
        if not correct_type:
            self.dbg_print(ERR, "type of" + str(self.a_type.get_type()),\
                             "missmatched to " + type(value))
            return {"info-code": -1, "info-message": "Setting of the value failed",\
                    "info-type": "Incorrect type/format of value passed expected " +
                    str(self.a_type.get_type())}

        #validate Format
        result = self.setvalue(value, changed, to_add)

        if result:
            return {"info-code": -1, "info-message": "Setting of the value failed",\
                    "info-type": "Incorrect type/format of value passed"}
      
        # bubble up the version default till object
        myver = self.version_active
        myparent = self.parent
        while (myparent != None) and (myver > myparent.version_active):
            myparent.version_active.from_string(myver.to_string())
            myparent = myparent.parent
        if myver > self.restobject.version_active:
            self.restobject.version_active.from_string(myver.to_string())
            self.dbg_print(DBG, "Active Version changed:", myver.to_string())
        return dict({self.name: self.getvalue()})


    def parseInfraset(self, value, changed = 1, to_add = False):
        valuedict = self.setInfravalue(value, changed, to_add)
        if isinstance(valuedict, dict):
            if "info-code" in valuedict.keys():
                print("Error :", valuedict['info-message'], "info",
                      valuedict['info-type'])
                return 1
        return 0
    

    def setvalue(self, value, changed=1, to_add = False):
        """Sets the value of the attribute internal function."""
        ver =  self.version_active     
        if self.getisattributemap() and not self.getisattributelist():
            self.dbg_print(DBG, "Container" , self.name , value)
            if value == None:
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
                                       self.name, "\" Value:",  myvalue)
                        return 1
                    if k1 in myvalue.keys():
                        if v1.version_active > ver:
                            ver.from_string(v1.version_active.to_string())
                            self.dbg_print(DBG, self.name,\
                                v1.version_active.to_string(), ver.to_string())
                            
                        v1.setvalue(myvalue[k1], changed)
                        self.dbg_print(DBG, "calling setvalue", v1.name)
                        
        elif self.getisattributelist():
            if isinstance(value, list) :
                if self.is_leaf:
                    self.dbg_print(DBG, "Leaf List ", self.name, value)
                    if not to_add:
                        self.value.clear()
                    for v1 in value:
                        self.value.append(v1)
                    self.dbg_print(DBG, "Leaf List ", self.name,
                                     self.value, value)
                else :    
                    for i in range(len(value)):
                        if len(self.value) <= i :
                            self.clone(i)

                    for i in range(len(value)):
                        self.dbg_print(DBG, "container List " , self.name ,
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
                                     self.name , value)
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
        else :
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
                    if ver == None or v1.version_supported.visible(ver):
                        mydisplay.append(self.value[k1].objdisplay(ver))

     
            mydict={"name": self.name, "pointer" :self,"value" :mydisplay,  "iskey": self.is_key, "isconfig" : self.is_config}
        else :
            mydict={"name": self.name, "pointer" :self,"value" :self.value,  "iskey": self.is_key, "isconfig" : self.is_config}
            
        self.dbg_print(DBG, mydict)
        return mydict


    def display(self, ver):
        """Displays an attribute."""
        mydisplay = []
        mydict = dict()
        if self.getisattributemap() or (self.getisattributelist() and self.is_leaf == 0):
            self.dbg_print(DBG, self.name, "::", self.value)
            if self.getisattributelist() :
                for i in range(len(self.value)):
                    tmpdict = self.value[i]
                    list1 = []
                    for k1, v1 in tmpdict.items():
                        if v1.version_supported.visible(ver):
                            #list1.append(tmpdict[k1].display(ver))
                            list1.append(v1.display(ver))
                    if  len(list1)>0:
                        mydisplay.append(list1)
            else:               
                for k1, v1 in self.value.items():
                    if v1.version_supported.visible(ver):
                        #mydisplay.append(self.value[k1].display(ver))
                        mydisplay.append(v1.display(ver))

            #mydict={"name": self.name,"value" :mydisplay}
            if self.version_supported.visible(ver):
                mydict={self.name: mydisplay}
                self.dbg_print(DBG, self.name, "::", mydict)
                    
        else :
            #mydict={"name": self.name, "value" :self.value}
            if self.version_supported.visible(ver):
                mydict={self.name:self.value}
            
        self.dbg_print(DBG, mydict)
        return mydict


    def __repr__(self):
        return (json.dumps(self, cls=rest_object_encoder, sort_keys=True, indent=4))


    def supportedop (self, op, ver):
        """Checks if the attribute is supported for the GET methods requested."""
        if 0 == self.version_supported.visible(ver):
            self.dbg_print(DBG, "Ignored class[", \
                self.display(self.version_active), "] Active Version:",\
                self.version_active.to_string()," Requested version ",\
                ver.to_string())
            return 0
        if self.filter == 1 and (op == rest_get_method.GET_ALL_FILTERS or
                                 op == rest_get_method.GET_ALL_FILTERS_KEY):
            return 1
        if self.is_leaf:
            if op == rest_get_method.GET_ALL_KEY_CONFIG:
                if self.getisconfig() or self.getiskey() or self.is_mandatory:
                    return 1
            if op == rest_get_method.GET_ALL_KEY or op == rest_get_method.GET_ALL_FILTERS_KEY:
                if self.getiskey():
                    return 1
            if op == rest_get_method.GET_KEY_AND_MODIFIED_CONFIG:
                if self.getisconfig() and self.getisvaluechanged() or self.getiskey():
                    self.dbg_print(DBG, self.name, " :", self.value, "Changes:", self.getisvaluechanged())
                    return 1
            if op == rest_get_method.GET_ALL_CONFIG:
                    if self.getisconfig() and not self.getiskey():
                        return 1
            if op == rest_get_method.GET_MODIFIED_CONFIG:
                    if self.getisconfig() and self.getisvaluechanged():
                        return 1
        elif self.getisattributelist():
            for i in range(len(self.value)):
                for k1,v1 in self.value[i].items():
                    if v1.supportedop(op, ver) == 1:
                        return 1
        elif self.getisattributemap():
            for k1,v1 in self.value.items():
                if v1.supportedop(op, ver) == 1:
                    return 1
                
        return 0


    def create_html_content(self, optype, version):
        """Creates the post string data equivalent for an attribute."""
        poststring = ""
        usefilter = 0
        if optype == rest_get_method.GET_ALL_FILTERS or \
            optype == rest_get_method.GET_ALL_FILTERS_KEY:
            usefilter = 1
        self.dbg_print(DBG, self.name , " : ", self.value, "OP :",  self.supportedop(optype, version)) 
        if self.getisattributemap() and not self.getisattributelist() and \
               self.supportedop(optype, version):
            poststringchild = ""
            if self.filter == 1 and usefilter == 1:
                return "\n<" + self.name + "></" + self.name + ">"
            else:
                for k1, v1 in self.value.items():
                    poststringchild += v1.create_html_content(optype, version)
                if (len(poststringchild)):
                    poststringchild = re.sub("\n", "\n\t", poststringchild)
                    poststring = "\n<" + self.name + ">" + poststringchild + "\n</" + self.name + ">"
                else:
                    return (poststringchild)
            return poststring
        elif self.getisattributelist() and self.supportedop(optype, version):
            if self.filter == 1 and usefilter == 1:
                return "\n<" + self.name + "></" + self.name + ">"
            elif None != self.value:
                poststringchild = ""
                listvalue = self.value
                if isinstance(listvalue, list):
                    for i in range(len(listvalue)):
                        poststringchild = ""
                        value = listvalue[i]
                        # Leaf List Handling
                        if self.is_leaf:
                            if value != "undef" :
                                poststring += "\n<" + self.name + ">" + value + "</" + self.name + ">"
                        else:
                            # Not a Leaf List Handling
                            for k1, v1 in value.items():
                                poststringchild += v1.create_html_content(optype, version)
                                
                            if (len(poststringchild)):
                                poststringchild = re.sub("\n", "\n\t", poststringchild)
                                poststring += "\n<" + self.name + ">" + poststringchild + "\n</" + self.name + ">"
                    return poststring
        else:
            if self.filter == 1 and usefilter == 1:
                return "\n<" + self.name + "></" + self.name + ">"
            elif self.value != None and self.supportedop(optype, version):
                return ("\n<" + self.name + ">" + str(self.value) + "</" + self.name + ">");
        return ""
        
    def uri_string(self, optype, ver):
        """Creates the URI string data equivalent for an attribute."""
        if (self.getisattributemap() or self.getisattributelist()) and self.is_leaf == 0:
            uristring = "/" + self.name
            if optype == rest_get_method.GET_ALL_FILTERS:
                return "\n</" + self.name + ">"
            for k1, v1 in self.value.items():
                if v1.supportedop(optype, ver):
                    uristring += v1.uri_string()
            return uristring
        else:
            if optype == rest_get_method.GET_ALL_FILTERS:
                return "\n</" + self.name + ">"
            elif None != self.getvalue() :
                return ("/" + self.name + "/" + urllib.parse.quote(str(self.getvalue()), safe=''));
        return ""

    def dbg_print(self, level, *args):
        self.restobject.dbg_print(level, args)


class rest_handler(rest_debug):
    """ This class encompasses all the REST operations supported from the FOS objects as per YANG.
    
    Attributes:
        session: The login `session` to a FOS switch.
        uri_base:  The `uri_base` is the base URI string to access the corresponding object.
        obj:  The `obj` is the corresponding REST object instance for rest_handler to work on.
        test: The `test` dictionary captures all the different test executions.

    """
    global test
    test = dict()
    test.update({1 : {"total_tc": 0,"show_all": 0, "get" : 0, "get_uri": 0, "post": 0, "patch": 0, "create_uri":0, "delete" :0, "delete_uri":0, "modify_put" :0, "modify_put_uri" :0, "modify_patch": 0, "modify_patch_uri" :0}})
    

    def __init__(self, uri_base):
        rest_debug.__init__(self)
        self.uri_base = uri_base
        self.obj = self
        
        if not self.obj.obj_type in test.keys():
            test.update({self.obj.obj_type : {"show_all": 0, "get" : 0, "get_uri": 0, "post": 0, "patch": 0, "create_uri":0, "delete" :0, "delete_uri":0, "modify_put" :0, "modify_put_uri" :0, "modify_patch": 0, "modify_patch_uri" :0}})
        
    def createtest(self, request, negative = 0):
        dictglobal = test[1]
        dictobj = test[self.obj.obj_type]
        counttotal = dictglobal['total_tc']
        counttotal +=1
        countg = dictglobal[request]
        countg +=1
        counto = dictobj[request]
        counto +=1

        dictglobal[request] = countg
        dictobj[request] = counto
        dictglobal['total_tc'] = counttotal
        mytestcase="Testing " + request + " for " + getrestobjectname(self.obj.obj_type) + str(self.__class__)
        testcaseID = "Rest" + str(counttotal) + "." + request + "." + str(countg) + getrestobjectname(self.obj.obj_type, 1)+ "." + str(counto) +""
        pyfos_util.test_title_set(testcaseID.upper(), mytestcase.upper())
        pyfos_util.test_negative_test_set(negative)
        time.sleep(3)

    def isvalidsession(self, session):
        #print self.session
        if isinstance(session, dict) and "credential" in session.keys():
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
        
    def validate(self, negative, retdict):
        if self.checkstatus(retdict):
                if not negative:
                    getdict = self.show(0,0)
                    if self.checkstatus(getdict):
                        #showstr = json.dumps(getdict, sort_keys=True)
                        #objstr self.obj.display()
                        #objstr = json.dumps(self.obj.display(), sort_keys=True)
                        #if re.search(objstr, showstr):
                            #print "found"
                        #print "Show:\n", showstr
                        #print "\nOBJ:\n", objstr
                        if self.obj.container in getdict.keys() and self.obj.compare(getdict) == 1:
                            #pyfos_util.test_explicit_result_failed("Objects do not match")
                            print ("Return Dict:\n",getdict,"\nObj Display:\n")
                            self.obj.display()
                            #print "\n"
                            
                
        return retdict
        

    def show_all(self, session, negative = 0, is_tc=0):
        ret = self.obj.is_valid(session)
        if ( ret["info-code"] != 0 ) :
            return ret;
        if is_tc :
            self.createtest("show_all", negative)
        return pyfos_util.get_request(session, self.uri_base, "")


    def get(self, session, negative = 0, is_tc=0):
        ret = self.obj.is_valid(session)
        if ( ret["info-code"] != 0 ) :
            return ret;
        if is_tc: 
            self.createtest( "get", negative)
        if self.isfilterset() > 0:
            ret =  pyfos_util.get_request(session, self.uri_base, self.obj.create_html_content(rest_get_method.GET_ALL_FILTERS_KEY, session))
        else:
            ret =  pyfos_util.get_request(session, self.uri_base, self.obj.create_html_content(rest_get_method.GET_ALL_KEY, session))
        return (ret)
    

    def get_uri(self, session, negative = 0, is_tc = 0):
        ret = self.obj.is_valid(session)
        if ( ret["info-code"] != 0 ) :
            return ret;
        if is_tc:
            self.createtest("get_uri", negative)
        ret = pyfos_util.get_request(session, self.uri_base + self.obj.uri_string(rest_get_method.GET_ALL_KEY, session), "")
        self.dbg_print(DBG,"GET URI:\n", self.uri_base + self.obj.uri_string(rest_get_method.GET_ALL_KEY, session), ret)
        return ret


    def options(self, session, negative = 0, is_tc = 0):
        ret = self.obj.is_valid(session)
        if ( ret["info-code"] != 0 ) :
            return ret;
        if is_tc:
            self.createtest("options", negative)
        ret = pyfos_util.options_request(session, self.uri_base, self.obj.create_html_content(0, session))
        self.dbg_print(DBG,"Options:\n", self.uri_base, self.obj.create_html_content(0, session), ret)
        return ret


    def post(self, session, negative = 0, is_tc = 0):
        ret = self.obj.is_valid(session)
        if ( ret["info-code"] != 0 ) :
            return ret;
        if is_tc:
            self.createtest("post", negative)
        ret = pyfos_util.post_request(session, self.uri_base, self.obj.create_html_content(0, session))
        self.dbg_print(DBG,"Create:\n", self.uri_base, self.obj.create_html_content(0, session), ret)
        return ret


    def delete(self, session, negative = 0, is_tc = 0):
        ret = self.obj.is_valid(session)
        if ( ret["info-code"] != 0 ) :
            return ret
        if is_tc :
            self.createtest("delete", negative)
        ret = pyfos_util.delete_request(session, self.uri_base, self.obj.create_html_content(rest_get_method.GET_KEY_AND_MODIFIED_CONFIG, session))
        self.dbg_print(DBG,"Delete:\n", self.uri_base, self.obj.create_html_content(rest_get_method.GET_KEY_AND_MODIFIED_CONFIG, session), ret)
        return ret


    def delete_uri(self, session, negative =0, is_tc =0):
        ret = self.obj.is_valid(session)
        if ( ret["info-code"] != 0 ) :
            return ret
        if is_tc:
            self.createtest("delete_uri", negative)
        ret = pyfos_util.delete_request(session, self.uri_base + self.obj.uri_string(rest_get_method.GET_KEY_AND_MODIFIED_CONFIG, session), "")
        self.dbg_print(DBG,"Delete:\n", self.uri_base + self.obj.uri_string(rest_get_method.GET_KEY_AND_MODIFIED_CONFIG, session), ret)
        return ret


    def patch(self, session, negative = 0, is_tc = 0, modified_dict = {}):
        ret = self.obj.is_valid(session)
        if ( ret["info-code"] != 0 ) :
            return ret
        self.load(modified_dict, 1)
        if is_tc:
            self.createtest("patch", negative)
        ret = pyfos_util.patch_request(session, self.uri_base, self.obj.create_html_content(rest_get_method.GET_KEY_AND_MODIFIED_CONFIG, session))
        self.dbg_print(DBG,"Delete:\n", self.uri_base, self.obj.create_html_content(rest_get_method.GET_KEY_AND_MODIFIED_CONFIG, session), ret)
        return ret


    @staticmethod
    def patch_all(session, negative = 0, is_tc = 0, modified_dict = {},
                  objsList=[]):
        "The patch_all handler handles more than one object to perform a patch operation; for example, a list of ports."
        buf = ""
        if "Authorization" in session['credential'].keys() == 0:
            return {"info-code": -1, "info-message": "Invalid session", "info-type": "Incorrect auth details in session"}

        for obj in objsList:
            '''
            print ("Type\n", type(obj), type(obj.obj))
            ret = obj.obj.is_valid(session)

            if ( ret["info-code"] != 0 ) :
                return ret
            obj.load(modified_dict, 1)
            if is_tc:
                obj.createtest("patch", negative)
            '''
            uri_base = obj.uri_base

            buf += obj.obj.create_html_content(rest_get_method.GET_KEY_AND_MODIFIED_CONFIG, session)


        ret = pyfos_util.patch_request(session, uri_base, buf)
        self.dbg_print(DBG,"Delete:\n", uri_base, buf, ret)
        return ret


    @staticmethod
    def post_all(session, negative = 0, is_tc = 0, modified_dict = {},
                  objsList=[]):
        "The post_all handler handles more than one object to perform post operation; for example, a list of ports."

        buf = ""
        
        if "Authorization" in session['credential'].keys() == 0:
            return {"info-code": -1, "info-message": "Invalid session", "info-type": "Incorrect auth details in session"}

        for obj in objsList:
            '''
            ret = obj.obj.is_valid(session)
            if ( ret["info-code"] != 0 ) :
                return ret
            obj.load(modified_dict, 1)

            if is_tc:
                obj.createtest("patch", negative)
            '''

            uri_base = obj.uri_base
            buf += obj.obj.create_html_content(0, session)

        ret = pyfos_util.post_request(session, uri_base, buf)
        self.dbg_print(DBG,"Delete:\n", uri_base, buf, ret)
        return ret


    def patch_uri(self, session,  negative =0, is_tc = 0, modified_dict = {}):
        ret = self.obj.is_valid(session)
        if ( ret["info-code"] != 0 ) :
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
       # print (myobj.display())
       pyfos_util.response_print(myobj)

      Get using a key as a value::
    
       # Importing the module

       from pyfos.pyfos_brocade_gigabitethernet import extension_gigabitethernet

       # Using key as a dictionary
       myobj = extension_gigabitethernet.get(session, '4/15')

       # Display the object
       # print (myobj.display())
       pyfos_util.response_print(myobj)
       
      Get all::
    
       # Importing the module

       from pyfos.pyfos_brocade_gigabitethernet import extension_gigabitethernet

       # Using key as a dictionary
       objlist = extension_gigabitethernet.get(session)

       # Display the object
       # For i in range(len (objlist)):
       #    print(objlist[i].display())
       pyfos_util.response_print(objlist)

    """
    def __init__(self, obj_type, uri, visible_version = VER_RANGE_820_ABOVE):
        """ This is the constructor of the class."""
        self.obj_type = obj_type
        self.attributes_dict = dict()
        self.attributes = []
        self.clone_instance = dict()
        uriarray = uri.split("/")
        i = len(uriarray)
        self.container = uriarray[i-1]
        self.initialized = 0
        rest_handler.__init__(self, uri)
        self.version_supported = fosversion_range(visible_version)
        self.version_active = fosversion(self.version_supported.start.to_string())
        self.keyslist = []
        self.use_custom_cli = 1
        self.use_custom_dict = None


    def load(self, dictvalues, changed = 0, ver = None):
        """The function loads or deserialzes from a dictionary of values into the object itself."""
        if ver == None:
            ver = fosversion(self.version_active.to_string())
        self.initialized = 1
        if dictvalues != None and len(dictvalues):
            if self.container in dictvalues.keys():
                retdict = dictvalues[self.container]
            else:
                retdict = dictvalues
            for k1, v1 in retdict.items():
                if k1 in self.attributes_dict.keys():
                    attribute = self.attributes_dict[k1];
                    attribute.setvalue(v1, changed)
                    if (ver < attribute.version_active):
                        ver.from_string(attribute.version_active.to_string())
                else:
                    self.dbg_print(ERR, "Unknown Attribute \"" + k1 +
                                     "\" found in Object load",
                                     getrestobjectname(self.obj_type))
                    
        if ver != self.version_active:
            self.version_active.from_string(ver.to_string());


    def clean(self, filters=None):
        """The function cleans an object."""
        for k1,v1 in self.attributes_dict.items():
            v1.clean(filters)


    def getInstances(self, session, filters=None):
        get_by_key = 0
        obj = self.__class__()
        for i in range(len (self.keyslist)):
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
        elif not isinstance(obj_list, dict) or \
             obj.getcontainer() not in obj_list.keys():
            self.dbg_print(ERR, "Incorrect response format/data received",
                           obj_list)
            return (obj_list)
        elif obj_list[obj.getcontainer()] is None:
            return self
        elif isinstance(obj_list[obj.getcontainer()], dict):
            if obj_list[obj.getcontainer()] is not None:
                #self.dbg_print(DBG, pyfos_util.response_print(obj_list[obj.getcontainer()]))
                self.load(obj_list[obj.getcontainer()])
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
                if len(obj.keyslist) == len (args):
                    for i in range(len(obj.keyslist)):
                        obj.keyslist[i].setvalue(args[i])
                else:
                    self.dbg_print(ERR, "Incorrect key details passed[",
                                     cls, "] needs ", len(self.keylist),
                                     "keys, but given ", len(args))
            else:
                if len(obj.keyslist) == 1:
                    obj.keyslist[0].setvalue(args)

        return obj.getInstances(session, filters)


    def display(self, ver= None):
        """The function serializes the object to a dictionary."""
        if ver == None:
            ver = self.version_active

        mydict =  dict()
        for i in range(len(self.attributes)):
            mydict.update(self.attributes[i].display(ver))
        retdict = { self.container : mydict}
        return retdict

        
    def objdisplay(self, ver=None):
        """The function serializes the object to a dictionary with object pointer details."""
        #if ver == None:
           #ver = self.version_active

        mydict =  dict()
        for i in range(len(self.attributes)):
            mydict.update(self.attributes[i].objdisplay(ver))
        retdict = { self.container : mydict}
        return mydict

            
    def add(self, attribute, parents=[]):
        """The function adds the attribute to the REST object."""
        if attribute.version_active == None:
            attribute.setversion(self.version_supported.to_string())
        else:
            if 0 == self.version_supported.visible(attribute.version_active):
                self.dbg_print(ERR, "Version of attribute not supported by parent:",
                                 attribute.name)
                self.dbg_print(ERR, "Parent version::", self.version_supported.to_string())
                self.dbg_print(ERR, "Attribute version::", attribute.version_active.to_string())
                return 0

        attribute.restobject = self;
        #This is only required that direct level attributes are added to the attributes_dict
        if len(parents) == 0:
            self.attributes_dict.update(attribute.todict())
            self.attributes.append(attribute);
        else:
            parent = self.getparent(parents, attribute.version_active)
            if parent != None:
                parent.addchild(attribute)
            else:
                self.dbg_print(ERR, "No parent found matching hierarchy??", parents)
                self.dbg_print(INF,"Attribute:", attribute.getname(),\
                    " version::", attribute.version_active.to_string())
                return 0

        # Set the clonename of the attribute
        attribute.setclonename()
        attribute.setusage()
        myfunc = attribute.getclonename()
        # Install the generic Setters and getters of the function
        setattr(self, "set_" + myfunc.lower(), attribute.setuservalue)
        setattr(self, "peek_" + myfunc.lower(), attribute.getuservalue)
        self.addclone(attribute.uname, attribute)

        if attribute.is_key:
            self.keyslist.append(attribute)
            

    def addclone(self, name, attribute):
        """Adds the clone instance Update."""
        self.clone_instance.update({name: attribute})
        self.dbg_print(INF, "clone instance ", name, self.clone_instance)
        

    def default_set(self, value, changed=1):
        parentcaller = str(inspect.stack()[1][4])
        myfunc = re.sub('set_','',re.sub('^.*\w\.','',re.sub('\\(.*','',parentcaller)), 1)
        if myfunc in self.name_dict.keys():
            attribute = self.name_dict[myfunc]
            if attribute.supportedop(rest_get_method.GET_ALL_KEY_CONFIG):
                self.name_dict[myfunc].setvalue(value, changed)
            else :
                print  ("Unsupported: ", "set_" + myfunc, " function is not allowed for the attribute \"", attribute.getname(),"\".\n")
        else :
            print ("CALL: ", parentcaller, "FUNC: ", myfunc, self.name_dict.keys())
            return {"info-code": -1, "info-message": "Incorrect call", "info-type": "Unable to locate the attrib in the calls"}       


    def default_get(self):
        parentcaller = str(inspect.stack()[1][4])
        myfunc = re.sub('get_','',re.sub('^.*\w\.','',re.sub('\\(.*','',parentcaller)))
        if myfunc in self.name_dict.keys():
            return self.name_dict[myfunc].getvalue()
        else :
            print ("CALL: ", parentcaller, "FUNC: ", myfunc, self.name_dict.keys())
            return {"info-code": -1, "info-message": "Incorrect call", "info-type": "Unable to locate the attrib in the calls"}


    def reprJSON(self, ver = None):
        """Represents the REST object in JSON format."""
        if ver == None:
            ver = self.version_active
        retdict = dict()
        retdict[self.container] = dict()
        for k1, v1 in self.attributes_dict.items():
            if v1.is_empty() == False:
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
                return (self.use_custom_dict[clonename])
        return None


    def showusage(self, filters=None):
        cmd_mandatory = " <-i IPADDR> <-L LOGIN> <-P PASSWORD>"
        cmd_optional = " [-f VFID] [-s MODE] [-v]"
        objusagestr=""
        objkeystr=""
        objmandatory=""
        objoptional=""
        for k1,v1 in self.clone_instance.items():
            cmd_mandatory += v1.getmyopts(rest_useropt.FILTER_CMDLINE_MANDATORY, filters)
            cmd_optional += v1.getmyopts(rest_useropt.FILTER_CMDLINE_OPTIONAL, filters)
            if v1.is_key:
                objkeystr += v1.getusage(filters)
            elif v1.is_mandatory:
                objmandatory += v1.getusage(filters)
            else:
                objoptional += v1.getusage(filters)

        objusagestr = objkeystr + objmandatory + objoptional
        usagestr = "\n" + os.path. basename(sys.argv[0]) + cmd_mandatory + cmd_optional +"\n"
        usagestr += 'Usage:\n'
        usagestr += "\n  Infrastructure options:\n\n"
        usagestr += '{0:5}{1:3}--{2:40}{3:35}\n'.format("", "-i,", "ipaddr=IPADDR", "IP address of FOS switch.")
        usagestr += '{0:5}{1:3}--{2:40}{3:35}\n'.format("", "-L,", "login=LOGIN", "login name.")
        usagestr += '{0:5}{1:3}--{2:40}{3:35}\n'.format("", "-P,", "password=PASSWORD", "password.")
        usagestr += '{0:5}{1:3}--{2:40}{3:35}\n'.format("", "-f,", "vfid=VFID", "VFID of LS context to which the request is directed to [OPTIONAL].")
        usagestr += '{0:5}{1:3}--{2:40}{3:35}\n'.format("", "-s,", "secured=MODE", "HTTPS mode \"self\" or \"CA\" [OPTIONAL].")
        usagestr += '{0:5}{1:3}--{2:40}{3:35}\n'.format("", "-v,", "verbose", "verbose mode[OPTIONAL].")
        usagestr += "\n  Util scripts options:\n\n"
        usagestr += objusagestr
            
        return (usagestr)


    @classmethod
    def cliusage(cls, filters=None):
        myobj = cls()
        return (myobj.showusage(filters))

        
    def getmyopts(self, useropt, filters=None):
        if useropt == rest_useropt.FILTER_LGETOPT:
            myopts=[]
            for k1,v1 in self.clone_instance.items():
                    myopts += v1.getmyopts(useropt, filters)
            return myopts
        else:
            myopts=""
            for k1,v1 in self.clone_instance.items():
                    myopts += v1.getmyopts(useropt, filters)
            return myopts
        return ""


    def parse_attrib(self, opt, arg, filters=None):
        for k1,v1 in self.clone_instance.items():
            self.dbg_print(DBG, opt, arg,
                             v1.getmyopts(rest_useropt.FILTER_ALLOPT, filters))
            if opt in v1.getmyopts(rest_useropt.FILTER_ALLOPT, filters):
                if v1.is_leaf and v1.is_list:
                    return (v1.parseInfraset(arg.split(';')))
                elif v1.is_leaf:
                    return (v1.parseInfraset(arg))
                else:
                    modifiedarg=re.sub(";", " ", arg)
                    mydict = ast.literal_eval(modifiedarg)
                    another = json.loads(mydict)
                    if len(mydict)>0:
                        return (v1.parseInfraset(another))
                    else:
                        return 1
                return 0
        return 1
    

    def setmycustomcli(self, mydict):
        if mydict is not None:
            self.use_custom_dict = mydict
            self.use_custom_cli = 1
            for k1,v1 in self.clone_instance.items():
                v1.setusage()
        else:
            self.use_custom_dict = None
            self.use_custom_cli = 0            
        

    def resetmycustomcli(self):
        self.use_custom_dict = None
        self.use_custom_cli = 0
        for k1,v1 in self.clone_instance.items():
            v1.setusage()

 
    def displaycustomcli(self):
        retdict=dict()
        for k1,v1 in self.clone_instance.items():
            attribdict = v1.displaycustomcli()
            if attribdict is not None:
                retdict.update(attribdict)
        return {self.container : retdict}
            


    @classmethod
    def parse(cls, argv, inputs, filters, custom_cli, validate=None):
        myobj = cls()
        if custom_cli is not None:
            myobj.setmycustomcli(custom_cli)
        myopts = ["help", "ipaddr=", "vfid=", "login=", "password=", "secured=", "verbose"] + myobj.getmyopts(rest_useropt.FILTER_LGETOPT, filters)
        myobj.dbg_print(DBG, "Short:", myobj.getmyopts(rest_useropt.FILTER_SGETOPT, filters))
        myobj.dbg_print(DBG, "LONG:", myobj.getmyopts(rest_useropt.FILTER_LGETOPT, filters))
        try:
            opts, args = getopt.getopt(argv, "hi:f:L:P:s:v" + myobj.getmyopts(rest_useropt.FILTER_SGETOPT, filters), myopts)
        except getopt.GetoptError as err:
            print("getopt error", str(err))
            print(myobj.showusage(filters))
            return None

        myobj.dbg_print(DBG, opts)
        for opt, arg in opts:
            myobj.dbg_print(DBG, "OPTIONS->", opt, " : ", arg)
            if opt in ("-h", "--help"):
                print (myobj.showusage(filters))
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
                inputs.update({'login': arg})
            elif opt in ("-P", "--password"):
                inputs.update({'password': arg})
            elif opt in ("-s", "--secured"):
                if arg != "self" and arg != "CA":
                    print("defaults to CA")
                    arg = "CA"
                inputs.update({'secured': arg})
            elif opt in ("-v", "--verbose"):
                inputs.update({'verbose': 1})
            elif myobj.parse_attrib(opt, arg, filters):
                print("Invalid options specified ", opt)
                print(myobj.showusage(filters))
                return None

        if "ipaddr" not in inputs.keys():
            print("Missing IP address input")
            print(myobj.showusage(filters))
            return None
            # ipaddr = input("Please provide switch IP address:")
            # inputs.update({'ipaddr': ipaddr})

        ipaddr = inputs['ipaddr']
        if not pyfos_util.isIPAddr(ipaddr):
             print("*** Invalid ipaddr:", ipaddr)
             print(myobj.showusage(filters))
             return None

        if validate is not None  and validate(myobj) != 0:
            print("Please provide the missing util script option.")
            print(myobj.showusage(filters))
            return None

        if "login" not in inputs.keys():
            login = input("Login:")
            inputs.update({'login': login})

        if "password" not in inputs.keys():
            password = getpass.getpass()
            inputs.update({'password': password})

        if "secured" not in inputs.keys():
            inputs.update({'secured': None})
            
        return myobj
               

    def showfilter(self):
        filters = []
        for k1,v1 in self.clone_instance.items():
            v1.getfilter(filters)
        return filters


    def isfilterset(self):
        filters = self.showfilter()
        if (len(filters)) > 0:
            return 1
        return 0


    def getattribute(self, name):
        attrib = self.attributes_dict[name]
        return (attrib)

    
    def getparent(self, parents, ver, list_count=0):
        parentobj = None
        for i in range(len(parents)):
            if i == 0 :
                if parents[i] in self.attributes_dict.keys():
                    parentobj = self.attributes_dict[parents[i]]
                    if  0 == parentobj.version_supported.visible(ver):
                        self.dbg_print(ERR, parentobj.getname(),
                            ":Parent version not supported Version::",
                              parentobj.version_supported.to_string(),
                              ver.to_string())
                        return None
                else:
                    self.dbg_print(ERR, "Unknown Parent hierarchy", parents)
            elif parentobj != 0:
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
        return

    
    def update(self, attribute):
        myattrib = self.attributes_dict[attribute.getname()]
        myattrib.setvalue(attribute.getvalue)
        return

      
    def is_empty(self):
        count = len(self.attributes_dict)
        if count > 0 :
            return 0
        return 1

    
    def namekeys(self):
        return (self.attributes_dict.keys())


    def is_key_attrib(self, name):
        attrib = self.attributes_dict[name]
        return attrib.getiskey()

    
    def is_config_attrib(self, name):
        return self.attributes_dict[name].getisconfig()


    def is_value_changed(self, name):
        return self.attributes_dict[name].getisvaluechanged()

    
    def set_value_changed(self, name, changed = 0):
        return self.attributes_dict[name].setvaluechanged(changed)


    def getvalue(self, name):
        return self.attributes_dict[name].getvalue()


    def compare(self, retdict, reset_changed = 0):
        if len(retdict):
            if self.container in retdict.keys():
                retdict = retdict[self.container]
            
        for k1,v1 in self.attributes_dict.items():
            if k1 in retdict:
                if v1.compare(retdict[k1], reset_changed) == 0:
                    return 0
            else :
                return 0
            
        return 1


    def __repr__(self):
        return (json.dumps(self, cls=rest_attribute_encoder, sort_keys=True, indent=4))


    def modified(self):
        for k1,v1 in self.attributes_dict.items():
            if v1.modified(retdict[k1]) == 0:
                return 0
        return 1


    def is_valid(self, session):
        self.setdbg_session(session)
        if self.isvalidsession(session) == 0:
            return {"info-code": -1,
                    "info-message": "Invalid session",
                    "info-type": "Incorrect auth details in session"}
        if session['version'] is not None:
            if not self.version_supported.visible(session['version']):
                self.dbg_print(ERR, "Version not supported")
                self.dbg_print(ERR, "Session [",
                               session['version'].to_string(),
                               "] Supported version[",
                               self.version_supported.to_string(),"]")
                ret_error = {"info-code": -1,
                             "info-message": "Switch version is lower than the object",
                             "info-type": "Informational"}
                return ret_error
        ret_error = {"info-code": 0,
                     "info-message": "attributes details are present",
                     "info-type": "Informational"}
        return ret_error


    def create_html_content(self, optype = 0, session = None, add_container = 1):
        version = None
        if session is not None:
            version = session['version']
            self.setdbg_session(session)
        if version == None:
            version = self.version_active
        string_post=""
        for name in self.namekeys():
            attrib = self.attributes_dict[name]
            if attrib.is_key:
                if self.attributes_dict[name].supportedop(optype, version):
                    string_post += self.attributes_dict[name].create_html_content(optype, version)
        for name in self.namekeys():
            attrib = self.attributes_dict[name]
            if not attrib.is_key:
                if self.attributes_dict[name].supportedop(optype, version):
                    string_post += self.attributes_dict[name].create_html_content(optype, version)
        if add_container:
            string_post = re.sub("\n", "\n\t", string_post)
            string_post = "\n<" + self.container + ">" + string_post + "\n</" + self.container + ">"
        self.dbg_print(INF,"HTML CONTENT DATA:\n", string_post)
        return (string_post)

    
    def uri_string(self, optype = 0, session=None):
        version = None
        if session is not None:
            version = session['version']
            self.setdbg_session(session)
        if version == None:
            version = self.version_active
        string_uri="";
        for name in self.namekeys():
            if self.attributes_dict[name].supportedop(optype, version):
                string_uri += self.attributes_dict[name].uri_string(optype, version)
        self.dbg_print(INF, string_uri)
        return string_uri


    def dbg_print(self, level, *args):
        self.setdbg_log(level, args)

