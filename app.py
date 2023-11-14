from flask import Flask, render_template, request
import mbta_helper


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def search_results():
    """
    Function will use mbta_helper to return the MBTA station results.
    """
    return mbta_helper.main()

def home():
    if request.method == 'POST':
        address = request.form.get('address')
        mbta_helper.place_name = address
        results = search_results()
        return render_template('index.html', results=results)
    return render_template('index.html', message='Address not valid')


if __name__ == '__main__':
    app.run(debug=True)
