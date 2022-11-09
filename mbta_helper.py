import urllib.request
import json
from pprint import pprint

# Your API KEYS (you need to use your own keys - very long random characters)
# from config import MAPQUEST_API_KEY, MBTA_API_KEY

MAPQUEST_API_KEY = 'GhfoZNG9Jc4VcYqUrLwUI8sRiOHai3iC'
# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = "http://mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"


# A little bit of scaffolding if you want to use it
def remove_space(string):
    return(string.replace(' ', ''))

def create_url(place_name):
    place_name = remove_space(place_name)
    url = f'{MAPQUEST_BASE_URL}?key={MAPQUEST_API_KEY}&location={place_name}'
    return url


def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.

    Both get_lat_long() and get_nearest_station() might need to use this function.
    """
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    return response_data

# print(get_json(f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location=Wellesley,MA'))


def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developer.mapquest.com/documentation/geocoding-api/address/get/
    for Mapquest Geocoding API URL formatting requirements.
    """
    url = create_url(place_name)
    data = get_json(url)
    coords = data['results'][0]['locations'][0]['latLng']
    coordinates = coords['lat'], coords['lng']
    return coordinates



def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    address = 'Washington Street'
    url = f'{MBTA_BASE_URL}?sort=distance&filter%5Blatitude%5D={latitude}&filter%5Blongitude%5D={longitude}'
    data = get_json(url)
    nearest_station = data['data'][0]['attributes']['name']
    wheelchair = data['data'][0]['attributes']['wheelchair_boarding']
    if wheelchair == 0:
        accessibility = 'No Information'
    elif wheelchair == 1:
        accessibility = 'Accessible'
    else:
        accessibility = 'Inaccessible'
    return nearest_station, accessibility
    

def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """
    coordinates = get_lat_long(place_name)
    latitude = coordinates[0]
    longitude = coordinates[1]
    res = get_nearest_station(latitude, longitude)
    return res


def main():
    """
    You can test all the functions here
    """
    find_stop_near('Wellesley Hills')


if __name__ == '__main__':
    main()
