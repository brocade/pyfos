#!/usr/bin/env python3

"""
 Copyright 2017 Brocade Communications Systems, Inc.  All rights reserved.

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
import getpass
import getopt
import sys
import atexit

session = None


def exit_handler():
    global session

    if session is not None:
        pyfos_auth.logout(session)


def exit_register(local_session):
    global session
    session = local_session
    atexit.register(exit_handler)


def generic_input(argv, usage):
    if len(argv) == 0:
        usage()
        sys.exit()

    ret_dict = dict()

    try:
        opts, args = getopt.getopt(
                argv, "hn:i:m:f:p:a:d:u:e:s:c:L:P:",
                ["name=", "ipaddr=", "members=", "vf=", "pmembers=",
                 "allaccess=", "device=", "username=", "enabled=",
                 "speed=", "compare=", "hostname=", "hostport=",
                 "targetname=", "targetport=", "login=", "password="
                 ])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            usage()
            sys.exit()
        elif opt in ("-i", "--ipaddr"):
            ret_dict["ipaddr"] = arg
        elif opt in ("-a", "--allaccess"):
            ret_dict["allaccess"] = int(arg)
        elif opt in ("-c", "--compare"):
            ret_dict["compare"] = arg
        elif opt in ("-d", "--device"):
            ret_dict["device"] = arg
        elif opt in ("-e", "--enabled"):
            ret_dict["enabled"] = int(arg)
        elif opt in ("-f", "--vf"):
            ret_dict["vfid"] = int(arg)
        elif opt in ("-m", "--members"):
            ret_dict["members"] = arg.split(";")
        elif opt in ("-n", "--name"):
            ret_dict["name"] = arg
        elif opt in ("-p", "--pmembers"):
            ret_dict["pmembers"] = arg.split(";")
        elif opt in ("-s", "--speed"):
            ret_dict["speed"] = int(arg)
        elif opt in ("-u", "--username"):
            ret_dict["username"] = arg
        elif opt in ("--hostname"):
            ret_dict["hostname"] = arg
        elif opt in ("--hostport"):
            ret_dict["hostport"] = arg
        elif opt in ("--targetname"):
            ret_dict["targetname"] = arg
        elif opt in ("--targetport"):
            ret_dict["targetport"] = arg
        elif opt in ("-L", "--login"):
            ret_dict["login"] = arg
        elif opt in ("-P", "--password"):
            ret_dict["password"] = arg

    if "login" not in ret_dict.keys():
        login = input("Login:")
        ret_dict["login"] = login

    if "password" not in ret_dict.keys():
        password = getpass.getpass()
        ret_dict["password"] = password

    return ret_dict
