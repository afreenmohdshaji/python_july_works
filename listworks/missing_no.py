lst=[1,5,6]

limit=len(lst)-1

i=0
while(i<limit):
    j=i+1

    diff=lst[j]-lst[i]
    if(diff==1):
        i+=1
    else:
        print(lst[i]+1,"is missing")
        break







# max_num=max(lst)

# total=max_num*(max_num+1)/2

# cur_sum=sum(lst)

# diff=total-cur_sum

# if(diff==0):
#     print(max_num+1,"is missing")
# else:
#     print(diff,"is missing")