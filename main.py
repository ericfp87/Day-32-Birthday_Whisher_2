import datetime as dt
import random
import pandas as pd
import smtplib

MY_USER = "teste@gmail.com"
MY_PASSWORD = "1234abc()"

date = dt.datetime.now()
today_month = date.month
today_day = date.day
today = (today_month, today_day)



data = pd.read_csv("birthdays.csv")


birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}



if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    random_letter = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(random_letter) as letter_file:
        letter = letter_file.read()
        new_letter = letter.replace("[NAME]", birthday_person["name"])
        print(new_letter)



    with smtplib.SMTP("smtp.gmail.com") as connection:

        connection.starttls()
        connection.login(user=MY_USER, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_USER, to_addrs=birthday_person["email"], msg=f"Subject: Happy Birthday!\n\n{new_letter}")


