lst=[1,2,4,5,6,8,9,3,7]

count=0
p_count=0
v_count=0

for i in range(1,len(lst)-1):
    x=lst[i-1]
    y=lst[i]
    z=lst[i+1]

    if x<y>z:
        p_count+=1
        count+=1
    elif x>y<z:
        v_count+=1
        count+=1

print(f"total numbers of peak and valley are {count}")
print(f"total numbers of peaks={p_count} and total number of valleys={v_count}")

