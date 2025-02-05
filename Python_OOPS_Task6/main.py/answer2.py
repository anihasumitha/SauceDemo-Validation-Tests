class Employee: #main class
    def __init__(self,name,base_salary):
        self.__name=name #private
        self.__base_salary=base_salary #private
        pass

    def cal_salary(self):
        return self.__base_salary
    def get_base_salary(self):
        return self.__base_salary
    
class RegularEmployee(Employee): #child class
    def __init__(self, name, base_salary,overtime_pay):
        super().__init__(name, base_salary)
        self.overtime_pay= overtime_pay
    def cal_salary(self): #calculating salary for regular employee
        regularemployee_salary=self.get_base_salary()+self.overtime_pay
        return regularemployee_salary


class ContractEmployee(Employee): #subclass called contractemployee with inherited properties from Employee
    def __init__(self, name,base_salary,hourly_wage, hours_worked):
        super().__init__(name,base_salary) #inhertiance from parent class
        self.hourly_wage=hourly_wage
        self.hours_worked=hours_worked
    def cal_salary(self): #calculating salary for contract employee
        contractemployee_salary=self.hourly_wage*self.hours_worked
        return contractemployee_salary   


class Manager(Employee): #subclass called manager with inherited properties from Employee
    def __init__(self, name, base_salary,bonus,):
        super().__init__(name, base_salary) #inhertiance from parent class
        self.bonus=bonus
    def cal_salary(self): #calculating salary for manager
        manager_salary=self.get_base_salary()+self.bonus
        return manager_salary
    

#Testing the classes

emp=Employee("Aniha",20000) #main class 

reg_employee=RegularEmployee("Casey",20000,5000) #prints regular employee salary
print("Regular Employee Salary:",reg_employee.cal_salary())

contract_employee = ContractEmployee("Jordan",0,500,40)  # Base salary can be 0 or not needed for contract employee
print("Contract Employee Salary:", contract_employee.cal_salary()) #prints contract employee salary

manager = Manager("Alisha", 30000, 7000)
print("Manager Salary:", manager.cal_salary()) #prints managers salary