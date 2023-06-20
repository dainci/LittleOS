import subprocess


def install_module():
    try:
        subprocess.check_call(["pip", "install", "-r", "requirements.txt"])
    except subprocess.CalledProcessError:
        print(f"Error : failed to install.")


install_module()
