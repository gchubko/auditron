import os
import logging
from netmiko import ConnectHandler


# Set up logging
logging.basicConfig(
    filename="netmiko_logs.log",  # Log file name
    filemode="a",  # Append mode
    format="%(asctime)s [%(levelname)s] %(message)s",  # Log format
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.DEBUG  # Set logging level to DEBUG for detailed logs
)

# Create a logger instance
logger = logging.getLogger(__name__)


def connect_and_collect_outputs(devices):
    for ip, params in devices.items():
        print(f"\nConnecting to {ip}...")
        logger.info(f"Attempting to connect to {ip}...")

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
                logger.info(f"Successfully connected to {ip}.")

                conn.enable()  # Enter privileged mode
                hostname = conn.find_prompt().strip("#>").split()[0]  # Extract hostname

                # Create directory
                dir_name = f"{hostname}_{ip.replace('.', '_')}"
                dir_name = "./output data/"+dir_name
                os.makedirs(dir_name, exist_ok=True)
                logger.info(f"Created directory '{dir_name}' for saving outputs.")


                for cmd in commands:
                    logger.info(f"Running command on {ip}: {cmd}")
                    print(f"Running command on {ip}: {cmd}")
                    output = conn.send_command(cmd, expect_string=r"{$hostname#}", read_timeout=60000)

                    # Save each command output in its own file
                    safe_cmd = cmd.replace(" ", "_").replace("/", "_")
                    filename = os.path.join(dir_name, f"{safe_cmd}.txt")

                    with open(filename, "w", encoding="utf-8") as f:
                        f.write(f"Command: {cmd}\n\n")
                        f.write(output)

                        logger.info(f"Command '{cmd}' output saved to '{filename}'.")

                print(f"Output saved in '{dir_name}'.")
                logger.info(f"Finished processing for '{ip}'. Directory: {dir_name}")


        except Exception as e:
            print(f"Failed to connect to {ip}: {e}")
            logger.exception(f"Error occurred while connecting to {ip}: {e}")


