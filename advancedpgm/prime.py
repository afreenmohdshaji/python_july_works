num=int(input("enter a number"))

prime=[num%n==0 for n in range(2,num)]
print("prime" if any(prime)==False else "not prime")