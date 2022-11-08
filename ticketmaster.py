from urllib import response
import urllib.request
import json
from datetime import date
# from config import TICKETMASTER_API_KEY
from mbta_helper import get_json, get_lat_long

TICKETMASTER_BASE_URL = 'https://app.ticketmaster.com/discovery/v2/events.json'
TICKETMASTER_API_KEY = 'uJLPZiofrWRvRkq5cUYyLQJwqjbtqCVI'

def find_events(latitude, longitude):
    """
    return
    """
    lat = str(latitude)
    long = str(longitude)
    latlong = lat +','+ long
    today = str(date.today())
    print(today)
    url = f'{TICKETMASTER_BASE_URL}?apikey={TICKETMASTER_API_KEY}&latlong={latlong}&radius=5&unit=miles&startDateTime={today}T00:00:00Z&sort=distance,asc'
    data = get_json(url)
    name = data['_embedded']['events'][0]['name']
    venue = data['_embedded']['events'][0]['_embedded']['venues'][0]['name']
    link = data['_embedded']['events'][0]['url']
    return name, venue, link

def get_event_near(place):
    if ',' not in place:
        return ((None, None), True)

    lat, lng = get_lat_long(place)

    return (find_events(lat, lng), False)

def main():
    print(get_event_near("Back Bay, Boston"))

if __name__=='__main__':
    main()