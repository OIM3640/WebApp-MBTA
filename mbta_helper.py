from config import (
    MAPBOX_TOKEN,
    MBTA_API_KEY,
    OPEN_WEATHER_API_KEY,
    TICKETMASTER_API_KEY,
    GOOGLE_MAPS_API_KEY,
)
import requests
import json
import pprint
import urllib.request


# Useful URLs (you need to add the appropriate parameters for your requests)
MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

query = "Boston College"
query = query.replace(" ", "%20")
# In URL encoding, spaces are typically replaced with "%20". You can also use urllib.parse.quote function.
url = f"{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi"
# print(url)  # Try this URL in your browser first

with urllib.request.urlopen(url) as f:
    response_text = f.read().decode("utf-8")
    response_data = json.loads(response_text)


def get_json(url: str) -> dict:
    """
    Given a properly formatted URL for a JSON web API request, return a Python JSON object containing the response to that request.

    Both get_lat_lng() and get_nearest_station() might need to use this function.
    """
    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode("utf-8")
        response_data = json.loads(response_text)
    return response_data


# pprint.pprint(get_json(url))


def get_lat_lng(place_name: str) -> tuple[str, str]:
    """
    Given a place name or address, return a (latitude, longitude) tuple with the coordinates of the given place.

    See https://docs.mapbox.com/api/search/geocoding/ for Mapbox Geocoding API URL formatting requirements.
    """
    # query = place_name.replace(" ", "%20")
    # query = query.replace(" ", "%20")
    # url = f"{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi"
    # response = requests.get(url)
    # if response.status_code == 200:
    #     data = response.json()
    #     longitude, latitude = data["features"][0]["center"]
    #     return str(latitude), str(longitude)
    # else:
    #     return "Error", "Error"
    query = place_name.replace(" ", "%20")
    url = f"{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()

        if not data["features"]:
            return "Error", "Error"

        longitude, latitude = data["features"][0]["center"]
        return str(latitude), str(longitude)
    else:
        return "Error", "Error"


# lat, lng = get_lat_lng("Babson College")
# print(lat, lng)
# lat, lng = get_lat_lng("Boston College")
# print(lat, lng)


def get_nearest_station(latitude: str, longitude: str) -> tuple[str, bool]:
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible) tuple for the nearest MBTA station to the given coordinates.

    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL formatting requirements for the 'GET /stops' API.
    """
    url = f"https://api-v3.mbta.com/stops?api_key={MBTA_API_KEY}&filter[latitude]={latitude}&filter[longitude]={longitude}&sort=distance"

    response_data = get_json(url)

    if len(response_data["data"]) == 0:
        return "Could not find a stop nearby", False
    else:
        name = response_data["data"][0]["attributes"]["name"]
        wheelchair_accessible = response_data["data"][0]["attributes"][
            "wheelchair_boarding"
        ]
        wheelchair_accessible = bool(wheelchair_accessible)
        return (name, wheelchair_accessible)


# print(get_nearest_station(lat, lng))
# print(get_nearest_station(42.3358655, -71.1694295))


def find_stop_near(place_name: str) -> tuple[str, bool]:
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """
    lat, lng = get_lat_lng(place_name)
    if lat == "Error" or lng == "Error":
        return "Error in getting the coordinates", False

    station_name, wheelchair_accessible = get_nearest_station(lat, lng)
    wheelchair_accessible = bool(wheelchair_accessible)
    return station_name, wheelchair_accessible


# Additional APIs
def get_real_time_nearest_station(place_name: str) -> tuple[str, bool]:
    """
    Given the place name, return the nearest MBTA stop and whether it is wheelchair accessible as well as the real-time data for that stop.
    """
    lat, lng = get_lat_lng(place_name)
    if lat == "Error" or lng == "Error":
        return "Error in getting location coordinates", False, None, None
    url = f"https://api-v3.mbta.com/stops?api_key={MBTA_API_KEY}&filter[latitude]={lat}&filter[longitude]={lng}&sort=distance"
    response_data = get_json(url)

    if not response_data["data"]:
        return "Could not find a stop nearby", False, None, None

    name = response_data["data"][0]["attributes"]["name"]
    wheelchair_accessible = response_data["data"][0]["attributes"][
        "wheelchair_boarding"
    ]
    wheelchair_accessible = bool(wheelchair_accessible)
    stop_id = response_data["data"][0]["id"]
    url_stop = f"https://api-v3.mbta.com/schedules?api_key={MBTA_API_KEY}&filter[stop]={stop_id}"
    # print(url_stop)
    real_time_nearest_station_data = get_json(url_stop)

    if not real_time_nearest_station_data["data"]:
        return (
            name,
            wheelchair_accessible,
            "No real-time data available",
            "No real-time data available",
        )

    arrival_time = real_time_nearest_station_data["data"][0]["attributes"][
        "arrival_time"
    ]
    departure_time = real_time_nearest_station_data["data"][0]["attributes"][
        "departure_time"
    ]
    return name, wheelchair_accessible, arrival_time, departure_time


