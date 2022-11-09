"""
Simple "Hello, World" application using Flask
"""

from flask import Flask, request, render_template
from mbta_helper import find_stop_near


app = Flask(__name__)


@app.route('/', methods=["GET","POST"])
def show_location():
    if request.method == "POST":
        location = request.form['location']
        stat, wheelchair_access = find_stop_near(location)
        return render_template('index-result.htmi',location=stat, wheelchair_access=wheelchair_access)
    else:
        return render_template('index.htmi')
    
if __name__ == '__main__':
    app.run(debug=True)



def hello():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
