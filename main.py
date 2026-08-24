from sheetydata import SheetyData
from flightdata import IataFinder

# TODO: 9. find iata codes for places from sheety
# TODO: 10. update iata codes column in places sheet
# TODO: 11. fetch desired prices for places from sheety
# TODO: 12. fetch iata codes from sheety in a list 
# TODO: 12. search for flights for all iata codes
# TODO: 13. parse json and return flight date, destination and price
# TODO: 14. compare the flight price with desired price
# TODO: 15. make email message if price is low 

sheety= SheetyData()
airport= IataFinder()

cities_list= sheety.get_places_list()
iata_codes_list=[]
for city in cities_list:
    iatacode= airport.get_iata_code(city)
    iata_codes_list.append(iatacode)
for row in range(len(cities_list)):
    sheety.update_iata(iata_codes_list[row], row+2)


