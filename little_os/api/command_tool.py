import os
import shlex
import subprocess
import sys
import time
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


def run():
    os.chdir(HOME_PATH)
    commands.clear(())

    while True:
        """
        Faire une variable qui prend le nom du dossier nommé "home" pour les intimes
        """
        parent_directory = str(Path.cwd())
        folders = parent_directory.split(os.sep)

        last_three_folders = folders[-3:]
        path = os.sep.join(last_three_folders).replace("\\", "/")

        prompt_header = "~/.../" if len(folders) > 3 else ""
        prompt = console.input(
            f"\n[green]┌── {prompt_header}{path} ──┤" f"\n[cyan]└───〉[/]"
        )
        print("")

        if not prompt:
            continue
        else:
            parts = shlex.split(prompt)
            command = parts[0]
            args = parts[1:]

        # command args
        if prompt.lower() == "exit":
            console.print("[red]ended by user[/]")
            time.sleep(0.3)
            break

        try:
            if command in command_list:
                command_list[command](args)

            else:
                console.print(f"[red]command not recognized[/]")

        except subprocess.CalledProcessError as e:
            console.print(f"[red]Erreur :{str(e)}[/]")
            sys.exit(0)
