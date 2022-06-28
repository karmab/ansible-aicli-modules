#!/usr/bin/python
# coding=utf-8

from ansible.module_utils.basic import AnsibleModule
from ailib import AssistedClient


DOCUMENTATION = '''
module: ai_host
short_description: Handles AI host using ailib
description:
    - Longer description of the module
    - You might include instructions
version_added: "0.2"
author: "Karim Boumedhel, @karmab"
notes:
    - Details at https://github.com/karmab/aicli
requirements:
    - aicli python package you can grab from pypi'''

EXAMPLES = '''
- name: Update aicli host
  ai_host:
    name: localhost
    state: present
    hostname: biloute

- name: Delete that host
  ai_host:
    name: biloute
    state: absent
'''


def main():
    """

    """
    argument_spec = {
        "state": {
            "default": "present",
            "choices": ['present', 'absent', 'updated'],
            "type": 'str'
        },
        "url": {"type": "str", "default": "https://api.openshift.com"},
        "name": {"required": True, "type": "str"},
        "offlinetoken": {"required": False, "type": "str"},
        "parameters": {"required": False, "type": "dict"},
    }
    module = AnsibleModule(argument_spec=argument_spec)
    overrides = module.params['parameters'] if module.params['parameters'] is not None else {}
    hostname = module.params['name']
    offlinetoken = module.params['offlinetoken']
    url = module.params['url']
    ai = AssistedClient(url, offlinetoken=offlinetoken)
    state = module.params['state']
    changed, skipped = True, False
    if state in ['present', 'updated']:
        meta = ai.update_host(hostname, overrides)
    elif [x['name'] for x in ai.list_hosts()]:
        meta = ai.delete_host(hostname)
    else:
        changed, skipped = False, True
        meta = {'result': 'skipped'}
    module.exit_json(changed=changed, skipped=skipped, meta=meta)


if __name__ == '__main__':
    main()
