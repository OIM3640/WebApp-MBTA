"""
Simple "Hello, World" application using Flask
"""
import mbta_helper 
from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/nearest', methods = ['GET', 'POST'])
def get_result(): 
    if request.method == "POST":
        place_name = request.form['place']
        if mbta_helper.find_stop_near(place_name) == None: 
            return render_template('error.html', place = place_name)
        else: 
            near_stop, wheelchair_accessible, weather, temp, air_quality = mbta_helper.find_stop_near(place_name)
        
            return render_template("result.html", place=place_name, nearest=near_stop, accessibility = wheelchair_accessible, weather = weather, temp = temp, air = air_quality) 
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
