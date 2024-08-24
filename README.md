# Ansible fm-dx-webserver

Ansible code to automate build and deploy:

- xdrd
- fm-dx-webserver

## Supported

Currently known to work on Debian derived distributions:

- Debian 12 (bookworm) on Raspberry Pi.
- Debian 12 (bookworm) on x86_64.
- Ubuntu 24.04 LTS (noble) on x86_64.

## Unsupported

Know *not* to work on:

- Ubuntu 22.04 LTS (jammy) on x86_64, the Ubuntu provided node.js is too old.

## Requirements

A supported system with a user which can run commands as root, ie su or sudo via ssh.

## Configuration

Copy inventories/inventory.ini-example to inventories/inventory.ini.

Edit the [inventories/inventory.ini](inventories/inventory.ini) file, so it includes only the systems you want to install on.

Edit the [group_vars/fmdx_servers.yml](group_vars/fmdx_servers.yml) to contain the settings you want.

## Example run

### Command

Use the user credentials from your remote system

```text
ansible-playbook main.yml -u fmdx -kK
SSH password: 
BECOME password[defaults to SSH password]: 
```

### Output

```text

PLAY [Run roles on target systems] *********************************************

TASK [Gathering Facts] *********************************************************
ok: [fmdx-vm]

TASK [xdrd : Install xdrd build dependencies] **********************************
changed: [fmdx-vm]

TASK [xdrd : Ensure /tmp/build directory exists] *******************************
changed: [fmdx-vm]

TASK [xdrd : Download the ZIP file] ********************************************
ok: [fmdx-vm -> localhost]

TASK [xdrd : Copy ZIP file to host] ********************************************
changed: [fmdx-vm]

TASK [xdrd : Unzip the file] ***************************************************
changed: [fmdx-vm]

TASK [xdrd : Build xdrd executable] ********************************************
changed: [fmdx-vm]

TASK [xdrd : Copy xdrd to /usr/bin] ********************************************
changed: [fmdx-vm]

TASK [xdrd : Add xdrd user with no interactive login and add to dialout group] ***
changed: [fmdx-vm]

TASK [xdrd : Deploy xdrd.service from template] ********************************
changed: [fmdx-vm]

TASK [xdrd : Reload systemd daemon] ********************************************
ok: [fmdx-vm]

TASK [xdrd : Ensure xdrd service is started and enabled] ***********************
changed: [fmdx-vm]

TASK [fm_dx_webserver : Install  nodejs, and npm] ******************************
changed: [fmdx-vm]

TASK [fm_dx_webserver : Download the ZIP file] *********************************
ok: [fmdx-vm -> localhost]

TASK [fm_dx_webserver : Copy ZIP file to host] *********************************
changed: [fmdx-vm]

TASK [fm_dx_webserver : Unzip the file] ****************************************
changed: [fmdx-vm]

TASK [fm_dx_webserver : Add the current user to the audio group] ***************
changed: [fmdx-vm]

TASK [fm_dx_webserver : Run npm install in the fm-dx-webserver-main directory] ***
changed: [fmdx-vm]

TASK [fm_dx_webserver : Check if fm-dx-webserver config file exists] ***********
ok: [fmdx-vm]

TASK [fm_dx_webserver : Create fm-dx-webserver config on first install] ********
changed: [fmdx-vm]

TASK [fm_dx_webserver : Reload systemd daemon] *********************************
ok: [fmdx-vm]

TASK [fm_dx_webserver : Deploy fm-dx-webserver.service from template] **********
changed: [fmdx-vm]

TASK [fm_dx_webserver : Ensure fm-dx-webserver service is started and enabled] ***
changed: [fmdx-vm]

PLAY RECAP *********************************************************************
fmdx-vm                    : ok=23   changed=17   unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

After this you can continue to finish the configuration of your fm-dx-server on your system in your browser.
