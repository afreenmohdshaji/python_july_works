f_read=open("C:\\Users\\afisr\\Desktop\\july_pythonworks\\fileoperation\\years.py")

f_write=open("C:\\Users\\afisr\\Desktop\\july_pythonworks\\fileoperation\\leap_years.py","w")

for l in f_read:
    year=int(l.rstrip("\n"))
    if year%100==0 and year%400==0:
        f_write.write(str(year)+"\n")
    elif year%100!=0 and year%4==0:
        f_write.write(str(year)+"\n")

f_write.close()
f_read.close()