# print(get_real_time_nearest_station("Boston University"))


def get_city_name(place_name: str) -> str:
    """
    Given a place name or address, return the city name of the given place.
    https://developers.google.com/maps/documentation/places/web-service/op-overview
    """
    place_name_encoded = place_name.replace(" ", "%20")
    # requests.utils.quote(place_name)
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={place_name_encoded}&key={GOOGLE_MAPS_API_KEY}"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()

        if data["status"] == "OK":
            for component in data["results"][0]["address_components"]:
                if (
                    "locality" in component["types"]
                    and "political" in component["types"]
                ):
                    return component["long_name"]

            return "City name not found"
        else:
            return "Error: Google Maps could not find the location"
    else:
        return "Error: Failed to contact Google Maps API"


# print(get_city_name("Boston College"))


def get_city_weather(place_name):
    """
    Given a place name or address, return the current temperature in Fahreneit , main weather condition, and a brief description of the weather for the city.
    """
    city = get_city_name(place_name)
    country_code = "us"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&APPID={OPEN_WEATHER_API_KEY}&units=imperial"

    try:
        with urllib.request.urlopen(url) as f:
            response_text = f.read().decode("utf-8")
            response_data = json.loads(response_text)

        weather_data = {
            "temperature": response_data["main"]["temp"],
            "condition": response_data["weather"][0]["main"],
            "description": response_data["weather"][0]["description"],
        }
        return weather_data
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": "Failed to retrieve weather data"}


# print(get_city_weather("Boston College"))


def get_nearby_events(place_name):
    """
    Retrieves top 6 of nearby events based on the given place name using ticketmaster API.
    """
    lat, lng = get_lat_lng(place_name)
    if lat == "Error" or lng == "Error":
        return ["Error in getting location coordinates"]

    url = f"https://app.ticketmaster.com/discovery/v2/events.json?apikey={TICKETMASTER_API_KEY}&latlong={lat},{lng}&size=6"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        events = []

        # Extract relevant information for each event
        for event in data["_embedded"]["events"]:
            event_info = {
                "name": event["name"],
                "url": event["url"],
                "date": event["dates"]["start"]["localDate"],
                "venue": event["_embedded"]["venues"][0]["name"],
            }
            events.append(event_info)

        return events
    else:
        return ["Error in fetching events"]


def top_restaurants_near_station(place_name):
    """
    Retrieves top 3 of nearby restaurants based on the given place name using Google Map API.
    """
    lat, lng = get_lat_lng(place_name)
    if lat == "Error" or lng == "Error":
        return ["Error in getting location coordinates"]

    station_name, _ = get_nearest_station(lat, lng)

    station_lat, station_lng = get_lat_lng(station_name)

    places_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        "location": f"{station_lat},{station_lng}",
        "radius": 1000,  # Search within 1000 meters of the station
        "type": "restaurant",
        "key": GOOGLE_MAPS_API_KEY,
    }

    response = requests.get(places_url, params=params)
    if response.status_code == 200:
        results = response.json()["results"]

        # Sort the results by rating and get the top 5
        top_restaurants = sorted(
            results, key=lambda x: x.get("rating", 0), reverse=True
        )[:5]

        # Extract relevant information for each restaurant
        restaurant_info = [
            {
                "name": restaurant["name"],
                "address": restaurant["vicinity"],
                "rating": restaurant.get("rating"),
            }
            for restaurant in top_restaurants
        ]

        return restaurant_info
    else:
        return ["Error in fetching restaurant data"]


def main():
    """
    You should test all the above functions here
    """
    print("Coordinates for Boston College:")
    print(get_lat_lng("Boston College"))

    print("Coordinates for Boston University:")
    print(get_lat_lng("Boston University"))

    print("Nearest MBTA station for Boston College:")
    print(get_nearest_station(42.3358655, -71.1694295))

    print(find_stop_near("Boston College"))
    print(find_stop_near("Boston University"))

    print(get_real_time_nearest_station("Boston College"))
    print(get_real_time_nearest_station("Boston University"))
    print(get_real_time_nearest_station("Massachusetts Institute of Technology"))

    print(get_city_name("Boston University"))

    print(get_city_weather("Boston University"))

    # events = get_nearby_events("Babson College")
    # for event in events:
    #     pprint.pprint(event)

    restaurants = top_restaurants_near_station("Boston University")
    for restaurant in restaurants:
        pprint.pprint(restaurant)


if __name__ == "__main__":
    main()
