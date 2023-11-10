from config import API_KEY_MAP
import json, urllib.request

MAPBOX_BASE_URL = 'https://api.mapbox.com/geocoding/v5/mapbox.places'
MAPBOX_TOKEN = API_KEY_MAP

query = input('\nPlease type in the name of the closest business/building you are near:\n\n')
query = query.replace(' ', '%20')
url = f'{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi'

# print(url)

with urllib.request.urlopen(url) as f:
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    # pprint.pprint(response_data)

# Function to extract the latitude and longitude from the MAPBOX JSON response
def get_coords():
    """
    Returns the set of coordinates for feature 0 in dictionary in a list
    """
    your_coords = []
    k = response_data['features'][0]['geometry']['coordinates']

    for i in k:
        your_coords.append(i)

    return your_coords

# print(f'The coordinates of that destination are: {get_coords()}')
# print(url)