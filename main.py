from sheetydata import SheetyData
from flightdata import IataFinder
from flightsearch import FlightSearcher
from datetime import datetime
from datetime import timedelta

# TODO: 12. search for flights for all iata codes
# TODO: 13. parse json and return flight date, destination and price
# TODO: 14. compare the flight price with desired price
# TODO: 15. make email message if price is low 


# get desired prices
sheety= SheetyData()
desired_prices= sheety.get_desired_prices()

# get iata_codes for desired places
airport= IataFinder()
cities_list= sheety.get_places_list()
iata_codes_list=[]
for city in cities_list:
    iatacode= airport.get_iata_code(city)
    iata_codes_list.append(iatacode)
for row in range(len(cities_list)):
    sheety.update_iata(iata_codes_list[row], row+2)

# search for flights for all iata codes
one_week_later= datetime.now()+ timedelta(days= 7)
two_week_later= datetime.now()+ timedelta(days= 14)
outbound_date= str(one_week_later).split(" ")
return_date= str(two_week_later).split(" ")
flight_searcher= FlightSearcher()
for code in iata_codes_list:
    flight_searched= flight_searcher.search_flights(code,outbound_date, return_date)
    print(flight_searched)

