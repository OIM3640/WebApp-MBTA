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
    dict = raw['results'][0]['locations'][0]['latLng']

    return dict['lat'], dict['lng']


def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    API_KEY = MBTA_API_KEY
    url = f'https://api-v3.mbta.com/stops?api_key={API_KEY}&sort=distance&filter%5Blatitude%5D={latitude}&filter%5Blongitude%5D={longitude}'
    raw_mbta = get_json(url)

    if len(raw_mbta['data']) > 0:
        station_name = raw_mbta['data'][0]['attributes']['name']
        wheelchair_accessible = raw_mbta['data'][6]['attributes']['wheelchair_boarding']  # 0 is no information, 1 is accessible, 2 is inaccessible
        return station_name, wheelchair_accessible
    else:
        return f'There is no nearest station. Please get into the city!'


def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """
    if wheelchair_accessible == 0:
        wheelchair_info = 'There is no information on accessibility.'
    elif wheelchair_accessible == 1:
        wheelchair_info = "Wheelchair boarding is accessible."
    else:
        wheelchair_info = "Wheelchair boarding is inaccessible."
    pass


def main():
    """
    You can test all the functions here
    """
    API_KEY = MAPQUEST_API_KEY
    # pprint(get_json(f'http://www.mapquestapi.com/geocoding/v1/address?key={API_KEY}&location=Babson%20College'))    # Checking
    # print(get_lat_long(f'Babson College'))  # Checking
    # print(get_nearest_station('42.344593', '-71.144416'))
    # print(get_nearest_station('42.29822', '-71.26543'))


if __name__ == '__main__':
    main()
