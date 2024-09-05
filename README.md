# Ansible fm-dx-webserver

Ansible code to automate build and deploy:

- xdrd
- fm-dx-webserver

## Supported

Currently known to work on Debian derived distributions:

- Debian 12 (bookworm) on Raspberry Pi.
- Debian 12 (bookworm) on x86_64.
- Debian 12 (bookworm) on i386.

## Unsupported

Known *not* to work on:

- Ubuntu 22.04 LTS (jammy) on x86_64, the Ubuntu provided node.js is too old.
- Ubuntu 24.04 LTS (noble) on x86_64. some issue with ansible git module.

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
PLAY [Prepare target systems] *****************************************************************************************************************************************************************************************************

TASK [Gathering Facts] ************************************************************************************************************************************************************************************************************
[WARNING]: Platform linux on host fmdx-vm-debian is using the discovered Python interpreter at /usr/bin/python3.11, but future installation of another Python interpreter could change the meaning of that path. See
https://docs.ansible.com/ansible-core/2.17/reference_appendices/interpreter_discovery.html for more information.
ok: [fmdx-vm-debian]

TASK [Ensure the system is Debian-based] ******************************************************************************************************************************************************************************************
ok: [fmdx-vm-debian] => {
    "changed": false,
    "msg": "All assertions passed"
}

TASK [Check if sudo is installed] *************************************************************************************************************************************************************************************************
fatal: [fmdx-vm-debian]: FAILED! => {"changed": false, "cmd": ["which", "sudo"], "delta": "0:00:00.002359", "end": "2024-08-24 06:26:31.382914", "msg": "non-zero return code", "rc": 1, "start": "2024-08-24 06:26:31.380555", "stderr": "", "stderr_lines": [], "stdout": "", "stdout_lines": []}
...ignoring

TASK [Install sudo if not installed] **********************************************************************************************************************************************************************************************
changed: [fmdx-vm-debian]

TASK [Configure passwordless sudo for fmdx] ***************************************************************************************************************************************************************************************
changed: [fmdx-vm-debian]

PLAY [Run roles on target systems] ************************************************************************************************************************************************************************************************

TASK [Gathering Facts] ************************************************************************************************************************************************************************************************************
ok: [fmdx-vm-debian]

TASK [xdrd : Install xdrd build dependencies] *************************************************************************************************************************************************************************************
changed: [fmdx-vm-debian]

TASK [xdrd : Ensure /tmp/build directory exists] **********************************************************************************************************************************************************************************
changed: [fmdx-vm-debian]

TASK [xdrd : Download the ZIP file] ***********************************************************************************************************************************************************************************************
ok: [fmdx-vm-debian -> localhost]

TASK [xdrd : Copy ZIP file to host] ***********************************************************************************************************************************************************************************************
changed: [fmdx-vm-debian]

TASK [xdrd : Unzip the file] ******************************************************************************************************************************************************************************************************
changed: [fmdx-vm-debian]

TASK [xdrd : Build xdrd executable] ***********************************************************************************************************************************************************************************************
changed: [fmdx-vm-debian]

TASK [xdrd : Copy xdrd to /usr/bin] ***********************************************************************************************************************************************************************************************
changed: [fmdx-vm-debian]

TASK [xdrd : Add xdrd user with no interactive login and add to dialout group] ****************************************************************************************************************************************************
changed: [fmdx-vm-debian]

TASK [xdrd : Deploy xdrd.service from template] ***********************************************************************************************************************************************************************************
changed: [fmdx-vm-debian]

TASK [xdrd : Reload systemd daemon] ***********************************************************************************************************************************************************************************************
ok: [fmdx-vm-debian]

TASK [xdrd : Ensure xdrd service is started and enabled] **************************************************************************************************************************************************************************
changed: [fmdx-vm-debian]

TASK [fm_dx_webserver : Install  nodejs, and npm] *********************************************************************************************************************************************************************************
changed: [fmdx-vm-debian]

TASK [fm_dx_webserver : Download the ZIP file] ************************************************************************************************************************************************************************************
ok: [fmdx-vm-debian -> localhost]

TASK [fm_dx_webserver : Copy ZIP file to host] ************************************************************************************************************************************************************************************
changed: [fmdx-vm-debian]

TASK [fm_dx_webserver : Unzip the file] *******************************************************************************************************************************************************************************************
changed: [fmdx-vm-debian]

TASK [fm_dx_webserver : Add the current user to the audio group] ******************************************************************************************************************************************************************
ok: [fmdx-vm-debian]

TASK [fm_dx_webserver : Run npm install in the fm-dx-webserver-main directory] ****************************************************************************************************************************************************
changed: [fmdx-vm-debian]

TASK [fm_dx_webserver : Check if fm-dx-webserver config file exists] **************************************************************************************************************************************************************
ok: [fmdx-vm-debian]

TASK [fm_dx_webserver : Create fm-dx-webserver config on first install] ***********************************************************************************************************************************************************
changed: [fmdx-vm-debian]

TASK [fm_dx_webserver : Reload systemd daemon] ************************************************************************************************************************************************************************************
ok: [fmdx-vm-debian]

TASK [fm_dx_webserver : Deploy fm-dx-webserver.service from template] *************************************************************************************************************************************************************
changed: [fmdx-vm-debian]

TASK [fm_dx_webserver : Ensure fm-dx-webserver service is started and enabled] ****************************************************************************************************************************************************
changed: [fmdx-vm-debian]

PLAY RECAP ************************************************************************************************************************************************************************************************************************
fmdx-vm-debian             : ok=28   changed=18   unreachable=0    failed=0    skipped=0    rescued=0    ignored=1   
```

After this you can continue to finish the configuration of your fm-dx-server on your system in your browser.
