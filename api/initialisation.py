from variables import commands, errors

from colorama import Fore, Back, Style
import shlex
import os
import time

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

username = "classic"
current_file = os.path.dirname(os.path.abspath(__file__))


def unknown_command(args):
    print(f"{Fore.RED}Unknown command{Style.RESET_ALL}")



def command_prompt(username):
    parent_directory = os.path.dirname(current_file)
    os.chdir(parent_directory)
    folders = parent_directory.split(os.sep)
    last_three_folders = folders[-3:]
    path = os.sep.join(last_three_folders).replace('\\', '/')
    prompt = f"{Fore.GREEN}{'~/.../' if len(folders) > 3 else ''}{path}   {Fore.CYAN}\n=[{username}]=> {Fore.RESET}"
    return prompt

try:
    while True:
        print(Style.RESET_ALL)
        command = input(f"{Fore.WHITE}{command_prompt(username)}{Style.RESET_ALL}")
        print(Style.RESET_ALL)
        parts = shlex.split(command)
        cmd = parts[0]
        args = parts[1:]
        try:
            pass
        except Exception as e:
            errors.handle_error(cmd, args)
            print("Error:", e)
except KeyboardInterrupt:
    print("Program terminated by user")
    u = input("enter to quit")