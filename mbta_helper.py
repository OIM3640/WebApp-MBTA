# Your API KEYS (you need to use your own keys - very long random characters)
from config import MAPBOX_TOKEN, MBTA_API_KEY, WEATHER_APIKEY, TICKET_KEY

import json
import pprint
import urllib.request

# Useful URLs (you need to add the appropriate parameters for your requests)
MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"
   
def url_encode(place_name: str) -> str:
    """
    
    """
    place_name = place_name.replace(' ', '%20')
    url = f'{MAPBOX_BASE_URL}/{place_name}.json?access_token={MAPBOX_TOKEN}&types=poi'
    return url

# A little bit of scaffolding if you want to use it
# def get_json(url: str) -> dict:
#     """
#     Given a properly formatted URL for a JSON web API request, return a Python JSON object containing the response to that request.

#     Both get_lat_long() and get_nearest_station() might need to use this function.
#     """
#     query = 'Babson College'
#     query = query.replace(' ', '%20') # In URL encoding, spaces are typically replaced with "%20"
#     url=f'{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi'
#     print(url) # Try this URL in your browser first

#     with urllib.request.urlopen(url) as f:
#         response_text = f.read().decode('utf-8')
#         response_data = json.loads(response_text)
#         pprint.pprint(response_data)
    
#     print(response_data['features'][0]['properties']['address'])

def get_lat_long(place_name: str) -> tuple[str, str]:
    """
    Given a place name or address, return a (latitude, longitude) tuple with the coordinates of the given place.

    See https://docs.mapbox.com/api/search/geocoding/ for Mapbox Geocoding API URL formatting requirements.
    """
    place_name = place_name.replace(' ', '%20')
    url =f'{MAPBOX_BASE_URL}/{place_name}.json?access_token={MAPBOX_TOKEN}&types=poi'

    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode('utf-8')
        response_data = json.loads(response_text)

    longitude, latitude = response_data['features'][0]['center']
    return latitude,longitude 

def get_nearest_station(latitude: str, longitude: str) -> tuple[str, bool]:
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible) tuple for the nearest MBTA station to the given coordinates.

    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL formatting requirements for the 'GET /stops' API.
    """
    mbta_url = f"{MBTA_BASE_URL}?filter[latitude]={latitude}&filter[longitude]={longitude}&sort=distance&api_key={MBTA_API_KEY}"

    print(mbta_url)

    with urllib.request.urlopen(mbta_url) as f:
        response_text = f.read().decode('utf-8')
        response_data = json.loads(response_text)
        pprint.pprint(response_data)

        station_name = response_data['data'][0]['attributes']['name']
        print(station_name)

        wheelchair_accessible = response_data['data'][0]['attributes']['name']
        print(wheelchair_accessible)
        return station_name, wheelchair_accessible
 


def find_stop_near(place_name: str) -> tuple[str, bool]:
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """
    pass

def get_temperature(place_name):
    """
    
    """
    url = f'https://api.openweathermap.org/data/2.5/weather?q={place_name},us&APPID={WEATHER_APIKEY}&units=metric'
    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode('utf-8')
        response_data = json.loads(response_text)
    
    return response_data['main']['temp']

# def find_event(place_name):
#     """
    
#     """
#     url = f'https://app.ticketmaster.com/discovery/v2/events.json?{TICKET_KEY}'
#     with urllib.request.urlopen(url) as f:
#         response_text = f.read().decode('utf-8')
#         response_data = json.loads(response_text)
    
#     return response_data['main']['temp']


def main():
    """
    You should test all the above functions here
    """
    place_name = input("Please provide a place name or address: ")
    print (get_lat_long(place_name)) 
    longitude, latititude = get_lat_long(place_name)
    print(get_nearest_station(longitude, latititude))
    print(get_temperature(place_name))


if __name__ == '__main__':
    main()


