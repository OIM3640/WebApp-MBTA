import requests
import json
import urllib.request
from config import MAPBOX_TOKEN, MBTA_API_KEY, APIKEY_Weather


MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"


def get_json(url: str) -> dict:
    """
    Given a properly formatted URL for a JSON web API request, return a Python JSON object containing the response to that request.
    """
    response = requests.get(url)
    json_data = json.loads(response.text)
    return json_data


def get_lat_long(place_name: str) -> tuple[str, str]:
    """
    Given a place name or address, return a (latitude, longitude) tuple with the coordinates of the given place.
    See https://docs.mapbox.com/api/search/geocoding/ for Mapbox Geocoding API URL formatting requirements.
    :param place_name: str representing a place name or address
    :return: tuple of strings representing latitude and longitude
    """
    place_name = place_name.replace(" ", "%20")
    url = f"{MAPBOX_BASE_URL}/{place_name}.json?access_token={MAPBOX_TOKEN}"
    response = get_json(url)
    latitude = response["features"][0]["center"][1]
    longitude = response["features"][0]["center"][0]
    return str(latitude), str(longitude)



def get_nearest_station(latitude: str, longitude: str) -> tuple[str, bool]:
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible) tuple for the nearest MBTA station to the given coordinates.
    """
    url = f"{MBTA_BASE_URL}?sort=distance&filter[latitude]={latitude}&filter[longitude]={longitude}&api_key={MBTA_API_KEY}"
    response = get_json(url)
    station_name = response["data"][0]["attributes"]["name"]
    wheelchair_accessible = (
        response["data"][0]["attributes"]["wheelchair_boarding"] == 1
    )
    return station_name, wheelchair_accessible


def find_stop_near(place_name: str) -> tuple[str, bool]:
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.
    """
    latitude, longitude = get_lat_long(place_name)
    nearest_station, is_accessible = get_nearest_station(latitude, longitude)
    return nearest_station, is_accessible


def get_weather_conditions(city: str, country_code: str) -> str:
    """
    Given a city and country code, return a string representing the current weather conditions.
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&APPID={APIKEY_Weather}"
    f = urllib.request.urlopen(url)
    response_text = f.read().decode("utf-8")
    response_data = json.loads(response_text)
    weather_conditions = response_data["weather"][0]["description"]
    return weather_conditions


def get_local_temperature(city: str, country_code: str) -> float:
    """
    Given a city and country code, return the current temperature in Fahrenheit.
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&units=imperial&appid={APIKEY_Weather}"
    f = urllib.request.urlopen(url)
    response_text = f.read().decode("utf-8")
    response_data = json.loads(response_text)
    temperature = response_data["main"]["temp"]
    return temperature

def recommend_clothes(city: str, country_code: str, APIKEY_Weather: str):
    temperature = get_local_temperature(city, country_code, APIKEY_Weather)
    weather_conditions = get_weather_conditions(city, country_code, APIKEY_Weather)
    recommendations = []
    
    if temperature < 40:
        recommendations.append("Remember to bring a jacket!")
    elif temperature > 75:
        recommendations.append("It's time to wear lighter clothes!")
    if "rain" in weather_conditions.lower():
        recommendations.append("Remember to bring an umbrella!")
    elif "snow" in weather_conditions.lower():
        recommendations.append("Recommend staying inside.")
    if "clear" in weather_conditions.lower() or "sunny" in weather_conditions.lower():
        recommendations.append("Remember sunglasses or a hat!")
    
    return recommendations

    

