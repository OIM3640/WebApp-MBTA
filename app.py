# app.py
from flask import Flask, render_template, request, redirect, url_for
from assignment3_mbtahelper import get_lat_long_with_weather, find_closest_stop

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        place_name = request.form['place_name']
        transportation_mode = request.form['transportation_mode']
        return redirect(url_for('nearest_mbta', place_name=place_name, mode=transportation_mode))
    return render_template('index.html')
#Route handling the main page; If the request method is POST, the form data is processed
#If the request method is GET, it renders the index.html template


@app.route('/nearest_mbta/<place_name>/<mode>')
def nearest_mbta(place_name, mode):
    location_info = get_lat_long_with_weather(place_name)
    latitude, longitude = location_info['latitude'], location_info['longitude']
    closest_stop = find_closest_stop(latitude, longitude, mode)
    #Route handling for the display of the closest MBTA stop & weather info

    if closest_stop:
        weather_info = location_info['weather']

        # Ensure temperature and condition are present in the weather_info dictionary
        temperature = weather_info.get('main', {}).get('temp')
        condition = weather_info.get('weather', [{}])[0].get('description')

        return render_template('mbta_station.html', place_name=place_name, closest_stop=closest_stop, temperature=temperature, condition=condition)
    else:
        return render_template('error.html', place_name=place_name)

if __name__ == '__main__':
    app.run(debug=True)