##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import smtplib
import datetime as dt
import random
import pandas as pd

letter_list = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
letter = random.choice(letter_list)


#--------------- DATETIME SECTION ----------------#
now = dt.datetime.now()
current_month = now.month
current_day = now.day

#--------------- CSV DATA ------------------#
data = pd.read_csv("birthdays.csv")
# print(data)

matching_rows = data[(data['month'] == current_month) & (data['day'] == current_day)]

for name in matching_rows.name:
    celebrant = name

for email in matching_rows.email:
    celebrant_email = email

#--------------- SMTP SECTION -------------------#

sender = "sender@gmail.com"
sender_password = "password"
recipient = "recipient@gmail.com"

#----------------- LOGIC SECTION --------------------#

if not matching_rows.empty:

    with open(f'letter_templates/{letter}', 'r') as file:
        content = file.read()

    new_path = "./letter_templates/to_send.txt"
    old_string = "[NAME]"
    new_string = f"{celebrant}"
    to_send = content.replace(old_string, new_string)

    with open(new_path, "w") as send_letter:
        send_letter.write(to_send)

    with open(new_path, "r") as send_letter:
        message = send_letter.read()

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=sender, password=sender_password)
        connection.sendmail(
            from_addr=sender,
            to_addrs=celebrant_email,
            msg=f"Subject: Happy Birthday!\n\n{message}"
        )

