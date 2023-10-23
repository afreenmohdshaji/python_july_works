from re import*

varname=input("enter a varible")

pattern="[k-n][369][a-zA-z0-9]*"

matcher=fullmatch(pattern,varname)

if matcher==None:
    print("invalid")
else:
    print("valid")