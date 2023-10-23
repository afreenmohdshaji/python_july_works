mobile={"imeu":"APPLERFG","brand":"Apple","Model":"14 PRO","proccessor":"A16","price":135000}

print(mobile["brand"])

if "Model" in mobile:
    print(mobile["Model"])
else:
    print("invalid key")

# mobile["offer"]=12000
# mobile["price"]-=12000
# print(mobile)

mobile["offer"]="15%"

current_price=mobile["price"]

discounted=(current_price/100)*15
print(discounted)
mobile["price"]-=discounted
print(mobile)