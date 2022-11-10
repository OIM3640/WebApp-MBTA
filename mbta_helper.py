# Your API KEYS (you need to use your own keys - very long random characters)
from config import MAPQUEST_API_KEY, MBTA_API_KEY
import urllib.request
import json
import pprint

# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = "http://www.mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"


# A little bit of scaffolding if you want to use it


def get_json(url,location):
    """
    Given a properly formatted URL for a JSON web API request and a location name, return
    a Python JSON object containing the response to that request.

    Both get_lat_long() and get_nearest_station() might need to use this function.
    """
    #crate a proper url using the api key and location to obtian JSON object
    final = url + "?key="+ MAPQUEST_API_KEY + "&location=" + location
    #open the url and read the JSON file 
    with urllib.request.urlopen(final) as f:
        response_text = f.read().decode('utf-8')
        #create variable 'data' to hold the json dicitonary of the data
        data = json.loads(response_text)
        #return data in a useable format
        return data







def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developer.mapquest.com/documentation/geocoding-api/address/get/
    for Mapquest Geocoding API URL formatting requirements.
    """
    #change all spaces in the location name to %20 to make the URL useable
    place_name = place_name.replace(" ","%20")
    #obtain the useuable data from the get_json funciton
    data = get_json(MAPQUEST_BASE_URL,place_name)
    #reutrn the Latitude and Longitude in a dictionary formal from the data obtained, from the first result in the API
    return(data['results'][0]['locations'][0]['latLng'])

    


def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    #create a proper url using my api key and the latitude and longitude provided
    #this url returns MBTA stops sorted by distance (closest to farthest) from the provided latitude and longtitude
    url = "https://api-v3.mbta.com/stops?api_key=" + MBTA_API_KEY + "&sort=distance&filter%5Blatitude%5D=" + str(latitude) + "&filter%5Blongitude%5D=" + str(longitude)

    #decode the data from the url to make it into a useable form
    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode('utf-8')
        #load data into variable data
        data = json.loads(response_text)
        #use a if statement to see if wheelchair boarding is accessible or not
        if data['data'][0]['attributes']['wheelchair_boarding']==0:
            #return the name of the MBTA stop and if it is weelchair accessible or not
            return (data['data'][0]['attributes']['name']), "Not Wheelchair Accessible"
        else:
            return (data['data'][0]['attributes']['name']),"Wheelchair Accessible"


def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """
    #find the latitude and longitude form the get_lat_long function
    firststep = get_lat_long(place_name)
    #serperate the latitude and longitude into distinct variables
    latitude = firststep['lat']
    longitude = firststep['lng']

    #plug the latitude and longitude into the get_nearest_station function to find the nearest MBTA stop
    secondstep = get_nearest_station(latitude,longitude)
    #return the nearest MBTA stop and if its wheelchair accessbile
    return secondstep


def main():
    """
    You can test all the functions here
    The more specific location you enter, the more accurate the result
    """
    #ask the user to input the location
    location = input("Choose a Location: ")

    #test of each function
    #get_json(MAPQUEST_BASE_URL,location)
    #print(get_lat_long(location))
    #print(get_nearest_station(42.35311, -71.06973))
    #print("The nearset stop is "+ str(find_stop_near(location)))


if __name__ == '__main__':
    main()
