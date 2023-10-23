from re import*

date=input("enter a dob:")

pattern="\d{4}[-]+\d{2}[-]+\d{2}"

matcher=fullmatch(pattern,date)

print("invalid" if matcher==None else "valid")