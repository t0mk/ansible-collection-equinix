#!/usr/bin/python
# -*- coding: utf-8 -*-

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

# DOCUMENTATION, EXAMPLES, and RETURN are generated by
# ansible_specdoc. Do not edit them directly.

DOCUMENTATION = '''
author: Equinix DevRel Team (@equinix) <support@equinix.com>
description: Gather information about Equinix Metal VLAN resources
module: metal_vlan_info
notes: []
options:
  project_id:
    description:
    - Filter vlans by Project UUID.
    required: false
    type: str
requirements: null
short_description: Gather VLANs.
'''
EXAMPLES = '''
- name: list vlans
  equinix.cloud.metal_vlan_info: null
  register: listed_vlan
'''
RETURN = '''
resources:
  description: Found resources
  returned: always
  sample:
  - "\n[\n  {\n    \"vxlan\": 1234,\n    \"metro\": \"se\",\n    \"id\": \"845b45a3-c565-47e5-b9b6-a86204a73d29\"\
    ,\n    \"description\": \"My VLAN\"\n  }\n]"
  type: dict
'''

# End

from ansible.module_utils._text import to_native
from ansible_specdoc.objects import SpecField, FieldType, SpecReturnValue
import traceback

from ansible_collections.equinix.cloud.plugins.module_utils.equinix import (
    EquinixModule,
    getSpecDocMeta,
)

module_spec = dict(
    project_id=SpecField(
        type=FieldType.string,
        description=['Filter vlans by Project UUID.'],
        required=False,
    ),
)

specdoc_examples = ['''
- name: list vlans
  equinix.cloud.metal_vlan_info:
  register: listed_vlan
''',
]

result_sample = ['''
[
  {
    "vxlan": 1234,
    "metro": "se",
    "id": "845b45a3-c565-47e5-b9b6-a86204a73d29",
    "description": "My VLAN"
  }
]''',
]

SPECDOC_META = getSpecDocMeta(
    short_description="Gather VLANs.",
    description=(
        'Gather information about Equinix Metal VLAN resources'
    ),
    examples=specdoc_examples,
    options=module_spec,
    return_values={
        "resources": SpecReturnValue(
            description='Found resources',
            type=FieldType.dict,
            sample=result_sample,
        ),
    },
)


def main():
    module = EquinixModule(
        argument_spec=SPECDOC_META.ansible_spec,
        is_info=True,
    )
    try:
        module.params_syntax_check()
        return_value = {'resources': module.get_list("metal_vlan")}
    except Exception as e:
        tr = traceback.format_exc()
        module.fail_json(msg=to_native(e), exception=tr)
    module.exit_json(**return_value)


if __name__ == '__main__':
    main()
