import os
from netmiko import ConnectHandler

def connect_and_collect_outputs(devices):
    for ip, params in devices.items():
        print(f"\nConnecting to {ip}...")

        try:
            # Prepare Netmiko parameters (host = ip)
            netmiko_params = {
                'host': ip,
                'device_type': params['device_type'],
                'username': params['username'],
                'password': params['password'],
                'secret': params['secret']
            }

            commands = params.get('commands', [])

            # Connect
            with ConnectHandler(**netmiko_params) as conn:
                conn.enable()  # Enter privileged mode
                hostname = conn.find_prompt().strip("#>").split()[0]  # Extract hostname

                # Create directory
                dir_name = f"{hostname}_{ip.replace('.', '_')}"
                os.makedirs(dir_name, exist_ok=True)

                for cmd in commands:
                    print(f"Running command on {ip}: {cmd}")
                    output = conn.send_command(cmd, max_loops=50000, delay_factor=5)

                    # Save each command output in its own file
                    safe_cmd = cmd.replace(" ", "_").replace("/", "_")
                    filename = os.path.join(dir_name, f"{safe_cmd}.txt")

                    with open(filename, "w", encoding="utf-8") as f:
                        f.write(f"Command: {cmd}\n\n")
                        f.write(output)

                print(f"Output saved in '{dir_name}'.")

        except Exception as e:
            print(f"Failed to connect to {ip}: {e}")

