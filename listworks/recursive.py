text="ABCADFDCE"

lst=[]

for ch in text:
    char_count=lst.count(ch)
    if char_count==0:
        lst.append(ch)
    else:
        print(f"{ch} recursive is found")
        break