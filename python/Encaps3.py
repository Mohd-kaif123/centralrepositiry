#____________Level-3 Q1) Employee______________#

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