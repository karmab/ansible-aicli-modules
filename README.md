# ansible-aicli-modules

Provides access to the latest release of the aicli modules. 

Include this role in a playbook, and any other plays, roles, and includes will have access to the modules.

The modules are found in the [library folder](./library)

## Requirements

- Ansible
- [aicli](https://github.com/karmab/aicli)

**Note**: Download the latest version of Ansible(https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html) 

## Installation and use

Use the Galaxy client to install the role:

```
$ ansible-galaxy install karmab.ansible_aicli_modules
```
**Note**: Before using the playbooks, please make sure to download these
1. `openshift_pull.json` from cloud.redhat.com(https://console.redhat.com/openshift/install/pull-secret)
2. `ocm token` and export it as a `OFFILINE TOKEN` from Openshift Offline Token(https://console.redhat.com/openshift/token) 


## How to use 

The following modules are available

- ai_cluster
- ai_cluster_info
- ai_infraenv
- ai_infraenv_info
- ai_host_info

For all of them, apart from mandatory parameters, you can provide a parameters dict with all your parameters

All parameters supported by AI (and extra parameters provided by aicli) can be used

### ai_cluster

```
  - name: Create a cluster named tahitibob forcing sno and network type
    ai_cluster:
      name: tahitibob
      state: present
      parameters:
       network_type: OVNKubernetes
       sno: true
```

|Parameter   |Required |Default Value         |
|------------|---------|----------------------|
|name        |true     |                      |
|state       |true     |                      |
|parameters  |false    |Empty dict            |

Note that cluster state can be:
- absent
- present
- updated (to run an update)
- installed (to wait for install to be completed)

### ai_cluster_info

```
- name: Get id from cluster tahitibob
  ai_cluster_info:
    name: tahitibob
  register: result
- debug: var=result['id']
```

|Parameter   |Required |Default Value         |
|------------|---------|----------------------|
|name        |true     |                      |

### ai_infraenv

```
  - name: Create an infraenv tahitibob
    ai_infraenv:
      name: tahitibob
      state: present
      parameters:
       minimal: true
```

|Parameter   |Required |Default Value         |
|------------|---------|----------------------|
|name        |true     |                      |
|state       |true     |                      |
|parameters  |false    |Empty dict            |

### ai_infraenv_info

```
- name: Get id from infraenv tahitibob
  ai_infraenv_info:
    name: tahitibob
  register: result
- debug: var=result['id']
```

|Parameter   |Required |Default Value         |
|------------|---------|----------------------|
|name        |true     |                      |

### ai_host_info

```
- name: Get id from host jimmyhendrix
  ai_host_info:
    name: jimyhendrix
  register: result
- debug: var=result['id']
```

|Parameter   |Required |Default Value         |
|------------|---------|----------------------|
|name        |true     |                      |

## License

Apache V2
