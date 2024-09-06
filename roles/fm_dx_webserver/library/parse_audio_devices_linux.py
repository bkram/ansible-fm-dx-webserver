from ansible.module_utils.basic import AnsibleModule
import re


def parse_audio_devices_linux():
    # Hardcoded file path for Linux
    file_path = "/proc/asound/cards"
    audio_devices = []

    try:
        # Open the file and read its content
        with open(file_path, "r", encoding="utf-8") as file:
            data = file.read()

        # Regular expression to match text inside square brackets
        regex = r"\[([^\]]+)\]"
        matches = re.findall(regex, data)

        # Process each match
        for match in matches:
            # Remove any extra whitespace and prefix with 'hw:'
            device_name = "hw:" + match.strip()
            audio_devices.append({"name": device_name})

        if not audio_devices:
            return False, "No audio devices found", audio_devices
        else:
            return True, f"Found {len(audio_devices)} audio devices.", audio_devices

    except FileNotFoundError:
        return False, f"Error: File {file_path} not found.", []
    except Exception as e:
        return False, f"Error reading file: {str(e)}", []


def run_module():
    # Create AnsibleModule instance
    module = AnsibleModule(
        argument_spec=dict(),  # Add any arguments you need here (none in this case)
        supports_check_mode=False,
    )

    # Default result
    result = dict(changed=False, audio_devices=[])

    # Parse the audio devices from the file
    success, message, audio_devices = parse_audio_devices_linux()

    # Set the result for Ansible output
    result["audio_devices"] = audio_devices
    result["message"] = message
    result["changed"] = success

    if not success:
        module.fail_json(msg=message, **result)
    else:
        module.exit_json(**result)


def main():
    run_module()


if __name__ == "__main__":
    main()
