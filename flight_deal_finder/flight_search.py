import requests
from datetime import datetime, timedelta

API_KEY = os.environ.get("API_KEY")
APP_ID = os.environ.get("APP_ID")
LOCATIONS_URL = "https://tequila-api.kiwi.com"

headers = {
    "apikey": API_KEY,
}

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def __init__(self):
        self.price = ""
        self.departure_city_name = "Wrocław",
        self.departure_airport_iata_code = "WRO",
        self.arrival_city_name = "",
        self.arrival_airport_iata_code = "",
        self.from_date = "",
        self.to_date = ""


    def get_iataCodes(self, city):

        params = {
            "term": city,
            "location_types": "airport",
        }

        response = requests.get(url=f"{LOCATIONS_URL}/locations/query", params=params, headers=headers)
        result = response.json()
        return result["locations"][0]["code"]

    def search_flight(self, city_code, price):
        tomorrow = datetime.now() + timedelta(days=1)
        tomorrow_formatted = tomorrow.strftime("%d/%m/%Y")
        in_6_months = datetime.now() + timedelta(days=180)
        in_6_months_formatted = in_6_months.strftime("%d/%m/%Y")

        params = {
            "fly_from": "WRO",
            "fly_to": city_code,
            "date_from": tomorrow_formatted,
            "date_to": in_6_months_formatted,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "price_to": price,
            "max_stopovers": 0,
            "flight_type": "round"
        }

        response = requests.get(url=f"{LOCATIONS_URL}/v2/search", params=params, headers=headers)
        rezult = response.json()
        if rezult["data"] != []:
            print(f'{rezult["data"][0]["cityTo"]}: {(rezult["data"][0]["price"])*4} PLN')
            self.price = rezult["data"][0]["price"]*4
            self.arrival_city_name = rezult["data"][0]["cityTo"]
            self.arrival_airport_iata_code = rezult["data"][0]["cityCodeTo"]
            arrival_date = rezult["data"][0]["local_arrival"]
            date_back = rezult["data"][0]["local_departure"]
            self.from_date = arrival_date.split("T")
            self.to_date = date_back.split("T")
