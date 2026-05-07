#______________LEVEL-1 Q1)______________#

class car:
    def move(self):
        print("car chal rahi hai -- Vroom Vroom!")
class Bike:
    def move(self):
        print("Bike chal rahi hai-- phat phta!")
class Bus:
    def move(self):
        print("Bus chal rahi hai -- Dharam Dharam!")

gadi = [car(), Bike(), Bus()]

for gadiya in gadi:
    gadiya.move()


#______________LEVEL-1 Q2)______________#

class circle:
    def draw(self):
        print("Circle draw ho raha hai!")
class square:
    def draw(self):
        print("Box draw ho raha hai!")
class Triangle:
    def draw(self):
        print("Triangle draw ho raha hai!")

geometry = [circle(), square(), Triangle()]
for geom in geometry:
    geom.draw()