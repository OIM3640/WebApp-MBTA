from flask import Flask, redirect, render_template, request


app = Flask(__name__)

from mbta_helper import build_url, get_json, get_nearest_station, get_wheelchair_status

# @app.route('/')
# def hello():
#     return 'Hello User!'

# get_data_from_api
# asked chatGPT how to incorporate the mbta_helper module to be used in flask
def get_data_from_api(query):
    # query = 'Emmerson College'
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
    # print('MBTA data:', mbta_data)
    # print('MBTA Wheelchair data:', mbta_wheelchair_data)
    # print('Mapbox data:', mapbox_data)
    return {
        'mapbox_data': mapbox_data,
        'mbta_data': mbta_data,
        'mbta_wheelchair_data': mbta_wheelchair_data
    }


# asked on how to format code to be used in the flask webpage 
# asked how to pull data from the above function to be used in flask webpage
# also asked how to incorporate an error page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            query = request.form['query']
            if query:
                data = get_data_from_api(query)
                return render_template('new_index.html', data=data)
            else:
                error_message = "Please enter a valid Boston location"
                return render_template('error.html', error_message=error_message)
        except Exception as e:
            error_message = f'An error occurred: {str(e)}'
            return render_template('error.html', error_message=error_message)
    else:
        return render_template('new_index.html')
    #     user_query = request.form['query']
    #     data = get_data_from_api(user_query)
    #     return render_template('new_index.html', data=data)
    # return render_template('new_index.html', data={})

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
    app.run(debug=True)
    # main()
