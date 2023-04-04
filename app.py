from mbta_helper import find_stop_near
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/nearest', methods=['POST'])
def nearest_station():
    # use place_name to calcuate the nearest MBTA station
    place_name = request.form['place_name']
    result = find_stop_near(place_name)

    # Retrun result to result.html template
    return render_template('result.html', place_name=place_name, result=result)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
