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
        self.basic= HTTPBasicAuth(username=self.sheety_username, password=self.sheety_password)

    def get_users_emails(self):
        self.emails_list=[]
        self.emails_response= requests.get(url=self.users_sheet_api, auth=self.basic).json()['users']
        for data in range(len(self.emails_response)):
            user_email= self.emails_response[data]['email']
            self.emails_list.append(user_email)
        print(self.emails_list)

sheet= SheetyData()
sheet.get_users_emails()