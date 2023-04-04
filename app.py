from flask import Flask, request, redirect, render_template
from mbta_helper import find_stop_near


app = Flask(__name__)

# this page will be the main landing page with a form 
@app.route('/')
def hello():
    return render_template("index.html") 

#this page will show the results of the user's search input 
@app.route('/nearest_mbta', methods = ['POST'])
def get_nearest_mbta():
    user_location = request.form['location']
    return user_location

if __name__ == '__main__':
    app.run(debug=True)
