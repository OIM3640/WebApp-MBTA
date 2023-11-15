from flask import Flask, render_template, request
from mbta_helper import find_stop_near, get_weather

app = Flask(__name__)


@app.get('/')
def mbta_get():
    return render_template("index.html") #Simply showcase landing page


@app.post('/nearest_mbta')
def result():
    # Get the location from the form submission
    place_name = request.form['currentLocation']

    # Call the functions to get the information
    nearest_station_info =find_stop_near(place_name)
    weather_info = get_weather(place_name)
    if find_stop_near(place_name)==None:
        return render_template('index.html', error=True) #error sends back to landing page
    else:
    # Render the result page with the obtained information
        return render_template('nearest.html', nearest_station_name=nearest_station_info[0], #Tuple accepts only integers
                            is_accessible=nearest_station_info[1],
                            weather_info=weather_info)

if __name__ == '__main__':
    app.run(debug=True)


