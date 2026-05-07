#____________Level-2 Q1) school marks______________#

class student:
    def __init__(self,name,marks):
        self.name=name
        self.__marks=marks
    def get_marks(self):
        return self.name
    def get_name(self):
        return self.__marks
    def set_marks(self):
        if self.__marks>0 and self.__marks<100:
            print(f"{self.name} marks is: {self.__marks}")
        else:
            print("marks is Invalid")
    def grade(self):
        if self.__marks>90:
            print("Grade: A")
        elif self.__marks>70:
            print("Grade: B")
        elif self.__marks>50:
            print("Grade: C")
        else:
            print("Fail")
m=student("kaif",-10)
#print(m.get_name())
#print(m.get_marks())
m.set_marks()
m.grade()

#____________Level-2 Q2) swiggy wallet______________#

class wallet:
    def __init__(self,owner,balance):
        self.owner=owner
        self.__balance=balance
    def add_money(self,amount):
        self.amount=amount
        if self.amount>0:
            self.amount += self.__balance
            print(f"{amount} Added in you Account successfully!")
            print (f"New Balance: {self.amount}")
        else:
            print("Amount is Invalid!")
    def pay(self,p_amount):
        self.p_amount=p_amount
        if self.__balance>=p_amount:
            self.__balance-=p_amount
            print(f"{p_amount} Transfer successfully!")
        else:
            print("Sufficiant Balance is not present")
    def get_current(self):
        return self.__balance
    
b=wallet("wais",5000)
b.add_money(20000)
b.pay(10000)
print(f"Current Balance: {b.get_current()}")