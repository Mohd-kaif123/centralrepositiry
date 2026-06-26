from bs4 import BeautifulSoup
import requests
'''
html ='<html><body><h1>Linux</h1></body></html>'
Soup=BeautifulSoup(html,'html.parser')
print(Soup.h1.text)
'''
'''
html = '<html><head><p>My Website</p></head></html>'
Soup=BeautifulSoup(html,'html.parser')
print(Soup.html.p.text)
'''

'''
html ='<p class="course">Python</p>'
soup=BeautifulSoup(html,'html.parser')

course=soup.find('p', class_='course')
print(course.text)
'''
'''
html='<h2 id="name">Kaif</h2>'
soup=BeautifulSoup(html,'html.parser')

name=soup.find('h2', id='name')
print(name.text)
'''
'''
html ='<div>First</div><div>Second</div>'
soup=BeautifulSoup(html,'html.parser')

first=soup.find('div')
print(first.text)
'''

'''
html='<ul><li>Python</li><li>Linux</li><li>Docker</li></ul>'
soup=BeautifulSoup(html,'html.parser')

list1=soup.find_all('li')
for list in list1:
    print(list.text)
'''
'''
url = "https://www.google.com/"
response =requests.get(url)

print(response.status_code)
soup =BeautifulSoup(response.text, 'html.parser')
print(soup.title.text)
'''
'''
html="<a href=https://www.google.com/> Google </a>"
soup=BeautifulSoup(html,'html.parser') 
print(soup.a.text)
link_tag= soup.find('a')
link_url = link_tag["href"]
print(link_url)
'''
'''
html ="<img src=cat.jpg>"
soup =BeautifulSoup(html,'html.parser')
img=soup.find("img")
print(img["src"])
'''
'''
html="<a href=https://github.com>GitHub</a>"
soup=BeautifulSoup(html,'html.parser')
print(soup.a.text)
link_tag=soup.find('a')
link_url=link_tag["href"]
print(link_url)
'''
'''
html="<img src=linux.png>"
soup=BeautifulSoup(html,'html.parser')
img=soup.find('img')
print(img['src'])
'''
'''
html="<a href=https://openai.com>OpenAI</a>"
html1="<a href=https://google.com>Google</a>"
html2="<a href=https://github.com>GitHub</a>"
soup=BeautifulSoup(html,'html.parser')
all_link=soup.find('a')
for link in all_link:
    print(link.text)
    pass
'''


'''
html = """
<a href="https://openai.com">OpenAI</a>
<a href="https://google.com">Google</a>
<a href="https://github.com">GitHub</a>
"""
soup = BeautifulSoup(html, 'html.parser')

# 1. Saare links ko nikala
all_links = soup.find_all('a')

# 2. For loop chalaya (yahan 'link' har ek alag-alag tag ko pakdega)
for link in all_links:
    # Dhyan do yahan 'soup' nahi, 'link' use kiya hai
    print(f"{link.text} -> {link['href']}")

'''