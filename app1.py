"""
Simple "Hello, World" application using Flask
"""

import sqlite3
from flask import Flask, render_template, request, abort, g
from mbta import find_stop_near

app = Flask(__name__)

DATABASE = 'app.db'

<<<<<<< HEAD
@app.route('/')
def hello():
    return render_template('index.html')
=======
from flask import request

# 1. 
# Hello page + input form

# 2. 
# @app post/nearest post request
# 3.  
# Render a page present result from part 1
# 4. 
# Or error page say the search did not work + button(link) redirect to the first page

>>>>>>> c38768c4dba67b4ee2d8ccbb699f534665cbf6a4

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__ == '__main__':
    app.run(debug=True)