# Your API KEYS (you need to use your own keys - very long random characters)
from urllib import response
from config import MAPQUEST_API_KEY, MBTA_API_KEY
import urllib.request
import json
from pprint import pprint


# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = "http://www.mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"


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


def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developer.mapquest.com/documentation/geocoding-api/address/get/
    for Mapquest Geocoding API URL formatting requirements.
    """
    place_name = place_name.replace(' ', '%20')
    response_data = get_json(
        f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location={place_name},MA')
    lat_long = response_data['results'][0]['locations'][0]['latLng']
    lat_long = tuple(lat_long.values())

    return lat_long


def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """

    response_data_MBTA_without_key = get_json(
        f'https://api-v3.mbta.com/stops?sort=distance&filter%5Blatitude%5D={latitude}&filter%5Blongitude%5D={longitude}')

    mbta_station_name = response_data_MBTA_without_key['data'][0]['attributes']['name']
    mbta_station_wheelchair = response_data_MBTA_without_key[
        'data'][0]['attributes']['wheelchair_boarding']

    if mbta_station_wheelchair == 0:
        mbta_station_wheelchair = 'No Information'
    elif mbta_station_wheelchair == 1:
        mbta_station_wheelchair = 'Accessible'
    elif mbta_station_wheelchair == 2:
        mbta_station_wheelchair = 'Inaccessible'

    return (mbta_station_name, mbta_station_wheelchair)


def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """

    lat_long = get_lat_long(place_name)
    print(lat_long)
    return get_nearest_station(lat_long[0], lat_long[1])


def main():
    """
    You can test all the functions here
    """
    #get_json(f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location=Babson%20College,MA')
    #get_lat_long('Monument Sq, Charlestown')
    #print(get_nearest_station(42.355181,-71.063323))
    #print(find_stop_near('Boston Common, Boston'))


if __name__ == '__main__':
    main()
