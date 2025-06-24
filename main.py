from load_csv_into_dict import parse_csv_files
from get_outputs import connect_and_collect_outputs

commands_csv_file_path = "commands.csv"
iplist_csv_file_path = "iplist.csv"

devices = parse_csv_files(commands_csv_file_path, iplist_csv_file_path)
connect_and_collect_outputs(devices)