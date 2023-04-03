# Your API KEYS (you need to use your own keys - very long random characters)
from config import MAPBOX_TOKEN, MBTA_API_KEY
import urllib.request
import json
import requests
import pprint


# Useful URLs (you need to add the appropriate parameters for your requests)
MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

# A little bit of scaffolding if you want to use it


def get_url(place: str):
    """
    Given the name of a place, return a Map Box url
    """
    query = place.replace(" ", "%20")
    url = f'{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi'
    return url


def get_json(url: str) -> dict:
    """
    Given a properly formatted URL for a JSON web API request, return a Python JSON object containing the response to that request.

    Both get_lat_long() and get_nearest_station() might need to use this function.
    """
    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode('utf-8')
        response_data = json.loads(response_text)
        return response_data


def get_lat_long(place_name: str) -> tuple[str, str]:
    """
    Given a place name or address, return a (latitude, longitude) tuple with the coordinates of the given place.

    See https://docs.mapbox.com/api/search/geocoding/ for Mapbox Geocoding API URL formatting requirements.
    """
    url = get_url(place_name)
    response_data = get_json(url)
    latitude, longitude = response_data['features'][0]['center']
    return latitude, longitude


def get_nearest_station(latitude: str, longitude: str) -> tuple[str, bool]:
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible) tuple for the nearest MBTA station to the given coordinates.

    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL formatting requirements for the 'GET /stops' API.
    """
    param = {
        'filter[latitude]': latitude,
        'filter[longitude]': longitude,
        "filter[radius]": 1000,
        'include': 'wheelchair_boarding',
        'sort': 'distance'
    }
    response = requests.get(MBTA_BASE_URL, params=param)
    response.raise_for_status()

    response_data = response.json()
    if not response_data['data']:
        return None

    stop = response_data['data'][0]
    attributes = stop['attributes']
    station_name = attributes['name']
    wheelchair_accessible = attributes.get('wheelchair_boarding') == 1

    return station_name, wheelchair_accessible


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
    # url = get_url("Babson College")
    # pprint.pprint(get_json(url))
    # print(get_lat_long("Babson College"))
    latitute, longitude = get_lat_long("Babson College")
    get_nearest_station(latitute, longitude)


if __name__ == '__main__':
    main()
