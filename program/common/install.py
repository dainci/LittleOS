import subprocess
import os

from program.api import command_tool

def install_module(module_name):
    try:
        subprocess.check_call(["pip", "install", module_name])
        print(f"the {module_name} module has been correctly installed or updated.")
    except subprocess.CalledProcessError:
        print(f"Error : failed to install {module_name}.")

# Liste des modules à installer
modules_to_install = [
    'colorama',
    'time',
    'shlex',
    'tabulate',
    'tqdm',
    'shlex',
    'PrettyTable',
]

# Installation des modules un par un
for module in modules_to_install:
    install_module(module)
    lambda args: (os.system('cls' if os.name == 'nt' else 'clear'), command_tool.littleos())