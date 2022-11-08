# Your API KEYS (you need to use your own keys - very long random characters)
# from config import MAPQUEST_API_KEY, MBTA_API_KEY
import urllib.request
import json
from pprint import pprint

# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = "http://www.mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"


# A little bit of scaffolding if you want to use it


def get_json(place_name):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.

    Both get_lat_long() and get_nearest_station() might need to use this function.
    """
    place_name=str(place_name)
    result= place_name.replace(" ","%20") # replace any space in the location name with '%20' to avoid error in url
    MAPQUEST_API_KEY = '2LChdSQpT6Drb9wsby5RMnPHDK4Ve5hz'
    url = f'http://mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location={result}'
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
    locations = get_json(place_name)['results'][0]['locations']
    
    for location in locations:
        if location['adminArea3']=="MA": # select the returned longtitude and latitude in MA only
            lattitude = location['displayLatLng']['lat']
            longtitude = location['displayLatLng']['lng']
            return lattitude, longtitude
    return 42.3601,71.0589 # if none of the locations returned from API stays in MA, we will automatically set the values of latitude and longtitude in Boston


def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    MBTA_API_KEY= '810c5d8678a7493db5e4e3bfbe5d7a08'
    url = f'https://api-v3.mbta.com/stops?api_key={MBTA_API_KEY}&sort=distance&filter%5Blatitude%5D={latitude}&filter%5Blongitude%5D={longitude}'
    f = urllib.request.urlopen(url)
    text = f.read().decode('utf-8')
    data = json.loads(text)
    # pprint(response_data)
    CLOSEST_MBTA_NAME=data['data'][0]['attributes']['name']
    CLOSEST_MBTA_WHEELCHAIR=data['data'][0]['attributes']['wheelchair_boarding']
    return CLOSEST_MBTA_NAME,CLOSEST_MBTA_WHEELCHAIR


def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """
    latitude, longtitude=get_lat_long(place_name)
    station, wheelchair=get_nearest_station(latitude,longtitude)
    if wheelchair == 0:
        wheelchair_access="There is no information about wheelchair accessibility."
    elif wheelchair==1:
        wheelchair_access="It is accessible to wheelchair."
    else:
        wheelchair_access="It is not accessible to wheelchair."
    return station, wheelchair_access


def main():
    """
    You can test all the functions here
    """
    print('Please enter an location within Boston, or we will default your location to Boston.')
    location=input('Please enter the address:')
    # pprint(get_json(location))
    # print(get_json()['results'][0]['locations'][0]['postalCode'])
    # print(get_lat_long(location))
    # latitude,longtitude=get_lat_long(location)
    # print(get_nearest_station(latitude,longtitude))
    stop, wheechair_availability = find_stop_near(location)
    print(f'The closest station to {location} is {stop}. {wheechair_availability}')


if __name__ == '__main__':
    main()
