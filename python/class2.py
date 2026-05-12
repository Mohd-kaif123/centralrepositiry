'''class BankAccount:
    def __init__(self,owner_name,balance):
        self.owner_name=owner_name
        self.balance=balance
    def deposite(self,amount):
        self.balance += amount
        print(f"Account Holder Name: {self.owner_name}")
        print(f"Deposite Amount: {amount}.\nNew Balance: {self.balance}")
    def withdraw(self,amount):
        if amount < self.balance:
            self.balance -= amount
            print(f"Withdraw Ammount : {amount}.\nRemaining Balance: {self.balance}")
        else:
            print("Amount is not Enough")
    def check_balance(self):
        print(f"Current Balance : {self.balance}")

Bank_detail=BankAccount("Kaif",5000)
Bank_detail.deposite(3000)
Bank_detail.withdraw(6000)
Bank_detail.check_balance()'''




class instauser:
    def __init__(self,username,followers):
        self.username=username
        self.followers=followers
    def post_karo(self,captions):
        print(f"{self.username} ne ye post kiya: {captions}")
    def follow(self,otheruser):
        otheruser.followers += 1
        print(f"{self.username} ne follow kiya {otheruser.username}")
        print(f"{otheruser.username} ke ab {otheruser.followers} followers hai ")

user1 = instauser("kaif",100)
user2 = instauser("wais", 200)

user1.post_karo("I am good today")
user1.follow(user2)