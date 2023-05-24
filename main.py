import commands
from colorama import Fore, Back, Style
import time
import shlex
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

username = "classic"
default_path = os.path.dirname(os.path.abspath(__file__))

cmds = {
#    'cd': commands.cd,
    'clear': lambda args: (os.system('cls' if os.name == 'nt' else 'clear'), littleos()),
    'exit': exit,
    'help': commands.help,
    'ls': commands.ls,
#    'mkdir': commands.mkdir,
    'os': commands.os, # -doc; -info; -v
    'python': commands.python, #doc
#    'rm': commands.rm,
#    'touch': commands.touch,

}


def unknown_command(args):
    print(Fore.RED + "Unknown command" + Style.RESET_ALL)

def command_prompt(username):
    directory = os.getcwd().replace('\\', '/')
    prompt = Fore.GREEN + "⁅" + directory + "⁆" + Fore.CYAN + "\n-{" + username + "}-> "
    return prompt

while True:
    print(Style.RESET_ALL)
    command = input(Fore.GREEN + command_prompt(username) + Style.RESET_ALL)
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
