# WebApp-MBTA
 This is the base repo for MBTA project. Please read [instructions](instructions.md). 

Project Reflection: (~2 paragraphs) After you finish the project, Please write a short document for reflection.

 Did you have a good plan for unit testing? How will you use what you learned going forward? What do you wish you knew before you started that would have helped you succeed?


## Project Overview 

### Functionality 
This program allows users to search for the nearest MBTA stop, wheelchair accessibility, current weather, and air quality of a place of their choice. If there is no information about a certain place, the error page would prompt the user to return to the home page and search again. If there is available information, the result page would also allow users go back to the home page to do a second search. 

### Extensions 

In addition to the required APIs, this programs also uses OpenWeatherMap API and IQAir API. The API keys are stored in a configuration file. 

## Project Reflection 

### About the Project 
The overall process went well. We did not spend much time on debugging, and we finished mbta_helper quicky. However, it did take us some time to obeserve demo code on GitHub and learn the overall structure of Flask and the html file. This project allows us to familiarize ourselves better with working with Flask and html as well as available tools. For the mbta_helper part, we especially enjoyed observing the pattern of urls as well as response data. One obstacle we encountered was the Ticketmater API. As we were hoping to use latitude and longitude to find nearby events, we found that the regular way to encode lag and long does not work out, and we were worried that the API provider took that parameter out. Therefore, we deicded to seek other APIs instead. 

### Area for Imporvement 
We could improve on the way of returning to the error page. We chose to edit mbta_helper in order for it to return None if it encounters error (cannot not find the corresponding information). But we could make the app.py to return the error page directly. 

### Collaboration Process 
For the simplicity of collaboration and the common learning goals shared between the team members, we worked together throughout the working process, which was fairly smooth and turned out to be an excellent pair learning opportunity for us. We were able to exchange knowledge with each other. 

### Self-Learning 
1) We learned how to create and read configuration files. 

2) We learned how to encode urls. 

3) We learned how to redirect to another page in html. 

4) We learned adding styles and and fomatting the html. 

We are looking forward to apply what we have learned about creating user interface and web page presentation to our waitlist project. 