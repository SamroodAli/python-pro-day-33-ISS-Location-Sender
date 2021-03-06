import requests
import datetime as dt
import smtplib
import time
# My latitude and longitude
MY_LAT = 10.915731
MY_LONG = 76.018570
# Email address and Password
MY_EMAIL = "Your email address here"
PASSWORD = "Your email address password here"

# Function to check if International Space Station is near me
def is_iss_overhead():
    # International Space Station Location
    iss_url = "http://api.open-notify.org/iss-now.json"
    response = requests.get(url=iss_url)
    response.raise_for_status()
    # ISS API Data
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    # returning if iss is near me, i.e: -5 my location +5
    return MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG


def is_sky_dark():
    # API Parameters ofr sunrise sunset api endpoint
    api_parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }
    # Sunrise sunset api endpoint
    sunset_url = f"https://api.sunrise-sunset.org/json"
    # Requesting api
    sunset_response = requests.get(url=sunset_url, params=api_parameters)
    # Response status code handler inbuilt in requests library
    sunset_response.raise_for_status()
    # API DATA
    sunset_data = sunset_response.json()
    # Sun rise and Sun set
    sunrise = sunset_data["results"]["sunrise"]
    sunset = sunset_data["results"]["sunset"]
    # Filtering to get sunrise and sunset hours
    sunrise_hour = int(sunrise.split("T")[1].split(":")[0])
    sunset_hour = int(sunset.split("T")[1].split(":")[0])
    time_now = dt.datetime.now().hour
    # return if either after sunset or before sunrise when it is dark
    return time_now >= sunset_hour or time_now <= sunrise_hour


# Running script every 60 seconds
while True:
    time.sleep(60)
    if is_iss_overhead() and is_sky_dark():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs= MY_EMAIL,
                msg="Subject:Look Up👆\n\nThe ISS (International Space Station) is above you in the sky. "
                    "This is an automated email from python pro Udemy course day 33 ISS Location Sender"
            )
