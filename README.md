# WebApp-MBTA
by Hanlu Ma, Sabrina Chen, Reese Hu
## Project Overview
 Overall, the logistic of this project is to build a website where we can find the nearest MBTA station by inputing the current location. It is done by locating the current location with the applicaion of API connection which returns information about the input location, and then filter its coordinates and whether it is wheelchair accessible by Json processing. API is also utilized to call the closest MBTA station around that coornidates as well. Also, we designed three webpages, which are the homepage for input location, the page for result, and the page when there is indexerror.

## Project Reflection
 Regarding the process, we went through a few problems and confusions along coding. The major one is while we were trying to get the coordinates of the location, the API sometimes calls information of several places with the same name and some of them are far from the range of MBTA stations in Massachusetts. This might be inaccurate since the desired input location may not be the one returned by the function. Our current solution is to add a filter in function and limit the location in Massachusetts, and always returns the lat and long of the first place in the dictionary. What's more, we give instruction on the webpage that suggest specifying the input and add ",Boston" at the end of the address name. If more time is given, we could improve by applying more filters. In terms of other improvements, we could put more efforts on the design and aesthetics of the webpage. Moreover, we could possibly link the result to other websites such as the official site of MBTA with the information of the specific station that's provided in the result. The project could also be expanded to find railway stations in other states.

 Speaking of teamwork, we cooperated well and did everything timely and efficiently. We helped each other out in sorting out the logistics and how we were going to carry out. At first, we intended to work together on the same part then move to the next, however, gradually we started working on different parts, then cross examine for the whole project. Sabrina was in charge of the website, Hanlu did major design of functions and filter for JSON, Reese was in charge of API connection and integration write ups. In the process, we did not encounter big issues. Therefore, we are confident in working together and communicating for the next group project.

 


