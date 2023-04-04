from mbta_helper import find_stop_near
from flask import Flask, render_template, request

app = Flask(__name__)


@app.get('/')
def home_page():
    return render_template('index.html')


@app.post('/nearest')
def nearest_station():
    # use place_name to calcuate the nearest MBTA station
    place_name = request.form.get('place_name')
    stop = find_stop_near(place_name)

    # Retrun result to result.html template
    return render_template('result.html', place_name=place_name, nearest_stop=stop)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
