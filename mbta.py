"""
To accomplish this, we will use the MBTA-realtime API. Check out the details for GET /stops in the documentation. 
Hints: Prepare valid latitude and longitude numbers of any Boston address for testing. 
Under GET /stops, click "Try it out" button. Enter/select the following parameters:

sort: select "distance" (not "-distance") for ascending order.
filter[latitude]: enter the testing latitude value.
filter[longitude]: enter the testing longitude value.

Then click "Execute" button. You should be able to find a generated URL in Curl. 
Hints: Observe the generate URL and learn how to build that URL using variables. 
Remember to add api_key={YOUR_MBTA_API_KEY}& right after ? in the URL.
Note: You need to request an API key from MBTA V3 API Portal.


What you need to do: create a function that takes a latitude and longitude 
and returns the name of the closest MBTA stop and whether it is wheelchair accessible.

Note: Sadly there are no MBTA stops close enough to Babson College - you have to get out into the city!
"""

import urllib.request
from urllib.request import Request
from urllib.parse import urlparse

from dotenv import load_dotenv
import os
import json
import requests
# get mbta key


def configure_dotenv():
    load_dotenv()


configure_dotenv()
MBTA_KEY = os.getenv('API_KEY_MBTA')


# example url
# https://api-v3.mbta.com/stops?sort=distance&filter%5Blatitude%5D=42.29822&filter%5Blongitude%5D=-71.26543

# https://api-v3.mbta.com/stops?api_key=e096ee50efcf47d98254dae1ae24ac9a&sort=distance&filter%5Blatitude%5D=40.29822&filter%5Blongitude%5D=72

# function to get mbta stops
def get_clostest_stop(lat, lng):
    domain = 'https://api-v3.mbta.com/stops'
    key = f'api_key={MBTA_KEY}'
    sort = 'sort=distance'
    filters = f'filter%5Blatitude%5D={lat}&filter%5Blongitude%5D={lng}'
    url = domain + '?' + key + '&' + sort + '&' + filters
    print(url)
    #header = {'accept': 'application/vnd.api+json'}
    #request = Request(url=url, headers=header)
    f = urllib.request.urlopen(url)
    response_data = f.read().decode('utf-8')
    response_text = json.loads(response_data)
    return response_text


if __name__ == '__main__':
    result = get_clostest_stop(0, 0)
    print(result)
