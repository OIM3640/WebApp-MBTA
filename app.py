from flask import Flask, render_template, request, flash, url_for, redirect
from mbta_helper import find_stop_near

app = Flask(__name__)
app.secret_key = 'some_secret_key'

# @app.route("/")
@app.route('/')
def get_mbta_station():
    return render_template("index.html")

@app.route('/mbta', methods = ['POST'])
def find():
    try:
        place_name = request.form['place_name']
        station_name, is_accessible = find_stop_near(place_name)
        return render_template('place.html', station_name=station_name, is_accessible=is_accessible)
    except IndexError:
        flash("No MBTA station nearby your location. Please try a different one.")
        return redirect(url_for('index'))
    except Exception as e:
        flash(f"An error has occurred: {str(e)}")
        return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html') 

if __name__ == '__main__':
    app.run(debug=True)
