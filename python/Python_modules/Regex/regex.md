## ------------------------------------------------------------------------##
Regex Kya Hai? — Ek Dam Simple
Socho tumhare paas 1000 log ka data hai ek file me — aur tumhe sirf phone numbers nikalne hain.
Kya tum manually padhoge? Impossible!
Regex ek pattern hota hai — tum batate ho "kaise dikhna chahiye" — aur wo dhundh ke de deta hai.
"Mera number 98765-43210 hai aur email abc@gmail.com hai"
                ^^^^^^^^^                ^^^^^^^^^^^^^^
                Regex dhundh leta hai!

## ------------------------------------------------------------------------##

Ek Real Example Pehle
pythonimport re  # Pehle ye likhna padta hai — regex library hai ye

text = "Mera number 9876543210 hai"

result = re.search(r'\d+', text)  # \d+ matlab "koi bhi number dhundho"
print(result.group())  # 9876543210
Bas itna hi basic idea hai — pattern do, dhundh ke dega.

## ------------------------------------------------------------------------##

Regex me Kya Kya Hota Hai — Ek Ek Karke
# 1. \d — Koi bhi Number
pythonimport re

text = "Mera roll number 42 hai"
result = re.search(r'\d+', text)
print(result.group())  # 42
PatternMatlab\dEk digit (0-9)\d+Ek ya zyada digits\d{10}Exactly 10 digits

# 2. \w — Koi bhi Word/Letter
pythontext = "Rahul123"
result = re.search(r'\w+', text)
print(result.group())  # Rahul123
PatternMatlab\wEk letter ya digit\w+Ek ya zyada letters/digits

# 3. . — Koi bhi Ek Character
pythontext = "cat bat rat"
results = re.findall(r'.at', text)
print(results)  # ['cat', 'bat', 'rat']

# 4. ^ aur $ — Start aur End
pythontext = "Rahul bhai hai"

re.search(r'^Rahul', text)  # ✅ Start me "Rahul" hai
re.search(r'hai$', text)    # ✅ End me "hai" hai
re.search(r'^bhai', text)   # ❌ Start me "bhai" nahi hai

# 5. [] — Inme se Koi Ek
pythontext = "cat bat rat fat"
results = re.findall(r'[cbr]at', text)
print(results)  # ['cat', 'bat', 'rat']  — fat nahi aaya!

## ------------------------------------------------------------------------##

4 Main Functions Jo Hamesha Use Honge

# re.search() — Pehla match dhundho
pythontext = "Mera number 9876543210 hai"
result = re.search(r'\d{10}', text)

if result:
    print(result.group())  # 9876543210
else:
    print("Nahi mila!")

# re.findall() — Saare matches dhundho
pythontext = "Rahul: 9876543210, Amit: 8765432109"
results = re.findall(r'\d{10}', text)
print(results)  # ['9876543210', '8765432109']

# re.sub() — Dhundho aur Replace karo
pythontext = "Mera number 9876543210 hai"
result = re.sub(r'\d{10}', 'XXXXXXXXXX', text)
print(result)  # Mera number XXXXXXXXXX hai

# re.match() — Sirf Start se match karo
pythontext = "Python best hai"
result = re.match(r'Python', text)  # ✅ Start me hai

text2 = "Mujhe Python pasand hai"
result2 = re.match(r'Python', text2)  # ❌ Start me nahi hai

## ------------------------------------------------------------------------##

Ab Saare Patterns Ek Jagah
Pattern         Matlab              Example
\d              Digit (0-9)         9, 4
\w              Letter ya digit     a, Z, 3 
\s              Space                
.               Koi bhi character   a, !, 9
+               1 ya zyada          \d+ = 123
*               0 ya zyada          \d* = `` ya 123
?               0 ya 1 baar         \d? = `` ya 5
{n}             Exactly n baar      \d{10} = 10 digits
^               String ka start     ^Hello
$               String ka end       bye$
[]              Inme se koi ek      [abc]

