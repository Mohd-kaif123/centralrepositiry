#____________Level-3 Q1) Employee______________#
'''
class Employee:
    def __init__(self,name,salary,dept):
        self.__name=name
        self.__salary=salary
        self.__dept=dept
    def get_name(self):
        return self.__name
    def get_salary(self):
        return self.__salary
    def get_dept(self):
        self.__dept
    def set_salary(self,n_salary):
        if self.__salary>0 and self.__salary< 500000:
            self.__salary = n_salary
            print(f"salary set to: {self.__salary}")
        else:
            print("Invalid salary! Limit: 0 to 5 lakh")
    def appraisal(self,percent):
        raise_amount=(self.__salary * percent) / 100 
        temp_salary = self.__salary + raise_amount

        if temp_salary <= 500000:
            self.__salary = temp_salary
            print(f"Appraisal Successful! New Salary: {self.__salary}")
        else:
            print("Appraisal successful: salary cannot exceed 5 lakh.")
    def details(self):
        print(f"Name: {self.__name} | Dept: {self.__dept} | salary: {self.__salary}")
emp=Employee("kaif",400000,"DevOps")        
emp.set_salary(300000)
emp.appraisal(6)
emp.details()
'''

class Employee:
    def __init__(self,name,salary,dept):
        self.__name=name
        self.__salary=salary
        self.__dept=dept
    def get_name(self):
        return self.__name
    def get_salary(self):
        return self.__salary
    def get_dept(self):
        return self.__dept
    def set_s(self,n_salary):
        self.__salary=n_salary
        if self.__salary>0 and self.__salary<500000:
            print(f"Salary set to: {n_salary}")
        else:
            print("Salary is Invalid")
    def appraisal(self,percent):
        temp_s=(self.__salary * percent )/100
        new_salary = self.__salary + temp_s
        if new_salary <=500000:
            self.__salary=new_salary
            print(f"Appraisal successfull!\nNew salary: {self.__salary}")
        else:
            print("Appraisal Failed: Salary cannot exceed 5 lakh.")
    def details(self):
        #print(f"Updated salary: {self.__salary}")
        print(f"Name: {self.__name}\nDepartment: {self.__dept}\nSalary:{self.__salary}")

e1=Employee("sahil",320000,"software")
#e1.set_s(300000)
e1.appraisal(6)
e1.details()

#____________Level-3 Q2) Instagram______________#
class User:
    def __init__(self,username,private=True):
        self.__username=username
        self.__followers=0
        self.__private=private
    def request(self,other_user):
        if other_user.__private:
            print(f"Request send to {self.__username}")
        #elif self.__private == False:
         #   self.__followers+=1
          #  print("other user followed successfully")
        else:
            other_user.__followers +=1
            print(f"Direct follow successfully! {other_user.__username} has now {other_user.__followers} followers.")
    def get_followers(self):
        return self.__followers

class Adminuser(User):
    def __init__(self,username):
        super().__init__(username, private=True)

    def force_unfollow(self,user):
        if user._User__followers > 0:
            user._User__followers -= 1
            print(f"Admin Action: {user._User__username} ka follower ghata diya gaya.")
        else:
            print("pehle se 0 followers hai!")
u1=User("sahil",private=True)
u2=User("kaif",private=False)
admin = Adminuser("superman")

admin.request(u1)
admin.request(u2)

admin.force_unfollow(u2)
