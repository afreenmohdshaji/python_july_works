from re import*
mob=input("enter a num:")

pattern="[0-9]{4}[-\s]?[0-9]{4}[-\s]?[0-9]{4}"

matcher=fullmatch(pattern,mob)

print("invalid" if matcher==None else "valid")