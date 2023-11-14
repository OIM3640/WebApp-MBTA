import json
import urllib.request
from config import MAPBOX_TOKEN, MBTA_API_KEY, EVENTBRITE_TOKEN, OPENWEATHER_API

MAPBOX_TOKEN = MAPBOX_TOKEN
MBTA_API_KEY = MBTA_API_KEY
EVENTBRITE_TOKEN = EVENTBRITE_TOKEN
MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"
EVENTBRITE_BASE_URL = "https://www.eventbriteapi.com/v3/"
OPENWEATHER_BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


def get_json(url: str) -> dict:
    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode('utf-8')
    return json.loads(response_text)


def get_lat_long(place_name: str) -> tuple[str, str]:
    # this equation was mainly done with chat gpt as I was confused where to start with this one
    query = place_name.replace(' ', '%20')
    url = f'{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}'
    response = get_json(url)
    coordinates = response['features'][0]['geometry']['coordinates']
    return str(coordinates[1]), str(coordinates[0])


def get_nearest_station(latitude: str, longitude: str) -> tuple[str, bool]:
    url = f"{MBTA_BASE_URL}?api_key={MBTA_API_KEY}&filter[latitude]={latitude}&filter[longitude]={longitude}&sort=distance"
    response = get_json(url)
    station = response['data'][0]
    return station['attributes']['name'], station['attributes']['wheelchair_boarding'] == 1


def find_stop_near(place_name: str) -> tuple[str, bool]:
    lat, long = get_lat_long(place_name)
    return get_nearest_station(lat, long)


def get_weather_data(latitude: str, longitude: str) -> dict:
    url = f"{OPENWEATHER_BASE_URL}?lat={latitude}&lon={longitude}&appid={OPENWEATHER_API}"
    return get_json(url)

# def get_eventbrite_events(latitude: str, longitude: str) -> dict:
#     url = f"{EVENTBRITE_BASE_URL}/events/search/?token={EVENTBRITE_TOKEN}&location.latitude={latitude}&location.longitude={longitude}"
#     return get_json(url)


def main():
    place_name = 'Newbury Street'
    station_name, wheelchair_accessible = find_stop_near(place_name)
    print(
        f"The nearest MBTA station to {place_name} is {station_name}, Wheelchair accessible: {'Yes' if wheelchair_accessible else 'No'}")
    lat, long = get_lat_long(place_name)
    weather_data = get_weather_data(lat, long)
    temp = weather_data['main']['temp']
    print(
        f"Weather near {place_name} is {weather_data['weather'][0]['description']}. Temperature: {temp} Kelvins.")

    # eventbrite_events = get_eventbrite_events(lat, long)
    # print(f'Events near you:{eventbrite_events}')
if __name__ == '__main__':
    main()
