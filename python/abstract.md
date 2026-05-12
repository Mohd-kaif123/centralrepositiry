# 1. ABC aur abstractmethod kya hai?
from abc import ABC, abstractmethod
             ^^^
      Abstract Base Class
      Python ka built-in tool hai Abstraction ke liye
      Ye import karna padta hai — tabhi Abstraction kaam karega.
      from abc        →  Python ke ek special dabba hai jiska naam "abc" hai
      import ABC      →  Us dabbe se "ABC" nikalo
      import abstractmethod  →  Us dabbe se "abstractmethod" bhi nikalo

# 2. Abstract Class kya hai?
pythonclass Phone(ABC):     # Ye ek BLUEPRINT ka bhi BLUEPRINT hai
    pass

Phone directly use nahi ho sakta
Ye sirf batata hai ki "jo bhi mujhse banega, uske paas ye kaam hona chahiye"
Isko "incomplete class" bhi keh sakte ho

pythonp = Phone()    # ❌ ERROR aayega — directly object nahi bana sakte!

# 3. Abstract Method
python@abstractmethod
def call_karo(self):
    pass
Ye 3 cheezein hain — ek ek samjho:
@abstractmethod — ye ek warning tag hai:
@abstractmethod  →  "Ye method ZAROOR likhna hoga jo bhi inherit kare"
                     "Bhool gaya toh ERROR!"
def call_karo(self): — sirf naam diya hai:
Ye bol raha hai →  "Ek kaam hoga jiska naam call_karo hai"
                   "Lekin kaam KAISE hoga — abhi nahi bataunga"
pass — matlab "khaali chhoddo":
pass  →  "Andar kuch mat likho — ye sirf placeholder hai"
Real life me:
Job description me likha:
"Developer ko coding karni hogi"   ← @abstractmethod

Actual developer ne bataya:
"Main Python me coding karunga"    ← Child class me define karna


# 4.  Child Class
pythonclass Samsung(Phone):
    def call_karo(self):
        print("Samsung se call ho rahi hai!")
class Samsung(Phone)  →  "Samsung, Phone ka blueprint follow karega"
def call_karo(self)   →  "Ab KAISE karna hai — ye main bata raha hu"
print(...)            →  "Ye hai actual kaam"
Ab Samsung ne call_karo() define kar diya — error nahi aayega!


Ek Table Me Poora Structure
CheezKya HaiKyu Use Kartefrom abc import...Tools lanaBina iske kaam nahiclass Phone(ABC)Master blueprintDirect use band karna@abstractmethodWarning tagBhoolne pe error denapassKhaali jagahKaam baad me likha jaayegaclass Samsung(Phone)Actual classAsli kaam yahan hoga

Ek Line Summary 🎯
Phone(ABC)       →  "Ye kaam karna PADEGA" — rule set kiya
@abstractmethod  →  "Bhool gaya toh ERROR" — rule enforce kiya  
Samsung(Phone)   →  "Theek hai, ye raha actual kaam" — rule follow kiya

