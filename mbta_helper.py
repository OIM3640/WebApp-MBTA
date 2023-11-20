import json
import requests
import pprint
import urllib.request

MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MAPBOX_TOKEN = "pk.eyJ1IjoieGh1NiIsImEiOiJjbG94NTI5c2gwYXkzMnFwaXRvcW44NGtwIn0.0OUOBgmbdqbT3kxVMhdb5A"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"
MBTA_Prediction ="https://api-v3.mbta.com/predictions"
# query = "Babson College"
# query = query.replace(
#     " ", "%20"
# )  # In URL encoding, spaces are typically replaced with "%20"
# url = f"{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi"
# # # print(url) # Try this URL in your browser first

# with urllib.request.urlopen(url) as f:
#     response_text = f.read().decode("utf-8")
#     MAPBOX = json.loads(response_text)
#     pprint.pprint(response_text)


# Get JSON response from a URL
def get_json(url: str) -> dict:
    """
    Given a properly formatted URL for a JSON web API request, return a Python JSON object containing the response to that request.

    Both get_lat_long() and get_nearest_station() might need to use this function.
    """
    response = requests.get(url)
    # d = response.json()
    # return d

    if (
        response.status_code == 200
    ):  # check the status of the HTTP request; the standard successfull HTTP request is 200
        return response.json()
    else:
        response.raise_for_status()  # handle potnetial error if the request is not successful


# print (get_json(MBTA_BASE_URL))
# MBTA = get_json(MBTA_BASE_URL)

# Create Mapbox URL link
from urllib.parse import urlencode


def create_mapbox_url(address):
    """
    the function creates a URL fo a Mapbox API geocoding request
    """

    encoded_address = urllib.parse.quote(address)  # encode the address
    url = (
        f"{MAPBOX_BASE_URL}/{encoded_address}.json?access_token={MAPBOX_TOKEN}"
    )
    return url


# get latitude and longtitude from mapbox
def get_lat_long(place_name: str) -> tuple[str, str]:
    """
    Given a place name or address, return a (latitude, longitude) tuple with the coordinates of the given place.

    See https://docs.mapbox.com/api/search/geocoding/ for Mapbox Geocoding API URL formatting requirements.
    """
    # d = MAPBOX
    # l = len(d["features"])
    # for i in range(l - 1):
    #     if place_name in d["features"][i]["place_name"]:
    #         latitude = str(d["features"][i]["geometry"]["coordinates"][1])
    #         longitude = str(d["features"][i]["geometry"]["coordinates"][0])
    #         return (latitude, longitude)
    url = create_mapbox_url(place_name)
    response = get_json(url)
    # print(response)
    coordinates = response["features"][0]["geometry"]["coordinates"]
    latitude = coordinates[1]
    longtitude = coordinates[0]
    return latitude, longtitude


# print(get_lat_long("boston university"))

# for k in MAPBOX['features'][0].keys():
#     print (k)
# print (MAPBOX['features'][0])
# print (get_lat_long('Babson College'))


# Find the nearest MBTA station
def get_nearest_station(latitude: str, longitude: str) -> tuple[str, bool]:
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible) tuple for the nearest MBTA station to the given coordinates.

    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL formatting requirements for the 'GET /stops' API.
    """
    # initial attempt:
    # d = MBTA
    # latitude = float(latitude)
    # longitude = float(longitude)
    # l = len(d["data"])
    # for i in range(l - 1):
    #     if (
    #         d["data"][i]["attributes"]["latitude"] == latitude
    #         and d["data"][i]["attributes"]["longitude"] == longitude
    #     ):
    #         if d["data"][i]["attributes"]["wheelchair_boarding"] == 1:
    #             return (d["data"][i]["attributes"]["name"], True)
    #         else:
    #             return (d["data"][i]["attributes"]["name"], False)

    # improved attempt: Cite "Chatgpt"
    # sort URL
    sorted_url = f"{MBTA_BASE_URL}?filter[latitude]={latitude}&filter[longitude]={longitude}&sort=distance"
    response = get_json(sorted_url)
    # print(response)
    if len(response["data"]) > 0:
        nearest = response["data"][0]
        station_name = nearest["attributes"]["name"]
        wheelchair_accessible = nearest["attributes"]["wheelchair_boarding"] == 1
        stop_id = nearest['id']
        return station_name, wheelchair_accessible, stop_id
    else:
        raise ValueError("No nearby stations found")


# get_nearest_station(42.350692, -71.1063435)

# print (type(MBTA['data'][0]['attributes']['latitude']))
# print (type(MBTA['data'][0]['attributes']['wheelchair_boarding']))
# print (get_nearest_station('42.425322', '-71.189411'))


def find_stop_near(place_name: str) -> tuple[str, bool]:
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """
    lat, lon = get_lat_long(place_name)
    station, accessible, stop_id = get_nearest_station(lat, lon)
    return station, accessible, stop_id


# print(find_stop_near("boston university"))

# integrate real-time data from mbta API for arrival times and delays 
def get_real_time_info(stop_id):
    """
    the function fetches and return a dictionary of real-time arrivals and delay information for a MTBA station
    """
    url=f"{MBTA_Prediction}?filter[stop]={stop_id}"
    response = get_json(url)

    real_time_info=[]
    for item in response['data']:
        arrival_time = item['attributes'].get('arrival_time', None)
        status = item['attributes'].get('status', None)
        info = {
            'arrival_time': arrival_time,
            'status': status
        }
        real_time_info.append(info)
    if real_time_info:
            first_arrival = real_time_info[0]
            arrival_time = first_arrival['arrival_time']
            status = first_arrival['status']
            return arrival_time, status
    else:
        print("No real-time data available.")

           
            

def main():
    """
    You should test all the above functions here
    """
    place_name= 'boston university'
    station, accessible, stop_id = find_stop_near(place_name)
    print(station, accessible)
    real_time_info = get_real_time_info(stop_id)
    print(real_time_info)




if __name__ == "__main__":
    main()
