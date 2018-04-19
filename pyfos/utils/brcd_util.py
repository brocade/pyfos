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

import pyfos.pyfos_auth as pyfos_auth
import pyfos.pyfos_util as pyfos_util
import getpass
import getopt
import sys
import atexit
import inspect
import pyfos.utils.brcd_cli as brcd_cli

session = None


def full_usage(usage):
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


def base_generic_input(argv, usage, valid_options):
    if len(argv) == 0:
        full_usage(usage)
        sys.exit()

    ret_dict = dict()

    # default value that should be added here
    ret_dict["secured"] = None
    ret_dict["verbose"] = 0

    try:
        opts, args = getopt.getopt(
                argv, "hi:f:s:L:P:v",
                [
                    "allaccess=",
                    "compare=",
                    "device=",
                    "disable",
                    "enable",
                    "filename=",
                    "help",
                    "hostname=",
                    "hostport=",
                    "ipaddr=",
                    "login=",
                    "members=",
                    "name=",
                    "password=",
                    "pmembers=",
                    "reffcport=",
                    "secured=",
                    "speed=",
                    "template=",
                    "targetname=",
                    "targetport=",
                    "usepeer=",
                    "username=",
                    "verbose",
                    "vfid=",
                    "xlsapply=",
                    "xlscheck=",
                ]
                )
    except getopt.GetoptError as err:
        print("getopt error", str(err))
        full_usage(usage)
        sys.exit(2)

    if len(args) > 0:
        print("*** Contains invalid options:", args[0])
        full_usage(usage)
        sys.exit(3)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            full_usage(usage)
            sys.exit()
        elif opt in ("--allaccess"):
            if not pyfos_util.isInt(arg):
                print("*** Invalid allacess:", arg)
                full_usage(usage)
                sys.exit(5)

            ret_dict["allaccess"] = int(arg)
        elif opt in ("--compare"):
            ret_dict["compare"] = arg
        elif opt in ("--disable"):
            ret_dict["disable"] = True
        elif opt in ("--device"):
            if not pyfos_util.isWWN(arg):
                print("*** Invalid device:", arg)
                full_usage(usage)
                sys.exit(5)

            ret_dict["device"] = arg
        elif opt in ("--enable"):
            ret_dict["enable"] = True
        elif opt in ("-f", "--vfid"):
            if not pyfos_util.isInt(arg):
                print("*** Invalid vfid:", arg)
                full_usage(usage)
                sys.exit(5)

            ret_dict["vfid"] = int(arg)
        elif opt in ("--filename"):
            ret_dict["filename"] = arg
        elif opt in ("--hostname"):
            ret_dict["hostname"] = arg
        elif opt in ("--hostport"):
            if not pyfos_util.isWWN(arg):
                print("*** Invalid hostport:", arg)
                full_usage(usage)
                sys.exit(5)

            ret_dict["hostport"] = arg
        elif opt in ("-i", "--ipaddr"):
            if not pyfos_util.isIPAddr(arg):
                print("*** Invalid ipaddr:", arg)
                full_usage(usage)
                sys.exit(5)

            ret_dict["ipaddr"] = arg
        elif opt in ("-L", "--login"):
            ret_dict["login"] = arg
        elif opt in ("--members"):
            ret_dict["members"] = arg.split(";")
        elif opt in ("--name"):
            ret_dict["name"] = arg
        elif opt in ("--pmembers"):
            ret_dict["pmembers"] = arg.split(";")
        elif opt in ("-P", "--password"):
            ret_dict["password"] = arg
        elif opt in ("--reffcport"):
            if not pyfos_util.isSlotPort(arg):
                print("*** Invalid reffcport:", arg)
                full_usage(usage)
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
        elif opt in ("--show"):
            ret_dict["show"] = 1
        elif opt in ("--speed"):
            if not pyfos_util.isInt(arg):
                print("*** Invalid speed:", arg)
                full_usage(usage)
                sys.exit(5)

            ret_dict["speed"] = int(arg)
        elif opt in ("--template"):
            ret_dict["template"] = arg
        elif opt in ("--targetname"):
            ret_dict["targetname"] = arg
        elif opt in ("--targetport"):
            if not pyfos_util.isWWN(arg):
                print("*** Invalid targetport:", arg)
                full_usage(usage)
                sys.exit(5)

            ret_dict["targetport"] = arg
        elif opt in ("--username"):
            ret_dict["username"] = arg
        elif opt in ("--usepeer"):
            if arg != "WWN" and arg != "":
                print("*** Invalid userpeer:", arg)
                full_usage(usage)
                sys.exit(5)

            ret_dict["usepeer"] = arg
        elif opt in ("-v", "--verbose"):
            ret_dict["verbose"] = 1
        elif opt in ("--xlscheck"):
            ret_dict["xlscheck"] = arg
        elif opt in ("--xlsapply"):
            ret_dict["xlsapply"] = arg
        else:
            print("unknown", opt)
            full_usage(usage)
            sys.exit(5)

    if "login" not in ret_dict.keys():
        login = input("Login:")
        ret_dict["login"] = login

    if "password" not in ret_dict.keys():
        password = getpass.getpass()
        ret_dict["password"] = password

    if valid_options is not None:
        for k, v in ret_dict.items():
            if (k != "login" and k != "password" and
                    k != "ipaddr" and k != "secured" and
                    k != "vfid" and k != "verbose"):
                found = False
                for valid_option in valid_options:
                    if valid_option == k:
                        found = True
                        break
                if not found:
                    print("*** Invalid option given:", k)
                    full_usage(usage)
                    sys.exit(4)

    if "ipaddr" not in ret_dict:
        print("*** IP address must be given:")
        full_usage(usage)
        sys.exit(6)

    return ret_dict


def generic_input(argv, cls_usage, filters=None, validate=None):
    inputs = dict()
    if inspect.isclass(cls_usage):
        custom_cli = brcd_cli.getcustomcli(cls_usage().container)
        restobject = cls_usage.parse(argv, inputs, filters, custom_cli, validate)
        if restobject is None:
                sys.exit(4)
        else:
            inputs.update({'utilobject': restobject})
            inputs.update({'utilclass': cls_usage})
            inputs.update({'utilfilters': filters})
            inputs.update({'utilusage': restobject.showusage(filters)})
        return inputs
    else:
        # Check filters can be none as well based on the utils.
        inputs = base_generic_input(argv, cls_usage, filters)
    return inputs


def parse(argv, cls_usage, filters=None, validate=None):
    return (generic_input(argv, cls_usage, filters, validate))


def getsession(inputs):
    ishttps = None
    if 'secured' in inputs.keys():
        ishttps = inputs['secured']
    session = pyfos_auth.login(inputs["login"], inputs["password"],
                               inputs["ipaddr"], ishttps)
    if pyfos_auth.is_failed_login(session):
        print("login failed because",
              session.get(pyfos_auth.CREDENTIAL_KEY)
              [pyfos_auth.LOGIN_ERROR_KEY])
        print(inputs['utilusage'])
        sys.exit(3)
    exit_register(session)
    if 'vfid' in inputs:
        pyfos_auth.vfid_set(session, inputs['vfid'])
    if 'verbose' in inputs:
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


def defaultclioptions(cls):
    retdict = dict()
    if inspect.isclass(cls):
        retdict.update(cls().displaycustomcli())
    elif isinstance(cls, list):
        for i in range(len(cls)):
            retdict.update(cls[i]().displaycustomcli())
    return retdict
