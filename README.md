# <b>Assignment_3 Write-up</b>

## <u><b>Project Overview</b></u>

<h4>
The objective of this project was to create a web app using Flask,  where users would enter any location within Massachusetts and the app would return the closest MBTA station to the given location and whether it is wheelchair accesible. To start the project, we requested and API from Mapquest and created a function that would generate a Mapquest URL for every location being input by the user. We then created another function using the json library to return a json object containing the response for the API request of the given URL. We then obtained the co-ordinates of the given location. We then fed these co-ordinates to the MBTA API and found the nearest station and its accesibility status. Lastly, we combined all helpers into a single function that accepts a place name as an argument and returns the nearest station and its accesibility status. We then incorporated this function into a wep page.
</h4> 


## <u><b>Project Reflection </u></b>

<h4> 
In terms of process, what worked well for us was that we divided the project into two parts. We first focused on creating helper functions that could interact with the API and return to us our desired output. Then, we worked on creating a webpage that could interact with the user and receive their inputs. An area to improve in would be fully understanding the assignments and reading the tips we were given, as we spent too much time on figuring out the data structure of the MBTA json object, when we were given hints towards how to read it all along. That being said, we worked well as a team as we chose to pair program together. This was useful because we could quickly find solutions to porblems as we had two sets of eyes on the code. 
<br>
<br>
We spent a lot of our time focusing on unit testing as we wanted the program to not work only if the input was wrong or if the database did not contain the entered locations. In order to acheive this, we ensured that all inputs would be converted into a string without spaces as this is how the data was stored. Additionally, we added ',MA' to every input to ensure that the latitude and longitude returned by MapQuest was for the location in Massachusetts and not a similarly spelled location somewhere else. 
We also accounted for a user not entering anything into the web app form, by taking them back to the homepage if they pressed the result button without an input. In terms of errorhandling, we created another webpage that the users would be redirected to, if the address was not found or if the input was invalid. This page had a button to return to the home page and provided a message explaining that there has been an error. 
</h4>

