class Employee:

    def __init__(self,name,salary,dept):
        self.name=name
        self.salary=salary
        self.dept=dept
    @property
    def set_name(self):
        return self.name
    def __str__(self):
        return self.name
    @property
    def set_salary(self):
        return self.salary
    
emp=Employee("afreen",2500,"IT")
print(emp.set_name)
print(emp.set_salary)
print(emp)