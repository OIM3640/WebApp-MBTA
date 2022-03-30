import urllib.request
import json
from pprint import pprint

def get_lat(city):
    """"""
    city=city.replace(' ',"%20")
    MAPQUEST_API_KEY = 'HHQCVcQVkeaG9GCvrd7rEDyGNtBt5CsS'
    url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location={city}'
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    return response_data['results'][0]['locations'][0]['displayLatLng']['lat']

def get_lng(city):
    """"""
    city=city.replace(' ',"%20")
    MAPQUEST_API_KEY = 'HHQCVcQVkeaG9GCvrd7rEDyGNtBt5CsS'
    url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location={city}'
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    return response_data['results'][0]['locations'][0]['displayLatLng']['lng']

def close_mbta(lat,lng):
    """"""
    MBTA_API_KEY='b1af33cc51a848478b7bdf152795cc9e'
    url=f'https://api-v3.mbta.com/stops?api_key={MBTA_API_KEY}&sort=distance&filter%5Blatitude%5D={lat}&filter%5Blongitude%5D={lng}'
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    pprint(response_data)
    if response_data['data'][0]['attributes']['wheelchair_boarding']==1:
        wheel_chair='Some vehicles at this stop can be boarded by a rider in a wheelchair.'
    elif response_data['data'][0]['attributes']['wheelchair_boarding']==0:
        wheel_chair='No accessibility information for the stop'
    else:
        wheel_chair='Wheelchair boarding is not possible at this stop'
    return response_data['data'][0]['attributes']['address'], wheel_chair

def main():
    city=input('Input your location')
    close_mbta(get_lat(city), get_lng(city))
    