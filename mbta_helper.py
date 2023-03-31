


import urllib.request
import json
from pprint import pprint

MAPBOX_TOKEN = "pk.eyJ1IjoicnNwZWlzczEiLCJhIjoiY2xmdnExMHF1MDR4ZDNlcnlodTVycmIxZCJ9.jNxSH_Iy8OkzjmJ0_9JuIQ"
MBTA_API_KEY = "bb95e42e949546e79148fee122c28d83"
MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"


# query = 'Babson%20College'
# url=f'{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi'
# # print(url) # Try this URL in your browser first

# with urllib.request.urlopen(url) as f:
#     response_text = f.read().decode('utf-8')
#     response_data = json.loads(response_text)
#     # pprint(response_data)
#     # print(response_data['features'][0]['properties']['address'])
#     print(response_data['features'][1]['geometry']['coordinates'])

# test = url




def get_json(url: str) -> dict:
    """
    Given a properly formatted URL for a JSON web API request, return a Python JSON object containing the response to that request.

    Both get_lat_long() and get_nearest_station() might need to use this function.
    """
    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode('utf-8')
        response_data = json.loads(response_text)
    return response_data


# pprint(get_json(test))


def remove_spaces(place_name:str):
    """formats spaces for api"""

    single = ""

    for character in place_name:

        if character.isspace() == True:
            single = single + "%20"
        else:
            single = single + character
    return single

def get_url_mapbox(place_name: str):
    """gets url response collection using mapbox base api"""

    place_name = remove_spaces(place_name)
    
    url=f'{MAPBOX_BASE_URL}/{place_name}.json?access_token={MAPBOX_TOKEN}&types=poi'

    return url

# print(get_url_mapbox("babson college"))    

def get_lat_long(place_name: str) -> tuple[str, str]:
    """
    Given a place name or address, return a (latitude, longitude) tuple with the coordinates of the given place.
    """
    url = get_url_mapbox(place_name)

    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode('utf-8')
        response_data = json.loads(response_text)
        # pprint(response_data)
        # print(response_data['features'][0]['properties']['address'])
        coordinates_ = response_data['features'][0]['geometry']['coordinates']

        coordinates = [str(coordinates_[1]),str(coordinates_[0])]
        coordinates = tuple(coordinates)

        return coordinates

# print(get_lat_long("babson college"))

    
def get_url_mbta(latitude: str, longitude: str):
    """gets url response collection using mbta api"""
    
    url=f"{MBTA_BASE_URL}?api_key={MBTA_API_KEY}&sort=distance&filter%5Blatitude%5D={latitude}&filter%5Blongitude%5D={longitude}"

    return url

def get_nearest_station(latitude: str, longitude: str) -> tuple[str, bool]:
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible) tuple for the nearest MBTA station to the given coordinates.

    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL formatting requirements for the 'GET /stops' API.
    """
    url = get_url_mbta(latitude,longitude)

    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode('utf-8')
        response_data = json.loads(response_text)
        # pprint(response_data["data"])
        # print(response_data['features'][0]['properties']['address'])
        station = response_data["data"][0]["attributes"]
        name = station["name"]
        accessible = station["wheelchair_boarding"]
        # pprint(accessible)
        # 0: no info, 1: yes, 2: no
        # ________________________________________________________________also closest transport________________________bool
        info = tuple([name,accessible])

        return info
    


# print(get_nearest_station("42.361145","-71.057083"))





def find_stop_near(place_name: str) -> tuple[str, bool]:
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """ 
    coordinates = get_lat_long(place_name)
    station_info = get_nearest_station(coordinates[0],coordinates[1])

    return station_info

# print(find_stop_near("north quincy"))


def main():
    """
    You can test all the functions here
    """
    
    place_name = "ashmont"
    print(get_lat_long(place_name))
    print(find_stop_near(place_name))


if __name__ == '__main__':
    main()
