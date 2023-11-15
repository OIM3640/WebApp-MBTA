from flask import Flask, render_template, request, url_for
from mbta_helper import find_stop_near, get_weather


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/nearest_mbta', methods=['POST']) # route for finding the nearest MBTA stop based on user input
def nearest_mbta():
    place_name = request.form.get('Location') # get location input from the form
    if not place_name: # check if location is provided, if not display error page
        return render_template('error.html', error_message="Please enter a location.", url_for_home=url_for('index'))
    try:
        result, accessible = find_stop_near(place_name) # try to find nearest MBTA stop
        weather_info = get_weather() # try to get weather information
        return render_template("mbta_station.html", result=result, accessible=accessible, weather_info=weather_info) # shows results on template
    except Exception as e: # display error message if exception occurs
        print(e)
        return render_template("error.html", error_message="An error occured.", url_for_home=url_for('index'))

@app.route('/error') # route for displaying generic error page
def error():
    return render_template("error.html", error_message="An error occured.", url_for_home=url_for('index'))
    

if __name__ == '__main__':
    app.run(debug=True)
