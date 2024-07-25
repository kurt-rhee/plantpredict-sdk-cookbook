import plantpredict as pp
import pprint as ppr
from scripts.authentication.authentication import authenticate


# # --- localhost API credentials ---
api = authenticate()

plant = api.powerplant(
    project_id=111058,
    prediction_id=701697
).get_json()

plant['blocks'][0]['arrays'][0]['inverters'][0]['dcFields'][0]['postHeight'] = 10
plant['blocks'][0]['arrays'][0]['inverters'][0]['dcFields'][0]['modulesHigh'] = 10
plant['blocks'][0]['arrays'][0]['inverters'][0]['dcFields'][0]['trackingBacktrackingType'] = 1

api.powerplant(
    project_id=111058,
    prediction_id=701697
).update_from_json(
    plant
)


print('done')
