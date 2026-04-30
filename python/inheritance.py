# Level : 1 --Easy ---Q) Animal

class animal:
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

# Q2) Vehicles

class vehicles:
    def __init__(self,brand,speed):
        self.brand=brand
        self.speed=speed
    def move(self):
        print(f"{self.brand} chal raha hai!")
class car(vehicles):
    def ac_chalo(self):
        print ("AC on hai!")

c1=vehicles("TATA","320 km/hr")
c1.move()

c1=car(vehicles)
c1.ac_chalo()


        