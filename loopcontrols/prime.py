num=int(input("enter a number"))
prime=True
for i in range(2,num):
    if(num%i==0):
        prime=False
        break
if(prime==True):
    print(f"{num} is prime")
else:
    print(f"{num} is not prime")        