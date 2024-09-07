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

## Unsupported

Known *not* to work on:

- Ubuntu 22.04 LTS (jammy) on x86_64, the Ubuntu provided node.js is too old.
- Ubuntu 24.04 LTS (noble) on x86_64. some issue with ansible git module.

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
ansible-playbook main.yml -u fmdx -kK
SSH password: 
BECOME password[defaults to SSH password]: 
```

### Output

```text

PLAY [Prepare target systems] **************************************************

TASK [Gathering Facts] *********************************************************
ok: [fmdx-debian]

TASK [Ensure the system is Debian-based] ***************************************
ok: [fmdx-debian] => {
    "changed": false,
    "msg": "All assertions passed"
}

TASK [Check if sudo is installed] **********************************************
ok: [fmdx-debian]

TASK [Install sudo if not installed] *******************************************
skipping: [fmdx-debian]

TASK [Configure passwordless sudo for fmdx] ************************************
skipping: [fmdx-debian]

PLAY [Run roles on target systems] *********************************************

TASK [Gathering Facts] *********************************************************
ok: [fmdx-debian]

TASK [xdrd : Add xdrd user with no interactive login and add to dialout group] ***
ok: [fmdx-debian]

TASK [xdrd : Install xdrd build dependencies] **********************************
ok: [fmdx-debian]

TASK [xdrd : Create /opt/build-xdrd directory] *********************************
changed: [fmdx-debian]

TASK [xdrd : Clone or update the XDRD repo from GitHub] ************************
changed: [fmdx-debian]

TASK [xdrd : Build xdrd executable] ********************************************
changed: [fmdx-debian]

TASK [xdrd : Copy xdrd to /usr/bin] ********************************************
ok: [fmdx-debian]

TASK [xdrd : Deploy xdrd.service from template] ********************************
changed: [fmdx-debian]

TASK [xdrd : Ensure xdrd service is started and enabled] ***********************
ok: [fmdx-debian]

TASK [fm_dx_webserver : Install  nodejs, and npm] ******************************
ok: [fmdx-debian]

TASK [fm_dx_webserver : Add the current user to the audio group] ***************
ok: [fmdx-debian]

TASK [fm_dx_webserver : Create /opt/fm-dx-webserver directory] *****************
changed: [fmdx-debian]

TASK [fm_dx_webserver : Clone or update the fm-dx-webserver repo from GitHub] ***
changed: [fmdx-debian]

TASK [fm_dx_webserver : Install npm dependencies in the fm-dx-webserver-main directory] ***
changed: [fmdx-debian]

TASK [fm_dx_webserver : Check if fm-dx-webserver config file exists] ***********
ok: [fmdx-debian]

TASK [fm_dx_webserver : Get list of audio devices] *****************************
ok: [fmdx-debian]

TASK [fm_dx_webserver : Set audio device when none is configured] **************
ok: [fmdx-debian]

TASK [fm_dx_webserver : Create fm-dx-webserver config on first install] ********
changed: [fmdx-debian]

TASK [fm_dx_webserver : Deploy fm-dx-webserver.service from template] **********
changed: [fmdx-debian]

TASK [fm_dx_webserver : Ensure fm-dx-webserver service is started and enabled] ***
ok: [fmdx-debian]

TASK [fm_dx_plugins : Iterate over fmdx_plugins list and include tasks] ********
included: git/ansible-fm-dx-webserver/roles/fm_dx_plugins/tasks/install_plugin.yml for fmdx-debian => (item={'name': 'webserver-station-logos', 'shortname': 'station-logos', 'url': 'https://github.com/Highpoint2000/webserver-station-logos.git', 'entrypoint': 'StationLogo/updateStationLogo.js', 'install': True})
included: git/ansible-fm-dx-webserver/roles/fm_dx_plugins/tasks/install_plugin.yml for fmdx-debian => (item={'name': 'fm-dx-webserver-plugin-weather', 'shortname': 'weather', 'url': 'https://github.com/NoobishSVK/fm-dx-webserver-plugin-weather.git', 'entrypoint': 'weather/frontend.js', 'install': True})

TASK [fm_dx_plugins : Ensure /opt/fm-dx-plugins/ directory exists] *************
changed: [fmdx-debian]

TASK [fm_dx_plugins : Debug the current plugin details] ************************
ok: [fmdx-debian] => {
    "msg": "Processing plugin: webserver-station-logos with URL: https://github.com/Highpoint2000/webserver-station-logos.git and install status: True"
}

TASK [fm_dx_plugins : Clone or update the plugin repo webserver-station-logos] ***
changed: [fmdx-debian]

TASK [fm_dx_plugins : Synchronize plugin station-logos] ************************
changed: [fmdx-debian]

TASK [fm_dx_plugins : Ensure /opt/fm-dx-plugins/ directory exists] *************
ok: [fmdx-debian]

TASK [fm_dx_plugins : Debug the current plugin details] ************************
ok: [fmdx-debian] => {
    "msg": "Processing plugin: fm-dx-webserver-plugin-weather with URL: https://github.com/NoobishSVK/fm-dx-webserver-plugin-weather.git and install status: True"
}

TASK [fm_dx_plugins : Clone or update the plugin repo fm-dx-webserver-plugin-weather] ***
changed: [fmdx-debian]

TASK [fm_dx_plugins : Synchronize plugin weather] ******************************
changed: [fmdx-debian]

RUNNING HANDLER [xdrd : Restart xdrd service] **********************************
changed: [fmdx-debian]

RUNNING HANDLER [fm_dx_webserver : Restart fm-dx-webserver] ********************
changed: [fmdx-debian]

PLAY RECAP *********************************************************************
fmdx-debian                : ok=35   changed=16   unreachable=0    failed=0    skipped=2    rescued=0    ignored=0   
```

After this you can continue to finish the configuration of your fm-dx-server on your system in your browser.
