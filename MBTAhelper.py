from config import MAPQUEST_API_KEY, MBTA_API_KEY
import urllib.request
import json
from pprint import pprint
import urllib.parse

# place_name = "Brookline, MA"
#input("Please insert a location:")
#encoded_place = urllib.parse.quote(place_name)

mpq_key = MAPQUEST_API_KEY
mbta_key = MBTA_API_KEY

base_url = f"http://mapquestapi.com/geocoding/v1/address?"


def new_url(place_name):
    """
    creates new url based on user inputs
    """
    place_name = place_name.replace(" ", "")
    url = f"{base_url}key={mpq_key}&location={place_name}"
    return url


def get_json(url):
    """
    return a Python JSON object containing the response to that request.
    """

    f = urllib.request.urlopen(url)
    response_text = f.read().decode("utf-8")
    response_data = json.loads(response_text)
    return response_data


def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    """

    url = new_url(place_name)
    data = get_json(url)
    # pprint(data)

    lat_lng = data['results'][0]['locations'][0]['latLng']

    lat = lat_lng['lat']
    lng = lat_lng['lng']

    return lat, lng


def get_nearest_station(lat, lng):
    """
    Return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    """

    # for lat, lng in MAPQUEST_BASE_URL:

    url2 = f"https://api-v3.mbta.com/stops?api_key={mbta_key}&sort=distance&filter%5Blatitude%5D={lat}&filter%5Blongitude%5D={lng}"

    data2 = get_json(url2)
    # print(data2)
    data = data2['data']
    attributes1 = data[0]
    attributes2 = attributes1['attributes']
    station_name = attributes2['name']
    wheelchair_accessibile = attributes2['wheelchair_boarding']

    # MBTA API has a number system to judge how wheelchair accessible it is
    if wheelchair_accessibile == 1:
        x = "Some wheelchair boarding available"
        return station_name, x
    elif wheelchair_accessibile == 2:
        y = "wheelchair boarding not possible"
        return station_name, y
    else:
        z = 'No information available'
        return station_name, z
    # print(type(data))
    print(station_name)


def find_stop_near(place_name):
    """
    Return the nearest MBTA stop and whether it is wheelchair accessible.
    """
    lat, lng = get_lat_long(place_name)
    result = get_nearest_station(lat, lng)

    return result


def main():
    print(find_stop_near("Brookline, MA"))


if __name__ == "__main__":
    main()
