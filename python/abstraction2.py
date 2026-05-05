# ------ Level-1 Q1) Vehivle--------#
from abc import ABC, abstractmethod

class vehicle(ABC):

    @abstractmethod
    def start_karo(self):
        pass
class car(vehicle):
    def start_karo(self):
        print("car start hui -- vroom vroom!")

class Bike(vehicle):
    def start_karo(self):
        print("Bike start hogai !")

vic=car()
vic.start_karo()

bik=Bike()
bik.start_karo()   

# ------ Level-1 Q2) Animal--------#

from abc import ABC, abstractmethod
class animal(ABC):
    @abstractmethod
    def awaaz(self):
        pass

class Dog(animal):
    def awaaz(self):
        print("Bhow Bhow!")

class cat(animal):
    def awaaz(self):
        print("Meow Meow!")

class cow(animal):
    def awaaz(self):
        print("Bhee!")

a=Dog()
a.awaaz()

b=cat()
b.awaaz()

c=cow()
c.awaaz()

# ------ Level-1 Q3) Shape--------#

from abc import ABC, abstractmethod

@abstractmethod
class shape(ABC):
    def describe(self):
        pass

class circle(shape):
    def describe(self):
        print("mai ek circle hu")

class square(shape):
    def describe(self):
        print("Mai ek square hu!")

a1=circle()
a1.describe()

b1=square()
b1.describe()


