# I used this file to play around with the functions at the start. the main functions used in the app file are found in find_station.py. I did not want to erase this file as it was part of work however it is not used anywhere else 



import json
import pprint
import urllib.request
import urllib.parse

MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MAPBOX_TOKEN = 'pk.eyJ1IjoiZndvbHRlcjEiLCJhIjoiY2xvcTFuNm1yMGN3NjJpcXE4cDl5bjlhOCJ9.YRXp5p_bTfIuuer-qLPInw'
query = 'Prudential Center'
query = query.replace(' ', '%20') # In URL encoding, spaces are typically replaced with "%20"
url=f'{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi'
print(url) # Try this URL in your browser first. THIS CREATES JSON FILE 

with urllib.request.urlopen(url) as f:
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    pprint.pprint(response_data)


# #print(response_data['features'][0]['properties']['address'])





def get_coordinates(response_data):
    '''This function looks through the response data and returns a tuple of coordinates (latitude, longitude) for the given location'''
    if response_data['features']:
        key_of_feature = response_data['features'][0]
        center = key_of_feature['center']
        longitude, latitude = center  
        return (latitude, longitude) 
    else:
        return None


print(get_coordinates(response_data))

def create_url(location):
    """
    this function creates a url using a location input. this url is used for the geo API
    """
    MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
    MAPBOX_TOKEN = 'pk.eyJ1IjoiZndvbHRlcjEiLCJhIjoiY2xvcTFuNm1yMGN3NjJpcXE4cDl5bjlhOCJ9.YRXp5p_bTfIuuer-qLPInw'
    query = location
    query = query.replace(' ', '%20') # In URL encoding, spaces are typically replaced with "%20"
    url =f'{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi'
    return url
    






def get_closest_mbta_stop(latitude, longitude, api_key):
    '''this function uses a set of given coordinates to find the nearest train station. It creates a url which is used to call the api. using this url it then looks for 
    data if it exist it then looks the name of station and it it has wheel chair access. '''

    
    base_url = "https://api-v3.mbta.com/stops"
    params = {"sort": "distance", "filter[latitude]": latitude,  "filter[longitude]": longitude,"api_key": api_key}
    url_with_params = base_url + "?" + urllib.parse.urlencode(params) # I used chatgbt for this part I tried creating the url with the same format as the function above but could not make it work

    
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

# Usage example
api_key = '06b53ae5b7cf4a858c5765c130316d25'



    
