text="ABCCDFAD"

lst=[]

dp_lst=[]

for ch in text:
    char_count=lst.count(ch)
    if char_count==0:
        lst.append(ch)
    else:
        dp_lst.append(ch)

print(lst)
print(dp_lst[2])