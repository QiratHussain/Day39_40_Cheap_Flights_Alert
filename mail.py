import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

class Notifier:
    def __init__(self):
        self.my_email= os.getenv("MY_EMAIL")
        self.my_password= os.getenv("MY_PASSWORD")
    
    def send_email(self,mail_body, receiver):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=self.my_email, password=self.my_password)
            connection.sendmail(from_addr=self.my_email, to_addrs=receiver,msg= f"Subject: Flight Alert!\n\n{mail_body} ")

notify= Notifier()
notify.send_email("ok", "testingcode4python@gmail.com")