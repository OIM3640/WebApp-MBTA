import json
import urllib.request
from urllib.parse import quote


def generate_mapbox_url(address, mapbox_token):
    """
    URL for mapbox
    """
    base_url = "https://api.mapbox.com/geocoding/v5/mapbox.places"
    encoded_address = quote(address)
    return f"{base_url}/{encoded_address}.json?access_token={mapbox_token}&limit=1"


def get_coordinates(address, mapbox_token):
    """
    Latitude and longitude for the address.
    """
    url = generate_mapbox_url(address, mapbox_token)
    with urllib.request.urlopen(url) as response:
        data = json.load(response)
        coordinates = data["features"][0]["geometry"]["coordinates"]
        # Mapbox API returns coordinates in the order [longitude, latitude].
        return coordinates[1], coordinates[0]


def generate_mbta_url(lat, lon, mbta_api_key):
    """
    Generate a URL based on latitude and longitude
    """
    base_url = "https://api-v3.mbta.com/stops"
    return f"{base_url}?filter[latitude]={lat}&filter[longitude]={lon}&sort=distance&api_key={mbta_api_key}"


def find_closest_mbta_stop(lat, lon, mbta_api_key):
    """
    Find the closest transition stop.
    """
    url = generate_mbta_url(lat, lon, mbta_api_key)
    with urllib.request.urlopen(url) as response:
        data = json.load(response)
        stop_name = data["data"][0]["attributes"]["name"]
        wheelchair_accessible = data["data"][0]["attributes"]["wheelchair_boarding"]
        # Wheelchair accessibility is represented by a number in the MBTA API.
        # It can be translated to more meaningful information as needed.
        return stop_name, wheelchair_accessible


__name__ == "__main__"
MAPBOX_TOKEN = "pk.eyJ1IjoieXpoYW5nMTIiLCJhIjoiY2x1bXNhODdhMHV3OTJpbzFmMDVrOXE3YiJ9.q69jiTi7aXGjGmQDbwukmA"
MBTA_API_KEY = "d9fa3e8fb55e42cc95ede40ff80ab074"
address = "Boston Common, Boston, MA"
