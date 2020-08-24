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

:mod:`nport_map_del` - PyFOS util for deleting F-port to N-port mappings
***********************************************************************************
The:mod:`nport_map_del` provides option to remove the F-port to N-port mappings

This module can be used to delete F-port from N-port mappings
when the switch is in Access Gateway mode.

* inputs:

|  Infrastructure options:

  | -i,--ipaddr=IPADDR     IP address of FOS switch
  | -L,--login=LOGIN       login name.
  | -P,--password=PASSWORD password.
  | -f,--vfid=VFID         VFID to which the request is directed to [OPTIONAL].
  | -s,--secured=MODE      HTTPS mode "self" or "CA" [OPTIONAL].
  | -v,--verbose           verbose mode[OPTIONAL].

|  Util scripts options:

  | --config-f-ports=CONFIG-F-PORTS           List of mapped F-ports
  | --static-f-ports=STATIC-F-PORTS           List of statically mapped F-ports
  | --preferred-f-ports=CONFIG-F-PORTS        List of preferred mapped F-ports
  | --n-port=N-PORT                           N-Port Name

* outputs:
    * Status of the mappings delete operation

.. function:: nport_map_del.del_mapped_fports(session, nport, mfports)


    * Delete F-port from list of mapped F-port for a given N-port

        Example usage of the method::

            ret = nport_map_del.del_mapped_fports(session, nport, mfports)
            print (ret)

        Details::


            nport_obj = n_port_map()
            nport_obj.set_n_port(nport)
            if mfports is not None:
                nport_obj.set_configured_f_port_list_f_port(mfports)
            result = _del_access_gateway_nportmap(session, nport_obj)

        * inputs:
            :param session: session returned by login.
            :param N-port: N-port identifier in slot/port format.
            :param mfports: F-ports to be removed from N-port mappings.

        * outputs:
            :rtype: dictionary of return status matching rest response

        *use cases*

1.Removes specified list of F_Ports list of mapped F-ports for a given N_Port

.. function:: nport_map_del.del_static_fports(session, nport, sfports)

    * Delete F-port from list of statically mapped F-ports from a given N-port

        Example usage of the method::

            ret = nport_map_del.del_static_fports(session, nport, sfports)
            print (ret)

        Details::

            nport_obj = n_port_map()
            nport_obj.set_n_port(nport)
            if sfports is not None:
                nport_obj.set_configured_f_port_list_f_port(sfports)
            result = _add_access_gateway_nportmap(session, nport_obj)

        * inputs:
            :param session: session returned by login.
            :param N-port: N-port identifier in slot/port format.
            :param sfports: F-ports to be statically mapped to N-port.

        * outputs:
            :rtype: dictionary of return status matching rest response

        *use cases*

         1. Removes specified list of static F_Ports from \
         the mapping for a given N_Port.

.. function:: nport_map_del.del_preferred_fports(session, nport, preffports)

    * Deletes the preferred N_Port for the F_Ports

        Example usage of the method::

            ret = nport_map_del.del_preferred_fports\
(session, nport, preffports)
            print (ret)

        Details::

            nport_obj = n_port_map()
            nport_obj.set_n_port(nport)
            if preffports is not None:
                nport_obj.set_preferred_f_ports_preferred_f_port(preffports)
            result = _del_access_gateway_nportmap(session, nport_obj)

        * inputs:
            :param session: session returned by login.
            :param N-port: N-port identifier in slot/port format.
            :param preffports: F-port to be preferred to N_Port.

        * outputs:
            :rtype: dictionary of return status matching rest response

        *use cases*

         1. Deletes the preferred N_Port for the F_Ports.

"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.utils import brcd_util
from pyfos.pyfos_brocade_access_gateway import n_port_map


def _del_access_gateway_nportmap(session, restobject):
    return restobject.delete(session)


def del_mapped_fports(session, nport, mfports):
    nport_obj = n_port_map()
    nport_obj.set_n_port(nport)
    if mfports is not None:
        nport_obj.set_configured_f_port_list_f_port(mfports)
    result = _del_access_gateway_nportmap(session, nport_obj)
    return result


def del_static_fports(session, nport, sfports):
    nport_obj = n_port_map()
    nport_obj.set_n_port(nport)
    if sfports is not None:
        nport_obj.set_static_f_port_list_f_port(sfports)
    result = _del_access_gateway_nportmap(session, nport_obj)
    return result


def del_preferred_fports(session, nport, preffports):
    nport_obj = n_port_map()
    nport_obj.set_n_port(nport)
    if preffports is not None:
        nport_obj.set_preferred_f_ports_preferred_f_port(preffports)
    result = _del_access_gateway_nportmap(session, nport_obj)
    return result


def validate(nportmap_obj):
    if (nportmap_obj.peek_n_port() is None or
            (not nportmap_obj.peek_configured_f_port_list_f_port() and
             not nportmap_obj.peek_static_f_port_list_f_port() and
             not nportmap_obj.peek_preferred_f_ports_preferred_f_port())):
        return 1
    return 0


def main(argv):

    # Print arguments
    # print(sys.argv[1:])

    filters = [
        'n_port', 'configured_f_port_list_f_port',
        'static_f_port_list_f_port', 'preferred_f_ports_preferred_f_port']
    inputs = brcd_util.parse(argv, n_port_map, filters, validate)

    session = brcd_util.getsession(inputs)

    result = _del_access_gateway_nportmap(
        inputs['session'], inputs['utilobject'])
    pyfos_util.response_print(result)

    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
