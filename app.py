"""
Lead to a page ask for entering a place and show the nearest station and whether it's wheelchair accessible
"""
from mbta_helper import find_stop_near
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def MBTA():
    if request.method == 'POST':
        place_name = request.form['place']
        t = find_stop_near(place_name)
        station_name = t[0]
        wheel = t[1]
        if wheel == 'Yes':
            S = 'It is'
        if wheel == 'Maybe':
            S = 'It might be'
        else:
            S = 'It is not'
        return render_template('result.html', station = station_name,status = S)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
