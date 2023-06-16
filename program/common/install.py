import subprocess


def install_module():
    try:
        subprocess.check_call(["pip", "install", "-r", "requirements.txt"])
    except subprocess.CalledProcessError:
        print(f"Error : failed to install.")

# Liste des modules à installer

# Installation des modules un par un
install_module()