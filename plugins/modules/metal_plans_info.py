#!/usr/bin/python
# -*- coding: utf-8 -*-

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

# DOCUMENTATION, EXAMPLES, and RETURN are generated by
# ansible_specdoc. Do not edit them directly.

DOCUMENTATION = '''
author: Equinix DevRel Team (@equinix) <support@equinix.com>
description: Gather information about Equinix Metal plans
module: metal_plans_info
notes: []
options:
  categories:
    description:
    - Filter plans by its categories.
    required: false
    type: list
  exclude:
    description:
    - Nested attributes to exclude.
    - Excluded objects will return only the href attribute.
    - Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    required: false
    type: list
  include:
    description:
    - Nested attributes to include.
    - Included objects will return their full attributes.
    - Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    required: false
    type: list
  organization_id:
    description:
    - UUID of the organization containing the plan.
    required: false
    type: str
  project_id:
    description:
    - ID of the project where the plan is scoped to.
    required: false
    type: str
  slug:
    description:
    - Filter plans by slug.
    required: false
    type: str
  type:
    description:
    - Filter plans by its plan type.
    required: false
    type: str
requirements: null
short_description: Gather information about Equinix Metal plans
'''
EXAMPLES = '''
- name: Gather information about all plans
  hosts: localhost
  tasks:
  - equinix.cloud.metal_plans_info
- name: Gather information for plans starting with c3.medium
  hosts: localhost
  tasks:
  - equinix.cloud.metal_plans_info:
      slug: c3.medium
'''
RETURN = '''
resources:
  description: Found resources
  returned: always
  sample:
  - "\n\n[  \n  {                                                                \
    \           \n    \"changed\": false,                                        \
    \                                 \n    \"resources\": [                     \
    \                                                                            \
    \                                                   \n      {                \
    \                                                                     \n     \
    \   \"available_in\": [],                                                    \
    \                                                                            \
    \                       \n        \"available_in_metros\": [],\n        \"category\"\
    : [\n          \"compute\",\n          \"current_gen\"\n        ],\n        \"\
    class\": \"a3.large.opt-m3a2\",\n        \"deployment_types\": [],\n        \"\
    description\": \"a3.large.opt-m3a2.x86\",\n        \"id\": \"8c04950a-87ab-5e52-a112-5a90bbca8868\"\
    ,\n        \"legacy\": false,\n        \"line\": \"baremetal\",\n        \"name\"\
    : \"a3.large.opt-m3a2.x86\",\n        \"pricing_hour\": 8.2,\n        \"pricing_month\"\
    : null,\n        \"slug\": \"a3.large.opt-m3a2\"\n      },\n    ]\n  }\n]"
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
    categories=SpecField(
        type=FieldType.list,
        description=['Filter plans by its categories.'],
    ),
    type=SpecField(
        type=FieldType.string,
        description=['Filter plans by its plan type.'],
    ),
    slug=SpecField(
        type=FieldType.string,
        description=['Filter plans by slug.'],
    ),
    include=SpecField(
        type=FieldType.list,
        description=[
            'Nested attributes to include.',
            'Included objects will return their full attributes.',
            'Attribute names can be dotted (up to 3 levels) to included deeply nested objects.',
        ],
    ),
    exclude=SpecField(
        type=FieldType.list,
        description=[
            'Nested attributes to exclude.',
            'Excluded objects will return only the href attribute.',
            'Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.',
        ],
    ),
    organization_id=SpecField(
        type=FieldType.string,
        description=['UUID of the organization containing the plan.'],
    ),
    project_id=SpecField(
        type=FieldType.string,
        description="ID of the project where the plan is scoped to.",
    ),
)

specdoc_examples = ['''
- name: Gather information about all plans
  hosts: localhost
  tasks:
      - equinix.cloud.metal_plans_info
''', '''
- name: Gather information for plans starting with c3.medium
  hosts: localhost
  tasks:
      - equinix.cloud.metal_plans_info:
          slug: c3.medium
''',
]

result_sample = ['''

[  
  {                                                                           
    "changed": false,                                                                         
    "resources": [                                                                                                                                                    
      {                                                                                     
        "available_in": [],                                                                                                                                                       
        "available_in_metros": [],
        "category": [
          "compute",
          "current_gen"
        ],
        "class": "a3.large.opt-m3a2",
        "deployment_types": [],
        "description": "a3.large.opt-m3a2.x86",
        "id": "8c04950a-87ab-5e52-a112-5a90bbca8868",
        "legacy": false,
        "line": "baremetal",
        "name": "a3.large.opt-m3a2.x86",
        "pricing_hour": 8.2,
        "pricing_month": null,
        "slug": "a3.large.opt-m3a2"
      },
    ]
  }
]''',
]

SPECDOC_META = getSpecDocMeta(
    short_description="Gather information about Equinix Metal plans",
    description=(
        'Gather information about Equinix Metal plans'
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
        mutually_exclusive=[('project_id', 'organization_id')],
    )
    try:
        module.params_syntax_check()
        if module.params.get('organization_id'):
            return_value = {'resources': module.get_list("metal_organization_plans")}
        elif  module.params.get('project_id'):
            return_value = {'resources': module.get_list("metal_project_plans")}
        else:
            return_value = {'resources': module.get_list("metal_plans")}
    except Exception as e:
        tr = traceback.format_exc()
        module.fail_json(msg=to_native(e), exception=tr)
    module.exit_json(**return_value)


if __name__ == '__main__':
    main()
