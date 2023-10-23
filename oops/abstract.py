data=[
        {"id":100,"name":"galaxya5","price":35000},
        {"id":101,"name":"mi11i","price":25000},
        {"id":102,"name":"iphone15","price":135000},
        {"id":103,"name":"s23","price":145000},
        {"id":104,"name":"neo","price":35000},
        

    ]

def create(*args,**kwargs):
    data.append(kwargs)
    return kwargs

create(id="105",name="12pro",price=50000)

def retrieve(*args,**kawrgs):
    id=kawrgs.get("id")
    obj=[m for m in data if m.get("id")==id]
    return obj

print(retrieve(id="105"))
