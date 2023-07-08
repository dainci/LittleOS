import os
import pathlib
from datetime import datetime
from pathlib import Path
from typing import Tuple
import shutil

from rich import box, print
from rich.console import Console
from rich.table import Table

# our dependencies
import program.api.command_tool as command_tool
from program.env.variables import HOME_PATH, os_version

console = Console()


# all possible command errors
def require_argument(command):
    console.print(
        f"[red]ERROR : [/]{command}"
        f"[red] command require an argument,"
        f" do [help -[/]{command}[red]] for more informations[/]"
    )


def not_an_argument(argument):
    console.print(f"[red]The argument(s) [/]{argument}[red] are not valid argument.[/]")
    console.print(
        "[red]To see all the possible arguments for this command,"
        " do [cyan]help -[command].[/]"
    )


# the help command
def helps(args):
    if len(args) == 0:
        all_help()
    elif args[0] == "-remove":
        print(". file : delete the file you want")
        print(". dir : delete the directory you want")

    elif args[0] == "-littleos":
        print(". -v : show the version of the OS")
        print(". -doc : show the official documentation of the OS")

    elif args[0] == "-python":
        print(". -doc : show the official documentation of Python")

    elif args[0] == "-ls":
        print(". -fi / -file : shows only files")
        print(". -fo / -folder : shows only folders")

    elif args[0] == "-clear":
        print("Deletes all previous commands, needs no arguments to run")

    elif args[0] == "-cp":
        print(". <source> <destination> : copy file or directory")

    elif args[0] == "-mv":
        print(". <source> <destination> : move file or directory")

    elif args[0] == "-cat":
        print(". <file> : display file content")

    elif args[0] == "-echo":
        print(". <text> : display text")

    elif args[0] == "-grep":
        print(". <keyword> <file(s)> : search for keyword in file(s)")

    elif args[0] == "-head":
        print(". <file> [num_lines] : display the first lines of a file")

    else:
        console.print("[red]The argument you want to use is invalid or misspelled.[/]")




def all_help():
    console.print(
        'all the basics commands available. for more specific commands type [cyan]help -[command][/]'
    )

    print("------------------------------------------------ \n"
          "help : all commands \n"
          "exit : exit program \n"
          "clear : clear screen \n"
          "------------------------------------------------ \n"
          "python -[argument] : have information for Python \n"
          "littleos -[argument] : have information for the OS \n"
          "------------------------------------------------ \n"
          "ls -(argument) : list all files in current directory \n"
          "cd <directory> : change directory \n"
          "remove -[argument] <directory> : remove directory \n"
          "make -[argument] <directory> : create a directory \n"
          "------------------------------------------------ \n"
          "cp <source> <destination> : copy file or directory \n"
          "mv <source> <destination> : move file or directory \n"
          "cat <file> : display file content \n"
          "echo <text> : display text \n"
          "grep <keyword> <file(s)> : search for keyword in file(s) \n"
          "head <file> [num_lines] : display the first lines of a file \n")


# copy
def cp(args):
    if len(args) < 2:
        require_argument("cp")
    else:
        source = args[0]
        destination = args[1]
        try:
            shutil.copy2(source, destination)
            print(f"Le fichier {source} a été copié vers {destination}.")
        except FileNotFoundError:
            print(f"Le fichier {source} est introuvable.")
        except IsADirectoryError:
            print(f"{source} est un répertoire, utilisez l'option -r pour copier récursivement.")

# move
def mv(args):
    if len(args) < 2:
        require_argument("mv")
    else:
        source = args[0]
        destination = args[1]
        try:
            shutil.move(source, destination)
            print(f"Le fichier {source} a été déplacé vers {destination}.")
        except FileNotFoundError:
            print(f"Le fichier {source} est introuvable.")
        except IsADirectoryError:
            print(f"{source} est un répertoire, utilisez l'option -r pour déplacer récursivement.")


# see in a file
def cat(args):
    if len(args) < 1:
        require_argument("cat")
    else:
        file_path = args[0]
        try:
            with open(file_path, 'r') as file:
                content = file.read()
                print(content)
        except FileNotFoundError:
            print(f"Le fichier {file_path} est introuvable.")

# head
def head(args):
    if len(args) < 1:
        require_argument("head")
    else:
        file_path = args[0]
        num_lines = 10  # Par défaut, affiche les 10 premières lignes
        if len(args) > 1:
            try:
                num_lines = int(args[1])
            except ValueError:
                print("Le nombre de lignes spécifié est invalide.")
                return

        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                for line in lines[:num_lines]:
                    print(line.strip())
        except FileNotFoundError:
            print(f"Le fichier {file_path} est introuvable.")

