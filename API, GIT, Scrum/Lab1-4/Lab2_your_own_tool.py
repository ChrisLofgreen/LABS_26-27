



# Lab 2: Your own tool


from api_client import get_json
import requests
import openmeteo_requests
import pandas as pd
import requests_cache
from retry_requests import retry

# 1.
'''
response = get_json("https://geocoding-api.open-meteo.com/v1/search", params= {"name" : "Stockholm", "count": 1})
print(response)
print(response["results"][0]["latitude"], response["results"][0]["longitude"])
'''

# 2.
'''
city = get_json("https://geocoding-api.open-meteo.com/v1/search", params= {"name" : "Stockholm", "count": 1})
coordinates = (city["results"][0]["latitude"], city["results"][0]["longitude"])

latitude, longitude = coordinates


weather = get_json("https://api.open-meteo.com/v1/forecast", params= {"latitude" : latitude, "longitude": longitude, "current": ["temperature_2m", "wind_speed_10m"]})
print(weather["current_units"])
print(weather["current"])
'''