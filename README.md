# WebApp-MBTA
 This is the base repository for Web App Developement project. Please read [instructions](instructions.md). 

# Team Members
Yuefan Cao & Jade Liang

# 1. Project Overview
When building mbta_helper, we encountered the first problem of trying to get the correct lattitude and longitude in the function get_lat_lng. The function could only return "None", indicating the response data was an empty dataset. We manually added another filter to the url that is named as "radius", and set to a value of 1000. However, this only worsened the problem. Everytime we change the latitude and longitude, the output is always the same. We found out that after we eliminate the radius filter, 
