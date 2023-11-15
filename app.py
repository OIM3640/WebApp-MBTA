from flask import Flask, render_template, request, redirect
from mbta_helper import find_stop_near, get_temp


app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/nearest_mbta', methods=['POST'])
def nearest_mbta():
    location = request.form['location']
    location = find_stop_near(location)
    if location == None: #exceptions
        return redirect('/error_page')
    wheelchair_access = str(location[1])
    name = location[0]

    if wheelchair_access:
        wheelchair_access = 'This location has wheelchair access'

    else:
        wheelchair_access = 'This location does not have wheelchair access'
    
    temp, temp_feel = get_temp('Boston')

    return render_template ('nearest_mbta.html', name = name, wheelchair_access = wheelchair_access, temp = temp, temp_feel = temp_feel)


@app.route('/error_page')
def error_page():
    return render_template('error_page.html')


if __name__ == '__main__':
    app.run(debug=True)
