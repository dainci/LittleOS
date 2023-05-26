import os
from tabulate import tabulate
from colorama import Fore, Back, Style

def help(args):
    if len(args) == 0:
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
