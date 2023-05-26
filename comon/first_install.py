import subprocess

# Modules requis
required_modules1 = ['tqdm', 'sys']

def install_modules():
    print("Installation des modules requis...")
    for module in required_modules1:
        subprocess.run(['pip', 'install', module], check=True)

    print("installer les modules requis ? (y/n)")

if __name__ == '__main__':
    install_modules()

import importlib
import subprocess
import sys
from tqdm import tqdm
import colorama

# Liste des modules requis
required_modules = ['colorama', 'os', 'tabulate', 'time', 'shlex']

def check_install_modules():
    # Check if the modules are already installed
    missing_modules = []
    for module in tqdm(required_modules, desc='Checking modules'):
        try:
            importlib.import_module(module)
        except ImportError:
            missing_modules.append(module)

    # Install the colorama module first
    if 'colorama' in missing_modules:
        print("Installing colorama module...")
        subprocess.run([sys.executable, '-m', 'pip', 'install', 'colorama'], check=True)
        print("Installation complete.")
        colorama.init()

    # Install other required modules
    if missing_modules:
        print("\nInstalling required modules...")
        for module in tqdm(missing_modules, desc='Installing modules'):
            subprocess.run([sys.executable, '-m', 'pip', 'install', module], check=True)

    # Display installation status for each module
    print("\nModule installation report:")
    for module in required_modules:
        try:
            importlib.import_module(module)
            print(f"{module}: {colorama.Fore.GREEN}installed{colorama.Style.RESET_ALL}")
        except ImportError:
            print(f"{module}: {colorama.Fore.RED}not installed{colorama.Style.RESET_ALL}")

    # Update pip
    print("\nUpdating pip...")
    subprocess.run([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'], check=True)
    print("pip update complete.")

    # Display a centered completion message
    print("\n" + "=" * 50)
    print("{:^50}".format("Installation complete."))
    print("{:^50}".format("You can now close this window"))
    print("{:^50}".format("and open main.py."))
    print("=" * 50)

    # Show a progress bar
    with tqdm(total=100, desc='Processing') as pbar:
        # Perform processing
        for _ in range(100):
            pbar.update(1)
        pbar.set_description('Processing complete')

go = input("--> ")
if go == "y":
    check_install_modules()
else:
    exit
