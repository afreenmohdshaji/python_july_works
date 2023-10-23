from re import*
mob_num=input("enter your num")

pattern="(91)?[0-9]{10}"

matcher=fullmatch(pattern,mob_num)

print("invalid" if matcher==None else "valid")