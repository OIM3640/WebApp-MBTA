import requests
import json
import webcolors
from config import MBTA_KEY, yelp_api

# Useful URLs (you need to add the appropriate parameters for your requests)
MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"


def get_lat_long(place_name: str) -> tuple[str, str]:
    """
    Given a place name or address, return a (latitude, longitude) tuple with the coordinates of the given place.

    See https://docs.mapbox.com/api/search/geocoding/ for Mapbox Geocoding API URL formatting requirements.
    """
    url = f"https://api.mapbox.com/geocoding/v5/mapbox.places/{place_name}.json"
    key = {
        "access_token": "pk.eyJ1Ijoic2xpOSIsImEiOiJjbGZ2cWlueDYwMDg5M2RvZGp4bGt1dDZ4In0.OhZHNyEJGKdMYpuhOkeMNQ"
    }
    response = requests.get(url, params=key)
    response_json = response.json()
    features = response_json.get("features")
    if features and len(features) > 0:
        first_feature = features[0]
        geometry = first_feature.get("geometry")
        if geometry:
            latitude = geometry.get("coordinates")[1]
            longitude = geometry.get("coordinates")[0]
            return latitude, longitude
    return None, None


def get_nearest_station(latitude: str, longitude: str) -> tuple[str, bool, str]:
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible, line_id) tuple for the nearest MBTA station to the given coordinates.

    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL formatting requirements for the 'GET /stops' API.
    """
    url = f"https://api-v3.mbta.com/stops?sort=distance&filter[latitude]={latitude}&filter[longitude]={longitude}&filter[radius]=0.1"

    # Make the API call and retrieve the JSON response
    response = requests.get(url)
    data = response.json()

    # print(f"This is data: {data}")

    if not data.get("data"):
        return (
            "not found",
            None,
            None
        )

    try:
        name = data["data"][0]["attributes"]["name"]
        print(f"This is name: {name}")

        wheelchair = data["data"][0]["attributes"]["wheelchair_boarding"]
        if wheelchair == 2:
            wheelchair_boarding = False
        elif wheelchair == 1:
            wheelchair_boarding = True
        print(f"This is wheelchair: {wheelchair_boarding}")

        return name, wheelchair_boarding

    except:
        if not data.get("data"):
            return "Location unavailable, try again.", False, None
        return "An error occurred. Please try again later.", False, None



def find_stop_near(place_name: str) -> tuple[str, bool]:
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """
    latitude = get_lat_long(place_name)[0]
    longitude = get_lat_long(place_name)[1]
    return get_nearest_station(latitude, longitude)

# def get_stop_id(stop_name):
#     encoded_stop_name = requests.utils.quote(stop_name)

#     # Define the API endpoint URL
#     url = f'https://api-v3.mbta.com/stops?filter[route_type]=0&filter[stop]=true&filter[name]={encoded_stop_name}'

#     response = requests.get(url)

#     if response.status_code == 200:
#         stop_id = response.json()['data'][0]['id']

#         return stop_id
#     else:
#         response.raise_for_status()


import requests

def get_nearby_restaurants(location, radius=1500):
    """
    Returns a list of nearby restaurants for a given location using the Yelp Fusion API.
    """
    url = 'https://api.yelp.com/v3/businesses/search'
    headers = {
        'Authorization': 'Bearer ' + yelp_api
    }
    params = {
        'term': 'restaurants',
        'location': location,
        'radius': radius,
        'categories': 'restaurants'
    }
    response = requests.get(url, headers=headers, params=params)
    businesses = response.json()['businesses']
    restaurants = []
    for business in businesses:
        restaurant = {
            'name': business['name'],
            'address': ', '.join(business['location']['display_address']),
            'latitude': business['coordinates']['latitude'],
            'longitude': business['coordinates']['longitude'],
            'rating': business.get('rating', None)
        }
        restaurants.append(restaurant)
    return restaurants



def main():
    """
    You can test all the functions here
    """
    commons = "Boston Commons"
    commons_coords = get_lat_long(commons)
    # print(commons_coords)
    lat = commons_coords[0]
    long = commons_coords[1]
    print(get_nearest_station(lat, long))

    station_near_commons=find_stop_near(commons)
    print(station_near_commons)
    print(get_nearby_restaurants(commons))

    # stop_id=get_stop_id(station_near_commons[0])
    # print(stop_id)


if __name__ == "__main__":
    main()
