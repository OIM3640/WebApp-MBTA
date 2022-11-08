import urllib.request
import json
from pprint import pprint
import os

from dotenv import load_dotenv


import urllib.request
import json
from pprint import pprint

import url

# API key stored in dotenv

# load dotenv


def configure():
    load_dotenv()


# test code to get babson Location Info
# def get_babson_location_info():
#    configure()
#    url = f"http://mapquestapi.com/geocoding/v1/address?key={os.getenv('API_KEY')}&location=Babson%20College"
#    f = urllib.request.urlopen(url)
#    response_text = f.read().decode('utf-8')
#    response_data = json.loads(response_text)
#    return response_data

destination = url.get_url('Babson College')
# get location info from location name


def get_location_info(url):
    configure()
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    return response_data


# get latitude and longitude of location
def get_coordinates(response):
    result = response['results'][0]['locations'][0]['latLng']
    lat, lng = result['lat'], result['lng']
    return lat, lng


# test code for getting latitude and longitude of location
if __name__ == '__main__':
    print(destination)
    response_data = get_location_info(destination)
    print(response_data)
    result = get_coordinates(response_data)
    pprint(result)
