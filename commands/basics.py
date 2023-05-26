import os
from tabulate import tabulate
from colorama import Fore, Back, Style

# Ouvrir le fichier en mode lecture
'''with open('../docs/os_info.txt', 'r') as file:
    # Parcourir chaque ligne du fichier
    for line in file:
        # Diviser la ligne en clé et valeur en utilisant le signe "="
        key, value = line.strip().split('=')
        # Supprimer les espaces inutiles autour de la clé et de la valeur
        key = key.strip()
        value = value.strip()
        # Utiliser des conditions pour affecter les valeurs aux variables appropriées
        if key == 'OS version':
            osversion = value
        elif key == 'OS type':
            ostype = value'''



def os(args):
    url = "https://github.com/dainci/LittleOS/wiki"
    
    if len(args) == 0:
        print(Fore.RED + "Error: OS command requires arguments" + Style.RESET_ALL)
    elif args[0] == "-doc":
        print("The official documentation of LittleOS : " + Fore.CYAN + url + Style.RESET_ALL)
    elif args[0] == "-v":
        print(osversion)
    elif args[0] == "-info":
        table_data = [
        ["users", "OS version", "OS type"],
        ["username", osversion, Fore.CYAN + ostype + Style.RESET_ALL],
        ]
        table = tabulate(table_data, headers="firstrow", tablefmt="fancy_grid")
        print(table)
    else:
        print(Fore.RED + "Unknown OS command" + Style.RESET_ALL)
        

def python(args):
    url = "https://docs.python.org/3/library/"
    
    if len(args) == 0:
        print(Fore.RED + "Error: OS command requires arguments" + Style.RESET_ALL)
    elif args[0] == "-doc":
        print(f"the official documentation for Python : " + Fore.CYAN + url + Style.RESET_ALL)
    else:
        print(Fore.RED + "Unknown OS command" + Style.RESET_ALL)