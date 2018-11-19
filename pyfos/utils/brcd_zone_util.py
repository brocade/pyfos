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

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
import pyfos.pyfos_brocade_zone as pyfos_zone
import pyfos.utils.zoning.zoning_cfg_save as cfgsave
import pyfos.utils.zoning.zoning_cfg_abort as cfgabort
from pyfos.utils import brcd_util


def zone_name_members_pmembers_func(session, inputs, usage, func):
    # comment zone helper to execute & commit
    # name, member, and principal member based operations
    if "name" not in inputs:
        print("*** missing input: name")
        pyfos_auth.logout(session)
        brcd_util.full_usage(usage)
        sys.exit()
    name = inputs["name"]

    if "members" not in inputs:
        members = None
    else:
        members = inputs["members"]

    if "pmembers" not in inputs:
        pmembers = None
    else:
        pmembers = inputs["pmembers"]

    if members is None and pmembers is None:
        print("*** missing input: members & pmembers")
        pyfos_auth.logout(session)
        brcd_util.full_usage(usage)
        sys.exit()

    current_effective = pyfos_zone.effective_configuration.get(session)

    print("executing", func.__name__)
    result = func(session, name, members, pmembers)
    if pyfos_util.is_failed_resp(result):
        pyfos_util.response_print(result)
        print(func.__name__, "failed. \n\nAborting transaction.")
        result = cfgabort.cfgabort(session)
        pyfos_util.response_print(result)
    else:
        pyfos_util.response_print(result)
        print(func.__name__, "succeeded. \n\nSaving transaction.")
        result = cfgsave.cfgsave(session, current_effective.peek_checksum())
        if pyfos_util.is_failed_resp(result):
            pyfos_util.response_print(result)
            print(func.__name__, "failed. \n\nAborting transaction.")
            result = cfgabort.cfgabort(session)
            pyfos_util.response_print(result)


def zone_name_members_func(session, inputs, usage, func):
    # comment zone helper to execute & commit
    # name, and member based operations
    if "name" not in inputs:
        print("*** missing input: name")
        pyfos_auth.logout(session)
        brcd_util.full_usage(usage)
        sys.exit()
    name = inputs["name"]

    if "members" not in inputs:
        print("*** missing input: members")
        pyfos_auth.logout(session)
        brcd_util.full_usage(usage)
        sys.exit()
    members = inputs["members"]

    current_effective = pyfos_zone.effective_configuration.get(session)

    print("executing", func.__name__)
    result = func(session, name, members)
    if pyfos_util.is_failed_resp(result):
        pyfos_util.response_print(result)
        print(func.__name__, "failed. \n\nAborting transaction.")
        result = cfgabort.cfgabort(session)
        pyfos_util.response_print(result)
    else:
        pyfos_util.response_print(result)
        print(func.__name__, "succeeded. \n\nSaving transaction.")
        result = cfgsave.cfgsave(session, current_effective.peek_checksum())
        if pyfos_util.is_failed_resp(result):
            pyfos_util.response_print(result)
            print(func.__name__, "failed. \n\nAborting transaction.")
            result = cfgabort.cfgabort(session)
            pyfos_util.response_print(result)


def zone_name_func(session, inputs, usage, func):
    # comment zone helper to execute & commit
    # name based operations
    if "name" not in inputs:
        print("*** missing input: name")
        pyfos_auth.logout(session)
        brcd_util.full_usage(usage)
        sys.exit()
    name = inputs["name"]

    current_effective = pyfos_zone.effective_configuration.get(session)

    print("executing", func.__name__)
    result = func(session, name)
    if pyfos_util.is_failed_resp(result):
        pyfos_util.response_print(result)
        print(func.__name__, "failed. \n\nAborting transaction.")
        result = cfgabort.cfgabort(session)
        pyfos_util.response_print(result)
    else:
        pyfos_util.response_print(result)
        print(func.__name__, "succeeded. \n\nSaving transaction.")
        result = cfgsave.cfgsave(session, current_effective.peek_checksum())
        if pyfos_util.is_failed_resp(result):
            pyfos_util.response_print(result)
            print(func.__name__, "failed. \n\nAborting transaction.")
            result = cfgabort.cfgabort(session)
            pyfos_util.response_print(result)
