from flask import Flask, render_template, request
from mbta_helper import find_stop_near


app = Flask(__name__)


@app.route('/')
def hello():
    return 'Welcome to my MBTA Helper Web App Development Project!'

@app.route('/mbta/')
@app.get('/mbta/')
def mbta_get():
    return render_template("mbta_form.html")

@app.post('/mbta/')
def mbta_post():
    place_name=request.form["place"]
    print("place is here")
    stop_near=find_stop_near(place_name)[0]
    if find_stop_near(place_name)[1]==True:
        handicap="True"
        print(handicap)
    else:
        handicap="False"
        print(handicap)
    return render_template("result.html", place=place_name, station=stop_near, access= handicap)


if __name__ == '__main__':
    app.run(debug=True)
