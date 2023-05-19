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


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def ls(directory='.'):
    files = os.listdir(directory)
    print(Fore.BLUE + '    '.join(files) + Style.RESET_ALL)

'''
def mkdir(args):
    if not args:
        print("mkdir: missing operand")
        return
    try:
        os.makedirs(args[0])
    except FileExistsError:
        print(f"mkdir: cannot create directory '{args[0]}': File exists")
'''

def os_doc():
    url = "https://www.google.com/"
    print(f"the official documentation for LittleOS : " + Fore.CYAN + url + Style.RESET_ALL)


def os_info():
    print(Fore.BLUE + "your version of LittleOS is a classic version, "
                      "which means that no software are preinstalled on it " + Style.RESET_ALL)


def os_version():
    print(Fore.BLUE + "LittleOS V0.0.1 " + Style.RESET_ALL)


def python_doc():
    url = "https://docs.python.org/3/library/"
    print(f"the official documentation for Python : " + Fore.CYAN + url + Style.RESET_ALL)


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


def unknown_command():
    print(Fore.RED + "Unknown command" + Style.RESET_ALL)


def command_prompt(tool):
    return f"{tool} $ "


def help():
    print("help : all commands")
    print("exit : exit program")
    print("clear : clear screen")
    print("python -doc : shows the official documentation of Python")
    print("os -doc : shows the official documentation of littleOS")
    print("os -v : shows the version of littleOS")
    print("ls : list all files in current directory")
    print("cd <directory> : change directory")
    print("rm <directory> : remove directory")
    print("mkdir <directory> : create a directory")
    print("touch <file> : create a file")
