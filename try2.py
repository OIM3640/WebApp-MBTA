# Your API KEYS 
from config import MAPBOX_TOKEN, MBTA_API_KEY

import requests
print(requests.__version__)
from simplejson import json

# Useful URLs 
MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

def get_json(url):
    """Given a properly formatted URL for a JSON web API request, return 
    a Python JSON object containing the response to that request."""
    
    response = requests.get(url)
    return json.loads(response.text)

def get_lat_long(place_name):
    """Given a place name or address, return a (latitude, longitude) tuple with 
    the coordinates of the given place."""
    
    url = f"{MAPBOX_BASE_URL}/{place_name}.json?access_token={MAPBOX_TOKEN}"
    data = get_json(url)
    
    latitude = data['features'][0]['center'][1]
    longitude = data['features'][0]['center'][0]
    
    return (latitude, longitude)

def get_nearest_station(latitude, longitude):
    """Given latitude and longitude strings, return a (station_name, wheelchair_accessible) 
    tuple for the nearest MBTA station to the given coordinates."""
    
    url = f"{MBTA_BASE_URL}?api_key={MBTA_API_KEY}&filter[latitude]={latitude}&filter[longitude]={longitude}&sort=distance"
    data = get_json(url)
    
    station_name = data['data'][0]['attributes']['name']
    wheelchair_accessible = data['data'][0]['attributes']['wheelchair_boarding']
    
    return (station_name, wheelchair_accessible)
    
def find_stop_near(place_name):
    """Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible."""
    
    latitude, longitude = get_lat_long(place_name)
    station_name, wheelchair_accessible = get_nearest_station(latitude, longitude)
    
    return (station_name, wheelchair_accessible)

def main():
    place = "Boston Common"
    print(find_stop_near(place))

if __name__ == '__main__':
    main()