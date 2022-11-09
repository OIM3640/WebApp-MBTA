from config import MAPQUEST_API_KEY, MBTA_API_KEY

mpq_key = MAPQUEST_API_KEY 

mbta_key = MBTA_API_KEY



# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = "http://mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"




def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    Both get_lat_long() and get_nearest_station() might need to use this function.
    """
    import urllib.request
    import json
    from pprint import pprint


    f = urllib.request.urlopen(url)
    response_text = f.read().decode("utf-8")
    response_data = json.loads(response_text)
    return response_data 
    


def get_lat_long(place_name): 

    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developer.mapquest.com/documentation/geocoding-api/address/get/
    for Mapquest Geocoding API URL formatting requirements.
    """
    import urllib.parse
    encoded_place = urllib.parse.quote(place_name)

    
    url = f"http://mapquestapi.com/geocoding/v1/address?key={mpq_key}&location={encoded_place}"

    data = get_json(url)

    lat_lng = data['results'][0]['locations'][0]['latLng']

    lat = lat_lng['lat']
    lng = lat_lng['lng']


    return lat, lng 

    

get_lat_long('Brookline, MA')


def get_nearest_station(lat, lng):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    get_lat_long = lat, lng

    for lat, lng in MAPQUEST_BASE_URL:
        MBTA_API_KEY = '76b1bc5471f9443d864ad4ff9ba714e7' 
        url = f"https://api-v3.mbta.com/stops?{MBTA_API_KEY}sort=distance&filter%5Blatitude%5D={lat}&filter%5Blongitude%5D={lng}"
        
        data = get_json(url)

        station_name = data['stop_name']
        wheelchair_accessibile = data['wheelchair_boarding']

    return station_name, wheelchair_accessibile

get_nearest_station()


def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.
    This function might use all the functions above.
    """
    pass


def main():
    """
    You can test all the functions here
    """
    pass


if __name__ == "__main__":
    main()