'''class server:
    def __init__(self, name,ip):
        self.name = name
        self.ip = ip
    def status(self):
        print(f"{self.name} at {self.ip} is running")

web_server = server("Webserver","198.162.1.10")
web_server.status()'''









class server:
    def __init__(self,name,ip,subnet):
        self.name=name
        self.ip=ip
        self.subnet=subnet
    
    def curent_status(self):
        print(f"{self.name} is running.....")
        print(f"{self.name} IP Address and subnet is {self.ip}\n{self.subnet}")
webserver=server("webserver","198.162.121","255.255.255.0")    
webserver.curent_status()
