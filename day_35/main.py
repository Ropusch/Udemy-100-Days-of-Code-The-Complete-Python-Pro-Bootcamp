from dotenv import load_dotenv
import os
import requests
import json

MY_LAT = 50.064651
MY_LON = 19.944981

current_weather_url = "https://api.openweathermap.org/data/2.5/weather"
_5day_3h_weather_url = "https://api.openweathermap.org/data/2.5/forecast"

load_dotenv()
api_key = os.getenv("OPEN_WEATHER_API_KEY")


parameters = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(url=_5day_3h_weather_url, params=parameters)
response.raise_for_status()

with open('forecast.json', 'w') as fp:
    json.dump(response.json(), fp)

