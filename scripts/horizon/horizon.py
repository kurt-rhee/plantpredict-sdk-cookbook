import os
import sys
import pprint
import plantpredict as pp

import os
import sys
path_to_folder = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, path_to_folder)
from scripts.authentication.authentication import authenticate

api = authenticate()
prediction = api.prediction(
    project_id=136798,
    id=757745
)

horizon = prediction.get()['horizon_details']
print(horizon)
