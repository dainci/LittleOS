import os
from tabulate import tabulate
from colorama import Fore, Back, Style

from functions import initialisation



        
        
# ls command, displays elements in current folder
def ls(args):
    import os


    if '-fi' in args and '-fo' in args:
        print(Fore.RED + "Error: Cannot specify both -fi and -fo.")
        return
    elif '-fi' in args:
        files = [f for f in os.listdir() if os.path.isfile(f)]
        for file in files:
            print(file)
    else:
        folders = [f for f in os.listdir() if os.path.isdir(f)]
        for folder in folders:
            print(folder)
            
# make directory
def mkdir(args):
    if not args:
        print("mkdir: missing operand")
        return
    try:
        os.makedirs(args[0])
    except FileExistsError:
        print(f"mkdir: cannot create directory '{args[0]}': File exists")
        
# remove file/folder
def rm(file_path):
    try:
        os.remove(file_path)
    except OSError:
        print(f"Erreur: Impossible de supprimer {file_path}")
        
# create a file
def touch(file_path):
    try:
        with open(file_path, 'a'):
            os.utime(file_path, None)
    except OSError:
        print(f"Erreur: Impossible de créer {file_path}")
        
        
def pwd(args): 
    if len(args) == 0:
        current_file = os.path.dirname(os.path.abspath(__file__))
        parent_file = os.path.dirname(current_file)
        path = f"path \n----- \n{parent_file}"
        print(path)
    else:
        print("pwd not require an argument")