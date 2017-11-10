#!/usr/bin/env python3

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

:mod:`switchgigeportstateset` - PyFOS util for setting GE port state.
***********************************************************************************
The :mod:`switchgigeportstateset` provides for specific port op use case.

This module is a standalone script that can be used to set the
switch GE port state on an extension platform.

* inputs:
    * -L=<login>: Login ID. If not provided, interactive
        prompt will request one.
    * -P=<password>: Password. If not provided, interactive
        prompt will request one.
    * -i=<IP address>: IP address
    * -n=<name>: GE port name expressed as slot/port.
    * -e=<enabled>: Enabled state of the GE port.

* outputs:
    * Python dictionary content with RESTCONF response data. 

.. function:: switchgigeportstateset.port_state_set(session, name, enabled)
    
    *Modify extension gigabitethernet state* 

        Example usage of the method::
        
            ret = switchgigeportstateset.port_state_set(session, name, enabled)
            print (ret)
                
        Details::
        
            gestate = {
                            "name": name,
                            "enabled-state": enabled,
 
                      }
            gigabitethernet = extension_gigabitethernet(gestate)
            result = gigabitethernet.patch(session)

        * inputs:
            :param session: session returned by login
            :param name: gigabitethernet port name expressed as slot/port.
            :param speed: speed for the GE port to be set.

        * outputs:    
            :rtype: dictionary of return status matching rest response

        *use cases*

        1. Modify extension gigabitethernet port state to enabled or disabled.
"""

import pyfos.pyfos_auth as pyfos_auth
import pyfos.pyfos_util as pyfos_util
from pyfos.pyfos_brocade_gigabitethernet import extension_gigabitethernet
import getpass
import getopt
import sys
import pyfos.utils.brcd_util as brcd_util

isHttps = "0"

def usage():
	print ("usage:")
	print ('switchgigeportstateset.py -i <ipaddr> -n <name> -e <enable mode in bool>')

def port_state_set(session, name, enabled):
	value_dict = {'name' : name, 'enabled-state': enabled}
	gigabitethernet = extension_gigabitethernet(value_dict)
	gigabitethernet = port.patch(session)
	return result
	
	
def main(argv):
	#myinputs = "-i 10.17.3.70 -n 4/17 -e 1"
	#argv = myinputs.split()
	inputs = brcd_util.generic_input(argv, usage)

	session = pyfos_auth.login(inputs["login"], inputs["password"],
                                   inputs["ipaddr"], isHttps)
	if pyfos_auth.is_failed_login(session):
		print ("login failed because",
		    session.get(pyfos_auth.CREDENTIAL_KEY)[pyfos_auth.LOGIN_ERROR_KEY])
		usage()
		sys.exit()

	brcd_util.exit_register(session)

	vfid = None
	if 'vfid' in inputs:
		vfid = inputs['vfid']

	if vfid is not None:
		pyfos_auth.vfid_set(session, vfid)

	if "name" not in inputs:
		pyfos_auth.logout(session)
		usage()
		sys.exit()
	name = inputs["name"]

	if "enabled" not in inputs:
		pyfos_auth.logout(session)
		usage()
		sys.exit()
	enabled = inputs["enabled"]

	port = extension_gigabitethernet()
	result = port_state_set(session, name, enabled)
	pyfos_util.response_print(result)

	pyfos_auth.logout(session)

if __name__ == "__main__": main(sys.argv[1:])
