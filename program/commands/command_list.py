from program.commands import commands
from program.apps.Vimpyr import vimpyr

cmd = {
    "help": commands.helps,
    "ls": commands.ls,
    "littleos": commands.little_os,
    "python": commands.python,
    "clear": commands.clear,
    "cd": commands.cd_command,
    "make": commands.make,
    "rm": commands.remove,
    "cp": commands.cp,
    "mv": commands.mv,
    "cat": commands.cat,
    "head": commands.head,
    "grep": commands.grep,
    "echo": commands.echo,

    "vimpyr": vimpyr().run,
}
