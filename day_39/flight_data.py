import requests
from dotenv import load_dotenv
import os

class FlightData:

    def __init__(self):
        load_dotenv()
        self.serpapi_key = os.getenv("SERPAPI_KEY")
        self.google_flights_endpoint = "https://serpapi.com/search"
        self.flights_parameters = {
            "engine": "google_flights_autocomplete",
            "q": "city",
            "api_key": self.serpapi_key
        }

    def iata_code(self, city_name: str) -> str:
        self.flights_parameters["q"] = city_name

        response = requests.get(url=self.google_flights_endpoint, params=self.flights_parameters)
        data = response.json()
        try:
            return data["suggestions"][0]["airports"][0]["id"]
        except (KeyError, IndexError):
            return "NOT FOUND"









