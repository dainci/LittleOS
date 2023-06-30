import os
import shlex
import subprocess
import sys
import time
from pathlib import Path

from rich.console import Console
from program.commands import command_list
from program.commands import commands
from program.env.variables import HOME_PATH

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


def littleos():
    console.print(f"[black on cyan]{ASCII_ART}[/]")
    console.print("[i]this is a beta ![/i]")


commands.clear(())
time.sleep(0.5)

os.chdir(HOME_PATH)

while True:
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
    parts = shlex.split(prompt)
    command = parts[0]
    args = parts[1:]

    # command args
    if prompt.lower() == "exit":
        console.print("[red]ended by user[/]")
        time.sleep(0.3)
        break

    try:
        if command in command_list.cmd:
            command_list.cmd[command](args)

        else:
            console.print("[red]command not recognized[/]")

    except subprocess.CalledProcessError as e:
        console.print(f"[red]Erreur :{str(e)}[/]")
        sys.exit(0)
