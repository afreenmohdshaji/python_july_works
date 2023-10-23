cakes=[{"id":1,"name":"bluberry","shapes":["round","square","heart"],"varient":[
        {"weight":"0.5kg","price":350},
        {"weight":"1kg","price":500},
        {"weight":"1.5kg","price":700},
        ]},

     {"id":2,"name":"black forest","shapes":["round","square","heart"],"varient":[   
        {"weight":"0.5kg","price":400},
        {"weight":"1kg","price":500},
        {"weight":"1.5kg","price":800},
    ]},

     {"id":3,"name":"red velvet","shapes":["round","square","heart"],"varient":[   
        {"weight":"0.5kg","price":500},
        {"weight":"1kg","price":900},
        {"weight":"1.5kg","price":1200},
    ]},

     {"id":4,"name":"dream cake","shapes":["round","square","heart"],"varient":[   
        {"weight":"0.5kg","price":700},
        {"weight":"1kg","price":1200},
        {"weight":"1.5kg","price":1800},
    ]}]


expensive=max([v.get("price") for c in cakes for v in c.get("varient") ])
print(expensive)

all_shapes=[c.get("shapes")for c in cakes]
print(all_shapes)

for c in cakes:
    if c.get("name")=="dream cake":
        for v in c.get("varient"):
            if v.get("weight")=="1kg":
                print(v.get("price"))

f=[v.get("price") for c in cakes if c.get("name")=="dream cake" for v in c.get("varient") if v.get("weight")=="1kg"]
print(f)

f=[c.get("id") for c in cakes]
print(f)

cheap_cake=min(cakes,key=lambda c:[c.get("name")  for c in cakes for v in c.get("varient")])
print(cheap_cake)

f=[c.get("name") for c in cakes for v in c.get("varient") if v.get("price") in range(300,700)]
print(set(f))

f=[c.get("name") for c in cakes for v in c.get("varient") if v.get("price")<500]
print(f)

f=[c.get("name") for c in cakes for v in c.get("varient") if v.get("weight")<"1kg"]
print(f)