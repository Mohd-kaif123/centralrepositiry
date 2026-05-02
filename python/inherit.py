class vehicles:
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