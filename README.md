# nvim-config-move
A python script to move the current neovim configuration out of the way in order to start over when wanting to experiment with other configurations. The nvim configuration and plugins are kept in the 4 directories listed below. The idea is that all of these directories will be renamed together as a set which would return nvim to factory defaults so to speak, and can then be restored later if desired. 

Imaginative extensions such as below could be used (without the period):

|   EXTENSION   |       DESCRIPTION       | 
|--------------:|-------------------------|
|.bak           | vanilla backup          |
|.b4anv         | before astronvim        |
|.mine          | your config             |
|.distrotube    | distrotube's config     |
|.kickstart     | kickstart config        |

All 4 of the nvim config directories must exists or the script will abort:

~/.config/nvim

~/.local/share/nvim

~/.local/state/nvim

~/.cache/nvim

You could create any empty directories manually if they don't exist.

Works on macOS, Linux and Windows.

## Installation

git clone https://github.com/chevybeef/nvim-config-move.git

cd nvim-config-move

## Usage

python3 main.py {operation} {extension}

## Examples

python3 main.py move bak

python3 main.py restore bak

note: the dot before the extension is not required

note: the script will abort if it doesn't find all 4 directories (make them manually if required)
