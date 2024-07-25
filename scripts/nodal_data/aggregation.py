"""
Aggregates system level data into one dataframe
"""
import pandas as pd
import plantpredict as pp

from scripts.authentication.authentication import authenticate


# --- Auth ---
api = authenticate()

# --- Prediction ---
nodals = []
for array in range(1, 7):
    print(f"Array: {array}")

    # -- Inverter --
    inverters = ['A']
    if array in [2, 3, 4, 5, 6]:
        inverters.append('B')
    if array in [4, 5]:
        inverters.append('C')
    if array in [6]:
        inverters.append('D')

    # -- Get --
    for inverter in inverters:

        prediction = api.prediction(
            id=797445,
            project_id=130172
        ).get_nodal_data(
            params={
                'block_number': 1,
                'array_number': array,
                'inverter_name': inverter,
                # 'dc_field_number': 1
            }
        )

        repeater = prediction['inverter_repeater']

        overview_dataframe = pd.DataFrame(prediction)
        df = overview_dataframe['inverter_data'].apply(pd.Series)
        df.set_index('timestamp', inplace=True)
        nodals.append(df[['dc_power']] * repeater)

system = pd.concat(nodals, axis=1)
dc_power_site = system.sum(axis=1)
dc_power_site = dc_power_site / 1000
dc_power_site.name = 'power (kW)'
dc_power_site.to_csv("dc_energy_sum_NEW_PAN.csv")

print('done')
