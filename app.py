from flask import Flask, render_template, request
from mbta_helper import find_stop_near


app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def show_station():

    try:
        if request.method == 'POST':
            place_name = request.form['place']

            result = find_stop_near(place_name)
            station = result[0]
            WheelchairTF = result[1]


            return render_template('station-result.html', place = place_name, station = station, Wheelchair = WheelchairTF)
        else:
            return render_template('index.html')
    except Exception:
        return render_template('error.html')


if __name__ == '__main__':
    app.run(debug=True)
