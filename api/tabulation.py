# tab auto complete 
import os

# Obtenir le chemin absolu du fichier actuel
current_file = os.path.abspath(__file__)

# Se placer sur le répertoire contenant le fichier
current_directory = os.path.dirname(current_file)
os.chdir(current_directory)

# Afficher le chemin absolu du fichier actuel
print("Chemin absolu du fichier actuel :", current_file)