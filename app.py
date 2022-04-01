"""
Simple "Hello, World" application using Flask
"""

from flask import Flask, render_template, request

from mbta_helper import find_stop_near


app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def show_nearest_mbta():
    if request.method == 'POST':
        street_name = request.form['Street']
        city_name = request.form['City']
        street = street_name.replace(' ', '%20')
        city = city_name.replace(' ', '%20')
        result = find_stop_near(f'{street},{city}')
        return render_template('mbta_station.html', station = result[0], accessibility = result[1])
    
    return render_template("index.html")
    

if __name__ == '__main__':
    app.run(debug=True)
