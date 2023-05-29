from functions import initialisation

import sys
import os

def restart_program(args):
    if len(initialisation.args) == 0:
        python = sys.executable
        os.execl(python, python, *sys.argv)
    else:
        print("no")

