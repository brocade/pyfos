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

:mod:`pyfos_version` - PyFOS module  to provide versioning functionality \
        for rest classes and attributes.
**********************************************************************************
The :mod:`pyfos_version`  Provides the versioning support for REST
supported classes.

"""


def compareRelease(lhs, rhs):
    if lhs == '*' or rhs == '*':
        return 0
    return (relvalue(lhs) - relvalue(rhs))


def relvalue(rel):
    if rel == 'x':
        return -1
    elif rel == 'a':
        return 1
    elif rel == 'b':
        return 2
    elif rel == 'c':
        return 3
    elif rel == 'd':
        return 4
    elif rel == 'e':
        return 5
    elif rel == 'f':
        return 6
    elif rel == 'g':
        return 7
    elif rel == '*':
        return 0
    else:
        return 0


class fosversion():
    """
    class for version support for the rest object and attributes.
    """
    def __init__(self, ver_string="8.2.0"):
        fwversion = ver_string.split(".")
        if len(fwversion) > 4:
            mylist = []
            mylist.append(fwversion[0].replace("v", ""))
            mylist.append(fwversion[1])
            ver_patch = fwversion[2]
            length = len(ver_patch)
            release = "*"
            patch = ver_patch[0]
            mylist.append(patch)
            mylist.append(release)
            self.setvalue(int(mylist[0]), int(mylist[1]), int(mylist[2]),
                          mylist[3])
        else:
            mylist = self.from_string(ver_string)
            if len(mylist) == 4:
                mylist[0].replace("v", "")
                self.setvalue(int(mylist[0]), int(mylist[1]),
                              int(mylist[2]), mylist[3])

    def setvalue(self, ver_major=8, ver_minor=2, ver_patch=0, ver_release=""):
        self.major = ver_major
        self.minor = ver_minor
        self.patch = ver_patch
        if ver_release == "x" or \
           ver_release == "a" or \
           ver_release == "b" or \
           ver_release == "c" or \
           ver_release == "d" or \
           ver_release == "e" or \
           ver_release == "f" or \
           ver_release == "*" or \
           ver_release == "g":
            self.release = ver_release
        else:
            self.release = "x"

    def to_string(self):
        mylist = [str(self.major), str(self.minor), str(self.patch)]
        return(".".join(mylist) + self.release)

    def from_string(self, version_string):
        fwversion = version_string.split(".")
        if (len(fwversion)) >= 3:
            ver_patch = fwversion[2]
            length = len(ver_patch)
            if len(fwversion) > 3:
                release = "*"
            else:
                release = "x"
            patch = ver_patch[0]
            if length >= 2:
                if release == 'x':
                    release = ver_patch[1]
        else:
            return []
        mylist = []
        mylist.append(fwversion[0].replace("v", ""))
        mylist.append(fwversion[1])
        mylist.append(patch)
        mylist.append(release)
        self.setvalue(int(mylist[0]), int(mylist[1]), int(mylist[2]),
                      mylist[3])
        return mylist

    def __lt__(self, rhs):
        if isinstance(rhs, fosversion):
            if self.major < rhs.major:
                return True
            elif (self.major == rhs.major) and (self.minor < rhs.minor):
                return True
            elif (self.major == rhs.major) and (self.minor == rhs.minor)\
                    and (self.patch < rhs.patch):
                return True
            elif (self.major == rhs.major) and (self.minor == rhs.minor)\
                    and (self.patch == rhs.patch)\
                    and compareRelease(self.release, rhs.release) < 0:
                return True
        return False

    def __le__(self, rhs):
        if isinstance(rhs, fosversion):
            if self.major < rhs.major:
                return True
            elif (self.major == rhs.major) and (self.minor < rhs.minor):
                return True
            elif (self.major == rhs.major) and (self.minor == rhs.minor)\
                    and (self.patch < rhs.patch):
                return True
            elif (self.major == rhs.major) and (self.minor == rhs.minor)\
                    and (self.patch == rhs.patch)\
                    and compareRelease(self.release, rhs.release) < 0:
                return True
            elif (self.major == rhs.major) and (self.minor == rhs.minor)\
                    and (self.patch == rhs.patch)\
                    and compareRelease(self.release, rhs.release) <= 0:
                return True
        return False

    def __gt__(self, rhs):
        if isinstance(rhs, fosversion):
            if self.major > rhs.major:
                return True
            elif (self.major == rhs.major) and (self.minor > rhs.minor):
                return True
            elif (self.major == rhs.major) and (self.minor == rhs.minor)\
                    and (self.patch > rhs.patch):
                return True
            elif (self.major == rhs.major) and (self.minor == rhs.minor)\
                    and (self.patch == rhs.patch)\
                    and compareRelease(self.release, rhs.release) > 0:
                return True
        return False

    def __ge__(self, rhs):
        if isinstance(rhs, fosversion):
            if self.major > rhs.major:
                return True
            elif (self.major == rhs.major) and (self.minor > rhs.minor):
                return True
            elif (self.major == rhs.major) and (self.minor == rhs.minor)\
                    and (self.patch > rhs.patch):
                return True
            elif (self.major == rhs.major) and (self.minor == rhs.minor)\
                    and (self.patch == rhs.patch):
                return True
            elif (self.major == rhs.major) and (self.minor == rhs.minor)\
                    and (self.patch == rhs.patch)\
                    and compareRelease(self.release, rhs.release) > 0:
                return True
            elif (self.major == rhs.major) and (self.minor == rhs.minor)\
                    and (self.patch == rhs.patch)\
                    and compareRelease(self.release, rhs.release) >= 0:
                return True
        return False

    def __eq__(self, rhs):
        if isinstance(rhs, fosversion):
            if (self.major == rhs.major) and (self.minor == rhs.minor)\
                   and (self.patch == rhs.patch):
                return True
        return False

    def __ne__(self, rhs):
        if isinstance(rhs, fosversion):
            if (self.major != rhs.major) or (self.minor != rhs.minor)\
                   or (self.patch != rhs.patch)\
                   or compareRelease(self.release, rhs.release) != 0:
                return True
        return False


class fosversion_range():
    """
    class for version range support for the rest object and attributes.
    """
    def __init__(self, version_dict):
        self.start = fosversion(version_dict['START'])
        if 'END' in version_dict.keys():
            self.end = fosversion(version_dict['END'])
        else:
            self.end = fosversion("9999.9999.9")

    def to_string(self):
        retdict = dict()
        retdict.update({'START': self.start.to_string()})
        retdict.update({'END': self.end.to_string()})
        return retdict

    def from_string(self, retdict):
        self.start.from_string(retdict['START'])
        self.end.from_string(retdict['END'])

    def visible(self, version):
        if self.start <= version and self.end >= version:
            return True
        return False

    def __lt__(self, rhs):
        if isinstance(rhs, fosversion_range):
            if self.start <= rhs.start and self.end >= rhs.end:
                return True
        return False


VER_820 = "8.2.0"
VER_RANGE_820_ABOVE = {'START': "8.2.0", 'END': "9999.9999.9"}
VER_RANGE_820_PATCH_A = {'START': "8.2.0", 'END': "8.2.0a"}
VER_RANGE_820a_and_ABOVE = {'START': "8.2.0a", 'END': "9999.9999.9"}

