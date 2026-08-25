import os
import serpapi
from dotenv import load_dotenv

load_dotenv()

class FlightSearcher:
    def __init__(self):
        self.serpapi= os.getenv("SERP_API")

    def search_flights(self, iata, start_date, end_date):
        self.params={"engine":"google_flights", "departure_id":"LHE", "arrival_id":iata, "outbound_date": start_date, "return_date":end_date,"currency":"USD"}
        client= serpapi.Client(api_key=self.serpapi)
        serp_response= client.search(self.params)
        if 'best_flights' in serp_response:
            flights_response= serp_response['best_flights']
            flight_price=flights_response[0]['price']
            return flight_price
        elif 'other_flights' in serp_response:
            flights_response= serp_response['other_flights']
            flight_price= flights_response[0]['price']
            return flight_price
        else:
            return None
