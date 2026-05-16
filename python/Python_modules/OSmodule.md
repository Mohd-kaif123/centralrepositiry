Pehle Samjho — os Module Hai Kya?
Socho tumhare paas ek assistant hai jo tumhare computer ka kaam kar sakta hai:

Folders banana
Folders delete karna
Files dekhna
Current location batana
Files rename karna

Ye sab kaam os module karta hai!

# import os   # Assistant ko bulao

Bas ye ek line — aur tumhare paas poora computer control! 💻

############################################################################

Sabse Common Kaam — Ek Ek Karke

1. Abhi Kahan Ho? — os.getcwd()
import os

location = os.getcwd()
print(location)
# Output: C:\Users\Rahul\Desktop

cwd = Current Working Directory
Matlab — "abhi tu computer me kahan hai?"


2. Folder Banana — os.mkdir()
import os

os.mkdir("mera_folder")
# Ek naya folder ban gaya — "mera_folder" naam ka!

Waise hi jaise Windows me Right Click → New Folder karte ho — bas code se!


3. Folder ke Andar Kya Hai? — os.listdir()
import os

cheezein = os.listdir()
print(cheezein)
# Output: ['file1.txt', 'mera_folder', 'photo.jpg']

Matlab — "is folder me kya kya pada hua hai?"


4. Folder me Jaana — os.chdir()
import os

os.chdir("mera_folder")   # Us folder me ghus jao
print(os.getcwd())        # Ab yahan ho tum
# Output: C:\Users\Rahul\Desktop\mera_folder

Waise hi jaise folder pe double click karte ho!


5. Folder Delete Karna — os.rmdir()
import os

os.rmdir("mera_folder")
# Folder delete ho gaya!

⚠️ Dhyan rakho — sirf khali folder delete hoga is se!


6. File ya Folder Exist Karta Hai Kya? — os.path.exists()
import os

print(os.path.exists("mera_folder"))   # True ya False
print(os.path.exists("abcd"))          # False — ye hai hi nahi

Kaam aata hai jab pehle check karna ho ki folder hai ya nahi — phir banana!


7. Rename Karna — os.rename()
import os

os.rename("purana_naam", "naya_naam")
# File ya folder ka naam badal gaya!

8. Environment Variables — os.environ
import os

print(os.environ.get("PATH"))
# Tumhare system ka PATH variable print hoga

Ye thoda advanced hai — passwords aur secret keys store karne ke kaam aata hai!

############################################################################

Saari Commands Ek Jagah :-

##Command##                           ##Kaam##
os.getcwd()                           Abhi kahan ho
os.mkdir("naam")                      Naya folder banao
os.listdir()                          Folder me kya hai
os.chdir("naam")                      Folder me jao
os.rmdir("naam")                      Folder delete karo
os.path.exists("naam")                Exist karta hai kya
os.rename("purana", "naya")           Naam badlo
os.environ                            System variables