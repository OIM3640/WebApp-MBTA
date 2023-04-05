from mbta_helper import find_stop_near, get_nearest_station
from flask import Flask, render_template, request

app = Flask(__name__)


@app.get('/')
def home_page():
    return render_template('index.html')


@app.post('/nearest')
def nearest_station():
    # use place_name to calcuate the nearest MBTA station
    place_name = request.form.get('place_name')
    stop, wheelchair = find_stop_near(place_name)

    # Retrun result to result.html template
    return render_template('result.html', place_name=place_name, nearest_stop=stop, wheelchair_accessible=wheelchair)


@app.route('/map/')
def show_map():
    lat, lng = get_nearest_station()
    html_map = f'<iframe src="https://maps.google.com/maps?q={lat},{lng}&amp;t=&amp;z=15&amp;ie=UTF8&amp;iwloc=&amp;output=embed"></iframe>'
    return render_template('result.html', html_map=html_map)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
