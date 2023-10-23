num=int(input("enter a number"))
i=1
out=0
sum=0
while(i<=num):
    out=out*10+num
    sum=sum+out
    print(out)
    i+=1
print(sum)    