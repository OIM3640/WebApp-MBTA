from flask import Flask, request, render_template
from mbta_helper import find_stop_near, get_realtime_arrival
import logging

# Configure logging
logging.basicConfig(filename='app.log', level=logging.DEBUG, 
                    format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    # Render an HTML form for input (index.html)
    return render_template('index.html')

@app.route('/nearest_mbta', methods=['POST'])
def nearest_mbta():
    try:
        place_name = request.form['place_name']
        mode_of_travel = request.form.get('mode_of_travel', 'metro')  # Default mode of travel
        station_name, wheelchair_accessible, station_id = find_stop_near(place_name, mode_of_travel)
        arrival_times = get_realtime_arrival(station_id) if station_id else None

        if station_name:
            # Render an HTML page with MBTA info (mbta_station.html)
            return render_template(
                'mbta_station.html',
                station_name=station_name,
                wheelchair_accessible=wheelchair_accessible,
                arrival_times=arrival_times
            )
        else:
            # Render an error page (error.html)
            logging.error(f'No nearby station found for {place_name} with mode {mode_of_travel}')
            return render_template('error.html', error_message='No nearby station found.')
    except Exception as e:
        # Log the exception and render an error page
        logging.exception("An unexpected error occurred while processing the nearest_mbta endpoint.")
        return render_template('error.html', error_message=str(e))

if __name__ == '__main__':
    app.run(debug=True)
