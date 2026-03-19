import csv
import os

def parse_csv_files(commands_csv_file_path, iplist_csv_file_path):
    devices = {}
    commands_dict = {}

    # Check if files exist
    if not os.path.isfile(commands_csv_file_path):
        print(f"Error: commands file not found: {commands_csv_file_path}")
        return devices
    if not os.path.isfile(iplist_csv_file_path):
        print(f"Error: iplist file not found: {iplist_csv_file_path}")
        return devices

    # Read commands.csv
    try:
        with open(commands_csv_file_path, newline='') as f:
            reader = csv.reader(f, delimiter=';')
            headers = next(reader)
            for row in reader:
                if len(row) < 3:
                    print(f"Warning: Skipping malformed commands row: {row}")
                    continue
                device_type = row[0].strip()
                device_class = row[1].strip()
                cmds = [cmd.strip() for cmd in row[2:] if cmd.strip()]
                commands_dict[(device_type, device_class)] = cmds
    except Exception as e:
        print(f"Error reading commands CSV: {e}")
        return devices

    # Read iplist.csv
    try:
        with open(iplist_csv_file_path, newline='') as f:
            reader = csv.reader(f, delimiter=';')
            headers = next(reader)
            for row in reader:
                if len(row) < 5:
                    print(f"Warning: Skipping malformed device row: {row}")
                    continue
                ip = row[0].strip()
                device_type = row[1].strip()
                device_class = row[2].strip()
                username = row[3].strip()
                password = row[4].strip()
                secret = row[5].strip() if len(row) > 5 else ""

                cmd_list = commands_dict.get((device_type, device_class), [])

                devices[ip] = {
                    'device_type': device_type,
                    'device_type_class': device_class,
                    'username': username,
                    'password': password,
                    'secret': secret,
                    'commands': cmd_list
                }
    except Exception as e:
        print(f"Error reading iplist CSV: {e}")
        return devices

    return devices
