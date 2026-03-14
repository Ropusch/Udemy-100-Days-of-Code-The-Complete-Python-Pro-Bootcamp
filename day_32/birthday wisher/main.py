#I'm using this site whith dummy emails for educational purposes: https://ethereal.email/create
import smtplib
import datetime as dt
import pandas as pd
import random

my_email = "teresa.kling@ethereal.email"
password = "u2Mvsrc12RtK2ddP5r"

now = dt.datetime.now()
today = (now.month, now.day)

df = pd.read_csv('birthdays.csv')

birth_dict = {((data_row["month"], data_row["day"]), data_row["name"]): data_row for (index, data_row) in df.iterrows()}

for key in birth_dict.keys():
    if key[0] == today:
        with open(file=f"letter_{random.randint(1,3)}.txt") as f:
            letter = f.read()
            letter = letter.replace("[NAME]", key[1])
        with smtplib.SMTP("smtp.ethereal.email", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=birth_dict[key]["email"],
                                msg=f"Subject: Happy birthday!\n\n {letter}")