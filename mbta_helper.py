# Your API KEYS (you need to use your own keys - very long random characters)
from inspect import Attribute
from config import MAPQUEST, MBTA_API
import urllib.request
import json
from pprint import pprint


# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = "http://www.mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"


# A little bit of scaffolding if you want to use it


def get_input():
    '''
    Gets address input from customer. Cleans the url and returns it with API key included. 

    Returns
    -------
    cleaned and usable url

    '''
    cust_location = input("Please enter location: ")
    cust_location = cust_location.replace(" ", "%20")
    url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST}&location={cust_location}'
    
    return url 

def get_json():
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.

    Both get_lat_long() and get_nearest_station() might need to use this function.
    """
    url = get_input()
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    # pprint(response_data)
    return response_data


def get_lat_long():
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developer.mapquest.com/documentation/geocoding-api/address/get/
    Credit: https://towardsdatascience.com/using-mapquest-api-to-get-geo-data-a0b4375145e3
    for Mapquest Geocoding API URL formatting requirements.
    
    Returns
    -------
    tuple with ZIP code (sometimes missing if there are multiple), Latitude & Longitude
    """
    
    response = get_json()
    results = response['results'][0]
    locations = results['locations']
    for location in locations:
        if location['adminArea3'] == 'MA':
            latLng = location['latLng']
            return(latLng['lat'], latLng['lng'])
    # return response['results'][0]['locations'][0]['postalCode'], response['results'][0]['locations'][0]['latLng']['lat'], response['results'][0]['locations'][0]['latLng']['lng']

def get_nearest_station_url():
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    info_location = get_lat_long()
    lat = info_location[0] 
    long = info_location[1]
    station_url = f'https://api-v3.mbta.com/stops?api_key={MBTA_API}&sort=distance&sort=wheelchair_boarding&filter%5Blatitude%5D={lat}&filter%5Blongitude%5D={long}'
    # Hard coded url
    # https://api-v3.mbta.com/stops?api_key=6cbb9987c1e94035a98b7ec078de747b&sort=distance&sort=wheelchair_boarding&filter%5Blatitude%5D=38.49441&filter%5Blongitude%5D=-81.92902
    return station_url

def find_stop_near():
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    """
    station_url = get_nearest_station_url() #this portion could be optimized but it is hard to use get_jason() again because it uses the MAPQUEST key above so we can't put the MBTA url
    f = urllib.request.urlopen(station_url)
    response_text = f.read().decode('utf-8')
    response = json.loads(response_text)
    # print(response)
    stations =response['data']
    nearst_station = stations[0]
    attributes = nearst_station['attributes']
    return (attributes['name'], attributes['wheelchair_boarding'])
    




def main():
    """
    Testing cases.
    """
    # print(get_json())
    # print(get_lat_long())
    # print(get_nearest_station_url())
    print(find_stop_near())


if __name__ == '__main__':
    main()

