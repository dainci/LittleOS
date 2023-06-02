import exeptions

import __init__



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
    prompt = input(f"├──── {'~/.../' if len(folders) > 3 else ''}{path} ────┤\n└────>")
    
    if prompt.lower() == "exit":
        print("ended by user")
        time.sleep(0.3)
        break

    try:
        if hasattr(help, prompt):
            command_function = getattr(girgo, prompt)
            command_function()
        else:
            print("Commande non reconnue")

    except subprocess.CalledProcessError as e:
        print("Erreur :", str(e))

