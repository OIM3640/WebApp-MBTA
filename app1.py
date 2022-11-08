"""
Simple "Hello, World" application using Flask
"""

import sqlite3
from flask import Flask, render_template, request, abort, g
from mbta_helper1 import find_stop_near

app = Flask(__name__)

DATABASE = 'app.db'

@app.route('/')
def hello():
    return render_template('index.html')

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