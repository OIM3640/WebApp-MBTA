from config import API_KEY_MBTA
from mapboxdemo import get_coords
import json, urllib.request

MBTA_BASE_URL = 'https://api-v3.mbta.com/stops'

# Sorting filter
sort_filt = 'distance'

# Sort radius
radius = '0.05'

# Maximum number of results
limit = 35

# Bring coordinates in from mapbox, store in local variable
YOUR_coords = get_coords()

# Split coordinates into a latitude and longitude value
latitude = YOUR_coords[-1]
longitude = YOUR_coords[0]


url = f"{MBTA_BASE_URL}?page%5Blimit%5D={limit}&sort={sort_filt}&filter%5Blatitude%5D={latitude}&filter%5Blongitude%5D={longitude}&filter%5Bradius%5D={radius}&api_key={API_KEY_MBTA}"


with urllib.request.urlopen(url) as f:
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    # pprint.pprint(response_data)

def get_stations():
    """
    Returns the top x stations that are closest to the given coordinates
    """
    close_stations = []
    k = response_data['data']

    for item in k:
        description = item['attributes']['description']
        if description is not None:
            close_stations.append(description)
        
    return close_stations

def count_stations():
    number_of_stations = 0
    for i in get_stations():
        number_of_stations += 1
    
    return number_of_stations

def top_x():
    count = 1 
    print()
    print(f'Here is a list of the {count_stations()} closest MBTA stations to this location:\n')
    for station in get_stations():
        print(f'{count}. {station}')
        count += 1