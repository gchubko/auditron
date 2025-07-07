from load_csv_into_dict import parse_csv_files
from get_outputs import connect_and_collect_outputs

COMMANDS_CSV_FILE_PATH = "input data/commands.csv"
IPLIST_CSV_FILE_PATH = "input data/iplist.csv"

def main():
    # Parse CSV files into a device list
    devices = parse_csv_files(COMMANDS_CSV_FILE_PATH, IPLIST_CSV_FILE_PATH)

    # Collect outputs
    connect_and_collect_outputs(devices)


if __name__ == "__main__":
    # Entry point of the script
    main()
