from pprint import pprint
import json
import urllib.request
import requests

# Useful URLs (you need to add the appropriate parameters for your requests)
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"
MBTA_API_KEY = '921c13397cb140b2aaf7b840c81c8bc2'
MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MAPBOX_TOKEN = 'pk.eyJ1IjoibGlseWljaGlzZSIsImEiOiJjbGZ5Y2s3a20wcHV6M2RwNmhiZ24zY2xpIn0.tdctb2NgGOa8Sb1out2BRg'


def get_json(url: str) -> dict:
    response = requests.get(url)
    json_data = response.json()
    return json_data


def get_lat_long(place_name: str) -> tuple[str, str]:
    url = f"{MAPBOX_BASE_URL}/{place_name}.json?access_token={MAPBOX_TOKEN}"
    response_data = get_json(url)

    try:
        latitude = str(response_data["features"][0]["center"][1])
        longitude = str(response_data["features"][0]["center"][0])
        return latitude, longitude
    except (IndexError, KeyError):
        return None, None


def get_nearest_station(latitude: str, longitude: str) -> tuple[str, bool]:
    url = f"{MBTA_BASE_URL}?filter[latitude]={latitude}&filter[longitude]={longitude}&sort=distance&api_key={MBTA_API_KEY}"
    response_data = get_json(url)

    try:
        station_name = response_data["data"][0]["attributes"]["name"]
        wheelchair_accessible = response_data["data"][0]["attributes"]["wheelchair_boarding"] == 1
        return station_name, wheelchair_accessible
    except (IndexError, KeyError):
        return None, None


def find_stop_near(place_name: str) -> tuple[str, bool]:
    latitude, longitude = get_lat_long(place_name)

    if latitude is not None and longitude is not None:
        return get_nearest_station(latitude, longitude)
    else:
        return None, None


def main():
    place_name = input("Enter a place name or address: ")
    stop_name, wheelchair_accessible = find_stop_near(place_name)
    if stop_name is not None and wheelchair_accessible is not None:
        print(
            f"The nearest MBTA stop to {place_name} is {stop_name}. Wheelchair accessibility: {wheelchair_accessible}")
    else:
        print("Nearest MBTA stop not found.")


if __name__ == '__main__':
    main()
