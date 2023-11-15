# WebApp-MBTA
### Maria Dominguez and Natalie Guillamon
******IF WE COULD PLEASE GET MORE TIME TO TURN IN A MORE DIGNIFIED PIECE OF WORK IT WOULD BE EXTREMELY APPRECIATED
 This is the base repository for Web App Developement project. Please read [instructions](instructions.md). 

**1. Project Overview** (~1 paragraph)

This project is based on MBTA public transportation, which is based on the Massachussetts Bay. Using the MBTA's API, we will create a website that takes an address and returns the nearest MBTA station and whether it is wheelchair accessible. This project has 4 components to it:
1. Python code for functions that process MBTA and MapBox API's to return output. (mbta_helper2)
2. Building app that indicates how information is collected and processed in terms of visual output (app.py)
3. Templates where html code is used to design graphics and visual details of website (templates)
4. Creative add-ons: What can we add for this to be an appealing site


**2. Reflection** (~3 paragraphs + screenshots)

After you finish the project, Please write a short document for reflection.

1. Discuss the **process** point of view, including what went well and what could be improved. Provide reflections on topics such as project scoping, testing, and anything else that could have helped the team succeed.

 In terms of process, we outlines the steps of the project as the following:
 -Create functions in mbta_helper that will (together) take in an address and return the nearest MBTA stop and whether it is wheelchair accessible
 -Using those functions, code app in app.py, which designs actions for the website (ex: address is input, mbta station is returned). So the goal in this part is to program the actual functionality of the website?
 -Templates for the webapp interface
 -Extra features, Reflection and submissions

 Intially, we believed this was going to be somewhat of a linear process, but that couldn't have been further from the truth. Each aspect of the project built on the other, and in order to implement a change, the infrastructure underneath had to be well interconnected and in consensus. Although we believe we had a good project scope and a realistic goal of finalizing the functionality before adding onto our interface, we didn't know HTML prior to this, so we weren't confident with moving into that step without being absolutely sure of our functionalty (which, suprise, Never happened! THE CODE NEVER WORKED SEND HELP PROF. ZHI!!!!!!!!!!!!!!!!!)

 In terms of testing, had our tests been successful, we are sure that we could have proceeded with more ease and turn in a much higher quality, and ambitious project. However after tortouring hours of making small changes and testing their outcomes, we are effectively stuck.


1. Discuss your **team's work division**, including how the work was planned to be divided and how it actually happened. Address any issues that arose while working together and how they were addressed. Finally, discuss what you would do differently next time.

We have had a great team dynamic and communication. Neverheless, it has been difficult to work on the same files and share our knowledge/make edits in real time as it is complicated to manage the pull requests and merge our works if we both work on the same file. We planned to divide the work with one of us taking care of the mbta_helper2 and another one taking over the webapp building. However, failure to ensure functionality of mbta_helper led to us switching roles constantly, in attempts to avoid being burnt out of the section assigned. Nevertheless, not even by consulting ChatGPT, we weren't able to ensure our mbta_helper2.py code was working. With a simple request such as "Boston Common", No results were shown. Additionally, there are no errors that flag us in a specific direction... Therefore, the code just doesn't do what we mean for it to. On the other end, we have app.py where we faced similar issues and although the code and templates seem to be working, we can't fully test it out given its reliance on mbta_helper2. This led us to be stuck in the mbta_helper code for hours, consulting as many online resources, API documentation, etc. as we could, but we haven't been able to identify the source of issues.

3. Discuss from a **learning** perspective, what you learned through this project and how you'll use what you learned going forward. Reflect on how ChatGPT helped you and what you wish you knew beforehand that could have helped you succeed. Consider including screenshots to demonstrate your project's progress and development.


From a learning perspective, we have learned a couple tricks to work more effectively in a remote setting, which is extremely helpful for us to perfect our partnership for the final project. Additionally, working with flask and html templates has been a great experience that opened our eyes to the countless features that can be added to enhance our Webapp. Sadly, given that we were stuck on mbta_helper2 for so long, we weren't able to implement features we would have loved to continue exploring with (ex: google maps graphic on the webapp, trying to acces MBTA API for schedules,etc) but we will attempt to continue expanding on this assingment once we get over the bottleneck. We wish we could have been more sure about the program, because if we had we could have advanced other areas while fixing the issues.

