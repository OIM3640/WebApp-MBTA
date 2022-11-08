from mapquest import get_coordinates, get_location_info

from mbta import get_clostest_stop

from url import get_url


location = input('Type a location: ')
print(f'your location is {location}')
url = get_url(location)
print(f'your url is {url}')
location_info = get_location_info(url)
print(f'your location_info is {location_info}')
coordinates = get_coordinates(location_info)
print(f'your coordinates is {coordinates}')
(lat, lng) = coordinates
clostest_stop = get_clostest_stop(lat, lng)
print(f'your closest_stop is {clostest_stop}')
