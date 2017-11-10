# Copyright 2017 Brocade Communications Systems, Inc.  All rights reserved.
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

:mod:`pyfos_rest_util` - PyFOS module to provide rest support for FOS objects.
**********************************************************************************
The :mod:`pyfos_rest_util` provides a framework to add new FOS objects for REST support.

-Steps to add REST support for new FOS object
    * Add a new enum for your FOS object in the rest_obj_type class.
        :Example:

        ``class rest_obj_type():``
            ``unknown         = 0``
            ``**ipif**            = **11**``

            
    * Add the name of your FOS object type in the function getrestobjectname.
        :Example:

            ``elif objtype == rest_obj_type.ipif:``
                ``return "Extension IP ADDRESS"``
                
    * Inherit from class rest_object and init the base class.
    * Add attributes as per the yang definitions as per `Steps to add a Rest Attribute`.

        :Example:
    
            ``class extension_ipaddress(rest_object):``
                ``def __init__(self, session, dictvalues={}):``
                    ``rest_object.__init__(self, session, rest_obj_type.ipif, "/rest/running/brocade-interface/extension-ip-interface")``
                    ``self.add(rest_attribute("name", None, 1, 0))``
                    ``self.add(rest_attribute("ip-address", None, 1, 0))``
                    ``self.add(rest_attribute("dp-id", None, 1, 0))``
                    ``self.add(rest_attribute("ip-prefix-length", None, 0, 1))``
                    ``self.add(rest_attribute("mtu-size", None, 0, 1))``
                    ``self.add(rest_attribute("vlan-id", None, 0, 1))``
                    ``self.add(rest_attribute("status-flags", None, 0, 0))``
                    ``self.load(dictvalues)``
                    
-Steps to add REST attributes in a FOS object.
    * Leaf attribute with no parent.

        :Example:
        
            ``self.add(rest_attribute("name", None, 1, 0))``
        
    * Container or list attribute
        :Example:
        
            ``self.add(rest_attribute("l2-cos", dict(), 0, 1, **1**))``
            
    * leaf attribute with another container or list as its parent.

        :Example:
        
            ``self.add(rest_attribute("priority-control", None, 0, 1), **["l2-cos"]**)``
            ``self.add(rest_attribute("fc-priority-high", None, 0, 1), **["l2-cos"]**)``
            ``self.add(rest_attribute("fc-priority-medium", None, 0, 1), **["l2-cos"]**)``
            ``self.add(rest_attribute("fc-priority-low", None, 0, 1), **["l2-cos"]**)``
            ``self.add(rest_attribute("ip-priority-high", None, 0, 1), **["l2-cos"]**)``
            ``self.add(rest_attribute("ip-priority-medium", None, 0, 1),**["l2-cos"]**)``
            ``self.add(rest_attribute("ip-priority-low", None, 0, 1), **[l2-cos]**)``
        
