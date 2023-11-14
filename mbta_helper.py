# Your API KEYS (you need to use your own keys - very long random characters)
from config import MAPBOX_TOKEN, MBTA_API_KEY
import urllib.request
import json
import pprint
from dateutil import parser

# Useful URLs (you need to add the appropriate parameters for your requests)
MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

def get_url(place: str):
    """
    Construct a request URL for the Mapbox Geocoding API.
    """
    try:
        encoded_query = urllib.parse.quote(place)
        url = f'{MAPBOX_BASE_URL}/{encoded_query}.json?access_token={MAPBOX_TOKEN}&limit=1'
        return url
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def get_json(url: str) -> dict:
    """
    Fetches a JSON response from a given URL and converts it into a Python dictionary.

    Parameters:
    - url (str): The URL from which to fetch the JSON data.

    Returns:
    - dict: A dictionary representing the JSON response.
    """
    try:
        with urllib.request.urlopen(url) as response:
            response_text = response.read().decode('utf-8')
            response_data = json.loads(response_text)
            return response_data
    except Exception as e:
        print(f"An error occurred while fetching the JSON: {e}")
        return None

def get_lat_long(place_name: str) -> tuple[str, str]:
    """
    Given a place name or address, return a (latitude, longitude) tuple with the coordinates of the given place.

    """
    # Get the URL for the Mapbox API request
    url = get_url(place_name)
    if not url:
        print("Failed to generate the URL.")
        return None, None

    # Fetch the JSON data from the Mapbox API
    json_data = get_json(url)
    if not json_data:
        print("Failed to fetch JSON data.")
        return None, None

    # Extract the latitude and longitude coordinates
    try:
        coordinates = json_data['features'][0]['center']
        longitude, latitude = map(str, coordinates)  # Mapbox API returns longitude first
        return latitude, longitude
    except (IndexError, KeyError):
        print("Failed to extract latitude and longitude.")
        return None, None


def get_nearest_station(latitude: str, longitude: str, mode: str = None) -> tuple[str, bool]:
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible) tuple for the nearest MBTA station to the given coordinates.

    """
    mode_types = {
        'commuter rail': '2',
        'ferry': '4',
        'metro': '1',
        'bus': '3'
    }
    mode_filter = mode_types.get(mode.lower()) if mode else None

    # Construct the URL with a mode filter 
    url = f'{MBTA_BASE_URL}?api_key={MBTA_API_KEY}&filter[latitude]={latitude}&filter[longitude]={longitude}&sort=distance'
    if mode_filter:
        url += f'&filter[route_type]={mode_filter}'

    # Fetch the JSON data from the MBTA API
    json_data = get_json(url)
    if not json_data:
        print("Failed to fetch JSON data from MBTA.")
        return None, None

    # Extract the nearest station's name and wheelchair accessibility
    try:
        
        # Get the first stop from the data list, which should be the nearest based on the sort parameter
        nearest_station = json_data['data'][0]
        station_name = nearest_station['attributes']['name']
        station_id = nearest_station['id']
        # Wheelchair accessibility is a boolean: 1 for accessible, 2 for not accessible, and 0 for no information
        wheelchair_accessible = nearest_station['attributes']['wheelchair_boarding'] == 1
        return station_name, wheelchair_accessible, station_id
    except (IndexError, KeyError) as e:
        print(f"An error occurred while extracting station information: {e}")
        return None, None, None

def get_realtime_arrival(station_id: str):
    url = f'https://api-v3.mbta.com/predictions?filter[stop]={station_id}&api_key={MBTA_API_KEY}'
    json_data = get_json(url)
    if not json_data:
        print("Failed to fetch real-time data.")
        return None
    
    # Process the JSON data to extract and format arrival times
    formatted_arrival_times = []
    for prediction in json_data.get('data', []):
        arrival_time = prediction['attributes'].get('arrival_time')
        if arrival_time:
            # Parse the ISO 8601 time format and convert it to a string in the desired format
            local_time = parser.isoparse(arrival_time)
            formatted_arrival_times.append(local_time.strftime('%I:%M %p'))  # e.g., "08:45 PM"
    
    return formatted_arrival_times


def find_stop_near(place_name: str, mode_of_travel: str = 'metro') -> tuple[str, bool, str]:
    """
    Given a place name or address, return the nearest MBTA stop, whether it is wheelchair accessible,
    and the station ID.

    """
    # Get latitude and longitude for the given place name
    latitude, longitude = get_lat_long(place_name)
    if not latitude or not longitude:
        print(f"Failed to get coordinates for {place_name}")
        return None, None, None

    # Get the nearest MBTA station using the latitude and longitude
    station_name, wheelchair_accessible, station_id = get_nearest_station(latitude, longitude, mode_of_travel)
    if not station_name:
        print(f"Failed to find the nearest MBTA stop near {place_name}")
        return None, None, None

    return station_name, wheelchair_accessible, station_id

def main():
    place_name = input("Enter the name of the place: ") 
    mode_of_travel = input("Enter your preferred mode of travel (commuter rail, ferry, metro, bus): ") 

    # Get latitude and longitude for the place name
    latitude, longitude = get_lat_long(place_name)
    if not latitude or not longitude:
        print(f"Failed to get coordinates for {place_name}")
        return
    
    # Get the nearest MBTA station and its ID using the latitude, longitude, and mode of travel
    station_name, wheelchair_accessible, station_id = get_nearest_station(latitude, longitude, mode=mode_of_travel)
    if not station_name:
        print(f"Failed to find the nearest MBTA station for mode {mode_of_travel}")
        return

    # Get the real-time arrival data for the station
    arrival_times = get_realtime_arrival(station_id)
    if not arrival_times:
        print(f"Failed to get arrival times for station {station_name}")
        return

    print(f"The nearest MBTA station to {place_name} is {station_name}.")
    print(f"Wheelchair accessible: {'Yes' if wheelchair_accessible else 'No'}")
    print(f"Upcoming arrival times: {arrival_times}")

if __name__ == '__main__':
    main()

