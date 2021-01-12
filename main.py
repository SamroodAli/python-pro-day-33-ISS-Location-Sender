import requests
import json
import datetime as dt

# My latitude and longitude
MY_LAT = 10.915731
MY_LONG = 76.018570
# API Parameters ofr sunrise sunset api endpoint
API_PARAMETERS = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}
# Sunrise sunset api endpoint
URL = f"https://api.sunrise-sunset.org/json"
# Requesting api
response = requests.get(url=URL, params=API_PARAMETERS)
# Response status code handler inbuilt in requests library
response.raise_for_status()
# API DATA
data = response.json()
sunrise = data["results"]["sunrise"]
sunrise_hour = sunrise.split("T")[1].split(":")[0]
sunset = data["results"]["sunset"]
sunset_hour = sunset.split("T")[1].split(":")[0]
now = dt.datetime.now()


