#----------- Level-2 Q1) payment -------------#

from abc import ABC, abstractmethod
class payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass
    
class upi(payment):
    def pay(self,amount):
        self.amount=amount
        print(f"Upi se {amount} rupees pay hogae!")
class cash(payment):
    def pay(self,amount):
        self.amount=amount
        print(f"Cash me {amount} pay ho gae!")

a=upi()
a.pay(5000)

b=cash()
b.pay(10000)

#----------- Level-2 Q2) Employee -------------#

from abc import ABC, abstractmethod
class Employee(ABC):
    @abstractmethod
    def kaam_karo(self):
        pass
    def salary_dikhao(self,amount):
        pass
class developer(Employee):
    def kaam_karo(self):
        print("Code likh raha hu!")
    def salary_dikhao(self,amount):
        self.amount=amount
        print(f"Developer salary: {amount}")
class designer(Employee):
    def kaam_karo(self):
        print("Design bana raha hu!")
    def salary_dikhao(self,amount):
        print(f"Designer salary: {amount}")
a1=developer()
a1.kaam_karo()
a1.salary_dikhao(50000)

b1=designer()
b1.kaam_karo()
b1.salary_dikhao(40000)


#----------- Level-2 Q3) Food -------------#

from abc import ABC, abstractmethod

class food(ABC):
    @abstractmethod
    def prepare(self):
        pass
    def serve(self):
        pass
class pizza(food):
    def prepare(self):
        print("Pizza ban raha hai!")
    def serve(self):
        print("Pizza serve ho gaeya!")
class Biryani(food):
    def prepare(self):
        print("Biryani Dum pe chad gai hai")
    def serve(self):
        print("Biryani plate me serve ho gai hai!")
a2=pizza()
a2.prepare()
a2.serve()

b2=Biryani()
b2.prepare()
b2.serve()