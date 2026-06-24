# you need to install beautifulsoup4 library before running this code
# sudo apt install python3-bs4
from bs4 import BeautifulSoup
html='<html><body><h1>Welcome to PW SKILLS</h1></body></html>'
soup=BeautifulSoup(html,'html.parser')
print(soup.h1.text)

html2="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python Web Scraping</title>
</head>
<body>
    <h1>PW SKILLS</h1>
    <p class="info">Web Automation</p>
    
</body>
</html>
"""

soup2=BeautifulSoup(html2,'html.parser')
print("Title:", soup2.title.text)
print("Heading:", soup2.h1.text)
print("Paragraph:", soup2.p.text)
print("Paragraph Class:", soup2.find("p",class_="info").text)