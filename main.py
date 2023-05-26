from commands import basics, help_command, navigation
from errors import osErrors

from colorama import Fore, Back, Style
import time
import shlex
import os
import sys

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
default_path = os.path.dirname(os.path.abspath(__file__))


cmds = {
    'cd': navigation.cd,
    'clear': lambda args: (os.system('cls' if os.name == 'nt' else 'clear'), littleos()),
    'exit': exit,
    'help': help_command.help,
    'ls': navigation.ls,
    'mkdir': navigation.mkdir,
    'os': basics.os, # -doc; -info; -v
    'python': basics.python, #doc
    'rm': navigation.rm,
    'touch': navigation.touch,
}


def unknown_command(args):
    print(f"{Fore.RED}Unknown command{Style.RESET_ALL}")

def command_prompt(username):
    directory = os.getcwd().replace('\\', '/')
    prompt = f"{Fore.GREEN}⁅{directory}⁆{Fore.CYAN}\n-[{username}]-> {Fore.RESET}"
    return prompt


try:
    while True:
        print(Style.RESET_ALL)
        command = input(f"{Fore.WHITE}{command_prompt(username)}{Style.RESET_ALL}")
        print(Style.RESET_ALL)
        parts = shlex.split(command)
        cmd = parts[0]
        args = parts[1:]
        if cmd == "cd":
            if args:
                os.chdir(args[0])
            else:
                print("Error: cd command requires an argument")
        else:
            fn = cmds.get(cmd, unknown_command)
            fn(args)
except:
    osErrors.handle_error(command, args)