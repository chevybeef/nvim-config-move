import os
import shutil
import sys

# this program moves config folders out the way in order to "start over configuring neovim"
# it can also restore from a previous move operation
# usage: config.py "operation" "extension"
# operation can be either "move" or "restore"


def directories_exist(directories) -> bool:
    number_of_paths = 0
    for directory in directories:
        number_of_paths += int(os.path.exists(directory))
    return number_of_paths == len(directories)


def rename_directories(from_directories, to_directories):
    for index, _ in enumerate(from_directories):
        shutil.move(from_directories[index], to_directories[index])


arguments_passed = len(sys.argv)
print("Number of arguments passed: ", arguments_passed)
if arguments_passed != 3:
    print(f"Usage: python3 {sys.argv[0]} operation extension")
    exit(1)

operation = sys.argv[1]
extension = "." + sys.argv[2]
supported_operations = ["move", "restore"]
if operation not in supported_operations:
    print(
        f"Operation '{operation}' not supported. Only {supported_operations} implemented."
    )
    exit(1)

print(f"This is a '{operation}' operation using extension '{extension}'")

if sys.platform == "win32":
    user_directories = [os.getenv(
        'LOCALAPPDATA') + '\\nvim', os.getenv('LOCALAPPDATA') + '\\nvim-data']
else:
    user_directories = [
        "~/.config/nvim",
        "~/.local/share/nvim",
        "~/.local/state/nvim",
        "~/.cache/nvim",
    ]

# if this is a move operation, create the list of directories to move to
from_directories = []
to_directories = []
for index, directory in enumerate(user_directories):
    if operation == "move":
        from_directories.append(os.path.expanduser(directory))
        to_directories.append(from_directories[index] + extension)
    if operation == "restore":
        to_directories.append(os.path.expanduser(user_directories[index]))
        from_directories.append(to_directories[index] + extension)
# if any of the from directories don't exist then abort
if not directories_exist(from_directories):
    print(f"{from_directories} doesn't exist, aborting.")
    exit(1)
# if any of the to_directories already exist then abort
if directories_exist(to_directories):
    print(f"{to_directories} already exists, aborting.")
    exit(1)
print(f"{from_directories} will be moved to \n{to_directories}")
if input("Proceed [y/N]?") == "y":
    rename_directories(from_directories, to_directories)
else:
    print("Okay, aborting...")
