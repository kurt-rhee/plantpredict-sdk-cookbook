import plantpredict as pp
import pprint

import os
import sys
sys.path.insert(0, "/home/skrhee/Programs/plantpredict-sdk-cookbook/")
from scripts.authentication.authentication import authenticate


# # --- localhost API credentials ---
api = authenticate()

plant = api.powerplant(
    project_id=111058,
    prediction_id=890841
).get()

pprint.pprint(plant['blocks'][0]['arrays'][0]['inverters'][0]['dc_fields'])

# api.powerplant(
#     project_id=111058,
#     prediction_id=701697
# ).update_from_json(
#     plant
# )


# print('done')
