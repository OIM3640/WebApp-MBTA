# Your API KEYS (you need to use your own keys - very long random characters)
# from config import MAPBOX_TOKEN, MBTA_API_KEY

TOKEN = "pk.eyJ1IjoienlhbmczIiwiYSI6ImNsdWtoY2c0djBwNjkyam1qaDIzOGxwNHEifQ.-i1DfUI64pspA8nUrJU6eg"
API_KEY = "ad31559715e24741b45b8a986ce62672"


# Useful URLs (you need to add the appropriate parameters for your requests)
MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"


import json
import pprint
import urllib.request

MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MAPBOX_TOKEN = TOKEN

query = "Babson College"
query = query.replace(" ", "%20")
# In URL encoding, spaces are typically replaced with "%20". You can also use urllib.parse.quote function.
url = f"{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi"
# print(url) # Try this URL in your browser first

with urllib.request.urlopen(url) as f:
    response_text = f.read().decode("utf-8")
    response_data = json.loads(response_text)
    # pprint.pprint(response_data)


def get_json(url: str) -> dict:
    """
    Given a properly formatted URL for a JSON web API request,

    return a Python JSON object containing the response to that request.

    Both get_lat_lng() and get_nearest_station() might need to use this function.
    """
    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode("utf-8")
        response_data = json.loads(response_text)
        # pprint.pprint(response_data)
    return response_data


# pprint.pprint(get_json(url))


def get_lat_lng(place_name: str) -> tuple[str, str]:
    """
    Given a place name or address,

    return a (latitude, longitude) tuple with the coordinates of the given place.

    See https://docs.mapbox.com/api/search/geocoding/ for Mapbox Geocoding API URL formatting requirements.
    """
    query = place_name
    query = query.replace(
        " ", "%20"
    )  # In URL encoding, spaces are typically replaced with "%20". You can also use urllib.parse.quote function.
    url = f"{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi"

    response_data = get_json(url)

    result = tuple(response_data["features"][0]["geometry"]["coordinates"][::-1])
    return result


# print(get_lat_lng("Babson College"))


def get_nearest_station(latitude: str, longitude: str) -> tuple[str, bool]:
    """
    Given latitude and longitude strings,

    return a (station_name, wheelchair_accessible) tuple for

    the nearest MBTA station to the given coordinates.

    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL formatting requirements for the 'GET /stops' API.

    Value of Wheelchair Meaning:
    0	No Information
    1	Accessible (if trip is wheelchair accessible)
    2	Inaccessible
    """
    url = f"https://api-v3.mbta.com/stops?api_key={API_KEY}&filter[latitude]={latitude}&filter[longitude]={longitude}&sort=distance"

    response_data = get_json(url)
    # pprint.pprint(response_data)

    if len(response_data["data"]) == 0:
        return f"There isn't any MBTA station nearby."
    else:
        name = response_data["data"][0]["attributes"]["name"]
        wheelchair = response_data["data"][0]["attributes"]["wheelchair_boarding"]
        return (name, wheelchair)


# Test
# print(get_lat_lng("Boston College"))
# pprint.pprint(get_nearest_station(42.3358655, -71.1694295))
# pprint.pprint(get_nearest_station(42.2981925, -71.263598))


def find_stop_near(place_name: str) -> tuple[str, bool]:
    """
    Given a place name or address,

    return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """
    index1 = get_lat_lng(place_name)[0]
    index2 = get_lat_lng(place_name)[1]
    # print(index1,index2)
    return get_nearest_station(index1, index2)


# Test
# print(find_stop_near("Boston College"))


### Optional Question ###
def get_url(place_name: str):
    """
    takes an address or place name as input

    returns a properly encoded URL to make a Mapbox geocoding request
    """
    query = place_name
    query = query.replace(" ", "%20")
    url = f"{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi"
    return url


def get_realtime(place_name: str) -> tuple[str, bool]:
    """
    Given a place name or address,

    return the nearest MBTA stop, whether it is wheelchair accessible, realtime arrival data, and departure time to suggest the optimal station to walk to
    """
    index1 = get_lat_lng(place_name)[0]
    index2 = get_lat_lng(place_name)[1]

    url = f"https://api-v3.mbta.com/stops?api_key={API_KEY}&filter[latitude]={index1}&filter[longitude]={index2}&sort=distance"

    response_data = get_json(url)

    if len(response_data["data"]) == 0:
        return f"There isn't any MBTA station nearby."
    else:
        name = response_data["data"][0]["attributes"]["name"]
        wheelchair = response_data["data"][0]["attributes"]["wheelchair_boarding"]
        stop_id = response_data["data"][0]["id"]
        # Get real time for the route
        url1 = f"https://api-v3.mbta.com/schedules?api_key={API_KEY}&filter[stop]={stop_id}"
        schedule_data = get_json(url1)
        # pprint.pprint(schedule_data)
        arrival_time = schedule_data["data"][0]["attributes"]["arrival_time"]
        departure_time = schedule_data["data"][0]["attributes"]["departure_time"]
        return (name, wheelchair, arrival_time, departure_time)


