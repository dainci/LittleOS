from colorama import Fore, Back, Style
import os



def cd(args):
    if not args:
        os.chdir(os.path.expanduser("~"))
    else:
        path = os.path.join(*args)
        if not os.path.isdir(path):
            print("cd: %s: No such directory" % path)
            return
        os.chdir(path)


def clear(args):
    os.system('cls' if os.name == 'nt' else 'clear')


def ls(args):
    import os  # Importer os à l'intérieur de la fonction
    directory = '.'
    files = os.listdir(directory)
    print(Fore.BLUE + '    '.join(files) + Style.RESET_ALL)

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
    if len(args) == 0:
        print(Fore.RED + "Error: OS command requires arguments" + Style.RESET_ALL)
    elif args[0] == "-doc":
        print("OS documentation...")
    elif args[0] == "-v":
        print("v0.1.7")
    elif args[0] == "-info":
        print("OS info...")
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
