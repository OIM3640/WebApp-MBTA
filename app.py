from flask import Flask, render_template, request
import mbta_helper2

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def find_station():
    address = request.form.get('address')
    station_info = mbta_helper2.find_stop_near(address)

    if station_info:
        station_name, wheelchair_accessible = station_info
        return render_template('results.html', station_name=station_name, wheelchair_accessible=wheelchair_accessible)
    else:
        return render_template('results.html', message='No results found. Please try again.')
    
    
if __name__ == '__main__':
    app.run(debug=True)
