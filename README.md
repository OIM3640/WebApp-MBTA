# WebApp-MBTA Project Writeup and Reflection

 This is the base repo for MBTA project. Please read [instructions](instructions.md). 

### **Project Overview:**

This project creates a local HTML page using Flask and returns the closest MBTA stop to an inputted location within Boston, MA. 

To accomplish this, the project used two APIs: 
1) [*MapQuest*](https://developer.mapquest.com/documentation/geocoding-api/address/get/): Returns the latitude and longitude of a speciifc place name/address

2) [*MBTA-realtime API*](https://api-v3.mbta.com/docs/swagger/index.html): Returns the name and wheelchair accessibility of the nearest MBTA stop from a given location. 

Using these APIs, I wrote functions to find the latitude/longitude of a user-inputted location, and return the nearest MBTA stop and whether it is wheelchair accessible.

The front-end for this application was built in Flask and consists of three pages: 

* Index: Uses the POST request method to prompt user to input their location. Redirects user to correct HTML page. If location is close to a MBTA station, then it redirects to closestMBTA. Adversely, it redirects to the error page if there is no close station.
* closestMBTA: This page shows a successful result by returning the nearest MBTA station and whether it is wheelchair accessible, based on an inputted location. The user is then given the option to search for another location.
* Error: This page prompts the user with an error message if there is no station near their inputted location, then prompts them to search again.

To store information across pages, I stored it in session["place"]. However, this forced me to use a secret key, which I stored in the config file.

### **Project Reflection:**

From a process point of view, this project went relatively well, as I believe my program accomplishes its required tasks. However, I did have some trouble initially trying to restrict the latitude and longitude of a location within Massachusetts. But I was able to solve this in a simple way by adding "MA" after the JSON request. 

I also had a good plan for unit testing, as I did some research into locations in Massachusetts that would test all possibilities: having a wheelchair accessible MBTA stop nearby, having a MBTA stop nearby that is NOT wheelchair accessible, and simply not having a MBTA stop nearby. These test cases can be seen at the bototm of this README file.

I learned that it is extremely important to research the API documentation before writing code, as that helped me tremendously in understanding how the JSON files are organized. Moving forward, I will apply this knowledge in my final project, as I am more comfortable using web APIs now. 

Nevertheless, there are always ways to improve. Specifically, I did not have time to add any unique features such as sorting the stops by type of transportation or making the front-end look nicer or be more interactive. 

In terms of dividing work, I did this project individually, therefore I did the task by myself. I will also be doing the final project by myself, as it works better with my schedule this semester. 


### **Example Test Cases:** ###

1. Boston Commons, Boston

2. My Vegan Thai Cafe

3. Harvard University

4. Shanghai
- Returns error since it is not near a MBTA station

5. 100 Cambridge St Ste 2, Boston, MA 02114
- Not accessible by wheelchair