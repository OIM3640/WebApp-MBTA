# WebApp-MBTA
by Hanlu Ma, Sabrina Chen, Reese Hu
# Project Overview
 Overall, the logistic of this project is to build a website where we can find the nearest MBTA station by inputing the current location. It is done by locating the current location with the applicaion of API connection which returns information about the input location, and then filter its coordinates and whether it is wheelchair accessible by Json processing. API is also utilized to call the closest MBTA station around that coornidates as well. Also, we designed three webpages, which are the homepage for input location, the page for result, andthe page when there is indexerror.

# Project Reflection
 Regarding the process, we went through a few problems and confusions along coding. The major one is while we were trying to get the coordinates of the location, the API sometimes calls information of several places with the same name and some of them are far from the range of MBTA stations in Massachusetts, and we our function always returns the lat and long of the first place in the dictionary. This might be inaccurate since the desired input location may not be the one returned by the function. Our current solution is to specify the input and add ",Boston" at the end of the address name in the input. If more time is given, we could improve by adding 


