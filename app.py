from flask import Flask, request, render_template
from mbta_helper import get_lat_lng, find_stop_near, MAPBOX_TOKEN, MBTA_API_KEY

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route('/find', methods=['POST'])    
def find():
    address = request.form['address']
    try:
        coordinates = get_lat_lng(address, MAPBOX_TOKEN) 
        lat = coordinates[0]
        lon = coordinates[1]
      
        stop_name, wheelchair = find_stop_near(address, MAPBOX_TOKEN,MBTA_API_KEY)
      
        if wheelchair == [1]:
            accessibility = "Yes"
        else:
            accessibility = "No"
        return render_template('result.html', stop_name=stop_name, accessible=accessibility)
    except: #error
        
      
    
      
if __name__ == "__main__":
    app.run(debug=True)
