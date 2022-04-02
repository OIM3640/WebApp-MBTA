"""
Flask program which uses find_stop_near function from mbta_helper.py
This creates the web page which allows users to input a street name and city and find the nearest MBTA station and whether it is wheelchair accessibile or not
"""

from flask import Flask, render_template, request

from mbta_helper import find_stop_near

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def show_nearest_mbta():
    if request.method == 'POST':
        street_name = request.form['Street']
        city_name = request.form['City']
        street_for_result = street_name.replace(' ', '%20') # replace for url purposes
        city_for_result = city_name.replace(' ', '%20')
        result = find_stop_near(f'{street_for_result},{city_for_result}')
        return render_template('mbta_station.html', street=street_name, city=city_name, station=result[0], accessibility=result[1], )

    return render_template("mbta_form.html")

# handling errors
@app.errorhandler(Exception)
def basic_error(e):
    return render_template('404.html')


if __name__ == '__main__':
    app.run(debug=True)
