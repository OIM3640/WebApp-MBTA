# Project Wrap-up
**Angelina Cho and Kotaro Yabe**

## Project Overview
**Write a short abstract describing your project. Include all the extensions to the basic requirements**

We have a config file where we store our API keys when accessing the files. The mbta_helper.py has four functions: get_json, get_lat_long, get_nearest_station, and find_stop_near. We use mbta_helper.py to, ultimately, find the nearest station and its wheelchair accessibility. We have another file, app.py to help us use flask to construct a simple website. We imported the find_stop_near function from mbta_helper.py into the app.py, so we can use it to find the nearest station of a place given by the user. We have three html pages, indicating the main page (index.html), the result page (station-result.html), and the error page (error.html). The main page greeted the user, and provide a text box for user to input a place in Boston. It then brings us to either the result page or the error page. It brings us to the error page when there is some sort of error, and it gives user a button to bring them back to main page. The result page presents the nearest station and information on wheelchair accessibility, as well as a button that allows the user to go back to the main page.

## Project Reflection
1. From a process point of view, what went well? What could you improve? Other possible reflection topics: Was your project appropriately scoped? Did you have a good plan for unit testing? What self-studying did you do? How will you use what you learned going forward? What do you wish you knew before you started that would have helped you succeed?
2. Also discuss your team process in your reflection. How did you plan to divide the work (e.g. split by module/class, always pair program together, etc.) and how did it actually happen? Were there any issues that arose while working together, and how did you address them? What would you do differently next time?