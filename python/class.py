# yeha print karo Webserver at 198.162.1.10 is running
'''class server:
    def __init__(self, name,ip):
        self.name = name
        self.ip = ip
    def status(self):
        print(f"{self.name} at {self.ip} is running")

web_server = server("Webserver","198.162.1.10")
web_server.status()'''

# Yeha per bhi wahi print karo but with subnet mask
'''class server:
    def __init__(self,name,ip,subnet):
        self.name=name
        self.ip=ip
        self.subnet=subnet
    
    def curent_status(self):
        print(f"{self.name} is running.....")
        print(f"{self.name} IP Address and subnet is {self.ip}\n{self.subnet}")
webserver=server("webserver","198.162.121","255.255.255.0")    
webserver.curent_status()'''

# print karna hai name roll no. aur marks
'''class student:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
    def introduction(self):
        print(f"mera naam {self.name} hai, mera roll no. {self.roll_no}")
        if self.marks>=40:
            print("Pass")
        else:
            print("Fail")

Details=student("kaif",21,45)
Details.introduction()'''


# 3 alag alg car bano

class car:
    def __init__(self,brand,color,speed):
        self.brand=brand
        self.color=color
        self.speed=speed

    def details(self):
        print(f"brand name hai {self.brand}")
        print(f"car ka color hai {self.color}")
        print(f"car ki speed hai {self.speed}")
    
    def honk(self):
        print(f"{self.brand} -- Beep Beep!")
print("####################################")
cars_detail=car("bukati","Black","280km/hr")
cars_detail.details()
cars_detail.honk()
print("####################################")
cars_detail=car("lemborgini","White","300Km/hr")
cars_detail.details()
cars_detail.honk()

