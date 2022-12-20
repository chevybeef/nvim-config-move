# nvim-config-move
A script to move the current nvim config out the way in order to experiment with other configurations. Not tested at all on Windows yet.

## Usage

python3 main.py {operation} {extension}

## Installation
git clone https://github.com/chevybeef/nvim-config-move.git

cd nvim-config-move

## Examples

python3 main.py move bak

python3 main.py restore bak

note: the dot before the extension is not required

note: the script will abort if it doesn't find all 4 directories (make them manually if required)
