"""
Simple "Hello, World" application using Flask
"""

from flask import Flask, render_template, request, redirect, url_for, session
from mbta_helper import *
from config import *

app = Flask(__name__)

app.secret_key = APP_SECRET_KEY
# @app.route('/')

# def hello():
#     return 'Hello World!'

@app.route('/',methods=['POST','GET'])
def index():
    """ Index/home page of the website
    """
    if request.method =='POST':
        session["place"] = request.form["place"] # Stores "place" input in session
        return redirect(url_for("nearMBTA"))
    else:
        return render_template("index.html")

@app.route("/nearMBTA")
def nearMBTA():
    """ If place has a nearby MBTA, returns the page with that info,
        else (or if any other errors), returns an error page 
    """
    try:
        text = find_stop_near(session["place"])
        return render_template("closestMBTA.html", text = text)
    except:
        return render_template('error.html')


if __name__ == '__main__':
    app.run(debug=True)
