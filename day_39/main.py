import requests
from dotenv import load_dotenv
import os
from pprint import pprint
from flight_data import FlightData
from flight_search import FlightSearch

load_dotenv()

SHEETY_TOKEN = os.getenv("FLIGHT_SHEETY_KEY")
MY_AIRPORT = "KRK"

sheety_url = "https://api.sheety.co/a37ddb13b30c6e79dbefa8a269846895/day3940,Flights/arkusz1"
sheety_headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + SHEETY_TOKEN
}


flight_data = FlightData()


def flights_iata_filling():
    sheety_response = requests.get(url=sheety_url, headers=sheety_headers).json()
    for city in sheety_response["arkusz1"]:
        if city["iataCode"] == "":
            put_url = sheety_url + "/" + str(city["id"])
            put_content = {
                "arkusz1": {
                    'iataCode': flight_data.iata_code(city["city"])
                }
            }
            response = requests.put(url=put_url, json=put_content, headers=sheety_headers).json()
            print(response)


flight_search = FlightSearch()
def find_cheapest(_from, _to):
    print(flight_search.cheapest_flight(_from=_from, _to=_to))


# flights_iata_filling() - this function is kinda one time use - it fills iata codes in google sheets
#   I skipped part where it fetches city iata codes - insted im using largest airports for every city
#   #(it should be easy x with right api)


find_cheapest("JFK", "CDG")