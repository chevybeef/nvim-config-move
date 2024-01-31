#!/usr/bin/env python3

import os
import shutil
import sys
import psutil

'''
this program moves nvim config folders out the way in order to
"start over configuring neovim"
it can also restore from a previous move operation
or swap to another configuration
'''

if sys.platform == "win32":
    user_directories = [
        os.getenv('LOCALAPPDATA') + '\\nvim',
        os.getenv('LOCALAPPDATA') + '\\nvim-data'
    ]
    nvim_process = "nvim.exe"
else:
    user_directories = [
        "~/.config/nvim",
        "~/.local/share/nvim",
        "~/.local/state/nvim",
        "~/.cache/nvim",
    ]
    nvim_process = "nvim"


def directories_exist(directories, create_if_not_exists) -> bool:
    number_of_paths = 0
    for directory in directories:
        if create_if_not_exists and not os.path.exists(directory):
            os.makedirs(directory)
        number_of_paths += int(os.path.exists(directory))
    return number_of_paths == len(directories)


def rename_directories(from_directories, to_directories):
    for index, _ in enumerate(from_directories):
        shutil.move(from_directories[index], to_directories[index])
        print(from_directories[index], to_directories[index])


for process in psutil.process_iter(['name']):
    if process.info['name'] == nvim_process:
        print("Neovim is running, best to exit before continuing.")
        exit(1)


supported_operations = ["move", "restore", "change"]


def usage():
    print(f"Usage: python3 {sys.argv[0]} {
        supported_operations} [to_extension, from_extension]")
    exit(1)


arguments_passed = len(sys.argv)
if arguments_passed < 2 or arguments_passed > 4:
    usage()

operation = sys.argv[1].strip(" .")
if (operation == "move" or operation == "restore") and arguments_passed != 3:
    usage()

if operation == "change" and arguments_passed != 4:
    usage()

to_extension = "." + sys.argv[2].strip(" .")
from_extension = to_extension
if arguments_passed == 4:
    from_extension = "." + sys.argv[3].strip(" .")
    print(f"This is a '{operation}' operation using extensions '{
        to_extension}, {from_extension}'")
else:
    print(f"This is a '{operation}' operation using extension '{
        to_extension}'")

from_directories = []
to_directories = []
for index, directory in enumerate(user_directories):
    if operation == "move" or operation == "change":
        from_directories.append(os.path.expanduser(directory))
        to_directories.append(from_directories[index] + to_extension)

for index, directory in enumerate(user_directories):
    if operation == "restore" or operation == "change":
        from_directories.append(os.path.expanduser(
            user_directories[index]) + from_extension)
        to_directories.append(os.path.expanduser(user_directories[index]))

if not directories_exist(from_directories, False):
    print(f"{from_directories} from must exist, aborting.")
    exit(1)
if operation == "change":
    if directories_exist(to_directories[0:4], False):
        print(f"{to_directories[0:4]} to must not exist, aborting.")
        exit(1)
else:
    if directories_exist(to_directories, False):
        print(f"{to_directories} to must not exist, aborting.")
        exit(1)

print("These directories:")
for fd in from_directories:
    print(f"{fd}")
print("Will be renamed to this:")
for td in to_directories:
    print(f"{td}")

if input("Proceed [y/N] ") == "y":
    rename_directories(from_directories, to_directories)
else:
    print("Okay, aborting, nothing has been changed.")
