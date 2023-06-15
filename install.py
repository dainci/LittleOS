import subprocess


def install_modules():
    try:
        subprocess.check_call(["pip", "install", "-r", "requirements.txt"])
    except subprocess.CalledProcessError as e:
        print(f"Error: failed to install.", e.__cause__)


if __name__ == "__main__":
    install_modules()
