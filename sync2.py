import os
import shutil
import time
import argparse
from colorama import init, Fore, Back, Style

# Initialize colorama
init(autoreset=True)

def print_boxed_text(text, color):
    """
    Print text in a colorized box.
    """
    length = len(text)
    print(color + "+" + "-"*(length+2) + "+")
    print(color + "|" + " "*(length+2) + "|")
    print(color + "| " + text + " |")
    print(color + "|" + " "*(length+2) + "|")
    print(color + "+" + "-"*(length+2) + "+")

def synchronize_folders(source_folder, replica_folder, log_file):
    """
    Synchronize two folders, maintaining an identical copy of the source folder at the replica folder.
    """
    # Synchronize the folders
    for root, dirs, files in os.walk(source_folder):
        # Get corresponding subdirectory in replica folder
        replica_root = root.replace(source_folder, replica_folder, 1)

        # Create subdirectory in replica folder if it does not exist
        if not os.path.exists(replica_root):
            os.makedirs(replica_root)

        # Synchronize files in current directory
        for file in files:
            source_path = os.path.join(root, file)
            replica_path = os.path.join(replica_root, file)

            # Copy file if it does not exist in replica folder or if it is different from source file
            if not os.path.exists(replica_path) or os.path.getmtime(source_path) > os.path.getmtime(replica_path):
                shutil.copy2(source_path, replica_path)
                log_file.write(f'Copied {source_path} to {replica_path}\n')
                print_boxed_text(f'Copied {source_path} to {replica_path}', Fore.GREEN)

        # Remove files from replica folder if they do not exist in source folder
        for file in os.listdir(replica_root):
            replica_path = os.path.join(replica_root, file)
            source_path = os.path.join(root, file)

            if not os.path.exists(source_path):
                os.remove(replica_path)
                log_file.write(f'Removed {replica_path}\n')
                print_boxed_text(f'Removed {replica_path}', Fore.RED)

if __name__ == '__main__':
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Synchronize two folders')
    parser.add_argument('source_folder', type=str, help='path to source folder')
    parser.add_argument('replica_folder', type=str, help='path to replica folder')
    parser.add_argument('--interval', type=int, default=60, help='synchronization interval in seconds (default: 60)')
    args = parser.parse_args()

    # Get command-line arguments
    source_folder = args.source_folder
    replica_folder = args.replica_folder
    interval_seconds = args.interval

    # Print help in a colorized box
    print_boxed_text('Help:', Fore.CYAN)
    parser.print_help()
    print()

    # Synchronize folders once initially
    with open('sync_log.txt', 'a') as log_file:
        synchronize_folders(source_folder, replica_folder, log_file)

# Synchronize folders periodically
while True:
    # Open log file
    with open('sync_log.txt', 'a') as log_file:
        # Synchronize folders
        synchronize_folders(source_folder, replica_folder, log_file)

        # Read the contents of the log file and print with color formatting
        log_file.seek(0)
        log_contents = log_file.read()

        # Define colors for different types of messages
        added_color = '\033[92m'  # green
        removed_color = '\033[91m'  # red
        reset_color = '\033[0m'  # reset color



# Print log contents with color formatting
    if log_contents:
        print('\033[94m' + '#' * 50)  # print colored border
        print(f'{added_color}{"ADDED:":<10}{"FILE PATH":<50}{"SIZE (bytes)":<15}{"MODIFIED":<25}{reset_color}')
        for line in log_contents.split('\n'):
            if line.startswith('Copied'):
                parts = line.split(' -> ')
                print(f'{added_color}{"ADDED:":<10}{parts[1]:<50}{parts[2]:<15}{parts[0]:<25}{reset_color}')
            elif line.startswith('Removed'):
                parts = line.split(' -> ')
            print(f'\033[91m{"REMOVED:":<10}{parts[1]:<50}{parts[2]:<15}{parts[0]:<25}\033[0m')
        print('\033[94m' + '#' * 50 + reset_color)  # print colored border

        # Wait for interval
        time.sleep(interval_seconds)
