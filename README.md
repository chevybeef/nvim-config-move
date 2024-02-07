# nvim-config-move
A script to move the current neovim config "out of the way" in order to 
start from a blank slate when wanting to experiment with other configurations.
The nvim configuration and plugins are kept in the 4 directories listed below.
The idea is that all of these directories will be renamed together as a set
which would return nvim to factory defaults so to speak, and can then be 
restored later if desired. 

Imaginative extensions such as below could be used (without the period):

|   EXTENSION   |       DESCRIPTION       | 
|--------------:|-------------------------|
|bak            | vanilla backup          |
|b4anv          | before astronvim        |
|mine           | your config             |
|distrotube     | distrotube's config     |
|kickstart      | kickstart's config      |

All 4 of the nvim config directories must exists or the script will abort:

```
~/.config/nvim
~/.local/share/nvim
~/.local/state/nvim
~/.cache/nvim
```

You could create any empty directories manually if they don't exist.

Works on macOS, Linux and Windows.

## Installation

install psutil dependency: 

```pip install psutil```

git clone https://github.com/chevybeef/nvim-config-move.git

cd nvim-config-move

chmod a+x nvim-config-move.py

## Usage

```./nvim-config-move.py move, restore, change extension [extension]```

## Examples

```
# to rename the 4 directories mentioned above to .bak
./nvim-config-move.py move bak 

# to bring back the bak config (if those 4 folders above don't already exist)
./nvim-config-move.py restore bak

# move the current config to .lazyvim and restore .kickstart
./nvim-config-move.py change lazyvim kickstart
```

note: the dot before the extension is not required

note: the script will abort if it doesn't find all 4 directories (make them manually if required)
