import requests
import datetime as dt
import smtplib
from email.mime.text import MIMEText

DIGITAL_CURRENCY = "BTC"
MARKET = "USD"
PERCENT_DIFFERENCE = 1

ALPHAVANTAGE_API_KEY = "YOUR API KEY HERE"
NEWSAPIORG_API_KEY = "YOUR API KEY HERE"

MY_EMAIL = "YOUR EMAIL HERE"
MY_PASSWORD = "YOUR PASSWORD HERE"

#-------------------- Get Current Date in YYYY-MM-DD Format --------------------#
current_date = dt.date.today()
yesterday = current_date - dt.timedelta(days=1)
day_before_yesterday = yesterday - dt.timedelta(days=1)

#-------------------- Get Price ----------------------#
def get_price():
    parameters = {
        "function": "DIGITAL_CURRENCY_DAILY",
        "symbol": DIGITAL_CURRENCY,
        "market": MARKET,
        "apikey": ALPHAVANTAGE_API_KEY,
    }

    response = requests.get(url="https://www.alphavantage.co/query", params=parameters)
    response.raise_for_status()
    data = response.json()

    price_close_1 = float(data["Time Series (Digital Currency Daily)"][f"{yesterday}"][f"4a. close ({MARKET})"])
    price_close_2 = float(data["Time Series (Digital Currency Daily)"][f"{day_before_yesterday}"][f"4a. close ({MARKET})"])

    return price_close_1, price_close_2

#------------------------ Get Percentage Difference ----------------------#
def get_percentage_diff(price_close_1, price_close_2):
    percentage_difference = round(abs((price_close_1 - price_close_2) / ((price_close_1 + price_close_2) / 2)) * 100, 2)
    return percentage_difference

#------------------------ Get News -------------------------#
parameters = {
    "q": "bitcoin",
    "apiKey": NEWSAPIORG_API_KEY
}

def get_news():
    response = requests.get(url="https://newsapi.org/v2/everything", params=parameters)
    response.raise_for_status()
    data = response.json()

    articles = data["articles"]

    sources = []
    titles = []
    descriptions = []
    urls = []

    for i in range(3):  # Get values from index 0 to 2
        source = articles[i]["source"]["name"]
        title = articles[i]["title"]
        description = articles[i]["description"]
        url = articles[i]["url"]

        sources.append(source)
        titles.append(title)
        descriptions.append(description)
        urls.append(url)

    return sources, titles, descriptions, urls

#-------------------------- Send Notification -------------------------#
price_close_1, price_close_2 = get_price()
percentage_difference = get_percentage_diff(price_close_1, price_close_2)

if percentage_difference > PERCENT_DIFFERENCE:

    sources, titles, descriptions, urls = get_news()

    email_message = f"Subject: BTC Price Monitoring: {percentage_difference}\n\n" \
                    f"Article 1:\n" \
                    f"  Title: {titles[0]}\n" \
                    f"  Description: {descriptions[0]}\n" \
                    f"  Source URL: {urls[0]}\n\n" \
                    f"Article 2:\n" \
                    f"  Title: {titles[1]}\n" \
                    f"  Description: {descriptions[1]}\n" \
                    f"  Source URL: {urls[1]}\n\n" \
                    f"Article 3:\n" \
                    f"  Title: {titles[2]}\n" \
                    f"  Description: {descriptions[2]}\n" \
                    f"  Source URL: {urls[2]}\n"

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)

        msg = MIMEText(email_message, 'plain', 'utf-8')
        msg['From'] = MY_EMAIL
        msg['To'] = MY_EMAIL
        msg['Subject'] = f"BTC Price Monitoring: {percentage_difference}%"

        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=msg.as_string(),
            )
    print("Notification Sent")
