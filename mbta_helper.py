# Your API KEYS (you need to use your own keys - very long random characters)
# from config import MAPQUEST_API_KEY, MBTA_API_KEY
import urllib.request
import json
from pprint import pprint
from config import MAPQUEST_API_KEY, MBTA_API_KEY


# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = "http://www.mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"


# url = f'http://www.mapquestapi.com/geocoding/v1/address?key={API_KEY}&location=Babson%20College'

def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.

    Both get_lat_long() and get_nearest_station() might need to use this function.
    """
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    # print(response_data['results'][0]['locations'][0]['latLng'])
    return response_data


def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developer.mapquest.com/documentation/geocoding-api/address/get/
    for Mapquest Geocoding API URL formatting requirements.
    """
    API_KEY = MAPQUEST_API_KEY
    # for letter in place_name:
    #     if ' ':
    #         letter.replace('%20')
    new_place = place_name.replace(' ', '%20')

    url = f'http://www.mapquestapi.com/geocoding/v1/address?key={API_KEY}&location={new_place}'

    raw = get_json(url)

    return raw['results'][0]['locations'][0]['latLng']
    # pass


def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    pass


def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """
    pass


def main():
    """
    You can test all the functions here
    """
    API_KEY = MAPQUEST_API_KEY
    # pprint(get_json(f'http://www.mapquestapi.com/geocoding/v1/address?key={API_KEY}&location=Babson%20College'))    # Checking
    print(get_lat_long(f'Babson College'))


if __name__ == '__main__':
    main()