import urllib.request
import json


def get_city(place_name):
    """
    Input a place and returns the municiple of the place.
    """
    index1 = get_lat_lng(place_name)[0]
    index2 = get_lat_lng(place_name)[1]

    url = f"https://api-v3.mbta.com/stops?api_key={API_KEY}&filter[latitude]={index1}&filter[longitude]={index2}&sort=distance"

    placedata = get_json(url)

    return placedata["data"][0]["attributes"]["municipality"]


def get_temp(place_name):
    """
    Input a place name and returns the temperature in Fahreneit of the municiple of the place.
    """
    index1 = get_lat_lng(place_name)[0]
    index2 = get_lat_lng(place_name)[1]

    url = f"https://api-v3.mbta.com/stops?api_key={API_KEY}&filter[latitude]={index1}&filter[longitude]={index2}&sort=distance"

    placedata = get_json(url)

    city = placedata["data"][0]["attributes"]["municipality"]

    APIKEY = "8429cc7d55e53a9874db5460c45cdb5f"
    country_code = "us"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&APPID={APIKEY}&units=imperial"

    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode("utf-8")
        response_data = json.loads(response_text)
        f = response_data["main"]["temp"]

    return f


import requests


# This code is coded with help of ChatGPT because the data structure is too complicated and ChatGPT helped me understand it better
def get_nearby_events(place_name):
    """
    Input a place and returns the top 5 events along with info about the events nearby.
    """
    index1 = get_lat_lng(place_name)[0]
    index2 = get_lat_lng(place_name)[1]

    api_key = "RfkzywdmNAyyjVzFFjPzZ1aFFi9x3lLX"
    url = f"https://app.ticketmaster.com/discovery/v2/events.json?apikey={api_key}&latlong={index1},{index2}&radius={10}"

    response = requests.get(url)
    data = response.json()

    events = []
    # Check whether there is any avaliable events nearby
    if "_embedded" in data and "events" in data["_embedded"]:
        for event in data["_embedded"]["events"][:5]:
            # get the top 5 events
            events.append(
                {
                    "name": event["name"],
                    "date": event["dates"]["start"]["localDate"],
                    "time": (
                        event["dates"]["start"]["localTime"]
                        if "localTime" in event["dates"]["start"]
                        else None
                    ),
                    "venue": event["_embedded"]["venues"][0]["name"],
                    "url": event["url"],
                }
            )
    else:
        return "There isn't any events nearby."

    return events


def main():
    """
    You should test all the above functions here
    """
    pprint.pprint(get_nearby_events("Boston College"))
    # json for Babson College
    print(f"\njson for Babson College")
    pprint.pprint(get_json(url))

    # Coordinate for Boston College
    print(f"\nCoordinates for Babson College")
    print(get_lat_lng("Boston College"))

    # Nearest Station for Babson College
    print(f"\nNearest MBTA Station for Boston College")
    print(get_nearest_station(42.3358655, -71.1694295))

    # Nearest Station for Babson College
    print(f"\nNearest MBTA Station for Babson College")
    print(get_nearest_station(42.2981925, -71.263598))

    # Find nearest Station for Harvard University
    print(f"\nNearest MBTA Station for Harvard University")
    print(find_stop_near("Harvard University"))

    ### Optional Question ###

    # Get URL for Babson College from Mapbox
    print("\nURL for Babson College from Mapbox")
    print(get_url("Babson College"))

    # Get realtime arrival and departure time for nearest MBTA around Harvard University
    print(
        f"\nNearest MBTA Station for Harvard University with realtime arrival and departure time"
    )
    print(get_realtime("Harvard University"))

    # Get the city Harvard University is located in
    print("\nThe city Harvard University is located in is:")
    print(get_city("Harvard University"))

    # Get the top 5 events near Harvard University
    print("\nThe top 5 events near Harvard University are:")
    events = get_nearby_events("Harvard University")
    for items in events:
        print(items)


if __name__ == "__main__":
    main()
