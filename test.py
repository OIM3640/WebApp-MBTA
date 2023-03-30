import urllib.request
import json
from pprint import pprint
# from config import MAPBOX_TOKEN

MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MAPBOX_TOKEN = "pk.eyJ1IjoiZ2luYTYyMjIiLCJhIjoiY2xmdmtmcnk0MDg3NTNzbjBhc3d0aHA0dCJ9.F8SoTEqpK3VDg1XOshpdvg"
query = 'Babson%20College'
url=f'{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi'
print(url) # Try this URL in your browser first

with urllib.request.urlopen(url) as f:
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    pprint(response_data)

print(response_data['features'][0]['properties']['address'])