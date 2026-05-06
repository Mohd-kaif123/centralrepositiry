Encapsulation — Ek Dum Real Life Se
Pehle Ek Scene Socho 🏧
Tu ATM pe gaya — card daala, PIN daala, paisa nikala.
Lekin kya tune ye kiya?

Bank ka database khola? ❌
Apna balance directly change kiya? ❌
Server se connect kiya? ❌

Nahi! Tu sirf buttons dabata hai — baaki sab ATM ne andar andar kar diya.

Ye hi hai Encapsulation — Andar ki cheezein chupaao, bahar sirf buttons do!

________________________________________________________________________

Ab Code Me Samjho
Pehle Bina Encapsulation Ke — Khatarnak! ☠️

# pythonclass BankAccount:
    def __init__(self, naam, balance):
        self.naam = naam
        self.balance = balance  # Seedha access possible!

# account = BankAccount("Rahul", 10000)

# Koi bhi directly balance change kar sakta hai!
account.balance = 999999999  # 😱 Koi bhi kar sakta hai ye!
print(account.balance)       # 999999999

________________________________________________________________________

# Ab Encapsulation Ke Saath — Safe! 🔒
pythonclass BankAccount:
    def __init__(self, naam, balance):
        self.naam = naam
        self.__balance = balance  # __ (double underscore) = PRIVATE!
                                  # Ab bahar se koi directly access nahi kar sakta!

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} jama hua! New balance: {self.__balance}")
        else:
            print("Amount sahi nahi hai!")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Balance kam hai!")
        else:
            self.__balance -= amount
            print(f"{amount} nikala! New balance: {self.__balance}")

    def check_balance(self):
        print(f"Tera balance hai: {self.__balance}")


account = BankAccount("Rahul", 10000)

# Direct access karne ki koshish karo
account.__balance = 999999  # ❌ Ye kaam nahi karega!

# Sirf inhi methods se kaam hoga
account.deposit(5000)       # 5000 jama hua! New balance: 15000
account.withdraw(2000)      # 2000 nikala! New balance: 13000
account.check_balance()     # Tera balance hai: 13000

________________________________________________________________________

# __ Double Underscore Ka Matlab
pythonself.naam       # Public   — koi bhi access kar sakta hai
self.__balance  # Private  — sirf class ke andar se access hoga

________________________________________________________________________

Getters aur Setters — Balance Safely Dekhna aur Badalna
Kabhi kabhi tumhe private variable dekhna ya change karna hota hai — lekin safely. Iske liye getter aur setter use karte hain:
# pythonclass Student:
    def __init__(self, naam, marks):
        self.naam = naam
        self.__marks = marks      # Private

    # GETTER — sirf dekhne ke liye
    def get_marks(self):
        return self.__marks

    # SETTER — safely change karne ke liye
    def set_marks(self, new_marks):
        if new_marks < 0 or new_marks > 100:
            print("Galat marks hai bhai!")
        else:
            self.__marks = new_marks
            print(f"Marks update ho gaye: {self.__marks}")


s1 = Student("Amit", 85)

print(s1.get_marks())    # 85 — getter se dekha
s1.set_marks(95)         # Marks update ho gaye: 95
s1.set_marks(150)        # Galat marks hai bhai! — setter ne roka

# Setter ka fayda — galat value andar jaane se roka! Seedha __marks change karte toh koi bhi 150 ya -5 daal deta!

________________________________________________________________________

Encapsulation Kyu Use Karte Hain? — 3 Reasons
1. SAFETY 🔒
   Private data ko bahar se protect karna
   Jaise bank ka safe — seedha haath nahi daal sakte

2. CONTROL 🎮
   Data change karne se pehle check karna
   Jaise setter me condition lagayi — 150 marks allowed nahi

3. SIMPLICITY 😌
   User ko andar ki complexity nahi dikhani
   Jaise car chalate ho — engine nahi samajhna padta

________________________________________________________________________

