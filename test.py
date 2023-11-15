MAPBOX_TOKEN = 'pk.eyJ1IjoiYXN1cGVyYmFibzAxMiIsImEiOiJjbG94anpqY2sxNjhkMnFwa3NoajhvNzhpIn0.xlbXXqbREbuFjW0ID8b4DQ'
import json
import pprint
import urllib.request

YOUR_MBTA_API_KEY = '413e4a87c8c9471cb8b11e4aa4c65b4d'

# Useful URLs (you need to add the appropriate parameters for your requests)
MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
query = 'Babson College'
query = query.replace(' ', '%20') # In URL encoding, spaces are typically replaced with "%20"
url=f'{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi'
# print(url) # Try this URL in your browser first
with urllib.request.urlopen(url) as f:
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    # pprint.pprint(response_data)

# print(response_data['features'][4]['properties']['address'])
# print(response_data['features'][2]['properties'])
# Output: 231 Forest St

latitude = response_data['features'][1]['geometry']['coordinates'][0]
longitude = response_data['features'][1]['geometry']['coordinates'][1]

latitude = 42.37431 
longitude = -71.11811

real_url = f'https://api-v3.mbta.com/stops?api_key={YOUR_MBTA_API_KEY}&sort=distance&filter%5Blatitude%5D={latitude}&filter%5Blongitude%5D={longitude}'
# print(real_url)
# real_url = f'{MBTA_BASE_URL}?api_key={YOUR_MBTA_API_KEY}&sort=distance&filter%5Blatitude%5D={latitude}&filter%5Blongitude%5D={longitude}'

with urllib.request.urlopen(real_url) as g:
    response_text1 = g.read().decode('utf-8')
    response_data1 = json.loads(response_text1)
    pprint.pprint(response_data1)

# question1 = input('Give me a place: ')