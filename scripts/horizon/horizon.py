import os
import sys
import pprint
import plantpredict as pp

import os
import sys
path_to_folder = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, path_to_folder)
from scripts.authentication.authentication import authenticate

# authenticate
api = authenticate()

# put prediction into a python object
prediction = api.prediction(
    project_id=136798,
    id=757745
)

# Get the horizon from the prediction in list of dictionaries format
horizon = prediction.get()['horizon_details']

# Edit the first entry by changing the elevation to another number
horizon_edited = horizon.copy()
horizon_edited[0]['elevation'] = 10.0
prediction.horizon_details = horizon_edited

# Send update
prediction.update()
