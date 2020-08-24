#!/usr/bin/env python3

"""
 Copyright 2018 Brocade Communications Systems LLC.  All rights reserved.

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may also obtain a copy of the License at
 http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""

import getpass
import getopt
import sys
import os
import atexit
import inspect
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.utils import brcd_cli
from pyfos.pyfos_auth_token import auth_token_manager
from pyfos import pyfos_rest_util

# pylint: disable=W0603
session = None

full_usage_infra_short_1 = "<-i IPADDR> <-L LOGIN> <-P PASSWORD>"
full_usage_infra_short_2 = "[-f VFID] [-v]"


def full_usage(usage, valid_options, sessionless=True):
    o_str = ""
    for v_op in valid_options:
        o_str = o_str + " <--" + v_op + "=" + v_op.upper() + ">"
    print(os.path.basename(sys.argv[0]) +
          " " + full_usage_infra_short_1 +
          o_str +
          " " + full_usage_infra_short_2)
    print("")
    print("Usage:")
    print("")
    print("  Infrastructure options:")
    print("")
    print("    -i, --ipaddr=IPADDR          IP address of FOS switch")
    print("    -L, --login=LOGIN            login name")
    print("    -P, --password=PASSWORD      password")
    print(
            "    -f, --vfid=VFID              VFID to which"
            " the request is directed to. [OPTIONAL]")
    print(
            "    -s, --secured=MODE           HTTPS mode \"self\" or"
            " \"CA\". [OPTIONAL]")
    print("    -v, --verbose                verbose mode. [OPTIONAL]")
    if sessionless:
        print("    -a, --authtoken              AuthToken value string" +
              " or AuthTokenManager config file. [OPTIONAL]")
        print("    -z, --nosession              Session less Authentication.",
              " [OPTIONAL]")
        print("        --nocredential           No credential ",
              "Authentication. [OPTIONAL]")
    print("")
    usage()


def exit_handler():
    global session

    if session is not None:
        pyfos_auth.logout(session)


def exit_register(local_session):
    global session
    session = local_session
    atexit.register(exit_handler)


def base_generic_input(argv, usage, valid_options, sessionless):
    ret_dict = dict()

    # default value that should be added here
    ret_dict["secured"] = None
    ret_dict["verbose"] = 0
    ret_dict['utilusage'] = ""

    try:
        opts, args = getopt.getopt(
                argv, "hi:f:s:L:P:avz",
                [
                    "activate",
                    "allaccess=",
                    "authtoken=",
                    "acceptEULA",
                    "compare=",
                    "device=",
                    "disable",
                    "displayEULA",
                    "enable",
                    "filename=",
                    "help",
                    "hbaid=",
                    "hostname=",
                    "banner=",
                    "hostport=",
                    "ipaddr=",
                    "login=",
                    "members=",
                    "name=",
                    "password=",
                    "pmembers=",
                    "portid=",
                    "protocol=",
                    "messageid=",
                    "reffcport=",
                    "secured=",
                    "speed=",
                    "stage",
                    "template=",
                    "targetname=",
                    "targetport=",
                    "type=",
                    "usepeer=",
                    "username=",
                    "userpassword=",
                    "verbose",
                    "vfid=",
                    "xlsapply=",
                    "xlscheck=",
                    "json",
                    "nosession",
                    "nocredential",
                ]
                )
    except getopt.GetoptError as err:
        print("getopt error", str(err))
        full_usage(usage, valid_options, sessionless)
        sys.exit(2)

    if len(args) > 0:
        print("*** Contains invalid options:", args[0])
        full_usage(usage, valid_options, sessionless)
        sys.exit(3)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            full_usage(usage, valid_options, sessionless)
            sys.exit()
        elif opt == "--activate":
            ret_dict["activate"] = True
        elif opt == "--allaccess":
            if not pyfos_util.isInt(arg):
                print("*** Invalid allacess:", arg)
                full_usage(usage, valid_options, sessionless)
                sys.exit(5)

            ret_dict["allaccess"] = int(arg)
        elif opt == "--acceptEULA":
            ret_dict["acceptEULA"] = "accept-eula"
        elif opt in "--compare":
            ret_dict["compare"] = arg
        elif opt in "--disable":
            ret_dict["disable"] = True
        elif opt in "--displayEULA":
            ret_dict["displayEULA"] = "display-eula"
        elif opt in "--device":
            if not pyfos_util.isWWN(arg):
                print("*** Invalid device:", arg)
                full_usage(usage, valid_options, sessionless)
                sys.exit(5)

            ret_dict["device"] = arg
        elif opt in "--enable":
            ret_dict["enable"] = True
        elif opt in ("-f", "--vfid"):
            if not pyfos_util.isInt(arg):
                print("*** Invalid vfid:", arg)
                full_usage(usage, valid_options, sessionless)
                sys.exit(5)

            ret_dict["vfid"] = int(arg)
        elif opt in "--filename":
            ret_dict["filename"] = arg
        elif opt in "--hbaid":
            ret_dict["hbaid"] = arg
        elif opt in "--hostname":
            ret_dict["hostname"] = arg
        elif opt in "--banner":
            ret_dict["banner"] = arg
        elif opt in "--hostport":
            if not pyfos_util.isWWN(arg):
                print("*** Invalid hostport:", arg)
                full_usage(usage, valid_options, sessionless)
                sys.exit(5)

            ret_dict["hostport"] = arg
        elif opt in ("-i", "--ipaddr"):
            if not pyfos_util.isIPAddr(arg):
                print("*** Invalid ipaddr:", arg)
                full_usage(usage, valid_options, sessionless)
                sys.exit(5)

            ret_dict["ipaddr"] = arg
        elif opt in "--json":
            ret_dict["json"] = True
        elif opt in ("-L", "--login"):
            ret_dict["login"] = arg
        elif opt in "--members":
            ret_dict["members"] = arg.split(";")
        elif opt in "--name":
            ret_dict["name"] = arg
        elif opt in "--pmembers":
            ret_dict["pmembers"] = arg.split(";")
        elif opt in ("-P", "--password"):
            ret_dict["password"] = arg
        elif opt in "--portid":
            ret_dict["portid"] = arg
        elif opt in "--protocol":
            ret_dict["protocol"] = arg
        elif opt in "--messageid":
            ret_dict["messageid"] = arg
        elif opt in "--reffcport":
            if not pyfos_util.isSlotPort(arg):
                print("*** Invalid reffcport:", arg)
                full_usage(usage, valid_options, sessionless)
                sys.exit(5)

            ret_dict["reffcport"] = arg
        elif opt in ("-s", "--secured"):
            if arg == "self":
                ret_dict["secured"] = "self"
            elif arg == "CA":
                ret_dict["secured"] = "CA"
            else:
                print("defaults to CA")
                ret_dict["secured"] = "CA"
        elif opt in "--show":
            ret_dict["show"] = 1
        elif opt in "--speed":
            if not pyfos_util.isInt(arg):
                print("*** Invalid speed:", arg)
                full_usage(usage, valid_options, sessionless)
                sys.exit(5)

            ret_dict["speed"] = int(arg)
        elif opt in "--stage":
            ret_dict["stage"] = True
        elif opt in "--template":
            ret_dict["template"] = arg
        elif opt in "--targetname":
            ret_dict["targetname"] = arg
        elif opt in "--targetport":
            if not pyfos_util.isWWN(arg):
                print("*** Invalid targetport:", arg)
                full_usage(usage, valid_options, sessionless)
                sys.exit(5)

            ret_dict["targetport"] = arg
        elif opt in "--type":
            ret_dict["type"] = arg
        elif opt in "--username":
            ret_dict["username"] = arg
        elif opt in "--userpassword":
            ret_dict["userpassword"] = arg
        elif opt in "--usepeer":
            if arg not in ('WWN', ''):
                print("*** Invalid userpeer:", arg)
                full_usage(usage, valid_options, sessionless)
                sys.exit(5)

            ret_dict["usepeer"] = arg
        elif opt in ("-v", "--verbose"):
            ret_dict["verbose"] = 1
        elif opt in ("-z", "--nosession"):
            ret_dict["sessionless"] = True
        elif opt in "--nocredential":
            ret_dict["nocredential"] = True
        elif opt in ("-a", "--authtoken"):
            if len(arg) == 0:
                ret_dict['authtoken'] = None
            else:
                ret_dict['authtoken'] = arg
        elif opt in "--xlscheck":
            ret_dict["xlscheck"] = arg
        elif opt in "--xlsapply":
            ret_dict["xlsapply"] = arg
        else:
            print("unknown", opt)
            full_usage(usage, valid_options, sessionless)
            sys.exit(5)

    if "ipaddr" not in ret_dict:
        print("Missing IP address input")
        print("")
        full_usage(usage, valid_options, sessionless)
        sys.exit(6)

    if "login" not in ret_dict.keys():
        login = input("Login:")
        ret_dict["login"] = login

    if "password" not in ret_dict.keys():
        if 'authtoken' not in ret_dict.keys() and\
           'nocredential' not in ret_dict.keys():
            password = getpass.getpass()
            ret_dict["password"] = password

    if valid_options is not None:
        # pylint: disable=W0612
        for k, v in ret_dict.items():
            if k not in ('login', 'password', 'ipaddr',
                         'secured', 'vfid', 'verbose',
                         'authtoken', 'sessionless', 'utilusage',
                         'nocredential'):
                found = False
                for valid_option in valid_options:
                    if valid_option == k:
                        found = True
                        break
                if not found:
                    print("*** Invalid option given:", k)
                    full_usage(usage, valid_options, sessionless)
                    sys.exit(4)

    return ret_dict


def generic_input(argv, cls_usage, filters=None, validate=None,
                  sessionless=True):
    inputs = dict()
    if isinstance(cls_usage, str):
        mydict = brcd_cli.pseudorestcli(cls_usage)
    if inspect.isclass(cls_usage):
        custom_cli = brcd_cli.getcustomcli(cls_usage().container)
        restobject = cls_usage.parse(argv, inputs, filters,
                                     custom_cli, validate)
        if restobject is None:
            sys.exit(4)
        else:
            inputs.update({'utilobject': restobject})
            inputs.update({'utilclass': cls_usage})
            inputs.update({'utilfilters': filters})
            inputs.update({'utilusage': restobject.showusage(filters)})
        return inputs
    elif isinstance(cls_usage, str) and mydict is not None:
        restobject = pyfos_rest_util.rest_object.pseudodictrestobject(mydict)
        restobject = restobject.parse_commandline(argv, inputs,
                                                  filters, None, validate)
        if restobject is None:
            sys.exit(4)
        else:
            inputs.update({'utilobject': restobject})
            inputs.update({'utilclass': "runtime"})
            inputs.update({'utilfilters': filters})
            inputs.update({'utilusage': restobject.showusage(filters)})
        return inputs

    else:
        # Check filters can be none as well based on the utils.
        inputs = base_generic_input(argv, cls_usage, filters, sessionless)
    return inputs


def parse(argv, cls_usage, filters=None, validate=None):
    return generic_input(argv, cls_usage, filters, validate)


def getsession(inputs):
    global session
    tokenManager = None
    ishttps = None
    if 'authtoken' in inputs.keys():
        # Always need to use the Default Token Manager config
        # if user wants to use a different configuration then user
        # config store should be set as default store using the set
        # default store option.
        if inputs['authtoken'] is None or \
           auth_token_manager.isvalidconfig(inputs['authtoken']):
            tokenManager = auth_token_manager(inputs['authtoken'])
        else:
            tokenManager = inputs['authtoken']
        # tokenManager.show()

    # Get the password or else None
    ip = inputs.get("ipaddr", None)
    user = inputs.get("login", None)
    password = inputs.get("password", None)
    sessionless = inputs.get('sessionless', False)
    nocred = inputs.get('nocredential', False)

    if 'secured' in inputs.keys():
        ishttps = inputs['secured']

    # Default DEFAULT_THROTTLE_DELAY 1.1
    session = pyfos_auth.login(user, password,
                               ip, ishttps,
                               1.1, 0,
                               tokenManager,
                               sessionless,
                               nocred)

    if pyfos_auth.is_failed_login(session):
        print("login failed because",
              session.get(pyfos_auth.CREDENTIAL_KEY)
              [pyfos_auth.LOGIN_ERROR_KEY])
        print(inputs['utilusage'])
        sys.exit(3)
    exit_register(session)
    if 'vfid' in inputs:
        pyfos_auth.vfid_set(session, inputs['vfid'])
    if 'verbose' in inputs and inputs['verbose'] != 0:
        pyfos_auth.debug_set(session, 1)
    inputs['session'] = session
    return session


def clean(inputs):
    restobject = None
    filters = None
    if 'utilobject' in inputs.keys():
        restobject = inputs['utilobject']
        if 'utilfilters' in inputs.keys():
            filters = inputs['utilfilters']
        if restobject is not None:
            restobject.clean(filters)
            inputs['utilobject'] = restobject


def pseudodictrestobject(mydictkey):
    mydict = brcd_cli.pseudorestcli(mydictkey)
    if mydict is not None and isinstance(mydict, dict):
        restobject = pyfos_rest_util.rest_object.pseudodictrestobject(mydict)
        return restobject
    return None


def defaultclioptions(cls):
    retdict = dict()
    if inspect.isclass(cls):
        retdict.update(cls().displaycustomcli())
    elif isinstance(cls, list):
        for i in range(len(cls)):
            retdict.update(cls[i]().displaycustomcli())
    return retdict
