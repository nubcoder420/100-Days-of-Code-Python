from bs4 import BeautifulSoup
import requests
import lxml
import smtplib
from email.mime.text import MIMEText

MY_EMAIL = "YOUR EMAIL HERE"
MY_PASSWORD = "YOUR PASSWORD HERE"

PRICE_THRESHOLD = 200 # price for testing

AMAZON_PRODUCT_PAGE = "https://www.amazon.com/dp/B08CFZF16Y/ref=sbl_dpx_kitchen-electric-cookware_B08CFZF16Y_0?th=1"

# https://myhttpheader.com/
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

r = requests.get(url=AMAZON_PRODUCT_PAGE, headers=headers)
result = r.text

soup = BeautifulSoup(result, "lxml")
# print(soup.prettify())

price = float(soup.find('span', class_='a-offscreen').text.strip().split("$")[1])

print(price)

#--------------- Send Email Notification ------------------#

if price < PRICE_THRESHOLD:

    email_message = f"{AMAZON_PRODUCT_PAGE} for only ${price}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)

        msg = MIMEText(email_message, "plain", "utf-8")
        msg['From'] = MY_EMAIL
        msg['To'] = MY_EMAIL
        msg['Subject'] = f"Amazon Price Tracker: ${price}"

        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=msg.as_string(),
        )

    print("Notification Sent")
