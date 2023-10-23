from json import load

path=("C:/Users/afisr/Desktop/july_pythonworks/countries/data.json")
with open(path,encoding="utf-8") as f:
    data=load(f)

# print(len(data))

all_regions={r.get("region") for r in data}
# print(all_regions)

asian_count=[a.get("name") for a in data if a.get("region")=="Asia"]
# print(asian_count)

independent_country=[i.get("name") for i in data if i.get("independent")==True]
# print(independent_country)

high_popu=max(data,key=lambda p:p.get("population"))
# print(high_popu.get("name"))

indian_border=[c.get("borders") for c in data if c.get("name")=="India"  ]
# print(indian_border)

# cp={}

# for c in data:
#     c_name=c.get("name")
#     c_capital=c.get("capital")
#     cp[c_name]=c_capital

# print(cp)
    
pop=sum(r.get("population") for r in data if r.get("region")=="Asia")
# print(pop)

cp={}

for r in data:
    if r.get("region")=="Asia":
        c_name=r.get("name")
        c_pop=r.get("population")
        cp[c_name]=c_pop

print(cp)
