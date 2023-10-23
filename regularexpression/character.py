from re import*

text="abcabdcAdacabc l@98h ASDFRZH"

# pattern="[a-z]"
# pattern="[A-Z]"
# pattern="@"
# pattern="[a-zA-Z0-9]"
# pattern="[^a-z]"
pattern="\d"
# pattern="\D"
# pattern="\W"
matcher=finditer(pattern,text)
for m in matcher:
    print(m.start(),m.group())