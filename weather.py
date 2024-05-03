"""
This module fetches weather data from the OpenWeatherMap API.
"""

import requests

# Variables
API_KEY = "14358a08906d6bb768977032b8e7dbfe"
LOCATION = "Nashville,TN,USA"


# Definitions
def fetch_current_weather(api_key, location):
    """
    Accept two args: api_key & location.

    api_key is from https://openweathermap.org/
    location must be in the following format: City,State(abbrev),Country(abbrev)

    Returns current weather data in json format.
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=imperial"
    response = requests.get(url, timeout=10)
    return response.json()


# Print information you want
current_weather_data = fetch_current_weather(API_KEY, LOCATION)
current_temp = current_weather_data["main"]["temp"]
current_weather_description = current_weather_data["weather"][0]["description"]

# print("current weather:", current_weather_data)

print(
    f"The current temperature in {LOCATION} is {current_temp} degrees F with {current_weather_description}."
)


# def fetch_weather_forecast(api_key, location):
#     """_summary_

#     Args:
#         api_key (_type_): _description_
#         location (_type_): _description_

#     Returns:
#         _type_: _description_
#     """
#     url = f"http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={api_key}&units=imperial"
#     response = requests.get(url, timeout=10)
#     return response.json()


# weather_forecast_data = fetch_weather_forecast(API_KEY, LOCATION)
# print("weather forecast:", weather_forecast_data)
