class Student():
    rol:int
    course:str
    total:int

    def __init__(self,rolnum,course,total):
        self.rol=rolnum
        self.course=course
        self.total=total
    
    def display(self):
        print(self.rol,self.course,self.total)

st1=Student(12,"django",300)
st1.display()