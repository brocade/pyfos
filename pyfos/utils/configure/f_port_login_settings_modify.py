#!/usr/bin/env python3

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

:mod:`f_port_login_settings_modify` - PyFOS util for configuring login
**********************************************************************
The :mod:`f_port_login_settings_modify` provides for configuring login

This module is a standalone script that can be used to display login
attributes

* inputs:
    * -L=<login>: Login ID. If not provided, interactive
        prompt will request one.
    * -P=<password>: Password. If not provided, interactive
        prompt will request one.
    * -i=<IP address>: IP address
    * -f=<VFID>: VFID or -1 if VF is disabled. If unspecified,
        VFID of 128 is assumed.

* Util scripts options:

    * --free-fdisc=FREE-FDISC                         Configures fdisc logins.
    * --max-logins-port=MAX-LOGINS-PORT               Sets Max Logins port.
    * --enforce-login=ENFORCE-LOGIN                   Sets Login precedence.
    * --max-logins-switch=MAX-LOGINS-SWITCH           Sets Max Logins switch.
    * --max-logins=MAX-LOGINS                         Sets Max logins system.
    * --stage-interval=STAGE-INTERVAL                 Sets stage interval time.


* outputs:
    * HTTP Status in JSON format

.. function:: patch_login_conf (session, maxl, mflps, si, ff, el, mflpp)

        Example usage of the method::

            ret = f_port_login_settings_modify.patch_login_conf (session, maxl,
                                mflps, si, ff, el, mflpp)
            print (ret)

        Details::

            val = {
                "max-logins": maxl,
                "max-flogi-rate-per-switch": mflps,
                "stage-interval": si,
                "free-fdisc": ff,
                "enforce-login": el,
                "max-flogi-rate-per-port": mflpp
                }
            obj = f_port_login_settings(val)
            result = _patch_login_conf(session, obj)
            return result

        * inputs:
            :param session: session returned by login.
            :param maxl: Configures system wide Max logins.
            :param mflps: Configures Max Logins per second in a switch.
            :param si: Configures stage interval time in milliseconds.
            :param ff: Configures freely allowed fdisc logins before staging.
            :param el: Configures the login type precedence during collision.
            :param mflpp: Configures Max Logins per second in a port.

        * outputs:
            :rtype: dictionary of return status matching rest response

        *use cases*

        1. Patch the f-port login parameters of switch.


"""

import pyfos.pyfos_auth as pyfos_auth
import pyfos.pyfos_brocade_fibrechannel_configuration as py_fc
import pyfos.pyfos_util as pyfos_util
import sys
import pyfos.utils.brcd_util as brcd_util

login = py_fc.f_port_login_settings


def patch_login_conf(session, maxl, mflps, si, ff, el, mflpp):
    val = {
        "max-logins": maxl,
        "max-flogi-rate-per-switch": mflps,
        "stage-interval": si,
        "free-fdisc": ff,
        "enforce-login": el,
        "max-flogi-rate-per-port": mflpp
        }
    obj = login(val)
    result = _patch_login_conf(session, obj)
    return result


def validate(obj):
    flag = 0
    if obj.peek_max_logins() is not None:
        flag = flag + 1
    if obj.peek_max_flogi_rate_per_switch() is not None:
        flag = flag + 1
    if obj.peek_stage_interval() is not None:
        flag = flag + 1
    if obj.peek_free_fdisc() is not None:
        flag = flag + 1
    if obj.peek_enforce_login() is not None:
        flag = flag + 1
    if obj.peek_max_flogi_rate_per_port() is not None:
        flag = flag + 1

    return 0 if flag >= 1 else 1


def _patch_login_conf(session, restobject):
    return restobject.patch(session)


def main(argv):

    filters = ['enforce_login', 'free_fdisc', 'max_flogi_rate_per_port',
               'max_flogi_rate_per_switch', 'max_logins', 'stage_interval']

    inputs = brcd_util.parse(argv, login, filters, validate)
    session = brcd_util.getsession(inputs)

    result = _patch_login_conf(inputs['session'], inputs['utilobject'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
