import requests
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta

class FlightSearch:

    def __init__(self):
        load_dotenv()
        self.serpapi_key = os.getenv("SERPAPI_KEY")
        self.google_flights_endpoint = "https://serpapi.com/search"
        self.today = datetime.today().strftime("%Y-%m-%d")
        self.tomorrow = (datetime.today() + timedelta(days=1)).strftime("%Y-%m-%d")
        self.flights_parameters = {
            "engine": "google_flights",
            "departure_id": "---",
            "arrival_id": "---",
            "outbound_date": self.today,
            "return_date": self.tomorrow,
            "currency": "USD",
            "hl": "en",
            "api_key": self.serpapi_key,
        }

    def cheapest_flight(self, _from: str, _to: str, ) -> str:
        self.flights_parameters["departure_id"] = _from
        self.flights_parameters["arrival_id"] = _to

        response = requests.get(url=self.google_flights_endpoint, params=self.flights_parameters)
        print(response.json())
        data = response.json()
        try:
            return data["price_insights"]["lowest_price"]
        except (KeyError, IndexError):
            return "NOT FOUND"



