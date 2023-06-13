
import os
import pathlib
from datetime import datetime
from pathlib import Path
from typing import Tuple

from colorama import Fore, Style
from tabulate import tabulate

# our dependencies
import program.api.command_tool as command_tool


# all possible command errors
def require_argument(command):
    print(f"{Fore.RED}ERROR : {Fore.WHITE}{command}{Fore.RED} command require an argument, do [help -{Fore.WHITE}{command}{Fore.RED}] for more informations{Fore.RESET}")
    
def not_an_argument(argument):
    print(f"{Fore.RED}The argument(s) {Fore.WHITE}{argument}{Fore.RED} are not valid argument.{Fore.RESET}")
    print(f"{Fore.RED}To see all the possible arguments for this command, do {Fore.CYAN}help -[command].{Fore.RESET}")


# the help command
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

    elif args[0] == "-clear":
        print("Deletes all previous commands, needs no arguments to run")

    else:
        print(Fore.RED + "the argument you want to use is invalid or misspelled" + Style.RESET_ALL)

# clear command
def clear(args):
    if len(args) == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        command_tool.littleos()
    else:
        not_an_argument(args)

# LittleOS commands
def little_os(args):
    import main
    if len(args) == 0:
        require_argument("os")
    elif args[0] == "-v":
        print(Fore.CYAN + "your os version is :" + main.os_version + Fore.RESET)
    elif args[0] == "-doc":
        print(Fore.CYAN + "Official LittleOS documentation : " + Fore.BLUE + "https://github.com/dainci/LittleOS/wiki" + Fore.RESET)
    else:
        not_an_argument(args)
    

# python
def python(args):
    if len(args) == 0:
        require_argument("python")
    elif args[0] == "-doc":
        print(Fore.BLUE + "https://docs.python.org/3/" + Fore.RESET)


def ls(args):
    """Navigation dans le système."""
    content = {'file': [], 'dir': []}

    for entry in Path.cwd().iterdir():
        if entry.is_dir():
            content['dir'].append(entry.name)
        elif entry.is_file():
            content['file'].append(entry.name)

    def find_arguments(keys: Tuple[str, ...]) -> bool:
        return any(arg_key in args for arg_key in keys)

    is_file_only = find_arguments(("-fi", "-file"))
    is_folder_only = find_arguments(("-fo", "-folder"))

    if is_file_only and is_folder_only:
        print("Illegal combinaison, cannot display file only if folder only is enabled")
        return

    if is_file_only:
        directory_contents = content['file']
    elif is_folder_only:
        directory_contents = content['dir']
    else:
        directory_contents = content['dir'] + content['file']

    def path_info(path: str) -> Tuple[str, str, str]:
        timestamp = os.path.getmtime(path)
        return (
            str(datetime.fromtimestamp(timestamp)),
            f"{Fore.YELLOW}{os.path.getsize(path)}{Fore.RESET}",
            f"{Fore.CYAN}{os.path.basename(path)}{Fore.RESET}"
        )


    print(
        tabulate(
            [
                path_info(path)
                for path in directory_contents
            ],
            headers=("Date", "Poids", "Nom")
        )
    )


def cd_command(args):
    if len(args) == 0:
        target_path = pathlib.Path.cwd() / "program" / "home"
    else:
        target_path = (pathlib.Path.cwd() / args[0])

    try:
        os.chdir(target_path.absolute())
    except FileNotFoundError:
        print(f"cd: no such file or directory:", target_path.name)
    except NotADirectoryError:
        print("cd: not a directory:", target_path.name)
    except Exception as e:
        print("cd: error", e.__cause__)
