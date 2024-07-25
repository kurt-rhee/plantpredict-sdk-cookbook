import os
import sys
import pprint
import plantpredict as pp

sys.path.insert(0, "/home/skrhee/Programs/PPRaDA/pprada")
from scripts.authentication.authentication import authenticate

api = authenticate()
prediction = api.prediction(
    project_id=136798,
    id=753510
)
print(prediction.get()['degradation_model'])

prediction.degradation_model = pp.enumerations.DegradationModelEnum.LINEAR_DC
prediction.update()
print(prediction.get()['degradation_model'])



# prediction.run()
# results = prediction.get_results_summary()
# pprint.pprint(results, sort_dicts=False)
# print('done')
