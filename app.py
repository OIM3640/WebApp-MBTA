from flask import Flask, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        place_name = request.form['place-name']
        # perform calculation using place_name variable
        result = f"The place name you entered was: {place_name}"
        return redirect(url_for('nearest_mbta', place_name=place_name), code=307)

    return '''
        <form method="post">
            <p>Hello World!</p>
            <p>Please enter a place name:</p>
            <input type="text" id="place-name" name="place_name">
            <button type="submit">Submit</button>
        </form>
    '''

@app.route('/nearest_mbta', methods=['POST'])
def nearest_mbta():
    place_name = request.form['place_name']
    # perform calculation using place_name variable
    result = f"The nearest MBTA station to {place_name} is X"
    return result

if __name__ == '__main__':
    app.run(debug=True)
