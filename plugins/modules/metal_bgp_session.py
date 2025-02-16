#!/usr/bin/python
# -*- coding: utf-8 -*-

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

# DOCUMENTATION, EXAMPLES, and RETURN are generated by
# ansible_specdoc. Do not edit them directly.

DOCUMENTATION = '''
author: Equinix DevRel Team (@equinix) <support@equinix.com>
description: Manage BGP sessions in Equinix Metal.Create, update or delete BGP session.
  To look up an existing session, pass only the *id* attribute.
module: metal_bgp_session
notes: []
options:
  address_family:
    description:
    - BGP session address family, "ipv4" or "ipv6"
    required: false
    type: str
  default_route:
    description:
    - Boolean flag to set the default route policy. False by default.
    required: false
    type: bool
  device_id:
    description:
    - Device ID for the BGP session
    required: false
    type: str
  id:
    description:
    - UUID of the BGP session to look up
    required: false
    type: str
requirements: null
short_description: Manage BGP sessions in Equinix Metal
'''
EXAMPLES = '''
- name: Start first test bgp session
  hosts: localhost
  tasks:
  - equinix.cloud.metal_bgp_session:
      device_id: 8ea9837a-6d19-4607-b166-f7f7bb04b022
      address_family: ipv6
      default_route: true
- name: Delete bgp session
  hosts: localhost
  tasks:
  - equinix.cloud.metal_bgp_session:
      id: 1273edef-39af-4df0-85bb-02a847a484d1
      state: absent
'''
RETURN = '''
metal_bgp_session:
  description: The module object
  returned: always
  sample:
  - "\n [\n        {\n            \"address_family\": \"ipv4\",\n            \"default_route\"\
    : true,\n            \"device_id\": \"2066d33e-7c43-4d78-87a3-aaa434913f7f\",\n\
    \            \"id\": \"fc2d43e6-d606-47f7-9611-9d77aee443b5\"\n        },\n  \
    \      {\n            \"address_family\": \"ipv6\",\n            \"default_route\"\
    : true,\n            \"device_id\": \"bfab58c0-0723-49aa-a64e-6caf1b8ea2e2\",\n\
    \            \"id\": \"277d4a7a-82dd-4e7c-bf79-8a1de6882982\"\n        }\n   \
    \ ]\n"
  type: dict
'''

# End of generated documentation


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


module_spec = dict(
    id=SpecField(
        type=FieldType.string,
        description="UUID of the BGP session to look up",
    ),
    device_id=SpecField(
        type=FieldType.string,
        description="Device ID for the BGP session",
    ),
    address_family=SpecField(
        type=FieldType.string,
        description="BGP session address family, \"ipv4\" or \"ipv6\"",
        editable=False,
    ),
    default_route=SpecField(
        type=FieldType.bool,
        description="Boolean flag to set the default route policy. False by default.",
        editable=False,
    ),
)


specdoc_examples = ['''
- name: Start first test bgp session
  hosts: localhost
  tasks:
  - equinix.cloud.metal_bgp_session:
      device_id: 8ea9837a-6d19-4607-b166-f7f7bb04b022
      address_family: ipv6
      default_route: true
''', '''
- name: Delete bgp session
  hosts: localhost
  tasks:
  - equinix.cloud.metal_bgp_session:
      id: 1273edef-39af-4df0-85bb-02a847a484d1
      state: absent
''',
]

result_sample = ['''
 [
        {
            "address_family": "ipv4",
            "default_route": true,
            "device_id": "2066d33e-7c43-4d78-87a3-aaa434913f7f",
            "id": "fc2d43e6-d606-47f7-9611-9d77aee443b5"
        },
        {
            "address_family": "ipv6",
            "default_route": true,
            "device_id": "bfab58c0-0723-49aa-a64e-6caf1b8ea2e2",
            "id": "277d4a7a-82dd-4e7c-bf79-8a1de6882982"
        }
    ]
''']

MUTABLE_ATTRIBUTES = [
    k for k, v in module_spec.items() if v.editable
]

SPECDOC_META = getSpecDocMeta(
    short_description='Manage BGP sessions in Equinix Metal',
    description=(
        'Manage BGP sessions in Equinix Metal.'
        'Create, update or delete BGP session. To look up an existing session, pass only the *id* attribute.'
    ),
    examples=specdoc_examples,
    options=module_spec,
    return_values={
        "metal_bgp_session": SpecReturnValue(
            description='The module object',
            type=FieldType.dict,
            sample=result_sample,
        ),
    },
)


def main():
    module = EquinixModule(
        argument_spec=SPECDOC_META.ansible_spec,
        required_one_of=[("id", "address_family"), ("id", "default_route"), ("id", "device_id")],
    )

    state = module.params.get("state")
    changed = False

    fetched = {}
    try:
        module.params_syntax_check()
        if module.params.get("id"):
            tolerate_not_found = state == "absent"
            fetched = module.get_by_id("metal_bgp_session", tolerate_not_found)
        else:
            fetched = module.get_one_from_list(
                "metal_bgp_session",
                ["device_id"],
            )

        if fetched:
            module.params['id'] = fetched['id']
            if state == "present":
                diff = get_diff(module.params, fetched, MUTABLE_ATTRIBUTES)
                if diff:
                    fetched = module.update_by_id(diff, "metal_bgp_session")
                    changed = True

            else:
                module.delete_by_id("metal_bgp_session")
                changed = True
        elif state == "present":
            fetched = module.create("metal_bgp_session")
            if 'id' not in fetched:
                module.fail_json(msg="UUID not found in resource creation response")
            changed = True

    except Exception as e:
        tb = traceback.format_exc()
        module.fail_json(msg="Error in metal_bgp_session: {0}".format(to_native(e)),
                         exception=tb)

    fetched = {} if not fetched else fetched
    fetched.update({'changed': changed})
    module.exit_json(**fetched)


if __name__ == '__main__':
    main()
