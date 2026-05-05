
# Poora Code Ek Saath 
from abc import ABC, abstractmethod   # Tools import karo

class Phone(ABC):                     # Master blueprint — directly use nahi hoga
    
    @abstractmethod                   # Warning tag — "ye likhna ZAROOR hai"
    def call_karo(self):              # Sirf naam — kaam nahi
        pass                          # Khaali


class Samsung(Phone):                 # Samsung, Phone ko follow karega
    def call_karo(self):              # Ab actual kaam likh rahe hain
        print("Samsung se call!")     # Ye hai Samsung ka kaam


class iPhone(Phone):                  # iPhone, Phone ko follow karega
    def call_karo(self):              # iPhone ka apna kaam
        print("iPhone se call!")      # Ye hai iPhone ka kaam


s = Samsung()                         # Samsung ka object
s.call_karo()                         # Samsung se call!

i = iPhone()                          # iPhone ka object
i.call_karo()                         # iPhone se call!