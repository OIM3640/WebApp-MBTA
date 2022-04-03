# Your API KEYS (you need to use your own keys - very long random characters)
MAPQUEST_API_KEY='QMhaQ4tAP42jeBUajvl64nmkts3mfDO1'
MBTA_API_KEY='2e4902ccdaa848bbabec02723220a826'

# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = f"http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location=Washington,DC"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

# Import packages
import urllib.request
import json

def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    Both get_lat_long() and get_nearest_station() might need to use this function.
    """
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    return json.loads(response_text)
# get_json(f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location=Washington,DC')

def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developer.mapquest.com/documentation/geocoding-api/address/get/
    for Mapquest Geocoding API URL formatting requirements.
    """
    pass


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
    pass


if __name__ == '__main__':
    main()
