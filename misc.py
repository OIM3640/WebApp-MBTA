import urllib.request
import json
from pprint import pprint

MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MAPBOX_TOKEN = 'pk.eyJ1IjoiYWJpcnNldGhpIiwiYSI6ImNsZnpzbjZyMTBhc3EzbXFwdnV2enNoZ3YifQ.50Xh5oJ7YoMHk8Aq5aMNiQ'
query = 'Babson%20College'
url=f'{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi'
# print(url) # Try this URL in your browser first

with urllib.request.urlopen(url) as f:
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    pprint(response_data)
# print(response_data['features'][0]['properties']['address'])
# Output: 231 Forest St