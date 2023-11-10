import json
import pprint
import urllib.request

MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MAPBOX_TOKEN = 'pk.eyJ1IjoiZndvbHRlcjEiLCJhIjoiY2xvcTFuNm1yMGN3NjJpcXE4cDl5bjlhOCJ9.YRXp5p_bTfIuuer-qLPInw'
query = 'Babson College'
query = query.replace(' ', '%20') # In URL encoding, spaces are typically replaced with "%20"
url=f'{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi'
print(url) # Try this URL in your browser first

""" with urllib.request.urlopen(url) as f:
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    pprint.pprint(response_data)


print(response_data['features'][0]['properties']['address'])
 """


#def get_geometry(): 

    
