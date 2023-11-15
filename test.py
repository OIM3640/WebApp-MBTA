api_key = '4dab2290df5542b18165131a46cc26bb'
latitude = '147.4754275'
longitude = '-42.828105'

mbta_api_url = f"https://api-v3.mbta.com/stops?api_key={api_key}&sort=distance&filter%5Blatitude%5D={latitude}&filter%5Blongitude%5D={longitude}"
print(mbta_api_url)

import mbta_helper
print(mbta_helper.find_stop_near("Boston Common"))