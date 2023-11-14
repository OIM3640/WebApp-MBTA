from flask import Flask , render_template , request
from mbta_helper_final import find_stop_near
app = Flask(__name__)


@app.get('/')
def mbta_finder(name=None):
    return render_template('index.html', name=name) #functioning as intended.

@app.post('/')
def hello():
        user_location_input = request.form['user_location_input']
        answer_1, answer_2 = find_stop_near(user_location_input)
        #split answer into two variables and use them to say where the person is. 
        return render_template('sucessful_query_results.html',
                    answer_1 = answer_1,
                    answer_2 = answer_2,
                    user_location_input = user_location_input
                    )
        
             


if __name__ == '__main__':
    app.run(debug=True)

