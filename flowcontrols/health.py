gender="female"
tummy_size=80
buttock_size=75
value=tummy_size/buttock_size
print(value)
if(gender=="female"):
    if(value<=0.80):
        print(f"{value}, your health risk is low")
    elif(value>=0.80 and value<0.85):
        print(f"{value}, your health risk is moderate")
    else:
        print(f"{value}, your health risk is high")
if(gender=="male"):
    if(value<=0.95):
        print(f"{value}, your health risk is low")
    elif(value>=0.95 and value<1.0):
        print(f"{value}, your health risk is moderate")
    else:
        print(f"{value}, your health risk is high")        