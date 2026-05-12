############################################################################
Pehle Naam Samjho
Poly = Many (bahut saare)
Morph = Forms (roop)
Polymorphism = Ek cheez — bahut saare roop

Real Life Se Samjho 🎭
Socho tumhara ek dost hai — Rahul

Ghar pe → Beta hai (maa baap se seedha baat karta hai)
College me → Dost hai (yaar log se masti karta hai)
Office me → Employee hai (sir sir karta hai 😄)

Rahul ek hi insaan hai — lekin situation ke hisaab se alag alag behave karta hai!
Yahi hai Polymorphism — same naam, alag alag kaam!

############################################################################

Code Me Polymorphism Kaise Hota Hai?
Python me Polymorphism 2 tarike se hota hai:
1. Same method — alag alag classes me alag kaam kare
2. Same method — child class me override kare (baad me sikhenge)

Type 1 — Same Method, Alag Alag Classes
class Dog:
    def sound(self):
        print("Dog bolta hai — Bhow Bhow! 🐶")

class Cat:
    def sound(self):
        print("Cat bolti hai — Meow Meow! 🐱")

class Cow:
    def sound(self):
        print("Cow bolti hai — Moo Moo! 🐄")
Teen alag classes — teeno me same method naam sound() — lekin kaam alag alag!
dog = Dog()
cat = Cat()
cow = Cow()

dog.sound()   # Dog bolta hai — Bhow Bhow! 🐶
cat.sound()   # Cat bolti hai — Meow Meow! 🐱
cow.sound()   # Cow bolti hai — Moo Moo! 🐄


Aur Bhi Powerful — List me Daalo!
animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal.sound()

# Dog bolta hai — Bhow Bhow! 🐶
# Cat bolti hai — Meow Meow! 🐱
# Cow bolti hai — Moo Moo! 🐄
Ek hi loop — automatically sab sahi sahi print ho gaya!
Python ko pata hai ki kaun sa object hai — aur uske hisaab se sahi sound() chalata hai.

############################################################################

Real Life App Example — Swiggy Payment 💳
Swiggy me payment ke kai tarike hain — UPI, Card, Cash. Teeno ka kaam same hai — payment karna — lekin process alag alag!
pythonclass UPI:
    def payment_karo(self, amount):
        print(f"UPI se {amount} rupaye pay kiye! ✅")

class Card:
    def payment_karo(self, amount):
        print(f"Card se {amount} rupaye pay kiye! ✅")

class Cash:
    def payment_karo(self, amount):
        print(f"Cash me {amount} rupaye pay kiye! ✅")
python# Customer ne UPI choose kiya
payment = UPI()
payment.payment_karo(250)   # UPI se 250 rupaye pay kiye! ✅

# Doosre customer ne Card choose kiya
payment = Card()
payment.payment_karo(500)   # Card se 500 rupaye pay kiye! ✅
Method naam same — payment_karo() — kaam alag! Yahi Polymorphism hai!

Ek Line Me Yaad Rakho 🎯

Same method naam — alag alag classes — alag alag kaam
Jaise "Khana" — Rahul khana khata hai, Dog khana khata hai, Cat khana khati hai — kaam same, tarika alag! 🍕🦴🐟

