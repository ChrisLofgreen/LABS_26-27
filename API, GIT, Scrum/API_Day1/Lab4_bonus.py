



# Lab 4: Bonus


# Modified base program from lab 2 (made it slightly cleaner with a separete function ("get_info()") to merge data from the two sources into "data")


# 1.

# weather.json reads:
'''
[
  {
    "city": "Stockholm",
    "country": "Sweden",
    "temperature": 11.6,
    "temperature_unit": "\u00b0C",
    "windspeed": 21.2,
    "windspeed_unit": "km/h"
  }
]
'''

# 2.
# Yes, it can repeat the answer any number of times within 10 minutes from the quiry timestamp

# 3.
# Short time local storage could be useful for many reasons but token cost, internet access, internet-cost and usage limits are certainly a few.
# Then there is the thing that a new query will be slightly slower and poses a risk of failing. So reused might make for a snappier application.


from api_client import get_json
import json, os, time







def get_city_info(city_name):
    city = get_json("https://geocoding-api.open-meteo.com/v1/search", params= {"name" : city_name, "count": 1})
    
    try:
        city_info = [city["results"][0]["name"], 
                     city["results"][0]["country"], 
                     (city["results"][0]["latitude"], city["results"][0]["longitude"])]
    except KeyError:
        city_info = []
    
    return city_info


def get_weather(coordinates):
    latitude, longitude = coordinates
    weather = get_json("https://api.open-meteo.com/v1/forecast", params= {"latitude" : latitude, "longitude": longitude, "current": ["temperature_2m", "wind_speed_10m"]})
    
    try:
        weather_info = [weather["current"]["temperature_2m"], 
                    weather["current_units"]["temperature_2m"], 
                    weather["current"]["wind_speed_10m"], 
                    weather["current_units"]["wind_speed_10m"]]
    except TypeError:
        weather_info = []
    
    return weather_info



def get_info(user_city):
    city_info = get_city_info(user_city)
    if len(city_info) > 0:
        weather = get_weather(city_info[2])
        if len(weather) > 0:
            return {"city": city_info[0], 
                    "country": city_info[1], 
                    "temperature": weather[0], 
                    "temperature_unit": weather[1], 
                    "windspeed": weather[2], 
                    "windspeed_unit": weather[3],
                    "timestamp": time.time(),
                    "source": "query"}
        else:
             return {"city": "Errormess", "error": "Weather not availible", "timestamp": time.time()}
    else:
        return {"city": "Errormess", "error": "City not found", "timestamp": time.time()}


def save_data():
    config_data = weather_data
    weather_file = 'weather.json'

    with open(weather_file, 'w') as config_file:
        json.dump(config_data, config_file, indent=2)

    return f"\nData successfully written to {weather_file}"


def load_data():

    weather_file = 'weather.json'
    try:
        with open(weather_file, 'r') as config_file:
            data_loaded = json.load(config_file)
        weather_data = data_loaded
        print("weatherfile loaded.\n")
        return weather_data

    except FileNotFoundError:
        weather_data = []
        return weather_data


def remove_old_data():
    for data in weather_data:
        if ((time.time() - data["timestamp"]) / 60) > 10:
            weather_data.remove(data) 



weather_data = load_data()
remove_old_data()
weather_query = None

user_input = str(input("Type city to get it's current weather:\n")).strip()


for data in weather_data:
        if data["city"].lower() == user_input.lower() and ((time.time() - data["timestamp"]) / 60) < 10:
            data["source"] = "from store"
            weather_query = data
            continue

if weather_query is None : weather_query = get_info(user_input)

if weather_query["city"] == "Errormess":
    print(f"\n{weather_query["error"]}")
else:
    print(f"\n{weather_query["city"]}, {weather_query["country"]}: temp {weather_query["temperature"]} {weather_query["temperature_unit"]}, wind {weather_query["windspeed"]} {weather_query["windspeed_unit"]}")
    print(f"data source: {weather_query["source"]}")

weather_data.append(weather_query)

save_data()