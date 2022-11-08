import urllib.request
import json

from config import MAPQUEST_API_KEY

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

def get_lat(place_name):
    """
    Given a place name or address, return a latitude 
    with the coordinates of the given place.
    See https://developer.mapquest.com/documentation/geocoding-api/address/get/
    for Mapquest Geocoding API URL formatting requirements.
    """
    APIKEY = 'KLCHVIzbwJYnum2wdTaGFsIJX5IGM2y5'
    place_name = place_name.replace(" ","")
    response_data = get_json(f'http://www.mapquestapi.com/geocoding/v1/address?key={APIKEY}&location={place_name}')
    Location_lat = (response_data['results'][0]['locations'][0]['displayLatLng']['lat']) 
    
    return Location_lat

def get_long(place_name):
    """
    Given a place name or address, return a longitude 
    with the coordinates of the given place.
    See https://developer.mapquest.com/documentation/geocoding-api/address/get/
    for Mapquest Geocoding API URL formatting requirements.
    """
    APIKEY = 'KLCHVIzbwJYnum2wdTaGFsIJX5IGM2y5'
    place_name = place_name.replace(" ","")
    response_data = get_json(f'http://www.mapquestapi.com/geocoding/v1/address?key={APIKEY}&location={place_name}') 
    Location_long= (response_data['results'][0]['locations'][0]['displayLatLng']['lng'])
    
    return Location_long


def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    APIKEY = '594f04f3e2cd43b6a8911492d241417a'
    response_data = get_json(f'https://api-v3.mbta.com/stops?api_key={APIKEY}&sort=distance&filter%5Blatitude%5D={latitude}&filter%5Blongitude%5D={longitude}')
    
    a = 0 
    a = int(response_data['data'][0]['attributes']['wheelchair_boarding']) 
    if a == 1:
        wheelchair = 'Wheel Chair Accessible'
    elif a == 2:
        wheelchair = 'Wheel Chair Inaccessible'
    else:
        wheelchair = 'No Information'

    station = (response_data['data'][0]['attributes']['name'], wheelchair)
    
    return station


def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """
    lat = get_lat(place_name)
    long = get_long(place_name)
    try:
        return get_nearest_station(lat, long)
    except:
        return None

def main():
    """
    You can test all the functions here
    """
    location = 'Newbury Street, Boston'
    print (find_stop_near(location))



if __name__ == '__main__':
    main()
