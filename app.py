from flask import Flask, render_template, request, redirect
from main import your_closest_station

"""BEGIN FUNCTIONALITY"""

app = Flask(__name__)

@app.route('/')
def index():

    """
    returns the home page using render template
    """

    return render_template('/index.html/')


@app.route('/not_found')
def not_found():

    """
    returns the not found page using render template
    """

    return render_template('/not_found.html')


@app.route('/result', methods=['POST'])
def result():

    """
    Takes in data from html form and passes it through to backend, gets result from the backend, checks if result is error code, if not, checks if accessibility value from dictionary is 0, 1, or 2, returns result page and passes these values to the page using render template
    """

    data_from_form = request.form['QUERY']
    query = data_from_form
    result = your_closest_station(data_from_form)

    if result == 999:
        return redirect('/not_found')
    
    else:
        result = str(your_closest_station(data_from_form)[0])
        access_index = your_closest_station(data_from_form)[1]

        if access_index == [1]:
            accessibility = "has wheelchair accessibility accomodations (if trip is wheelchair accessible)"
        elif access_index == [2]:
            accessibility = "does not have accessibility accomodations" 
        else:
            accessibility = "has no information about accessibility"

        formatted_result = result[2:len(result)-2]

        return render_template('/result.html', result=formatted_result, query = query, accessibility = accessibility)


@app.route('/redirect', methods = ['GET'])
def redirect_home():

    """
    Returns user to home page using redirect
    """

    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)
