class Mobiles:
    data=[
        {"id":100,"name":"galaxya5","price":35000},
        {"id":101,"name":"mi11i","price":25000},
        {"id":102,"name":"iphone15","price":135000},
        {"id":103,"name":"s23","price":145000},
        {"id":104,"name":"neo","price":35000},
        ]
    
    def create(self,*args,**kwargs):
        self.data.append(kwargs)
        return kwargs
    
    def retrieve(self,id,*args,**kwargs):
        obj=[m for m in self.data if m.get("id")==id].pop()
        return obj

    def get(self,*args,**kwargs):
        return self.data
    
    def put(self,id,*args,**kwargs):
        obj=[m for m in self.data if m.get("id")==id].pop()
        obj.update(kwargs)
        return obj
    
    def destroy(self,*args,**kwargs):
        id=kwargs.get("id")
        des=[m for m in self.data if m.get("id")==id].pop()
        self.data.remove(des)
        return f"{des} is removed"


obj=Mobiles()
print(obj.create(id=105,name="nothing",price=70000))
print(obj.put(id=104,name="15pro",price=150000))
# print(obj.retrieve(id=101))    
print(obj.destroy(id=101))
print(obj.get())
