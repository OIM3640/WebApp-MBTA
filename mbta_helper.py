import urllib.request
import json
import ssl
from pprint import pprint
from datetime import datetime, timezone
ssl._create_default_https_context = ssl._create_unverified_context

# Your API KEYS (you need to use your own keys - very long random characters)
MAPBOX_TOKEN = "pk.eyJ1IjoibXN5MDExMDE1IiwiYSI6ImNsZnpxZjFneTB3aGwzb3Bhb3RubGRvZ28ifQ.zFSapXqQ8ccVtVLWG4qIVA"


# Useful URLs (you need to add the appropriate parameters for your requests)
MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"


def get_lat_long(place_name: str) -> tuple[str, str]:
    """
    Given a place name or address, return a (latitude, longitude) tuple with the coordinates of the given place.
    """
    # format the input
    replacement = "%20"
    output_place = place_name.replace(" ", replacement)
    # process the data
    query = output_place
    url = f'{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi'
    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode('utf-8')
        response_data = json.loads(response_text)
    # find the coordinates in the list
    lat_long = tuple(response_data['features'][0]['geometry']['coordinates'])
    lat_long = tuple(f"{coord:.4f}" for coord in lat_long)
    lat_long = tuple(reversed(lat_long))
    # print(type(lat_long))
    return lat_long


def get_nearest_station(latitude: str, longitude: str) -> tuple[str, bool]:
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible) tuple for the nearest MBTA station to the given coordinates.
    """
    MBTA_API_KEY = "fb950d9d0aaa490aac903e818b264994"
    url = f"https://api-v3.mbta.com/stops?api_key={MBTA_API_KEY}&sort=distance&filter%5Blatitude%5D={latitude}&filter%5Blongitude%5D={longitude}"
    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode('utf-8')
        response_data = json.loads(response_text)
        # pprint (response_data) >> use the lat and long to find the nearest stations
        # if can't find any station
        if len(response_data['data']) == 0:
            return None
        # create a list to hold 3 nearest stations
        nearest_stations = []
        # if less than 3 then just find all
        for i in range(min(3, len(response_data['data']))):
            station_name = response_data['data'][i]['attributes']['name']
            wheelchair_accessible = response_data['data'][i]['attributes']['wheelchair_boarding'] == 1
            stop_id = response_data['data'][i]['id']
            # append the tuple to the list
            nearest_stations.append(
                (station_name, wheelchair_accessible, stop_id))
        return nearest_stations


def prediction(stopid):
    """
    Given stop ids, return a list of departure times for each specified stop.
    """
    MBTA_API_KEY = "fb950d9d0aaa490aac903e818b264994"
    # create a list to hold departure time
    predictions = []
    for id in stopid:
        url = f"https://api-v3.mbta.com/predictions?api_key={MBTA_API_KEY}&sort=departure_time&filter%5Bstop%5D={id}"
        with urllib.request.urlopen(url) as f:
            response_text = f.read().decode('utf-8')
            response_data = json.loads(response_text)
            # if prediction available
            if len(response_data['data']) > 0:
                departure_time = response_data['data'][0]['attributes']['departure_time']
                predictions.append(departure_time)
            else:
                predictions.append(None)
    return predictions

def minutes_until_departure(prediction_time):
    """
    Given a departure time prediction, return the number of minutes until the vehicle departs.
    """
    if prediction_time is None:
        return None
    
    # Convert departure time string to datetime object
    departure_time = datetime.fromisoformat(prediction_time[:-6])
    
    # Calculate time difference in seconds and convert to minutes
    time_diff = (departure_time - datetime.now()).total_seconds()
    minutes = int(time_diff // 60)
    
    if minutes < 0:
        return "The Bus Just Left"
    else:
        return f"{minutes} minutes left"


def find_stop_near(place_name: str) -> tuple[str, bool]:
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """
    # find 3 nearest stations
    latitude, longitude = get_lat_long(place_name)
    nearest_stations = get_nearest_station(latitude, longitude)
    # for each station, find the stop id
    stop_ids = []
    if nearest_stations is not None:
        for station in nearest_stations:
            stop_ids.append(station[2])
    else:
        return []
    # prediction
    predictions = prediction(stop_ids)
    # Combine station info with corresponding prediction
    stops_with_predictions = []
    for i, station in enumerate(nearest_stations):
        stop_name = station[0]
        wheelchair_accessible = station[1]
        prediction_time = predictions[i]
        minutes_left = minutes_until_departure(prediction_time)
        stops_with_predictions.append(
            (stop_name, wheelchair_accessible, prediction_time, minutes_left))
    return stops_with_predictions


def main():
    """
    You can test all the functions here
    """
    # print(get_lat_long("Babson College"))
    # print(get_lat_long("boston university"))
    # print(get_nearest_station("42.350692" ,"-71.1063435"))
    print(find_stop_near('boston university'))
    # pprint(prediction(stop_id))


if __name__ == '__main__':
    main()
