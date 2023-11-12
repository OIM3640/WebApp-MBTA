import requests
from config import MAPBOX_TOKEN, MBTA_API_KEY

# Useful URLs
MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

def get_json(url: str, params: dict) -> dict:
    """
    Send a GET request to the specified URL with 
    parameters and return the JSON response.
    """
    response = requests.get(url, params=params)
    response.raise_for_status()  # This will raise an exception for HTTP errors.
    return response.json()

def get_lat_long(address: str) -> tuple:
    """
    Given a place name or address, return a (latitude, longitude) 
    tuple with the coordinates of the given place.
    """
    encoded_address = requests.utils.quote(address)
    url = f"{MAPBOX_BASE_URL}/{encoded_address}.json"
    params = {'access_token': MAPBOX_TOKEN}
    data = get_json(url, params)
    if data['features']:
        longitude, latitude = data['features'][0]['center']
        return latitude, longitude
    else:
        raise ValueError("No geocoding data found for the provided address.")

def find_nearest_station(latitude: float, longitude: float) -> tuple:
    """
    Given latitude and longitude, return the name of the nearest MBTA station 
    and its wheelchair accessibility status.
    """
    params = {
        'api_key': MBTA_API_KEY,
        'sort': 'distance',
        'filter[latitude]': latitude,
        'filter[longitude]': longitude
    }
    data = get_json(MBTA_BASE_URL, params)
    if data['data']:
        station_name = data['data'][0]['attributes']['name']
        wheelchair_status_code = data['data'][0]['attributes']['wheelchair_boarding']
        wheelchair_accessible = interpret_wheelchair_accessibility(wheelchair_status_code)
        return station_name, wheelchair_accessible
    else:
        raise ValueError("No nearby MBTA stops found.")

def find_stop_near(place_name: str) -> tuple:
    """
    Given a place name or address, return the nearest MBTA 
    stop and whether it is wheelchair accessible.
    """
    latitude, longitude = get_lat_long(place_name)
    return find_nearest_station(latitude, longitude)

def interpret_wheelchair_accessibility(status_code: int) -> str:
    """
    Interpret the wheelchair accessibility status 
    from the MBTA API into a human-friendly string.
    """
    return {
        0: "No information on wheelchair accessibility",
        1: "Wheelchair accessible",
        2: "Not wheelchair accessible"
    }.get(status_code, "Unknown wheelchair accessibility status")

def main():
    """
    Main function to test Mapbox 
    and MBTA API functionality.
    """
    place_name = "Fenway Park"
    try:
        latitude, longitude = get_lat_long(place_name)
        stop_name, wheelchair_accessible = find_nearest_station(latitude, longitude)
        print(f"Latitude: {latitude}, Longitude: {longitude}")
        print(f"Nearest MBTA Stop: {stop_name}")
        print(f"Wheelchair Accessible: {wheelchair_accessible}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()