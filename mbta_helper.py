import urllib.request
import json
from pprint import pprint

def get_data(place_name):
    """
    Returns a Python JSON object containing the response to a properly formatted URL for a JSON web API request.

    Returns coordinate data for a given location using MapQuest API.
    """

    MAPQUEST_API_KEY = '6qLDSiDDkB1qKjkwDBOWXepRG7AzYRnM'
    place_name = place_name.replace(' ', "%20")
    url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location={place_name}'
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    location_data = response_data['results'][0]['locations'][0]['latLng']

    return location_data['lat'], location_data['lng']


def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, w_accessibility) tuple for the nearest MBTA station to the given coordinates.
    """

    MBTA_API_KEY = '358cf651f4124ce28ee386d04a4c7b42'
    url = f'https://api-v3.mbta.com/stops?api_key={MBTA_API_KEY}&sort=distance&filter%5Blatitude%5D={latitude}&filter%5Blongitude%5D={longitude}'
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    data = response_data['data'][0]['attributes']['name']
    accessibility = response_data['data'][0]['attributes']['wheelchair_boarding']

    if accessibility == 1:
        wheelchair = 'This station offers accessibility accomodations.'
    elif accessibility == 0:
        wheelchair = 'No accessibility information available.'
    else:
        wheelchair = 'This station does not offer accessibility accomodations.'

    return data, wheelchair


def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.
    """

    lat, lng = get_data(place_name)
    station_name, w_accessibility = get_nearest_station(lat, lng) #w_accessibility = wheelchair accessibility
    return station_name, w_accessibility


def main():
    """
    You can test all the functions here
    """
    #get_data('wellesley')
    #get_nearest_station(get_data('wellesley'))


if __name__ == '__main__':
    main()
