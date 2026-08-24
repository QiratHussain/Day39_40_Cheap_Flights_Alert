import airportsdata

class IataFinder:
    def __init__(self):
        self.iata_data=airportsdata.load('IATA') 
    def get_iata_code(self,city_name):
        for iata, data in self.iata_data.items():
            if data['city'].lower()==city_name.lower():
                iata_code=iata
                return iata_code

iatafinder= IataFinder()
paris=iatafinder.get_iata_code('paris')
print(paris)