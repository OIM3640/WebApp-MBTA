# Your API KEYS (you need to use your own keys - very long random characters)
MAPQUEST_API_KEY = 'GU2tcnSdaMsdzlr6KZOYIkN35Oz1yVM9'
MBTA_API_KEY = '059086035f0a4da5978b006780b0f9a9'


# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = "http://www.mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"


# A little bit of scaffolding if you want to use it

# Import Necessary Packages
import urllib.request
import json
from pprint import pprint

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
    # pprint(response_data)

# get_json(f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location=Babson%20College')  # for testing


def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developer.mapquest.com/documentation/geocoding-api/address/get/
    for Mapquest Geocoding API URL formatting requirements.
    """
    place = place_name.replace(' ', '%20')
    url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location={place}'
    detail = get_json(url)
    latitude = detail['results'][0]['locations'][0]['latLng']['lat']
    longitude = detail['results'][0]['locations'][0]['latLng']['lng']
    return (latitude, longitude)

# print(get_lat_long('Boston Common, MA'))  # for testing


def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    url = f"https://api-v3.mbta.com/stops?api_key={MBTA_API_KEY}&sort=latitude&filter%5Blatitude%5D={latitude}&filter%5Blongitude%5D={longitude}"
    detail = get_json(url)
    station_name = detail['data'][0]['attributes']['name']
    wheelchair = detail['data'][0]['attributes']['wheelchair_boarding']
    if wheelchair == 1:
        wheelchair_accessible = 'yes, it is wheelchair accessible!'
    if wheelchair == 0:
        wheelchair_accessible = 'unfortunately, important information is missing about wheelchair accessibility'
    else:
        wheelchair_accessible = 'unfortunately, it is not wheelchair accessible'
    return (station_name, wheelchair_accessible)

# print(get_nearest_station(42.37401, -71.06005))  # for testing


def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """
    latitude = get_lat_long(place_name)[0]
    longitude = get_lat_long(place_name)[1]
    return get_nearest_station(latitude, longitude)

# print(find_stop_near('Babson College, MA'))  # for testing

def main():
    """
    You can test all the functions here
    """
    return find_stop_near('Boston Common, MA')


if __name__ == '__main__':
    main()
