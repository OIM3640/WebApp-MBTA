###1
import requests

# Your API KEYS (you need to use your own keys - very long random characters)

MAPBOX_TOKEN = "pk.eyJ1Ijoib2xpdmlhc2FuIiwiYSI6ImNsb3dmdDBybzBoODAyaXFtbnlnYzE5NWsifQ.to7UXVaPvsqxNdoeiAhWJg"
MBTA_API_KEY = "1828fa4da1ed4d58a11044e033ef26a6"

# Useful URLs (you need to add the appropriate parameters for your requests)
MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

# A little bit of scaffolding if you want to use it
def get_json(url: str) -> dict:
    """
    Given a properly formatted URL for a JSON web API request, return a Python JSON object containing the response to that request.

    Both get_lat_long() and get_nearest_station() might need to use this function.
    """
    response = requests.get(url)
    return response.json()

def get_lat_long(place_name: str) -> tuple[str, str]:
    """
    Given a place name or address, return a (latitude, longitude) tuple with the coordinates of the given place.

    See https://docs.mapbox.com/api/search/geocoding/ for Mapbox Geocoding API URL formatting requirements.
    """
    mapbox_url = f"{MAPBOX_BASE_URL}/{place_name}.json?access_token={MAPBOX_TOKEN}"
    response = get_json(mapbox_url)
    
    features = response.get('features', [])
    if features:
        coordinates = features[0].get('geometry', {}).get('coordinates', [])
        if len(coordinates) == 2:
            latitude, longitude = coordinates
            return latitude, longitude
    # Here, we try to get coordinates from the response
    return None, None


# Example:
place_name = "Boston Common"
latitude, longitude = get_lat_long(place_name)
print(f"Coordinates for {place_name}: Latitude {latitude}, Longitude {longitude}")

###2

import json
import pprint
import urllib.request

MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MAPBOX_TOKEN = "pk.eyJ1Ijoib2xpdmlhc2FuIiwiYSI6ImNsb3dmdDBybzBoODAyaXFtbnlnYzE5NWsifQ.to7UXVaPvsqxNdoeiAhWJg"

def get_coordinates(place_name):
    # Replace spaces with "%20" for URL encoding
    query = place_name.replace(' ', '%20')

    # Create the URL
    url = f'{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi'

    # Print the URL for testing
    print(url)

    # Request the data from the URL
    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode('utf-8')

    # Parse the JSON response
    response_data = json.loads(response_text)

    # We try to extract latitude and longitude
    if 'features' in response_data and response_data['features']:
        first_feature = response_data['features'][0]
        if 'center' in first_feature:
            latitude, longitude = first_feature['center']
            return latitude, longitude

    # Return None if the data doesn't contain the expected structure
    return None

# Example 
place_name = 'Babson College'
coordinates = get_coordinates(place_name)
if coordinates:
    print(f'Coordinates for {place_name}: Latitude {coordinates[0]}, Longitude {coordinates[1]}')
else:
    print(f'Unable to retrieve coordinates for {place_name}')

###3

import urllib.parse

MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MAPBOX_TOKEN = "pk.eyJ1Ijoib2xpdmlhc2FuIiwiYSI6ImNsb3dmdDBybzBoODAyaXFtbnlnYzE5NWsifQ.to7UXVaPvsqxNdoeiAhWJg"

def build_mapbox_url(place_name):
    # Replace spaces with "%20" for URL encoding
    query = place_name.replace(' ', '%20')

    params = {
        'access_token': MAPBOX_TOKEN,
        'types': 'poi'  # This is customizable
    }
    # Define parameters for the request

    # Encode the parameters and construct the URL
    encoded_params = urllib.parse.urlencode(params)
    url = f'{MAPBOX_BASE_URL}/{query}.json?{encoded_params}'

    return url

# Example 
place_name = 'Babson College'
url = build_mapbox_url(place_name)
print(url)


###4

import requests

MBTA_BASE_URL = "https://api-v3.mbta.com/stops"
MBTA_API_KEY = "1828fa4da1ed4d58a11044e033ef26a6"

def find_closest_stop(latitude, longitude):
    # Create the URL for MBTA API request
    mbta_params = {
        'filter[latitude]': latitude,
        'filter[longitude]': longitude,
        'sort': 'distance',
        'api_key': MBTA_API_KEY
    }
    mbta_url = f'{MBTA_BASE_URL}?{urllib.parse.urlencode(mbta_params)}'

    try:
        # Send the request to MBTA API
        mbta_response = requests.get(mbta_url)
        mbta_data = mbta_response.json()

        # Check to see if any stops were found
        if mbta_data['data']:
            # Extract information about the closest stop
            closest_stop = mbta_data['data'][0]['attributes']['name']
            accessible = mbta_data['data'][0]['attributes']['wheelchair_boarding'] == 1

            return closest_stop, accessible
        else:
            return None, None  # No stops found

    except requests.RequestException as e:
        print(f"Error accessing MBTA API: {e}")
        return None, None

# Example 
latitude = 42.3601  
longitude = -71.0589  

closest_stop, accessible = find_closest_stop(latitude, longitude)

if closest_stop:
    print(f"The closest MBTA stop is '{closest_stop}' and {'is' if accessible else 'is not'} wheelchair accessible.")
else:
    print("No MBTA stops found.")

