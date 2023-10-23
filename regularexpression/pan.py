from re import*

num=input("enter a number:")

pattern="[A-Z]{3}[PCAFHT]{1}[A-Z]{1}[0-9]{4}[A-Z]{1}"

matcher=fullmatch(pattern,num)

print("invalid" if matcher==None else "valid")