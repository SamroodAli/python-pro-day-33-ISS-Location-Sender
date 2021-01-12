import requests
import datetime as dt

# International Space Station Location
ISS_URL ="http://api.open-notify.org/iss-now.json"
response = requests.get(url=ISS_URL)
response.raise_for_status()
# ISS API Data
data = response.json()
iss_latitude =float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

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
SUNSET_URL = f"https://api.sunrise-sunset.org/json"
# Requesting api
response = requests.get(url=SUNSET_URL, params=API_PARAMETERS)
# Response status code handler inbuilt in requests library
response.raise_for_status()
# API DATA
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
# Filtering to get sunrise and sunset hours
sunrise_hour = int(sunrise.split("T")[1].split(":")[0])
sunset_hour = int(sunset.split("T")[1].split(":")[0])
now = dt.datetime.now()

