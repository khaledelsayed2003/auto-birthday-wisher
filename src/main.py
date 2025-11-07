import smtplib
import pandas as pd
from datetime import datetime as dt
import os
from dotenv import load_dotenv

# Load the .env file from the config folder
load_dotenv("auto-birthday-wisher/config/.env")


# Read environment variables
smtp_host = os.getenv("SMTP_HOST")
smtp_port = int(os.getenv("SMTP_PORT", "587"))
sender_email = os.getenv("SENDER_EMAIL")
sender_password = os.getenv("SENDER_PASSWORD")


# getting today's date (month, day)
today = (dt.now().month, dt.now().day)


# read recipients data from csv file using pd
with open("auto-birthday-wisher/data/birthdays.csv") as file:
    data = pd.read_csv(file)


birthdays_dic = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}
if today in birthdays_dic:
    birthday_person = birthdays_dic[today]
    # read the birthday letter from txt file 
    with open("auto-birthday-wisher/data/letter_1.txt") as file:
        letter = file.read()
        customized_letter = letter.replace("[name]", birthday_person["name"])
        ## the message
        subject = "Happy Birthday!"
        body = customized_letter
        msg = f"Subject: {subject}\n\n{body}"
        ##create SMTP connection
        with smtplib.SMTP(smtp_host, smtp_port) as server:
            server.starttls()            # Secure the connection
            server.login(user=sender_email, password=sender_password)  # Authenticate
            server.sendmail(from_addr=sender_email, to_addrs=birthday_person["email"], msg=msg)  # Send
            print("✅ Email sent securely!")
        
        






    
    