-setters and getters for attributes
    Any attrbute added in the derived class of rest object has the option to get
    and set value for each attribute. For each attribute in the derived class a
    default setter and getter function is installed and can be invoked independently
    as and when needed.

    :note:
        1.  The getters and setters are prefixed with get_ or set_.
        2.  Then it contains all the parents string starting from the top level container till the immediate parent concatenated with an underscore \'_\'.
        3.  Then it contains the corresponding attrbute name.
        4.  All '-' are replaced with '_' and in lowercase for installing the function.
        
        
    * Leaf attribute with no parent:  
        :Example:
        
            ``self.add(rest_attribute("vlan-id", None, 0, 1))``
            
            * Default setter: **set_vlan_id**
            * Default getter: **get_vlan_id**
        
            :note:
                In test code following can be invoked by the user as below.
            
                ``myipobject = pyfos_extension_ipaddress.extension_ipaddress(session)``
                ``myipobject.set_vlan_id(800)``
                ``myipobject.get_vlan_id()``
            
    * Container or List attribute.
        :Example:
        
            ``self.add(rest_attribute("l2-cos", dict(), 0, 1, **1**))``
            
            * Default setter: **set_l2_cos**
            * Default getter: **get_l2cos**

             :note:
                The value for setter will be a list of dictionary values from its child attributes.
                 
                ``mytunnelobject = pyfos_extn_tunnel.extension_tunnel(session)``
                ``mytunnelobject.set_l2_cos([{ 'priority-control": 0, 'fc-priority-high" : 1 ........}])``
                ``mytunnelobject.get_l2_cos()``
        
    *  Leaf attribute with another container or list as its parent.
        :Example:

            ``self.add(rest_attribute("fc-priority-low", None, 0, 1), ``
            **["l2-cos"]**
            ``)``

            * Default setter: **set_l2_cos_fc_priority_low**
            * Default getter: **get_l2cos_fc_priority_low**

            :note:
            
                The value for setter will be a list of dictionary values from its child attributes.
            
                ``mytunnelobject = pyfos_extn_tunnel.extension_tunnel(session)``
                ``mytunnelobject.set_l2_cos_fc_priority_low(5)``
                ``mytunnelobject.get_l2_cos_fc_priority_low()``

-writting a test code.
        
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
from pyfos.pyfos_type import pyfos_type

class rest_obj_type():
    """This class identifies the different rest objects supported by FOS

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
    fos_end         = 200
    #use enums from 100 onwards
    
def getrestobjectname(objtype, fmt = 0):
    """This function provides the name for all instance of rest_object supported by FOS

    All derived class from rest_object should define their object name.
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
        elif objtype == rest_obj_type.tunnel_stats:
            return "Extension Circuit stats"
        elif objtype == rest_obj_type.ipsec:
            return "Extension IPSec"
        elif objtype == rest_obj_type.gige:
            return "Extension GigE"
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
        elif objtype == rest_obj_type.tunnel_stats:
            return "circuitstats"
        elif objtype == rest_obj_type.ipsec:
            return "IPSec"
        elif objtype == rest_obj_type.gige:
            return "GigE"
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
        
        else:
            return "Unknown"
        


class rest_get_method():
    """This class provides enum definition for different request methods for rest_handler class

    Based on these enum definitions the rest handler class creates appropriate URI and or POST data for request.
    """
    GET_ALL_KEY_CONFIG = 0
    GET_ALL_KEY = 1
    GET_ALL_CONFIG = 2
    GET_MODIFIED_CONFIG = 3
    GET_KEY_AND_MODIFIED_CONFIG = 4


global  REST_ATTRIBUTE_KEY
global  REST_ATTRIBUTE_CONFIG
global  REST_ATTRIBUTE_CONFIG_MANDATORY
global  REST_ATTRIBUTE_NOT_CONFIG
global  REST_ATTRIBUTE_CONTAINER
global  REST_ATTRIBUTE_LEAF_LIST
global  REST_ATTRIBUTE_CONTAINER_LIST
    
    
REST_ATTRIBUTE_KEY = dict ({'is_key':1, 'is_config': 0, 'is_mandatory': 0 , 'is_attribute_map':0, 'is_list':0, 'is_leaf':1})
REST_ATTRIBUTE_CONFIG = dict ({'is_key':0, 'is_config': 1, 'is_mandatory': 0, 'is_attribute_map':0, 'is_list':0, 'is_leaf':1})
REST_ATTRIBUTE_CONFIG_MANDATORY = dict ({'is_key':0, 'is_config': 1, 'is_mandatory': 1, 'is_attribute_map':0, 'is_list':0, 'is_leaf':1})
REST_ATTRIBUTE_NOT_CONFIG = dict ({'is_key':0, 'is_config': 0, 'is_mandatory': 0, 'is_attribute_map':0, 'is_list':0, 'is_leaf':1})
REST_ATTRIBUTE_CONTAINER = dict ({'is_key':0, 'is_config': 1, 'is_mandatory': 0, 'is_attribute_map':1, 'is_list':0, 'is_leaf':0})
REST_ATTRIBUTE_LEAF_LIST = dict ({'is_key':0, 'is_config': 1, 'is_mandatory': 0, 'is_attribute_map':0, 'is_list':1, 'is_leaf':1})
REST_ATTRIBUTE_CONTAINER_LIST = dict ({'is_key':0, 'is_config': 1, 'is_mandatory': 0, 'is_attribute_map':1, 'is_list':1, 'is_leaf':0})

class rest_attribute_encoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, 'reprJSON'):
            return obj.reprJSON()
        else:
            return json.JSONEncoder.default(self, obj)

class rest_attribute():
    """ This class encompasses a rest attribute and may be a leaf or be a container attribute as per yang
    
    Attributes:
        name: The `name` of the attribute as per the yang definition.
        is_config:  The `is_config` indicates if its a config attribute as per yang.
        isattributemap:  The `isattributemap` indicates if its a container attribute as per yang.
        is_key: The `is_key` confirms if its key attribute.
        parent: The `parent` is the parent container of object.
        value: The `value` of the attribute. The details of attribute value is as below.
                * Leaf Attribute **value** is the value of the object
                * Container Attribute **value** is the value of its children dictionary.
                * Leaf List Attribute **Value** is a list of values.
                * Container List Attribute **value** is a list of dictionary values of a child.
         

    """

 
    def __init__(self, name, a_type, value=dict(), properties = dict(), parent = 0, list_count = 0):
        """Instantiate a rest_attribute """
        self.name = name
        self.a_type = pyfos_type(a_type)
        self.is_key = properties['is_key']
        self.is_config = properties['is_config']
        self.is_mandatory = properties['is_mandatory']
        self.is_attribute_map = properties['is_attribute_map']
        self.is_list = properties['is_list']
        self.is_leaf = properties['is_leaf']
        self.properties = properties
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
                self.value = [ dict()]
        else:
            self.value = value
        self.parent_is_list = 0
        self.value_changed = 0
        self.attrib = dict()
        self.clone_name=None
        self.clone_dict = dict({ 'name':name, 'value': value, 'type': a_type, 'prop': properties})
        self.hierarchy = []
        self.restobject = None
        
    def setclonename(self):
        """ This is the cloning name and should be called after linking it with the Parent is complete """
        clonename = re.sub('-', '_', str(self.getallparentstring() + self.getname()))
        self.clone_name = clonename.lower()
        #print self.clone_name

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

    def reprJSON(self):
        """Get the JSON representation of the rest_attribute"""
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
                    else:
                        return self.value

                retarray = []
                if self.value is not None:
                    for v1 in self.value:
                        retdict = dict()
                        for k2, v2 in v1.items():
                            if v2.is_empty() == False:
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
            else:
                return self.value

    def getclonename(self):
        """Get the clone name of the rest_attribute"""
        return (self.clone_name)
     
    def getname(self):
        """Get the name of the rest_attribute """
        return self.name

    def setparent(self, parent, list_count = 0):
        """Set the parent of the rest_attribute """
        if  parent.getisattributelist() or parent.parent_is_list:
            self.parent = parent
            self.parent_is_list = 1          
        else:
            self.parent = parent
        return
    
    def compare(self, retdict, reset_modified = 0):
        """Compare the object to the passed dictionary values """
        if self.getisattributemap() and not self.getisattributelist():
            for k1,v1 in self.value.items():
                if isinstance(retdict, list):
                    myvalue = retdict[0]
                elif isinstance(retdict, dict):
                    myvalue = retdict;
                else:
                    #TODO remove the newline check after xmltodict merge
                    if len (retdict) and retdict != '\n':
                        print ("Illegal param passed for Key", self.clone_name, "Dict:", retdict, "\n")
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
                    print ("Mismatch values for Attribute ",self.getname(), "Value (", retdict, "/",  self.getvalue())
                    return 0

        if reset_modified:
            self.setvaluechanged(0)
        return 1

    def modified(self):
        """Check if any of the values in the object is modified """
        if self.getisattributemap():
            for k1,v1 in self.value.items():
                if v1.modified() == 1:
                    return 1
        elif self.getisattributelist():
            #Leaf list handling
            if self.is_list:
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

        
    def getchildattrib(self, name, list_count = 0):
        """Get the Child attribute for this Attribute. """     
        if self.getisattributemap() and not self.getisattributelist() and name in self.value.keys():
            return (self.value[name])
        elif self.getisattributelist():
            if list_count < len(self.value):
                value = self.value[list_count]
                if name in value.keys():
                    return value[name]
        return 0

    def addchild(self, attribute, list_count = 0):
        """Add a child attribute to anpther attribute which is a map """
        if self.getisattributemap()  and not self.getisattributelist():
            self.value.update(attribute.todict())
            attribute.setparent(self)
        elif self.getisattributelist():
            if self.is_leaf:
                print ("Cannot add child to leaf list")
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
            print ("Error not an attribute map or list ", self.name)
            return 0
        
        if self.restobject.initialized == 0:
            self.addhierarchy(attribute)

        return 1

    def addhierarchy(self, attribute):
        """Add a child attribute to anpther attribute which is a map """
        if self.getisattributelist() or self.getisattributemap():
            if self.is_leaf == 0:
                self.hierarchy.append(attribute.clone_dict)
        #print self.hierarchy

    def gethierarchy(self, attribute):
        """Returns the clone hierarchy of the attribute"""
        if self.getisattributelist() or self.getisattributemap():
            self.hierarchy            

    def getuservalue(self):
        """Get the value of the attribute this is External function """
        correct_type, value = self.a_type.validate_peek(self.getvalue())
        if correct_type:
            return value
        else:
            return "type of" + str(self.a_type.get_type()) + "missmatched to" + str(self.getvalue())
        
    def getvalue(self):
        """Get the value of the attribute this is internal function for the object """
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
        """Check if the attribute is top level i.e direct child attribute of the rest object"""
        if self.getallparentstring() == "":
            return True
        else:
            return False

    def getallparentstring(self):
        """Get all the parent string for generic setters and getters implementation """
        if self.parent:
            getparentstring = self.parent.getallparentstring()
            return getparentstring + self.parent.getname() + "_"
        return ""

    def getiskey(self):
        """Get the is_key value of this attribute"""
        return self.is_key

    def getisconfig(self):
        """Get the is_config value of this attribute"""
        return self.is_config

    def getisattributemap(self):
        """Get the isattributemap value of this attribute"""
        return self.is_attribute_map
    
    def getisattributelist(self):
        """Get the isattributemap value of this attribute"""
        return self.is_list

    def todict(self):
        """Convert the attribute in to a dictonary"""
        self.attrib={self.name: self}
        return self.attrib

    def fromdict(self, attribdict):
        """Assign the attrbiute value from a dict"""
        self.setvalue((attribdict[self.name]).getvalue())

    def getisvaluechanged(self):
        """Get if the value is changed for the object"""
        return (self.value_changed)

    def setvaluechanged(changed):
        """Set if the value is changed for the object"""
        self.value_changed = changed
        return
        
    def copy(self):
        """Copy Constructor for an Attribute"""
        return rest_attribute(self.name, self.value, self.is_key, self.is_config)

    def clone(self, list_count = 0):
        """Clone an Attribute"""
        if self.getisattributelist() or self.getisattributemap():
            hierarchy = self.restobject.gethierarchy(self.clone_name)
            # "Hierarchy ",hierarchy, self.clone_name, "\n"
            self.clone_hierarchy(hierarchy, self, list_count)
            
    def clone_hierarchy(self, hierarchy,  parent, list_count):
        """Clone the attribute hierarchy of the attribute"""
        if isinstance(hierarchy, list):
            for i in range(len(hierarchy)):
                clone_dict = hierarchy[i]
                attribute = rest_attribute(clone_dict['name'], clone_dict['type'], clone_dict['value'], clone_dict['prop'], parent,  list_count)
                attribute.restobject = self.restobject
                self.addchild(attribute, list_count)
                attribute.setclonename()
                # The list_count always starts from 0 becuase we are inside a container or list
                attribute.clone(0)
           
    def setuservalue(self, value, changed = 1):
        """Set the value of the attribute External function"""
        if self.supportedop(rest_get_method.GET_ALL_KEY_CONFIG):
            self.setvalue(value, changed)
        else:
            print  ("Unsupported: ", "set_" + myfunc, " function is not allowed for the attribute \"", attribute.getname(),"\".\n")
            return {"info-code": -1, "info-message": "Incorrect call", "info-type": "Unsupported operation on attribute"}

    def setvalue(self, value, changed=1):
        """Set the value of the attribute internal function"""
        
        if self.getisattributemap() and not self.getisattributelist():
            #print ("Container" , self.name , value)
            if value == None:
                self.value.clear()
            else:
                for k1, v1 in self.value.items():
                    #print (value)
                    myvalue = value
                    if isinstance(value, list):
                        myvalue = value[0]
                    #print (k1, myvalue,v1)
                    if k1 in myvalue.keys():
                        v1.setvalue(myvalue[k1], changed)
                        #print ("calling setvalue")
        elif self.getisattributelist():
            if isinstance(value, list) :
                if self.is_leaf:
                    #print ("Leaf List" , self.name , value)
                    for v1 in value:
                        self.value.append(v1)
                else :    
                    for i in range(len(value)):
                        if len(self.value) <= i :
                            self.clone(i)
                
                    for i in range(len(value)):
                        #print ("container List" , self.name , value)
                        myvalue = value[i]
                        objvalue = self.value[i]
                        for k1, v1 in objvalue.items():
                            if k1 in myvalue.keys():
                                v1.setvalue(myvalue[k1], changed)
            else:
                if self.is_leaf:
                    #print ("Leaf List with one entry only" , self.name , value)
                    self.value.append(value)
                else:
                    for i in range(len(self.value)):
                        objvalue = self.value[i]
                        for k1, v1 in objvalue.items():
                            if k1 in value.keys():
                                v1.setvalue(value[k1], changed)
                    
            
        else :
            self.value = value
        
        self.value_changed = changed
        return

    def objdisplay(self):
        """Display an Attribute"""
        mydisplay = []
        if self.getisattributemap() or (self.getisattributelist() and self.is_leaf == 0):
            #print self.value
            if self.getisattributelist():
                for i in range(len(self.value)):
                    tmpdict = self.value[i]
                    list1 = []
                    for k1, v1 in tmpdict.items():
                        list1.append(tmpdict[k1].objdisplay())
                    mydisplay.append(list1)                 
            else:
                for k1, v1 in self.value.items():
                    mydisplay.append(self.value[k1].objdisplay())

     
            mydict={"name": self.name, "pointer" :self,"value" :mydisplay,  "iskey": self.is_key, "isconfig" : self.is_config}
        else :
            mydict={"name": self.name, "pointer" :self,"value" :self.value,  "iskey": self.is_key, "isconfig" : self.is_config}
            
        #print mydict
        return mydict

    def display(self):
        """Display an Attribute"""
        mydisplay = []
        if self.getisattributemap() or (self.getisattributelist() and self.is_leaf == 0):
            #print self.value
            if self.getisattributelist() :
                for i in range(len(self.value)):
                    tmpdict = self.value[i]
                    list1 = []
                    for k1, v1 in tmpdict.items():
                        list1.append(tmpdict[k1].display())
                    mydisplay.append(list1)
            else:               
                for k1, v1 in self.value.items():
                    mydisplay.append(self.value[k1].display())

            #mydict={"name": self.name,"value" :mydisplay}
            mydict={self.name: mydisplay}
                    
        else :
            #mydict={"name": self.name, "value" :self.value}
            mydict={self.name:self.value}
            
        #print mydict
        return mydict

    def supportedop (self, op):
        """Check if the attribute is supported for the GET methods requested"""
        if self.is_leaf:
            if op == rest_get_method.GET_ALL_KEY_CONFIG:
                if self.getisconfig() or self.getiskey() or self.is_mandatory:
                    return 1
            if op == rest_get_method.GET_ALL_KEY or self.is_mandatory :
                if self.getiskey():
                    return 1
            if op == rest_get_method.GET_KEY_AND_MODIFIED_CONFIG:
                if self.getisconfig() and self.getisvaluechanged() or self.getiskey() or self.is_mandatory:
                    return 1
            if op == rest_get_method.GET_ALL_CONFIG or self.is_mandatory :
                    if self.getisconfig() and not self.getiskey():
                        return 1
            if op == rest_get_method.GET_MODIFIED_CONFIG:
                    if self.getisconfig() and self.getisvaluechanged() or self.is_mandatory:
                        return 1
        elif self.getisattributelist():
            for i in range(len(self.value)):
                for k1,v1 in self.value[i].items():
                    if v1.supportedop(op) == 1:
                        return 1
        elif self.getisattributemap():
            for k1,v1 in self.value.items():
                if v1.supportedop(op) == 1:
                    return 1
                
        return 0

    def create_html_content(self, optype):
        """Create the post string data equivalent for an Attribute"""
        poststring = ""
        if self.getisattributemap() and not self.getisattributelist() and self.supportedop(optype):
            poststringchild = ""
            for k1, v1 in self.value.items():
                poststringchild += v1.create_html_content(optype)
            if (len(poststringchild)):
                poststringchild = re.sub("\n", "\n\t", poststringchild)
                poststring = "\n<" + self.name + ">" + poststringchild + "\n</" + self.name + ">"
            else:
                return (poststringchild)
            
            return poststring
        elif self.getisattributelist() and self.supportedop(optype):
            if None != self.value:
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
                                poststringchild += v1.create_html_content(optype)
                                
                            if (len(poststringchild)):
                                poststringchild = re.sub("\n", "\n\t", poststringchild)
                                poststring += "\n<" + self.name + ">" + poststringchild + "\n</" + self.name + ">"
                            
                    return poststring
        else:
            if self.value != None and self.supportedop(optype):
                return ("\n<" + self.name + ">" + str(self.value) + "</" + self.name + ">");
        return ""
        
    def uri_string(self, optype):
        """Create the uri string data equivalent for an Attribute"""
        if (self.getisattributemap() or self.getisattributelist()) and self.is_leaf == 0:
            uristring = "/" + self.name 
            for k1, v1 in self.value.items():
                if v1.supportedop(optype):
                    uristring += v1.uri_string()
            return uristring
        else:
            if None != self.getvalue() :
                return ("/" + self.name + "/" + urllib.parse.quote(str(self.getvalue()), safe=''));
        return ""


class rest_handler():
    """ This class encompasses all the REST operations supported from the FOS Objects as per yang
    
    Attributes:
        session: The login `session` to a FOS switch.
        uri_base:  The `uri_base` is the base URI string to access the corresponding object.
        obj:  The `obj` is the corresponding rest object instance for rest_handler to work on.
        test: The `test` dictionary is to capture all the different test executions.

    """
    global test
    test = dict()
    test.update({1 : {"total_tc": 0,"show_all": 0, "get" : 0, "get_uri": 0, "post": 0, "patch": 0, "create_uri":0, "delete" :0, "delete_uri":0, "modify_put" :0, "modify_put_uri" :0, "modify_patch": 0, "modify_patch_uri" :0}})
    

    def __init__(self, uri_base):
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
        #test[request] = count
        mytestcase="Test to " + request + " an " + getrestobjectname(self.obj.obj_type) + " Object"
        testcaseID = "TC_" + str(counttotal) +"_[" + request + "_" + str(countg) + "_[" + getrestobjectname(self.obj.obj_type, 1) + "[ID" + str(self.obj.obj_type) +"]_" + str(counto) +"]]"
        pyfos_util.test_title_set(testcaseID.upper(), mytestcase.upper())
        pyfos_util.test_negative_test_set(negative)
        time.sleep(2)

    def isvalidsession(self, session):
        #print self.session
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
        if is_tc :
            self.createtest("show_all", negative)
        return pyfos_util.get_request(session, self.uri_base, "")

    def get(self, session, negative = 0, is_tc=0):
        ret = self.obj.is_valid(session)
        if ( ret["info-code"] != 0 ) :
            return ret;
        if is_tc: 
            self.createtest( "get", negative)
        ret =  pyfos_util.get_request(session, self.uri_base, self.obj.create_html_content(rest_get_method.GET_ALL_KEY))
        return (ret)
    

    def get_uri(self, session, negative = 0, is_tc = 0):
        ret = self.obj.is_valid(session)
        if ( ret["info-code"] != 0 ) :
            return ret;
        if is_tc:
            self.createtest("get_uri", negative)
        return pyfos_util.get_request(session, self.uri_base + self.obj.uri_string(rest_get_method.GET_ALL_KEY), "")
   
    def post(self, session, negative = 0, is_tc = 0):
        ret = self.obj.is_valid(session)
        if ( ret["info-code"] != 0 ) :
            return ret;
        if is_tc:
            self.createtest("post", negative)
        ret = pyfos_util.post_request(session, self.uri_base, self.obj.create_html_content())
        return ret

    def delete(self, session, negative = 0, is_tc = 0):
        ret = self.obj.is_valid(session)
        if ( ret["info-code"] != 0 ) :
            return ret
        if is_tc :
            self.createtest("delete", negative)
        ret = pyfos_util.delete_request(session, self.uri_base, self.obj.create_html_content())
        return ret

    def delete_uri(self, session, negative =0, is_tc =0):
        ret = self.obj.is_valid(session)
        if ( ret["info-code"] != 0 ) :
            return ret
        if is_tc:
            self.createtest("delete_uri", negative)
        return pyfos_util.delete_request(session, self.uri_base + self.obj.uri_string(rest_get_method.GET_ALL_KEY),  "")

    def patch(self, session, negative = 0, is_tc = 0, modified_dict = {}):
        ret = self.obj.is_valid(session)
        if ( ret["info-code"] != 0 ) :
            return ret
        self.load(modified_dict, 1)
        if is_tc:
            self.createtest("patch", negative)
        ret = pyfos_util.patch_request(session, self.uri_base, self.obj.create_html_content(rest_get_method.GET_KEY_AND_MODIFIED_CONFIG))
        return ret

    def patch_uri(self, session,  negative =0, is_tc = 0, modified_dict = {}):
        ret = self.obj.is_valid(session)
        if ( ret["info-code"] != 0 ) :
            return ret
        self.load(modified_dict, 1)
        if is_tc:
            self.createtest("patch_uri", negative)
        ret = pyfos_util.patch_request(session, self.uri_base + self.obj.uri_string(rest_get_method.GET_ALL_KEY), self.obj.create_html_content(rest_get_method.GET_MODIFIED_CONFIG))
        return self.validate(negative, ret)
    
class rest_object_encoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, 'reprJSON'):
            return obj.reprJSON()
        else:
            return json.JSONEncoder.default(self, obj)
    
class rest_object(rest_handler):
    """ This class encompasses a REST supported FOS object as per yang
    
    Attributes:
        obj_type: The `obj_type` corresponding to a FOS object.
        uri_base:  The `uri_base` is the base URI string to access the corresponding object.
        obj:  The `obj` is the corresponding rest object instance for rest_handler to work on.
        test: The `test` dictionary is to capture all the different test executions.

    """
    def __init__(self, obj_type, uri):
        """ This is the constructor of the class"""
        self.obj_type = obj_type
        self.attributes_dict = dict()
        self.attributes = []
        self.clone_instance = dict()
        uriarray = uri.split("/")
        i = len(uriarray)
        self.container = uriarray[i-1]
        self.initialized = 0
        rest_handler.__init__(self, uri)

    def load(self, dictvalues, changed = 0):
        """The function is to load or deserialze from a dictionary of values into the object itself"""
        self.initialized = 1
        if dictvalues != None and len(dictvalues):
            if self.container in dictvalues.keys():
                retdict = dictvalues[self.container]
            else:
                retdict = dictvalues
            for k1, v1 in retdict.items():
                self.attributes_dict[k1].setvalue(v1, changed)

    def display(self):
        """The function is to serialize the object to a dictionary"""
        mydict =  dict()
        for i in range(len(self.attributes)):
            mydict.update(self.attributes[i].display())
        retdict = { self.container : mydict}
        return retdict
        
    def objdisplay(self):
        """The function is to serialize the object to a dictionary with object pointer details"""
        mydict =  dict()
        for i in range(len(self.attributes)):
            mydict.update(self.attributes[i].objdisplay())
        return mydict
            
    def add(self, attribute, parents=[]):
        """The function is to add the attribute to the rest object"""
        attribute.restobject = self;

        #This is only required that direct level attributes are added to the attributes_dict
        if len(parents) == 0:
            self.attributes_dict.update(attribute.todict())
            self.attributes.append(attribute);
        else:
            parent = self.getparent(parents)
            if parent != 0:
                parent.addchild(attribute)
            else:
                print ("Error No parent found matching hierarchy")
                return 0

        #Set the clonename of the attribute
        attribute.setclonename()
        myfunc = attribute.getclonename()
        #Install the generic Setters and getters of the function
        setattr(self, "set_" + myfunc.lower(), attribute.setuservalue)
        setattr(self, "peek_" + myfunc.lower(), attribute.getuservalue)
        self.addclone(attribute.clone_name, attribute)

    def addclone(self, name, attribute):
        """Add the clone instance Update"""
        self.clone_instance.update({name: attribute})
        #print  "clone instance", name, self.clone_instance, "\n"
        

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

    def reprJSON(self):
        """Represent the rest object in the JSON format"""
        retdict = dict()
        retdict[self.container] = dict()
        for k1, v1 in self.attributes_dict.items():
            if v1.is_empty() == False:
                retdict[self.container][k1] = v1
        return retdict

    def getcontainer(self):
        """Get the rest container object name"""
        return self.container
        
    def gethierarchy(self, clonename):
        """Get the clone hierarchy given a clone name"""
        if clonename in self.clone_instance.keys():
            attribute = self.clone_instance[clonename]
            if attribute.getisattributelist() or attribute.getisattributemap():
                return attribute.hierarchy  
    
    def getattribute(self, name):
        attrib = self.attributes_dict[name]
        return (attrib)

    def getparent(self, parents, list_count=0):
        parentobj = 0
        for i in range(len(parents)):
            if i == 0 :
                parentobj = self.attributes_dict[parents[i]]
            elif parentobj != 0:
                child = parentobj.getchildattrib(parents[i])
                parentobj = child
            else:
                print ("No parent found in the hierarchy", parents)
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

    def modified(self):
        for k1,v1 in self.attributes_dict.items():
            if v1.modified(retdict[k1]) == 0:
                return 0
        return 1

    def is_valid(self, session):
        if self.isvalidsession(session) == 0:
            return {"info-code": -1, "info-message": "Invalid session", "info-type": "Incorrect auth details in session"}
        
        if self.is_empty():
            ret_error = {"info-code": -1, "info-message": "attributes details are not present", "info-type": "Informational"}
            return ret_error;
        
        ret_error = {"info-code": 0, "info-message": "attributes details are present", "info-type": "Informational"};
        return ret_error;

    def create_html_content(self, optype = 0, add_container = 1):
        string_post=""
        for name in self.namekeys():
            attrib = self.attributes_dict[name]
            if self.attributes_dict[name].supportedop(optype):
                string_post += self.attributes_dict[name].create_html_content(optype)
        if add_container:
            string_post = re.sub("\n", "\n\t", string_post)
            string_post = "\n<" + self.container + ">" + string_post + "\n</" + self.container + ">"
        #print ("HTML CONTENT DATA:\n", string_post)
        return (string_post)
    
    def uri_string(self, optype = 0):
        string_uri="";
        for name in self.namekeys():
            if self.attributes_dict[name].supportedop(optype):
                string_uri += self.attributes_dict[name].uri_string(optype)
        #print  string_uri
        return string_uri
    
def get_all(session, object_type):
    obj = object_type()
    obj_list = obj.show_all(session)
    #pyfos_util.response_print(obj_list)
    if pyfos_util.is_failed_resp(obj_list):
        return obj_list      
    elif obj_list[obj.getcontainer()] is None:
        retobj = object_type()
        return retobj
    elif isinstance(obj_list[obj.getcontainer()], dict):
        retobj = object_type()
        if obj_list[obj.getcontainer()] is not None:
            #pyfos_util.response_print(obj_list[obj.getcontainer()])
            retobj.load(obj_list[obj.getcontainer()])
        return retobj
    else:
        retobj_list = []
        for one_instance in obj_list[obj.getcontainer()]:
            retobj = object_type()
            #pyfos_util.response_print(one_instance)
            retobj.load(one_instance)
            retobj_list.append(retobj)
        return retobj_list
