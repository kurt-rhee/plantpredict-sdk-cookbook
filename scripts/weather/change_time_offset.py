import json
import pytz
import numpy as np
import pandas as pd
import plantpredict as pp

from plantpredict.enumerations import WeatherPLevelEnum, WeatherDataTypeEnum, WeatherDataProviderEnum, LibraryStatusEnum

import os
import sys
path_to_folder = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, path_to_folder)

from scripts.authentication.authentication import authenticate

def change_time_offset():

    # authentication
    api = authenticate()
    weather = api.weather()

    # load the example weather file
    with open('scripts/weather/weather_details.json', 'rb') as json_file:
        weather_details = json.load(json_file)

    # --- CONVERT THE TIMEZONE ---
    df = pd.DataFrame.from_dict(weather_details)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['timestamp'] = df['timestamp'].dt.tz_localize(pytz.FixedOffset(-8 * 60))
    df['timestamp'] = df['timestamp'].dt.tz_convert(pytz.UTC)
    df['timestamp'] = df['timestamp'].dt.tz_localize(None)
    df['timestamp'] = df['timestamp'].dt.strftime('%Y-%m-%dT%H:%M:%S')
    weather_details = df.to_dict(orient="records")

    # some configuration steps
    latitude = 35.0
    longitude = -119.0
    geo = api.geo(latitude=latitude, longitude=longitude)
    location_info = geo.get_location_info()

    # Set other parameters
    weather.name = "Python SDK Test Weather"
    weather.latitude = 35.0
    weather.longitude = -119.0
    weather.country = location_info['country']
    weather.country_code = location_info['country_code']
    weather.data_provider = WeatherDataProviderEnum.METEONORM
    weather.weather_details = weather_details
    weather.elevation = round(geo.get_elevation()["elevation"], 2)
    weather.locality = location_info['locality']
    weather.region = location_info['region']
    weather.state_province = location_info['state_province']
    weather.state_province_code = location_info['state_province_code']
    weather.time_zone = geo.get_time_zone()['time_zone']
    weather.status = LibraryStatusEnum.DRAFT_PRIVATE
    weather.data_type = WeatherDataTypeEnum.MEASURED
    weather.p_level = WeatherPLevelEnum.P95
    weather.time_interval = 60  # minutes
    weather.global_horizontal_irradiance_sum = round(
        sum([w['global_horizontal_irradiance'] for w in weather_details])/1000, 2
    )
    weather.diffuse_horizontal_irradiance_sum = round(
        sum([w['diffuse_horizontal_irradiance'] for w in weather_details])/1000, 2
    )
    weather.direct_normal_irradiance_sum = round(
        sum([w['direct_normal_irradiance'] for w in weather_details])/1000, 2
    )
    weather.average_air_temperature = np.round(np.mean([w['temperature'] for w in weather_details]), 2)
    weather.average_relative_humidity = np.round(np.mean([w['relative_humidity'] for w in weather_details]), 2)
    weather.average_wind_speed = np.round(np.mean([w['windspeed'] for w in weather_details]), 2)
    weather.max_air_temperature = np.round(max([w['temperature'] for w in weather_details]), 2)

    # create weather file in plantpredict
    weather.create()
    print("weather file creation complete")


if __name__ == '__main__':
    change_time_offset()
