## Table of Contents

1. [Python Folder Synchronization Program](#python-folder-synchronization-progran)
2. [Stories ](#stories)
3. [Functionality](#functionality)
4. [User Interface](#user-interface)
5. [How Does it works?](#how-does-it-works)
6. [Usage](#usage)
7. [Functions)](#functions)
   - synchronize_folders()
   - __main__()
8. [Requirements](#requirements)
9. [Dependencies](#dependencies)
10. [Configuration](#configuration)
11. [Contributors](#license)
12. [Support](#support)
13. [License](#license)


# Python Folder Synchronization Program

The Python script `sync_folders.py` synchronizes two folders, maintaining an identical copy of the source folder at the replica folder. The script uses the `os` and `shutil` modules to manipulate files and directories, and the argparse module to parse command-line arguments.

# Stories

The script is designed to synchronize two folders, maintaining an identical copy of the source folder at the replica folder. It is useful for backing up data or sharing files between different devices.

The script is also designed to be run from the command line, making it easy to use and automate.

# Functionality:
The main function in the script is `synchronize_folders()`, which takes three arguments: `source_folder`,   `replica_folder`, and `log_file`. The function synchronizes the files in the source folder with the corresponding files in the replica folder. It performs the following actions:
1. Walks through the source folder using the `os.walk()` method.
2. For each file in the source folder, it does the following:
    - Gets the corresponding file in the replica folder.
    - If the file does not exist in the replica folder or is different from the source file, it is copied to the replica folder.
    - If the file exists in the replica folder but not in the source folder, it is removed from the replica folder.
3. Logs synchronization events to a file called `sync_log.txt` using the `log_file` argument.
  The script synchronizes the folders once initially, and then continues to synchronize the folders periodically based on the specified interval using a while loop and the `time.sleep()` method.

# User Interface:
The script is run from the command line with the following syntax:
```sh
python synchronize_folders.py source_folder replica_folder [--interval INTERVAL]
```

- `source_folder` is the path to the source folder to be synchronized.
- `replica_folder` is the path to the replica folder where the copy of the source folder will be maintained.
- `--interval INTERVAL` (optional) is the synchronization interval in seconds (default: 60).

The script logs all synchronization events to a log file named `sync_log.txt` in the current directory and prints them to the console in colored text.

# How Does it works?
The script works by synchronizing two folders, maintaining an identical copy of the `source folder` at the `replica folder`. It does this by walking through the directory tree rooted at the `source_folder` and copying all files that do not exist in the `replica_folder` or are different from the corresponding files in the `source_folder`. It also removes files from the `replica_folder` that do not exist in the `source_folder`. The script logs all synchronization events to a log file and prints them to the console in colored text.

The script is run from the command line with the paths to the `source_folder` and `replica_folder` as arguments, and an optional synchronization interval in seconds. The script then synchronizes the folders once initially using the `synchronize_folders()` function with a log file opened in append mode. It then enters a loop that synchronizes the folders periodically at the specified interval using the `synchronize_folders()` function and waits for the interval using the `time.sleep()` function.

# Usage
To run the script, use the following command in your terminal:
```sh
python synchronize_folders.py /path/to/source/folder /path/to/replica/folder --interval 120
```

This command will synchronize the contents of the source folder located at `/path/to/source/folder` with the replica folder located at `/path/to/replica/folder`. The synchronization will occur every 120 seconds (2 minutes) by default. You can change the synchronization interval by providing a different value for the `--interval` argument.

Note that the script will create the replica folder if it does not already exist. Also, any files in the replica folder that do not exist in the source folder will be deleted during synchronization.

You can view the log file for a record of the synchronization actions by opening the `sync_log.txt` file in the same directory as the script.

# Functions

This Python code provides a function called `synchronize_folders()` that synchronizes two folders, maintaining an identical copy of the source folder at the replica folder. The function takes three parameters: `source_folder` which is the path to the source folder, `replica_folder` which is the path to the replica folder, and `log_file` which is a file object for logging synchronization events.

The function uses the `os` and `shutil` modules to perform file and folder operations, and the `time` module for setting synchronization intervals. It also utilizes the `argparse` module to parse command-line arguments.

The `synchronize_folders()` function first walks through the source folder using `os.walk()`, gets the corresponding subdirectory in the replica folder, and creates the subdirectory if it does not exist. It then synchronizes the files in the current directory by copying the file to the replica folder if it does not exist or if it is different from the source file. If a file exists in the replica folder but not in the source folder, it is removed from the replica folder. The function logs each synchronization event to the specified `log_file`.

The code also includes a `if __name__` == `'__main__'`: block that uses the argparse module to parse command-line arguments, including the source folder path, replica folder path, and synchronization interval in seconds. It then calls the synchronize_folders() function once initially with the specified arguments, and then synchronizes the folders periodically at the specified interval.



# Requirements

Python 3.6 or later
Required packages listed in requirements.txt
To install the required packages, run the following command in your terminal:

```sh
pip install -r requirements.txt
```

# Dependencies

This script requires the following Python modules:
* `os`
* `shutil`
* `time`
* `argparse`

## Colored console:
This script uses colored console output to highlight the synchronization process. The following color codes are used:
* 🟩 **Green**: indicates a file has been copied from the source folder to the replica folder.
* 🟥 **Red**: indicates a file has been removed from the replica folder because it no longer exists in the source folder.
* ⬜ **White**: default color for all other output.

# Configuration

The script requires user to specify in the terminal:

- Source Folder
- Replica Folder
- Interval (Optional) 

# Contributors ✨

<table>
  <tbody>
    <tr>
      <td align="center"><a href="https://hurr13ane.com"><img src="https://avatars.githubusercontent.com/u/76591840?v=4" width="100px;" alt="Jeroen Engels"/><br /><sub><b>Diana-Maria Iercosan</b></sub></a><br />
      </td>
    </tr>
  </tbody>
</table>

# Support
For any questions or support, please contact me via https://hurr13ane.com/contact/

# License
This project is licensed under the MIT License.
