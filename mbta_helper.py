# Your API KEYS (you need to use your own keys - very long random characters)
from config import MAPQUEST_API_KEY, MBTA_API_KEY


# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = "http://www.mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"


# A little bit of scaffolding if you want to use it

from pprint import pprint


def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.

    Both get_lat_long() and get_nearest_station() might need to use this function.
    """
    import urllib.request
    import json


    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    # pprint(response_data)
    return(response_data)


def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developer.mapquest.com/documentation/geocoding-api/address/get/
    for Mapquest Geocoding API URL formatting requirements.
    """
    from pprint import pprint

    place = place_name.replace(' ','%')
    url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location={place},MA'
    json_data = get_json(url)
    # lat = json_data['displayLatLng']
    # long = ['displayLatLng']
    
    results = json_data['results'][0]['locations'][0]['displayLatLng']
    # pprint(results)
    return(results)




def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """

    nearby = get_json(f'https://api-v3.mbta.com/stops?api_key={MBTA_API_KEY}&sort=distance&filter%5Blatitude%5D={latitude}&filter%5Blongitude%5D={longitude}&filter%5Bradius%5D=0.1') #took me soooo long to figure this out on my own
    station_name_1 = nearby['data'][1]['attributes']['name']
    accessible_1 = nearby['data'][1]['attributes']['wheelchair_boarding']
    accessible_clean = 0
    if accessible_1 == 1:
        accessible_clean = 'wheelchair accessible'
    elif accessible_1 == 0:
        accessible_clean = 'unknown if the stop is wheelchair accessible'
    elif accessible_1 == 2:
        accessible_clean = 'not wheelchair accessible'
    # vehicle_type = nearby['data'][0]['attributes']['vehicle_type']
    # address = nearby['data'][0]['attributes']['address']
    # city = nearby['data'][0]['attributes']['municipality']
    station_1_info = (station_name_1,accessible_clean)
    #2nd closest station
    # station_name_2 = nearby['data'][1]['attributes']['name']
    # accessible_2 = nearby['data'][1]['attributes']['wheelchair_boarding']
    # station_2_info = (station_name_2,accessible_2)
    return(station_1_info)
    # print(type(station_info))
    # print(station_info)

def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """
    lat_long_dict = get_lat_long(place_name)
    latitude = float(lat_long_dict['lat'])
    longitude = float(lat_long_dict['lng'])
    # return(latitude)
    return(get_nearest_station(latitude, longitude))
    # return(lat_long_dict)

def main():
    """
    You can test all the functions here
    """
    # get_lat_long('wellesley college')
    # get_nearest_station(42.29822,-71.26543)
    print(find_stop_near('boston university')) #IndexError: list index out of range (fixed)
    #('Wellesley Hills', 2)


if __name__ == '__main__':
    main()
