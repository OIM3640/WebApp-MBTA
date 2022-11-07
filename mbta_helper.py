# Your API KEYS (you need to use your own keys - very long random characters)
# from config import MAPQUEST_API_KEY, MBTA_API_KEY
from configparser import ConfigParser
import urllib.request 
import json 
from pprint import pprint 
from urllib.parse import urlencode 

# Useful URLs (you need to add the appropriate parameters for your requests)
config = ConfigParser()
config.read('config/config.ini')
MAPQUEST_API_KEY = config.get('MAPQUEST', 'MAPQUEST_API_KEY')
MBTA_API_KEY = config.get('MBTA', 'MBTA_API_KEY')
weather_API_KEY = config.get('openweathermap', 'weather_API_KEY')
air_API_KEY = config.get('AIRVISUAL', 'air_API_KEY')

MAPQUEST_BASE_URL = "https://www.mapquestapi.com/geocoding/v1/address?"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops?"
# MAPQUEST_API_KEY = 's3TPavFyK0zg2h1kyscEOE8YMptpk2yU'
# MBTA_API_KEY = '797d5d3a4cf54c3993dc93d5f54a49ce'
# weather_API_KEY = 'd79b7191a0578bfcb747de50bb6825c0'
events_API_KEY = 'KmXKmlzZgHhfaWrjq5J73ytov3DGtL1Y'
# air_API_KEY = '8d3ae0cd-8759-42a7-a907-5bd9872c75ce'

# MAPQUEST_API_KEY = 's3TPavFyK0zg2h1kyscEOE8YMptpk2yU'
# LOCATION = 'Babson%20College'
# url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location={LOCATION}' 

# A little bit of scaffolding if you want to use it


def get_url(LOCATION): 
    """write a function that takes an address or place name as input and returns a properly encoded URL to make a MapQuest geocode request."""
    MAPQUEST_url = MAPQUEST_BASE_URL + urlencode({"key": MAPQUEST_API_KEY, "location": LOCATION})
    return MAPQUEST_url

def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.

    Both get_lat_long() and get_nearest_station() might need to use this function.
    """
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    # pprint(response_data)
    return response_data


def get_lat_long(place_name): 
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developer.mapquest.com/documentation/geocoding-api/address/get/
    for Mapquest Geocoding API URL formatting requirements.
    """
    url = get_url(place_name)
    response_data = get_json(url) 
    j = response_data['results'][0]['locations'][0] 
    lat = j['latLng']['lat']
    lng = j['latLng']['lng']
    t =  (lat, lng)
    return t


def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.

    Value	Meaning
    0	No Information
    1	Accessible (if trip is wheelchair accessible)
    2	Inaccessible
    """
    MBTA_url = MBTA_BASE_URL + urlencode({'api_key': MBTA_API_KEY, 'sort': 'distance', 'filter[latitude]': latitude, 'filter[longitude]': longitude})
    data = get_json(MBTA_url)
    if data['data'] != []: 
        station_name = data['data'][0]['attributes']['name']
        wheelchair_boarding = data["data"][0]['attributes']["wheelchair_boarding"]
        t = (station_name, wheelchair_boarding)
        return t
    else: 
        return None 

def get_weather(latitude, longitude): 
    """returm curretn weather and temperature """
    weather_url = f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={weather_API_KEY}'
    data = get_json(weather_url)
    weather = data['weather'][0]['description']
    temp = data['main']['temp']
    return weather, temp 

# def get_events(post_code): 
#     events_url = f'https://app.ticketmaster.com/discovery/v2/events.json?postalCode={post_code}&apikey={events_API_KEY}'
#     data = get_json(events_url)
#     events = ["_embedded"]['events'][0]['name']
#     return events 


def get_airquality(latitude, longitude): 
    """return curretn air quality """
    air_url = f'http://api.airvisual.com/v2/nearest_city?lat={latitude}&lon={longitude}&key={air_API_KEY}'
    data = get_json(air_url)
    air_quality = data['data']['current']['pollution']['aqius']
    return air_quality


def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """
    latitude, longitude = get_lat_long(place_name)
    weather, temp = get_weather(latitude, longitude) 
    air_quality = get_airquality(latitude, longitude)
    if get_nearest_station(latitude, longitude) == None: 
        return None 
    else: 
        latitude, longitude = get_lat_long(place_name)
        near_stop, wheelchair_boarding = get_nearest_station(latitude, longitude)
        if wheelchair_boarding == 1: 
            wheelchair_accessible = 'accessible'
        elif wheelchair_boarding == 2: 
            wheelchair_accessible = 'inaccessible'
        else: 
            wheelchair_accessible = 'unkown'
        return near_stop, wheelchair_accessible, weather, temp, air_quality  


def main():
    """
    You can test all the functions here
    """
    LOCATION = 'Boston Public Garden'
    # LOCATION = 'Boston Commons'
    MAPQUEST_url = get_url(LOCATION)

    # print(get_url(LOCATION))
    # latitude, longitude = get_lat_long(LOCATION)
    # print(get_nearest_station(latitude, longitude))
    
    print(find_stop_near(LOCATION))
    latitude, longitude = get_lat_long(LOCATION)
    print(get_airquality(latitude, longitude))

if __name__ == '__main__':
    main()
