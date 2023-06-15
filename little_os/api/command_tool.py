import os
import shlex
import subprocess
from pathlib import Path

from rich.console import Console

from ..commands import command_list, commands
from ..env.variables import HOME_PATH

console = Console()

ASCII_ART = (
    (" " * 11 + "dainci's").ljust(77)
    + "\n"
    + "                                                                             "
    "\n    █████  ██      ██          ████████  ██████   ██████  ██      ███████    "
    "\n   ██   ██ ██      ██             ██    ██    ██ ██    ██ ██      ██         "
    "\n   ███████ ██      ██             ██    ██    ██ ██    ██ ██      ███████    "
    "\n   ██   ██ ██      ██             ██    ██    ██ ██    ██ ██           ██    "
    "\n   ██   ██ ███████ ███████        ██     ██████   ██████  ███████ ███████    "
    "\n                                                                             "
    "\n                                                          Classic            "
)


def print_title():
    console.print(f"[black on cyan]{ASCII_ART}[/]")
    console.print("[i]this is a beta ![/i]")


def get_prompt() -> str:
    parent_directory = str(Path.cwd())
    folders = parent_directory.split(os.sep)

    last_three_folders = folders[-3:]
    path = os.sep.join(last_three_folders).replace("\\", "/")

    prompt_header = "~/.../" if len(folders) > 3 else ""
    return f"\n[green]┌── {prompt_header}{path} ──┤" f"\n[cyan]└───〉[/]"


def execute_command(user_input: str) -> bool:
    if not user_input:
        return True

    command_name, *args = shlex.split(user_input)

    if user_input.lower() == "exit":
        console.print("[red]ended by user[/]")
        return False

    handler = command_list.get(command_name)
    if handler is None:
        console.print(f"[red]command not recognized[/]")
        return True

    try:
        handler(args)
    except subprocess.CalledProcessError as e:
        console.print(f"[red]Erreur :{str(e)}[/]")
        return False
    else:
        return True


def run() -> None:
    os.chdir(HOME_PATH)
    commands.clear(args=())

    is_running = True
    while is_running:
        try:
            user_input = console.input(get_prompt())

        except (EOFError, KeyboardInterrupt):
            user_input = "exit"

        print(end="\n")
        is_running = execute_command(user_input)
