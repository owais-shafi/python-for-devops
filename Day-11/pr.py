# pip install requests and import requests module to talk to github API and we need this module to call the API

import requests

# response = requests.get("URL") , we used a requests.get() function to get the info or response from api url

# from github we find to get the api for getting the pull request 
# /repos/owner/{repo}/pulls  -> In github documentation of pull
# before this, above written api call, use https://api.github.com then /repo/owner/{repo}/pulls
# since we are trying to get list of pull requests from kubernetes we will use kubernetes in owner place
# In place of {repo},we use kubernetes because when go to github kubernetes project u will find it in URL. 

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
# this will call the api to get pull requests from kubernetes open source project and store it in response variable.
#  If we tried to print(response) we will not get it in the form we wanted, this is because it is an class or an object.
# print(type(response)) -> this will print the type of response, we see in output it is basically an class or an object.
# to get response in the form we wanted we will use: print(response.json())
# print(response.json())
# this function automatically converts json to dictionary, and hence we will get the output we wanted. 
# but output is not readable so, we will get extract the needed info 

complete_details = response.json()
for i in range(len(complete_details)) :
   print(complete_details[i]["user"]["login"])# with the help of dictionaries we retrieved the value of "login" which is Aaina26
# traversing is very easy in dictionaries, for example: complete_details[0]["users"][login]
# in the first one(0) there is 'users' and in 'users' there is 'login'.

