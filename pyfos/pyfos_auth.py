# Copyright 2017 Brocade Communications Systems, Inc.  All rights reserved.
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

:mod:`pyfos_auth` - PyFOS module to faciliate \
        estabishing a session to FOS switch
**********************************************************************************
The :mod:`pyfos_auth` module provides functions to establish,
modify and terminate a session to FOS switch for management.
Information from the session is referenced by each subsequent calls.
Providing invalid session information will result in error.

.. note::
    Session idle timeout is set to 2 hours on FOS switch.

.. note::
    Only limited number of sessions are available. Thus proper
    termination of a session is recommended after usage.

.. note::
    A session is defaulted to Virtual Fabric ID of 128 at the time
    of login. And must be changed using :func:`vfid_set` to
    direct the subsequent requests to a given VFID.

Example usage of the module::

    session = pyfos_auth.login("myname", "mypassword", "10.10.10.10", 1)

    if pyfos_auth.is_failed_login(session):
        print("login failed because",
              session.get(pyfos_auth.CREDENTIAL_KEY)[pyfos.auth.LOGIN_ERROR_KEY])
        sys.exit()

    pyfos_auth.logout(session)

.. _error-structure-reference:

PyFOS functions generally returns generic error structure upon failure.

Generic error structure:

    +----------------+-------------------------+------------------------------+
    |Dictionary key  |Description              |Example                       |
    +================+=========================+==============================+
    |error-app-tag   |Application error tag    |Error, Info, or Warning       |
    +----------------+-------------------------+------------------------------+
    |error-info	     |Array of "error-code"    |-20			      |
    +----------------+-------------------------+------------------------------+
    |error-message   |Error message in string  |Invalid speed ...	      |
    +----------------+-------------------------+------------------------------+
    |error-path	     |URI path		       |/fibrechannel/name/0/0/speed  |
    +----------------+-------------------------+------------------------------+
    |error-tag	     |mapped to HTTP error     |Operation-failed	      |
    +----------------+-------------------------+------------------------------+
    |error-type	     |Error type	       |application or protocol       |
    +----------------+-------------------------+------------------------------+

"""

import pyfos.pyfos_login as pyfos_login
import errno
from socket import error as socket_error

LOGIN_ERROR_KEY = 'login-error'
CREDENTIAL_KEY = 'credential'


def login(username, password, ip_addr, isHttps):
    """Establish a session to FOS switch based on valid login credential

    :param username: user name to be used to establish a session
    :param password: password to be used to establish a session
    :param ip_addr: IP address of the FOS switch to establish a session with
    :param isHttps: 0 or 1 to indicate to use http or https
    :rtype: dictionary of error description
        :ref:`error-structure-reference` or session description
    """
    try:
        credential = pyfos_login.login(username, password, ip_addr,
                                       isHttps)
    except socket_error as serr:
        if serr.errno == errno.ECONNREFUSED:
            return {CREDENTIAL_KEY:
                    {LOGIN_ERROR_KEY: ip_addr + " refused connection"},
                    "ip_addr": ip_addr,
                    "vfid": 128, "ishttps": isHttps, "debug": 0}
        elif serr.errno == errno.EHOSTUNREACH:
            return {CREDENTIAL_KEY:
                    {LOGIN_ERROR_KEY: ip_addr + " not reachable"},
                    "ip_addr": ip_addr,
                    "vfid": 128, "ishttps": isHttps, "debug": 0}
        else:
            print("unknown error:", serr.errno)

    if isinstance(credential, list):
        return credential
    else:
        return {CREDENTIAL_KEY: credential, "ip_addr": ip_addr,
                "vfid": 128, "ishttps": isHttps, "debug": 0}


def logout(session):
    """Terminate a session to FOS

    :param session: dictionary of session returned by :func:`login`
    :rtype: none
    """
    return pyfos_login.logout(session.get(CREDENTIAL_KEY),
                              session.get("ip_addr"), session.get("ishttps"))


def vfid_set(session, vfid):
    """Assign a new VFDI to a session

    :param session: dictionary of session returned by :func:`login`
    :param vfid: new VFID to be assigned to the session
    :rtype: none
    """
    session['vfid'] = vfid

    return "Success"


def is_failed_login(session):
    if LOGIN_ERROR_KEY in session.get(CREDENTIAL_KEY).keys():
        return True
    else:
        False


def debug_set(session, debug):
    session['debug'] = debug

    return "Success"
