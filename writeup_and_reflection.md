# Web App Development - MBTA Helper by Alan Xian and Maciej Czapnik

## Project Overview:

We have created a simple text based MBTA Helper, a web application that finds the closest MBTA station to the location provided by the user.

[x] Upon visiting the index page at http://127.0.0.1:5000/, the user will be greeted by a page that says hello, and includes an input form that requests a place name.
[x] Upon clicking the 'Submit' button, the data from the form will be sent via a POST request to the Flask backend at the route POST /nearest
[x] (Optional) Perform some simple validation on the user input. See wtforms.
[x] The Flask backend will handle the request to POST /nearest_mbta. Then your app will render a mbta_station page for the user - presenting nearest MBTA stop and whether it is wheelchair accessible. In this step, you need to use the code from Part 1.
[x] If something is wrong, the app will render a simple error page, which will include some indication that the search did not work, in addition to a button (or link) that will redirect the user back to the home page.

## Project Reflection:

- This was by far the most fun and rewarding assignment we have had so far in the class. We felt like we could have implemented more features, such as providing the vehicle type and exact location of the stop. We got stuck on certain parts of the assignment, which was frustrating. At first, we did not know how to generate the link from the MBTA website; however, we re-read the assignment instructions. While this was tedious, it was interesting to read the documentation top to bottom and try to contruct the URL by ourselves (unsuccessfully). Then, after finishing mbta_helper.py and the Flask set-up, we ran into some issues with some locations not showing up. After talking with Professor Li, we realized that we failed to specify the general area in the coordinates lookup and thus were getting results from around the world, which does not work with the MBTA API. If we had more time with the assignment, we would definitely expand more, create new features, and try out new APIs (such as the Google Maps API).

- I believe this project gave us a great idea of where do we stand as a team and what do we have to improve on to be successful with our term project. With this assignment we have been a little chaotic and didn't divide the work very clearly. Fixing that will allow us to be more productive and efficient, write more and better functions easier. 