data=[
    {"id":1,"name":"harry potter","price":450},
    {"id":2,"name":"spider man","price":200},
    {"id":3,"name":"great minds","price":500},
    {"id":4,"name":"one man show","price":400},
    {"id":5,"name":"trading strategies","price":1000},
]

def create(*args,**kwargs):
    data.append(kwargs)
    return kwargs

def retreive(*args,**kwargs):
    id=kwargs.get("id")
    ret=[book for book in data if book.get("id")==id]
    return ret

def set(*args,**kwargs):
    return data

def destroy(*args,**kwargs):
    id=kwargs.get("id")
    des=[b for b in data if b.get("id")==id].pop()
    data.remove(des)
    return f"{des} is removed"

def put(id,*args,**kwargs):
    obj=[b for b in data if b.get("id")== id].pop()
    obj.update(kwargs)
    return obj

print(put(id=5,name="strategies",price=1200))


create(id=6,name="mans power",price=750)

# print(retreive(id=6))

# print(set())


print(destroy(id=4))
print(set())
















