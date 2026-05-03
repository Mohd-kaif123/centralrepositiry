# Level : 1 --Easy ---Q1) Animal

'''class animal:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def eat(self):
        print(f"{self.name} kha raha hai!")

class dog(animal):
    def bark(self):
        print(f"{self.name} Woof woof! kar raha hai")

Dog1=animal("Tommy","black")
Dog1.eat()

Dog1=dog("Tommy","black")
Dog1.bark()

OutPut :- Tommy kha raha hai!
          Tommy Woof woof! kar raha hai
'''

# Q2) Vehicles

'''class vehicles:
    def __init__(self,brand,speed):
        self.brand=brand
        self.speed=speed
    def move(self):
        print(f"{self.brand} chal raha hai!")
class car(vehicles):
    def ac_chalo(self):
        print ("AC on hai!")

c1=car("TATA","320 km/hr")
c1.move()
c1.ac_chalo()

OutPut :-   TATA chal raha hai!
            AC on hai!
'''


# ---Level 2 ----- #
# Q1) Employee
'''class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def work(self):
        print(f"{self.name} kaam kar raha hai!")  
    
class manager(Employee):
    def meeting(self):
        print(f"{self.name} Meeting kar raha hai!")

class developer(Employee):
    def code_likho(self):
        print(f"{self.name} code likh raha hai")

m1=manager("kaif",50000)
m1.work()
m1.meeting()

e1=developer("Rahul",30000)
e1.work()
e1.code_likho()'''

# ---------Level 3-------#
# Q4) Bank account

class BankAccount:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance

    def deposite(self,amount):
        self.balance+=amount
        print(f"{amount} Deposite succesfully! Total: {self.balance}")
    def withdraw(self,w_amount):
        self.w_amount=w_amount
        if w_amount <= self.balance:
            self.balance -= w_amount
            print(f"{self.w_amount} withdrraw successfully!")
        else:
            print("Balance is not sufficieant")
    def check_balance(self):
        print(f"{self.balance} Available balance!")

class saving(BankAccount):
    def interest(self):
        self.interest = self.balance * 0.10
        self.balance += self.interest
        print(f"10% Interest is added! New Balance: {self.balance}")
class current(BankAccount):
    def overdraft(self,limit):
        self.limit=limit
        print(f"Overdraft limit set to: {self.limit}")

    def o_withdraw(self,amount):
        if self.balance - amount >= -self.limit:
            self.balance -= amount
            print(f"{amount} nikal gaye! New Balance : {self.balance}")
        else:
            print("sorry! limit ke bahar hai ye amount.")

c1=saving("kaif",10000)
c1.deposite(5000)
c1.withdraw(10000)
c1.interest()
c1.check_balance()

c2=current("wais",50000)
c2.deposite(60000)
c2.withdraw(11000)
c2.check_balance()
c2.overdraft(100000)
c2.o_withdraw(110000)