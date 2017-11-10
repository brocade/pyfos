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

:mod:`switchgigeportspeedset` - PyFOS util for setting GE port speed.
***********************************************************************************
The :mod:`switchgigeportspeedset` provides for specific port op use case.

This module is a standalone script that can be used to set the
switch GE port speed on an extension platform.

* inputs:
    * -L=<login>: Login ID. If not provided, interactive
        prompt will request one.
    * -P=<password>: Password. If not provided, interactive
        prompt will request one.
    * -i=<IP address>: IP address
    * -n=<name>: GE port name expressed as slot/port.
    * -s=<speed>: Speed to be set for the GE port.

* outputs:
    * Python dictionary content with RESTCONF response data. 

.. function:: switchgigeportspeedset.set_port_speed(session, name, speed)
    
    *Modify extension gigabitethernet speed* 

        Example usage of the method::
        
            ret = switchgigeportspeedset.set_port_speed(session, name, speed)
            print (ret)
                
        Details::
        
                gigabitethernet = extension_gigabitethernet()
                gigabitethernet.set_name(name)
                gigabitethernet.set_speed(speed)
                        
                result = gigabitethernet.patch(session)

        * inputs:
            :param session: session returned by login
            :param name: gigabitethernet port name expressed as slot/port.
            :param speed: speed for the GE port to be set.

        * outputs:    
            :rtype: dictionary of return status matching rest response

        *use cases*

        1. Modify extension gigabitethernet port speed to 1G or 10G.
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
	print ('switchgigeportspeedset.py -i <ipaddr> -n <name> ' +\
               '-s <1000000000|10000000000|40000000000>')

def set_port_speed(session, name, speed):
	gigabitethernet = extension_gigabitethernet()
	gigabitethernet.set_name(name)
	gigabitethernet.set_speed(speed)
		
	result = gigabitethernet.patch(session)
	return (result)
	


def main(argv):
	#myinputs = "-i 10.17.3.70 -n 4/17 -s 10000000000"
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

	if "speed" not in inputs:
		pyfos_auth.logout(session)
		usage()
		sys.exit()
	speed = inputs["speed"]

	result = set_port_speed(session, name, speed)
	pyfos_util.response_print(result)
	pyfos_auth.logout(session)

if __name__ == "__main__": main(sys.argv[1:])
