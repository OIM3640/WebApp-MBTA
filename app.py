from flask import Flask, render_template, request, redirect, url_for
from mbta_helper import find_stop_near, get_lat_long
from datetime import datetime

app = Flask(__name__)

@app.template_filter('datetimeformat')
def datetimeformat(value, format='%H:%M:%S (%m-%d-%Y)'):
    return datetime.fromisoformat(value).strftime(format)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        place_name = request.form['place_name'].strip()
        if place_name:
            try:
                station_info = find_stop_near(place_name)
                return render_template('mbta_station.html', station_info=station_info)
            except Exception as e:
                error_message = str(e)
                return render_template('error.html', error_message=error_message)
        else:
            return render_template('index.html', error_message='Please enter a place name.')
        
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

# http://127.0.0.1:5000