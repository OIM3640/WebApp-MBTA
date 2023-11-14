# Your API KEYS (you need to use your own keys - very long random characters)
#cannot get this to import
# from config import MAPBOX_TOKEN, MBTA_API_KEY
import json
import pprint
import urllib.request
from datetime import datetime

MAPBOX_TOKEN = 'pk.eyJ1IjoibWlrZXN3aWVyIiwiYSI6ImNsb3E4OXp4djA0aWQya21rdzN3YXk0MHcifQ.Y7Sv0ziTdOh6Zn2Fo417nA'

MBTA_API_KEY= '22cf4606afa24b7cb29454b4db4e2fdf'
# Useful URLs (you need to add the appropriate parameters for your requests)
MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

def get_url(query: str):
    query = query.replace(' ', '%20') # In URL encoding, spaces are typically replaced with "%20"
    url=f'{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi'
#     # print(url)
    


# A little bit of scaffolding if you want to use it
def get_json(url: str) -> dict:
    """
    Given a properly formatted URL for a JSON web API request, return a Python JSON object containing the response to that request.

    Both get_lat_long() and get_nearest_station() might need to use this function.
    """
    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode('utf-8')
        response_data = json.loads(response_text)
        return response_data



def get_lat_long(place_name: str) -> tuple[str, str]:
    """
    Given a place name or address, return a (latitude, longitude) tuple with the coordinates of the given place.

    See https://docs.mapbox.com/api/search/geocoding/ for Mapbox Geocoding API URL formatting requirements.
    """
    place_name = place_name.replace(' ', '%20') # In URL encoding, spaces are typically replaced with "%20"
    url=f'{MAPBOX_BASE_URL}/{place_name}.json?access_token={MAPBOX_TOKEN}&types=poi'
    response_data= get_json(url)
    coordinates= response_data['features'][0]['geometry']['coordinates']
    lattitude, longtitude= coordinates[1], coordinates[0]

    return str(lattitude), str(longtitude)



def get_nearest_station(latitude: str, longitude: str) -> tuple[str, bool]:
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible) tuple for the nearest MBTA station to the given coordinates.

    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL formatting requirements for the 'GET /stops' API.
    """
    url = f"{MBTA_BASE_URL}?sort=distance&filter[latitude]={latitude}&filter[longitude]={longitude}&api_key={MBTA_API_KEY}"

    response_data= get_json(url)
    station_id = response_data["data"][0]["id"]

    
    times_url = f"https://api-v3.mbta.com/predictions?filter[stop]={station_id}&api_key={MBTA_API_KEY}"
    times_data = get_json(times_url)

    
    times = []
    for time in times_data["data"]:
        arrival_time = time["attributes"]["arrival_time"]
        times.append({"arrival_time": arrival_time})

    
    return {
        "station_name": response_data["data"][0]["attributes"]["name"],
        "wheelchair_accessible": response_data["data"][0]["attributes"]["wheelchair_boarding"] == 1,
        "times": times
    }
    


def find_stop_near(place_name: str) -> tuple[str, bool]:
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """
    latitude, longitude = get_lat_long(place_name)
    return get_nearest_station(latitude, longitude)


def main():
    """
    You should test all the above functions here
    """
    place_name = "Boston Common"
    print(get_lat_long(place_name))
    results = find_stop_near(place_name)
    pprint.pprint(f'The nearest MBTA Stop is {results["station_name"]}')
    pprint.pprint(f'Wheelchair Accessible: {results["wheelchair_accessible"]}')

    times = results["times"]
    if times:
        print("Real-Time Arrival Data:")
        for time in times:
            arrival_time = time.get('arrival_time')  # from, GPT if there is None
            if arrival_time is not None:
                arrival_time_formatted = datetime.fromisoformat(arrival_time).strftime(" %H:%M (%m-%d-%Y)")
                print(f"Arrival Time is{arrival_time_formatted}")
            else:
                print("Arrival Time: Not available")


if __name__ == '__main__':
    main()
