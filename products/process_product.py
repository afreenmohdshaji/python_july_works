from json import load

path="C:\\Users\\afisr\\Desktop\\july_pythonworks\\products\\products.json"

with open(path,encoding="utf-8") as f:
    data=load(f)

# print(len(data))

all_category={c.get("category") for c in data}
# print(all_category)

all_electronics={e.get("title")  for e in data if e.get("category")=="electronics"}

# print(all_electronics)

top_rated=max(data,key=lambda rd:float(rd.get("rating").get("rate")))

# print(top_rated.get("title"))

women_cloth=[c.get("title") for c in data if c.get("category")=="women's clothing" and c.get("price")>20 and c.get("price")<=30]
print(women_cloth)

# for c in data:
#     if c.get("price") in range(100,301) and c.get("category")=="women's clothing":
#         print(c)


most_count=max(data,key=lambda c:c.get("rating").get("count"))
# print(most_count.get("title"))

# jwel=[c.get("title") for c in data if c.get("category")=="jewelery"  for r in c.get("rating") if r.get("rate")>3]
# print(jwel)

wc={}
for p in data:
    category=p.get("category")
    if category not in wc:
        wc[category]=1
    else:
        wc[category]+=1
# print(wc)

keyval=([v,k] for k,v in wc.items())
# print(min(keyval))


# srt_item=sorted(data,reverse=True,key=lambda s:s.get("price"))
# for s in srt_item:
#     print(s.get("title"))

# jewel=[]

for j in data:
    if j.get("category")=="jewelery":
        # for r in j.get("rating"):
            if j.get("rating")["rate"]>3:
                 print(j.get("title"))
           
            


            