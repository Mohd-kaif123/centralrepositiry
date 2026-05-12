#import shutil

#shutil.copy("file.txt", "file1.txt")

#shutil.move("file","new_file")

#shutil.copytree("file1.txt","Backup")

#shutil.rmtree("file1.txt")

#--------------------------------------------------------
'''
details = shutil.disk_usage("/")
print(f"Total Storage: {details.total / (1024**3):.2f} GB")  #:.2f Ka Matlab? Iska matlab hai ki decimal (point) ke baad sirf 2 digits dikhao. Jaise 150.45678 ki jagah sirf 150.46 dikhega
print(f"Use Ho Rahi hai: {details.used / (1024**3):.2f} GB")
print(f"Free Storage : {details.free / (1024**3):.2f} GB")
'''
#--------------------------------------------------------
'''import os

def get_size(path='.'):
    total_size = 0
    # os.walk se saari files aur sub-folders ko scan karo
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # Agar file exist karti hai toh uska size add karo
            if os.path.exists(fp):
                total_size += os.path.getsize(fp)
    return total_size

# Current folder ka size check karo
current_dir_size = get_size(".")
print(f"Is folder ka total size: {current_dir_size / (1024**2):.2f} MB")
'''

###########################################################################


import shutil

'''if shutil.copy("file","f_backup"):
    print("file copy hogai!")
else:
    print("Koi file copy nahi hui hai")
'''
#-----------------------------------------------------
'''
details=shutil.disk_usage("/")
print(f"Disk usage: {details.used / (1024**3):.2f}GB")
print(f"Total space: {details.total / (1024**3):.2f}GB")
print(f"Available Memory:{details.free / (1024**3):.2f}GB")
'''
#------------------------------------------------------
'''
import os

#os.mkdir("old_folder")
#os.chdir("old folder")
#os.system("data.txt")
if shutil.move("old_folder", "new_folder"):
    print("File move ho gayi")
else:
    print("file move nahi hui")
'''
#-------------------------------------------------------
'''
total, used, free=shutil.disk_usage("/")
usaged=(used/total)*100
print(f"Disk usage: {used / (1024**3):.2f} GB ({usaged:.2f}%)")
if usaged >50:
    print("Alert: Disk space khatam honi wali hai")
else:
    print("Everything is fine")
'''

#--------------------------------------------------------

import os

os.mkdir("my_project")
os.chdir("my_project")
file_name = "file1","file2"
flags =os.O_CREAT
fd=os.open(file_name, flags)
shutil.copytree("my_project","new_project")
details=shutil.disk_usage("/")
print(f"Total Memory: {details.total / (1024**3):.2f}GB")
print(f"Disk Usage: {details.used / (1024**3):.2f}GB")
print(f"Space Available: {details.free /(1024**3):.2f}GB")
total, used, free = shutil.disk_usage("/")
usage=(used/total)*100
if usage<1:
    print("Warning: Storagr kam hai!")
else:
    print("storage theek hai, backup successfull!")
    