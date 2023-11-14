from config import (
    MAPBOX_TOKEN,
    MBTA_API_KEY,
    OPENWEATHERMAP_API_KEY,
    TICKETMASTER_API_KEY,
    BOOKING_API_KEY,
)
import json
import urllib.parse
import urllib.request
import requests

MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"
OPENWEATHERMAP_BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
TICKETMASTER_BASE_URL = "https://app.ticketmaster.com/discovery/v2/events"
BOOKING_BASE_URL = "https://apidojo-booking-v1.p.rapidapi.com/locations/auto-complete"


def get_json(url: str) -> dict:
    """
    Given a properly formatted URL for a JSON web API request, return a Python JSON object containing the response to that request.

    Both get_lat_long() and get_nearest_station() might need to use this function.
    """
    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode("utf-8")
        response_data = json.loads(response_text)
    return response_data


def get_lat_long(place_name: str) -> tuple[str, str]:
    """
    Given a place name or address, return a (latitude, longitude) tuple with the coordinates of the given place.

    See https://docs.mapbox.com/api/search/geocoding/ for Mapbox Geocoding API URL formatting requirements.
    """
    query = place_name.replace(" ", "%20")
    url = f"{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi"
    response_data = get_json(url)

    try:
        coordinates = response_data["features"][0]["geometry"]["coordinates"]
        latitude, longitude = map(str, coordinates[::-1])
        return latitude, longitude
    except (KeyError, IndexError):
        return None, None


def get_nearest_station(latitude: str, longitude: str) -> tuple[str, bool]:
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible) tuple for the nearest MBTA station to the given coordinates.

    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL formatting requirements for the 'GET /stops' API.
    """
    url_params = {
        "sort": "distance",
        "filter[latitude]": latitude,
        "filter[longitude]": longitude,
        "api_key": MBTA_API_KEY,
    }
    encoded_params = urllib.parse.urlencode(url_params)
    mbta_url = f"{MBTA_BASE_URL}?{encoded_params}"
    response_data = get_json(mbta_url)

    try:
        closest_stop_name = response_data["data"][0]["attributes"]["name"]
        wheelchair_accessible = (
            response_data["data"][0]["attributes"]["wheelchair_boarding"] == 1
        )
        return closest_stop_name, wheelchair_accessible
    except (KeyError, IndexError):
        return None, None


def get_weather_info(latitude: str, longitude: str) -> str:
    """
    Using OpenWeather API to return the local weather information
    """
    url_params = {"lat": latitude, "lon": longitude, "appid": OPENWEATHERMAP_API_KEY}
    encoded_params = urllib.parse.urlencode(url_params)
    weather_url = f"{OPENWEATHERMAP_BASE_URL}?{encoded_params}"
    response_data = get_json(weather_url)

    try:
        weather_description = response_data["weather"][0]["description"]
        return weather_description
    except (KeyError, IndexError):
        return "Weather information not available"


def get_ticketmaster_events(latitude, longitude, TICKETMASTER_API_KEY):
    """
    Given latitude and longitude strings, return a list of nearby events on using the TicketMaster API.
    """
    url_params = {
        "apikey": TICKETMASTER_API_KEY,
        "latlong": f"{latitude},{longitude}",
        "radius": "10",
    }
    response = requests.get(TICKETMASTER_BASE_URL, params=url_params)
    if response.status_code == 200:
        events_data = json.loads(response.text)
        return events_data
    else:
        return None


def get_nearby_hotels(
    latitude: str, longitude: str, BOOKING_API_KEY: str
) -> list[dict]:
    """
    Given latitude and longitude strings, return a list of nearby hotels using the hotel booking API.
    """
    hotel_api_key = BOOKING_API_KEY
    headers = {"Authorization": f"Bearer {BOOKING_API_KEY}"}
    params = {"latitude": latitude, "longitude": longitude, "radius": 10}
    response = requests.get(BOOKING_BASE_URL, headers=headers, params=params)

    if response.status_code == 200:
        hotel_data = response.json()
        hotels = hotel_data.get("hotels", [])
        return hotels
    else:
        return []


def find_stop_near(
    place_name: str,
    mapbox_token: str,
    mbta_api_key: str,
    openweathermap_api_key: str,
    ticketmaster_api_key: str,
    booking_api_key: str,
) -> tuple[str, bool, str, list[dict], list[dict]]:
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """
    latitude, longitude = get_lat_long(place_name)
    if latitude is not None and longitude is not None:
        nearest_station = get_nearest_station(latitude, longitude)
        if nearest_station[0] is not None and nearest_station[1] is not None:
            weather_info = get_weather_info(latitude, longitude)
            ticketmaster_events = get_ticketmaster_events(
                latitude, longitude, ticketmaster_api_key
            )
            hotels = get_nearby_hotels(latitude, longitude, booking_api_key)
            return (
                nearest_station[0],
                nearest_station[1],
                weather_info,
                ticketmaster_events,
                hotels,
            )
    return None, None, None, [], []


def main():
    """
    You should test all the above functions here
    """
    place_name = "Malden"
    (
        closest_stop,
        is_accessible,
        weather_info,
        ticketmaster_events,
        hotels,
    ) = find_stop_near(
        place_name,
        MAPBOX_TOKEN,
        MBTA_API_KEY,
        OPENWEATHERMAP_API_KEY,
        TICKETMASTER_API_KEY,
        BOOKING_API_KEY,
    )

    if (
        closest_stop is not None
        and is_accessible is not None
        and weather_info is not None
    ):
        print("Closest MBTA Stop:", closest_stop)
        print("Is Accessible:", is_accessible)
        print("Weather Information:", weather_info)

        if ticketmaster_events:
            print("Ticketmaster Events:")
            for event in ticketmaster_events.get("_embedded", {}).get("events", []):
                print(f"- {event['name']}")
        else:
            print("No Ticketmaster events found.")

        if hotels:
            print("Nearby Hotels:")
            for hotel in hotels:
                print(f"- {hotel.get('name')}")
        else:
            print("No nearby hotels found.")
    else:
        print("No results found or API keys are missing.")


if __name__ == "__main__":
    main()
