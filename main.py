import commands
from colorama import Fore, Back, Style
import time
import shlex
import os

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
time.sleep(0.5)

selected_tool = "classic"
default_path = os.path.dirname(os.path.abspath(__file__))

cmds = {
    'cd': commands.cd,
    'clear': commands.clear,
    'exit': exit,
    'help': commands.help,
    'ls': commands.ls,
#   'mkdir': commands.mkdir,
    'os -doc': commands.os_doc,
    'os -info': commands.os_info,
    'os -v': commands.os_version,
    'python -doc': commands.python_doc,
    'rm': commands.rm,
    'touch': commands.touch,

}


def unknown_command():
    print("unknown command")


def command_prompt(selected_tool):
    directory = os.getcwd().replace('\\', '/')
    prompt = Fore.GREEN + "⁅" + directory + "⁆" + Fore.CYAN + "\n-{" + selected_tool + "}-> "
    return prompt


while True:
    print(Style.RESET_ALL)
    command = input(Fore.GREEN + command_prompt(selected_tool) + Style.RESET_ALL)
    print(Style.RESET_ALL)
    parts = shlex.split(command)
    cmd = parts[0]
    args = parts[1:]
    if cmd == "cd":
        if args:
            commands.cd(args)
        else:
            print("Error: cd command requires an argument")
    else:
        fn = cmds.get(cmd, unknown_command)
        fn()
