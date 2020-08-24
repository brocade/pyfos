#!/usr/bin/env python3

# Copyright 2018-2019 Brocade Communications Systems LLC.  All rights reserved.
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

:mod:`pyfos_class_manager` - PyFOS module to Manage all pyfos classes.
**********************************************************************************
The :mod:`pyfos_class_manager`  Provides the management functionality
for all REST supported classes.

"""


import sys
import time
import logging
from pyfos.pyfos_brocade_fdmi import hba
from pyfos.pyfos_brocade_name_server import fibrechannel_name_server
from pyfos.pyfos_brocade_fibrechannel_diagnostics import \
     fibrechannel_diagnostics
from pyfos.pyfos_brocade_interface import fibrechannel
from pyfos.pyfos_brocade_zone import defined_configuration
from pyfos.pyfos_brocade_zone import effective_configuration
from pyfos.pyfos_brocade_extension_tunnel import extension_circuit
from pyfos.pyfos_brocade_extension_tunnel import extension_circuit_statistics
from pyfos.pyfos_brocade_extension_tunnel import extension_tunnel
from pyfos.pyfos_brocade_extension_tunnel import extension_tunnel_statistics
from pyfos.pyfos_brocade_extension_ip_route import extension_ip_route
from pyfos.pyfos_brocade_interface import extension_ip_interface
from pyfos.pyfos_brocade_extension_ipsec_policy import extension_ipsec_policy
from pyfos.pyfos_brocade_interface import gigabitethernet
from pyfos.pyfos_brocade_interface import \
    gigabitethernet_statistics
from pyfos.pyfos_brocade_interface import logical_e_port
from pyfos.pyfos_brocade_fibrechannel_logical_switch import \
    fibrechannel_logical_switch
from pyfos.pyfos_brocade_fibrechannel_switch import \
    fibrechannel_switch
from pyfos.pyfos_brocade_access_gateway import port_group
from pyfos.pyfos_brocade_access_gateway import f_port_list
from pyfos.pyfos_brocade_access_gateway import policy
from pyfos.pyfos_brocade_access_gateway import n_port_settings
from pyfos.pyfos_brocade_access_gateway import n_port_map
from pyfos.pyfos_brocade_fabric import access_gateway
from pyfos.pyfos_brocade_fibrechannel_configuration import\
     switch_configuration
from pyfos.pyfos_brocade_fibrechannel_configuration import\
     f_port_login_settings
from pyfos.pyfos_brocade_logging import raslog
from pyfos.pyfos_brocade_logging import raslog_module
from pyfos.pyfos_brocade_logging import log_quiet_control
from pyfos.pyfos_brocade_logging import log_setting
from pyfos.pyfos_brocade_fru import fan
from pyfos.pyfos_brocade_fru import blade
from pyfos.pyfos_brocade_fru import power_supply
from pyfos.pyfos_brocade_chassis import chassis
from pyfos.pyfos_brocade_chassis import ha_status
from pyfos.pyfos_brocade_time import clock_server
from pyfos.pyfos_brocade_time import time_zone
from pyfos.pyfos_brocade_security import radius_server
from pyfos.pyfos_brocade_security import tacacs_server
from pyfos.pyfos_brocade_security import ldap_server
from pyfos.pyfos_brocade_security import auth_spec
from pyfos.pyfos_brocade_security import ipfilter_policy
from pyfos.pyfos_brocade_security import ipfilter_rule
from pyfos.pyfos_brocade_security import sec_crypto_cfg
from pyfos.pyfos_brocade_security import sec_crypto_cfg_template
from pyfos.pyfos_brocade_security import sec_crypto_cfg_template_action
from pyfos.pyfos_brocade_security import ldap_role_map
from pyfos.pyfos_brocade_security import password_cfg
from pyfos.pyfos_brocade_security import user_config
from pyfos.pyfos_brocade_security import user_specific_password_cfg
from pyfos.pyfos_brocade_security import sshutil
from pyfos.pyfos_brocade_security import sshutil_key
from pyfos.pyfos_brocade_security import sshutil_public_key
from pyfos.pyfos_brocade_security import sshutil_public_key_action
from pyfos.pyfos_brocade_security import password
from pyfos.pyfos_brocade_security import security_certificate
from pyfos.pyfos_brocade_security import security_certificate_generate
from pyfos.pyfos_brocade_security import security_certificate_action
from pyfos.pyfos_brocade_fru import sensor
from pyfos.pyfos_brocade_fru import wwn
from pyfos.pyfos_brocade_fru import history_log
import pyfos.pyfos_util as utils
import pyfos.pyfos_auth as auth


class clsmanager():
    """
    class for management of all the rest supported classes.
    """
    # pylint: disable=W0602
    global clslist
    global ordering
    global optionsdict
    global sessionmgr
    global mystageoperation
    global pridict
    global restslotattributedict
    # pylint: disable=W0601
    global slotlist
    global mylogger
    global mylogapp
    global clslogger
    global uselogger

    clslist = [hba,
               fibrechannel_name_server,
               fibrechannel_diagnostics,
               fibrechannel,
               defined_configuration,
               effective_configuration,
               extension_circuit,
               extension_circuit_statistics,
               extension_tunnel,
               extension_tunnel_statistics,
               extension_ip_route,
               extension_ip_interface,
               extension_ipsec_policy,
               gigabitethernet,
               fibrechannel_logical_switch,
               fibrechannel_switch,
               port_group,
               f_port_list,
               policy,
               n_port_settings,
               n_port_map,
               gigabitethernet_statistics,
               switch_configuration,
               f_port_login_settings,
               raslog,
               raslog_module,
               log_quiet_control,
               log_setting,
               fan,
               blade,
               power_supply,
               clock_server,
               time_zone,
               tacacs_server,
               ldap_server,
               auth_spec,
               ipfilter_policy,
               ipfilter_rule,
               sec_crypto_cfg,
               sec_crypto_cfg_template,
               sec_crypto_cfg_template_action,
               ldap_role_map,
               password_cfg,
               user_specific_password_cfg,
               user_config,
               sshutil,
               sshutil_key,
               sshutil_public_key,
               sshutil_public_key_action,
               password,
               security_certificate,
               security_certificate_generate,
               security_certificate_action,
               radius_server,
               chassis,
               ha_status,
               sensor,
               wwn,
               history_log,
               logical_e_port]
    ordering = dict()
    sessionmgr = dict()
    mystageoperation = dict()
    pridict = dict()
    restslotattributedict = dict()
    slotlist = list()
    optionsdict = dict()
    mylogger = 0
    mylogapp = dict()
    clslogger = None
    uselogger = 0

    @classmethod
    def clsglobalinit(cls, logenable=0):
        """
        Init the globals for class Manager
        """
        global uselogger
        cls.initSlotObjectDict()
        cls.initpridict()
        cls.initConfigstages()
        cls.initoptionsdict()
        cls.log(1, "Global Class Init")
        if logenable != 0:
            uselogger = 1

    @classmethod
    def clsorderinginit(cls, slots):
        """
        Init the class ordering for class Manager
        """
        # pylint: disable=W0601
        global slotlist
        if isinstance(slots, list):
            slotlist = slots
        else:
            print("Error expecting a list of slots as input")
            cls.log(3, "Error expecting a list of slots as input")
        cls.initordering()
        cls.log(1, "Class ordering Init")

    @classmethod
    def initConfigstages(cls):
        """
        Init the class config stages for class Manager
        """
        mystageoperation.update(dict({'DELETE': str("DELETE")}))
        mystageoperation.update(dict({'POST': str("POST")}))
        mystageoperation.update(dict({'PRE_DELETE': str("PATCH")}))
        mystageoperation.update(dict({'PRE_PATCH': str("PATCH")}))
        mystageoperation.update(dict({'POST_PATCH': str("PATCH")}))
        mystageoperation.update(dict({'PUT': str("PUT")}))
        mystageoperation.update(dict({'GET': str("GET")}))
        cls.log(1, "Config stages Init")

    @classmethod
    def initlogger(cls, app):
        """
        Init the logger infra for class Manager
        """
        global mylogapp
        global mylogger
        if uselogger == 0:
            return None
        # pylint: disable=E0601
        if mylogger == 0:
            name = "Log_" + time.strftime("%Y%m%d_%H_%M_%S")
            logging.basicConfig(level=logging.DEBUG,
                                format='%(name)-12s:%(asctime)s ' +
                                '%(levelname)-8s %(message)s',
                                datefmt='%a, %d %b %Y %H:%M:%S',
                                filename=name,
                                filemode='w')
            mylogger = 1
        if app not in mylogapp:
            logger = logging.getLogger(app)
            mylogapp[app] = logger
        return mylogapp[app]

    @classmethod
    def logbase(cls, loggerObj, lvl, messages):
        """
        add the log messages
        """
        if uselogger == 0 or loggerObj is None:
            return
        if lvl == 1:
            loggerObj.debug(messages)
        if lvl == 2:
            loggerObj.info(messages)
        if lvl == 3:
            loggerObj.warning(messages)
        if lvl == 4:
            loggerObj.error(messages)

    @classmethod
    def log(cls, lvl, *msg):
        """
        add the log messages
        """
        global clslogger
        # pylint: disable=E0601
        if clslogger is None:
            clslogger = cls.initlogger("ClassManager")
        if clslogger is None:
            return
        cls.logbase(clslogger, lvl, "".join(map(str, msg)))

    @classmethod
    def updateordering(cls, instcls, stage, slot, supported, pri, CB=None):
        """
        Set/update the ordering/config stage per pyfos class.
        """
        clsdict = dict()
        stagedict = dict()
        slotdict = dict()
        if instcls in ordering.keys():
            clsdict = ordering[instcls]
            if stage in clsdict.keys():
                stagedict = clsdict[stage]
                if slot in stagedict.keys():
                    slotdict = stagedict[slot]
                    slotdict['supported'] = supported
                    slotdict['pri'] = pri
                    slotdict['CB'] = CB
                else:
                    slotdict.update(dict({slot: dict({'supported': supported,
                                                      'pri': pri,
                                                      'CB': CB})}))
                stagedict.update(slotdict)
            else:
                stagedict.update(dict({stage: dict({slot:
                                                    dict({'supported':
                                                          supported,
                                                          'pri': pri,
                                                          'CB': CB})})}))
            clsdict.update(stagedict)
        else:
            clsdict.update(dict({instcls:
                                 dict({stage:
                                       dict({slot:
                                             dict({'supported': supported,
                                                   'pri': pri,
                                                   'CB': CB})})})}))
        ordering.update(clsdict)

    @classmethod
    def getordering(cls, instcls, stage, slot):
        """
        Get the ordering config stage per pyfos class.
        """
        clsdict = dict()
        stagedict = dict()
        slotdict = dict()
        if instcls in ordering.keys():
            clsdict = ordering[instcls]
            if stage in clsdict.keys():
                stagedict = clsdict[stage]
                if slot in stagedict.keys():
                    slotdict = stagedict[slot]
                    return slotdict
        return None

    @classmethod
    def setClsStageSupported(cls, instcls, stage, slot, supported=True):
        """
        Set the ordering config stage supported per pyfos class.
        """
        if cls.getordering(instcls, stage, slot) is not None:
            ordering[instcls][stage][slot]['supported'] = supported

    @classmethod
    def resetClsStageSupported(cls, instcls, stage, slot, supported=False):
        """
        Reset the ordering config stage supported per pyfos class.
        """
        if cls.getordering(instcls, stage, slot) is not None:
            ordering[instcls][stage][slot]['supported'] = supported

    @classmethod
    def setClsStagePri(cls, instcls, stage, slot, pri):
        """
        Set the ordering config stage priority per pyfos class.
        """
        if cls.getordering(instcls, stage, slot) is not None:
            ordering[instcls][stage][slot]['pri'] = pri
            cls.setpriPridict(instcls, stage, pri)

    @classmethod
    def setClsStageCB(cls, instcls, stage, slot, CB):
        """
        Set the ordering config stage CallBack handler per pyfos class.
        """
        if cls.getordering(instcls, stage, slot) is not None:
            ordering[instcls][stage][slot]['CB'] = CB

    @classmethod
    def getClsStageCB(cls, instcls, stage, slot):
        """
        Get the ordering config stage CallBack handler per pyfos class.
        """
        if cls.getordering(instcls, stage, slot) is not None:
            return ordering[instcls][stage][slot]['CB']
        return None

    @classmethod
    def getClsStagePri(cls, instcls, stage, slot):
        """
        Get the ordering config stage priority per pyfos class.
        """
        if cls.getordering(instcls, stage, slot) is not None:
            return ordering[instcls][stage][slot]['pri']
        return 0

    @classmethod
    def getClsStageSupported(cls, instcls, stage, slot):
        """
        Get the ordering config stage Stage supported per pyfos class.
        """
        if cls.getordering(instcls, stage, slot) is not None:
            return ordering[instcls][stage][slot]['supported']
        return False

    @classmethod
    def initoptionsdict(cls):
        """
        Init the optionsdict per pyfos class.
        """
        for i in range(len(clslist)):
            optionsdict.update(dict({clslist[i]: dict({'OPTIONS': dict()})}))

    @classmethod
    def initordering(cls):
        """
        Init the ordering per pyfos class.
        """
        for i in range(len(clslist)):
            stages = cls.getConfigStages()
            for j in range(len(stages)):
                for k in range(len(slotlist)):
                    cls.initorderingclsslot(clslist[i], stages[j], slotlist[k])
        # print(ordering)
        cls.log(1, ordering)

    @classmethod
    def initorderingclsslot(cls, instcls, stage, slot):
        """
        Init the ordering per slot per pyfos class.
        """
        supported = True
        pri = cls.getpriPridict(instcls, stage)
        # pylint: disable=W0105
        """
        if instcls != effective_configuration:
            if stage in ("POST_PATCH", "PRE_DELETE"):
                if instcls == fibrechannel_switch:
                    if stage != "PRE_DELETE":
                        supported = False
                elif instcls  != port_group:
                    supported = False
        """
        cls.updateordering(instcls, stage, slot, supported, pri)

    @classmethod
    def initpridict(cls):
        """
        Init the pridict per config stage per pyfos class.
        """
        for i in range(len(clslist)):
            instcls = clslist[i]
            prilist = cls.pristage(instcls)
            configlist = cls.getConfigStages()
            tmpdict = dict()
            for j in range(len(configlist)):
                tmpdict.update(dict({configlist[j]: prilist[j]}))
            pridict.update(dict({instcls: tmpdict}))

    @classmethod
    def getpriPridict(cls, instcls, stage):
        """
        Get the pridict per stage per pyfos class.
        """
        if not any(pridict):
            cls.initpridict()
        try:
            pri = pridict[instcls][stage]
        except AttributeError as err:
            print("Err", err)
            return 0
        return pri

    @classmethod
    def setpriPridict(cls, instcls, stage, pri):
        """
        Set the pridict per stage per pyfos class.
        """
        if not any(pridict):
            cls.initpridict()
        try:
            pridict[instcls][stage] = pri
        except AttributeError as err:
            print("Err", err)
            return 0
        return pridict[instcls][stage]

    @classmethod
    def printordering(cls):
        """
        Display the ordering for all pyfos class.
        """
        print(ordering)

    @classmethod
    def getclsfromcontainer(cls, container):
        """
        Get the class from container name for all pyfos class.
        """
        for i in range(len(clslist)):
            if container == clslist[i]().getcontainer():
                return clslist[i]
        return None

    @classmethod
    def getContainerfromCls(cls, clsname):
        """
        Get the container from class name for all pyfos class.
        """
        for i in range(len(clslist)):
            if clsname == clslist[i]:
                return clslist[i]().getcontainer()
        return None

    @classmethod
    def getclskey(cls, tmpcls, op, slot):
        """
        Get the class key for all pyfos class.
        """
        return cls.getClsStagePri(tmpcls, op, slot)

    @classmethod
    def getInstacefromcls(cls, clsname, valuedict=None):
        """
        Get the Instance of class based on clsname for all pyfos class.
        """
        for i in range(len(clslist)):
            if clsname == clslist[i]:
                return clslist[i](valuedict)
        return None

    @classmethod
    def getInstacefromContainer(cls, container, valuedict=None):
        """
        Get the Instance of class based on container name
        for all pyfos class.
        """
        # print(container)
        for i in range(len(clslist)):
            if container == clslist[i]().getcontainer():
                tmp = clslist[i](valuedict)
                # print("cls :",clslist[i]().getcontainer(), tmp)
                return tmp
        return None

    # print(clsmanager.mapInstacefunction('displaycustomcli'))
    @classmethod
    def mapInstacefunction(cls, fname):
        """
        Map the Object function for all pyfos class.
        """
        newlist = list(clslist)
        # pylint: disable=W0123
        return list(map(lambda x: eval("x()." + fname+"()"), newlist))

    # print(clsmanager.mapInstacefunction('cliusage'))
    @classmethod
    def mapClsfunction(cls, fname):
        """
        Map the classmethod function for all pyfos class.
        """
        newlist = list(clslist)
        # pylint: disable=W0123
        return list(map(lambda x: eval("x." + fname+"()"), newlist))

    @classmethod
    def getAllCls(cls):
        """
        Get all the class list
        """
        newlist = list(clslist)
        return newlist

    @classmethod
    def getConfigStages(cls):
        """
        Get all the config stages for all classes.
        """
        newlist = list(["PRE_DELETE", "DELETE", "PRE_PATCH", "POST",
                        "POST_PATCH"])
        return newlist

    @classmethod
    def getConfigOperation(cls, stage):
        """
        Get the HTTP operation for a given config stage.
        """
        if stage in mystageoperation.keys():
            return mystageoperation[stage]
        print("Unknown option stage passed for operations:", stage)
        cls.log(2, "Unknown option stage passed for operations:",
                stage)
        return []

    @classmethod
    def getAllOperation(cls):
        """
        Get all the HTTP operation per config stages for a class.
        """
        # pylint: disable=W0108
        return list(map(lambda x: cls.getConfigOperation(x),
                        cls.getConfigStages()))

    @classmethod
    def getsortedlist(cls, op, slot):
        """
        Get a sorted list based on the priority per config stage
        per slot for all class.
        """
        sortedlist = sorted(cls.getAllCls(),
                            key=lambda x: clsmanager.getclskey(x, op, slot))
        return sortedlist

    @classmethod
    def setclsoptions(cls, tmpcls, session):
        """
        Set the OPTIONS for a pyfos class.
        """
        if len(optionsdict[tmpcls]['OPTIONS']) == 0:
            ret = tmpcls().options(session)
            if not utils.is_failed_resp(ret):
                optionsdict[tmpcls]['OPTIONS'] = ret

    @classmethod
    def setoptions(cls, session):
        """
        Set the OPTIONS for all pyfos class.
        """
        newlist = list(clslist)
        list(map(lambda x: cls.setclsoptions(x, session), newlist))

    @classmethod
    def getclsoptions(cls, tmpcls, session=None):
        """
        Set the OPTIONS for all pyfos class.
        """
        if session is not None:
            cls.setclsoptions(tmpcls, session)
        return optionsdict[tmpcls]['OPTIONS']

    @classmethod
    def isConfigClass(cls, tmpcls, session=None):
        """
        Check if a class is supported for config operation.
        """
        if session is not None:
            cls.getclsoptions(tmpcls, session)
        if 'POST' in optionsdict[tmpcls]['OPTIONS']:
            return True
        elif 'PUT' in optionsdict[tmpcls]['OPTIONS']:
            return True
        elif 'PATCH' in optionsdict[tmpcls]['OPTIONS']:
            return True
        elif 'DELETE' in optionsdict[tmpcls]['OPTIONS']:
            return True
        return False

    @classmethod
    def ispostSupportedClass(cls, tmpcls, session=None):
        """
        Check if a class is supported for config operation.
        """
        if session is not None:
            cls.getclsoptions(tmpcls, session)
        if 'POST' in optionsdict[tmpcls]['OPTIONS']:
            return True
        return False

    @classmethod
    def isValidrequest(cls, mgr, fid, op, tmpcls, slot, session=None):
        """
        Check if an config operation for a class is valid.
        """
        ormop = clsmanager.getConfigOperation(op)
        if session is not None:
            cls.getclsoptions(tmpcls, session)
        if ormop in optionsdict[tmpcls]['OPTIONS']:
            if cls.getClsStageSupported(tmpcls, op, slot) is True:
                inputs = mgr.get(fid, tmpcls, op, slot, session)
                if len(inputs) > 0:
                    return True
        return False

    @classmethod
    def isSingletonClass(cls, tmpcls):
        """
        Check if the class is a singleton class.
        """
        if tmpcls in [defined_configuration, effective_configuration]:
            if cls.ignoreClass(tmpcls):
                return False
            return True
        return False

    @classmethod
    def getSlotAttrib(cls, obj):
        """
        Get the slot attribute for a pyfos class object.
        """
        attr = None
        if obj.__class__ in restslotattributedict.keys():
            attr = restslotattributedict[obj.__class__]
        return attr

    @classmethod
    def getSlotforObject(cls, obj):
        """
        Get the slot from the class object.
        """
        if obj.__class__ in restslotattributedict.keys():
            attr = cls.getSlotAttrib(obj)
            if attr is not None:
                peek = getattr(obj, "peek_" + attr)
                slot = str(peek()).split('/')[0]
        else:
            return False, "0"
        return True, slot

    @classmethod
    def isSlotBasedObject(cls, instcls):
        """
        Check is the class is object are slot based.
        """
        if instcls in restslotattributedict.keys():
            return True
        return False

    @classmethod
    def ignoreClass(cls, tmpcls):
        if tmpcls in [effective_configuration]:
            return True
        return False

    @classmethod
    def sessionkey(cls, session):
        """
        Get the session key authorization.
        """
        return session["credential"]["Authorization"]

    @classmethod
    def addsession(cls, session, username, passwd):
        """
        Add the session for session management for Callback handling
        support.
        """
        sessionkey = cls.sessionkey(session)
        tmpdict = dict({'username': username, 'password': passwd})
        sessionmgr.update(dict({sessionkey: tmpdict}))

    @classmethod
    def getsessionuser(cls, session):
        """
        Get the session user from session
        """
        sessionkey = session["credential"]["Authorization"]
        if sessionkey in sessionmgr.keys():
            return True, sessionmgr[sessionkey]['username']
        return False, None

    @classmethod
    def getsessionpasswd(cls, session):
        """
        Get the session password from session
        """
        sessionkey = cls.sessionkey(session)
        if sessionkey in sessionmgr.keys():
            return True, sessionmgr[sessionkey]['password']
        return False, None

    @classmethod
    def reinitsession(cls, arg, session):
        """
        Callback Handler to reinit the session.
        """
        arg = None
        print("Dup Session start")
        cls.log(1, "Dup Session start")
        ret, username = cls.getsessionuser(session)
        if ret is False:
            print("Unable to reinit the session", session, arg)
            cls.log(3, "Unable to reinit the session",
                    session, arg)
            return False
        ret, passwd = cls.getsessionpasswd(session)
        if ret is False:
            print("Unable to reinit the session", session, arg)
            cls.log(3, "Unable to reinit the session",
                    session, arg)
            return False

        IP = session["ip_addr"]
        # vfid = session["vfid"]
        https = session["ishttps"]
        # debug = session["debug"]
        # throttle_delay = session["throttle_delay"]
        newsession = None
        retry = 0
        for i in range(10):
            retry = i
            newsession = auth.login(username, passwd, IP, https)
            if auth.is_failed_login(newsession):
                cls.sleep(20, session)
                continue
            break
        if not auth.is_failed_login(newsession):
            # print('old', cls.sessionkey(session), 'New',
            #       cls.sessionkey(newsession))
            session['credential'] = newsession['credential']
            session["version"] = newsession["version"]
            print("Dup Session Completed after Iterations:", retry)
            cls.log(1, "Dup Session Completed after Iterations:",
                    retry)
            return True
        print("Dup Session Failed.")
        cls.log(2, "Dup Session Failed.")
        sys.exit('Exiting as session dup didn\'t work')
        return False

    @classmethod
    def sleep(cls, delay, session):
        """
        Callback Handler to sleep the session.
        """
        print("Start sleep for [", delay, "]s.[", session['ip_addr'], "]")
        cls.log(1, "Start sleep for [", delay,
                "]s.[", session['ip_addr'], "]")
        time.sleep(delay)
        print("End sleep of [", delay, "]s.[", session['ip_addr'], "]")
        cls.log(1, "End sleep of [",
                delay, "]s.[", session['ip_addr'], "]")

    @classmethod
    def cbhandler(cls, session, cb_input):
        """
        Callback Handler function to execute all callbacks
        """
        commandhandler = dict()
        commandhandler.update(dict({'sleep': cls.sleep}))
        commandhandler.update(dict({'dupsession': cls.reinitsession}))
        for i in range(len(cb_input)):
            command = cb_input[i]['cmd']
            arg = cb_input[i]['arg']
            if command in commandhandler.keys():
                cb_input[i]['ret'] = commandhandler[command](arg, session)
            else:
                print("Unknown command passed", command)
                cls.log(3, "Unknown command passed", command)

    @classmethod
    def getcallback(cls, cmd, arg):
        """
        Get the Callback Handler list per config stage/class.
        """
        return [dict({'cmd': cmd, 'arg': arg, 'ret': None})]

    @classmethod
    def getsleepcallback(cls, arg):
        """
        Get the sleep Callback Handler as per delay args in seconds.
        """
        return cls.getcallback('sleep', arg)

    @classmethod
    def getreinitsessioncallback(cls, arg):
        """
        Get the Dup/Reinit session Callback.
        """
        return cls.getcallback('dupsession', arg)

    @classmethod
    def getbladeslots(cls, ret):
        """
        Get the blade slots as per blade response
        """
        tmpslots = []
        if not utils.is_failed_resp(ret):
            if isinstance(ret, blade):
                ret = [ret]
            for i in range(len(ret)):
                rret, slot = cls.getSlotforObject(ret[i])
                if rret is False and slot != '0':
                    print(ret[i])
                tmpslots.append(slot)
        return tmpslots

    @classmethod
    def diffignoreattrib(cls, instcls):
        """
        Get the list of ignored attrib in diff Calculation.
        """
        if instcls == effective_configuration:
            return ["checksum"]
        if instcls == fibrechannel:
            return ["neighbor_wwn"]
        if instcls == port_group:
            return ["port_group_f_ports_f_port"]
        if instcls == fibrechannel_switch:
            return ["enabled_state", "domain_id"]
        if instcls == fibrechannel_logical_switch:
            return ["ge_port_member_list_port_member"]
        return None

    @classmethod
    def stageordering(cls, instcls, old, new):
        """
        The stage ordering check and handling support for Callack handling.
        """
        if instcls == blade:
            ret, slot = cls.getSlotforObject(old)
            if ret is False and slot != '0':
                print(old)
            cblist = cls.getsleepcallback(400)
            if slot == '0':
                cblist += cls.getreinitsessioncallback(None)
            cblist += cls.getsleepcallback(30)
            if old.peek_extension_app_mode() == "FCIP" and\
               new.peek_extension_app_mode() == "hybrid":
                cls.setClsStageCB(instcls, "PRE_PATCH", slot, cblist)
                cls.setClsStagePri(instcls, "PRE_PATCH", slot, 10)
                # elif is causing identation error in all cases
                # adding return for all cases for flake8
                return
            if new.peek_extension_app_mode() == "FCIP" and\
               old.peek_extension_app_mode() == "hybrid":
                cls.setClsStageCB(instcls, "PRE_PATCH", slot, cblist)
                cls.setClsStagePri(instcls, "PRE_PATCH", slot, 1)
                return
            if new.peek_extension_ve_mode() == "20VE" and\
               old.peek_extension_app_mode() == "10VE":
                cls.setClsStageCB(instcls, "PRE_PATCH", slot, cblist)
                cls.setClsStagePri(instcls, "PRE_PATCH", slot, 10)
                return
            if new.peek_extension_app_mode() == "10VE" and\
               old.peek_extension_app_mode() == "20VE":
                cls.setClsStageCB(instcls, "PRE_PATCH", slot, cblist)
                cls.setClsStagePri(instcls, "PRE_PATCH", slot, 10)
                return
        elif instcls == fibrechannel_switch:
            ret, slot = cls.getSlotforObject(old)
            if ret is False and slot != '0':
                print(old)
            cblist = cls.getsleepcallback(400)
            if slot == '0':
                cblist += cls.getreinitsessioncallback(None)
            cblist += cls.getsleepcallback(30)
            if old.peek_ag_mode() != new.peek_ag_mode():
                cls.setClsStageCB(instcls, "PRE_DELETE", slot, cblist)
                # print(slot, cls.getClsStageCB(instcls, "PRE_DELETE", slot))
        elif instcls == chassis:
            ret, slot = cls.getSlotforObject(old)
            if ret is False and slot != '0':
                print(old)
            cblist = cls.getsleepcallback(500)
            if slot == '0':
                cblist += cls.getreinitsessioncallback(None)
            cblist += cls.getsleepcallback(30)
            if old.peek_vf_enabled() != new.peek_vf_enabled():
                cls.setClsStageCB(instcls, "PRE_PATCH", slot, cblist)
                # print(slot, cls.getClsStageCB(instcls, "PRE_PATCH", slot))

    @classmethod
    def sanitize(cls, instcls, old):
        """
        These are all conditional based set operation and defaults
        ignore settings as per yang being handled for class objects.
        They can be further handled separately per HTTP operation as
        well based on the diff operations identified individually for
        the objects as well.
        """
        if instcls == extension_tunnel:
            if old.peek_compression_protocol_fc_compression() == -1:
                old.set_compression_protocol_fc_compression(None)
            if old.peek_compression_protocol_ip_compression() == -1:
                old.set_compression_protocol_ip_compression(None)
            if old.peek_ficon() == 0:
                old.set_ficon_read_block_id_emulation(None)
                old.set_ficon_device_acknowledgement_emulation(None)
                old.set_ficon_tape_write_timer(None)
                old.set_ficon_tape_read_acceleration(None)
                old.set_ficon_xrc_acceleration(None)
                old.set_ficon_tin_tir_emulation(None)
                old.set_ficon_tape_read_max_devices(None)
                old.set_ficon_teradata_write_acceleration(None)
                old.set_ficon_tape_read_max_pipe(None)
                old.set_ficon_tape_write_max_devices(None)
                old.set_ficon_tape_write_max_devices(None)
                old.set_ficon_tape_write_acceleration(None)
                old.set_ficon_oxid_base(None)
                old.set_ficon_tape_write_max_chain(None)
                old.set_ficon_teradata_read_acceleration(None)
                old.set_ficon_tape_write_max_pipe(None)
        if instcls == extension_circuit:
            if old.peek_l2_cos_priority_control() == '0':
                old.set_l2_cos_priority_control(None)
            if old.peek_l2_cos_fc_priority_low() == '0':
                old.set_l2_cos_fc_priority_low(None)
            if old.peek_l2_cos_fc_priority_high() == '0':
                old.set_l2_cos_fc_priority_high(None)
            if old.peek_l2_cos_fc_priority_medium() == '0':
                old.set_l2_cos_fc_priority_medium(None)
            if old.peek_l2_cos_ip_priority_low() == '0':
                old.set_l2_cos_ip_priority_low(None)
            if old.peek_l2_cos_ip_priority_high() == '0':
                old.set_l2_cos_ip_priority_high(None)
            if old.peek_l2_cos_ip_priority_medium() == '0':
                old.set_l2_cos_ip_priority_medium(None)
            if old.peek_dscp_priority_control() == '0':
                old.set_dscp_priority_control(None)
            if old.peek_dscp_fc_priority_low() == '0':
                old.set_dscp_fc_priority_low(None)
            if old.peek_dscp_fc_priority_high() == '0':
                old.set_dscp_fc_priority_high(None)
            if old.peek_dscp_fc_priority_medium() == '0':
                old.set_dscp_fc_priority_medium(None)
            if old.peek_dscp_ip_priority_low() == '0':
                old.set_dscp_ip_priority_low(None)
            if old.peek_dscp_ip_priority_high() == '0':
                old.set_dscp_ip_priority_high(None)
            if old.peek_dscp_ip_priority_medium() == '0':
                old.set_dscp_ip_priority_medium(None)
            if old.peek_remote_ha_ip_address() == "0.0.0.0":
                old.set_remote_ha_ip_address(None)
            if old.peek_local_ha_ip_address() == "0.0.0.0":
                old.set_local_ha_ip_address(None)
            if old.peek_remote_ip_address() == "0.0.0.0":
                old.set_remote_ip_address(None)
            if old.peek_local_ip_address() == "0.0.0.0":
                old.set_local_ip_address(None)
        if instcls == extension_ipsec_policy:
            old.set_restart_ike_sessions(None)

    @classmethod
    def getclasspatchstage(cls, instcls, obj):
        """
        This is to get the patch stage for the class object based on diff
        default stage is PRE_PATCH.
        """
        stage = "PATCH"
        if instcls == fibrechannel_switch:
            return 'PRE_DELETE'
        elif instcls == effective_configuration:
            if obj.peek_default_zone_access() is not None:
                return 'PRE_PATCH'
            elif obj.peek_cfg_action() == 2:
                return 'PRE_DELETE'
            elif obj.peek_cfg_name() is not None:
                return 'POST_PATCH'
        elif instcls == port_group:
            return 'POST_PATCH'
        elif instcls == fibrechannel_logical_switch:
            return 'PRE_DELETE'
        return stage

    @classmethod
    def checkvfsupported(cls, instcls):
        vfsupportedlist = [fibrechannel,
                           extension_circuit,
                           extension_circuit_statistics,
                           extension_tunnel,
                           extension_tunnel_statistics,
                           extension_ip_route,
                           extension_ip_interface,
                           gigabitethernet,
                           gigabitethernet_statistics,
                           fibrechannel_logical_switch,
                           logical_e_port,
                           ]
        if instcls in vfsupportedlist:
            return True
        return False

    @classmethod
    def getpostsupported(cls, instcls, session=None):
        if cls.ispostSupportedClass(instcls, session):
            return "POST"
        return 'PRE_PATCH'

    @classmethod
    def pristage(cls, instcls):
        """
        The stage priority ordering per config stage for all class.
        """
        if instcls == hba:
            return (0, 0, 0, 0, 0)
        if instcls == fibrechannel_name_server:
            return (0, 0, 0, 0, 0)
        if instcls == fibrechannel_diagnostics:
            return (0, 0, 0, 0, 0)
        if instcls == fibrechannel:
            return (0, 0, 1, 0, 0)
        if instcls == defined_configuration:
            return (0, 0, 0, 0, 0)
        if instcls == effective_configuration:
            return (0, 1, 1, 1, 1)
        if instcls == extension_circuit:
            return (0, 2, 2, 7, 2)
        if instcls == extension_circuit_statistics:
            return (0, 0, 0, 0, 0)
        if instcls == extension_tunnel:
            return (0, 3, 3, 6, 3)
        if instcls == extension_tunnel_statistics:
            return (0, 0, 0, 0, 0)
        if instcls == extension_ip_route:
            return (0, 4, 4, 5, 4)
        if instcls == extension_ip_interface:
            return (0, 5, 5, 4, 5)
        if instcls == extension_ipsec_policy:
            return (0, 6, 6, 3, 6)
        if instcls == gigabitethernet:
            return (0, 7, 7, 2, 7)
        if instcls == fibrechannel_logical_switch:
            return (0, 0, 10, 0, 0)
        if instcls == fibrechannel_switch:
            return (0, 0, 0, 0, 0)
        if instcls == chassis:
            return (0, 10, 0, 0, 0)
        if instcls == ha_status:
            return (0, 0, 0, 0, 0)
        if instcls == port_group:
            return (0, 1, 3, 4, 0)
        if instcls == f_port_list:
            return (0, 0, 4, 0, 0)
        if instcls == policy:
            return (0, 3, 3, 1, 0)
        if instcls == n_port_settings:
            return (0, 1, 4, 2, 0)
        if instcls == n_port_map:
            return (0, 2, 5, 3, 0)
        if instcls == gigabitethernet_statistics:
            return (0, 0, 0, 0, 0)
        if instcls == switch_configuration:
            return (0, 0, 0, 0, 0)
        if instcls == f_port_login_settings:
            return (0, 0, 0, 0, 0)
        if instcls == raslog:
            return (0, 0, 0, 0, 0)
        if instcls == raslog_module:
            return (0, 0, 0, 0, 0)
        if instcls == log_quiet_control:
            return (0, 0, 0, 0, 0)
        if instcls == log_setting:
            return (0, 0, 0, 0, 0)
        if instcls == fan:
            return (0, 0, 0, 0, 0)
        if instcls == blade:
            return (0, 8, 1, 1, 8)
        if instcls == power_supply:
            return (0, 0, 0, 0, 0)
        if instcls == clock_server:
            return (0, 0, 0, 0, 0)
        if instcls == time_zone:
            return (0, 0, 0, 0, 0)
        if instcls == tacacs_server:
            return (0, 0, 0, 0, 0)
        if instcls == ldap_server:
            return (0, 0, 0, 0, 0)
        if instcls == auth_spec:
            return (0, 0, 0, 0, 0)
        if instcls == ipfilter_policy:
            return (0, 1, 0, 2, 0)
        if instcls == ipfilter_rule:
            return (0, 2, 0, 1, 0)
        if instcls == sec_crypto_cfg:
            return (0, 0, 0, 0, 0)
        if instcls == sec_crypto_cfg_template:
            return (0, 0, 0, 0, 0)
        if instcls == sec_crypto_cfg_template_action:
            return (0, 0, 0, 0, 0)
        if instcls == ldap_role_map:
            return (0, 0, 0, 0, 0)
        if instcls == password_cfg:
            return (0, 0, 0, 0, 0)
        if instcls == user_specific_password_cfg:
            return (0, 2, 2, 2, 0)
        if instcls == user_config:
            return (0, 1, 1, 1, 0)
        if instcls == sshutil:
            return (0, 0, 0, 0, 0)
        if instcls == sshutil_key:
            return (0, 0, 0, 0, 0)
        if instcls == sshutil_public_key:
            return (0, 0, 0, 0, 0)
        if instcls == sshutil_public_key_action:
            return (0, 0, 0, 0, 0)
        if instcls == password:
            return (0, 0, 0, 0, 0)
        if instcls == security_certificate:
            return (0, 0, 0, 0, 0)
        if instcls == security_certificate_generate:
            return (0, 0, 0, 0, 0)
        if instcls == security_certificate_action:
            return (0, 0, 0, 0, 0)
        if instcls == radius_server:
            return (0, 0, 0, 0, 0)
        if instcls == history_log:
            return (0, 0, 0, 0, 0)
        if instcls == sensor:
            return (0, 0, 0, 0, 0)
        if instcls == wwn:
            return (0, 0, 0, 0, 0)
        if instcls == logical_e_port:
            return (0, 0, 0, 0, 0)
        return (0, 0, 0, 0, 0)

    @classmethod
    def initSlotObjectDict(cls):
        """
        Init the slot object dict for mapping slot attribute per pyfos class.
        """
        restslotattributedict.update(dict({extension_tunnel: "name"}))
        restslotattributedict.update(dict({extension_circuit: "name"}))
        restslotattributedict.update(dict({extension_ip_interface: "name"}))
        restslotattributedict.update(dict({extension_ip_route: "name"}))
        restslotattributedict.update(dict({gigabitethernet: "name"}))
        restslotattributedict.update(dict({blade: "slot_number"}))

    @classmethod
    def getmultiplesheetdict(cls, container):
        """
        Get the sheet dictionary per class for dump and load configuration.
        """
        defined = 'defined-configuration'
        sheetdict = dict({'defined-configuration': dict()})
        sheetdict[defined].update(dict({'cfg': ['cfg_cfg_name',
                                                'cfg_member_zone_zone_name']}))
        sheetdict[defined].update(dict({'zone': ['zone_zone_name',
                                                 'zone_zone_type',
                                                 'zone_zone_type_string',
                                                 'zone_member_entry_' +
                                                 'entry_name',
                                                 'zone_member_entry_' +
                                                 'principal_entry_name'
                                                 ]}))
        sheetdict[defined].update(dict({'alias': ['alias_alias_name',
                                                  'alias_member_entry' +
                                                  '_alias_entry_name',
                                                  ]}))
        if container in sheetdict.keys():
            return sheetdict[container]

        return None
