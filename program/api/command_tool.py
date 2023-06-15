#import exeptions
from program.commands import commands
from program.commands import command_list
from program.env import variables

from pathlib import Path

from colorama import Fore, Back, Style
import shlex
import subprocess
import time
import os
import sys


def littleos():
    print(Back.CYAN + Fore.BLACK + "           dainci's                                                          ")
    print("                                                                             ")
    print("    █████  ██      ██          ████████  ██████   ██████  ██      ███████    ")
    print("   ██   ██ ██      ██             ██    ██    ██ ██    ██ ██      ██         ")
    print("   ███████ ██      ██             ██    ██    ██ ██    ██ ██      ███████    ")
    print("   ██   ██ ██      ██             ██    ██    ██ ██    ██ ██           ██    ")
    print("   ██   ██ ███████ ███████        ██     ██████   ██████  ███████ ███████    ")
    print("                                                                             ")
    print("                                                          Classic            ")
    print(Style.RESET_ALL)
    print("this is a beta !")
commands.clear(())

time.sleep(0.5)


while True:
    """
    Faire une variable qui prend le nom du dossier nommé "home" pour les intimes 
    """
    parent_directory = str(Path.cwd())
    folders = parent_directory.split(os.sep)

    last_three_folders = folders[-3:]
    path = os.sep.join(last_three_folders).replace('\\', '/')
    prompt = input(f"\n{Fore.GREEN}┌── {'~/.../' if len(folders) > 3 else ''}{path} ──┤\n{Fore.CYAN}└───〉{Fore.RESET}")
    print("")

    if not prompt:
        continue
    else:
        parts = shlex.split(prompt)
        command = parts[0]
        args = parts[1:]

#    command args args
    if prompt.lower() == "exit":
        print("ended by user")
        time.sleep(0.3)
        break

    try:
        if command in command_list.cmd:
            command_list.cmd[command](args)
        
        else:
            print(f"{Fore.RED}command not recognized{Fore.RESET}")

    except subprocess.CalledProcessError as e:
        print(f"{Fore.RED}Erreur :{str(e)}")
        sys.exit(0)
