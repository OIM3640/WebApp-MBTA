import json
import pprint
import urllib.request
import requests

# done based of my last work on assignment 2
with open ('config.json', 'r') as config_file:
    config = json.load(config_file)
# Your API KEYS (you need to use your own keys - very long random characters)

# from config import MAPBOX_TOKEN, MBTA_API_KEY
MAPBOX_TOKEN = config["MAPBOX_TOKEN"]
MBTA_API_KEY = config["MBTA_API_KEY"]

# Useful URLs (you need to add the appropriate parameters for your requests)
MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

# query = 'Babson College'
# query = query.replace(' ', '%20')
# url = f'{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi'
# print(url)

# with urllib.request.urlopen(url) as f:
#     response_text = f.read().decode('utf-8')
#     response_data = json.loads(response_text)
#     pprint.pprint(response_data)
#     print(response_data['features'][0]['properties']['address'])
#     for feature in response_data['features']:
#         coordinates = feature['geometry']['coordinates']
#         print(f'Coordinates: {coordinates}')
        # asked chatgpt how to grab the coordinates from the response text


# A little bit of scaffolding if you want to use it
def build_url(query):
    """
    Takes a given query and builds the proper Mapbox url to be used in the later function of get_json
    """
    new_query = query.replace(' ', '%20')
    url = f'{MAPBOX_BASE_URL}/{new_query}.json?access_token={MAPBOX_TOKEN}&types=poi'
    return url
# build_url('Babson College')


def get_json(url: str) -> dict:
    """
    Given a properly formatted URL for a JSON web API request, return a Python JSON object containing the response to that request.

    Both get_lat_long() and get_nearest_station() might need to use this function.
    """
    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode('utf-8')
        response_data = json.loads(response_text)
        # pprint.pprint(response_data)
        # this bottom half of the function was found through chatGPT
        for feature in response_data['features']:
            coordinates = feature['geometry']['coordinates']
            if coordinates:
                latitude = float(coordinates[1])
                longitude = float(coordinates[0])
                return latitude, longitude
# first two functions werer based from the instructions given


# url = build_url('Babson College')   
# get_json(url)
# asked chatGPT how to debug the interaction between build_url and get_json functions 
# def get_lat_long(place_name: str) -> tuple[str, str]:
#     """
#     Given a place name or address, return a (latitude, longitude) tuple with the coordinates of the given place.

#     See https://docs.mapbox.com/api/search/geocoding/ for Mapbox Geocoding API URL formatting requirements.
#     """
#     pass

# def get_nearest_station(latitude: str, longitude: str) -> tuple[str, bool]:

# asked multiple iterations in chatGPT on how to arrive at this final code
# first asked how to use the MBTA API
# next was to ask how to grab the data from the earlier functions to be used to find the nearest station
def get_nearest_station(latitude: float, longitude: float) -> None:
    """
    Given latitude and longitude strings, return a station_name for the nearest MBTA station to the given coordinates.

    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL formatting requirements for the 'GET /stops' API.
    """
    url = MBTA_BASE_URL
    params = {
        'api_key': MBTA_API_KEY,
        'sort': 'distance',
        'filter[latitude]': latitude,
        'filter[longitude]': longitude
        
        
    }
    response = requests.get(url, params=params)
    # print(response.url)
    #print(response.text) 
    if response.status_code == 200:
        stations = response.json()['data']
        # print (stations)
        if stations:
            closest_station = stations[0]
            station_name = closest_station['attributes']['name']
            station_latitude = closest_station['attributes']['latitude']
            station_longitude = closest_station['attributes']['longitude']
            # distance = closest_station['attributes']['distance']
            # wheelchair_accessible = closest_station['attributes']['wheelchair_boarding']
            # if wheelchair_accessible == 1:
            #     accessibility_status = 'Wheelchair Accessible'
            #     # need to return the accessibility status
            #     return accessibility_status
            # else:
            #     accessibility_status = 'Not Wheelchair Accessible'
            print(f'Closest station: {station_name}')
            print(f'Station Coordinates: Latitude: {station_latitude}, Longitude: {station_longitude}')
            # print(f'Distance: {distance} meters')
            # print(f'Accessibility: {accessibility_status}')
        else:
            print('No stations found nearby')
    else:
        print('Error fetching data from the MBTA API')
    return station_name

# essentially used the code right above but modified to return only wheelchair acccesibility
def get_wheelchair_status(latitude: float, longitude: float) -> None:
    """
    Given latitude and longitude strings, return if station is wheelchair_accessible for the nearest MBTA station to the given coordinates.

    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL formatting requirements for the 'GET /stops' API.
    """
    url = MBTA_BASE_URL
    params = {
        'api_key': MBTA_API_KEY,
        'sort': 'distance',
        'filter[latitude]': latitude,
        'filter[longitude]': longitude
        
        
    }
    response = requests.get(url, params=params)
    # print(response.url)
    #print(response.text) 
    if response.status_code == 200:
        stations = response.json()['data']
        # print (stations)
        if stations:
            closest_station = stations[0]
            wheelchair_accessible = closest_station['attributes']['wheelchair_boarding']
            if wheelchair_accessible == 1:
                accessibility_status = 'Wheelchair Accessible'
            else:
                accessibility_status = 'Not Wheelchair Accessible'
        else:
            print('No stations found nearby')
    else:
        print('Error fetching data from the MBTA API')
    return accessibility_status

    
# query = 'Massachusetts Institute of Technology'
# url = build_url(query)
# latitude, longitude = get_json(url)
# get_nearest_station(latitude, longitude)
# asked chatGPT how to use the MBTA API to pull the station data and whether it was wheelchair accessible or not
# def find_stop_near(place_name: str) -> tuple[str, bool]:
#     """
#     Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

#     This function might use all the functions above.
#     """
#     pass


def main():
    """
    You should test all the above functions here
    """
    query = 'Boston College'
    url = build_url(query)
    latitude, longitude = get_json(url)
    get_nearest_station(latitude,longitude)
    get_wheelchair_status(latitude, longitude)


if __name__ == '__main__':
    main()
