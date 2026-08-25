from sheetydata import SheetyData
from flightdata import IataFinder
from flightsearch import FlightSearcher
from datetime import datetime
from datetime import timedelta

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
flights_prices= []
for code in iata_codes_list:
    price_searched= flight_searcher.search_flights(code,outbound_date, return_date)
    flights_prices.append(price_searched)

# comparing the prices

for row_number in range(len(cities_list)):
    place_selected= cities_list[row_number]
    cost_desired= desired_prices[row_number]
    price_selected= flights_prices[row_number]
    if price_selected is not None and price_selected <= cost_desired:
        print('deal')
        print(price_selected ,"<=",cost_desired )
        print(place_selected)

    

