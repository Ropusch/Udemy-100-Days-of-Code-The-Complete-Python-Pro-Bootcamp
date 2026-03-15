import requests
from datetime import datetime
import smtplib


MY_LAT = 50.064651
MY_LON = 19.944981

my_email = "teresa.kling@ethereal.email"
password = "u2Mvsrc12RtK2ddP5r"


response = requests.get(url="http://api.open-notify.org/iss-now.json")
#rint(response) #response code - 1xx = wait, 2xx = ok, 3xx = no permission, 4xx = bad, 5xx = bad but on servers side
response.raise_for_status()

data = response.json()
#print(data) #{'timestamp': 1773576493, 'iss_position': {'longitude': '9.2029', 'latitude': '-38.6013'}, 'message': 'success'}

iss_pos = {"lon": float(data["iss_position"]["longitude"]),
           "lat": float(data["iss_position"]["latitude"])}


parameters = {
    "lat": MY_LAT,
    "lng": MY_LON,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)

data = response.json()['results']
sunrise = float(data['sunrise'].split("T")[1].split(":")[0] + "." + data['sunrise'].split("T")[1].split(":")[1])
sunset = float(data['sunset'].split("T")[1].split(":")[0] + "." + data['sunset'].split("T")[1].split(":")[1])

time_now = float(datetime.now().hour + 0.01*datetime.now().minute)


is_dark = time_now < sunrise or time_now > sunset
is_iss_close = abs(MY_LAT-iss_pos['lat']) <= 5 and abs(MY_LON-iss_pos['lon']) <= 5

if is_dark and is_iss_close: #or True - for testing purposes!
    with smtplib.SMTP("smtp.ethereal.email", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="teresa.kling@ethereal.email",
                            msg="Subject: ISS is above you!\n\n"
                                f"Hi!\n ISS is in: {iss_pos}, LOOK UP! \n\n"
                                "Have a nice night!")

