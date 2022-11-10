# Your API KEYS (you need to use your own keys - very long random characters)
from config import MAPQUEST_API_KEY, MBTA_API_KEY

import urllib.request
import json
from pprint import pprint

# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = "http://mapquestapi.com/geocoding/v1/address"
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
    place_name = place_name.replace(" ", "%20") 
    latLong = get_json(f"http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location={place_name},MA")["results"][0]["locations"][0]["latLng"]
    return latLong["lat"], latLong["lng"]

def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    responseData = get_json(f"{MBTA_BASE_URL}?api_key={MBTA_API_KEY}&filter[latitude]={latitude}&filter[longitude]={longitude}&sort=distance")["data"][0]['attributes']
    return responseData["name"], responseData["wheelchair_boarding"]

def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """
    responseData = get_nearest_station(get_lat_long(place_name)[0], get_lat_long(place_name)[1])
    if responseData[1] == 0:
        accessible_info = "not determined if it is accessible"
    elif responseData[1] == 1:
        accessible_info = "accessible"
    elif responseData[1] == 2:
        accessible_info = "NOT accessible"
    return f"The nearest station to {place_name} is {responseData[0]}, and it is {accessible_info} via wheelchair"

def main():
    """
    You can test all the functions here
    """
    # print(MAPQUEST_API_KEY)
    # print(MBTA_API_KEY)
    # get_json('http://mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location=Babson%20College')

    # # get_json('http://mapquestapi.com/geocoding/v1/address?key={MBTA_API_KEY}&location=Babson%20College')
    pass

if __name__ == '__main__':
    main()
