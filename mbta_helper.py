# Your API KEYS (you need to use your own keys - very long random characters)
from config import MAPBOX_TOKEN, MBTA_API_KEY
import requests
import urllib.request
import json
from pprint import pprint


# Useful URLs (you need to add the appropriate parameters for your requests)
MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"
MAPBOX_TOKEN = "pk.eyJ1IjoiYW5nZWxhd29uZzEyMyIsImEiOiJjbGZ2b2FyM28wOTh6M25wZGJhcW04ODZpIn0.lT5TeXhQjnwH3fzWq8mjAA"
MBTA_API_KEY = "b0f1e154e91042b5a636d8c6663e88ac"
WEATHER_API_KEY = "5f4ccf8ce381abfe7e6db22d4f1079a9"
# A little bit of scaffolding if you want to use it


def get_url(address) -> str:
    address = address.replace(" ", "%20")
    url = f"{MAPBOX_BASE_URL}/{address}.json?access_token={MAPBOX_TOKEN}&types=poi"
    return url


def get_json(url: str) -> dict:
    """
    Given a properly formatted URL for a JSON web API request, return a Python JSON object containing the response to that request.

    Both get_lat_long() and get_nearest_station() might need to use this function.
    """
    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode("utf-8")
        response_data = json.loads(response_text)
    return response_data


def get_lat_long(address: str) -> tuple[str, str]:
    """
    Given a place name or address, return a (latitude, longitude) tuple with the coordinates of the given place.

    See https://docs.mapbox.com/api/search/geocoding/ for Mapbox Geocoding API URL formatting requirements.
    """
    # Replace entered spaces in address with %20
    address = address.replace(" ", "%20")

    # Generate API url with get_url function and get the json data
    url = get_url(address)
    json_data = get_json(url)

    # Check if the json_data contains any data, and returns the longitude and latitude of the given address. If not, returns no result.
    if len(json_data["features"]) > 0:
        longitude, latitude = json_data["features"][0]["center"]
        return longitude, latitude
    else:
        print(f"No results found for place: {address}")


def get_nearest_station(
    longitude: str, latitude: str, route_type: str
) -> tuple[str, bool]:
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible) tuple for the nearest MBTA station to the given coordinates.

    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL formatting requirements for the 'GET /stops' API.
    """
    MBTA_STOPS_API_URL = "https://api-v3.mbta.com/stops"
    # Possible route types
    route_types = {
        "all": " ",
        "light rail": "0",
        "heavy rail": "1",
        "commuter rail": "2",
        "bus": "3",
        "ferry": "4",
    }
    # Parameters for API
    params = {
        "filter[latitude]": latitude,
        "filter[longitude]": longitude,
        "sort": "distance",
        "api_key": MBTA_API_KEY,
        "filter[route_type]": route_types[route_type],
    }
    # Get JSON data from API and store in station_data
    response = requests.get(MBTA_STOPS_API_URL, params=params)
    station_data = response.json()

    # If station_data contains data, extract the station name and whether it is wheelcahir accesible. If not, it will return None, which means that there are no MBTA stops close enough to the given place.
    if station_data["data"]:
        station_name = station_data["data"][0]["attributes"]["name"]
        wheelchair_accessible = station_data["data"][0]["attributes"][
            "wheelchair_boarding"
        ]
        return station_name, wheelchair_accessible
    else:
        print(f"No stops close enough.")
        return None, None


def find_stop_near(place_name: str, route_type: str) -> tuple[str, bool]:
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """
    place_name = place_name.replace(" ", "%20")

    # Get longitude and latitude for the given place name
    lat, lon = get_lat_long(place_name)
    # Get the nearest station and whether it is wheelchair accessible using the longitude and latitude from above.
    nearest_station, wheelchair_accessible = get_nearest_station(lat, lon, route_type)
    return nearest_station, wheelchair_accessible


def get_weather(place_name):
    """
    Given a place name or address, returns the current weather and temperature.
    """
    place_name = place_name.replace(" ", "%20")
    lon, lat = get_lat_long(place_name)
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&APPID={WEATHER_API_KEY}&units=metric"

    weather_data = get_json(url)
    # Get the current temperature and weather
    temperature = weather_data["main"]["temp"]
    weather = weather_data["weather"][0]["main"]
    return weather, temperature


def main():
    """
    You can test all the functions here
    """
    # Test the code
    # address = "harvard university"
    # lon, lat = get_lat_long(address)
    # print(get_nearest_station(long, lat))
    # place_name = "boston common"
    # route_type = 'all'
    # lon, lat = get_lat_long(place_name)
    # print(get_weather(place_name))
    # print(find_stop_near(place_name, route_type))


if __name__ == "__main__":
    main()
