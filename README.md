## auditron
This project is a lightweight tool for automating command execution across multiple network devices (Cisco, Juniper, etc.) using [Netmiko](https://github.com/ktbyers/netmiko). It reads device and command lists from CSV files, connects to the devices, runs the specified commands, and saves the outputs into structured folders.

## Project Structure
<pre>.
├── input data/
│ ├── commands.csv # Command templates per device type/class
│ └── iplist.csv # Device inventory and credentials
├── output data/ # Automatically generated command output files
├── get_outputs.py # Handles Netmiko connections and output saving
├── load_csv_into_dict.py # Parses input CSVs into structured dictionaries
├── main.py # Main entry point
└── netmiko_logs.log # (Generated) Log file with debug info </pre>


## 1. Install Dependencies
pip install netmiko

## 2. Prepare Input Files
input data/commands.csv (delimiter: ;) - This CSV file defines commands that should be run on devices
<pre>device_type;device_type_class;commands
cisco_ios;router;show logging;show clock;show ip interface brief;show interfaces;show arp;show ip route
cisco_ios;switch;show mac address-table;show spanning-tree;show memory;show tech-support;show ip route
juniper;router;show version;show configuration;show interfaces terse;show interfaces diagnostics optics
juniper;switch;show configuration;show chassis hardware</pre>

input data/iplist.csv (delimiter: ;) - This CSV file defines device credentials and classification
<pre>ip address;device_type;device_type_class;username;password;secret
192.0.0.1;cisco_ios;switch;cisco;cisco
192.0.0.2;cisco_ios;switch;cisco;cisco
192.0.0.3;cisco_ios;switch;cisco;cisco</pre>

## 3. Run the script
python main.py

## 4. Logging - All actions and errors are logged into:
netmiko_logs.log
