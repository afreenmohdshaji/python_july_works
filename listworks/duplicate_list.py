lst1=[10,20,23,43,54,60,15]
lst2=[34,54,20,25,15,10,22]

lst1.sort()
lst2.sort()

p1,p2=0,0
while(p1<len(lst1)and p2<len(lst2)):
    if lst1[p1]==lst2[p2]:
        print("common",lst1[p1])
        p1+=1
        p2+=1
    elif lst1[p1]<lst2[p2]:
        p1+=1
    else:
        p2+=1
