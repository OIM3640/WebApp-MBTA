"""
Simple "Hello, World" application using Flask
"""

from flask import Flask, render_template, request
from mbta_helper import find_stop_near


app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def mbta_station():
    if request.method=='POST':
        while True:
            try:
                place_name=request.form['place']
                nearest_station=find_stop_near(place_name)[0]
                wheelchair=find_stop_near(place_name)[1]
                if wheelchair==1:
                    flag=''
                else: 
                    flag='not'
                return render_template('result.html', place=place_name, station=nearest_station, accessibility=flag)
            except IndexError:
            # if the input location is not in the database
                return render_template('error.html')

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
