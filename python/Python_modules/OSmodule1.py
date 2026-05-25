'''# current directory: os.getcwd()
import os 
location = os.getcwd()  # cwd = Current Working Directory Matlab — "abhi ham computer me kahan hai?"
print(location)

# Folder Banana: os.mkdir()
import os

os.mkdir("mera_folder")  # 

# Folder ke andar kya hai? -- os.listdir()
import os
content=os.listdir()
print(content)

#Folder me jana--os.chdir()
import os
os.chdir("mera_folder")
print(os.getcwd())

# Folder Delete karna -- os.rmdir()
import os
os.rmdir("mera_folder")


# File ya folder Exist karte hai kya?--  os.path.exists()
import os
print(os.path.exists("mera_folder"))
print(os.path.exists("OSmodule.md"))
'''

# Environvent Variables -- os.enivron
import os
print(os.environ.get("path"))