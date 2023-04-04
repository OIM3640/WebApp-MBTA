# Your API KEYS (you need to use your own keys - very long random characters)
# from config import MAPBOX_TOKEN, MBTA_API_KEY


# Useful URLs (you need to add the appropriate parameters for your requests)
MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

import urllib.request
import json
from pprint import pprint

MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MAPBOX_TOKEN = "pk.eyJ1IjoibHBhdGExIiwiYSI6ImNsZzB5emJrbjFmemEzZHA2N3hyd2phZW4ifQ.PC064m-1E2K0hxfFHYVZzQ"

# query = 'Babson%20College'
# url=f'{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi'
# print(url)

# with urllib.request.urlopen(url) as f:
#     response_text = f.read().decode('utf-8')
#     response_data = json.loads(response_text)
#     pprint(response_data)
# print(response_data['features'][0]['properties']['address'])

# A little bit of scaffolding if you want to use it

MBTA_API_KEY = 'fe1a052ac7a146ab99013a71e70f5167'

def get_json() -> dict:
    """
    Given a properly formatted URL for a JSON web API request, return a Python JSON object containing the response to that request.

    Both get_lat_long() and get_nearest_station() might need to use this function.
    """
    # Write a function that takes an address or place name as input and returns a properly encoded URL to make a Mapbox geocoding request.
    location = str(input("What is your current location?: "))
    location = location.replace(" ","%20")
    # urllib.parse.urlencode(query=location, doseq=False, safe='', encoding=None, errors=None, quote_via=quote_plus)   #Tried with not muhc success (Would retry in future but got confused)
    url=f'{MAPBOX_BASE_URL}/{location}.json?access_token={MAPBOX_TOKEN}&types=poi'
    # print(url)
    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode('utf-8')
        response_data = json.loads(response_text)
        # pprint(response_data)
        return response_data


# def get_lat_long(place_name: str) -> tuple[str, str]:
def get_lat_long() -> tuple[str, str]:
    """
    Given a place name or address, return a (latitude, longitude) tuple with the coordinates of the given place.

    See https://docs.mapbox.com/api/search/geocoding/ for Mapbox Geocoding API URL formatting requirements.
    """
    data = get_json()
    lat_long_tuple = tuple(data['features'][0]['center'])
    return lat_long_tuple


# def get_nearest_station(latitude: str, longitude: str) -> tuple[str, bool]:
def get_nearest_station() -> tuple[str, bool]:
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible) tuple for the nearest MBTA station to the given coordinates.

    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL formatting requirements for the 'GET /stops' API.
    """
    lat_long_tuple = get_lat_long()
    latitude = str(lat_long_tuple[0])
    longitude = str(lat_long_tuple[1])
    url=f'https://api-v3.mbta.com/stops?api_key={MBTA_API_KEY}&sort=distance&filter%5Blatitude%5D={latitude}&filter%5Blongitude%5D={longitude}'
    # print(url)
    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode('utf-8')
        response_data = json.loads(response_text)
        print(response_data)
        # return response_data
    """
    THERE IS No Output Currently ###########
    """



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
    # get_json()
    # print(get_lat_long())
    get_nearest_station()


if __name__ == '__main__':
    main()
