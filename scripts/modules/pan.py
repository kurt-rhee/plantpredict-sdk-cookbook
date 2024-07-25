"""
Testing of PAN file capabilities
"""

import os
import pprint
from scripts.authentication.authentication import authenticate

# --- Authenticate ---
api = authenticate()

# --- Upload a module via PAN file ---
# file_name = "_files/PAN/Longi_LR5_72_HBD_560M_G2_Bifacial_Test.PAN"
# file_directory = os.path.dirname(__file__)
# file_path = os.path.join(file_directory, file_name)
#
#
# new_module_id = api.module().upload_pan_file(file_name, file_path)

# --- Get module details ---
test = api.module(id=44099).get()

pprint.pprint(test)
