#!/usr/bin/env python3.5

# Copyright 2018-2020 Brocade Communications Systems LLC.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may also obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,\
# either express or implied.
# See the License for the specific language governing permissions
# and limitations under the License.


"""

:mod:`supportlink_modify` - PyFOS util to modify supportlink config.
********************************************************************

The :mod:`supportlink_modify` Util is used to modify the
supportlink config used to access server for sending trace data.

This module is a stand-alone script that can be used to
modify the supportlink config in the switch.

supportlink_modify.py: Usage

* Input:

* Infrastructure options:

    * -i,--ipaddr=IPADDR: The IP address of the FOS switch.
    * -L,--login=LOGIN: The login name.
    * -P,--password=PASSWORD: The password.
    * -f,--vfid=VFID         The VFID to which the request is \
                             directed [OPTIONAL].
    * -s,--secured=MODE      The HTTPS mode "self" or "CA" [OPTIONAL].
    * -v,--verbose           Verbose mode [OPTIONAL].
    * -a,--authtoken: AuthToken value or AuthTokenManager config\
                      file[OPTIONAL].
    * -z,--nosession: Sessionless authentication based login[OPTIONAL].
    * --nocredential: No credential to be sent in the request[OPTIONAL].

* Util scripts options:

    * --server=SERVER: IP address or DNS name of server
    * -p,--port=VALUE: HTTPS port of server
    * -u,--user-name=VALUE: user name of account in server
    * -d,--start-date=VALUE: start date of operation
    * -t,--start-time=VALUE: start time of operation
    * -o,--end-time-period=VALUE: end time period from the start time
    * -r,--retry-time=VALUE: retry time after failure of operation
    * -i,--period=VALUE: frequency of operation
    * -c,--collection-time=VALUE: collection time
    * -g,--group-tag=VALUE: custom group tag
    * -v,--proxy-server=VALUE: IP address or DNS name of proxy server
    * -x,--proxy-port=VALUE: HTTPS port of proxy server
    * -y,--proxy-user=VALUE: user name of account in proxy server
    * -w,--proxy-password=VALUE: proxy password
    * -l,--proxy-protocol=VALUE: protocol used
    * -e,--supportlink-enabled=BOOL: supportlink feature enable/disable flag


* Output:
    * Python dictionary content with RESTCONF response data.

"""

import sys
import pyfos.pyfos_auth as pyfos_auth
import pyfos.pyfos_util as pyfos_util
import pyfos.utils.brcd_util as brcd_util
from pyfos.pyfos_brocade_supportlink import supportlink_profile


def _modify_supportlink_params(session, supportlink_obj):
    result = supportlink_obj.patch(session)
    return result


def modify_supportlink_params(session, server=None, port=None, username=None,
                              startdate=None, starttime=None,
                              endtimeperiod=None, retrytime=None,
                              period=None, collectiontime=None,
                              grouptag=None, proxyserver=None, proxyuser=None,
                              proxyport=None, proxypassword=None,
                              proxyprotocol=None, supportlinkenabled=None):
    supportlink_obj = supportlink_profile()
    if server is not None:
        supportlink_obj.set_server(server)
    if port is not None:
        supportlink_obj.set_port(port)
    if username is not None:
        supportlink_obj.set_user_name(username)
    if startdate is not None:
        supportlink_obj.set_start_date(startdate)
    if starttime is not None:
        supportlink_obj.set_start_time(starttime)
    if endtimeperiod is not None:
        supportlink_obj.set_end_time_period(endtimeperiod)
    if retrytime is not None:
        supportlink_obj.set_retry_time(retrytime)
    if period is not None:
        supportlink_obj.set_period(period)
    if collectiontime is not None:
        supportlink_obj.set_collection_time(collectiontime)
    if grouptag is not None:
        supportlink_obj.set_group_tag(grouptag)
    if proxyserver is not None:
        supportlink_obj.set_proxy_server(proxyserver)
    if proxyport is not None:
        supportlink_obj.set_proxy_port(proxyport)
    if proxyuser is not None:
        supportlink_obj.set_proxy_user(proxyuser)
    if proxypassword is not None:
        supportlink_obj.set_proxy_password(proxypassword)
    if proxyprotocol is not None:
        supportlink_obj.set_proxy_protocol(proxyprotocol)
    if supportlinkenabled is not None:
        supportlink_obj.set_supportlink_enabled(supportlinkenabled)
    result = _modify_supportlink_params(session, supportlink_obj)
    return result


def validate(supportlink_obj):
    if supportlink_obj.peek_server() is None and \
           supportlink_obj.peek_port() is None and \
           supportlink_obj.peek_user_name() is None and \
           supportlink_obj.peek_start_date() is None and \
           supportlink_obj.peek_start_time() is None and \
           supportlink_obj.peek_end_time_period() is None and \
           supportlink_obj.peek_retry_time() is None and \
           supportlink_obj.peek_period() is None and \
           supportlink_obj.peek_collection_time() is None and \
           supportlink_obj.peek_group_tag() is None and \
           supportlink_obj.peek_proxy_server() is None and \
           supportlink_obj.peek_proxy_port() is None and \
           supportlink_obj.peek_proxy_user() is None and \
           supportlink_obj.peek_proxy_password() is None and \
           supportlink_obj.peek_proxy_protocol() is None and \
           supportlink_obj.peek_supportlink_enabled() \
           is None:
        return 1
    return 0


def main(argv):
    filters = ["server", "port", "user_name", "start_date",
               "start_time", "end_time_period", "retry_time",
               "period", "collection_time", "group_tag",
               "proxy_server", "proxy_port", "proxy_user",
               "proxy_password", "proxy_protocol", "supportlink_enabled"]
    inputs = brcd_util.parse(argv, supportlink_profile, filters,
                             validate)
    supportlink_obj = inputs['utilobject']
    session = brcd_util.getsession(inputs)
    result = _modify_supportlink_params(session, supportlink_obj)
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
