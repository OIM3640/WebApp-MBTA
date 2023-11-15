# Your API KEYS (you need to use your own keys - very long random characters)
from config import MAPBOX_TOKEN, MBTA_API_KEY
import json
import pprint
import urllib.request

MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
query = 'Babson College'
query = query.replace(' ', '%20') # In URL encoding, spaces are typically replaced with "%20"
url=f'{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi'
print(url) # Try this URL in your browser first

with urllib.request.urlopen(url) as f:
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    pprint.pprint(response_data)

# Useful URLs (you need to add the appropriate parameters for your requests)
MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"
print(response_data['features'][0]['properties']['address'])

# A little bit of scaffolding if you want to use it
def get_json(url: str) -> dict:
    """
    Given a properly formatted URL for a JSON web API request, 
    return a Python JSON object containing the response to that request.

    Both get_lat_long() and get_nearest_station() might need to use this function.
    takes a string parameter url and returns a dictionary (dict)
    """
    with urllib.request.urlopen(url) as f: #This line opens a URL for reading uses Python's urllib.request.urlopen method, which sends an HTTP f is a file-like object representing the opened URL
        response_text = f.read().decode('utf-8') #reads the entire response from the URL (f.read()) and decodes it from UTF-8 format
        response_data = json.loads(response_text) #converts the JSON formatted string (response_text) into a Python dictionary (response_data) using json.loads()
    return response_data #eturns the Python dictionary containing the JSON response

def get_lat_long(place_name: str) -> tuple[str, str]: #akes a string parameter place_name and returns a tuple of two floats (longitute and latitude)
    """
    Given a place name or address, return a (latitude, longitude) tuple with the coordinates of the given place.

    See https://docs.mapbox.com/api/search/geocoding/ for Mapbox Geocoding API URL formatting requirements.
    """
    query = urllib.parse.quote(place_name)  # the function URL-encodes
    url = f'{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi' #constructs the URL for the Mapbox API request  The URL asks for JSON-formatted data about the point of interest (poi) matching the place_name.
    response_data = get_json(url) #get_json function is called with the constructed URL to get the response from the Mapbox API as a Python dictionary

    # Extract latitude and longitude
    coordinates = response_data['features'][0]['geometry']['coordinates'] #extract the coordinates from the response data where the latitude and longitude are located under ['features'][0]['geometry']['coordinates']
    longitude, latitude = coordinates  # Mapbox API returns coordinates in [longitude, latitude] order
    return latitude, longitude #^unpack the coordinates list into longitude and latitude variables. 
    #API returns coordinates in the order of [longitude, latitude]

def get_nearest_station(latitude: str, longitude: str) -> tuple[str, bool]:
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible) tuple for the nearest MBTA station to the given coordinates.

    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL formatting requirements for the 'GET /stops' API.

    takes two parameters: latitude and longitude, 
    The function return a tuple containing a string represents the station name and 
    the boolean indicates wheelchair accessibility.
    """
    url = f'https://api-v3.mbta.com/stops?sort=distance&filter%5Blatitude%5D={latitude}&filter%5Blongitude%5D={longitude}'
    """This line constructs the URL to make an API request to 
    the MBTA API incorporates the base URL for the API (MBTA_BASE_URL), the API key (MBTA_API_KEY), 
    the latitude and longitude values. The parameters filter[latitude] and filter[longitude] are set 
    sort=distance part of the URL requests that the API return results 
    sort by distance from the provided coordinates."""
    # Get the JSON response from the API
    response_data = get_json(url)

    # Check if there are any stations in the response
    if not response_data['data']: # checks if the data key in the response_data dictionary is empty or not. If it's empty, the function returns a tuple with the string "No station found" and a boolean False
        return "No station found", False
    
    # Get the nearest station's data 
    nearest_station_data = response_data['data'][0] #gets the first item from the data list, which should be the nearest station to the given coordinates the results are sorted by distance
    #extracts the name of the station from the attributes dictionary of nearest_station_data
    
    # Extract the station name and wheelchair accessibility
    station_name = nearest_station_data['attributes']['name']

    wheelchair_accessible = nearest_station_data['attributes']['wheelchair_boarding'] == 1
    #MBTA API indicates wheelchair accessibility with a value of 1 in the wheelchair_boarding field of the attributes dictionary. 
    #This line sets wheelchair_accessible to True if wheelchair_boarding is 1
    return station_name, wheelchair_accessible

def find_stop_near(place_name: str) -> tuple[str, bool]:
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """
    latitude, longitude = get_lat_long(place_name)
    station_name, wheelchair_accessible = get_nearest_station(str(latitude), str(longitude))

    # Check if no station was found and return a consistent value
    if not station_name or station_name == "No station found":
        return None, False
    return station_name, wheelchair_accessible

def main():
    print(get_lat_long('prudential center'))
    # Coordinates for Boston Common latitude = 42.3557 longitude = -71.0656
    latitude = 42.3557
    longitude = -71.0656
    print(get_nearest_station(latitude, longitude))
    print(find_stop_near("newbury"))

if __name__ == '__main__':
    main()
