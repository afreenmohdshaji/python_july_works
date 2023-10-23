# linear searching
lst=[10,20,30,40,50,60]

element=int(input("enter a element"))

is_present=False
for i in range(0,len(lst)):
    if lst[i]==element:
        is_present=True
        break

print(is_present)