# WebApp-MBTA
 This is the base repository for Web App Developement project. Please read [instructions](instructions.md). 

 Team members: Linhao Jiang, Jasmine Zhang

# Project Overview (~1 paragraph)

Our project aimed to assist users in locating the nearest MBTA station, and checking its wheelchair accessibility status. We use MAPBOX API to convert user-input addresses into coordinates, and MBTA API with these coordinates to find the nearest subway station and assess its wheelchair accessibility status. The core functionality of our application stays in the mbta_helper.py page, which interacts with those external APIs. The Flask framework is powered by app.py, it sets up the website and routing. When the user lands on the first page, will see a simple form where the user inputs their address. And once they hit 'submit', it begins a POST request to the '/find', the 'find' function in app.py takes over. 




# Reflection (~3 paragraphs + screenshots)

After you finish the project, Please write a short document for reflection.

Discuss the process point of view, including what went well and what could be improved. Provide reflections on topics such as project scoping, testing, and anything else that could have helped the team succeed.

Discuss your team's work division, including how the work was planned to be divided and how it actually happened. Address any issues that arose while working together and how they were addressed. Finally, discuss what you would do differently next time.

Discuss from a learning perspective, what you learned through this project and how you'll use what you learned going forward. Reflect on how ChatGPT helped you and what you wish you knew beforehand that could have helped you succeed. Consider including screenshots to demonstrate your project's progress and development.