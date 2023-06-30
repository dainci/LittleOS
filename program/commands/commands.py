import os
from datetime import datetime

from tabulate import tabulate
from colorama import Fore, Back, Style
from itertools import chain
from pathlib import Path

# all errors posible

def require_argument(command):
    print(f"{Fore.RED}ERROR : {Fore.WHITE}{command}{Fore.RED} command require an argument, do [help -{Fore.WHITE}{command}{Fore.RED}] for more informations{Fore.RESET}")
    
def not_an_argument(argument):
    print(f"{Fore.RED}The argument(s) {Fore.WHITE}{argument}{Fore.RED} are not valid argument.{Fore.RESET}")
    print(f"{Fore.RED}To see all the possible arguments for this command, do {Fore.CYAN}help -[command].{Fore.RESET}")





# commande help

def helps(args):
    if len(args) == 0:
        print(f"all the basics commands available. for more specific commands type {Fore.CYAN}help -[command]{Fore.RESET}")
        print("------------------------------------------------")
        print("help : all commands")
        print("exit : exit program")
        print("clear : clear screen")
        print("------------------------------------------------")
        print("python -[argument] : have information for Python")
        print("os -[argument] : have information for the OS")
        print("------------------------------------------------")
        print("ls -(argument) : list all files in current directory")
        # print("cd <directory> : change directory")
        # print("rm <directory> : remove directory")
        # print("mkdir <directory> : create a directory")
        # print("touch <file> : create a file")

    elif args[0] == "-os":
        print(". -v : show the version of the OS")
        print(". -doc : show the oficial documentation of the OS")

    elif args[0] == "-python":
        print(". -doc : show the official documentation of python")

    elif args[0] == "-ls":
        print(". -fi / -file : shows only files")
        print(". -fo / -folder : shows only folders")
    else:
        print(
            f"{Fore.RED}the argument you want to use is invalid or misspelled{Style.RESET_ALL}"
        )

# os
def os_command(args):
    import main
    if len(args) == 0:
        require_argument("os")
    elif args[0] == "-v":
        print(f"{Fore.CYAN}your os version is :{main.os_version}{Fore.RESET}")
    elif args[0] == "-doc":
        print(
            f"{Fore.CYAN}Official LittleOS documentation : {Fore.BLUE}https://github.com/dainci/LittleOS/wiki{Fore.RESET}"
        )
    else:
        not_an_argument(args)
    

# python
def python(args):
    if len(args) == 0:
        require_argument("python")
    elif args[0] == "-doc":
        print(f"{Fore.BLUE}https://docs.python.org/3/{Fore.RESET}")




# navigation dans le systeme

def ls(args):
    all_folders = [element.name for element in Path.cwd().iterdir() if element.is_dir()]
    all_files= [element.name for element in Path.cwd().iterdir() if element.is_file()]

    directory_contents = []
    directory_contents.append(all_folders)
    directory_contents.append(all_files)
    directory_contents_flat = sorted(chain.from_iterable(directory_contents))
    def get_date_modified(path):
        timestamp = os.path.getmtime(path)
        date_modified = datetime.fromtimestamp(timestamp)
        return date_modified

    def get_size(path):
        size = os.path.getsize(path) if os.path.isfile(path) else "-"
        return size



    if len(args) == 0:
            print(f"{Fore.LIGHTCYAN_EX}{directory_contents_flat}{Fore.RESET}")

            tableau = []
            for path in directory_contents_flat:
                date_modified = get_date_modified(path) #je sais pas quoi metre dans get_modified()
                size = get_size(path)
                name = os.path.basename(path)
                tableau.append([date_modified, size, name])

            # Affichage du tableau
            headers = ["Date", "Poids", "Nom"]
            print(tabulate(tableau, headers=headers))


    elif args[0] == "-fi" or "-file":
            print(f"{Fore.LIGHTCYAN_EX}{all_files}{Fore.RESET}")


    elif args[0] == "-fo" or "-folder":
        print(f"{Fore.LIGHTCYAN_EX}{all_folders}{Fore.RESET}")
