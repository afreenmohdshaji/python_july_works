from re import*
num=input("enter your num:")

pattern="[0-9]{4}[-\s]?[0-9]{4}[-\s]?[0-9]{4}"
matcher=fullmatch(pattern,num)
print("invalid" if matcher==None else "valid")
