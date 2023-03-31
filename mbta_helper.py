# Your API KEYS (you need to use your own keys - very long random characters)
from config import MAPBOX_TOKEN, MBTA_API_KEY
import requests

# Useful URLs (you need to add the appropriate parameters for your requests)
MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"
MAPBOX_TOKEN = "pk.eyJ1IjoiYW5nZWxhd29uZzEyMyIsImEiOiJjbGZ2b2FyM28wOTh6M25wZGJhcW04ODZpIn0.lT5TeXhQjnwH3fzWq8mjAA"
STATION_API = "b0f1e154e91042b5a636d8c6663e88ac"
# A little bit of scaffolding if you want to use it


def get_url(address) -> str:
    url = f"{MAPBOX_BASE_URL}/{address}.json?access_token={MAPBOX_TOKEN}&types=poi"
    return url


def get_json(url: str) -> dict:
    """
    Given a properly formatted URL for a JSON web API request, return a Python JSON object containing the response to that request.

    Both get_lat_long() and get_nearest_station() might need to use this function.
    """
    response = requests.get(url)
    response_json = response.json()
    return response_json


def get_lat_long(address: str) -> tuple[str, str]:
    """
    Given a place name or address, return a (latitude, longitude) tuple with the coordinates of the given place.

    See https://docs.mapbox.com/api/search/geocoding/ for Mapbox Geocoding API URL formatting requirements.
    """
    if len(data["features"]) > 0:
        latitude, longitude = data["features"][0]["center"]
        return latitude, longitude
    else:
        print(f"No results found for place: {address}")


def get_nearest_station(latitude: str, longitude: str) -> tuple[str, bool]:
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible) tuple for the nearest MBTA station to the given coordinates.

    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL formatting requirements for the 'GET /stops' API.
    """
    MBTA_STOPS_API_URL = "https://api-v3.mbta.com/stops"
    params = {
        "filter[latitude]": latitude,
        "filter[longitude]": longitude,
        "sort": "distance",
        "api_key": STATION_API,
    }
    response = requests.get(MBTA_STOPS_API_URL, params=params)
    station_data = response.json()
    station_name = station_data["data"][0]["attributes"]["name"]
    wheelchair_accessible = station_data["data"][0]["attributes"]["wheelchair_boarding"]
    return station_name, wheelchair_accessible


# Test the code
# address = 'Boston, MA'
# url = get_url(address)
# response_json = get_json(url)
# data = response_json
# data
# longitude,latitude = get_lat_long(address)
# get_nearest_station(latitude, longitude)


def find_stop_near(place_name: str) -> tuple[str, bool]:
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """
    pass


def main():
    """
    You can test all the functions here
    """
    pass


if __name__ == "__main__":
    main()
