#!/usr/bin/python
# -*- coding: utf-8 -*-

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

# DOCUMENTATION, EXAMPLES, and RETURN are generated by
# ansible_specdoc. Do not edit them directly.

DOCUMENTATION = '''
author: Equinix DevRel Team (@equinix) <support@equinix.com>
description: Manage the VLAN in Equinix Metal. You can use *id* or *vxlan* to lookup
  the resource. If you want to create new resource, you must provide *metro*.
module: metal_vlan
notes: []
options:
  description:
    description:
    - Description of the VLAN
    required: false
    type: str
  id:
    description:
    - UUID of vlan"
    required: false
    type: str
  metro:
    description:
    - Metro in which to create the VLAN
    required: false
    type: str
  project_id:
    description:
    - ID of parent project"
    required: false
    type: str
  vxlan:
    description:
    - VLAN ID, must be unique in metro
    required: false
    type: int
requirements: null
short_description: Manage a VLAN resource in Equinix Metal
'''
EXAMPLES = '''
- name: Create new VLAN
  hosts: localhost
  tasks:
  - equinix.cloud.metal_vlan:
      description: This is my new VLAN.
      metro: se
      vxlan: 1234
      project_id: 778h50f7-75b6-4271-bc64-632b80f87de2
'''
RETURN = '''
metal_vlan:
  description: The module object
  returned: always
  sample:
  - "\n{\n  \"changed\": false,\n  \"id\": \"7624f0f7-75b6-4271-bc64-632b80f87de2\"\
    ,\n  \"description\": \"This is my new VLAN.\",\n  \"metro\": \"se\",\n  \"vxlan\"\
    : 1234,\n  \"project_id\": \"778h50f7-75b6-4271-bc64-632b80f87de2\"\n}\n"
  type: dict
'''

# End of generated documentation

# This is a template for a new module. It is not meant to be used as is.
# It is meant to be copied and modified to create a new module.
# Replace all occurrences of "metal_resource" with the name of the new
# module, for example "metal_vlan".


from ansible.module_utils._text import to_native
from ansible_specdoc.objects import (
    SpecField,
    FieldType,
    SpecReturnValue,
)
import traceback

from ansible_collections.equinix.cloud.plugins.module_utils.equinix import (
    EquinixModule,
    get_diff,
    getSpecDocMeta,
)

MODULE_NAME = "metal_vlan"

module_spec = dict(
    id=SpecField(
        type=FieldType.string,
        description=['UUID of vlan"'],
    ),
    project_id=SpecField(
        type=FieldType.string,
        description=['ID of parent project"'],
    ),
    description=SpecField(
        type=FieldType.string,
        description=["Description of the VLAN"],
    ),
    metro=SpecField(
        type=FieldType.string,
        description=["Metro in which to create the VLAN"],
    ),
    vxlan=SpecField(
        type=FieldType.integer,
        description=["VLAN ID, must be unique in metro"],
    ),
)


specdoc_examples = [
    """
- name: Create new VLAN
  hosts: localhost
  tasks:
  - equinix.cloud.metal_vlan:
      description: "This is my new VLAN."
      metro: "se"
      vxlan: 1234
      project_id: "778h50f7-75b6-4271-bc64-632b80f87de2"
""",
]

result_sample = [
    """
{
  "changed": false,
  "id": "7624f0f7-75b6-4271-bc64-632b80f87de2",
  "description": "This is my new VLAN.",
  "metro": "se",
  "vxlan": 1234,
  "project_id": "778h50f7-75b6-4271-bc64-632b80f87de2"
}
"""
]

MUTABLE_ATTRIBUTES = [k for k, v in module_spec.items() if v.editable]

SPECDOC_META = getSpecDocMeta(
    short_description="Manage a VLAN resource in Equinix Metal",
    description=(
        "Manage the VLAN in Equinix Metal. "
        "You can use *id* or *vxlan* to lookup the resource. "
        "If you want to create new resource, you must provide *metro*."
    ),
    examples=specdoc_examples,
    options=module_spec,
    return_values={
        "metal_vlan": SpecReturnValue(
            description="The module object",
            type=FieldType.dict,
            sample=result_sample,
        ),
    },
)


def main():
    module = EquinixModule(
        argument_spec=SPECDOC_META.ansible_spec,
    )

    state = module.params.get("state")
    changed = False
    try:
        module.params_syntax_check()
        if module.params.get("id"):
            tolerate_not_found = state == "absent"
            fetched = module.get_by_id(MODULE_NAME, tolerate_not_found)
        else:
            fetched = module.get_one_from_list(
                MODULE_NAME,
                ["vxlan"],
            )

        if fetched:
            module.params["id"] = fetched["id"]
            if state == "present":
                diff = get_diff(module.params, fetched, MUTABLE_ATTRIBUTES)
                if diff:
                    module.fail_json(msg="Resource metal_vlan is not mutable.")

            else:
                module.delete_by_id(MODULE_NAME)
                changed = True
        else:
            if state == "present":
                fetched = module.create(MODULE_NAME)
                if "id" not in fetched:
                    module.fail_json(msg="UUID not found in resource creation response")
                changed = True
            else:
                fetched = {}
    except Exception as e:
        tb = traceback.format_exc()
        module.fail_json(msg=f"Error in {MODULE_NAME}: {to_native(e)}", exception=tb)

    fetched.update({"changed": changed})
    module.exit_json(**fetched)


if __name__ == "__main__":
    main()
