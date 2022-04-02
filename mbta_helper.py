# Your API KEYS (you need to use your own keys - very long random characters)
from config import MAPQUEST_API_KEY, MBTA_API_KEY
import urllib.request
from pprint import pprint
import json


# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = "http://www.mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"
MBTA_DISTANCE_URL=''


# A little bit of scaffolding if you want to use it
# upload api and hide 


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
    place_name=place_name.replace(' ','%20')+',MA'
    mapquest_pull=f'{MAPQUEST_BASE_URL}?key={MAPQUEST_API_KEY}&location={place_name}&boundingBox=42.4601311,-71.3159173,42.1755041,-70.8542204' 
    data=dict(get_json(mapquest_pull))
    lat=data['results'][0]['locations'][0]['latLng']['lat']
    lng=data['results'][0]['locations'][0]['latLng']['lng']
    return lat,lng

def get_nearest_station(latitude,longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible, lat, long)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    if longitude>0:
        longitude=-1*longitude
    try:
        mbta_pull=get_json(f'{MBTA_BASE_URL}?api_key={MBTA_API_KEY}&sort=distance&filter%5Blatitude%5D={latitude}&filter%5Blongitude%5D={longitude}')
        station_name=mbta_pull['data'][0]['attributes']['name']
        wheelchair_accessible=mbta_pull['data'][0]['attributes']['wheelchair_boarding']
        lat=mbta_pull['data'][0]['attributes']['latitude']
        long=mbta_pull['data'][0]['attributes']['longitude']
        
        if wheelchair_accessible == 2:
            wheelchair_accessible='not wheelchair accessible'
        elif wheelchair_accessible== 1:
            wheelchair_accessible='unknown'
        else: wheelchair_accessible='wheelchair accessible'
    except IndexError:
        return None
    return station_name,wheelchair_accessible,lat,long


def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """
    lat,long=get_lat_long(place_name)
    stop, wheelchair, lat, long=get_nearest_station(lat,long)
    return stop, wheelchair, lat, long

def map_maker(lat, long,w,h, zoom):
    """
    takes lat, long returns api url of map"""
    return f"https://open.mapquestapi.com/staticmap/v5/map?key={MAPQUEST_API_KEY}&center={lat},{long}&size={w},{h}@2x&zoom={zoom}&locations={lat},{long}"


def main():
    """
    You can test all the functions here
    """
    # pprint(get_json(f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location={location}'))
    # pprint(get_lat_long('boston common'))
    lat,long=get_lat_long('boston common')
    pprint(get_nearest_station(lat,long))
    print(lat,long)


if __name__ == '__main__':
    main()
