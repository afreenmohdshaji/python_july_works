mobiles=[
    {"id":1,"name":"samsungs22","brand":"samsung","varients":[
        {"ram":"8gb","rom":"128gb","price":84000},
        {"ram":"8gb","rom":"256gb","price":100000},

    ]}, 
    {"id":1,"name":"samsungsa52","brand":"samsung","varients":[
        {"ram":"4gb","rom":"128gb","price":54000},
        {"ram":"8gb","rom":"256gb","price":65000},

    ]},
     {"id":1,"name":"one plus nord2","brand":"one plus","varients":[
        {"ram":"8gb","rom":"128gb","price":34000},
        {"ram":"8gb","rom":"256gb","price":45000},

    ]},
     {"id":1,"name":"miii1","brand":"redmi","varients":[
        {"ram":"8gb","rom":"128gb","price":24000},
        {"ram":"8gb","rom":"256gb","price":35000},
        ]},
]

# all_mobiles=[m.get("name") for m in mobiles]
# print(all_mobiles)

# all_brand=[b.get("brand") for b in mobiles]
# print(set(all_brand))

# low_range=[l.get("name")  for l in varients if "price">=20000 and "price"<=40000]
# print(low_range)

# for m in mobiles:
#     for v in m.get("varients"):
#         if v.get("price") in range(20000,40001):
#             print(m.get("name"))

# for m in mobiles:
#     for v in m.get("varients"):
#         if v.get("price")<35000:
#             print(m.get("name"))

# for m in mobiles:
#     for v in m.get("varients"):
#         if v.get("ram")=="4gb":
#             print(m.get("name"))

# for m in mobiles:
#     for v in m.get("varients"):
#         if v.get("price") in range(20000,30001):
#             print(m.get("name"))

# price_fil=[m.get("name") for m in mobiles for v in m.get("varients") if v.get("price") in range(20000,30001)]
# print(price_fil)

# ram_fil=[m.get("name")  for m in mobiles for v in m.get("varients") if v.get("ram")=="4gb"]
# print(ram_fil)

# print([m.get("name") for m in mobiles for v in m.get("varients") if v.get("ram")=="8gb" and v.get("price")<40000])

#  costly=max(mobiles,key=lambda m:[m.get("name") for m in mobiles for v in m.get("varients")])
# print(costly)



costly=max([v.get("price") for m in mobiles for v in m.get("varients")])
print(costly)