low=int(input("enter a number"))
upp=int(input("enter a number"))
for num in range(low,upp+1):
    if(num%2!=0):
        print(num)