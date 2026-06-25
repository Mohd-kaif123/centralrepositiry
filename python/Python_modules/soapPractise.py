from bs4 import BeautifulSoup

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
