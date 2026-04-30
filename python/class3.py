
# This method is good for industry level using multiple class is good
class customer:
    def __init__(self,name,address):
        self.name=name
        self.address=address
class Restaurant:
    def __init__(self,name,menu_items):
        self.name=name
        self.menu_items=menu_items

# Order class (uper ki dono class ko use karegi customer aur restaurant ko)        
class order:
    def __init__(self,customer_obj,restaurant_obj):
        self.customer=customer_obj  # ye pora custommer object hai uper wala
        self.restaurant=restaurant_obj  # ye pora restaurant object hai uper wala
    def place_order(self):
        print(f"{self.customer.name} ne {self.restaurant.name} se {self.restaurant.menu_items} order kiya - {self.customer.address} pe aayega")

#---- Use kaise kare----

# Pehle objects banao
c1=customer("kaif","mumbai")
r1=Restaurant("Dominos","pizza")

# Ab order class ko ye object pass karo
my_order=order(c1, r1)
my_order.place_order()

# ye short cut Real life  industry ke liye sahi nahi hai 
class order:
    def __init__(self,name,add,Rest_name,menu_items):
        self.name=name
        self.add=add
        self.Rest_name=Rest_name
        self.menu_items=menu_items
    def place_order(self):
        print(f"{self.name} ne {self.Rest_name} se {self.menu_items} order kiya - {self.add} pe aayega!")

myorder=order("kaif","mumbai","dominos","pizza")
myorder.place_order()

