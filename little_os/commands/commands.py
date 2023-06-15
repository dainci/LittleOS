import os
import pathlib
from datetime import datetime
from pathlib import Path
from typing import Tuple

from rich import box
from rich.console import Console
from rich.table import Table

# our dependencies
from ..api import command_tool
from ..env.variables import HOME_PATH, os_version

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
        console.print(
            f"all the basics commands available."
            f" for more specific commands type"
            f" [cyan]help -[command][/]"
        )

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
        console.print("[red]the argument you want to use is invalid or misspelled[/]")


# clear command
def clear(args):
    if len(args) == 0:
        os.system("cls" if os.name == "nt" else "clear")
        command_tool.print_title()
    else:
        not_an_argument(args)


# LittleOS commands
def little_os(args):
    if len(args) == 0:
        require_argument("os")
    elif args[0] == "-v":
        console.print(f"[cyan]your os version is :{os_version}[/]")
    elif args[0] == "-doc":
        console.print(
            "[cyan]Official LittleOS documentation:"
            " [blue]https://github.com/dainci/LittleOS/wiki[/]"
        )
    else:
        not_an_argument(args)


# python
def python(args):
    if len(args) == 0:
        require_argument("python")
    elif args[0] == "-doc":
        console.print("[blue]https://docs.python.org/3/[/]")


def ls(args):
    """Navigation dans le système."""
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
    if len(args) == 0:
        target_path = HOME_PATH
    else:
        target_path = pathlib.Path.cwd() / args[0]

    try:
        os.chdir(target_path.absolute())
    except FileNotFoundError:
        print(f"cd: no such file or directory:", target_path.name)
    except NotADirectoryError:
        print("cd: not a directory:", target_path.name)
    except Exception as e:
        print("cd: error", e.__cause__)


def mkfile(args):
    if len(args) == 0:
        print("mkfile takes one given argument but 0 were given")
    elif len(args) > 1:
        print(
            f"mkfile takes one given argument but {len(command_tool.args)} were given"
        )
    else:
        try:
            with open(
                str(args).replace("[", "").replace("]", "").replace("'", ""), "w"
            ) as f:
                f.write("")
            print(f"Le fichier {args} a été créé avec succès.")
        except FileExistsError:
            print(f"Le fichier {args} existe déjà.")
        except Exception as e:
            print(f"Erreur lors de la création du fichier {args}: {str(e)}")


def rmdir(args):
    if len(args) == 0:
        print("mkdir takes one given argument but 0 were given")
    elif len(args) > 1:
        print(f"mkdir takes one given argument but {len(command_tool.args)} were given")
    else:
        try:
            os.rmdir(str(args).replace("[", "").replace("]", "").replace("'", ""))
            print(f"Le dossier {args} a été supprimé avec succès.")
        except FileNotFoundError:
            print(f"Le dossier {args} n'existe pas.")
        except OSError as e:
            print(f"Erreur lors de la suppression du dossier {args}: {str(e)}")


def rmfile(args):
    if len(args) == 0:
        print("mkdir takes one given argument but 0 were given")
    elif len(args) > 1:
        print(f"mkdir takes one given argument but {len(command_tool.args)} were given")
    else:
        try:
            os.remove(str(args).replace("[", "").replace("]", "").replace("'", ""))
            print(f"Le fichier {args} a été supprimé avec succès.")
        except FileNotFoundError:
            print(f"Le fichier {args} n'existe pas.")
        except OSError as e:
            print(f"Erreur lors de la suppression du fichier {args}: {str(e)}")
