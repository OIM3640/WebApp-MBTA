"""
A Website created using Flask and prompt user to enter a location where MBTA is reachable,
show the nearest station,
show whether the station is wheelchair accessible
"""

from flask import Flask, request, render_template
from mbta_helper import find_stop_near


app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def MBTA():
    if request.method == 'POST':
        try:
            place_name = request.form['place']
            result = find_stop_near(place_name)
            station_name = result[0]
            wheelchair = result[1]
            return render_template('station.html', place = place_name, station = station_name, wheelchair = wheelchair)
        except Exception:
            return render_template('error.html') 
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
