from flask import Flask, request, render_template
from app2 import get_coordinates
from app2 import MAPBOX_TOKEN
from app2 import find_closest_mbta_stop
from app2 import MBTA_API_KEY
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/find', methods=['POST'])     # when user send information tp the server, 'find()function will handle it.
def find():
    address = request.form['address']
    try:
      coordinates = get_coordinates(address, MAPBOX_TOKEN) 
      lat = coordinates[0]
      lon = coordinates[1]
      
      result = find_closest_mbta_stop(lat, lon, MBTA_API_KEY)
      
      
if __name__ == "__main__":
    app.run(debug=True)
