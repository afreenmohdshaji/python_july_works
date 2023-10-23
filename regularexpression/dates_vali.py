from re import*
f=open("C:\\Users\\afisr\\Desktop\\july_pythonworks\\regularexpression\\dates.txt")
pattern="(20)([01][0-9]|2[0-3])[-]+(0[1-9]|1[0-2])(-)+(0[1-9]|1[0-9]|2[0-9]|3[01])"
for line in f:
    dates=line.rstrip("\n")
    matcher=fullmatch(pattern,dates)
    if matcher != None:
        print(dates)
      

