import subprocess
import sys
import os

requirements_file = os.path.join(os.path.dirname(__file__), "requirements.txt")

if not os.path.isfile(requirements_file):
    print("ERROR: requirements.txt file not found.")
    sys.exit(1)

with open(requirements_file, 'r') as file:
    required_modules = [line.strip() for line in file]

missing_modules = []
for module in required_modules:
    try:
        __import__(module)
    except ImportError:
        missing_modules.append(module)

if missing_modules:
    print("Installation des modules requis...")
    for module in missing_modules:
        subprocess.run([sys.executable, '-m', 'pip', 'install', module], check=True)

from colorama import Fore

print(f"{Fore.GREEN}All modules are up to date{Fore.RESET}")
input("Press Enter to continue...")
