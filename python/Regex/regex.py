# importing regular expression module
import re 

#text to search for email address
text="User's email is nikunj_soni@pw.live"

# regular expression pattern to match email addresses
pattern=r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# searching for the pattern in the text
match=re.search(pattern,text)

if match:
    print("Email Found:",match.group())
else:
    print("Email is not Found!")