
import os
import sys


def add_scripts_to_path()
    """
    Add the scripts folder to the python path
    """
    path_to_folder = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    sys.path.insert(0, path_to_folder)
