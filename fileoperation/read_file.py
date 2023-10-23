f=open("C:\\Users\\afisr\\Desktop\\july_pythonworks\\fileoperation\\data.txt","r")

words=[l.rstrip("\n") for l in f]
print(words)
f.close()