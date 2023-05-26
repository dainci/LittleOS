errors = {
    'ERR01_CD_NOT_SUPPORTED': "Error: The 'cd' command is not supported.",
    'ERR02_CLEAR_NOT_SUPPORTED': "Error: The 'clear' command is not supported.",
    'ERR03_EXIT_NOT_SUPPORTED': "Error: the 'exit' command is not supported.",
    'ERR04_LS_NOT_SUPPORTED': "Error: The 'ls' command is not supported."
}



def handle_error(command, args):
    if command == 'cd':
        error_code = 'ERR_CD_NOT_SUPPORTED'
    elif command == 'clear':
        error_code = 'ERR_CLEAR_NOT_SUPPORTED'
    elif command == 'exit':
        error_code = 'ERR_EXIT_NOT_SUPPORTED'
    else:
        print("Erreur : Commande inconnue")