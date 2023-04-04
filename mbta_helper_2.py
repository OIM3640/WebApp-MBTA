def get_nearest_station(latitude: str, longitude: str) -> tuple[str, bool]:
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible) tuple for the nearest MBTA station to the given coordinates.

    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL formatting requirements for the 'GET /stops' API.
    """
    url = f"https://api-v3.mbta.com/stops?api_key={MBTA_API_KEY}&sort=distance&filter%5Blatitude%5D={latitude}&filter%5Blongitude%5D={longitude}"
    response_data = get_json(url)
    if response_data['data']:
        first_stop = response_data['data'][0]
        station_name, wheelchair_accessible = first_stop['attributes'][
            'description'], first_stop['attributes']['wheelchair_boarding']
        if wheelchair_accessible == 1:
            wheelchair_accessible = True
        else:
            wheelchair_accessible = False
        return station_name, wheelchair_accessible
    else:
        return f"There is no stop nearby ({latitude},{longitude}), please choose another location"
