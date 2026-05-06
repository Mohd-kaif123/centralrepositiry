
#----------- Level-3 Q1) Food -------------#

'''from abc import ABC, abstractmethod

class foodapp(ABC):
    @abstractmethod
    def order_karo(self,dish):
        pass
    def cancel_karo(self):
        pass
    def track_karo(self):
        pass

class swiggy(foodapp):
    def order_karo(self, dish):
        self.dish=dish
        print(f"swiggy se kaif ne {dish} order kiya")
    def cancel_karo(self):
        print("Order cancel hogaeya")
    def track_karo(self):
        print("10 mint me deliver hojaega")
class zomato(foodapp):
    def order_karo(self, dish,name):
        self.name=name
        print(f"{name} ne {dish} order kiya hai")
    def track_karo(self,distance):
        print(f"Order abhi {distance} duur hai")
    def cancel_karo(self,feedback,name,dish):
        self.feedback=feedback
        print(f"{name} ne {dish} order cancel kardiya,\nReason: {feedback}")

a=swiggy()
a.order_karo("biryani")
a.cancel_karo()
a.track_karo()

b=zomato()
b.order_karo("Motton gosh","kaif")
b.track_karo("2km")
b.cancel_karo("bahut late ho raha hai aur mere pass time nahi hai","kaif","motton gosh")
'''

#----------- Level-3 Q2) Food -------------#
'''
from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    @abstractmethod
    def deposite(self,d_amount):
        pass
    def withdraw(self,w_amount):
        pass
    def balance_av(self):
        pass

class s_account(BankAccount):
    def deposite(self, d_amount):
        self.balance+=d_amount
        print(f"Deposite Amount: {d_amount}")
        print(f"New Balance: {self.balance}")
        #self.balance+=amount
    def withdraw(self, w_amount):
        if self.balance>w_amount:
            self.balance-=w_amount
            print(f"Withdrawn Amount: {w_amount}")
        else:
            print("Balance is not sufficiant")
    def balance_av(self):
        print(f"Current Balance: {self.balance}")

class c_account(BankAccount):
    def deposite(self, d_amount):
        self.balance+=d_amount
        print(f"Deposite Amount: {d_amount}")
        print(f"New Balance: {self.balance}")
    def withdraw(self, w_amount):
        if self.balance>w_amount:
            self.balance-=w_amount
            print(f"Withdraw Ammount: {w_amount}")
        else:
            print("Sufficiant Balance is not present")
    def balance_av(self):
        print(f"Current Balance: {self.balance}")


a1=s_account("kaif",50000)
a1.deposite(5000)
a1.withdraw(30000)
a1.balance_av()

b1=c_account("wais",10000)
b1.deposite(5000)
b1.withdraw(8000)
b1.balance_av()
'''


#----------- Level-3 Q3) Game Character -------------#
'''from abc import ABC, abstractmethod
class Game(ABC):

    @abstractmethod
    def attack(self):
        pass
    def defend(self):
        pass
    def s_power(self):
        pass

class warrior(Game):
    def attack(self):
        print("warrior ne Talwar se wizard per attack kiya -50HP kam hogai")'''