import urllib.request
import json
from pprint import pprint

# Your API KEYS (you need to use your own keys - very long random characters)
# from config import MAPQUEST_API_KEY, MBTA_API_KEY
MAPQUEST_API_KEY= "vbvSagGcRQOERezgVV3BPEI4jcGvRAxG"
MBTA_API_KEY= "3e8a26a9583045e1aac5a93e4538d3d4"


def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.

    Both get_lat_long() and get_nearest_station() might need to use this function.
    """
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    return response_data
print(get_json(f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location=Boston%20Univeristy,MA'))
# http://www.mapquestapi.com/geocoding/v1/address?key=vbvSagGcRQOERezgVV3BPEI4jcGvRAxG&location=Boston%20Univeristy,MA

# https://api-v3.mbta.com/stops?api_key=3e8a26a9583045e1aac5a93e4538d3d4&sort=distance&filter%5Blatitude%5D=42.347991943359375&filter%5Blongitude%5D=-71.08220672607422