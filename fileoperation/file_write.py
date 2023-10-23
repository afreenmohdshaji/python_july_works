word=open("C:\\Users\\afisr\\Desktop\\july_pythonworks\\fileoperation\\leap_years.txt","w")

# lst=["hello","hai","good morning","hello world"]

# for w in lst:
#     word.write(w+"\n")

for y in range(1800,2025):
    if y%100==0 and y%400==0:
        word.write(str(y)+"\n")
    elif y%100!=0 and y%4==0:
        word.write(str(y)+"\n")

word.close()
