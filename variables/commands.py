#little OS modules
from commands import basics, help_command, navigation
from functions import update
from functions import initialisation
import main

#other modules
import os

cmds = {
    'cd': navigation.cd,
    'exit': exit,
    'clear': lambda args: (os.system('cls' if os.name == 'nt' else 'clear'), initialisation.littleos()),
    'help': help_command.help,
    'ls': navigation.ls,
    'mkdir': navigation.mkdir,
    'os': basics.os, # -doc; -info; -v
    'python': basics.python, #doc
    'rm': navigation.rm,
    'touch': navigation.touch,
    'pwd': navigation.pwd,
#    'upt': update.download_and_update_project,
    'reload': main.restart_program,
}