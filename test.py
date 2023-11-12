import json
import pprint
import urllib.request

MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MAPBOX_TOKEN = "pk.eyJ1Ijoicm9uYWxkbGl1anIiLCJhIjoiY2xvcHlra3I1MGFxaTJrbG52djMzc3k0MyJ9.Uixk2uqshXS9RYtV5RD3fg"
query = 'Babson College'
query = query.replace(' ', '%20') # In URL encoding, spaces are typically replaced with "%20"
url=f'{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi'
# print(url) # Try this URL in your browser first

with urllib.request.urlopen(url) as f:
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    pprint.pprint(response_data)

print(response_data['features'][0]['geometry']['coordinates'])
# Output: 231 Forest St

# curl -X GET "https://api-v3.mbta.com/stops?sort=distance&filter%5Blatitude%5D=42.296951&filter%5Blongitude%5D=-71.265258" -H "accept: application/vnd.api+json"