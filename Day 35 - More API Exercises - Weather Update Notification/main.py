import requests
import time
import smtplib

MNL_LAT = 14.599512 # Latitude
MNL_LONG = 120.984222 # Longitude

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = "f267308ff46cd7107ad413fa6604bc66"

my_email = "user@email.com" # Enter your email here
password = "password" # your password

parameters = {
    "lat": MNL_LAT,
    "lon": MNL_LONG,
    "appid": API_KEY,
}


response = requests.get(url=OWM_ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()
weather_data = data['weather'][0]['description']

# print(weather_data)

while True:

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)

        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject: Weather Update: {weather_data}"
        )

    print("Notification Sent")
    time.sleep(14400) # run every x hours

