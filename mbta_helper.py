# Your API KEYS (you need to use your own keys - very long random characters)
MAPQUEST_API_KEY='QMhaQ4tAP42jeBUajvl64nmkts3mfDO1'
MBTA_API_KEY='2e4902ccdaa848bbabec02723220a826'

# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = "http://www.mapquestapi.com/geocoding/v1/address"
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
    place = place_name.replace(' ','%20')
    url = f"http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location={place}"
    d = get_json(url)
    lst = list()
    lng =  d['results'][0]['locations'][0]['latLng']['lng']
    lat =  d['results'][0]['locations'][0]['latLng']['lat']
    lst.append(lat)
    lst.append(lng)
    t = tuple(lst)
    return t
# get_lat_long('Boston Harbor,ma')

def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    url = f'https://api-v3.mbta.com/stops?api_key={MBTA_API_KEY}&sort=distance&filter%5Blatitude%5D={latitude}&filter%5Blongitude%5D={longitude}'
    d = get_json(url)
    lst = list()
    station_name = list(d.values())[0][0]['attributes']['name']
    wheel = list(d.values())[0][0]['attributes']['wheelchair_boarding']
    if wheel == 1:
        wheelchair_accessible = 'Yes'
    if wheel == 0:
        wheelchair_accessible = 'Maybe'
    else:
        wheelchair_accessible = 'No'
    lst.append(station_name)
    lst.append(wheelchair_accessible)
    t = tuple(lst)
    return t
# get_nearest_station(42.358894, -71.056742)

def find_stop_near_time(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.
    This function might use all the functions above.
    """
    lat = get_lat_long(place_name)[0]
    long = get_lat_long(place_name)[1]
    return get_nearest_station(lat, long)
# find_stop_near('Boston Harbor, MA')

def main():
    """
    You can test all the functions here
    """
    return find_stop_near('Boston Common, MA')


if __name__ == '__main__':
    main()
