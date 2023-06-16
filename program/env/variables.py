import os
import pathlib

current_file = os.path.dirname(os.path.abspath(__file__))
parent_directory = os.path.dirname(current_file)

HOME_PATH = pathlib.Path(parent_directory) / "home"

os_version = "0.2.5"
