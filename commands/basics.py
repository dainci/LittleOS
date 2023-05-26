import os
from tabulate import tabulate
from colorama import Fore, Back, Style

osversion = 'v0.1.9'
ostype = ''

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