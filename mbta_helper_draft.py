# Your API KEYS (you need to use your own keys - very long random characters)
from config import MAPBOX_TOKEN, MBTA_API_KEY
import urllib.request
import json
import pprint


# Useful URLs (you need to add the appropriate parameters for your requests)
MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"


# print(url) # Try this URL in your browser first
# A little bit of scaffolding if you want to use it

def get_lat_long(query: str) -> tuple[str, str]:
    """
    Given a place name or address, return a (latitude, longitude) tuple with the coordinates of the given place.

    See https://docs.mapbox.com/api/search/geocoding/ for Mapbox Geocoding API URL formatting requirements.
    """
    query +=',boston,ma'
    query = query.replace(' ', '%20')
    url=f'{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi'
    print(url)
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)

    # length= len(response_data["features"])
    # for i in range(length):
    #     if place_name in response_data["features"][i]['place_name']:
    #         location = response_data["features"][i]["geometry"]["coordinates"]
    #         return tuple(location)
    lng, lat =  response_data['features'][0]["center"]
    return lat, lng

    

def get_nearest_station(latitude: str, longitude: str) -> tuple[str, bool]:
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible) tuple for the nearest MBTA station to the given coordinates.

    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL formatting requirements for the 'GET /stops' API.
    """

    # url = f'{MBTA_BASE_URL}?api_key={MBTA_API_KEY}&sort=distance&filter%5Blatitude%5D={latitude}&filter%5Blongitude%5D={longitude}'
    url = f'{MBTA_BASE_URL}?api_key={MBTA_API_KEY}&sort=distance&filter%5Blatitude%5D={latitude}&filter%5Blongitude%5D={longitude}'
    print(url)
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)

    stop_name = response_data['data'][0]['attributes']['name']  
    wheelchair = response_data['data'][0]['attributes']['wheelchair_boarding']
    if wheelchair == 0:
        return stop_name, "No Informaiton found."
    elif wheelchair == 1:
        return stop_name, "wheelchair accessible"
    elif wheelchair == 2:
        return stop_name, "wheelchair inaccessible"


def get_station(query:str):
    query +=',boston,ma'
    query = query.replace(' ', '%20')
    url=f'{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi'
    print(url)
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    lng, lat =  response_data['features'][0]["center"]

    url = f'{MBTA_BASE_URL}?api_key={MBTA_API_KEY}&sort=distance&filter%5Blatitude%5D={lat}&filter%5Blongitude%5D={lng}'
    print(url)
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    mbta_data = json.loads(response_text)

    stop_name = mbta_data['data'][0]['attributes']['name']  
    wheelchair = mbta_data['data'][0]['attributes']['wheelchair_boarding']
    if wheelchair == 0:
        return stop_name, "No Informaiton found."
    elif wheelchair == 1:
        return stop_name, "wheelchair accessible"
    elif wheelchair == 2:
        return stop_name, "wheelchair inaccessible"


def main():
    """
    You can test all the functions here
    """
    query = "copley place"
    # place_name = "231 Forest St"
    # pprint.pprint(get_json(place_name))
    # latitude, longitude = get_lat_long(query)
    # pprint.pprint(get_nearest_station(latitude,longitude))
    print(get_station(query))



if __name__ == '__main__':
    main()
