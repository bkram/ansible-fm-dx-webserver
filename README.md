# Ansible fm-dx-webserver

Ansible code to automate build and deploy:

- xdrd
- fm-dx-webserver
- plugins

## Supported

Currently known to work on Debian derived distributions:

- Debian 12 (bookworm) on Raspberry Pi.
- Debian 12 (bookworm) on x86_64.
- Debian 12 (bookworm) on i386.
- Ubuntu 24.04 (noble) of x86_64.

## Unsupported

Known *not* to work on:

- Ubuntu 22.04 LTS (jammy) on x86_64, the Ubuntu provided node.js is too old.

## Requirements

A supported system with a user which can run commands as root, ie su or sudo via ssh.

## Configuration

Copy inventories/inventory.ini-example to inventories/inventory.ini.

Edit the [inventories/inventory.ini](inventories/inventory.ini) file, so it includes only the systems you want to install on.

Edit the [group_vars/fmdx_servers.yml](group_vars/fmdx_servers.yml) to set the globale settings you want.

Copy and edit [host_vars/fmdx-debian.yaml]host_vars/fmdx-debian.yaml and edit to suit your requirements.

## Example run

### Command

Use the user credentials from your remote system

```text
ansible-playbook main.yml -u admin -kK
SSH password: 
BECOME password[defaults to SSH password]: 
```
