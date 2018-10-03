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

:mod:`maps_rule_create` - PyFOS util to create MAPS rule
*******************************************************************************

This script is used to create MAPS rule.

* inputs:

| Infrastructure options:

|   -i,--ipaddr=IPADDR     IP address of FOS switch.
|   -L,--login=LOGIN       login name.
|   -P,--password=PASSWORD password.
|   -f,--vfid=VFID         VFID to which the request is directed to [OPTIONAL].
|   -s,--secured=MODE      HTTPS mode "self" or "CA" [OPTIONAL].
|   -v,--verbose           verbose mode[OPTIONAL].

* Util scripts options:
    --name                     MAPS rule name
    --group-name               MAPS group on which rule is applied
    --monitoring-system        monitoring stat which we are going to monitor
    --time-base                interval of monitoring
    --logical-operator         condition of monitoring
    --threshold-value          threshold value
    --action                   action to be taken if rule violation happens

    --toggle-time              toggle time [OPTIONAL]
    --quiet-time               quiet time [OPTIONAL]
    --quiet-time-clear         clear quiet time [OPTIONAL]
    --un-quarantine-timeout    un-quarantine timeout [OPTIONAL]
    --un-quarantine-clear      clear un-quarantine [OPTIONAL]
    --event-severity           severity of the event [OPTIONAL]
    --is-rule-on-rule          set the flag for creating RoR rules [OPTIONAL]

* outputs:

    * success response or dictionary in case of error.

"""


import sys
import pyfos.pyfos_auth as pyfos_auth
import pyfos.pyfos_util as pyfos_util
from pyfos.pyfos_brocade_maps import rule
import pyfos.utils.brcd_util as brcd_util


def main(argv):

    filters = ["name", "group_name", "monitoring_system",
               "time_base", "logical_operator", "threshold_value",
               "actions_action", "toggle_time", "quiet_time",
               "quiet_time_clear", "un_quarantine_timeout",
               "un_quarantine_clear", "event_severity",
               "is_rule_on_rule"]
    inputs = brcd_util.parse(argv, rule, filters)

    rule_obj = inputs['utilobject']
    if rule_obj.peek_name() is None:
        print("Missing command line options")
        print(inputs['utilusage'])
        exit(1)

    # Login to switch
    session = brcd_util.getsession(inputs)

    result = rule_obj.post(session)
    pyfos_util.response_print(result)

    # Log out
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
