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

:mod:`maps_rule_update` - PyFOS util to update an existing MAPS rule.
*******************************************************************************

This script can be used to update an existing MAPS rule.

* Input:

* Infrastructure Options:

    * -i,--ipaddr=IPADDR     The IP address of the FOS switch.
    * -L,--login=LOGIN       The login name.
    * -P,--password=PASSWORD The password.
    * -f,--vfid=VFID         The VFID to which the request is \
                             directed [OPTIONAL].
    * -s,--secured=MODE      The HTTPS mode "self" or "CA" [OPTIONAL].
    * -v,--verbose           Verbose mode [OPTIONAL].

* Util Script Options:
    --name                   Specifies the MAPS rule name.
    --group-name             Sets the MAPS group to which the rule is applied.
    --monitoring-system      Sets the monitoring statistic to be monitored.
    --time-base              Sets the interval of monitoring.
    --logical-operator       Sets the condition of monitoring.
    --threshold-value        Sets the threshold value.
    --action                 Sets the action to take if a rule \
                             violation occurs.

    --toggle-time            Sets the toggle time [OPTIONAL].
    --quiet-time             Sets the quiet time [OPTIONAL].
    --quiet-time-clear       Sets the clear quiet time [OPTIONAL].
    --un-quarantine-timeout  Sets the un-quarantine timeout [OPTIONAL].
    --un-quarantine-clear    Sets the clear un-quarantine [OPTIONAL].
    --event-severity         Sets the severity of the event [OPTIONAL].

* Output:
    * A success response or a dictionary in case of error.

"""


import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_maps import rule
from pyfos.utils import brcd_util


def main(argv):

    filters = ["name", "group_name", "monitoring_system", "time_base",
               "logical_operator", "threshold_value", "actions_action",
               "toggle_time", "quiet_time", "quiet_time_clear",
               "un_quarantine_timeout", "un_quarantine_clear",
               "event_severity"]
    inputs = brcd_util.parse(argv, rule, filters)

    rule_obj = inputs['utilobject']
    if rule_obj.peek_name() is None:
        print("Missing command line options")
        print(inputs['utilusage'])
        exit(1)

    # Login to switch
    session = brcd_util.getsession(inputs)

    result = rule_obj.patch(session)
    pyfos_util.response_print(result)

    # Log out
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
