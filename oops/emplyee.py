class Employee:
    name:str
    id:int
    dept:str
    salary:int

    def set_employee(self,name,id,dept,salary):
        self.name=name
        self.id=id
        self.dept=dept
        self.salary=salary 

    def display(self):
        print(self.name,self.id,self.dept,self.salary)
    def __str__(self):
        return self.name

emp1=Employee()
emp1.set_employee("afreen",22024,"backend",8000)
emp1.display()
print(emp1)
emp2=Employee()
emp2.set_employee("ummer",11026,"frontend",7900)
emp2.display()
print(emp2)

