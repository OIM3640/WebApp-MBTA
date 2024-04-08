# WebApp-MBTA
 This is the base repository for Web App Developement project. Please read [instructions](instructions.md). 

# Team Members
Yuefan Cao & Jade Liang

# 2. Reflection
## 1. *process* POV

During the development of mbta_helper, we initially encountered an issue with retrieving the correct latitude and longitude coordinates in the get_lat_lng() function. The function consistently returned "None", indicating that the response data was empty. To address this issue, we attempted to refine our query by adding an additional filter to the URL called "radius", set to a value of 1000. However, this adjustment inadvertently exacerbated the problem, as we consistently received the same output regardless of the latitude and longitude inputs. Upon further investigation, we identified that the root cause of the issue was within the get_lat_lng() function itself. Originally, the function returned a tuple variable where latitude was mistakenly assigned as longitude, and longitude as latitude. By correcting this ordering and adjusting the output type to string, we were able to resolve the issue and ensure the correct functioning of the code. As both of us are trying to debug and push the code at the same time on GitHub, it is very inefficient because we both need to adapt to the changes made by the other person.Therefore, we kept one error code as test.py and the corrected version as mbta_helper.py. Keeping two versions of the code in different files from the begginning of this project would have helped accelerate this debugging process. 

## 3. *learning* POV

