#!/usr/bin/env python3.5

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

:mod:`supportftp_modify` - PyFOS util to modify supportftp config.
********************************************************************************
The :mod:`supportftp_modify` Util is used to modify the
supportftp config used to access server for sending trace data.

This module is a stand-alone script that can be used to
modify the supportftp config in the switch.

supportftp_modify.py: Usage

* Infrastructure options:
    * -i,--ipaddr=IPADDR: IP address of FOS switch.
    * -L,--login=LOGIN: Login name.
    * -P,--password=PASSWORD: Password.
    * -f,--vfid=VFID: VFID to which the request is directed[Optional].
    * -s,--secured=MODE: HTTPS mode "self" or "CA"[Optional].
    * -v,--verbose: Verbose mode[Optional].

* Util scripts options:
    * --host=HOST: IP address or DNS name of host server
    * -u,--user-name=VALUE: User name of account in server
    * -w,--password=VALUE: Base64 encoded password of account in server
    * -d,--remote-directory=VALUE: Directory path in server
    * -a,--auto-enabled=BOOL: true/false to enable/disable auto \
transfer of data
    * -p,--protocol=VALUE: Protocol(ftp/scp/sftp) to transfer data
    * -o,--port=VALUE: Port used with scp/sftp to transfer data
    * -c,--check-interval=VALUE: Interval to check server connectivity

* Outputs:
    * Python dictionary content with RESTCONF response data.

.. function:: supportftp_modify.modify_supportftp_params(session,\
host, username, password, directory, auto, protocol, port, interval)

    *Modify parameters for server access to transfer data from switch*

        Example usage of the method::

             ret = supportftp_modify.modify_supportftp_params(session,\
host, username, password, directory, auto, protocol, port, interval)
             print (ret)

        Details::

             supportftp_obj = supportftp()
             if host is not None:
                 supportftp_obj.set_host(host)
             if username is not None:
                 supportftp_obj.set_user_name(username)
             if password is not None:
                 supportftp_obj.set_password(password)
             if directory is not None:
                 supportftp_obj.set_remote_directory(directory)
             if auto is not None:
                 supportftp_obj.set_auto_enabled(auto)
             if protocol is not None:
                 supportftp_obj.set_protocol(protocol)
             if port is not None:
                 supportftp_obj.set_port(port)
             if interval is not None:
                 supportftp_obj.\
set_connectivity_check_interval(interval)
             result = _modify_supportftp_params(
                 session, supportftp_obj)
             return result

        * Inputs:
            :param session: Session returned by login
            :param host: IPv4/IPv6 address of host server
            :param username: User name of account in server
            :param password: Base64 password of account in server
            :param directory: Directory path in server
            :param auto: true/false for enable/disable auto supportftp
            :param protocol: Protocol to transfer data
            :param port: Port used with protocol to transfer data
            :param interval: Interval to check server connectivity

        * Outputs:
            :rtype: Dictionary of return status matching rest response.

        *Use cases*

         Modify the server access parameters to transfer data from switch.
"""

import sys
import pyfos.pyfos_auth as pyfos_auth
import pyfos.pyfos_util as pyfos_util
import pyfos.utils.brcd_util as brcd_util
from pyfos.pyfos_brocade_logging import supportftp
import pyfos.pyfos_version as version


def _modify_supportftp_params(session, supportftp_obj):
    result = supportftp_obj.patch(session)
    return result


def modify_supportftp_params(session, host=None, username=None, password=None,
                             directory=None, auto=None, protocol=None,
                             interval=None):
    supportftp_obj = supportftp()
    if host is not None:
        supportftp_obj.set_host(host)
    if username is not None:
        supportftp_obj.set_user_name(username)
    if password is not None:
        supportftp_obj.set_password(password)
    if directory is not None:
        supportftp_obj.set_remote_directory(directory)
    if auto is not None:
        supportftp_obj.set_auto_enabled(auto)
    if protocol is not None:
        supportftp_obj.set_protocol(protocol)
    if port is not None:
        supportftp_obj.set_port(port)
    if interval is not None:
        supportftp_obj.set_connectivity_check_interval(interval)
    result = _modify_supportftp_params(
        session, supportftp_obj)
    return result


def validate(supportftp_obj):
    if supportftp_obj.peek_host() is None and \
           supportftp_obj.peek_user_name() is None and \
           supportftp_obj.peek_password() is None and \
           supportftp_obj.peek_remote_directory() is None and \
           supportftp_obj.peek_auto_enabled() is None and \
           supportftp_obj.peek_protocol() is None and \
           supportftp_obj.peek_port() is None and \
           supportftp_obj.peek_connectivity_check_interval() \
           is None:
        return 1
    return 0


def main(argv):
    filters = ["host", "user_name", "password", "remote_directory",
               "auto_enabled", "protocol", "port",
               "connectivity_check_interval"]
    inputs = brcd_util.parse(argv, supportftp, filters,
                             validate)
    supportftp_obj = inputs['utilobject']
    session = brcd_util.getsession(inputs)
    if session['version'] < version.fosversion("9.0.0"):
        skipattributes = ""
        if supportftp_obj.peek_host() is not None:
            skipattributes += "host"
        if supportftp_obj.peek_user_name() is not None:
            if len(skipattributes) > 0:
                skipattributes += ","
            skipattributes += "user-name"
        if supportftp_obj.peek_password() is not None:
            if len(skipattributes) > 0:
                skipattributes += ","
            skipattributes += "password"
        if supportftp_obj.peek_remote_directory() is not None:
            if len(skipattributes) > 0:
                skipattributes += ","
            skipattributes += "remote-directory"
        if supportftp_obj.peek_auto_enabled() is not None:
            if len(skipattributes) > 0:
                skipattributes += ","
            skipattributes += "auto-enabled"
        if supportftp_obj.peek_protocol() is not None:
            if len(skipattributes) > 0:
                skipattributes += ","
            skipattributes += "protocol"
        if supportftp_obj.peek_port() is not None:
            skipattributes += "port"
        if supportftp_obj.peek_connectivity_check_interval() \
           is not None:
            if len(skipattributes) > 0:
                skipattributes += ","
            skipattributes += "connectivity-check-interval"
        if len(skipattributes) > 0:
            print("Skipping following attributes:(", skipattributes,
                  ") for patch as the switch fos version[",
                  session['version'].to_string(),
                  "]is below the supported attribute version of 9.0.0")
        pyfos_auth.logout(session)
        return
    result = _modify_supportftp_params(session, supportftp_obj)
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
