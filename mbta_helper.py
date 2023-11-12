# Your API KEYS (you need to use your own keys - very long random characters)
import json
import urllib.parse
import urllib.request
from pprint import pprint

# Mapbox API
MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MAPBOX_TOKEN = 'pk.eyJ1Ijoiemh1YW5nNCIsImEiOiJjbG93MHd4YXEwNTQxMmtwZmllbmI5czQ2In0.MZQGDDISBa04eKyJSW7qxA'

# MBTA API
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"
MBTA_API_KEY = 'fbe40c3523654681880a60c054016ff2'

# A little bit of scaffolding if you want to use it
def get_json(url: str) -> dict:
    """
    Given a properly formatted URL for a JSON web API request, return a Python JSON object containing the response to that request.

    Both get_lat_long() and get_nearest_station() might need to use this function.
    """
    with urllib.request.urlopen(url) as response:
        data = response.read().decode('utf-8')
        return json.loads(data)


def get_lat_long(place_name: str) -> tuple[str, str]:
    """
    Given a place name or address, return a (latitude, longitude) tuple with the coordinates of the given place.

    See https://docs.mapbox.com/api/search/geocoding/ for Mapbox Geocoding API URL formatting requirements.
    """
    encoded_place_name = urllib.parse.quote(place_name)
    url = f"{MAPBOX_BASE_URL}/{encoded_place_name}.json?access_token={MAPBOX_TOKEN}"
    response = get_json(url)
    coordinates = response['features'][0]['geometry']['coordinates']
    return coordinates[1], coordinates[0]


def get_nearest_station(latitude: str, longitude: str) -> tuple[str, bool]:
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible) tuple for the nearest MBTA station to the given coordinates.

    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL formatting requirements for the 'GET /stops' API.
    """
    url = f"{MBTA_BASE_URL}?api_key={MBTA_API_KEY}&filter[latitude]={latitude}&filter[longitude]={longitude}"
    response = get_json(url)
    
    if response['data']:
        station_name = response['data'][0]['attributes']['name']
        wheelchair_accessible = response['data'][0]['attributes']['wheelchair_boarding'] == 1
        return station_name, wheelchair_accessible
    else:
        return "No stations found", False


def find_stop_near(place_name: str) -> tuple[str, bool]:
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """
    latitude, longitude = get_lat_long(place_name)
    return get_nearest_station(latitude, longitude)


def main():
    """
    You should test all the above functions here
    """
    place_name = "YourPlaceNameHere"
    stop_name, is_accessible = find_stop_near(place_name)
    print(f"Nearest MBTA Stop: {stop_name}")
    print(f"Wheelchair Accessible: {is_accessible}")



if __name__ == '__main__':
    main()