# grep
def grep(args):
    if len(args) < 2:
        require_argument("grep")
    else:
        keyword = args[0]
        files = args[1:]
        for file_path in files:
            try:
                with open(file_path, 'r') as file:
                    lines = file.readlines()
                    if matching_lines := [
                        line for line in lines if keyword in line
                    ]:
                        print(f"Occurrences de '{keyword}' dans le fichier {file_path}:")
                        for line in matching_lines:
                            print(line.strip())
                    else:
                        print(f"Aucune occurrence de '{keyword}' dans le fichier {file_path}.")
            except FileNotFoundError:
                print(f"Le fichier {file_path} est introuvable.")


# echo
def echo(args):
    if len(args) < 1:
        require_argument("echo")
    else:
        text = ' '.join(args)
        print(text)


# clear command
def clear(args):
    if len(args) == 0:
        os.system("cls" if os.name == "nt" else "clear")
        command_tool.littleos()
    else:
        not_an_argument(args)


# LittleOS commands
def little_os(args):
    possible_arguments = {
        "-v": f"[cyan]your os version is: {os_version}[/]",
        "-doc": "[cyan]Official LittleOS documentation: "
                "[blue]https://github.com/dainci/LittleOS/wiki[/] (ctrl + click)"
    }

    if len(args) == 0:
        require_argument("littleos")
    elif args[0] in possible_arguments:
        console.print(possible_arguments[args[0]])
    else:
        not_an_argument(args)


# python
def python(args):
    possible_arguments = {
        "-doc": "[cyan]Official Python documentation: "
                "[blue]https://docs.python.org/3/[/] (ctrl + click)"
    }

    if len(args) == 0:
        require_argument("Python")
    elif args[0] in possible_arguments:
        console.print(possible_arguments[args[0]])
    else:
        not_an_argument(args)


def ls(args):
    content = {"file": [], "dir": []}

    for entry in Path.cwd().iterdir():
        if entry.is_dir():
            content["dir"].append(entry.name)
        elif entry.is_file():
            content["file"].append(entry.name)

    def find_arguments(keys: Tuple[str, ...]) -> bool:
        return any(arg_key in args for arg_key in keys)

    is_file_only = find_arguments(("-fi", "-file"))
    is_folder_only = find_arguments(("-fo", "-folder"))

    if is_file_only and is_folder_only:
        print("Illegal combinaison, cannot display file only if folder only is enabled")
        return

    if is_file_only:
        directory_contents = content["file"]
    elif is_folder_only:
        directory_contents = content["dir"]
    else:
        directory_contents = content["dir"] + content["file"]

    def path_info(filepath: str) -> Tuple[str, str, str]:
        timestamp = os.path.getmtime(filepath)
        return (
            str(datetime.fromtimestamp(timestamp)),
            f"[yellow]{os.path.getsize(filepath)}[/]",
            f"[cyan]{os.path.basename(filepath)}[/]",
        )

    table = Table(show_header=True, header_style="bold", box=box.SIMPLE_HEAD)

    table.add_column("Date")
    table.add_column("Poids", justify="right")
    table.add_column("Nom")

    for path in directory_contents:
        table.add_row(*path_info(path))

    console.print(table)


def cd_command(args):
    target_path = HOME_PATH if len(args) == 0 else pathlib.Path.cwd() / args[0]
    try:
        os.chdir(target_path.absolute())
    except FileNotFoundError:
        print("cd: no such file or directory:", target_path.name)
    except NotADirectoryError:
        print("cd: not a directory:", target_path.name)
    except Exception as e:
        print("cd: error", e.__cause__)


def make(args):
    if not args:
        require_argument("make")
    elif args[0] == 'dir':
        try:
            os.makedirs(str(args[1]), exist_ok=True)
            print(f"The directory [blue]{args[1]}[/] was successfully created.")
        except Exception as e:
            print(f"Error when creating the directory {args[1]}: {str(e)}.")
    elif args[0] == 'file':
        try:
            with open(str(args[1]), 'w') as f:
                f.write('')
            print(f"The file [blue]{args[1]}[/] was successfully created.")
        except FileExistsError:
            print(f"The file [blue]{args[1]}[/] already exists.")
        except Exception as e:
            print(f"Error when creating the file [blue]{args[1]}[/]: {str(e)}.")
    else:
        print(f"make takes one argument, but {len(args)} were given.")



def remove(args):
    if not args:
        require_argument("remove")

    elif args[0] == "-dir":
        try:
            os.rmdir(str(args[1]))
            print(f"The directory [blue]{args[1]}[/] was successfully removed.")
        except FileNotFoundError:
            print(f"The directory [blue]{args[1]}[/] do not exist.")
        except OSError as e:
            print(f"Error while deleting directory [blue]{args[1]}[/]: {str(e)}")

    elif args[0] == "-file":
        try:
            os.remove(str(args[1]))
            print(f"The file [blue]{args[1]}[/] was successfully removed.")
        except FileNotFoundError:
            print(f"The file [blue]{args[1]}[/] do not exist.")
        except OSError as e:
            print(f"Error while deleting file [blue]{args[1]}[/]: {str(e)}")

    elif len(args) > 2:
        print(f"make takes one given argument but {len(command_tool.args)} were given")
