from mbta_helper import find_stop_near, get_temp
# Referenced to learn about various flask modules https://flask.palletsprojects.com/en/2.2.x/quickstart/
from flask import Flask, request, render_template, redirect


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    # Referenced to learn about render_template function https://flask.palletsprojects.com/en/2.2.x/quickstart/
    return render_template('index.html')


@app.route('/nearest_mbta', methods=['POST'])
def nearest_mbta():
    # Referenced to learn about the request function https://flask.palletsprojects.com/en/2.2.x/quickstart/#the-request-object
    location = request.form['location']
    location = find_stop_near(location)
    if location == None: # find_stop_near returns None for any exceptions
        # Referenced to learn about the redirect function https://flask.palletsprojects.com/en/2.2.x/quickstart/#unique-urls-redirection-behavior
        return redirect('/error')
    temperature = get_temp(request.form['location'])
    accessible = str(location[1])
    name = location[0]
    if accessible:
        accessible = "This location is handicap accessible"
    else:
        accessible = "This location is not handicap accessible"
    # Referenced to learn about passing variables to HTML https://flask.palletsprojects.com/en/2.2.x/quickstart/#the-request-object
    return render_template('nearest_mbta.html', name = name, accessible = accessible, temperature = temperature)


@app.route('/error')
def empty():
    return render_template('error.html')


if __name__ == '__main__':
    app.run(debug=True)
