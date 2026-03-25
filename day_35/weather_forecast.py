import json


with open('forecast.json', 'r') as fp:
    weather_data = json.load(fp)["list"]

will_rain = False
for log in weather_data:
    for weather in log["weather"]:
        if weather["id"] < 700:
            will_rain = True
if will_rain:
    print("it will rain in next 12 hours!")

#   now you can send SMS using twilio! - done in day 36

