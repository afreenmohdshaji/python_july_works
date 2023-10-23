from re import*

gmail=input("enter your gmail:")

# pattern="[a-z0-9_]+@(gmail|live).com"
pattern="[a-z0-9_]+@[a-z]{2,}.com"


matcher=fullmatch(pattern,gmail)

print("invalid" if matcher==None else "valid")