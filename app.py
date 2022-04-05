from flask import Flask, render_template, request
from mbta_helper import find_stop_near


app = Flask(__name__)


@app.route('/index/', methods = ['GET', 'POST'])
def show_station():
    if request.method == 'POST':
        place_name = request.form['place']

        station = find_stop_near(place_name)

        return render_template('station-result.html', place = place_name, station = station)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
