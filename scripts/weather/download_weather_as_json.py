import pprint
import pandas as pd
import plantpredict as pp
from scripts.authentication.authentication import authenticate


api = authenticate()

weather = api.weather(
    id=155997
).get_details()
# pprint.pprint(weather.get_details(), sort_dicts=False)

df = pd.DataFrame.from_dict(weather)
df.drop([
    'id', 'weather_id', 'index',
    'albedo_data', 'downloaded_albedo',
    'beam_horizontal_irradiance', 'clear_sky_irradiance',
    'adjusted_timestamp',
    ],
    inplace=True,
    axis=1,
    )
df['rhi'] = 0
df.rename(
    columns = {
        'timestamp': 'time_stamp',
        'global_horizontal_irradiance': 'ghi',
        'diffuse_horizontal_irradiance': 'dhi',
        'direct_normal_irradiance': 'dni',
        'rhi': 'rhi',
        'plane_of_array_irradiance': 'gti',
        'backside_plane_of_array_irradiance': 'rti',
        'pressure': 'pressure',
        'temperature': 't_amb',
        'relative_humidity': 'rh',
        'windspeed': 'ws',
        'wind_direction': 'wd',
        'soiling_loss': 'soiling',
        'precipitable_water': 'p_wat',
        'rainfall': 'rainfall',
        'dewpoint': 'dew_point'
        },
    inplace=True
    )


df.to_json('sdk/test.json', orient='records')
print("done")
