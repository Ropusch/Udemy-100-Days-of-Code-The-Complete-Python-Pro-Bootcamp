import requests
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta

USERNAME = "ropusch"

load_dotenv()
pixela_token = os.getenv("PIXELA_TOKEN")

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": pixela_token,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url= pixela_endpoint, json=user_params)
# print(response.text)
# # {"message":"Success. Let's visit https://pixe.la/@ropusch , it is your profile page!","isSuccess":true}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graphreading1",
    "name": "Reading",
    "unit": "chaper(s)",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": pixela_token
}

# resposne = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(resposne.text)
# # {"message":"Success.","isSuccess":true}


graph_id = graph_config["id"]
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}"

yesterday = (datetime.today() - timedelta(days=2)).strftime("%Y%m%d")
today = (datetime.today()).strftime("%Y%m%d")

def add_pixel():
    pixels_config = {
        "date": today,
        "quantity": input("How many chapters have you read? ")
    }

    resposne = requests.post(url=pixel_endpoint, json=pixels_config, headers=headers)
    print(resposne.text)


update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}/{today}"

def update_pixel():
    pixels_config = {
        "quantity": input("How many chapters have you ACTUALLY read? ")
    }

    resposne = requests.put(url=update_pixel_endpoint, json=pixels_config, headers=headers)
    print(resposne.text)


delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}/{today}"

def delete_pixel():
    resposne = requests.delete(url=delete_pixel_endpoint, headers=headers)
    print(resposne.text)


# add_pixel()
# update_pixel()
# delete_pixel()

