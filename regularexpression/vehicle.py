from re import*

veh=input("enter a number")

pattern="(KL)[-\s]?[0-9]{2}[-\s]?[A-Z]{1,2}[-\s]?[0-9]{4}"

matcher=fullmatch(pattern,veh)

print("invalid" if matcher==None else "valid")