***Project Overview***

This project is a Web App that will take a form input of a location name, and then redirect to another web page to show the name of the nearest MTBA station and whether this station is wheelchair accessible. In order to fulfill such function, I write a mbta_helper function to automatically turn a place name into longtitude and latitude and then use these information to obtain the station and whealchair information. Two html template are used to take the input and return the output.

***Project Refelction***

From a process point of view, the overall assignment goes smoothly and I was able to utilize what I learnt in class to write the mbta_helper function and design an interactive web structure. There are 2 things that could be improved in the future. 

First, sometimes the get_lat_long function returns data difference from what I found via Google. After I change space into %20, some research results become correct but there are still certain search results go wrong. If I have time in the future, I would try to understand what cuases such mnistakes and fix the issues.

Seocnd, because sometimes the search results are not accurate, the website return an error instead of the result page. It could be better if the error page is edited and a button to return to homepage is added.

In terms of team process, I did this project alone as I planned to do my final project alone. This gives me a more comprehensive learning experience on every piece of code this project include.