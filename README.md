# WebApp-MBTA
 This is the base repository for Web App Developement project. Please read [instructions](instructions.md). 

# Team Members
Yuefan Cao & Jade Liang

# Project Overview
This project's purpose is to build a website that will allow people to find a nearby MBTA station and provide the current weather of the location. The website will request the user to input a location. If the input is valid, the site will bring the user to a new page that displays the nearby station and the weather of the provided location. However, if the user provides any irrelevant inputs such as a string of numbers or a random string of letters, it will bring them to an error page. This error page will have a message redirecting them to go back to the home page and provide a new input. To build this website, we will combine three APIs together: MapBox API, MBTA API, and OpenWeather API. 

# 2. Reflection
 ## 1. *Process* POV
During the development of mbta_helper, we initially encountered an issue with retrieving the correct latitude and longitude coordinates in the get_lat_lng() function. The function consistently returned "None", indicating that the response data was empty. To address this issue, we attempted to refine our query by adding an additional filter to the URL called "radius", set to a value of 1000. However, this adjustment inadvertently exacerbated the problem, as we consistently received the same output regardless of the latitude and longitude inputs. Upon further investigation, we identified that the root cause of the issue was within the get_lat_lng() function itself. Originally, the function returned a tuple variable where latitude was mistakenly assigned as longitude, and longitude as latitude. By correcting this ordering and adjusting the output type to string, we were able to resolve the issue and ensure the correct functioning of the code. As both of us are trying to debug and push the code at the same time on GitHub, it is very inefficient because we both need to adapt to the changes made by the other person.Therefore, we kept one error code as test.py and the corrected version as mbta_helper.py. Keeping two versions of the code in different files from the begginning of this project would have helped accelerate this debugging process. 
After the development of mbta_help, the project progressed much smoother. Writing the app and the html for the website was much easier for us. In fact it was the fun part because we got to be creative with the website design. Duirng the process of building the website, the most frequent error was NameError. For example, our html file was under the folder "template", but in our code in app.py, we would refer to it as "templates". As a result, our code would not work because they cannot find the folder. Another example would be missing underscores between words when we were naming our html files, which also impacted our ability to access to these html files in our code. So, during the process of building the website, we had an iterative process of consistently checking names when we encounter NameError. Otherwise, the overall process of building the MBTA finder website was smooth and less difficult in comparision to writing the code for mbta_helper.
 ## 2. Our Work Division
We originally planned to work separately, working whenever we are personally free because we both have very busy schedules. This usually leaves us with little shared time we can sit down together to work considering one of us also lives off-campus, and it would not be safe to call an Uber extremely late at night. However, we found a complication with this working method. Due to lack of communication of when we are working on the project and what part of the project we are working on, we often have conflict messages when fetching origin and pull each other’s work to our laptops.  

Therefore, to address this problem, we realized we should be clearer on how we split the parts. For example, Yuefan would write the code for the first three functions and Jade would write the last function and a new function for the extension. We also split up the app.py and the html work. Yuefan would write the app.py and Jade would write the html and CSS code to design the website because Jade has a strong interest in website designing. Another solution we implemented is to stay on call with each other while working to allow both of us to smoothly work simultaneously together and have quick access to each other. This is to substitute working together in the same setting. With the solutions implemented, our work process was much better, helping to eliminate the issue of overlapping work.  

We believe this was a good learning process for what worked well when working together between us, providing a precedent for our group project. Next time, we would start by clearly dividing our work and ensuring that we have clear communication. We found communication is very important when collaborating on Python code. 
## 3. *Learning* POV

While developing functions within MBTA_helper, we encountered challenges with the URL not functioning correctly, resulting in consistently returning "None" as the output. To resolve this issue, we sought guidance from ChatGPT on debugging techniques to identify the source of the error. Moreover, we looked into the specific website in the screenshot provided to look for any possible mistake on our part. Despite debugging and systematically printing outputs line by line, we discovered that the get_nearest_station function was returning an empty dataset. Although ChatGPT provided some scenarios for potential causes of this issue, it couldn't pinpoint the exact error. Consequently, we resorted to manually researching and comparing actual latitude and longitude coordinates for different locations to identify the root cause. It became apparent that our original location, Babson College, might not be widely recognized, leading to incorrect coordinates being returned. In hindsight, selecting a more prominent location initially would have facilitated the debugging process and mitigated this issue.

![alt text](image.png)

Through this project, we learned that having a consistent naming habit would be beneficial for us going forward to our group python project. This would save us time in identifying small errors, which can be difficult to identify sometimes because of how minor of an issue it is. ChatGPT was helpful in assisting us identify these small errors. The way ChatGPT was used to identify the errors is by sending it the code we have written along with the file locations and asking it to check our code. After a few times it told us our code had issue with inconsistent naming, we were able to better consistently name our files. Additionally, going forward, we will also keep this mind as well.  

In general, one thing we wish we knew beforehand was optimal ways to collaborate on a Python project. This would have helped us clear our confusion when we encountered conflicts when pulling from origin. We spent some time figuring out the issue and resolving the situation. We also lost some code due to the merging issue because at one point we just strived to resolve the merging conflict and have a synced Python between the two of us. As a result, we had to rewrite some codes. Therefore, if we were provided suggestions or a quick lesson on things to be aware of when collaborating on a Python project, it would have helped us out a lot.  
