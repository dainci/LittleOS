from colorama import Fore, Back, Style
import os
from tabulate import tabulate

OSversion = 'v0.1.8'

def cd(args):
    if not args:
        os.chdir(os.path.expanduser("~"))
    else:
        path = os.path.join(*args)
        if not os.path.isdir(path):
            print("cd: %s: No such directory" % path)
            return
        os.chdir(path)


"""def clear_screen(args):
    if len(args) == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        print(Fore.RED + "this commands dont have any arguments" + Style.RESET_ALL)"""
        


def ls(args):
    import os
    

    if '-fi' in args and '-fo' in args:
        print(Fore.RED + "Error: Cannot specify both -fi and -fo.")
        return
    elif '-fi' in args:
        files = [f for f in os.listdir() if os.path.isfile(f)]
        for file in files:
            print(file)
    else:
        folders = [f for f in os.listdir() if os.path.isdir(f)]
        for folder in folders:
            print(folder)
    

"""
def mkdir(args):
    if not args:
        print("mkdir: missing operand")
        return
    try:
        os.makedirs(args[0])
    except FileExistsError:
        print(f"mkdir: cannot create directory '{args[0]}': File exists")
"""
    
    
def os(args):
    url = "https://github.com/dainci/LittleOS/wiki"
    
    if len(args) == 0:
        print(Fore.RED + "Error: OS command requires arguments" + Style.RESET_ALL)
    elif args[0] == "-doc":
        print("The official documentation of LittleOS : " + Fore.CYAN + url + Style.RESET_ALL)
    elif args[0] == "-v":
        print(OSversion)
    elif args[0] == "-info":
        table_data = [
        ["users", "OS version", "OS type"],
        ["username", OSversion, Fore.CYAN + "Classic" + Style.RESET_ALL],
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


def rm(file_path):
    try:
        os.remove(file_path)
    except OSError:
        print(f"Erreur: Impossible de supprimer {file_path}")


def touch(file_path):
    """Crée un fichier vide avec le chemin spécifié"""
    try:
        with open(file_path, 'a'):
            os.utime(file_path, None)
    except OSError:
        print(f"Erreur: Impossible de créer {file_path}")
         

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
