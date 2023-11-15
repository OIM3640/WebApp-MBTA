###5

import requests
import json
import urllib.parse
import folium
import webbrowser
import os

MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MAPBOX_TOKEN = "pk.eyJ1Ijoib2xpdmlhc2FuIiwiYSI6ImNsb3dmdDBybzBoODAyaXFtbnlnYzE5NWsifQ.to7UXVaPvsqxNdoeiAhWJg"
#our unique Mapbox API key

MBTA_BASE_URL = "https://api-v3.mbta.com/stops"
MBTA_API_KEY = "1828fa4da1ed4d58a11044e033ef26a6"
#our unique MBTA API key

APIKEY = '4f2728b36f366688b8ed95b770a37281'
#our unique openweather API key


def get_json(url: str) -> dict:
    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode('utf-8')
        response_data = json.loads(response_text)
        return response_data
#from the given URL, extract the JSON data and return it as a dictionary

def get_lat_long_with_weather(place_name: str) -> dict:
    mapbox_params = {
        'access_token': MAPBOX_TOKEN,
        'types': 'poi'
    }
    mapbox_url = f'{MAPBOX_BASE_URL}/{urllib.parse.quote(place_name)}.json?{urllib.parse.urlencode(mapbox_params)}'
    response_data = get_json(mapbox_url)
    #for a given place, extract the latitude, longitude, and weather information

    coordinates = response_data['features'][0]['geometry']['coordinates']
    latitude, longitude = coordinates[1], coordinates[0]

    #Extract weather information
    city = 'Wellesley'
    country_code = 'us'
    weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&APPID={APIKEY}'

    with urllib.request.urlopen(weather_url) as f:
        weather_response_text = f.read().decode('utf-8')
        weather_data = json.loads(weather_response_text)

    result = {
        'latitude': latitude,
        'longitude': longitude,
        'weather': weather_data
    }

    return result


def find_closest_stop(latitude, longitude, mode='all'):
    mbta_params = {
        'filter[latitude]': latitude,
        'filter[longitude]': longitude,
        'sort': 'distance',
        'api_key': MBTA_API_KEY,
        'filter[route_type]': mode  # '0' for subway, '3' for bus, '2' for commuter rail
    }
    mbta_url = f'{MBTA_BASE_URL}?{urllib.parse.urlencode(mbta_params)}'
#Based on the given latitude and longitude, find the closest MBTA stop

    try:
        mbta_response = requests.get(mbta_url)
        mbta_data = mbta_response.json()

        if mbta_data['data']:
            closest_stop = mbta_data['data'][0]['attributes']
            accessible = closest_stop['wheelchair_boarding'] == 1

            return {'name': closest_stop['name'], 'accessible': accessible}
        else:
            return None

    except requests.RequestException as e:
        print(f"Error accessing MBTA API: {e}")
        return None


def calculate_distance(lat1, lon1, lat2, lon2):
    pass
#Calculate the distance between the coordinate sets

def show_location_on_map(latitude, longitude, stop_name):
    map_center = (latitude, longitude)
    mbta_stop_location = folium.Marker(location=map_center, popup=stop_name)
    mbta_map = folium.Map(location=map_center, zoom_start=15)
    mbta_stop_location.add_to(mbta_map)

    #Show the given location on a map and save the map to an HTML file instead of displaying (due to potential interference with Flask)
    map_filename = 'mbta_map.html'
    mbta_map.save(map_filename)
    print(f"Map saved to {map_filename}")


def main():
    place_name = input("Enter a place name or address: ")
    location_info = get_lat_long_with_weather(place_name)

    if location_info:
        mode = input("Enter your preferred mode of transportation (bus, subway, commuter rail, or all): ")
        closest_stop = find_closest_stop(location_info['latitude'], location_info['longitude'], mode)

        if closest_stop:
            print(f"The closest MBTA stop to {place_name} is '{closest_stop['name']}' and {'is' if closest_stop['accessible'] else 'is not'} wheelchair accessible.")
            # Show location on map
            show_location_on_map(location_info['latitude'], location_info['longitude'], closest_stop['name'])
            # Display weather information
            weather_info = location_info['weather']
            print(f'Current Temperature (Celsius): {weather_info["main"]["temp"] - 273.15:.2f} °C')
        else:
            print("No MBTA stops found.")
    else:
        print(f"Error: Unable to retrieve information for {place_name}.")


if __name__ == "__main__":
    main()
