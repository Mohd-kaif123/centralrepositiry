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

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def work(self):
        print(f"{self.name} work kar raha hai!")

class manager(Employee):
    def meeting(self):
        print("Meeting chal rahi hai!")

class developer(Employee):
    def code_likho(self):
        print(f"{self.name} code likh raha hai!")

m1=manager("kaif",50000)
m1.work()
m1.meeting()

emp=developer("Rahul", 30000)
emp.work()
emp.code_likho()