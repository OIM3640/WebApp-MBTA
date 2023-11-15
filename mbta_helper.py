# Your API KEYS (you need to use your own keys - very long random characters)
# from config import MAPBOX_TOKEN, MBTA_API_KEY

MAPBOX_TOKEN = 'pk.eyJ1IjoiYXN1cGVyYmFibzAxMiIsImEiOiJjbG94anpqY2sxNjhkMnFwa3NoajhvNzhpIn0.xlbXXqbREbuFjW0ID8b4DQ'
MBTA_API_KEY = '413e4a87c8c9471cb8b11e4aa4c65b4d'
import json
import pprint
import urllib.request

# Useful URLs (you need to add the appropriate parameters for your requests)



# MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

# real_url = f'https://api-v3.mbta.com/stops?api_key={MBTA_API_KEY}&sort=distance&filter%5Blatitude%5D={70}&filter%5Blongitude%5D={80}'



# A little bit of scaffolding if you want to use it
def get_json(url: str) -> dict:
    """
    Given a properly formatted URL for a JSON web API request, return a Python JSON object containing the response to that request.

    Both get_lat_long() and get_nearest_station() might need to use this function.
    """
    print(url) # Try this URL in your browser first
    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode('utf-8')
        response_data = json.loads(response_text)
        # pprint.pprint(response_data)
    return response_data


def get_lat_long(place_name: str) -> tuple[str, str]:
    """
    Given a place name or address, return a (latitude, longitude) tuple with the coordinates of the given place.

    See https://docs.mapbox.com/api/search/geocoding/ for Mapbox Geocoding API URL formatting requirements.
    """
    MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
    query = place_name
    query = query.replace(' ', '%20') # In URL encoding, spaces are typically replaced with "%20"
    url=f'{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi'
    link1 = get_json(url)
    # for i in range(len(link1['features'])):
        # if link1['features'][i]['properties']['address'] == place_name:
    if len(link1) == 0:
        return ('none', 'none')
    else:
        print(link1['features'][0]['center'][1], link1['features'][0]['center'][0])
        return link1['features'][0]['center'][1], link1['features'][0]['center'][0]

def get_nearest_station(latitude: str, longitude: str) -> tuple[str, bool]:
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible) tuple for the nearest MBTA station to the given coordinates.

    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL formatting requirements for the 'GET /stops' API.
    """
    MBTA_website = f'https://api-v3.mbta.com/stops?api_key={MBTA_API_KEY}&sort=distance&filter%5Blatitude%5D={latitude}&filter%5Blongitude%5D={longitude}'
    stop_data = get_json(MBTA_website)
    if len(stop_data["data"]) == 0:
        return ('none', False)
    else:
        # if stop_data['data'][0]['attributes']['latitude'] == latitude and stop_data['data'][0]['attributes']['longitude'] == longitude:
        for i in range(len(stop_data['data'])):
            if stop_data['data'][i]['attributes']['description'] == 'None':
                continue
            else:
                if stop_data['data'][i]['attributes']['wheelchair_boarding'] == 1:
                    return stop_data['data'][i]['attributes']['description'], True
                else:
                    return stop_data['data'][i]['attributes']['description'], False
    return ('None', False)
                

def find_stop_near(place_name: str) -> tuple[str, bool]:
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """
    a,b = get_lat_long(place_name)
    store1 = get_nearest_station(a, b)
    print(store1)
    return store1


def main():
    """
    You should test all the above functions here
    """
    # get_json(url)

    # place_name = '231 Forest St'
    # coordinate_ = get_lat_long(place_name)
    # list2 = coordinate_(0)
    # print(list2)
    # get_nearest_station('42.37431', '-71.11811')   
    # place_name = input('Give me a Place Name: ')
    # print(find_stop_near('Harvard - Brattle Square'))
    # print(find_stop_near('26 Oxford St'))
    print(find_stop_near('Harvard Square'))



if __name__ == '__main__':
    # main()
    print(find_stop_near('Harvard Square'))
