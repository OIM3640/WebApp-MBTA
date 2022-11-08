import os
from dotenv import load_dotenv
import urllib
from urllib.parse import urlencode, quote
import json

"""
What you need to do: write a function that takes an address or place name as input and returns a 
properly encoded URL to make a MapQuest geocode request.
"""


# configure APIkey


def configure():
    load_dotenv()


def get_url(location):
    configure()
    domain = "http://mapquestapi.com/geocoding/v1/address"
    API_key = os.getenv('API_KEY')
    location = quote(location)
    url = f'{domain}?key={API_key}&location={location}'
    return url


if __name__ == '__main__':
    result = get_url('Babson College')
    print(result)
