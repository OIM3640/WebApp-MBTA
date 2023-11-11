# Your API KEYS (you need to use your own keys - very long random characters)
# from config import MAPBOX_TOKEN, MBTA_API_KEY

import json
import pprint
import urllib.request
import requests

MBTA_API_KEY = '12d9224354af4b5e9e49fbbc5e272d17'
MAPBOX_TOKEN = 'pk.eyJ1IjoiYXJtYW5iYWJvIiwiYSI6ImNsb3E5azFyMTBlZ2QybXBxZHdvMzJqOWQifQ.WFgwpxUmfIooCJwFeD_DIw'
# Useful URLs (you need to add the appropriate parameters for your requests)
MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

# query = 'Babson College'
query = str(input("Where are you located?")) 
query = query.replace(' ', '%20')
url= f'{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi'
# A little bit of scaffolding if you want to use it
def get_json(url: str) -> dict:
    """
    Given a properly formatted URL for a JSON web API request, return a Python JSON object containing the response to that request.

    Both get_lat_long() and get_nearest_station() might need to use this function.
    """
    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode('utf-8')
        response_data = json.loads(response_text)
    return response_data

#pprint.pprint(get_json(url))

def get_lat_long(place_name: str) -> tuple[str, str]:
    """
    Given a place name or address, return a (latitude, longitude) tuple with the coordinates of the given place.

    See https://docs.mapbox.com/api/search/geocoding/ for Mapbox Geocoding API URL formatting requirements.
    """

    json_file = get_json(url)
    long_lat = json_file['features'][0]['center']
    coordinates = (long_lat[1],long_lat[0])
    return coordinates
    



def get_nearest_station(latitude: str, longitude: str) -> tuple[str, bool]:
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible) tuple for the nearest MBTA station to the given coordinates.

    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL formatting requirements for the 'GET /stops' API.
    """
    r = requests.get(f'https://api-v3.mbta.com/stops?api_key={MBTA_API_KEY}sort=distance&filter%5Blatitude%5D={latitude}&filter%5Blongitude%5D={longitude}" -H "accept: application/vnd.api+json')
    return r

    pass


def find_stop_near(place_name: str) -> tuple[str, bool]:
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """
    pass


def main():
    """
    You should test all the above functions here
    """
    print(get_lat_long('Boston Common'))
    latitude_1,longitude_1 = get_lat_long('Boston Common')
    print(get_nearest_station(latitude_1,longitude_1))
    pass


if __name__ == '__main__':
    main()