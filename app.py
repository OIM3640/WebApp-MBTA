"""
Simple "Hello, World" application using Flask
"""

from flask import Flask
from flask import redirect
from mbta_helper import find_stop_near
from flask import request
from flask import render_template
app = Flask(__name__)


#create the index, when opening render the template for form.html
@app.route('/')
def index():

    return render_template('form.html')
#create an error page, when this runs render the template for error.html
@app.route('/error')
def error():
    return render_template('error.html')

#indicate app to return /location in url
#Display methods to be POST or GET
@app.route('/location/', methods = ["POST","GET"])
def location():
    #check to see if method is POST (which it should be since POST is the only option from the form)
    if request.method == "POST":
        #obtain the reuslts from the completed form
        form_data = request.form
        #access the balues from the form
        for value in form_data.values():
            #handle and error exception that is type Index or Type
            try:
                #use the function find_stop_near from mbta_helper.py to find the MBTA stop from the value obtained from the form
                neareststop = find_stop_near(value)
                #split the MBTA stop and wheelchair accessibility into distinct bariables
                stop = neareststop[0]
                wheelchair = neareststop[1]
                #return the template locaiton.html, send in variable sstop and wheelchair
                return render_template('location.html', stop=stop, wheelchair = wheelchair )
            #in the case an error occurs
            except (IndexError,TypeError):
                #if an index or type error occurs, redirect the user to /error, showing the error.html template
                return redirect(('/error'))
        

if __name__ == '__main__':
    app.run(debug=True)
