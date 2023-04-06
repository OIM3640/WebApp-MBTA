from flask import Flask, redirect, request, render_template
from mbta_helper import find_stop_near, get_lat_long
from weather import get_weather_report 


app = Flask(__name__)


@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', method = ['POST', 'GET'])
def submit():
    if request.method == "POST":
        input_place = request.form['location']
        message, status = find_stop_near(input_place)
        if status == 400:
            condition = "not known"
            temp = "not known"
        else:
            long, lat = get_lat_long(input_place) 
            condition, temp = get_weather_report(latitude=lat, longitude=long)
        return render_template('result.html', input_place = input_place, message = message, temperature = temp, weather_condition = condition)

if __name__ == '__main__':
    app.run(debug=True)
