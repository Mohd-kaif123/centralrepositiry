import requests
'''
url="https://jsonplaceholder.typicode.com/users/1" #API endpoint
#url="https://jsonplaceholder.typicode.com/posts/1" #API endpoint
#url="https://www.google.com" #API endpoint

response=requests.get(url)

#print("Status Code:", response.status_code) # 200: OK, 404: Not Found, 500: Internal Server Error
#print("Headers:", response.headers)
#print("Content:", response.text)
if(response.status_code==200):
    data=response.json() # parse JSON response
    print("User Name:", data["username"])
    print("Email:", data["email"])
else:
    print("Failed to retrieve data. Status Code:", response.status_code)
    '''
'''
url = "https://api.github.com"
response=requests.get(url)
print("status code:", response.status_code)   
'''
'''
url = "https://api.github.com"
response=requests.get(url)
print(response.text)
'''

'''
url="https://www.google.com"
response=requests.get(url)

if (response.status_code==200):
    print("Website is Up")
else:
    print("Website is down ")
    '''

'''
url = "https://jsonplaceholder.typicode.com/users/1"
response= requests.get(url)
user_data = response.json()
print(user_data["name"])
'''
'''
url = "https://jsonplaceholder.typicode.com/users/1"
response=requests.get(url)
user_name=response.json()
username=response.json()
user_email=response.json()
print("Name:",user_name["name"])
print("Username:",username["title"])
print("Email:",user_email["completed"])
'''

'''
url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(url)

# 1. JSON data ko variable me store karo
todo_data = response.json()

# 2. Dictionary se values nikal kar variable me rakho
task_title = todo_data["title"]
is_completed = todo_data["completed"]

# 3. F-string ka use karke expected format me print karo
print(f"Task: {task_title}")
print(f"Completed: {is_completed}")
'''

import sys

'''
url =sys.argv[1]
response =requests.get(url)
print("Status code:",response.status_code)
'''
