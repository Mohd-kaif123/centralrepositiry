# sys module kya hai?

sys Python ka built-in module hai jo Python interpreter se related information aur command line arguments access karne ke liye use hota hai.

Sabse common use:  import sys

# sys.argv kya hai?

argv = Argument Vector

Ye ek list hoti hai jisme command line se pass kiye gaye arguments store hote hain.

Maan lo file ka naam hai:

python test.py Kaif

To:

sys.argv

return karega:

['test.py', 'Kaif']

Index wise:

Index	        Value
sys.argv[0]	    test.py
sys.argv[1]	    Kaif

# Multiple arguments

Command:

python test.py Kaif 25 Mumbai

sys.argv:

['test.py', 'Kaif', '25', 'Mumbai']

Access:

name = sys.argv[1]
age = sys.argv[2]
city = sys.argv[3]

print(name)
print(age)
print(city)

Output:

Kaif
25
Mumbai

# DevOps ke liye sys module ke important functions
sys.argv      # Command line arguments
sys.exit()    # Program band karna
sys.version   # Python version
sys.platform  # Linux/Windows check
sys.path      # Python modules search path