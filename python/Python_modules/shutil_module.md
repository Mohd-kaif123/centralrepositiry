############################################################################
shutil Module — Kya Hai Ye?
shutil = Shell Utility
Python ka ek built-in module hai — matlab install nahi karna, bas import karo aur use karo.
import shutil
Ye module kaam aata hai jab:

Files/Folders ke saath kaam karna ho
Disk ki details nikalni ho

############################################################################

Part 1 — File aur Folder Kaam

1. File Copy Karna — shutil.copy()
import shutil

shutil.copy("original.txt", "copy_of_original.txt")
# original.txt ka ek copy ban jaayega
==> Real life me kahan? → Jab backup banana ho kisi file ka!

2. File Move Karna — shutil.move()
import shutil

shutil.move("file.txt", "new_folder/file.txt")
# file.txt utha ke new_folder me chali jaayegi
==> Real life me kahan? → Jaise phone me photo ek album se doosre me move karo!

3. Pura Folder Copy Karna — shutil.copytree()
import shutil

shutil.copytree("mera_folder", "mera_folder_backup")
# Pura folder — andar ki saari files samet — copy ho jaayega
===> Real life me kahan? → Poore project ka backup lena!

4. Pura Folder Delete Karna — shutil.rmtree()
import shutil

shutil.rmtree("mera_folder")
# Pura folder andar ki saari files samet DELETE ho jaayega
# ⚠️ Seedha permanent delete — Recycle Bin me nahi jaata!
===> Real life me kahan? → Koi purana project folder permanently hatana!

5. File Rename/Move — shutil.move() se hi hota hai
import shutil

shutil.move("purana_naam.txt", "naya_naam.txt")
# File ka naam badal jaayega

############################################################################

Part 2 — Disk Details

6. Disk ki Details Nikalna — shutil.disk_usage()
import shutil

details = shutil.disk_usage("/")
# "/" matlab root drive — Windows me "C:/" likhna

print(f"Total Storage : {details.total / (1024**3):.2f} GB")
print(f"Use Ho Rahi  : {details.used / (1024**3):.2f} GB")
print(f"Free Storage  : {details.free / (1024**3):.2f} GB")

Output aisa aayega:

Total Storage : 512.00 GB
Use Ho Rahi  : 128.50 GB
Free Storage  : 383.50 GB

===> 1024**3 isliye kyunki computer bytes me count karta hai — us hisaab se GB me convert karna padta hai!

Saari Important Cheezein Ek Table Me :-
Method                      Kaam
shutil.copy()               File copy karna
shutil.move()               File move ya rename karna
shutil.copytree()           Pura folder copy karna
shutil.rmtree()             Pura folder delete karna
shutil.disk_usage()         Disk ki storage details