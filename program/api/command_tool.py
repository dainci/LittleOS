#import exeptions
from program.commands import commands
from program.commands import command_list

from colorama import Fore, Back, Style
import shlex
import subprocess
import time
import os



def littleos():
    print(Back.CYAN + Fore.BLACK + "           dainci                                                            ")
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
littleos()

time.sleep(0.5)


while True:
    current_file = os.path.dirname(os.path.abspath(__file__))
    parent_directory = os.path.dirname(current_file)
    os.chdir(parent_directory)
    folders = parent_directory.split(os.sep)
    last_three_folders = folders[-3:]
    path = os.sep.join(last_three_folders).replace('\\', '/')
    prompt = input(f"\n{Fore.GREEN}┌── {'~/.../' if len(folders) > 3 else ''}{path} ──┤\n{Fore.CYAN}└───〉{Fore.RESET}")
    print("")

    if not prompt:
        continue
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