#---------------LEVEL-1 Q)---------------#

#import os

#os.mkdir("my_practise")
#os.listdir("my_practise")
#os.rename("my_practise","my_pract")
#os.path.exists("my_practise")

#---------------LEVEL-2 Q)---------------#

#import os

'''if os.path.exists("my_pract"):
    print("Folder pahale se hai")
else:
    print("folder exist nahi karta")'''

#os.chdir("my_pract")
#print(os.getcwd())
#os.rmdir("my_pract")

#---------------LEVEL-3 Q)---------------#

import os
'''
os.mkdir("office")
os.chdir("office")

os.mkdir("HR")
os.mkdir("accounts")

content = os.listdir(".")
print(content)


if os.path.exists("Backup"):
    print("Backup folder already exists karta hai")
else:
    os.mkdir("Backup")
    print("Back folder is ready!")
print(os.getcwd())'''