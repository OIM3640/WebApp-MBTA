# import json
# import urllib.request
# import requests
# from mbta_helper import build_url, get_json, get_nearest_station

# with open ('config.json', 'r') as config_file:
#     config = json.load(config_file)
# # Your API KEYS (you need to use your own keys - very long random characters)

# # from config import MAPBOX_TOKEN, MBTA_API_KEY
# MAPBOX_TOKEN = config["MAPBOX_TOKEN"]
# MBTA_API_KEY = config["MBTA_API_KEY"]

# # Useful URLs (you need to add the appropriate parameters for your requests)
# MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
# MBTA_BASE_URL = "https://api-v3.mbta.com/stops"


# # def fetch_data_from_apis():
# #     query = 'Emmerson College'
# #     url = build_url(query)
# #     mapbox_data = get_json(url)
# #     print('Mapbox data:', mapbox_data)
# #     latitude, longitude = get_json(url)
# #     print('Latitude:', latitude)
# #     print('Longitude:', longitude)
# #     mbta_data = get_nearest_station(latitude, longitude)
# #     print('MBTA data:', mbta_data)
# #     return {
# #         'mapbox_data': mapbox_data,
# #         'mbta_data': mbta_data
# #     }


# # def test():
# #     query = 'Emmerson College'
# #     url = build_url(query)
# #     latitude, longitude = get_json(url)
# #     get_nearest_station(latitude,longitude)

# def main():
#     query = 'Emerson College'
#     url = build_url(query)
#     latitude, longitude = get_json(url)
#     get_nearest_station(latitude, longitude)

# if __name__ == '__main__':
#     main()


from mbta_helper import build_url, get_json, get_nearest_station, get_wheelchair_status

# @app.route('/')
# def hello():
#     return 'Hello User!'

# get_data_from_api

def main():
    query = 'Boston College'
    url = build_url(query)
    # mapbox_data = get_json(url)
    # print('Mapbox data:', mapbox_data)
    latitude, longitude = get_json(url)
    # print('Latitude:', latitude)
    # print('Longitude:', longitude)
    # mbta_data = get_nearest_station(latitude, longitude)
    # get_nearest_station(latitude, longitude)
    # get_wheelchair_status(latitude, longitude)
    mapbox_data = get_json(url)
    mbta_data = get_nearest_station(latitude, longitude)
    mbta_wheelchair_data = get_wheelchair_status(latitude, longitude)
    print('MBTA data:', mbta_data)
    print('MBTA Wheelchair data:', mbta_wheelchair_data)
    print('Mapbox data:', mapbox_data)
    return {
        'mapbox_data': mapbox_data,
        'mbta_data': mbta_data,
        'mbta_wheelchair_data': mbta_wheelchair_data
    }


# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         user_query = request.form['query']
#         data = get_data_from_api(user_query)
#         return render_template('new_index.html', data=data)
#     return render_template('new_index.html', data={})

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     data = None
#     if request.method == 'POST':
#         location_name = request.form.get('location')
#         if location_name:
#             data = get_data_from_api(location_name)
#     return render_template('new_index.html', mapbox_data=data, mbta_data=data, mbta_wheelchair_data=data)


# @app.get('/Location/')
# def location_get():
#     return 

# @app.post('/NearestLocation')
# def nearest_station_get():
#     location_name = request.form.get("Location")




if __name__ == '__main__':
    # app.run(debug=True)
    main()