from flask import Flask, render_template, request
from find_station import find_closest_station
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:0307Fede2110@localhost:3306/user_mbta'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class UserQuery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(80), nullable=False)
    mbta_stop = db.Column(db.String(80))
    wheelchair_accessible = db.Column(db.Boolean)

    def __repr__(self):
        return f'<UserQuery {self.location}>'

@app.before_request
def create_tables():
    db.create_all()

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/find_mbta', methods=['POST'])
def find_mbta():
    location = request.form['location']
    result = find_closest_station(location)

    if isinstance(result, str):
            return render_template('mbta_station.html', error=result, mbta_stop=None, wheelchair_accessible=None)

    

    mbta_stop, wheelchair_accessible = result
    wheelchair_accessible_bool = wheelchair_accessible == 'Yes'

    
    query = UserQuery(location=location, mbta_stop=mbta_stop, wheelchair_accessible=wheelchair_accessible_bool)
    db.session.add(query)
    db.session.commit()

    
    return render_template('mbta_station.html', mbta_stop=mbta_stop, wheelchair_accessible=wheelchair_accessible, error=False)

if __name__ == '__main__':
    app.run(debug=True)