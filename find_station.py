#from Location import get_coordinates, create_url, get_closest_mbta_stop
import json
import pprint
import urllib.request
import urllib.parse


def create_url(location):
    """
    this function creates a url using a location input. this url is used for the geo API
    """
    MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
    MAPBOX_TOKEN = 'pk.eyJ1IjoiZndvbHRlcjEiLCJhIjoiY2xvcTFuNm1yMGN3NjJpcXE4cDl5bjlhOCJ9.YRXp5p_bTfIuuer-qLPInw'
    query = location
    query = query.replace(' ', '%20') # In URL encoding, spaces are typically replaced with "%20"
    url =f'{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi'
    print(url)
    return url
def get_coordinates(response_data):
    '''This function looks through the response data and returns a tuple of coordinates (latitude, longitude) for the given location'''
    if response_data['features']:
        key_of_feature = response_data['features'][0]
        center = key_of_feature['center']
        longitude, latitude = center  
        latitude = round(latitude, 4)
        longitude= round(longitude, 4)
        print(latitude, longitude)
        return (latitude, longitude) 
    else:
        return None
def get_closest_mbta_stop(latitude, longitude, api_key):
    '''this function uses a set of given coordinates to find the nearest train station. It creates a url which is used to call the api. using this url it then looks for 
    data if it exist it then looks the name of station and it it has wheel chair access. '''


    
    base_url = "https://api-v3.mbta.com/stops"
    params = {"sort": "distance", "filter[latitude]": latitude,  "filter[longitude]": longitude, "filter[radius]": 0.1, "api_key": api_key}
    print(latitude,longitude)
    url_with_params = base_url + "?" + urllib.parse.urlencode(params)
     # I used chatgbt for this part I tried creating the url with the same format as the function above but could not make it work
    print(url_with_params)

    
    with urllib.request.urlopen(url_with_params) as response:
        response_data = response.read()
        data_stations = json.loads(response_data)
        if data_stations['data']:
            closest_stop = data_stations['data'][0]
            stop_name = closest_stop['attributes']['name']
            wheelchair_accessible = closest_stop['attributes']['wheelchair_boarding']
            wheel_chair_access = "Yes" if wheelchair_accessible == 1 else "No"
            return stop_name, wheel_chair_access
        else:
            return "No stops found near you"

def find_closest_station(location):
    api_key_mbta = '06b53ae5b7cf4a858c5765c130316d25'
    url = create_url(location)
    with urllib.request.urlopen(url) as f:
        response = f.read().decode('utf-8')
        response_data = json.loads(response)
        coordinates = get_coordinates(response_data)
        if coordinates:
            latitude, longitude = coordinates
            return get_closest_mbta_stop(latitude, longitude, api_key_mbta)  
        else:
            return "Location coordinates not found"


location = 'Babson College'
print(find_closest_station(location))
    




