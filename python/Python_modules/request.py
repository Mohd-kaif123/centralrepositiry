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
