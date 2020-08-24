#!/usr/bin/env python3


# Copyright © 2019 Broadcom. All rights reserved.
# The term “Broadcom” refers to Broadcom Inc. and/or its subsidiaries.
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


# lldp_stats_show.py(pyGen v1.0.0)


"""

:mod:`lldp_stats_show` - PyFOS util to show for lldp_statistics
*******************************************************************************
The :mod:`lldp_stats_show` PyFOS util to show for lldp_statistics


The LLDP protocol specific Tx, Rx and Error statistics of the port/s.

lldp_stats_show : usage

* Infrastructure Options:
    * -i,--ipaddr=IPADDR: The IP address of the FOS switch.
    * -L,--login=LOGIN: The login name.
    * -P,--password=PASSWORD: The password.
    * -f,--vfid=VFID: The VFID to which the request is directed.
    * -s,--secured=MODE: The HTTPS mode "self" or "CA" [Optional].
    * -v,--verbose: Verbose mode [Optional].

* Util Script Options:
    * --slot-port=SLOT-PORT Port name.
    * --frames-discarded=FRAMES-DISCARDED The number of LLDP discarded frames.
    * --in-frames=IN-FRAMES The number of LLDP In frames.
    * --frames-aged-out=FRAMES-AGED-OUT The number of LLDP aged out frames.
    * --tlv-unrecognized=TLV-UNRECOGNIZED The number of unrecognized LLDP\
      TLVs.
    * --tlv-discarded=TLV-DISCARDED The number of discarded LLDP TLVs.
    * --out-frames=OUT-FRAMES The number of LLDP out frames.
    * --error-frames=ERROR-FRAMES The number of LLDP error frames
* Output:
    * Python dictionary content with RESTCONF response data.


.. function:: lldp_stats_show.show_lldp_statistics(session, slot_port,\
frames_discarded, in_frames, frames_aged_out, tlv_unrecognized,\
tlv_discarded, out_frames, error_frames)

    *Show lldp_statistics*

        Example Usage of the Method::

            ret = lldp_stats_show.show_lldp_statistics(session, slot_port,\
            frames_discarded, in_frames, frames_aged_out, tlv_unrecognized,\
            tlv_discarded, out_frames, error_frames)
            print (ret)

        Details::

            lldp_statisticsObj = lldp_statistics()
            lldp_statisticsObj.set_slot_port(slot_port)
            lldp_statisticsObj.set_frames_discarded(frames_discarded)
            lldp_statisticsObj.set_in_frames(in_frames)
            lldp_statisticsObj.set_frames_aged_out(frames_aged_out)
            lldp_statisticsObj.set_tlv_unrecognized(tlv_unrecognized)
            lldp_statisticsObj.set_tlv_discarded(tlv_discarded)
            lldp_statisticsObj.set_out_frames(out_frames)
            lldp_statisticsObj.set_error_frames(error_frames)
            print (ret)

        * Input::

            :param session: The session returned by the login.
            :param slot_port: Port name.
            :param frames_discarded: The number of LLDP discarded frames.
            :param in_frames: The number of LLDP In frames.
            :param frames_aged_out: The number of LLDP aged out frames.
            :param tlv_unrecognized: The number of unrecognized LLDP TLVs.
            :param tlv_discarded: The number of discarded LLDP TLVs.
            :param out_frames: The number of LLDP out frames.
            :param error_frames: The number of LLDP error frames

        * Output:

            :rtype: None or more instance of class lldp_statistics on Success \
            or a dictionary with error.

"""


# Start utils imports
import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_lldp import lldp_statistics
from pyfos.utils import brcd_util
# End module imports


def _show_lldp_statistics(session, lldp_statisticsObj):
    objlist = lldp_statistics.get(session)
    lldp_statisticslist = list()
    if isinstance(objlist, lldp_statistics):
        objlist = [objlist]
    if isinstance(objlist, list):
        for i in range(len(objlist)):
            if lldp_statisticsObj.peek_slot_port() is not None and\
               lldp_statisticsObj.peek_slot_port() !=\
               objlist[i].peek_slot_port():
                continue
            if lldp_statisticsObj.peek_frames_discarded() is not None and\
               lldp_statisticsObj.peek_frames_discarded() !=\
               objlist[i].peek_frames_discarded():
                continue
            if lldp_statisticsObj.peek_in_frames() is not None and\
               lldp_statisticsObj.peek_in_frames() !=\
               objlist[i].peek_in_frames():
                continue
            if lldp_statisticsObj.peek_frames_aged_out() is not None and\
               lldp_statisticsObj.peek_frames_aged_out() !=\
               objlist[i].peek_frames_aged_out():
                continue
            if lldp_statisticsObj.peek_tlv_unrecognized() is not None and\
               lldp_statisticsObj.peek_tlv_unrecognized() !=\
               objlist[i].peek_tlv_unrecognized():
                continue
            if lldp_statisticsObj.peek_tlv_discarded() is not None and\
               lldp_statisticsObj.peek_tlv_discarded() !=\
               objlist[i].peek_tlv_discarded():
                continue
            if lldp_statisticsObj.peek_out_frames() is not None and\
               lldp_statisticsObj.peek_out_frames() !=\
               objlist[i].peek_out_frames():
                continue
            if lldp_statisticsObj.peek_error_frames() is not None and\
               lldp_statisticsObj.peek_error_frames() !=\
               objlist[i].peek_error_frames():
                continue
            lldp_statisticslist.append(objlist[i])
    else:
        print(objlist)
    return lldp_statisticslist


def show_lldp_statistics(session, slot_port=None, frames_discarded=None,
                         in_frames=None, frames_aged_out=None,
                         tlv_unrecognized=None, tlv_discarded=None,
                         out_frames=None, error_frames=None):
    lldp_statisticsObj = lldp_statistics()
    lldp_statisticsObj.set_slot_port(slot_port)
    lldp_statisticsObj.set_frames_discarded(frames_discarded)
    lldp_statisticsObj.set_in_frames(in_frames)
    lldp_statisticsObj.set_frames_aged_out(frames_aged_out)
    lldp_statisticsObj.set_tlv_unrecognized(tlv_unrecognized)
    lldp_statisticsObj.set_tlv_discarded(tlv_discarded)
    lldp_statisticsObj.set_out_frames(out_frames)
    lldp_statisticsObj.set_error_frames(error_frames)
    return _show_lldp_statistics(session, lldp_statisticsObj)


def validate(lldp_statisticsObj):
    if lldp_statisticsObj.peek_slot_port() is None or\
       lldp_statisticsObj.peek_frames_discarded() is None or\
       lldp_statisticsObj.peek_in_frames() is None or\
       lldp_statisticsObj.peek_frames_aged_out() is None or\
       lldp_statisticsObj.peek_tlv_unrecognized() is None or\
       lldp_statisticsObj.peek_tlv_discarded() is None or\
       lldp_statisticsObj.peek_out_frames() is None or\
       lldp_statisticsObj.peek_error_frames() is None:
        return 0
    return 0


def main(argv):
    filters = ["slot_port", "frames_discarded", "in_frames",
               "frames_aged_out", "tlv_unrecognized", "tlv_discarded",
               "out_frames", "error_frames"]
    inputs = brcd_util.parse(argv, lldp_statistics, filters, validate)
    session = brcd_util.getsession(inputs)
    result = _show_lldp_statistics(session, inputs['utilobject'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
