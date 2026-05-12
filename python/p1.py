'''class bankaccount:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    def deposite(self,amount):
        self.balance+=amount
        print(f"{amount} Deposite successfully. New Balance is : {self.balance}")
    def withdraw(self,w_amount):
        self.w_amount=w_amount
        if self.balance>w_amount:
            self.balance-=w_amount            
            print(f"Withdraw successfully : {w_amount} ")
        else:
            print("Balance is insufficient")
    def c_balance(self):
        print(f"Available Balance: {self.balance}")

class s_account(bankaccount):
    def interest_add(self):
        self.interest_add=self.balance*0.10
        self.balance+=self.interest_add
        print(f"Balance with Interest: {self.balance}")
class c_account(bankaccount):
    def overdruft(self, limit):
        self.limit=limit
        print(f"Over draft limit set to : {self.limit}")
    def withdraw(self,W_amount):
        self.W_amount=W_amount
        if self.W_amount<self.limit:
            self.balance-=self.W_amount
            print(f"Amount Withdraw sucessfully: {self.W_amount}")
        else:
            print("Anount is over to limit")

s1=s_account("Kaif",50000)
s1.deposite(30000)
s1.withdraw(60000)
s1.interest_add()
s1.c_balance()

c1=c_account("Wais",100000)
c1.deposite(50000)
c1.overdruft(100000)
c1.withdraw(60000)
c1.c_balance()
'''

# Q) Bankaccount problem using abstraction
from abc import ABC, abstractmethod
class Bank(ABC):
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    @abstractmethod
    def deposite(self,amount):
        pass
    def withdraw(self,amount):
        pass
    def balance_P(self):
        pass
class s_account(Bank):
    def deposite(self,amount):
        self.balance+=amount
        print(f"Deposite Ammount: {amount}")
        print(f"New Balance: {self.balance}")
    def withdraw(self,amount):
        if self.balance>amount:
            self.balance-=amount
            print(f"Withdraw Ammount: {amount}")
        else:
            print("Balance is not enough")
    def balance_p(self):
        print(f"Current Balance: {self.balance}")

a=s_account("kaif",5000)
a.deposite(5000)
a.withdraw(8000)
a.balance_p()