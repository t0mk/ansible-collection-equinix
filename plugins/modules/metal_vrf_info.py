#!/usr/bin/python
# -*- coding: utf-8 -*-

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

# DOCUMENTATION, EXAMPLES, and RETURN are generated by
# ansible_specdoc. Do not edit them directly.

DOCUMENTATION = '''
author: Equinix DevRel Team (@equinix) <support@equinix.com>
description: Gather information about Equinix VRFs
module: metal_vrf_info
notes: []
options:
  project_id:
    description:
    - Project ID where to look up VRFs.
    required: true
    type: str
  vrf_id:
    description:
    - ID of the VRF resource
    required: false
    type: str
requirements: null
short_description: Gather VRFs
'''
EXAMPLES = '''
- name: Gather information about VRFs in a project
  hosts: localhost
  tasks:
  - equinix.cloud.metal_vrf_info:
      project_id: 2a5122b9-c323-4d5c-b53c-9ad3f54273e7
- name: Retrieve information about resources within a specific VRF
  hosts: localhost
  tasks:
  - equinix.cloud.metal_vrf_info:
      project_id: 2a5122b9-c323-4d5c-b53c-9ad3f54273e7
      vrf_id: f421024d-c1e6-4886-a64d-5b2515696200
'''
RETURN = '''
resources:
  description: Found resources
  returned: always
  sample:
  - "\n\n[\n        {\n            \"description\": \"Test VRF with ASN 65000\",\n\
    \            \"id\": \"8b24de5b-c70e-4a4e-9dd2-064ceb09c587\",\n            \"\
    ip_ranges\": [\n                \"192.168.100.0/25\",\n                \"192.168.200.0/25\"\
    \n            ],\n            \"local_asn\": 65000,\n            \"metro\": {\n\
    \                \"href\": \"/metal/v1/locations/metros/108b2cfb-246b-45e3-885a-bf3e82fce1a0\"\
    ,\n                \"id\": \"108b2cfb-246b-45e3-885a-bf3e82fce1a0\"\n        \
    \    },\n            \"name\": \"ansible-integration-test-vrf-nw6dgvh5\",\n  \
    \          \"project_id\": \"06aea391-fd87-4cc7-9f4b-76f9e38fd4a4\"\n        }\n\
    \    ]"
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
        description=['Project ID where to look up VRFs.'],
        required=True
    ),
    vrf_id=SpecField(
        type=FieldType.string,
        description=['ID of the VRF resource'],
    ),
)

specdoc_examples = ['''
- name: Gather information about VRFs in a project
  hosts: localhost
  tasks:
      - equinix.cloud.metal_vrf_info:
          project_id: 2a5122b9-c323-4d5c-b53c-9ad3f54273e7
''', '''
- name: Retrieve information about resources within a specific VRF
  hosts: localhost
  tasks:
      - equinix.cloud.metal_vrf_info:
          project_id: 2a5122b9-c323-4d5c-b53c-9ad3f54273e7
          vrf_id: f421024d-c1e6-4886-a64d-5b2515696200
''',
                    ]

result_sample = ['''

[
        {
            "description": "Test VRF with ASN 65000",
            "id": "8b24de5b-c70e-4a4e-9dd2-064ceb09c587",
            "ip_ranges": [
                "192.168.100.0/25",
                "192.168.200.0/25"
            ],
            "local_asn": 65000,
            "metro": {
                "href": "/metal/v1/locations/metros/108b2cfb-246b-45e3-885a-bf3e82fce1a0",
                "id": "108b2cfb-246b-45e3-885a-bf3e82fce1a0"
            },
            "name": "ansible-integration-test-vrf-nw6dgvh5",
            "project_id": "06aea391-fd87-4cc7-9f4b-76f9e38fd4a4"
        }
    ]''',
]

SPECDOC_META = getSpecDocMeta(
    short_description="Gather VRFs",
    description=(
        'Gather information about Equinix VRFs'
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
        required_one_of=[('project_id', 'vrf_id')],
        supports_check_mode=True,
        is_info=True,
    )
    try:
        module.params_syntax_check()
        return_value = {'resources': module.get_list("metal_vrf")}
    except Exception as e:
        tr = traceback.format_exc()
        module.fail_json(msg=to_native(e), exception=tr)
    module.exit_json(**return_value)


if __name__ == '__main__':
    main()
