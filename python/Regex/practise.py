import re

text = "user email is mansoorikaif123@gmail.in"

pattern =r"[a-zA-Z0-9._%#+]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}"

match = re.search(pattern,text)

if match:
    print("Email Found:",match.group())