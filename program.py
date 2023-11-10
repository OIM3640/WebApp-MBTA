from config import API_KEY_MAP, API_KEY_MBTA
import json, urllib.request

MAPBOX_BASE_URL = 'https://api.mapbox.com/geocoding/v5/mapbox.places'
MAPBOX_TOKEN = API_KEY_MAP

MBTA_BASE_URL = 'https://api-v3.mbta.com/stops'
MBTA_TOKEN = API_KEY_MBTA


def make_mapbox_url(query:str):
    """
    Return properly formatted url from a given query for mapbox
    """
    query = query.replace(' ', '%20')
    url = f'{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi'
    return url


def get_json(url:str):
    """
    Return JSON object from a given properly-formatted URL
    """
    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode('utf-8')
        response_data = json.loads(response_text)
    
    return response_data


def get_coords(response_data:dict):
    """
    Return coordinates from response as a tuple
    """
    your_coords = ()
    k = response_data['features'][0]['geometry']['coordinates']

    for i in k:
        your_coords = your_coords + (i,)

    return your_coords



def make_mbta_url(your_coords:tuple):
    """
    Given coordinates, returns a properly formatted url for MBTA API request
    """
    sort_filt = 'distance'
    radius = '0.05'
    latitude = your_coords[-1]
    longitude = your_coords[0]

    url = f"{MBTA_BASE_URL}?sort={sort_filt}&filter%5Blatitude%5D={latitude}&filter%5Blongitude%5D={longitude}&filter%5Bradius%5D={radius}&api_key={MBTA_TOKEN}"

    return url


def get_stations(url:str):
    """
    Returns a list of closest station given a URL
    """
    response_data = get_json(url)

    close_stations = []

    if 'data' in response_data:
        for entity in response_data['data']:
            description = entity['attributes'].get('description')
            if description is not None and description != "":
                close_stations.append(description)
                break

    return close_stations


def your_closest_station(query:str):
    """
    Takes in a location as a str and returns the nearest mbta station
    """
    url = make_mapbox_url(query)
    dict = get_json(url)
    coords = get_coords(dict)
    station = make_mbta_url(coords)
    station_names = get_stations(station)

    if station_names:
        print(f'The closest station is: {station_names}')
    else:
        print('No station data found.')
