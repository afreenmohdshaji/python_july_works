f_news=open("C:\\Users\\afisr\\Desktop\\july_pythonworks\\fileoperation\\latestnews.txt")

f_stop=open("C:\\Users\\afisr\\Desktop\\july_pythonworks\\fileoperation\\stopwords.txt")

newswords=set()

stop_words={l.rstrip("\n") for l in f_stop}
# print(stop_words)

for l in f_news:
    words=l.split()
    for w in words:
        newswords.add(w)
print(newswords.difference(stop_words))