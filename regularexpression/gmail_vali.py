from re import*

f=open("C:\\Users\\afisr\\Desktop\\july_pythonworks\\regularexpression\\data.txt",encoding="utf-8")

patterm="[a-zA-Z0-9]+@[a-z]{2,}.com"

for l in f:
    mail=l.rstrip("\n")
    mathcher=fullmatch(patterm,mail)
    if mathcher!= None:
        print(mail)

# print(mail)
# print(f)
f.close()