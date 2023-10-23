words=open("C:\\Users\\afisr\\Desktop\\july_pythonworks\\fileoperation\\news.txt",encoding="utf-8")
wc={}
for l in words:
    word=l.rstrip("\n").split(" ")
    print(word)
    for w in word:
        if w not in wc:
            wc[w]=1
        else:
            wc[w]+=1

print(wc)

