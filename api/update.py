# Update Tool 
import subprocess
import sys
import os
import shutil
import urllib.request
from tqdm import tqdm
from colorama import Fore, Style

"""
def download_and_update_project(args):
    github_url = "https://github.com/dainci/LittleOS"

    if version == "last":
        branch = "master"
    elif version == "stable":
        branch = "stable"
    else:
        print(f"{Fore.RED}Invalid version argument. Please use 'last' or 'stable'.{Style.RESET_ALL}")
        return

    # Construire l'URL du fichier zip à télécharger
    zip_url = f"{github_url}{branch}.zip"

    # Télécharger le fichier zip
    print(f"{Fore.YELLOW}Downloading project files...{Style.RESET_ALL}")
    urllib.request.urlretrieve(zip_url, "project.zip")
    print(f"{Fore.GREEN}Download completed. Extracting files...{Style.RESET_ALL}")

    # Extraire le contenu du fichier zip
    shutil.unpack_archive("project.zip", "temp")

    # Copier les fichiers du zip dans le programme
    source_dir = os.path.join("temp", f"repo-{branch}")
    target_dir = os.path.dirname(__file__)

    for root, dirs, files in tqdm(os.walk(source_dir), desc="Copying files",
                                  bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}"):
        # Ignorer le dossier "user"
        if "user" in dirs:
            dirs.remove("user")

        # Parcourir tous les fichiers
        for file in files:
            source_path = os.path.join(root, file)
            target_path = os.path.join(target_dir, os.path.relpath(source_path, source_dir))

            # Créer les dossiers cibles si nécessaire
            os.makedirs(os.path.dirname(target_path), exist_ok=True)

            # Copier les fichiers en remplaçant les fichiers existants
            shutil.copyfile(source_path, target_path)

    # Supprimer les fichiers temporaires
    shutil.rmtree("temp")
    os.remove("project.zip")

    print(f"{Fore.GREEN}Update completed. Restarting the program...{Style.RESET_ALL}")

    # Redémarrer le programme
    subprocess.Popen([sys.executable] + sys.argv)
    sys.exit()


# Vérifier l'argument de la commande
if len(sys.argv) != 2:
    print(f"{Fore.RED}Invalid number of arguments. Please provide 'last' or 'stable' as the argument.{Style.RESET_ALL}")
else:
    version = sys.argv[1].lower()
    download_and_update_project(version)
"""