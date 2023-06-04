import os
from tabulate import tabulate
from colorama import Fore, Back, Style
from itertools import chain

# commande help

def helps(args):
    if len(args) == 0:
        print("")
        print("all the basics commands available. for more specific commands type 'help -[command]' ")
        print("------------------------------------------------")
        print("help : all commands")
        print("exit : exit program")
        print("clear : clear screen")
        print("python -[argument] : possible commands to see the version, have information or documentation of Python")
        print("os -[argument] : possible commands to see the version, have information or documentation of the OS")
        print("ls : list all files in current directory")
        print("cd <directory> : change directory")
        print("rm <directory> : remove directory")
        print("mkdir <directory> : create a directory")
        print("touch <file> : create a file")
    elif args[0] == "-os":
        print(". -v : show the version of the OS")
        print(". -doc : show the oficial documentation of the OS")
        print(". -info : shows useful information about your OS")
    elif args[0] == "-python":
        print(". -doc : show the official documentation of python")
    else:
        print(Fore.RED + "the argument you want to use is invalid or misspelled" + Style.RESET_ALL)

# navigation dans le systeme

def ls(args):
    all_folders = [f for f in os.listdir() if os.path.isdir(os.path.join(f))]
    all_files = [f for f in os.listdir() if os.path.isfile(os.path.join(f))]
    directory_contents = []
    directory_contents.append(all_folders); directory_contents.append(all_files)
    directory_contents_flat = list(chain.from_iterable(directory_contents))
    directory_contents_flat.sort()

    if len(args) == 0:
            print(f"{Fore.LIGHTCYAN_EX}{directory_contents_flat}{Fore.RESET}")

            print(tabulate(directory_contents_flat))

            

    elif args[0] == "-fi" or "-file":
        files = [f for f in os.listdir() if os.path.isfile(os.path.join(f))]
        for file in files:
            print(Fore.LIGHTBLUE_EX + file + Fore.RESET)
            

    elif args[0] == "-fo" or "-folder":
        for element in os.listdir(os.path.curdir):
            chemin = os.path.join(os.path.curdir, element)
            if os.path.isdir(chemin):
                print(element)