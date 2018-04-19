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

:mod:`switch_config_util` - PyFOS util for specific config op use case.
***********************************************************************************
The :mod:`switch_config_util` provides for specific config op use case.

This module is utility functions for switch config scripts.

"""

import json
import time
import os
import pyfos.pyfos_util as pyfos_util


def get_dirname(ipaddr):
    return ("FOS_" + ipaddr + "_" + time.strftime("%Y_%m_%d_%H:%M:%S"))


def in_template(template, obj_name, attribute_field):
    if template is None:
        # generating a backup copy, not a template
        return True

    for obj in template:
        for k1, v1 in obj.items():
            if k1 == obj_name:
                if "all" in v1:
                    return True
                else:
                    if attribute_field in v1:
                        return True
                    else:
                        return False
    return False


def get_template(filename):
    fp = open(filename, 'r')
    template_txt = fp.read()
    template_dict = json.loads(template_txt)
    fp.close()
    return template_dict


def find_matching_attrib_entry(old_attrib, keys):
    for entry in old_attrib.value:
        found = 0
        for entry in old_attrib.value:
            for k_e, v_e in entry.items():
                for key in keys:
                    for k, v in key.items():
                        if v_e.is_key:
                            if (k_e == k) and (v_e.getuservalue() == v):
                                found += 1
            if found == len(keys):
                return entry
    return None


def process_patch_attribute_map(
        old_attrib, current_attrib, is_print_only, template):
    patch_needed = 0
    old_v = old_attrib.getuservalue()
    current_v = current_attrib.getuservalue()

    if isinstance(current_v, list):
        for entry in current_attrib.value:
            keys = []
            for k, v in entry.items():
                if v.is_key:
                    temp_dict = {}
                    temp_dict[k] = v.getuservalue()
                    keys.append(temp_dict)
            matching_old_attrib_entry = find_matching_attrib_entry(
                    old_attrib, keys)
            if matching_old_attrib_entry:
                for k, v in entry.items():
                    if not v.is_key:
                        if k in matching_old_attrib_entry:
                            if (v.getuservalue() !=
                                    matching_old_attrib_entry[k].
                                    getuservalue()):
                                print(
                                        "\t", current_attrib.name, keys,
                                        "drifted from",
                                        matching_old_attrib_entry[k].
                                        getuservalue(),
                                        "to", v.getuservalue())
                                if not is_print_only:
                                    patch_needed += 1
                                    v.setuservalue(
                                            matching_old_attrib_entry[k].
                                            getuservalue())
    elif isinstance(current_v, dict):
        if not (old_attrib.is_empty() and current_attrib.is_empty()):
            if old_v != current_v:
                if current_attrib.is_config:
                    print(
                            "\t", current_attrib.name, "drifted from",
                            old_v, "to", current_v)
                    if not is_print_only:
                        patch_needed += 1
                        current_attrib.setuservalue(old_v)
                else:
                    print(
                            "\t(RO)", current_attrib.name, "drifted from",
                            old_v, "to", current_v)
    else:
        print("unknown")

    return patch_needed


def process_post_attribute_map(
        old_attrib, current_attrib, is_print_only, template):
    post_needed = 0
    old_v = old_attrib.getuservalue()
    current_v = current_attrib.getuservalue()

    if isinstance(old_v, list):
        index = 0
        for entry in old_attrib.value:
            keys = []
            for k, v in entry.items():
                if v.is_key:
                    temp_dict = {}
                    temp_dict[k] = v.getuservalue()
                    keys.append(temp_dict)

            matching_current_attrib_entry = find_matching_attrib_entry(
                    current_attrib, keys)
            if not matching_current_attrib_entry:
                print(
                        "\t", current_attrib.name, keys,
                        "removed. Old value", old_v[index])
                if not is_print_only:
                    post_needed += 1
                    current_attrib.value.append(entry)
            else:
                current_attrib.value.remove(matching_current_attrib_entry)
            index += 1
    elif isinstance(current_v, dict):
        if not old_attrib.is_empty() and current_attrib.is_empty():
            if current_attrib.is_config:
                print(
                        "\t", current_attrib.name, "removed. Old value",
                        old_v)
                if not is_print_only:
                    post_needed += 1
                    current_attrib.setuservalue(old_v)
            else:
                print(
                        "\t(RO)", current_attrib.name, "removed. Old value",
                        old_v)
    else:
        print("unknown")

    return post_needed


def process_delete_attribute_map(
        old_attrib, current_attrib, is_print_only, template):
    delete_needed = 0
    old_v = old_attrib.getuservalue()
    current_v = current_attrib.getuservalue()

    ret_keys = []

    if isinstance(current_v, list):
        index = 0
        for entry in current_attrib.value:
            keys = []
            for k, v in entry.items():
                if v.is_key:
                    temp_dict = {}
                    temp_dict[k] = v.getuservalue()
                    keys.append(temp_dict)

            matching_old_attrib_entry = find_matching_attrib_entry(
                    old_attrib, keys)
            if not matching_old_attrib_entry:
                print(
                        "\t", current_attrib.name, keys,
                        "Added. New value", current_v[index])
                if not is_print_only:
                    delete_needed += 1
                    for key in keys:
                        ret_keys.append(key)
            index += 1
    elif isinstance(current_v, dict):
        if not current_attrib.is_empty() and old_attrib.is_empty():
            if old_attrib.is_config:
                print(
                        "\t", old_attrib.name, "Added. New value",
                        current_v)
                if not is_print_only:
                    delete_needed += 1
                    current_attrib.setuservalue(old_v)
            else:
                print(
                        "\t(RO)", old_attrib.name, "Added. New value",
                        current_v)
    else:
        print("unknown")

    return delete_needed, ret_keys


def process_patch(old_object, current_object, is_print_only, template):
    keys = {}
    for k, v in current_object.attributes_dict.items():
        if v.is_key:
            keys[k] = v.getuservalue()

    print(
            "processing entries that changed",
            current_object.getcontainer(), keys)

    patch_needed = 0

    for k, v in current_object.attributes_dict.items():
        if v.is_key:
            # if the attribute is a key, no need to touch that
            continue
        elif v.is_attribute_map:
            local_patch_need = process_patch_attribute_map(
                    old_object.getattribute(k), v, is_print_only, template)
            patch_needed += local_patch_need
            continue
        elif v.is_list:
            print("deal with list later")
            continue
        elif v.is_leaf:
            if (template is not None and
                    not in_template(
                        template, current_object.getcontainer(), k)):
                continue

            if old_object.getattribute(k).getuservalue() != v.getuservalue():
                if v.is_config:
                    patch_needed += 1
                    print(
                            "\t", k, "drifted from",
                            old_object.getattribute(k).getuservalue(),
                            "to", v.getuservalue())
                    if not is_print_only:
                        v.setuservalue(
                                old_object.getattribute(k).getuservalue())
                else:
                    print(
                            "\t(RO)", k, "drifted from",
                            old_object.getattribute(k).getuservalue(),
                            "to", v.getuservalue())

    if patch_needed > 0:
        return True


def process_post(old_object, current_object, is_print_only, template):
    keys = {}
    for k, v in current_object.attributes_dict.items():
        if v.is_key:
            keys[k] = v.getuservalue()

    print(
            "processing entries requiring creation",
            current_object.getcontainer(), keys)

    post_needed = 0

    for k, v in current_object.attributes_dict.items():
        if v.is_key:
            # if the attribute is a key, no need to touch that
            continue
        elif v.is_attribute_map:
            local_post_need = process_post_attribute_map(
                    old_object.getattribute(k), v, is_print_only, template)
            post_needed += local_post_need
            continue
        elif v.is_list:
            print("deal with list later")
            continue
        elif v.is_leaf:
            # if both objects are there, this should be handled in patch
            continue

    if post_needed > 0:
        return True


def process_delete(
        old_object, current_object, delete_object, is_print_only, template):
    keys = {}
    for k, v in current_object.attributes_dict.items():
        if v.is_key:
            keys[k] = v.getuservalue()

    print(
            "processing entries requiring deletion",
            current_object.getcontainer(), keys)

    delete_needed = 0

    for k, v in current_object.attributes_dict.items():
        if v.is_key:
            # if the attribute is a key, no need to touch that
            continue
        elif v.is_attribute_map:
            local_delete_need, keys = process_delete_attribute_map(
                    old_object.getattribute(k), v, is_print_only, template)
            if local_delete_need:
                setfunc = getattr(delete_object, "set_" + k.lower())
                setfunc(keys)
                delete_needed += local_delete_need
            continue
        elif v.is_list:
            print("deal with list later")
            continue
        elif v.is_leaf:
            # if both objects are there, this should be handled in patch
            continue

    if delete_needed > 0:
        return True


def find_matching_object(fos_object, old_object, refkeys):
    keys = []
    for k, v in fos_object.attributes_dict.items():
        if v.is_key:
            keys.append(k)

    if isinstance(old_object, list):
        # this should not be. If I have a list, there should be a key
        if len(keys) == 0:
            return None

        for obj in old_object:
            found = 0
            if refkeys is not None:
                for refkey in refkeys:
                    for k, v in refkey.items():
                        if obj.getattribute(k).getuservalue() == v:
                            found += 1
            else:
                for key in keys:
                    if (obj.getattribute(key).getuservalue() ==
                            fos_object.getattribute(key).getuservalue()):
                        found += 1
            if found == len(keys):
                return obj

        return None

    else:
        # if there are no keys associated here, just return
        # the single object
        if len(keys) == 0:
            return old_object

        found = 0
        if refkeys is not None:
            for refkey in refkeys:
                for k, v in refkey.items():
                    if obj.getattribute(k).getuservalue() == v:
                        found += 1
        else:
            for key in keys:
                if (old_object.getattribute(key).getuservalue() ==
                        fos_object.getattribute(key).getuservalue()):
                    found += 1

        if found == len(keys):
            return old_object
        else:
            return None


def obj_to_short_str(fos_object):
    values = []
    for k, v in fos_object.attributes_dict.items():
        if v.is_key:
            values.append(v)

    return type(fos_object).__name__ + str(values)


def process_object(
        session, dir_name, pyfos_class,
        is_print_only, template, refkeys=None):
    # get the current object
    fos_object = pyfos_class.get(session)
    if pyfos_util.is_failed_resp(fos_object):
        print("cannot retrieve", pyfos_class.__name__)
        return

    # get the old object
    file_name = dir_name + "/" + pyfos_class.__name__
    try:
        os.stat(file_name)
    except OSError:
        print(file_name, "doesn't exist. Skipping")
        return

    fp = open(file_name, 'r')
    old_dict = json.load(fp)
    fp.close()

    old_object = None
    if isinstance(old_dict, list):
        old_object = []
        for old_entry in old_dict:
            old_entry_obj = pyfos_class()
            old_entry_obj.load(old_entry[pyfos_class().getcontainer()])
            old_object.append(old_entry_obj)
    else:
        old_object = pyfos_class()
        old_object.load(old_dict[pyfos_class().getcontainer()])

        # if isinstance(old_object, list):
        #   for obj in old_object:
        #       print(json.dumps(obj,
        #           cls=pyfos_rest_util.rest_object_encoder,
        #           sort_keys=True, indent=4))
        # else:
        #   print(json.dumps(old_object,
        #           cls=pyfos_rest_util.rest_object_encoder,
        #           sort_keys=True, indent=4))

    if isinstance(fos_object, list):
        for obj in fos_object:
            old_matching_object = find_matching_object(
                    obj, old_object, refkeys)
            if old_matching_object is None:
                print("didn't find a matching old object",
                        obj_to_short_str(obj))
            else:
                # print("compare")
                # print(json.dumps(obj,
                # cls=pyfos_rest_util.rest_object_encoder,
                # sort_keys=True, indent=4))
                # print(json.dumps(old_matching_object,
                # cls=pyfos_rest_util.rest_object_encoder,
                # sort_keys=True, indent=4))
                need_patching = process_patch(
                        old_matching_object, obj, is_print_only, template)
                if not is_print_only and need_patching:
                    result = obj.patch(session)
                    if ('success-type' in result and
                            result['success-type'] == 'Success'):
                        print("\tpatch success")
                    else:
                        print("\tpatch failed", result)
    else:
        old_matching_object = find_matching_object(
                fos_object, old_object, refkeys)
        if old_matching_object is None:
            print("didn't find a matching old object",
                    obj_to_short_str(fos_object))
        else:

            # print("compare")
            # print(json.dumps(fos_object,
            #       cls=pyfos_rest_util.rest_object_encoder,
            #       sort_keys=True, indent=4))
            # print(json.dumps(old_matching_object,
            #       cls=pyfos_rest_util.rest_object_encoder,
            #       sort_keys=True, indent=4))
            need_patching = process_patch(
                    old_matching_object, fos_object, is_print_only, template)
            if not is_print_only and need_patching:
            # print(fos_object.create_html_content(pyfos_rest_util.rest_get_method.GET_KEY_AND_MODIFIED_CONFIG))
                result = fos_object.patch(session)
                if ('success-type' in result and
                        result['success-type'] == 'Success'):
                    print("\tpatch success")
                else:
                    print("\tpatch failed", result)

            need_posting = process_post(
                    old_matching_object, fos_object, is_print_only, template)
            if not is_print_only and need_posting:
                # print(fos_object.create_html_content())
                result = fos_object.post(session)
                if ('success-type' in result and
                        result['success-type'] == 'Success'):
                    print("\tpost success")
                else:
                    print("\tpost failed", result)

            delete_object = pyfos_class()
            need_deleting = process_delete(
                    old_matching_object, fos_object,
                    delete_object, is_print_only, template)
            if not is_print_only and need_deleting:
                # print(delete_object.create_html_content())
                result = delete_object.delete(session)
                if ('success-type' in result and
                        result['success-type'] == 'Success'):
                    print("\tdelete success")
                else:
                    print("\tdelete failed", result)
