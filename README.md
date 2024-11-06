# Ansible Collection for aicli

Provides access to the latest release of the [aicli](https://github.com/karmab/aicli) modules.

Include this collection in a role or playbook to have access to the modules.

## Requirements

- Ansible >= 2.9, it is recommended to download the latest version of [Ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html).
- [aicli](https://github.com/karmab/aicli) tool and library (`pip install aicli`).

## Prerequisites

Before using the modules, please make sure to download these
1. `openshift_pull.json` from [cloud.redhat.com](https://console.redhat.com/openshift/install/pull-secret)
2. `ocm token` and export it as a `OFFLINE TOKEN` from [Openshift Offline Token](https://console.redhat.com/openshift/token)

## Installation

Use the Ansible Galaxy client to install the latest version of the collection:

```sh
$ ansible-galaxy collection install karmab.aicli
```

or using `requirements.yml`:

```yaml
collections:
  - name: karmab.aicli
```

### Installing a development version

If you want to install a _development version from GitHub_:

Install with `ansible-galaxy`:

```sh
$ ansible-galaxy collection install git+https://github.com/karmab/ansible-aicli-modules.git,main
```

or include it in `requirements.yml`:

```yaml
collections:
  - name: https://github.com/karmab/ansible-aicli-modules.git
    type: git
    version: main
```

In order to use a development version of the collection as a dependency of another collection, specify

```yaml
dependencies:
  git+https://github.com/karmab/ansible-aicli-modules.git: main
```

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

```yaml
  - name: Create a cluster named tahitibob forcing sno and network type
    karmab.aicli.ai_cluster:
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
- started (to start deployment once requirement are fulfilled)
- stopped (to stop a failing deployment)

### ai_cluster_info

```yaml
  - name: Get id from cluster tahitibob
    karmab.aicli.ai_cluster_info:
      name: tahitibob
    register: result
  - debug: var=result['id']
```

|Parameter   |Required |Default Value         |
|------------|---------|----------------------|
|name        |true     |                      |

### ai_infraenv

```yaml
  - name: Create an infraenv tahitibob
    karmab.aicli.ai_infraenv:
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

```yaml
  - name: Get id from infraenv tahitibob
    karmab.aicli.ai_infraenv_info:
      name: tahitibob
    register: result
  - debug: var=result['id']
```

|Parameter   |Required |Default Value         |
|------------|---------|----------------------|
|name        |true     |                      |

### ai_host_info

```yaml
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
