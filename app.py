from flask import Flask, request, render_template
from mbta_helper import find_stop_near, get_weather


app = Flask(__name__)

# this page will be the main landing page with a form 
@app.route('/')
def hello():
    return render_template("index.html") 

#this page will show the results of the user's search input 
@app.route('/nearest_mbta', methods = ['POST'])
def get_nearest_mbta():
    user_location = request.form['location']
    nearest_mbta = find_stop_near(user_location)
    weather = get_weather(user_location)
    output = f"{nearest_mbta} Weather: {str(weather)} °F"
    return output

if __name__ == '__main__':
    app.run(debug=True)
