import os
import shlex
import subprocess
import sys
import time
from pathlib import Path

from prompt_toolkit import prompt
from prompt_toolkit.completion import Completer, PathCompleter, WordCompleter
from prompt_toolkit.completion import WordCompleter
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

class FusionCompleter(Completer):
    def __init__(self, options):
        self.word_completer = WordCompleter(options)
        self.path_completer = PathCompleter()

    def get_completions(self, document, complete_event):
        text = document.text_before_cursor
        if '/' in text:
            yield from self.path_completer.get_completions(document, complete_event)
        else:
            yield from self.word_completer.get_completions(document, complete_event)

tab_completion = FusionCompleter(command_list.cmd)

while True:
    """
    Faire une variable qui prend le nom du dossier nommé "home" pour les intimes
    """
    parent_directory = str(Path.cwd())
    folders = parent_directory.split(os.sep)

    last_three_folders = folders[-3:]
    path = os.sep.join(last_three_folders).replace("\\", "/")

    prompt_header = "~/.../" if len(folders) > 3 else ""
    prompts = prompt(
        f"\n┌── {prompt_header}{path} ──┤"
        f"\n└───〉",
        completer=tab_completion,
    )
    print("")

    if not prompts:
        continue
    else:
        parts = shlex.split(prompts)
        command = parts[0]
        args = parts[1:]

    # command args
    if prompts.lower() == "exit":
        console.print("[red]ended by user[/]")
        time.sleep(0.3)
        break



    try:
        if command in command_list.cmd:
            command_list.cmd[command](args)

        else:
            console.print(f"[red]command not recognized[/]")

    except subprocess.CalledProcessError as e:
        console.print(f"[red]Erreur :{str(e)}[/]")
        sys.exit(0)
