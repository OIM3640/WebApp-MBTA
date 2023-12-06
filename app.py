from flask import Flask, render_template, request
from mbta_helper import find_stop_near
from weather import get_temp

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def placename():
    '''
    1. at http://127.0.0.1:5000/, the user will be greeted by a page that says hello, and includes an input form that requests a place name.
    2. Upon clicking the 'Submit' button, the data from the form will be sent via a POST request to the Flask backend at the route.
    3. Then your app will render a mbta_station page for the user - presenting nearest MBTA stop and whether it is wheelchair accessible.
    4. If something is wrong, the app will render a simple error page
    '''
    if request.method == 'POST':
        place_name = request.form.get("placename")
        try:
            station_name, wheelchair_accessible = find_stop_near(place_name)
            temperature = get_temp(place_name)
            return render_template("nearest_station.html", place_name=place_name, station_name=station_name, wheelchair_accessible=wheelchair_accessible, temperature=temperature)
            # return f"The Nearest Station in {place_name} is: {station_name}<br>Wheelchair Accessible:{wheelchair_accessible}<br>Temperature:{temperature} Kelvin"
        except Exception as e:
            # print(f"An error occurred: {e}")
            return error_page()
        
    return render_template("index.html")

def error_page():
    '''If something is wrong, the app will render a simple error page, which will include some indication that the search did not work, along with a button or link that redirects the user back to the home page.
    '''
    return render_template("error.html")

# @app.get('/') 
# def placename_get():
#     return render_template("index.html")

# @app.post('/')
# def placename_post():
#     place_name = request.form.get("placename")
#     station_name, wheelchair_accessible = find_stop_near(place_name)
#     temperature = get_temp(place_name)
#     return f"The Nearest Station in {place_name} is: {station_name}<br>Wheelchair Accessible:{wheelchair_accessible}<br>Temperature:{temperature} Kelvin"


if __name__ == '__main__':
    app.run(debug=True)
