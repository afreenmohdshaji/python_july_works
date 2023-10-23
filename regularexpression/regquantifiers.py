from re import*
text="abcaabcdbaacabcaaaa"
# pattern="a+"
# pattern="a*"
# pattern="a?"
pattern="a{2}"
# pattern="a{2,3}"
matcher=finditer(pattern,text)
for m in matcher:
    print(m.start(),m.group())



