import os
from dotenv import load_dotenv
import requests
from requests.auth import HTTPBasicAuth


load_dotenv()

class SheetyData:
    def __init__(self):
        self.sheety_username= os.getenv("SHEETY_USERNAME")
        self.sheety_password= os.getenv("SHEETY_PASSWORD")
        self.users_sheet_api= os.getenv("SHEETY_USERS_API")
        self.places_sheet_api= os.getenv("SHEETY_PLACES_API")
        self.basic= HTTPBasicAuth(username=self.sheety_username, password=self.sheety_password)

    def get_users_emails(self):
        self.emails_list=[]
        self.emails_response= requests.get(url=self.users_sheet_api, auth=self.basic).json()['users']
        for data in range(len(self.emails_response)):
            user_email= self.emails_response[data]['email']
            self.emails_list.append(user_email)
            return self.emails_list

    def get_places_list(self):
        self.places_list= []
        self.places_response=requests.get(url= self.places_sheet_api,auth=self.basic).json()['flights']
        for data in range(len(self.places_response)):
            place= self.places_response[data]['places']
            self.places_list.append(place)
        return self.places_list

    def update_iata(self,iata, row_id):
        request_body= {'flight':{"iataCodes":iata}}
        self.update= requests.put(url=f"{self.places_sheet_api}/{row_id}",json= request_body,auth= self.basic)

    def get_desired_prices(self):
        self.desired_prices_list=[]
        self.prices_response=requests.get(url= self.places_sheet_api, auth= self.basic).json()['flights']
        for number in range(len(self.prices_response)):
            price= self.prices_response[number]['prices']
            self.desired_prices_list.append(price)
        return self.desired_prices_list