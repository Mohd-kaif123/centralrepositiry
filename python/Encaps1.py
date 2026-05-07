#____________Level-1 Q1) marks______________#
'''
class Student:
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

#____________Level-1 Q2) patient______________#

class patient:
    def __init__(self,name,Age,disease):
        self.__name=name
        self.__Age=Age
        self.__disease=disease
    def get_name(self):
        return self.__name
    def get_Age(self):
        return self.__Age
    def get_desease(self):
        return self.__disease
    def set_disease(self,n_disease):
        if n_disease !="":
            self.__disease=n_disease
            print(f"Desease update ho gayi: {n_disease}")
        else:
            print("Desease space khali nahi ho sakti")
           
a1=patient("rajan",60,"bawasir")
print(a1.get_name())
print(a1.get_Age())
print(a1.get_desease())
a1.set_disease("Maleria")
'''

#____________Level-1 Q3) patient______________#

class phone:
    def __init__(self,owner,pin):
        self.__owner=owner
        self.__pin=pin
    def unlock(self,Input_pin):
        if self.__pin==Input_pin:
            print("Phone Unlocked!")
        else:
            print("wrong pin!")
    def change_pin(self,old_pin,new_pin):
        if old_pin==self.__pin:
            old_pin==new_pin
            print("Password changed sucessfully!")
        else:
            print("Password wrong")
    
my=phone("kaif",123)
my.unlock(129)
my.change_pin(123, 546)