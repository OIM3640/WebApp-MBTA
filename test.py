from mbta_helper_draft import get_station

def mbta_post():
    location_name = request.form.get('query')
    result = get_station(location_name)[0]
    result2=get_station(location_name)[1]
    print(result)

    # return render_template('index.html', name=result,wheelchair_boarding = result2 )