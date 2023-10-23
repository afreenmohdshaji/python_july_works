from re import*

text="ababcdabacd"

pattern="ba"

match=finditer(pattern,text)
count=0
for m in match:
    print(m.start())
    print(m.group())
    count+=1
print(count)


