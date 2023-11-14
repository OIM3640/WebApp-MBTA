import json
import urllib.request
import urllib.parse
from config import MAPBOX_TOKEN, MBTA_API_KEY

MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"


def get_json(url: str) -> dict:
    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode('utf-8')
        return json.loads(response_text)


def get_lat_long(place_name: str) -> tuple[str, str]:
    encoded_query = urllib.parse.quote(place_name)
    url = f'{MAPBOX_BASE_URL}/{encoded_query}.json?access_token={MAPBOX_TOKEN}&types=poi'
    response_data = get_json(url)

    if 'features' in response_data and response_data['features']:
        first_feature = response_data['features'][0]
        if 'center' in first_feature:
            return tuple(map(str, first_feature['center']))

    return None


def get_nearest_station(latitude: str, longitude: str) -> tuple[str, bool]:
    url = f'{MBTA_BASE_URL}?filter[latitude]={latitude}&filter[longitude]={longitude}&sort=distance&api_key={MBTA_API_KEY}'
    response_data = get_json(url)

    if 'data' in response_data and response_data['data']:
        closest_station = response_data['data'][0]['attributes']['name']
        wheelchair_accessible = response_data['data'][0]['attributes']['wheelchair_boarding'] == 1
        return closest_station, wheelchair_accessible

    return None


def find_stop_near(place_name: str) -> tuple[str, bool]:
    coordinates = get_lat_long(place_name)
    
    if coordinates:
        latitude, longitude = coordinates
        return get_nearest_station(latitude, longitude)

    return None


def main():
    # Example usage
    place_name = "Wellesly"
    result = find_stop_near(place_name)

    if result:
        station_name, wheelchair_accessible = result
        print(f"The nearest MBTA stop to {place_name} is {station_name}.")
        print(f"Wheelchair Accessible: {wheelchair_accessible}")
    else:
        print(f"No MBTA stop found near {place_name}.")

if __name__ == '__main__':
    main()
