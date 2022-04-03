# Assignment 3 MBTA Webapp by Martina and Carrie

## Project Overview
The project is done by Carrie and Martina, and it is a webapp that helps users to find the nearst MBTA station to the place they entered. In addition to the basic requirements, we added styles in the html templates to make it look nice and refine some of the functions in the mbta_helper.py to fix the error if the user enters a location that is not covered by the MBTA. We also added a index page before the webapp routing to the /mbta webpage.

## Project Reflection
### Project Process
From a process point of view, the project went well overall. However, we have ran into 2 major obstacles. One of them is when we using "Boston Common" as the location for testing purpose. It turns out there is Boston Common in Georgia. To fix it, we added a if statement in the get_lat_long() function so that it returns the coordinates of the place that is actually in Massachusettes. We later on added an else statement to return the coordinates for locations entered outside of Boston so that the code still runs even if the location entered is not within Boston. 

Another one is that the original mbta_helper.py functions asl for input instead of take a input, so flask cannot use the funtion and return the nearst station. Therefore, we rewrote the whole python file for it to work. One minor mistake we made is in the app file we put mbta-form.html instead of mbta_form.html, so the render_template cannot locate the template file. That was the main reason why our flak cannot run at first.

### Teamwork

