"""
Web application that shows the closest MBTA and whether 
or not it is WC accessible using user's inputted location and Flask.
"""

from flask import Flask, render_template, request
from mbta_helper import find_stop_near


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def show_near_station():
    if request.method == 'POST':
        location_name = str(request.form['location'])
        station_name = find_stop_near(location_name)
        return render_template('mbta_result.html', location = location_name, station = station_name)
    return render_template("mbta_form.html")




if __name__ == '__main__':
    app.run(debug=True)