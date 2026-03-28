import requests
from dotenv import load_dotenv
import os
from datetime import datetime


load_dotenv()
APP_ID = os.getenv("AB100_APP_ID")
API_KEY = os.getenv("AB100_API_KEY")


GENDER = "male"
WEIGHT_KG = 80
HEIGHT_CM = 180
AGE = 23


headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

url = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"

user_input = input("What exercises you did today? ")

parameters = {
    "query": user_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url, headers=headers, json=parameters)
result = response.json()


excercise_data = {
    "arkusz1": {
        "date": datetime.strftime(datetime.today(), "%d/%m/%Y"),
        "time": datetime.strftime(datetime.today(), "%H:%M:%S"),
        "exercise": result["exercises"][0]["name"].title(),
        "duration": result["exercises"][0]["duration_min"],
        "calories": result["exercises"][0]["nf_calories"]
    }
}


sheety_url = "https://api.sheety.co/a37ddb13b30c6e79dbefa8a269846895/100DaysWorkout/arkusz1"
sheety_token = "Bearer " + os.getenv("SHEETY_TOKEN")


sheety_headers = {
    "Content-Type": "application/json",
    "Authorization": sheety_token
}

sheety_response = requests.post(url=sheety_url, json=excercise_data, headers=sheety_headers)
print(sheety_response.json())







