import os
import shutil
import time
import argparse

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
                print(f'\033[7;32m Copied \033[0m {source_path} \033[7;32m to \033[0m {replica_path}')

        # Remove files from replica folder if they do not exist in source folder
        for file in os.listdir(replica_root):
            replica_path = os.path.join(replica_root, file)
            source_path = os.path.join(root, file)

            if not os.path.exists(source_path):
                os.remove(replica_path)
                log_file.write(f'Removed {replica_path}\n')
                print(f'\033[7;31m Removed \033[0m {replica_path}')

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

    # Synchronize folders once initially
    with open('sync_log.txt', 'a') as log_file:
        synchronize_folders(source_folder, replica_folder, log_file)

    # Synchronize folders periodically
    while True:
        # Open log file
        with open('sync_log.txt', 'a') as log_file:
            # Synchronize folders
            synchronize_folders(source_folder, replica_folder, log_file)

        # Wait for interval
        time.sleep(interval_seconds)
