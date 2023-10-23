f_read=open("C:\\Users\\afisr\\Desktop\\july_pythonworks\\fileoperation\\vehiclenumbers.txt")

f_write=open("C:\\Users\\afisr\\Desktop\\july_pythonworks\\fileoperation\\keralanumbers.txt","w")

for l in f_read:
    reg=l.rstrip("\n")

    if reg.startswith("kl"):
        f_write.write(reg+"\n")