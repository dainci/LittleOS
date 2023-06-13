from program.commands import commands
import os

cmd = {
    'help': commands.helps,
    'ls': commands.ls,
    'littleos': commands.little_os,
    'python': commands.python,
    'clear': commands.clear,
    'cd': commands.cd_command,
}
